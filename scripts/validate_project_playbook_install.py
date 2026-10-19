#!/usr/bin/env python3
"""Validate source playbooks against the installed skill copies."""

from __future__ import annotations

import argparse
import filecmp
import json
import os
import sys
from pathlib import Path


PREFLIGHT_MARKERS = (
    "## Project Memory Preflight",
    "`project-memory-playbook`",
    "`$HOME/Codex/project-memory`",
    "`memory/preferences.md`",
    "`memory/habits.md`",
    "`memory/development.md`",
    "`memory/decisions.md`",
    "`projects/*`",
    "`memory/design-style.md`",
    "习惯校准",
    "写回记忆库",
    "提交并推送",
)


def parse_args() -> argparse.Namespace:
    default_repo_root = Path(__file__).resolve().parents[1]
    default_installed_root = Path(
        os.environ.get("CODEX_SKILLS_HOME", Path.home() / ".codex" / "skills")
    )

    parser = argparse.ArgumentParser(
        description=(
            "Check that every project-facing playbook is identical between "
            "the source repository and the installed skills directory."
        )
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=default_repo_root,
        help="Source repository root. Defaults to the parent of this script.",
    )
    parser.add_argument(
        "--installed-root",
        type=Path,
        default=default_installed_root,
        help="Installed skills root. Defaults to CODEX_SKILLS_HOME or ~/.codex/skills.",
    )
    return parser.parse_args()


def load_project_facing_playbooks(repo_root: Path) -> list[str]:
    index_path = repo_root / "skills-index.json"
    with index_path.open(encoding="utf-8") as index_file:
        catalog = json.load(index_file)

    playbooks: list[str] = []
    for skill in catalog.get("skills", []):
        slug = skill.get("slug")
        if not isinstance(slug, str):
            continue
        if slug.endswith("-playbook") and slug != "project-memory-playbook":
            playbooks.append(slug)

    return playbooks


def iter_files(root: Path) -> set[Path]:
    return {path.relative_to(root) for path in root.rglob("*") if path.is_file()}


def compare_directories(source: Path, installed: Path) -> list[str]:
    failures: list[str] = []
    if not source.is_dir():
        return [f"missing source directory: {source}"]
    if not installed.is_dir():
        return [f"missing installed directory: {installed}"]

    source_files = iter_files(source)
    installed_files = iter_files(installed)

    for extra in sorted(source_files - installed_files):
        failures.append(f"missing installed file: {installed / extra}")
    for extra in sorted(installed_files - source_files):
        failures.append(f"unexpected installed file: {installed / extra}")
    for relative_path in sorted(source_files & installed_files):
        source_file = source / relative_path
        installed_file = installed / relative_path
        if not filecmp.cmp(source_file, installed_file, shallow=False):
            failures.append(f"content differs: {source_file} != {installed_file}")

    return failures


def validate_preflight(skill_path: Path) -> list[str]:
    failures: list[str] = []
    if not skill_path.is_file():
        return [f"missing skill file: {skill_path}"]

    skill_text = skill_path.read_text(encoding="utf-8")

    for marker in PREFLIGHT_MARKERS:
        if marker not in skill_text:
            failures.append(f"missing preflight marker {marker!r}: {skill_path}")

    heading_pos = skill_text.find("## Project Memory Preflight")
    overview_pos = skill_text.find("## Overview")
    if heading_pos == -1:
        return failures
    if overview_pos != -1 and heading_pos > overview_pos:
        failures.append(f"preflight appears after overview: {skill_path}")

    lines = skill_text.splitlines()
    h1_index = next((index for index, line in enumerate(lines) if line.startswith("# ")), -1)
    preflight_index = next(
        (
            index
            for index, line in enumerate(lines)
            if line.strip() == "## Project Memory Preflight"
        ),
        -1,
    )
    first_h2_after_h1 = next(
        (
            index
            for index, line in enumerate(lines)
            if h1_index != -1 and index > h1_index and line.startswith("## ")
        ),
        -1,
    )
    if first_h2_after_h1 != preflight_index:
        failures.append(f"preflight is not the first section after title: {skill_path}")

    return failures


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.expanduser().resolve()
    installed_root = args.installed_root.expanduser().resolve()
    playbooks = load_project_facing_playbooks(repo_root)

    if not playbooks:
        print("No project-facing playbooks found in skills-index.json.", file=sys.stderr)
        return 1

    failures: list[str] = []
    for slug in playbooks:
        source = repo_root / slug
        installed = installed_root / slug
        failures.extend(compare_directories(source, installed))
        failures.extend(validate_preflight(source / "SKILL.md"))

    standards_root = repo_root / "project-standards-playbook"
    for relative in ("references/standards.md", "references/platform-profiles.md",
                     "references/project-start-template.md", "references/evidence.md"):
        if not (standards_root / relative).is_file():
            failures.append(f"missing standards reference: {standards_root / relative}")
    for slug in playbooks:
        if slug == "project-standards-playbook":
            continue
        skill_path = repo_root / slug / "SKILL.md"
        if skill_path.is_file() and "`project-standards-playbook`" not in skill_path.read_text(encoding="utf-8"):
            failures.append(f"missing shared standards route: {skill_path}")

    if failures:
        print("Project-facing playbook install validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(playbooks)} project-facing playbooks against {installed_root}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

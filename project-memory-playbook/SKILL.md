---
name: project-memory-playbook
description: Read, apply, calibrate, and update NAN's private project-memory repository before and during project work. Use when starting, continuing, planning, designing, reviewing, debugging, or implementing any software/product project; when user habits or preferences seem under-specified; when choosing visual or engineering style; when the user expresses likes, dislikes, "remember this", "以后都这样", "别再这样", "不怎么了解我的习惯", or other durable preferences; and when project-specific conventions or reusable decisions should be captured.
---

# Project Memory Playbook

## Overview

Use NAN's private `it-nanyuan/project-memory` repository as durable cross-project memory.
Before project work, sync and read the memory so decisions match known preferences and known gaps.
During work, capture only durable preferences, habits, conventions, and decisions that should affect future projects.

## Enforcement In Other Playbooks

Other project-facing playbooks should keep a concise `Project Memory Preflight` section near the top of `SKILL.md`.
That preflight should require this skill before real project work, and should route sparse habits or unclear taste back to habit calibration instead of guessing.

## Repository

- Remote: `https://github.com/it-nanyuan/project-memory`
- Default local path: `$HOME/Codex/project-memory`
- Visibility: private

## Start-Of-Work Workflow

For any development, debugging, design, review, or planning task:

1. Ensure the memory repository exists locally.

```bash
test -d "$HOME/Codex/project-memory/.git" || gh repo clone it-nanyuan/project-memory "$HOME/Codex/project-memory"
```

2. Sync the latest memory before making project decisions.

```bash
git -C "$HOME/Codex/project-memory" pull --ff-only
```

If network or GitHub auth is unavailable, read the local checkout and mention that memory may be stale.

3. Read the memory files relevant to the task:

- Always read `README.md`, `memory/preferences.md`, `memory/habits.md`, `memory/development.md`, and `memory/decisions.md`.
- Read `memory/design-style.md` for frontend, product, UX, UI, visual, brand, website, app, game, slide, image, or design tasks.
- Read a project-specific note from `projects/` when it exists. Prefer a file named after the GitHub repo, such as `owner-repo.md`; otherwise use the current folder or product name.

4. Apply the memory quietly in the work. Mention only the memory that materially affects the current decision.

## Habit Calibration

Read [references/habit-calibration.md](references/habit-calibration.md) when:

- `memory/habits.md` is missing, sparse, or mostly marked as needing calibration.
- The user says the agent does not understand their habits, taste, or working style.
- A new project has no project-specific memory and the task involves style, structure, workflow, or product direction.
- Repeated corrections suggest a durable preference that has not been recorded.

When calibration is needed, do not pretend the memory is complete. State the known gaps briefly if relevant, ask at most 1 to 3 targeted questions only when the answer changes the immediate work, and update memory with confirmed habits or clearly labeled signals.

## Updating Memory

Update the repository when the conversation or project work reveals durable reusable context:

- Explicit user preferences, likes, dislikes, or corrections.
- Habit signals about communication, autonomy, review depth, naming, delivery flow, or taste.
- Repeated style or engineering choices that should carry across future projects.
- Project conventions, architecture choices, product decisions, or things to avoid.
- Final decisions after a meaningful tradeoff.

Do not record:

- API keys, tokens, credentials, recovery information, or secrets.
- Sensitive personal details unless the user explicitly asks to store them.
- Temporary debugging output, one-off experiments, or low-confidence guesses.
- Large transcripts or noisy logs.

## Where To Write

- Stable cross-project preferences: `memory/preferences.md`
- Working habits and calibration gaps: `memory/habits.md`
- Visual/product/interface taste: `memory/design-style.md`
- Engineering workflow and tooling preferences: `memory/development.md`
- Dated durable decisions: `memory/decisions.md`
- Project-specific context: `projects/<project>.md`

Keep entries concise, dated when useful, and easy to scan. Update existing sections instead of duplicating the same memory.

## Commit And Push Cadence

Do not push every small note immediately. Accumulate confirmed durable memory during the active task, then close the loop before finishing.

- If a task changes memory, finish that task with the memory repository committed, pushed, and clean.
- Keep memory commits separate from unrelated project code commits.
- For long-running work, create a memory checkpoint after a meaningful milestone, before switching projects, or before any handoff that could lose context.
- Do not create a memory commit when no durable memory changed.
- If network or GitHub auth prevents a push, keep the local changes intact and clearly report that GitHub does not have the latest memory.
- If there are existing uncommitted memory changes from the user, preserve them and work with them. Do not overwrite or revert user-authored memory.

Recommended sequence when memory changed:

```bash
git -C "$HOME/Codex/project-memory" status --short
git -C "$HOME/Codex/project-memory" add README.md memory projects
git -C "$HOME/Codex/project-memory" commit -m "Update project memory"
git -C "$HOME/Codex/project-memory" push
git -C "$HOME/Codex/project-memory" status --short
```

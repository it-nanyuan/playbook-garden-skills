---
name: project-memory-playbook
description: Read and update NAN's private project-memory repository before and during project work. Use when starting, continuing, planning, designing, reviewing, debugging, or implementing any software/product project; when choosing visual or engineering style; when the user expresses likes, dislikes, "remember this", "以后都这样", "别再这样", or other durable preferences; and when project-specific conventions or reusable decisions should be captured.
---

# Project Memory Playbook

## Overview

Use NAN's private `it-nanyuan/project-memory` repository as durable cross-project memory.
Before project work, sync and read the memory so decisions match known preferences.
During work, capture only durable preferences, conventions, and decisions that should affect future projects.

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

- Always read `README.md`, `memory/preferences.md`, `memory/development.md`, and `memory/decisions.md`.
- Read `memory/design-style.md` for frontend, product, UX, UI, visual, brand, website, app, game, slide, image, or design tasks.
- Read a project-specific note from `projects/` when it exists. Prefer a file named after the GitHub repo, such as `owner-repo.md`; otherwise use the current folder or product name.

4. Apply the memory quietly in the work. Mention only the memory that materially affects the current decision.

## Updating Memory

Update the repository when the conversation or project work reveals durable reusable context:

- Explicit user preferences, likes, dislikes, or corrections.
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
- Visual/product/interface taste: `memory/design-style.md`
- Engineering workflow and tooling preferences: `memory/development.md`
- Dated durable decisions: `memory/decisions.md`
- Project-specific context: `projects/<project>.md`

Keep entries concise, dated when useful, and easy to scan. Update existing sections instead of duplicating the same memory.

## Commit And Push

When memory is changed, keep the memory commit separate from unrelated project code:

```bash
git -C "$HOME/Codex/project-memory" status --short
git -C "$HOME/Codex/project-memory" add README.md memory projects
git -C "$HOME/Codex/project-memory" commit -m "Update project memory"
git -C "$HOME/Codex/project-memory" push
```

If there are existing uncommitted memory changes from the user, preserve them and work with them. Do not overwrite or revert user-authored memory.

# Project Memory Playbook

Apply these rules before project planning, design, implementation, debugging, or review work.

## Workflow

- Sync and read `it-nanyuan/project-memory` before making project decisions.
- Use the memory files to honor durable user preferences, style likes/dislikes, engineering conventions, and project-specific notes.
- Use `memory/habits.md` to understand working style and known calibration gaps.
- Capture new memory only when it is durable and reusable.
- Keep memory commits separate from unrelated project code.

## Memory Sources

- `README.md`
- `memory/preferences.md`
- `memory/habits.md`
- `memory/development.md`
- `memory/decisions.md`
- `memory/design-style.md` for design and product-facing work
- `projects/<project>.md` for project-specific context

## Guardrails

- Never store secrets, credentials, tokens, or recovery information.
- Avoid noisy logs, temporary experiments, and one-off notes.
- Prefer updating an existing memory section over duplicating entries.
- When habits are sparse or the user says preferences are not understood, follow `references/habit-calibration.md`.

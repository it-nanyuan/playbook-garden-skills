# Project Memory Playbook

Use this instruction set before starting, continuing, planning, designing, reviewing, debugging, or implementing project work.

## Core Behavior

- Sync and read the private `it-nanyuan/project-memory` repository before making project decisions.
- Apply recorded user preferences, design style notes, development conventions, and project-specific memory.
- Check `memory/habits.md` and calibrate when user habits or taste are sparse.
- Update memory only when the user states a durable preference, repeats a correction, or the work reveals a reusable project convention.
- Keep memory updates concise and separate from unrelated project code changes.

## Read Order

1. `README.md`
2. `memory/preferences.md`
3. `memory/habits.md`
4. `memory/development.md`
5. `memory/decisions.md`
6. `memory/design-style.md` for UI, UX, product, visual, website, app, game, slide, or image work
7. `projects/<project>.md` when a matching project note exists

## Calibration

- If habits are sparse or the user says the agent does not understand them, read `references/habit-calibration.md`.
- Do not pretend preferences are known when they are not recorded.
- Ask at most 1 to 3 targeted questions only when the answer changes the current work.

## Safety Rules

- Do not store API keys, tokens, credentials, recovery details, or secrets.
- Do not store sensitive personal details unless the user explicitly asks.
- Do not turn temporary logs, scratch experiments, or low-confidence guesses into memory.
- If the memory repository cannot be synced, use the local checkout and mention that memory may be stale.

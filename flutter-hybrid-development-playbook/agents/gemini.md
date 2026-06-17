# Flutter Hybrid Development Playbook for Gemini

Use these instructions when building Flutter or hybrid app features.

## Workflow

1. Confirm whether the project is pure Flutter, hybrid, or monorepo-based.
2. Split work across packages, widgets, state, repositories, and bridge layers.
3. Reuse shared modules before duplicating code.
4. If the task includes page design, also follow the repository's admin UI quality standards.

## Rules

- Keep one main type per file.
- Favor reusable packages and `melos`-style workspace discipline.
- Comment shared APIs, bridge contracts, and complex state.

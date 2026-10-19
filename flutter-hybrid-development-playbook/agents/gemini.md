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
- Isolate vendor/network types behind project-owned interfaces; consume versioned shared packages and verify interactive states in the running app.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

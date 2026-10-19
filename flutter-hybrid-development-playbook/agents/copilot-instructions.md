# Flutter Hybrid Development Playbook for GitHub Copilot

Apply these rules when planning or implementing Flutter work.

## Workflow

- Confirm whether the project is pure Flutter, hybrid, or a multi-package monorepo.
- Maintain clear package boundaries, reuse, and shared module ownership.
- Comment shared packages, bridge logic, and complex state.
- When the task includes UI design, also align with the repository's admin UI design baseline.

## Engineering Standard

- One primary type per file.
- Split pages, widgets, state, services, repositories, and packages clearly.
- Use `melos`-style thinking for medium and large codebases.
- Put external clients behind app-owned interfaces, consume versioned shared packages, and keep business state outside shared UI primitives.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

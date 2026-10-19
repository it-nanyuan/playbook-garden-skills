# Frontend Development Playbook for Gemini

Use these instructions when generating frontend application code.

## Workflow

1. Clarify product type, stack, and UI constraints.
2. Split the work into pages, components, hooks, services, and shared logic.
3. Reuse containers and components instead of copying implementations.
4. If the task includes page design, follow the repository's admin UI design baseline.

## Rules

- Comment complex interactions and business states.
- Preserve maintainable frontend structure.
- Avoid generic page output that ignores professional UI quality.
- Consume versioned shared UI packages for presentation while keeping business API, routes, stores, and permissions in the app; do not hide real API errors with fixtures.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

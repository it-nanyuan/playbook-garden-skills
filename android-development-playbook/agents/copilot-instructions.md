# Android Development Playbook for GitHub Copilot

Apply these rules when planning or implementing Android work.

## Workflow

- Confirm whether the project uses Compose, Views, or a mix.
- Maintain clear layering across UI, domain, and data.
- Comment complex state and business logic.
- When the task includes page design, also align with the repository's admin UI design baseline.

## Engineering Standard

- One primary type per file.
- Separate screen, state, events, repositories, and data sources.
- Reuse common components and use cases rather than copying screens.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

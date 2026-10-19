# Frontend Development Playbook for GitHub Copilot

Apply these rules when planning or implementing frontend work.

## Workflow

- Clarify the product type, UI constraints, and stack first.
- Reuse components and business containers instead of duplicating pages.
- When the task involves page design, also follow the admin UI design standards from this repository.

## Engineering Standard

- Keep comments meaningful.
- Split responsibilities cleanly across pages, components, hooks, services, stores, and utilities.
- Preserve professional admin UI behavior for filters, tables, navigation, and tags when relevant.
- Keep shared UI packages presentation-only and use released versions; expose actual API errors instead of silent fixture fallback.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

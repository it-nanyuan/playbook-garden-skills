# Frontend Development Playbook for Claude

Use this instruction set when building frontend pages, admin systems, dashboards, or business web interfaces.

## Core Behavior

- Clarify product type and UI constraints before implementing.
- Follow the engineering rules in the skill and the admin UI quality baseline when pages are involved.
- Keep comments, structure, reuse, and component boundaries clear.

## Rules

- Split pages, components, hooks, services, stores, and utilities by responsibility.
- Avoid oversized single-file pages and repeated business containers.
- For admin-style pages, preserve layout order, table behavior, and filter structure.
- Comment complex interactions, state logic, permissions, and data mapping.
- Shared UI libraries own presentation primitives; each app owns API, routes, stores, permissions, and domain models. Show real API failures unless a demo mode is explicitly selected.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

# Flutter Hybrid Development Playbook for Claude

Use this instruction set when implementing Flutter features, hybrid app screens, or monorepo package work.

## Core Behavior

- Split functionality into reusable widgets, packages, and shared modules.
- Keep bridge boundaries, state, services, and package ownership clear.
- Comment shared packages, bridge contracts, async behavior, and business state clearly.
- If the task includes UI design, also follow the repository's admin UI quality standards.

## Rules

- Keep one primary type per file.
- Prefer `melos`-friendly package boundaries for medium and large projects.
- Reuse design system, shared UI, and core packages before duplicating code.
- Keep HTTP and vendor SDK types inside adapters; features depend on project-owned interfaces and domain models. Use versioned shared packages and verify live interactions.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

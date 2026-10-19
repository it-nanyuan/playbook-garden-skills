# Android Development Playbook for Claude

Use this instruction set when implementing Android features with Kotlin, Compose, or View-based projects.

## Core Behavior

- Keep UI, domain, and data responsibilities separated.
- Reuse components, use cases, repositories, and shared logic before duplicating code.
- Comment business state, async behavior, public APIs, and reusable modules clearly.
- If the task includes screen design, also follow the repository's admin UI design standards where relevant.

## Rules

- One primary type per file.
- Keep Compose screens, state, events, repositories, and data sources cleanly separated.
- Prefer modular growth over monolithic screen files.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

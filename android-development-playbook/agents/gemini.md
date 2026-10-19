# Android Development Playbook for Gemini

Use these instructions when building Android features.

## Workflow

1. Confirm the UI stack: Compose, Views, or mixed.
2. Split the work across UI, domain, and data responsibilities.
3. Reuse shared pieces before duplicating code.
4. If the task includes screen design, also follow the repository's admin UI quality standards.

## Rules

- Keep one main type per file.
- Separate screens, state, events, repositories, and data sources.
- Comment business-critical states and reusable APIs.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

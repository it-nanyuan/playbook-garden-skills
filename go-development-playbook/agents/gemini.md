# Go Development Playbook for Gemini

Use these instructions when building Go services.

## Rules

- Organize by clear package boundaries.
- Keep business logic out of handlers.
- Handle errors explicitly and preserve context.
- Comment exported APIs and complex logic.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

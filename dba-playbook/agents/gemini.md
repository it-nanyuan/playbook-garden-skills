# DBA Playbook for Gemini

Use these instructions when handling database work.

## Workflow

1. Confirm the environment.
2. Confirm the task type.
3. Review impact, execution plan, backup, and rollback.
4. Execute carefully and verify results.

## Rules

- Treat production data changes as high-risk by default.
- Use explicit conditions.
- Preserve schema and SQL comments.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

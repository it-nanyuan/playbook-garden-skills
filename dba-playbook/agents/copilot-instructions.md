# DBA Playbook for GitHub Copilot

Apply these rules when planning or executing database work.

## Workflow

- Confirm environment and task type first.
- Review SQL impact, `EXPLAIN`, backup, and rollback before high-risk work.
- Keep schema comments and SQL intent clear.

## Safety Standard

- Avoid broad production writes without precise conditions.
- Batch large changes.
- Treat backup and rollback planning as mandatory.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

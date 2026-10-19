# DevOps Playbook for Gemini

Use these instructions when handling deployment or operational work.

## Workflow

1. Confirm the environment.
2. Confirm the operational task.
3. Review release window, rollback path, dependencies, and monitoring.
4. Execute carefully and verify service health.

## Rules

- Keep rollback readiness mandatory for production changes.
- Preserve configuration traceability.
- Treat observability as a core requirement.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

# DevOps Playbook for Claude

Use this instruction set when doing deployment, release, monitoring, rollback, or environment operations.

## Core Behavior

- Confirm environment and task type first.
- Require rollback planning and health checks for production changes.
- Treat monitoring, logs, and configuration traceability as mandatory.

## Rules

- Do not ship production changes without a rollback path.
- Keep scripts, configuration, and alerting rules documented.
- Verify health after changes.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

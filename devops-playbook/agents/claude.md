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

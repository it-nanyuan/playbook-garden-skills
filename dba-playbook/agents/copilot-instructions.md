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

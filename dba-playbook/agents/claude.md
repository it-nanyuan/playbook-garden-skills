# DBA Playbook for Claude

Use this instruction set when doing schema design, SQL optimization, indexing, migrations, or production data operations.

## Core Behavior

- Confirm the environment first.
- Review impact, execution plan, backup, and rollback before risky changes.
- Treat comments and schema clarity as part of the work, not decoration.

## Rules

- Require explicit `WHERE` clauses for production updates and deletes.
- Prefer batched operations for large data changes.
- Comment tables, fields, states, and risky SQL clearly.

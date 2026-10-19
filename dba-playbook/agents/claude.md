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

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

# Comment Style Playbook for Claude

Use this instruction set when defining or applying engineering comment rules.

## Core Behavior

- Comment to explain intent, constraints, and side effects.
- Avoid comments that simply restate obvious code.
- Prioritize public APIs, shared modules, async logic, state changes, and business rules.

## Rules

- Class comments explain responsibility and scope.
- Method comments explain input, output, side effects, async behavior, or transactions.
- Field comments explain business meaning, units, enum values, or constraints when needed.

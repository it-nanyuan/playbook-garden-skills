# Java Development Playbook for Claude

Use this instruction set when implementing Java backend work.

## Core Behavior

- Clarify whether the project is monolithic or microservices before designing the stack.
- Keep comments, layering, and component selection disciplined.
- Enforce `service` interfaces plus `service.impl` implementations.

## Rules

- Choose middleware based on business needs, not on completeness theater.
- Keep controller, service, manager, mapper, entity, DTO, VO, and convert responsibilities cleanly separated.
- Comment business rules, transactions, cache behavior, async consumers, and scheduled jobs clearly.

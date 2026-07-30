# Java Development Playbook for Claude

Use this instruction set when implementing Java backend work.

## Core Behavior

- Reuse an architecture decision already established in the conversation; ask about monolith versus microservices only when it remains unknown.
- For an ordinary monolith with unstable domain boundaries, prefer one application with layer-first packages instead of speculative business modules.
- Keep comments, layering, and component selection disciplined.
- Enforce `service` interfaces plus `service.impl` implementations.

## Rules

- Choose middleware based on business needs, not on completeness theater.
- Keep controller, service, manager, mapper, entity, DTO, VO, and convert responsibilities cleanly separated.
- Keep Request and View types out of controllers, and keep Mapper dependencies out of controllers.
- In a MyBatis-Plus project, use Mapper interfaces plus `mapper.xml` and remove JPA persistence paths.
- Use Lombok only for mechanical code; preserve constructors that initialize state or enforce rules.
- Keep URL-level security coarse, use `@PreAuthorize` for action roles, and preserve pre-validation denial for privileged writes.
- Comment business rules, transactions, cache behavior, async consumers, and scheduled jobs clearly.

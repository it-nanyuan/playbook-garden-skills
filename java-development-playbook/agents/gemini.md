# Java Development Playbook for Gemini

Use these instructions when building Java backend services.

## Workflow

1. Reuse an established architecture decision; ask whether the project is monolithic or microservices only when unknown.
2. Choose the appropriate framework and middleware accordingly.
3. For a normal monolith, prefer layer-first packages until stable domain or delivery boundaries justify modules.
4. Keep controller, service, manager, mapper, entity, DTO, and VO boundaries clear.
5. Keep Request and View types out of controllers, and keep Mapper dependencies out of controllers.
6. Use MyBatis-Plus with Mapper interfaces and `mapper.xml` without retaining JPA paths.
7. Use Lombok for mechanical code while preserving constructors with state initialization or validation.
8. Keep `SecurityFilterChain` coarse and action roles in `@PreAuthorize`; retain minimal early denial for privileged writes.
9. Comment business rules, transactions, cache behavior, MQ consumers, and scheduled jobs clearly.

## Rules

- `service` contains interfaces.
- `service.impl` contains implementations.
- Complex SQL belongs in `mapper.xml`.
- Keep supplier integrations behind capability contracts, redact sensitive diagnostics, and verify real provider calls separately from tests.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

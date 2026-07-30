# Java Development Playbook for GitHub Copilot

Apply these rules when planning or implementing Java backend work.

## Workflow

- Ask whether the project is monolithic or microservices only when the repository or conversation has not already established it.
- Then choose the appropriate framework, middleware, and structure.
- Keep comments, layering, and business boundaries clear.

## Engineering Standard

- `service` defines interfaces and `service.impl` contains implementations.
- Keep controllers limited to HTTP boundaries; place Request and View types in `dto` and `vo`.
- Prefer a layer-first single application for a monolith unless stable domain or build boundaries justify modules.
- Complex SQL belongs in `mapper.xml`.
- Do not mix JPA persistence paths into a project that selected MyBatis-Plus.
- Use Lombok annotations such as `@RequiredArgsConstructor`, `@Slf4j`, and safe Entity constructor annotations only for mechanical code.
- Keep `SecurityFilterChain` coarse and action roles in `@PreAuthorize`, with minimal early guards for privileged writes.
- Pick Redis, MQ, Elasticsearch, registry, gateway, tracing, and transaction tools only when the business actually needs them.

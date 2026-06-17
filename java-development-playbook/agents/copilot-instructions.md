# Java Development Playbook for GitHub Copilot

Apply these rules when planning or implementing Java backend work.

## Workflow

- Ask first whether the project is monolithic or microservices.
- Then choose the appropriate framework, middleware, and structure.
- Keep comments, layering, and business boundaries clear.

## Engineering Standard

- `service` defines interfaces and `service.impl` contains implementations.
- Complex SQL belongs in `mapper.xml`.
- Pick Redis, MQ, Elasticsearch, registry, gateway, tracing, and transaction tools only when the business actually needs them.

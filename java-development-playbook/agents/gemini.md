# Java Development Playbook for Gemini

Use these instructions when building Java backend services.

## Workflow

1. Ask first whether the project is monolithic or microservices.
2. Choose the appropriate framework and middleware accordingly.
3. Keep controller, service, manager, mapper, entity, DTO, and VO boundaries clear.
4. Comment business rules, transactions, cache behavior, MQ consumers, and scheduled jobs clearly.

## Rules

- `service` contains interfaces.
- `service.impl` contains implementations.
- Complex SQL belongs in `mapper.xml`.

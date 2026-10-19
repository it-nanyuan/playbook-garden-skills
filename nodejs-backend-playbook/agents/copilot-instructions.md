# Node.js Backend Playbook

Apply this playbook when working on Node.js or TypeScript backend services, APIs, BFF layers, workers, or business modules.

Start by clarifying:

1. Is the project based on NestJS, Express, Fastify, Koa, or an internal framework?
2. Is this an API/BFF service, worker, scheduled task, or script-like service?
3. Is TypeScript required? Which package manager and build system are in use?

Rules:

- Respect the existing runtime and module boundaries
- Keep controllers thin and business orchestration in services
- Keep data access, external clients, cache, and async jobs separated
- Handle timeout, retry, idempotency, and failure branches explicitly

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

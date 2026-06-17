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

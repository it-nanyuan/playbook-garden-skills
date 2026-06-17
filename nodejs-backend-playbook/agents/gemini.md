# Node.js Backend Playbook

Use this skill for Node.js and TypeScript backend services, APIs, BFF layers, workers, and scheduled jobs.

Before implementation, clarify:

1. Which framework is in use?
2. Is the target an API, BFF, worker, or scheduled task?
3. Is TypeScript mandatory, and what package/build setup exists?

Working rules:

- Prefer the existing runtime and module boundaries
- Keep route handlers thin and business logic in services
- Keep async tasks, cache, and external clients explicit and testable

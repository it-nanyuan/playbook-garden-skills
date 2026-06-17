# PHP Development Playbook

Use this skill for PHP backend services, APIs, admin systems, jobs, listeners, and callback workflows.

Before implementation, clarify:

1. Is the codebase using `Laravel`, `Symfony`, `Hyperf`, `ThinkPHP`, or a custom framework?
2. Are there existing project conventions for structure, responses, validation, and exceptions?
3. Which infrastructure pieces are involved: `MySQL`, `Redis`, queues, search, payments, storage, or webhooks?

Working rules:

- Prefer the existing framework conventions and project boundaries
- Keep controllers thin and business orchestration in services
- Centralize data access logic instead of scattering SQL
- Use comments to explain responsibility, side effects, and business meaning
- Keep cache, queue, testing, and security strategies explicit and consistent

Read next if needed:

- `../SKILL.md`
- `../references/framework-selection.md`
- `../references/security.md`
- `../references/cache-queue.md`

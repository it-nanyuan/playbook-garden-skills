# PHP Development Playbook

Apply this playbook when working on PHP backend services, APIs, admin systems, scheduled jobs, or business modules.

Start by clarifying:

1. Is the project based on `Laravel`, `Symfony`, `Hyperf`, `ThinkPHP`, or an existing custom framework?
2. Is this a new project or an existing codebase that already has conventions?
3. Which components are required: `MySQL`, `Redis`, queues, search, object storage, payments, webhook callbacks, or scheduled jobs?

Rules:

- Follow the existing framework and project conventions first
- Keep `Controller`, `Service`, `Repository`, `Model`, `DTO`, and `Job` responsibilities separate
- Do not put full business workflows into controllers
- Avoid scattering raw SQL strings through business code
- Write meaningful comments for responsibility, constraints, side effects, and business intent
- Keep response format, validation, exceptions, cache, queues, and security rules consistent

Read for details:

- `../SKILL.md`
- `../references/framework-selection.md`
- `../references/structure.md`
- `../references/testing.md`

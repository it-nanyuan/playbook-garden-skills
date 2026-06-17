# Ruby Development Playbook

Apply this playbook when working on Ruby services, Rails applications, APIs, background jobs, or business modules.

Start by clarifying:

1. Is the project based on Rails, Sinatra, Grape, Hanami, or an internal framework?
2. Is it a full business app, API-only service, background job system, or script-like service?
3. Are jobs handled by Sidekiq, ActiveJob, or another queue system?

Rules:

- Respect existing framework conventions and deployment model
- Keep controllers thin and business orchestration in services or use cases
- Avoid turning models into god objects
- Make retry, idempotency, and failure handling explicit for jobs

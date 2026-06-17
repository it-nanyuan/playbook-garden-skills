# C# Development Playbook

Use this skill for C# and .NET backend services, APIs, worker services, scheduled jobs, and shared business modules.

Before implementation, clarify:

1. Is the project a monolith, microservice, worker, or library?
2. Is it based on ASP.NET Core MVC, Minimal API, gRPC, or Worker Service?
3. Is data access using EF Core, Dapper, or a mixed strategy?

Working rules:

- Prefer the existing solution structure and common infrastructure
- Keep layers and module boundaries explicit
- Keep controllers thin and business orchestration in services or application layer
- Keep cache, messaging, testing, and security strategies consistent

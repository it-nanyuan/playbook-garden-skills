# C# Development Playbook

Apply this playbook when working on C# or .NET backend services, APIs, worker services, enterprise modules, or class libraries.

Start by clarifying:

1. Is the project a monolith, microservice, worker, or shared library?
2. Is it using ASP.NET Core MVC, Minimal API, gRPC, Worker Service, or an existing internal framework?
3. Is data access based on EF Core, Dapper, or a mixed approach?

Rules:

- Respect the existing solution layout and dependency injection conventions
- Keep `Api`, `Application`, `Domain`, and `Infrastructure` boundaries clear
- Do not place full business workflows in controllers or endpoints
- Keep logging, exceptions, response envelopes, cache, and messaging strategies consistent
- Use comments for responsibility, constraints, and side effects

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

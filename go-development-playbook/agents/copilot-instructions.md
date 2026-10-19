# Go Development Playbook for GitHub Copilot

Apply these rules when planning or implementing Go services.

## Rules

- Keep handler, service, repository, and client responsibilities separated.
- Do not hide errors.
- Comment exported functions and complex behavior.
- Preserve clear package structure and production-minded observability.

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

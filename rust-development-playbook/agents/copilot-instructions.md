# Rust Development Playbook

Apply this playbook when working on Rust services, async applications, CLIs, workers, libraries, or performance-sensitive modules.

Start by clarifying:

1. Is the project an API service, CLI, worker, system tool, or library?
2. Is it using axum, actix-web, tokio, clap, or an internal framework?
3. Is the project a single crate or a workspace?

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

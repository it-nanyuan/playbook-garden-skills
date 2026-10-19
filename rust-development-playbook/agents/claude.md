# Rust Development Playbook

在规划或实现 Rust API、异步服务、CLI、Worker 或通用库时使用本规范。

开始前先确认：

1. 当前项目是 API、CLI、Worker、系统工具还是库？
2. 使用 `axum`、`actix-web`、`tokio`、`clap`，还是已有内部封装？
3. 是单 crate 还是 workspace？是否涉及高性能或系统级约束？

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

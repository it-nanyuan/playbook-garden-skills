---
name: rust-development-playbook
description: Build maintainable Rust services, tools, and performance-sensitive modules with clear architecture and coding standards. Use when planning or implementing Rust APIs, async services, CLIs, libraries, workers, or system tools, and always clarify whether the project is an axum service, actix-web service, tokio async app, CLI, or reusable library before choosing module structure, async model, and common components such as PostgreSQL, Redis, MQ, or tracing.
---

# Rust Development Playbook

## Overview

这个 skill 用来为 Rust 项目建立稳定、可维护、偏生产导向的工程规范。它默认强调先判断项目形态、异步模型和 crate 边界，再决定模块组织、错误处理、性能取舍、测试和运行时约束。

## Workflow

1. 先确认项目类型：HTTP API、异步服务、CLI、系统工具、Worker 还是通用库。
2. 再确认使用 `axum`、`actix-web`、`warp`、`tokio`、`clap`，还是已有内部框架。
3. 再确认项目是单一 crate、workspace 多 crate，还是嵌入式 / 系统级工程。
4. 根据业务判断是否需要 `PostgreSQL`、`MySQL`、`Redis`、MQ、对象存储和 tracing 方案。
5. 已有项目优先跟随现有 crate 切分、错误类型和异步模型。
6. 编码时必须重视注释、所有权边界、错误建模、测试和性能意识。

## First Question

做 Rust 项目时，第一优先级问题是：

- 这是 API 服务、异步 Worker、CLI、库，还是系统级工具？

第二优先级问题是：

- 当前项目使用 `axum`、`actix-web`、`tokio`、`clap`，还是已有内部封装？是单 crate 还是 workspace？

如果用户没说明清楚，就先问；不要直接默认运行时和 crate 结构。

## Core Rules

- Handler 不承载完整业务流程
- Service / Use Case 负责业务编排，Repository / Adapter 负责数据和外部依赖
- 不把数据库访问、外部调用、缓存逻辑和业务规则堆在一个模块里
- 错误处理必须显式建模，不静默吞错
- 所有权、生命周期、并发边界要清晰，不为“先跑起来”牺牲可维护性
- 公共能力优先抽 crate 或 module，不复制粘贴

## Comments Standard

- public module、public type、public function 优先补职责注释
- 方法注释重点写输入、输出、副作用、错误语义和线程 / 异步约束
- 并发逻辑、unsafe、性能优化、状态流转、缓存更新和消息消费优先补齐注释

详细见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- `bin/`：可执行入口
- `lib.rs`：公共导出与模块组织
- `application` / `service`：业务编排
- `domain`：核心规则与模型
- `infrastructure` / `adapter`：数据库、缓存、消息、第三方集成
- `transport` / `http`：协议层
- `jobs` / `worker`：异步任务
- `shared`：公共能力

详细见 `references/structure.md`。

## API And Error Standard

- 返回结构、错误映射、分页对象和 trace 信息统一
- Handler 负责协议层，不承载完整业务实现
- 参数错误、业务错误、权限错误、系统错误清晰分层
- 错误类型、`Result` 语义和对外错误映射保持一致

详细见 `references/api-standard.md` 与 `references/error-handling.md`。

## Async And Performance Standard

- 明确 `tokio` 运行时、任务拆分、超时、取消和资源释放策略
- 对锁、共享状态、连接池、批处理和背压保持清醒
- 性能优化要有证据，避免过早优化和不必要的 `unsafe`

详细见 `references/async-performance.md`。

## Logging And Observability

- 使用统一 tracing 方案记录 requestId、traceId、关键主键、耗时和错误上下文
- 关键后台任务、消息消费和外部调用要可观测

详细见 `references/logging.md`。

## Cache And Messaging Standard

- Redis key、topic、consumer group、stream 命名统一
- 缓存、消息和数据库一致性策略明确
- 消费逻辑必须考虑幂等、重试、超时、死信和失败告警

详细见 `references/cache-messaging.md`。

## Testing Standard

- 核心业务、错误分支、边界条件、并发逻辑和异步任务要有测试
- 区分单元测试、集成测试、端到端验证和基准测试
- 性能敏感模块应具备最基本的 benchmark 意识

详细见 `references/testing.md`。

## Security Standard

- 参数校验、鉴权、敏感信息保护和外部输入边界必须统一
- 不在日志、错误信息或响应中泄露敏感信息
- 文件处理、回调处理、命令执行和系统接口调用重点考虑安全约束

详细见 `references/security.md`。

## Recommended Stack

- Web：`axum`、`actix-web`
- Async Runtime：`tokio`
- CLI：`clap`
- Serialization：`serde`
- Database：`sqlx`、`diesel`
- Cache：`redis`
- Error：`thiserror`、`anyhow`
- Tracing：`tracing`
- Testing：标准测试框架、`tokio::test`、`criterion`

详细见 `references/framework-selection.md`。

## When To Use

- 用户要开始一个 Rust API、异步服务、Worker、CLI 或库项目
- 用户要统一模块边界、错误建模、异步运行时、日志和测试规范
- 用户要在 `axum / actix-web / tokio / sqlx / tracing` 这类常见栈里建立工程标准
- 用户要做偏性能敏感、并发明显或系统工具类工程

## References

- `references/comments.md`
- `references/structure.md`
- `references/api-standard.md`
- `references/error-handling.md`
- `references/async-performance.md`
- `references/logging.md`
- `references/cache-messaging.md`
- `references/testing.md`
- `references/security.md`
- `references/framework-selection.md`

## Platform Adapters

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

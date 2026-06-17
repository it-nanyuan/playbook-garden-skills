---
name: go-development-playbook
description: Build maintainable Go services with clear engineering standards. Use when planning or implementing Go backend services, HTTP APIs, microservices, infrastructure-facing tools, or service modules that need strong structure, comments, package boundaries, observability, and production-oriented conventions.
---

# Go Development Playbook

## Overview

这个 skill 用来为 Go 服务建立稳定、可维护、偏生产导向的工程规范。它默认强调 package 边界、接口与实现职责、清晰注释、错误处理、日志、测试和可观测性，而不是把全部逻辑塞进 handler 或一个巨大的 service 文件里。

## Workflow

1. 先判断项目类型：HTTP API、内部服务、微服务、CLI、任务调度器或基础设施工具。
2. 再确认已有项目在用什么 HTTP 框架、ORM、日志和配置方案，不要默认切换。
3. 如果是已有项目，优先跟随现有目录结构、依赖选择和包边界。
4. 新增需求前先判断属于 handler、service、repository、client、job、config 还是 shared package。
5. 优先用小 package 和清晰边界组织代码，不让单个包无限膨胀。
6. 编码时重视注释、错误处理、上下文传递、日志和测试。

## First Question

做 Go 项目时，第一优先级问题是：

- 这是 HTTP API、微服务、Worker、CLI 工具，还是基础设施型工具？

第二优先级问题是：

- 当前项目使用 `gin`、`echo`、`chi` 还是标准库？数据库层是 `gorm`、`sqlx`、`ent`，还是标准库封装？

判断规则：

- HTTP API：优先明确路由、中间件、鉴权、返回体和可观测性要求
- 微服务：优先明确服务边界、配置中心、注册发现、MQ、熔断和链路追踪
- Worker / Job：优先明确重试、幂等、任务拆分和失败补偿
- CLI / Infra Tool：优先明确输入输出、执行环境、配置注入和日志级别

如果用户没说明清楚，就先问；不要一边写代码一边默认工程形态和框架。

## Core Rules

- 包职责清晰，不把 handler、业务逻辑、数据库访问和第三方调用揉在一起
- 一个文件可以包含多个相关函数，但不能无限堆逻辑；优先按职责拆分
- 公共能力优先抽 shared package，不复制粘贴
- 依赖通过接口边界控制，不直接到处 new 实现
- 错误处理必须显式，不静默吞错
- 日志、超时、context 传递和配置管理要统一

## Comments Standard

- package 注释说明职责和用途
- exported type 和 exported function 优先补齐注释
- 复杂业务函数、并发逻辑、重试逻辑、状态转换和副作用要写意图说明
- 字段注释只在业务语义、单位、状态值或约束不明显时写

详细注释规范见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- `cmd/`：入口
- `internal/`：内部业务实现
- `pkg/`：可复用公共能力，仅在确实需要对外复用时使用
- `api/`：协议、IDL、文档或 OpenAPI
- `configs/`：配置模板
- `scripts/`：脚本

常见拆分：

- `handler`
- `service`
- `repository`
- `model`
- `client`
- `config`
- `job`

详细见 `references/structure.md`。

## API And Error Standard

- 返回结构、错误码、分页对象、trace 信息要统一
- HTTP handler 负责协议层，不负责承载完整业务逻辑
- 业务错误、参数错误、权限错误、系统错误分层清晰

详细见 `references/api-standard.md` 与 `references/error-handling.md`。

## Logging And Observability

- 日志要带关键上下文，不打无意义噪音
- traceId、requestId、耗时、关键主键和异常原因要可检索
- context 传递要贯穿请求、数据库和下游调用

详细见 `references/logging.md`。

## Cache And Messaging Standard

- Redis key、topic、consumer group、stream 或 subject 命名要统一
- 缓存、消息和数据库一致性策略要明确，不允许各模块各写各的
- 消费逻辑必须考虑幂等、重试、超时、失败告警和死信处理
- 事件驱动适合做解耦，但不要把核心同步链路隐式拆散到难以排查

详细见 `references/cache-messaging.md`。

## Testing Standard

- 核心业务、错误分支、边界条件和并发相关逻辑要有测试
- 区分单元测试、集成测试和关键链路验证
- 不为覆盖率堆无价值测试，但关键流程不能裸奔

详细见 `references/testing.md`。

## Security Standard

- 参数校验、权限边界、敏感信息保护和外部调用超时控制要统一
- 不在日志或响应里泄露敏感信息
- 外部依赖调用要有超时、重试和熔断意识

详细见 `references/security.md`。

## Recommended Stack

- HTTP：`gin`、`echo` 或 `chi`，按项目现状选择
- Config：`viper`
- Database：`gorm`、`sqlx`、`ent` 或标准库
- Cache：`go-redis`
- MQ / Stream：`kafka-go`、`sarama`、`nats.go`
- Logging：`zap`、`zerolog`、`log/slog`
- Validation：`go-playground/validator`
- CLI / Tools：`cobra`
- Testing：标准库 `testing`，必要时配合 `testify`

详细见 `references/libraries.md`。

## Framework Guidance

- `gin`：常见于业务 API 和中后台服务，生态成熟，上手快
- `echo`：API 开发体验直接，项目少量抽象时也够用
- `chi`：更轻量，适合强调标准库风格和可控组合的项目
- 标准库：适合基础设施工具、轻量服务或已有较强公共基建的团队
- `gorm`：上手快，但要警惕复杂查询和隐式行为
- `sqlx`：更贴近 SQL，适合强调查询可控和性能感知的服务
- `ent`：适合对 schema、代码生成和类型安全要求更高的项目

详细见 `references/framework-selection.md`。

## When To Use

- 用户要开始一个 Go 后端或服务项目
- 用户要统一 Go 项目的包结构、注释、错误处理和测试规范
- 用户要为 API 服务、微服务或内部工具建立工程标准
- 用户要选择 Go 常用框架和基础库

## References

- `references/comments.md`
- `references/structure.md`
- `references/api-standard.md`
- `references/error-handling.md`
- `references/logging.md`
- `references/cache-messaging.md`
- `references/testing.md`
- `references/security.md`
- `references/libraries.md`
- `references/framework-selection.md`

## Platform Adapters

如果需要把这个 skill 接到不同平台：

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

优先查看：

- `references/platforms/README.md`
- `references/platforms/openai.md`
- `references/platforms/claude.md`
- `references/platforms/cursor.md`
- `references/platforms/gemini.md`
- `references/platforms/copilot.md`

---
name: csharp-development-playbook
description: Build maintainable C# and .NET services with clear architecture and coding standards. Use when planning or implementing ASP.NET Core APIs, enterprise backends, worker services, scheduled jobs, or business modules, and always clarify whether the project is a monolith, microservice, background worker, or library before choosing structure, middleware, and common components such as SQL Server, MySQL, Redis, MQ, or search.
---

# C# Development Playbook

## Overview

这个 skill 用来为 C# 与 .NET 项目建立稳定、可维护、偏生产导向的工程规范。它默认强调先判断项目形态和框架组合，再决定分层、模块边界、中间件与基础组件，同时把注释、测试、异常、日志和长期维护成本放在与功能实现同等重要的位置。

## Workflow

1. 先确认项目类型：ASP.NET Core API、单体业务系统、微服务、Worker Service、定时任务还是类库。
2. 再确认当前项目使用的是 `ASP.NET Core`、`Minimal API`、`MVC`、`gRPC`、`Worker Service` 还是已有企业框架。
3. 再根据业务判断是否需要 `SQL Server`、`MySQL`、`Redis`、`MQ`、`Elasticsearch`、对象存储、权限体系和任务调度。
4. 已有项目优先跟随现有解决方案结构、依赖注入方式、ORM 和公共中间件，不要随意换架构。
5. 新项目先定解决方案结构、分层和模块职责，再写 Controller、Application、Domain、Repository、DTO 和 Job。
6. 编码时必须重视注释、边界、异常处理、可测试性和复用。

## First Question

做 C# / .NET 项目时，第一优先级问题是：

- 这是单体、微服务、Worker、类库，还是已有企业系统扩展？

第二优先级问题是：

- 当前项目使用 `ASP.NET Core MVC`、`Minimal API`、`gRPC`，还是 `Worker Service`？数据访问是 `EF Core`、`Dapper` 还是混合方案？

判断规则：

- 单体：业务集中、模块多但部署统一
- 微服务：服务边界清晰、独立部署、需要治理与观测
- Worker：重点关注任务调度、重试、幂等和失败补偿
- 类库：重点关注 API 设计、兼容性和测试

如果用户没说明清楚，就先问；不要默认项目形态和技术路线。

## Core Rules

- Controller / Endpoint 不承载完整业务流程
- Application / Service 负责业务编排，Domain 负责核心规则
- Repository 或明确的数据访问层负责数据库访问，不在业务代码里散落 SQL
- 一个类一个主要职责，不把缓存、外部调用、业务编排和数据访问揉在一起
- 公共能力优先抽基础设施、公共模块或共享库，但不要把具体业务堆进 `Common`
- 依赖注入、配置、日志、异常和返回体要统一
- 复杂查询可以用 `Dapper` 或明确查询层，但不能让数据访问方式失控

## Comments Standard

- 类注释：说明职责、业务边界、适用场景
- 方法注释：说明输入、输出、副作用、异常、事务和缓存影响
- 属性注释：重点解释业务语义、单位、状态值和约束
- 对外接口、复杂服务、后台任务、消息消费、缓存更新和状态流转优先补齐注释

详细见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- `Api` / `Web`：协议层、鉴权门面、返回组装
- `Application`：业务编排、用例服务
- `Domain`：领域对象、规则、接口
- `Infrastructure`：数据库、缓存、消息、第三方集成
- `Contracts` / `DTOs`：跨层数据结构
- `BackgroundTasks` / `Workers`：异步任务与后台服务
- `Shared` / `Common`：通用能力，但不承载具体业务

详细见 `references/structure.md`。

## API And Error Standard

- 返回结构、错误码、分页对象、幂等约束、trace 信息要统一
- Controller / Endpoint 只负责协议层，不承载完整业务实现
- 参数错误、业务错误、权限错误、系统错误要清晰分层

详细见 `references/api-standard.md` 与 `references/error-handling.md`。

## Logging And Observability

- 日志必须带关键上下文，不打无意义噪音
- traceId、requestId、关键主键、耗时和异常原因要可检索
- 指标、健康检查、链路追踪和关键后台任务状态要可观测

详细见 `references/logging-observability.md`。

## Runtime And Deployment Standard

- API、Worker、定时任务和微服务要区分运行方式和发布约束
- 发布时明确配置来源、迁移脚本、缓存预热、后台任务重启和回滚策略
- 长驻 Worker 要关注内存增长、重试风暴和死信堆积

详细见 `references/runtime-deployment.md`。

## Cache And Messaging Standard

- Redis key、topic、queue、consumer group 命名要统一
- 缓存、消息和数据库一致性策略必须明确
- 消费逻辑必须考虑幂等、重试、超时、死信和失败告警

详细见 `references/cache-messaging.md`。

## Testing Standard

- 核心业务、异常分支、边界条件、后台任务和消息消费要有测试
- 区分单元测试、集成测试和关键链路验证
- 关键业务流程不能裸奔

详细见 `references/testing.md`。

## Security Standard

- 参数校验、认证鉴权、敏感信息保护、上传下载边界和后台权限必须统一
- 不在日志、异常或响应中泄露敏感数据
- 对外回调、Webhook、批量操作和高权限接口要重点考虑安全约束

详细见 `references/security.md`。

## Recommended Stack

- Framework：`ASP.NET Core MVC`、`Minimal API`、`gRPC`
- ORM / DB：`EF Core`、`Dapper`
- Database：`SQL Server`、`MySQL`、`PostgreSQL`
- Cache：`Redis`
- MQ：`RabbitMQ`、`Kafka`
- Validation：`FluentValidation`
- Docs：`Swagger / OpenAPI`
- Background Jobs：`Hangfire`、`Quartz.NET`
- Testing：`xUnit`、`NUnit`、`Moq`

详细见 `references/framework-selection.md`。

## When To Use

- 用户要开始一个 C# / .NET 后端项目
- 用户要统一 ASP.NET Core、Worker Service 或企业系统扩展规范
- 用户要规范分层、注释、日志、缓存、消息和测试策略
- 用户要在 `EF Core / Dapper / Redis / MQ` 这类常见栈里建立工程标准

## References

- `references/comments.md`
- `references/structure.md`
- `references/api-standard.md`
- `references/error-handling.md`
- `references/logging-observability.md`
- `references/runtime-deployment.md`
- `references/cache-messaging.md`
- `references/testing.md`
- `references/security.md`
- `references/framework-selection.md`

## Platform Adapters

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

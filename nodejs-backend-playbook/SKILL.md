---
name: nodejs-backend-playbook
description: Build maintainable Node.js and TypeScript backend services with clear architecture and coding standards. Use when planning or implementing Node.js APIs, BFF layers, microservices, workers, scheduled jobs, or business modules, and always clarify whether the project is NestJS, Express, Fastify, Koa, or an existing framework before choosing structure, runtime conventions, and common components such as PostgreSQL, MySQL, Redis, MQ, or search.
---

# Node.js Backend Playbook

## Overview

这个 skill 用来为 Node.js 与 TypeScript 后端项目建立稳定、可维护、偏生产导向的工程规范。它默认强调先判断框架、运行时形态和依赖管理，再决定目录结构、模块边界、任务运行策略和公共基建。

## Workflow

1. 先确认项目类型：API、BFF、微服务、Worker、定时任务、脚本服务还是网关层。
2. 再确认项目使用的是 `NestJS`、`Express`、`Fastify`、`Koa`，还是已有内部框架。
3. 再确认是否统一使用 `TypeScript`，以及包管理工具是 `pnpm`、`npm`、`yarn` 还是 monorepo 方案。
4. 再根据业务判断是否需要 `PostgreSQL`、`MySQL`、`Redis`、`MQ`、对象存储、搜索或第三方回调。
5. 已有项目优先跟随现有模块边界、中间件和构建方案。
6. 编码时必须重视注释、异步边界、错误处理、日志、测试和运行时约束。

## First Question

做 Node.js 后端项目时，第一优先级问题是：

- 这是 `NestJS`、`Express`、`Fastify`、`Koa` 项目，还是已有内部框架？

第二优先级问题是：

- 这是 API / BFF、Worker、定时任务还是脚本型服务？是否强制使用 `TypeScript`？

如果用户没说明清楚，就先问；不要直接默认框架和运行时形态。

## Core Rules

- Controller / Route 不承载完整业务编排
- Service 负责业务逻辑，Repository / DAO 负责数据访问
- 不把数据库访问、外部调用、缓存逻辑和业务编排全堆进一个文件
- 异步逻辑必须显式处理超时、重试、幂等和失败分支
- 公共能力优先抽模块，不复制粘贴
- 依赖管理、脚本入口、日志、异常和响应结构要统一

## Comments Standard

- 模块、类、公共函数优先补职责注释
- 方法注释重点写输入、输出、副作用、异步行为和边界条件
- 队列任务、回调处理、缓存更新、状态流转和批处理优先补齐注释

详细见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- `controller` / `routes`：协议层
- `service`：业务编排
- `repository` / `dao`：数据访问
- `modules`：按业务域拆分
- `clients`：第三方依赖调用
- `jobs` / `workers`：异步任务
- `config`：配置收口
- `common` / `shared`：公共能力

详细见 `references/structure.md`。

## API And Error Standard

- 返回结构、错误码、分页对象、trace 信息统一
- Route / Controller 只负责协议层和参数门面
- 参数错误、业务错误、权限错误、系统错误清晰分层

详细见 `references/api-standard.md` 与 `references/error-handling.md`。

## Runtime And Task Standard

- 统一处理进程退出、未捕获异常、未处理 Promise 拒绝和优雅停机
- Worker、定时任务和批处理要明确超时、重试、幂等、告警和补偿策略
- API 与任务共享代码时，明确事件循环、连接池和并发边界

详细见 `references/runtime-tasks.md`。

## Logging And Observability

- 日志要带 requestId、traceId、任务 ID、关键主键和耗时
- 不打印敏感信息，不打无意义噪音
- 指标、健康检查和关键任务状态要可观测

详细见 `references/logging.md`。

## Testing Standard

- 核心业务、异常分支、边界条件、异步任务和回调处理要有测试
- 区分单元测试、集成测试和关键链路验证

详细见 `references/testing.md`。

## Security And Dependency Standard

- 参数校验、认证鉴权、敏感信息保护、上传下载边界要统一
- 依赖管理优先统一工具链和锁文件，不允许环境漂移过大
- 回调、Webhook、导出接口和后台高权限接口重点考虑安全约束

详细见 `references/security.md` 与 `references/dependencies.md`。

## Recommended Stack

- Framework：`NestJS`、`Express`、`Fastify`
- Language：优先 `TypeScript`
- ORM / Query：`Prisma`、`TypeORM`、`Knex`
- Cache：`Redis`
- MQ：`BullMQ`、`RabbitMQ`、`Kafka`
- Validation：`zod`、`class-validator`
- Testing：`Jest`、`Vitest`
- Docs：`OpenAPI`

详细见 `references/framework-selection.md`。

## When To Use

- 用户要开始一个 Node.js 或 TypeScript 后端项目
- 用户要规范 API、BFF、Worker、定时任务或脚本服务的结构和运行时边界
- 用户要统一注释、异步任务、依赖管理、日志、测试和安全策略
- 用户要在 `NestJS / Express / Fastify / Prisma / Redis / MQ` 这类常见栈里建立工程标准

## References

- `references/comments.md`
- `references/structure.md`
- `references/api-standard.md`
- `references/error-handling.md`
- `references/runtime-tasks.md`
- `references/logging.md`
- `references/testing.md`
- `references/security.md`
- `references/dependencies.md`
- `references/framework-selection.md`

## Platform Adapters

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

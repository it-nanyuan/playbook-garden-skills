---
name: ruby-development-playbook
description: Build maintainable Ruby services and applications with clear architecture and coding standards. Use when planning or implementing Rails applications, Ruby APIs, background jobs, scheduled tasks, business systems, or service modules, and always clarify whether the project is Rails, Sinatra, Grape, Hanami, Sidekiq-based, or an existing internal framework before choosing structure, runtime conventions, and common components such as PostgreSQL, MySQL, Redis, queues, or search.
---

# Ruby Development Playbook

## Overview

这个 skill 用来为 Ruby 项目建立稳定、可维护、偏生产导向的工程规范。它默认强调先判断框架、应用形态和后台任务体系，再决定分层、模块边界、异步任务策略、测试方式和运行时约束。

## Workflow

1. 先确认项目类型：Rails 应用、API 服务、后台系统、Worker、定时任务还是业务脚本服务。
2. 再确认使用的是 `Rails`、`Sinatra`、`Grape`、`Hanami`，还是已有内部框架。
3. 再确认是否有 `Sidekiq`、`ActiveJob`、`Cron`、`Redis`、`PostgreSQL / MySQL` 和搜索能力。
4. 已有项目优先跟随现有目录结构、约定式组织、Gem 选型和部署方式。
5. 新项目先定模块职责、服务层边界、任务边界和公共能力，再写 Controller、Service、Model、Job、Serializer 和集成层。
6. 编码时必须重视注释、测试、事务边界、异步幂等、日志和安全约束。

## First Question

做 Ruby 项目时，第一优先级问题是：

- 这是 `Rails`、`Sinatra`、`Grape`、`Hanami` 项目，还是已有内部框架？

第二优先级问题是：

- 这是全栈业务系统、纯 API、后台任务系统还是脚本型服务？后台任务使用 `Sidekiq`、`ActiveJob`，还是别的方案？

判断规则：

- `Rails`：适合后台系统、业务系统、API 和中大型约定式项目
- `Sinatra`：更轻量，适合小型服务或定制化较强的项目
- `Grape`：偏 API 组织，适合接口边界较清晰的服务
- `Hanami`：更强调边界和模块化，但团队需要更稳的工程习惯
- `Sidekiq`：适合成熟后台任务体系，但必须补齐幂等、重试、告警和监控

如果用户没说明清楚，就先问；不要直接默认 `Rails` 或默认后台任务方案。

## Core Rules

- Controller / Endpoint 不承载完整业务编排
- Service / Use Case 负责业务流程，Model 负责领域数据和明确规则
- Repository / Query / Gateway 负责复杂查询和外部依赖，不把数据访问散落在业务代码里
- 不把缓存、外部调用、事务编排、状态流转和任务投递堆在一个方法里
- 公共能力优先抽 module、service object 或 shared concern，但不要滥用 concern 逃避清晰设计
- 约定式框架不代表可以放弃边界，结构清晰比“先能跑”更重要

## Comments Standard

- 类注释：说明职责、业务边界、适用场景
- 方法注释：说明输入、输出、副作用、事务、缓存、任务投递和异常语义
- 属性 / 常量注释：重点解释业务含义、状态值、单位和约束
- Service、Job、回调处理、状态流转、支付链路、缓存更新、批处理和复杂 ActiveRecord 查询优先补齐注释

详细见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- `controllers` / `api`：协议层
- `models`：领域数据与关系
- `services`：业务编排
- `queries` / `repositories`：复杂查询与数据访问封装
- `jobs` / `workers`：异步任务
- `serializers` / `presenters`：响应转换
- `interactors` / `use_cases`：复杂业务用例
- `clients` / `gateways`：第三方依赖集成
- `lib` / `shared`：公共能力

详细见 `references/structure.md`。

## API And Error Standard

- 返回结构、错误码、分页对象和 trace 信息统一
- Controller / Endpoint 只负责协议层和参数门面
- 参数错误、业务错误、权限错误、系统错误和第三方依赖错误清晰分层

详细见 `references/api-standard.md` 与 `references/error-handling.md`。

## ActiveRecord And Data Standard

- 复杂查询、批量更新、N+1 风险、事务边界和回调副作用要特别谨慎
- Model 不应该无限膨胀成“上帝对象”
- Scope、Query Object、Repository 的职责要分清

详细见 `references/activerecord-data.md`。

## Job And Runtime Standard

- `Sidekiq`、`ActiveJob`、定时任务和批处理要明确超时、重试、幂等、失败补偿和告警
- Web 进程、Job 进程和调度进程的运行方式与发布策略要区分
- 脚本服务不能无限堆散脚本，长期逻辑要升级为可维护模块

详细见 `references/jobs-runtime.md`。

## Logging And Observability

- 日志要带 requestId、traceId、任务 ID、关键主键和耗时
- 关键任务、外部调用、回调处理和批处理结果要可观测
- 不打印敏感信息，不打无意义噪音

详细见 `references/logging.md`。

## Testing Standard

- 核心业务、Service、Query、Job、回调处理和边界条件要有测试
- 区分单元测试、请求测试、集成测试和关键链路验证
- 关键业务流程不能完全依赖人工回归

详细见 `references/testing.md`。

## Security Standard

- 参数校验、认证鉴权、敏感信息保护、上传下载边界、后台权限统一
- Webhook、支付回调、批量操作、导出接口和高权限后台接口重点考虑安全约束
- 不在日志、异常或响应中泄露敏感数据

详细见 `references/security.md`。

## Recommended Stack

- Framework：`Rails`、`Sinatra`、`Grape`、`Hanami`
- Database：`PostgreSQL`、`MySQL`
- ORM：`ActiveRecord`、`Sequel`
- Queue / Jobs：`Sidekiq`、`ActiveJob`
- Cache：`Redis`
- API Serialization：`ActiveModelSerializers`、`Blueprinter`
- Testing：`RSpec`、`Minitest`、`FactoryBot`
- Quality：`RuboCop`、`Brakeman`

详细见 `references/framework-selection.md`。

## When To Use

- 用户要开始一个 Ruby、Rails、API、后台任务或业务系统项目
- 用户要统一 Ruby 项目的结构、注释、ActiveRecord 约束、任务策略、测试和安全规范
- 用户要在 `Rails / Sidekiq / Redis / PostgreSQL / RSpec` 这类常见栈里建立工程标准
- 用户要做偏业务系统、后台平台、任务系统或 API 服务

## References

- `references/comments.md`
- `references/structure.md`
- `references/api-standard.md`
- `references/error-handling.md`
- `references/activerecord-data.md`
- `references/jobs-runtime.md`
- `references/logging.md`
- `references/testing.md`
- `references/security.md`
- `references/framework-selection.md`

## Platform Adapters

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

---
name: php-development-playbook
description: Build maintainable PHP backend services with clear architecture and coding standards. Use when planning or implementing PHP APIs, admin backends, business systems, scheduled jobs, or service modules, and always clarify whether the project is Laravel, Symfony, Hyperf, ThinkPHP, or an existing custom framework before choosing structure, middleware, and common components such as MySQL, Redis, queues, search, or object storage.
---

# PHP Development Playbook

## Overview

这个 skill 用来为 PHP 后端项目建立稳定、可维护、偏生产导向的工程规范。它默认强调先判断框架与运行形态，再决定目录结构、模块边界、中间件和常用组件组合，同时把注释、分层、复用、测试和可维护性放在和功能实现同等重要的位置。

## Workflow

1. 开始前先确认项目形态：`Laravel`、`Symfony`、`Hyperf`、`ThinkPHP`，还是已有自定义框架。
2. 如果用户没明确说明，必须先问清楚，不要直接默认技术栈。
3. 再根据业务判断是否需要 `MySQL`、`Redis`、队列、搜索、对象存储、权限体系、定时任务、消息推送、第三方支付或回调处理。
4. 已有项目优先跟随现有框架约定、目录结构和公共基建，不要随意改分层。
5. 新项目先定框架、模块边界和目录职责，再写 Controller、Service、Repository、DTO、Model 和 Job。
6. 编码时必须重视注释、单职责、公共能力抽取、异常处理和测试。

## First Question

做 PHP 项目时，第一优先级问题是：

- 这是 `Laravel`、`Symfony`、`Hyperf`、`ThinkPHP`，还是已有项目约定框架？

判断规则：

- `Laravel`：后台业务、管理系统、API、生态完整、团队上手快
- `Symfony`：更强调组件化、领域边界和企业级结构
- `Hyperf`：高并发、协程服务、常驻内存进程、Swoole 体系
- `ThinkPHP`：已有历史项目维护或团队已有沉淀
- 自定义框架：必须先跟随既有结构，不要重写一套“标准答案”

如果用户没说清，就先问；不要一边写代码一边默认框架。

## Core Rules

- 项目重要的不只是能跑，而是后续好维护，所以注释必须认真写
- Controller、Service、Repository、Model、DTO、VO、Request、Resource、Job 各司其职
- Service 层负责业务编排，不把完整业务流程堆在 Controller
- Repository 或明确的数据访问层负责数据库交互，不要在业务代码里到处手写 SQL
- 一个类只承担一个主要职责，不要把业务流程、缓存逻辑、外部调用和数据访问揉在一起
- 公共逻辑优先抽公共服务、组件或 trait，但不要滥用 trait 逃避清晰设计
- 复杂查询可以放数据访问层或框架推荐位置，PHP 业务代码里不应散落大量原始 SQL 字符串
- 配置、日志、异常、缓存、队列和安全边界要统一，不能每个模块各写各的

## Comments Standard

- 类注释：说明类职责、业务边界、核心用途
- 方法注释：说明输入、输出、副作用、事务、异常、缓存或队列影响
- 属性注释：重点解释业务含义、单位、状态值、枚举语义或特殊约束
- 对外接口、复杂业务方法、异步任务、监听器、回调处理、支付链路、缓存更新逻辑优先补齐注释
- 注释重点写“为什么”“约束是什么”“副作用是什么”，不要只写“获取列表”“保存数据”这种空话

详细注释规范见 `references/comments.md`。  
跨语言注释母规范参考 `comment-style-playbook`。

## Structure Standard

- `controller` / `Http/Controllers`：协议层、参数接收、权限门面、返回组装
- `service` / `Services`：业务编排、核心流程
- `repository` / `Repositories`：数据库访问、查询封装
- `model` / `Models`：实体映射、关系定义
- `dto` / `Data`：入参、出参、跨层传输对象
- `request`：参数校验
- `resource` / `transformer`：响应转换
- `job` / `listener` / `event`：异步任务与事件处理
- `command`：CLI 命令、定时任务入口
- `config`：配置收口
- `common` / `Support`：公共能力，但不承载具体业务

项目可以采用简单聚合结构，至少清晰拆出公共能力和业务模块。详细见 `references/structure.md`。

## API Standard

- 接口返回结构、错误码、分页对象、幂等约束和版本策略应统一
- Controller 不直接裸返回 Model，不把 ORM 对象直接暴露给前端
- 入参、出参、分页、列表、详情、导入导出接口保持一致风格
- 返回体统一格式、错误码模板和分页对象命名必须在项目级统一

详细见 `references/api-standard.md`。

## Exception Standard

- 业务异常、系统异常、参数异常、权限异常要有清晰分层
- 对外返回信息统一，内部日志保留足够排查上下文
- 全局异常处理必须收口，不能在每个控制器里各自处理一套

详细见 `references/error-handling.md`。

## Cache And Queue Standard

- 缓存不是默认加速器，必须服务于明确热点数据、查询成本或并发场景
- Key 命名、过期时间、失效策略和一致性策略要统一
- 队列任务要有重试、幂等、失败告警和死信意识
- Redis、队列名、事件名、广播名都要统一命名

详细见 `references/cache-queue.md`。

## Testing Standard

- 核心业务、边界条件、异常分支、数据转换、支付回调和异步任务要有测试意识
- 区分单元测试、集成测试和关键链路验证
- 不要求为所有简单 getter / setter 堆测试，但关键流程不能裸奔

详细见 `references/testing.md`。

## Security Standard

- 参数校验、鉴权、签名校验、敏感信息保护、上传下载边界和后台权限必须统一
- 不在日志、异常或响应里泄露敏感数据
- 外部回调、支付通知、Webhook、文件上传、导出接口要重点考虑安全约束

详细见 `references/security.md`。

## Runtime And Deployment Standard

- `PHP-FPM`、队列 Worker、定时任务、`Swoole / Hyperf` 常驻进程要区分运行时约束
- 常驻进程环境下不能默认沿用传统 PHP “请求结束即释放状态”的心智
- 发布时要明确配置加载、缓存预热、队列重启、Supervisor 或进程管理和回滚方式

详细见 `references/runtime-deployment.md`。

## Recommended Stack

- Framework：`Laravel`、`Symfony`、`Hyperf`、`ThinkPHP` 按项目现状选择
- ORM / DB：`Eloquent`、`Doctrine`，或框架推荐数据库层
- Database：`MySQL`
- Cache：`Redis`
- Queue：`Laravel Queue`、`RabbitMQ`、`Kafka`、`Redis Queue`
- Search：`Elasticsearch`、`OpenSearch`
- Validation：框架原生校验器优先
- Docs：`Swagger / OpenAPI`
- Testing：`PHPUnit`、`Pest`
- Quality：`PHP-CS-Fixer`、`Laravel Pint`、`PHPStan`、`Psalm`

详细见 `references/libraries.md`。

## Framework Guidance

- `Laravel`：优先利用 Request、Resource、Job、Event、Listener、Policy、Service Provider 这些成熟结构
- `Symfony`：重视模块边界、依赖注入、Command、EventSubscriber 和组件职责
- `Hyperf`：特别注意协程环境、常驻内存状态污染、连接释放和并发安全
- `ThinkPHP`：优先跟随现有项目结构，逐步补注释、分层和测试，不要硬切陌生架构

详细见 `references/framework-selection.md`。

## When To Use

在这些场景触发这个 skill：

- 用户要开始一个 PHP 后端项目
- 用户要先判断该走 `Laravel / Symfony / Hyperf / ThinkPHP` 哪条路线
- 用户要统一 PHP 注释、结构、分层、测试、缓存和队列规范
- 用户要做管理后台 API、业务系统、支付链路、回调处理或异步任务
- 用户要建立可长期维护的 PHP 工程标准

## References

- `references/comments.md`
- `references/structure.md`
- `references/api-standard.md`
- `references/error-handling.md`
- `references/cache-queue.md`
- `references/testing.md`
- `references/security.md`
- `references/runtime-deployment.md`
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

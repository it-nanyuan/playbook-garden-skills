---
name: java-development-playbook
description: Build maintainable Java backend services with clear architecture and coding standards. Use when planning or implementing Spring-based backend projects, and always clarify whether the project is monolithic or microservices before choosing structure, middleware, and common components such as MyBatis-Plus, MySQL, Redis, MQ, or Elasticsearch.
---

# Java Development Playbook

## Overview

这个 skill 用来为 Java 后端项目建立稳定的工程规范。它默认强调先判断是单体架构还是微服务架构，再决定目录结构、模块边界、中间件和组件组合，同时把注释、分层、复用和可维护性放在和功能实现同等重要的位置。

## Workflow

1. 开始前先确认项目形态：单体架构还是微服务架构。
2. 如果用户没有明确说明，必须先问清楚，不要直接默认。
3. 再根据业务类型判断是否需要 `MySQL`、`Redis`、`MQ`、`Elasticsearch`、对象存储、定时任务、权限体系、配置中心、注册中心、链路追踪、限流熔断等常见组件。
4. 已有项目优先跟随现有技术栈和模块边界，不要随意换层次或换框架。
5. 新项目先定架构和分层，再写接口、Service、Mapper、实体和 DTO。
6. 编码时必须重视注释、单职责、公共能力抽取和目录清晰度。

## First Question

做 Java 项目时，第一优先级问题是：

- 这是单体架构还是微服务架构？

判断规则：

- 单体：业务边界相对集中、团队规模较小、服务数量不多、部署链路简单
- 微服务：业务域明确拆分、团队协作规模较大、服务独立部署、需要服务治理和异步解耦

如果用户没说清，就先问；不要一边写代码一边默认架构。

## Core Rules

- 项目重要的不只是能跑，而是后续好维护，所以注释必须认真写
- Controller、Service、Manager、Mapper、Entity、DTO、VO、Convert 各司其职
- `service` 必须定义接口，具体实现必须放在 `service.impl`
- 一个类只承担一个主要职责，不要把业务流程、数据库操作、缓存逻辑和第三方调用揉在一起
- 公共逻辑优先抽基础能力或公共模块，不要复制粘贴业务代码
- 默认使用清晰分层，不把 SQL、接口参数处理和业务规则堆在 Controller 中
- Java 业务代码里不允许直接出现 SQL 字符串
- 复杂查询、动态 SQL、联表逻辑统一放到 `mapper.xml` 或清晰的数据访问层，不要把 SQL 字符串散落在业务代码里
- 接口、事务、异常、日志和微服务治理要有统一约束，不能各写各的

## Comments Standard

- 类注释：说明类职责、业务边界、核心用途
- 方法注释：说明输入、输出、事务、副作用、异常、缓存或消息影响
- 字段注释：重点解释业务含义、单位、状态值或特殊约束
- 对外接口、复杂业务方法、异步消费、定时任务、缓存更新、ES 同步逻辑优先补齐注释
- 注释写“为什么”和“业务含义”，不要只写“查询数据”“保存对象”这种废话

详细注释规范见 `references/comments.md`。

## Structure Standard

- `controller`：接口入参校验、权限门面、返回组装
- `service`：只放服务接口定义
- `service.impl`：服务实现类，负责核心业务编排
- `manager` / `domain service`：跨资源协调、复杂领域能力
- `mapper`：数据库访问接口
- `mapper.xml`：复杂查询 SQL、动态条件、联表逻辑
- `entity`：数据库实体
- `dto`：入参 / 出参传输对象
- `vo`：视图展示对象
- `convert`：对象转换
- `config`：配置类
- `job`：定时任务
- `consumer` / `mq`：消息消费
- 项目可以采用简单聚合工程结构，至少清晰拆出 `common` 和业务项目模块
- `common` 负责通用能力、基础对象、公共配置、工具、统一返回体等共享内容
- 业务项目模块负责具体业务实现，不要把业务逻辑反向堆回 `common`

详细结构规则见 `references/structure.md`。

## API Standard

- 接口返回结构、分页对象、错误码、幂等约束、版本策略应统一
- Controller 不应把领域对象直接裸返回给外部调用方
- 入参、出参、分页、列表、详情、导入导出接口要有一致风格
- 返回体统一格式、错误码模板和分页对象命名必须在项目级统一，不允许每个模块各写一套

详细见 `references/api-standard.md`。

## Transaction Standard

- 事务只包真正需要原子性的业务步骤
- 不要把远程调用、长耗时任务、循环大批量处理盲目包进一个大事务
- 涉及消息、缓存、数据库多步骤一致性时，要明确事务边界和补偿策略

详细见 `references/transaction.md`。

## Exception Standard

- 业务异常、系统异常、参数异常、权限异常应有清晰分层
- 对外返回信息要统一，内部日志要保留足够排查上下文
- 全局异常处理必须收口，不能让异常处理方式散落在每个接口里

详细见 `references/exception.md`。

## Logging Standard

- 关键业务流、异常、重试、降级、MQ 消费、定时任务要有清晰日志
- 不打印敏感信息，不堆无意义日志，不漏关键上下文
- 微服务场景要重视 traceId、请求链路和关键耗时

详细见 `references/logging.md`。

## Cache Standard

- 缓存不是默认加速器，必须服务于明确的热点数据、查询成本或并发场景
- Key 命名、过期时间、删除策略、更新策略和穿透保护要统一
- 涉及缓存与数据库一致性时，要明确先删缓存还是先更新库，以及失败补偿策略
- Redis key 前缀规范必须统一，至少体现系统、业务域、资源类型和环境语义

详细见 `references/cache.md`。

## Naming Standard

- 包名、类名、方法名、DTO、VO、Enum、常量和数据库字段命名应统一清晰
- 命名优先体现业务语义，不接受随意缩写和模糊词
- 状态、类型、动作类命名必须可读，不靠注释猜意思
- MQ topic、tag、consumer group、消息 key 命名必须统一，不允许各模块自由发挥

详细见 `references/naming.md`。

## Testing Standard

- 核心业务、转换逻辑、异常分支、幂等逻辑和边界条件要有测试意识
- 至少区分单元测试、集成测试和关键链路验证
- 不要求每个 getter/setter 都测，但关键业务流程不能完全裸奔

详细见 `references/testing.md`。

## Security Standard

- 权限、认证、参数校验、敏感信息保护和接口暴露边界要有统一标准
- 不在日志、异常或返回体中泄露敏感数据
- 外部接口、上传下载、回调入口、管理后台接口要重点考虑安全约束

详细见 `references/security.md`。

## Common Stack

- Language：`Java`
- Framework：单体优先 `Spring Boot`，微服务优先 `Spring Boot + Spring Cloud` 或 `Spring Boot + Spring Cloud Alibaba`
- ORM：`MyBatis-Plus`
- SQL Mapping：`mapper.xml`
- Database：`MySQL`
- Cache：`Redis`
- Boilerplate：`Lombok`，基础实体和简单模型可用 `@Data`，但不要盲目滥用在所有领域对象
- Docs / Validation：`springdoc-openapi`、`jakarta validation`

## Middleware Selection

按项目需求选择组件，不要机械全上：

- 搜索、复杂检索、全文检索：`Elasticsearch`
- 异步削峰、解耦、广播：`RabbitMQ`、`RocketMQ`、`Kafka`
- 缓存、分布式锁、热点数据：`Redis`
- 文件上传和对象存储：按云厂商或项目现状选择
- 定时调度：`Spring Scheduling`，复杂场景再考虑调度平台
- 权限认证：`Spring Security`、`Sa-Token`、`JWT`
- 服务调用：`OpenFeign`
- 服务注册与配置：`Nacos`、`Eureka`、`Apollo`
- 网关：`Spring Cloud Gateway`
- 限流熔断降级：`Sentinel`、`Resilience4j`
- 分布式事务：`Seata`
- 调度平台：`XXL-Job`
- 链路追踪与可观测性：`SkyWalking`、`Zipkin`、`Micrometer`

详细技术栈见 `references/stack-selection.md`。

## Monolith Vs Microservices

- 单体项目优先保持模块清晰、边界明确、目录稳定，不要把所有业务挤在一个 package
- 微服务项目优先明确服务边界、共享能力边界、调用方式、配置和容错策略
- 微服务不要把本应独立的领域强耦合成同步链式调用
- 单体也不要因为“听起来高级”无脑拆服务
- 单体项目常见组合可以是 `Spring Boot + MyBatis-Plus + MySQL + Redis + Lombok + springdoc-openapi`
- 微服务项目常见组合可以是 `Spring Boot + Spring Cloud Alibaba + Nacos + OpenFeign + Gateway + Sentinel + Redis + MQ + MySQL`

详细见 `references/architecture.md`。

## Microservice Guidelines

- 微服务拆分按业务域和团队协作边界来，不按数据库表数量拆
- 服务调用、超时、重试、限流、降级、配置中心、注册发现、链路追踪都要统一规范
- Feign、Gateway、MQ、配置中心、注册中心、分布式事务等组件只在真正需要时引入

详细见 `references/microservice-guidelines.md`。

## When To Use

在这些场景触发这个 skill：

- 用户要开始一个 Java 后端项目
- 用户要先判断单体还是微服务
- 用户要统一 Java 注释、结构、分层、Mapper 和常用中间件规范
- 用户要强制 `service` + `service.impl` 标准结构
- 用户要在 `Spring Boot + MyBatis-Plus + MySQL + Redis` 这类常规栈里开发
- 用户要根据业务选 `ES`、`MQ` 等组件，而不是无脑堆技术栈

## References

- `references/comments.md`
- `references/structure.md`
- `references/architecture.md`
- `references/stack-selection.md`
- `references/api-standard.md`
- `references/transaction.md`
- `references/exception.md`
- `references/logging.md`
- `references/cache.md`
- `references/naming.md`
- `references/testing.md`
- `references/security.md`
- `references/microservice-guidelines.md`

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

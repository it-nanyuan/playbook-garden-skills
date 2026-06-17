# PHP Framework Selection

## Ask First

- 当前项目是新建还是维护已有项目？
- 团队对哪个框架最熟？
- 是否要求高并发常驻进程？
- 是否已有现成后台、权限、队列、支付或管理系统基建？

## Selection Guidance

- `Laravel`
  - 适合多数后台、业务系统、API 和管理平台
  - 生态完整，脚手架、队列、任务、认证、事件体系成熟

- `Symfony`
  - 适合更重视边界、组件化和长期企业级维护的系统
  - 结构更严谨，但团队需要更稳定的工程习惯

- `Hyperf`
  - 适合高并发、Swoole、协程常驻进程场景
  - 需要更强的运行时理解，避免静态变量和对象状态污染

- `ThinkPHP`
  - 多见于既有项目维护
  - 优先延续现有沉淀，逐步补规范，不建议突然推翻重来

## Common Components

- 数据库：`MySQL`
- 缓存：`Redis`
- 队列：`Redis Queue`、`RabbitMQ`、`Kafka`
- 搜索：`Elasticsearch`
- 存储：对象存储按云平台或项目现状选择

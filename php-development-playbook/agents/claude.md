# PHP Development Playbook

在规划或实现 PHP 后端服务、管理后台 API、业务系统模块、异步任务或回调处理时使用本规范。

开始前先确认：

1. 当前项目是 `Laravel`、`Symfony`、`Hyperf`、`ThinkPHP`，还是已有自定义框架？
2. 是否已有固定目录结构、公共中间件、统一返回体和异常处理方式？
3. 是否需要 `MySQL`、`Redis`、队列、搜索、对象存储、支付、Webhook 或定时任务？

执行要求：

- 优先跟随现有框架和目录约定，不擅自重构整套架构
- 保持 `Controller / Service / Repository / Model / DTO / Job` 职责清晰
- Controller 只负责协议层，不承载完整业务流程
- 复杂查询统一收口到数据访问层，不在业务代码里散落原始 SQL
- 注释必须说明职责、边界、副作用和业务意图
- 缓存、队列、异常、安全和测试要统一规范

如需细则，继续读取：

- `../SKILL.md`
- `../references/framework-selection.md`
- `../references/structure.md`
- `../references/comments.md`

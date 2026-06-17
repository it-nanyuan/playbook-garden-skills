# PHP Structure Standard

## Goals

- 让协议层、业务层、数据层、异步层和公共能力边界清晰
- 让已有框架能继续发挥生态优势，而不是被强行改造成奇怪结构

## Recommended Layers

- `Http/Controllers` 或 `controller`：接参、鉴权门面、返回组装
- `Services` 或 `service`：业务编排
- `Repositories` 或 `repository`：数据库访问与查询封装
- `Models` 或 `model`：实体与关系
- `DTO` / `Data` / `VO`：跨层数据结构
- `Http/Requests`：参数校验
- `Http/Resources` / `Transformer`：响应转换
- `Jobs` / `Listeners` / `Events`：异步逻辑
- `Console/Commands`：命令行任务和定时任务入口
- `Support` / `Common`：基础工具、统一返回、公共异常、辅助组件

## Rules

- Controller 不直接写完整业务流程
- Service 不直接承担协议层格式化职责
- Repository 不混入复杂业务判断
- 不把通用能力和具体业务都堆进 `Helpers` 或 `Utils`
- 大模块可继续细分为订单、用户、支付、库存等业务域

## Framework Notes

- Laravel：优先跟随 `app/Http`、`app/Models`、`app/Jobs`、`app/Console` 等约定
- Symfony：优先利用 `Controller`、`Command`、`EventSubscriber`、`Service` 等明确职责组件
- Hyperf：注意协程上下文、连接池和常驻进程对象状态
- ThinkPHP：保持现有项目约定，逐步补层次与注释

# C# Structure Standard

- `Api` / `Web`：协议层
- `Application`：业务编排
- `Domain`：核心业务规则
- `Infrastructure`：数据库、缓存、消息、第三方集成
- `Contracts` / `DTOs`：跨层对象
- `Workers` / `BackgroundTasks`：后台任务
- `Shared`：通用能力

规则：

- Endpoint 不直接承载完整业务流程
- Domain 不依赖 Web 层
- Infrastructure 不反向决定业务规则

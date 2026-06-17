# C# Framework Selection

- `ASP.NET Core MVC`：适合多数业务 API 和后台系统
- `Minimal API`：适合轻量服务或明确边界的小型接口层
- `gRPC`：适合内部高性能服务调用
- `Worker Service`：适合后台任务和常驻处理
- `EF Core`：开发效率高，适合多数 CRUD 和中型业务
- `Dapper`：更贴近 SQL，适合复杂查询和性能感知场景
- `Hangfire` / `Quartz.NET`：适合调度与后台任务

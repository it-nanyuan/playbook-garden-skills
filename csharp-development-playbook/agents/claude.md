# C# Development Playbook

在规划或实现 C# / .NET API、企业后台、Worker Service、定时任务或类库时使用本规范。

开始前先确认：

1. 当前项目是单体、微服务、Worker、类库，还是已有企业系统扩展？
2. 使用 `ASP.NET Core MVC`、`Minimal API`、`gRPC` 还是 `Worker Service`？
3. 数据访问是 `EF Core`、`Dapper`，还是混合方案？

执行要求：

- 优先跟随现有解决方案结构和公共基础设施
- 保持 `Api / Application / Domain / Infrastructure` 边界清晰
- Controller 或 Endpoint 不承载完整业务流程
- 日志、异常、返回体、缓存和消息策略统一
- 注释必须说明职责、边界和副作用

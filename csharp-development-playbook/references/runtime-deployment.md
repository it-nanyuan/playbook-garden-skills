# C# Runtime And Deployment Standard

- 区分 ASP.NET Core API、Worker Service、Hangfire、Quartz.NET 等运行形态
- 发布前确认配置、数据库迁移、缓存策略和任务兼容窗口
- 发布后明确是否需要重启 API、Worker、调度器和消息消费进程
- 生产变更必须有回滚思路

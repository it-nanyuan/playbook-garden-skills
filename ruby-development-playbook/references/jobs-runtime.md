# Ruby Jobs And Runtime Standard

- `Sidekiq`、`ActiveJob`、Cron、批处理脚本要明确重试、幂等、超时和告警
- Web 进程、Job 进程和调度进程发布策略区分处理
- 大任务拆分，不把完整长链路塞进单个 Job
- 失败补偿、死信和重复执行风险要有明确方案

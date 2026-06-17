# Node.js Runtime And Task Standard

- 统一处理未捕获异常、未处理 Promise 拒绝和优雅停机
- Worker、Cron、批处理任务必须考虑超时、重试、幂等和告警
- 长任务拆小，不让单个任务承担过重链路

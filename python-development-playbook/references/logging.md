# Python Logging Standard

## Core Rules

- 日志必须可检索、可关联、可定位问题
- API 请求、后台任务、回调处理和批处理都要带关键上下文
- 不打印敏感信息，不堆无意义调试日志

## Recommended Context

- `trace_id`
- `request_id`
- `task_id`
- 核心业务主键
- 外部依赖名称
- 耗时

## Common Scenarios

- API：记录入口、核心参数摘要、结果状态和耗时
- Worker：记录任务来源、重试次数、失败原因和补偿动作
- 批处理：记录批次号、成功失败数量和断点恢复信息

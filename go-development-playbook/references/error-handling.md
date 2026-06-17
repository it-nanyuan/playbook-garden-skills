# Error Handling

## Rule

- 显式处理 error
- 不静默吞错
- wrap 错误时保留上下文
- 业务错误与系统错误分层

## Good Bias

- 关键错误带业务主键信息
- 外部调用错误保留超时、状态码、依赖信息

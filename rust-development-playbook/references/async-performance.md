# Rust Async And Performance Standard

- 明确 `tokio` 运行时、任务取消、超时和资源释放策略
- 锁、共享状态、连接池和背压要有明确取舍
- 性能优化要有测量依据，不滥用 `unsafe`
- CPU 密集任务与 I/O 密集任务要区分处理

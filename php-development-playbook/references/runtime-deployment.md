# PHP Runtime And Deployment Standard

## Runtime Types

- `PHP-FPM`
  - 传统请求生命周期，单次请求结束后状态释放
  - 适合多数后台和 API 项目

- Queue Worker
  - 长时间运行
  - 要关注内存增长、失败重试、进程重启和日志轮转

- `Hyperf / Swoole`
  - 常驻内存进程
  - 必须防止静态变量、单例对象和上下文状态污染

## Deployment Rules

- 发布前确认配置、环境变量、迁移脚本和缓存策略
- 发布后明确是否需要重启 FPM、队列 Worker、Scheduler 或常驻进程
- 生产变更必须有回滚思路
- 涉及迁移、队列结构、缓存 key 变更时要说明兼容窗口

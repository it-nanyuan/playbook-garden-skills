# PHP Cache And Queue Standard

## Cache

- Redis key 前缀统一体现系统、环境、业务域和资源语义
- TTL 不能随意写死，关键缓存要说明更新和失效策略
- 先删缓存还是先更新数据库，要在项目级统一
- 热点缓存、详情缓存、配置缓存和统计缓存区别对待

## Queue

- 任务必须考虑幂等
- 明确重试次数、超时、失败转移和告警策略
- 队列名称、topic、tag、consumer group 统一命名
- 长任务、大批量任务要拆分，不在单个 Job 里长时间阻塞

## Events And Callbacks

- Event / Listener 适合业务解耦，不要隐式塞进核心同步链路里导致难排查
- Webhook / 回调处理要先验签，再验幂等，再更新状态

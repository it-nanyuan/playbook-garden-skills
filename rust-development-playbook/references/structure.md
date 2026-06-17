# Rust Structure Standard

- `bin/`：入口
- `lib.rs`：导出与模块组织
- `application` / `service`：业务编排
- `domain`：核心规则
- `infrastructure` / `adapter`：数据库、缓存、外部依赖
- `transport` / `http`：协议层
- `jobs` / `worker`：异步任务

规则：

- transport 不承载完整业务流程
- domain 不依赖具体协议层
- workspace 场景下 crate 边界要稳定

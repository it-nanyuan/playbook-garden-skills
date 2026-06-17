# Node.js Structure Standard

- `controller` / `routes`：协议层
- `service`：业务编排
- `repository` / `dao`：数据访问
- `clients`：第三方依赖调用
- `jobs` / `workers`：异步任务
- `modules`：业务域拆分
- `common` / `shared`：公共能力

规则：

- Route 不承载完整业务流程
- Service 不直接负责 HTTP 返回格式
- Repository 不混入复杂业务判断

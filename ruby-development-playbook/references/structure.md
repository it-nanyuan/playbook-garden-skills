# Ruby Structure Standard

- `controllers` / `api`：协议层
- `models`：领域数据与关系
- `services`：业务编排
- `queries` / `repositories`：复杂查询与数据访问封装
- `jobs` / `workers`：异步任务
- `serializers` / `presenters`：响应转换
- `clients` / `gateways`：第三方依赖
- `lib` / `shared`：公共能力

规则：

- Controller 不承载完整业务流程
- Model 不承担所有业务编排
- Query / Repository 不混入复杂业务判断

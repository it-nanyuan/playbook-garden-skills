# Ruby ActiveRecord And Data Standard

- 复杂查询、批量更新和事务边界要显式设计
- 特别注意 N+1、回调副作用和 Model 膨胀
- Scope 负责简单筛选，复杂查询优先 Query Object 或 Repository
- 数据迁移、索引和大批量数据修改要有兼容和回滚意识

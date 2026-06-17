# Safety

## Production Rules

- 先确认环境
- 先看影响范围
- 先准备回滚或备份
- 先看执行计划

## Dangerous Operations

- 无条件 `UPDATE`
- 无条件 `DELETE`
- 高峰期大表 `ALTER`
- 不分批的大范围修复

## Rule

- 生产变更优先选择低峰窗口
- 大批量操作分批执行
- 高风险语句先在低环境验证

# Comments

## Goal

前端项目也必须重视注释，尤其是在复杂交互和业务状态越来越多的时候。

## Required

- 组件：职责、关键 props、适用场景
- hooks：输入、输出、副作用、依赖
- 方法：业务作用、边界、异步行为
- 复杂 state：业务语义、枚举值、单位

## Priorities

- 表格页
- 筛选逻辑
- 权限逻辑
- 数据转换
- 缓存逻辑
- 复杂弹窗或抽屉表单

## Avoid

- `// render list`
- `// fetch api`
- `// set loading`

## Good Bias

- 注释重点写“为什么这样设计”
- UI 交互分支和业务规则优先写清楚

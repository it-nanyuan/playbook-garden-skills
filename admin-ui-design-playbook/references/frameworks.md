# Frameworks

## Default Stack

后台网页优先支持：

- `React + TypeScript + Ant Design`
- `Vue 3 + TypeScript + Element Plus`

## Selection Rules

- 已有仓库：严格跟随现有框架和组件体系
- 新项目、复杂企业后台、跨团队协作较多：可优先考虑 `React + TypeScript + Ant Design`
- Vue 团队、国内中后台、已有 Element 资产较多：可优先考虑 `Vue 3 + TypeScript + Element Plus`

## Component Usage

- 优先复用成熟组件，而不是从零手写所有控件
- 表单、表格、分页、抽屉、弹窗、标签、菜单等优先用组件库能力
- 复杂页面通过布局和信息架构形成品质，不靠自定义奇怪造型

## Implementation Bias

- 页面骨架先稳，再做视觉细化
- 后台项目优先保证导航、筛选、表格、状态和操作流顺手
- 如果要给代码，尽量用组件库原生能力组合出专业效果，而不是堆很多无意义装饰层

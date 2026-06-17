# Structure

## File Rules

- 一个文件一个主类型
- 相关扩展用 `extension` 拆开
- 不把模型、网络、页面、工具方法堆进同一个文件

## Suggested Split

- `FeatureView.swift`
- `FeatureViewModel.swift`
- `FeatureService.swift`
- `FeatureModel.swift`
- `FeatureRouter.swift`
- `FeatureView+Sections.swift`
- `FeatureViewModel+Actions.swift`

## Reuse Bias

- 公共按钮、空状态、错误态、加载态优先沉淀组件
- 列表页、表单页、详情页的通用容器优先抽象
- 对未来多个业务点可复用的逻辑优先从页面中抽离

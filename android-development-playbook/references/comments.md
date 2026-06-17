# Comments

## Goal

注释帮助理解业务意图、状态流转和接口边界，不是代码翻译器。

## Required

- Activity、Fragment、Compose 页面、ViewModel、UseCase、Repository：写职责
- 公共方法：写参数、返回值、副作用、线程或状态影响
- 复杂状态字段：写业务含义或特殊约束

## Avoid

- `// init view`
- `// request data`
- `// click event`

## Good Bias

- 复杂状态流、缓存策略、权限分支、兼容逻辑要说明原因
- 对团队复用的公共模块，注释优先级更高

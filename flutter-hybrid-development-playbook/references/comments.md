# Comments

## Goal

注释帮助团队理解 widget、状态和桥接逻辑的职责，不是逐行翻译 Dart 代码。

## Required

- 页面、widget、controller、service、model、bridge：写职责
- 公共方法：写输入、输出、副作用、异步行为
- 与原生交互字段：写协议含义和约束

## Avoid

- `// build widget`
- `// fetch data`
- `// set state`

## Good Bias

- 复杂状态切换、桥接协议、缓存策略、兼容逻辑附近补注释
- 公共 package 的注释优先级高于页面私有实现

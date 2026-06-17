# React Native Development Playbook

在规划或实现 React Native 页面、组件、导航流、状态管理、原生桥接或共享业务模块时使用本规范。

开始前先确认：

1. 当前项目是 `Expo`、裸 `React Native`，还是混合架构项目？
2. 使用什么导航和状态管理方案？
3. 这次需求属于 screen、component、hook、store、service、bridge 还是 feature module？

执行要求：

- 优先跟随现有导航、状态和 bridge 约定
- 保持 `screen / components / hooks / store / service / bridge` 职责清晰
- 不要把请求、状态、导航和页面展示全部堆在一个 screen 文件
- 混合项目要特别注意 RN 与原生宿主边界

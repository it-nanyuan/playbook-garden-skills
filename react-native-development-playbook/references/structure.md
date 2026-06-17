# React Native Structure Standard

- `screens`：页面
- `components`：可复用组件
- `hooks`：逻辑复用
- `store`：状态容器
- `services`：业务服务与网络编排
- `navigation`：导航定义
- `bridge`：原生桥接
- `shared` / `common`：跨业务公共能力

规则：

- screen 不承载完整业务流程
- hook 和 service 分工清晰
- bridge 逻辑不散落在页面层

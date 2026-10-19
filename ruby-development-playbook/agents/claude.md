# Ruby Development Playbook

在规划或实现 Ruby、Rails、API、后台任务、业务系统模块或脚本服务时使用本规范。

开始前先确认：

1. 当前项目使用 `Rails`、`Sinatra`、`Grape`、`Hanami`，还是已有内部框架？
2. 这是全栈业务系统、纯 API、后台任务系统还是脚本型服务？
3. 后台任务是 `Sidekiq`、`ActiveJob`，还是其他方案？

执行要求：

- 优先跟随现有框架约定和部署方式
- 保持 controller / service / model / query / job / serializer 边界清晰
- 不要让 Model 或 Controller 无限膨胀
- 任务逻辑必须明确重试、幂等和失败补偿

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

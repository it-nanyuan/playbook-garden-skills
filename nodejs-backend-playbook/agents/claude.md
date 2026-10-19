# Node.js Backend Playbook

在规划或实现 Node.js / TypeScript API、BFF、Worker、定时任务或业务模块时使用本规范。

开始前先确认：

1. 当前项目使用 `NestJS`、`Express`、`Fastify`、`Koa`，还是已有内部框架？
2. 这是 API / BFF、Worker、定时任务还是脚本型服务？
3. 是否统一使用 `TypeScript`？包管理工具和构建方案是什么？

执行要求：

- 优先跟随现有模块边界和运行时约束
- 保持 `controller / service / repository / jobs` 职责清晰
- 异步任务必须显式处理超时、重试、幂等和失败分支
- 日志、异常、响应、依赖管理和安全策略统一

## Cross-Project Standards

新项目启动、设计系统制定或跨页面规范统一时，先读取 `project-standards-playbook/SKILL.md` 及其适用细则；小修复按影响范围应用，保留已有确认参数。

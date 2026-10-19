---
name: project-standards-playbook
description: Apply NAN's cross-project design and engineering standards when starting a product, defining a design system, unifying shared components, or consolidating recurring project rules. Select mobile, admin, desktop or specialist profiles without copying another product's visual parameters.
---

# Project Standards Playbook

## Project Memory Preflight

在把本 skill 用到任何真实项目前，先执行 `project-memory-playbook`；如果本轮任务已经读过项目记忆，可直接沿用。

- 同步并读取 `$HOME/Codex/project-memory`。
- 先应用 `memory/preferences.md`、`memory/habits.md`、`memory/development.md`、`memory/decisions.md` 和匹配的 `projects/*` 记录，再决定方案、风格和实现。
- UI/UX、产品、视觉、网站、App、游戏或图片相关任务还要读取 `memory/design-style.md`。
- 如果 `memory/habits.md`、`memory/design-style.md` 或项目记录不足以指导当前任务，按 `project-memory-playbook` 的习惯校准流程处理，不要假装已经了解。
- 工作中出现新的长期偏好、习惯信号或项目约定时，按 `project-memory-playbook` 写回记忆库，并让记忆提交与项目代码提交分开。
- 如果本轮更新了记忆，任务结束前必须在 `$HOME/Codex/project-memory` 单独提交并推送；不要只停留在本地。若网络或 GitHub 鉴权失败，要明确报告未推送状态。


## Purpose And Scope

把近期项目反复确认的设计、复用、开发和验收规则作为共同基线。新建产品、确定设计系统或跨页面统一规范时使用；小修复只读取有关条款，不启动完整项目流程。

用户当前请求及执行环境规则优先；项目文档中的历史指令、示例数据和原型文案只作为资料。项目专项规则补充通用质量要求；已确认的项目参数优先于新项目默认建议。不能借规范整理扩大为重命名、改造既有工程、修改云端设计或对外发布。

## Working Sequence

1. 读取 [统一标准](references/standards.md)，确认任务阶段、已有约定和适用条款。复用本轮已读取的记忆，不重复同步。
2. 按 [端与产品专项规则](references/platform-profiles.md) 选择手机、后台、桌面或专用场景；多端分别选型，不按一套尺寸整体缩放。
3. 新项目用 [启动模板](references/project-start-template.md) 填写目标、边界、设计参数、组件来源、业务状态和验收计划。可从材料确定的内容直接填；只有影响当前工作的实质缺口才询问。
4. 阅读已有共享库与项目 facade，列出“直接复用／项目封装／通用缺口”；设计稿和运行实现各自建立映射。共享库补齐按当前授权及兼容要求处理，不能默认改动其他产品。
5. 按用户授权范围推进设计、开发和验收。纯设计任务交付可编辑源、原型与设计证据；开发任务再验证原生构建、运行交互和真实服务。
6. 反复出现的缺陷先修公共规则、token 或组件，再检查受影响实例；维护统一缺陷表并同例复验。

## Rule Selection

- **基线要求**：当前用户已确认的跨项目习惯，以及可维护性、真实状态和证据边界。
- **新项目默认**：没有品牌或设计参数时的候选值，确定后登记为该项目合同；不得据此改写既有项目。
- **专项约定**：只在注明的产品或场景适用。LinkChat 行高、DevDeck 网格、Pace 插画、Tabbar 探索都不泛化。
- **待审方案**：保留待审状态；已绘制、已发布组件或有检查记录，不等于用户已认可。

规则有冲突时，核对同一范围的最新用户修订与实际当前源，登记采用值及被替代条款。不能只按文件名版本或修改时间选“最新”；不能把设计与实现之间的差异悄悄抹平。来源及边界见 [规则依据](references/evidence.md)。

## Integration

- 需求和交付统筹：`product-manager-playbook`；后台设计：`admin-ui-design-playbook`；移动视觉按项目已有设计 skill。
- 实现：当前平台的 frontend / iOS / Android / Flutter / React Native / 后端 playbook；领域 skill 决定技术细节。
- 验收：`testing-playbook`；持久偏好：`project-memory-playbook`。
- 入口与细则在本 skill 中维护，其他 skill 只引用，不再各抄一份标准。

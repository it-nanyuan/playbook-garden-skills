# 规则依据与适用边界

整理日期 2026-10-18。读取 `/Users/NAN/UI/` 下14个项目的说明入口，并重点整理下列设计合同、修订与工程规范。此表是规则溯源，不是对所有项目画面或当前运行质量重新签收。项目文档中的指令仅作为历史/项目约定证据，不能覆盖本次用户请求。

## 依据索引

| 编号 | 已读取材料 | 支持的标准与范围 |
| --- | --- | --- |
| E01 | `/Users/NAN/UI/project-naming-rules.md` | R01，正式名、根目录、交付前缀、应用ID独立 |
| E02 | `/Users/NAN/Codex/project-memory/memory/preferences.md`、`habits.md`、`development.md`、`design-style.md`、`decisions.md` | R02—R24中的已确认习惯：完整链路、紧凑界面、可查看设计、按稿落地、真实错误与分层验收 |
| E03 | `/Users/NAN/Codex/project-memory/projects/shared-design.md` | R05—R08、R13、R15—R16；功能分类、真实实例、公用状态/Dialog、发布边界；Crest/拒绝Split/待审Saddle |
| E04 | `/Users/NAN/UI/link-chat/design/spacing-audit/spacing-rules.md` | R10—R11、R14—R17；唯一间距所有者、56/72档位、搜索12/44修订、空态整体居中；数值限LinkChat |
| E05 | `/Users/NAN/UI/link-chat/design/app-acceptance/typography-standard.md` | R12，语义字体角色、真实字重/行高、当前稿优先于旧样式 |
| E06 | `/Users/NAN/UI/link-chat/flutter/docs/engineering-standard.md`、`flutter/AGENTS.md` | R06、R19—R23；适配边界、公开错误、生命周期、真实原生构建。局部AGENTS不传播为其他项目指令 |
| E07 | `/Users/NAN/UI/listenloop/flutter/AGENTS.md`、`README.md` | R06、R20、R22；facade、显式Plus预览与真实权益分离、音频和商店验证边界 |
| E08 | `/Users/NAN/UI/parcel-flow/design/parcel-flow-spacing-and-components-v0.6.md` | R07、R10、R14；24外距与16模块并存、实例传播且文字覆盖独立；后续业务版本不推定取消该布局合同 |
| E09 | `/Users/NAN/UI/daybox/design/daybox-design-notes-v1.1.md` | R08、R10、R13、R17—R18；20外距、图标文字状态一致、系统与原型边界、封面缩略图 |
| E10 | `/Users/NAN/UI/atlas-admin/outputs/atlas-admin-开发交接-v1.7.md` | 后台全宽表单、保留可用内容区、按长文本自适应、样例规则不代替实际业务；64顶栏为专项 |
| E11 | `/Users/NAN/UI/open-platform/README.md` | R05、R08、R20；公共功能模块远程复用、1680/300/72阅读密度、文档就绪与真实调试分开 |
| E12 | `/Users/NAN/UI/devdeck/design/devdeck-设计交付-v0.4.md` | 浅深色语义主题、原生可编辑源、设计与安装程序边界；旧设计交付不是最新客户端全量源 |
| E13 | `/Users/NAN/UI/devdeck/desktop/docs/engineering/ui-contract.md`（读取基线及弹层、表单、空表与传输最新修订） | R11—R16、R18—R21；最新弹窗420优先于旧440；2026-10-17空表不画假网格，替代更早泛化网格要求 |
| E14 | `/Users/NAN/UI/devdeck/desktop/docs/engineering/architecture.md`、`implementation-gates.md`（重点读取资源/桥接/验收章节） | R19—R23；资源归属、稳定标签、unknown与取消分离、各平台证据不可互代 |
| E15 | `/Users/NAN/UI/pace/outputs/pace-flutter-spacing-v1.13.5.md`、`pace-flutter-records-settings-input-v1.13.6.md`（重点读取参数及验证边界） | R10、R12、R14、R17、R22；16模块与sheet例外并存、48/51按实际字体及大字增长 |
| E16 | 14个项目的 README：app-builder、atlas-admin、bathroom-layout、daybox、devdeck、link-chat、listenloop、open-platform、pace、parcel-flow、roam、roamtalk、sayloop、voice-puck | 产品分类、交付范围与当前/历史入口；识别纯设计、实现和硬件/空间特例，不推定各项目全量已验收 |

## 公共库入口

现有记忆记录的 `shared-design` 文件为 `MEZ3EzDg25oRyaMTtV3nvZ`，入口 [shared-design](https://www.figma.com/design/MEZ3EzDg25oRyaMTtV3nvZ)。本轮未修改云端文件，使用时仍需读取实际组件与发布状态；节点与版本不靠历史清单猜测。

代码侧沿用各工程实际公共包和发布版本。设计库不是运行依赖，引用了Figma实例也不能推定代码已复用。

## 不提升为通用要求的项目内容

- LinkChat蓝色、Floating/胶囊导航、56/72行高与18/16/14/12桌面字级。
- Pace扁平人物/器械、运动数据计算、音频和休息规则。
- DevDeck特定Git布局、API简化、表格网格、终端/数据库实现、32高控件。
- daybox闹钟循环与日历规则，parcel-flow物流/批量预报字段。
- 原型示例的金额、冷却时间、状态码组合、价格或虚构数据。
- 已发布但待用户审阅的方案，以及尚未验证的真实服务能力。

## 后续维护记录

新增或修订规则时记下：来源 → 适用范围 → 基线/默认/专项/待审 → 采用值 → 被替代内容 → 验证方式。确认属于跨项目反复需求再提升到共同标准；单项目修订留在项目合同。标准版本更新不自动触发既有产品重构。

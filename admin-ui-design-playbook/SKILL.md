---
name: admin-ui-design-playbook
description: Design professional, commercially credible admin and dashboard interfaces instead of text-heavy mockups. Use when the user wants backend web UI, admin pages, dashboards, operations consoles, or enterprise app layouts and needs the agent to clarify style, competitors, information density, and framework choices before proposing designs or code.
---

# Admin Ui Design Playbook

## Overview

这个 skill 用来把“我要做一个后台页面”这种模糊需求，转成有商用品质的后台 UI 方案。它默认反对夸张大标题、堆满说明文字、满屏卡片和没有信息层级的设计，优先产出清晰、克制、高密度但不压迫的企业级界面。

## Workflow

1. 先判断任务类型：是后台网页、运营控制台、数据看板、管理系统，还是移动 App。
2. 在开始设计前先补齐上下文；如果需求模糊，优先提问，不要直接出图或写页面。
3. 如果用户不擅长描述风格，优先追问竞品、参考产品、喜欢或讨厌的现有页面。
4. 如果是已有项目，先跟随现有技术栈、设计系统和交互模式，不要凭空换风格。
5. 如果是新项目，再根据业务复杂度决定布局、导航深度、组件库和信息密度。
6. 设计输出必须解释信息架构、布局规则、关键状态和组件选择，而不只是给一张“好看但不可落地”的图。

## Discovery Rules

设计前至少确认下面几类信息；如果用户没说清，优先提 3 到 5 个最关键的问题，而不是长篇盘问：

- 这是后台网页、运营平台、数据分析系统，还是移动 App
- 目标用户是谁，是老板、运营、客服、财务、审核员还是管理员
- 最核心的高频任务是什么，用户每天最常操作哪 3 件事
- 有没有竞品、参考产品、行业样板或现成系统截图
- 希望的风格是稳重企业、数据密集、轻量现代，还是偏运营中台
- 是新项目还是已有仓库，已有项目用什么技术栈和组件库

如果用户说不清风格，就问这类问题：

- 有没有你觉得“比较专业”的后台产品可以参考
- 更希望偏 `Linear / Notion` 的简洁感，还是偏 `Ant Design Pro / 阿里云控制台` 的企业后台感
- 是更看重信息密度，还是更看重轻松易读

详细提问模板见 `references/discovery.md`。

## Default Design Direction

如果用户没有给出明确视觉方向，这个 skill 默认采用下面的商用后台基线：

- 不是营销官网风，也不是大字报式 App 引导页
- 标题克制，页面主标题不夸张，不做整页视觉噪音
- 信息优先级明确，重点放在筛选、表格、状态、操作反馈
- 用组件和留白组织复杂信息，不靠大段解释文字堆层次
- 让界面看起来像真实业务系统，而不是 AI 拼出来的卡片墙

## Admin Web Rules

后台网页默认优先考虑 `Vue 3 + TypeScript + Element Plus` 或 `React + TypeScript + Ant Design`。

选择规则：

- 如果仓库已存在框架，严格跟随现有技术栈
- 如果是新项目且没有偏好，复杂企业后台优先可推荐 `React + TypeScript + Ant Design`
- 如果团队偏 Vue 生态或已有 Element 设计资产，推荐 `Vue 3 + TypeScript + Element Plus`

后台布局和交互细则见 `references/admin-web-layout.md`。  
视觉质量基线见 `references/visual-quality.md`。  
技术栈和组件库选择见 `references/frameworks.md`。

## Output Expectations

设计类任务输出至少应包含这些内容中的大部分：

- 对业务目标和目标用户的简短复述
- 明确的界面风格判断
- 页面信息架构或区域划分
- 关键模块说明，例如筛选区、列表区、详情区、操作区
- 状态设计，例如空状态、加载态、错误态、禁用态、权限态
- 如果要落代码，说明采用的框架、组件库和布局骨架

如果用户要求直接产出页面，不要省略这些隐含判断，而是把它们体现在结构和代码里。

## Anti-Patterns

默认避免这些问题：

- 页面一上来就是超大标题和成段说明文字
- 为了“显得丰富”堆很多卡片，实际没有信息组织
- 后台页面做成官网 Hero Section 风格
- 操作区、筛选区、表格区层级混乱
- 列表过宽但没有固定关键列或横向滚动策略
- 顶部导航、标签栏、侧边菜单和内容区一起乱滚
- 图标、颜色、间距全部靠随机感觉，没有系统

## When To Use

在这些场景触发这个 skill：

- 用户要设计后台网页、运营系统、管理平台、控制台、看板
- 用户抱怨 AI 设计出来的页面“不专业”“太多字”“没有商用价值”
- 用户希望先澄清风格、竞品和信息架构，再产出 UI
- 用户要在 `Vue` 或 `React` 后台项目里落地实际页面
- 用户要求 `Ant Design`、`Element Plus`、多级菜单、分栏布局、表格和筛选区规范

## References

按需读取这些参考文件：

- `references/discovery.md`：设计前该问什么，怎么在不打扰用户的前提下补齐上下文
- `references/admin-web-layout.md`：后台布局、导航、标签栏、筛选区、表格区和滚动规则
- `references/visual-quality.md`：商用品质基线、排版密度、卡片使用和常见反模式
- `references/frameworks.md`：`Vue`、`React`、`TypeScript`、`Ant Design`、`Element Plus` 的选择规则

## Platform Adapters

如果需要把这个 skill 接到不同平台：

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

优先查看：

- `references/platforms/README.md`
- `references/platforms/openai.md`
- `references/platforms/claude.md`
- `references/platforms/cursor.md`
- `references/platforms/gemini.md`
- `references/platforms/copilot.md`

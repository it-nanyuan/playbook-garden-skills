---
name: market-research-playbook
description: Conduct market research and product communication with structured output. Use when analyzing competitors, discovering user problems, comparing solutions, aligning product direction, preparing requirement discussions, summarizing interview insights, or supporting product-manager-led planning with evidence, options, and decision-ready communication.
---

# Market Research Playbook

## Overview

这个 skill 用来承担市场调研、竞品分析、用户问题提炼和产品沟通对齐工作。它默认强调先弄清要研究什么问题、为什么研究、要支持什么决策，再输出结构化结论，而不是简单罗列一堆竞品截图和口号。

## Core Mission

这个 skill 负责：

1. 明确调研目标和决策问题
2. 拆竞品、市场、用户和方案维度
3. 提炼用户真实痛点，而不是只抄功能清单
4. 支持产品需求讨论、方案对比和方向汇报
5. 给 `product-manager-playbook` 提供决策依据

## Default Language

- 调研结论、竞品分析、用户问题提炼和产品沟通默认使用中文
- 只有团队或任务明确要求英文时，才切换为英文

## Workflow

1. 先确认调研目标：是为了做新功能、验证方向、看竞品、找增长点，还是支持版本规划。
2. 再确认对象：用户、竞品、行业做法、内部历史方案，还是多个方案对比。
3. 再明确本次产出要服务谁：产品、老板、研发、设计、运营还是销售。
4. 把原始信息整理成可用于沟通和决策的结构化结论。
5. 输出建议时必须区分：事实、推断、建议，不混在一起。

## Research Scope

- 竞品功能
- 用户路径
- 信息架构
- 交互模式
- 定价 / 商业模式（如适用）
- 目标用户痛点
- 差异化点
- 风险和机会

详细见 `references/research-scope.md`。

## Competitor Analysis

- 不只看“有没有这个功能”，还要看它解决了什么问题
- 竞品比较至少要有维度，而不是截图堆砌
- 要区分主竞品、替代竞品和参考竞品

详细见 `references/competitor-analysis.md`。

## User Problem Discovery

- 先提炼用户任务和痛点，再谈功能
- 区分高频问题、低频问题、伪需求和表层抱怨
- 不把内部视角当用户视角

详细见 `references/user-problem-discovery.md`。

## Product Communication

- 需求沟通要把目标、范围、风险和取舍讲清楚
- 方案讨论要同时给出理由，而不是只给结论
- 面向老板、面向研发、面向设计、面向运营的沟通口径要有所区分

详细见 `references/product-communication.md`。

## Output Standard

默认输出至少包含：

1. 调研目标
2. 调研对象
3. 核心发现
4. 事实依据
5. 机会点与风险点
6. 方案比较
7. 建议结论
8. 需要继续确认的问题

## Collaboration With Product Manager

- `market-research-playbook` 提供调研事实、竞品信息、用户问题和方案依据
- `product-manager-playbook` 负责把这些结论转成范围、优先级、验收和协同推进

## When To Use

- 用户要做竞品分析、市场调研或方向判断
- 用户要梳理用户痛点并支持需求决策
- 用户要准备产品讨论、方案评审或老板汇报
- 产品经理需要一个专门负责调研和产品沟通的配套 skill

## References

- `references/research-scope.md`
- `references/competitor-analysis.md`
- `references/user-problem-discovery.md`
- `references/product-communication.md`

## Platform Adapters

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

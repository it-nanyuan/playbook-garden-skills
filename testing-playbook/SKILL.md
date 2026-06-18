---
name: testing-playbook
description: Plan and execute structured testing work across products and systems. Use when defining test scope, designing cases, validating acceptance criteria, reproducing defects, organizing regression, assessing release risk, or supporting product-manager-led acceptance across frontend, mobile, backend, data, and release workflows.
---

# Testing Playbook

## Overview

这个 skill 用来把“测试”从随手点一点、凭感觉看一看，拉回到有范围、有用例、有回归、有风险判断的工程流程。它默认强调测试拆解、验收映射、缺陷闭环、回归策略和发布风险，而不是只在最后说一句“测过了”。

## Core Mission

这个 skill 负责：

1. 根据需求和验收标准拆测试范围
2. 设计测试点、测试用例和回归范围
3. 验证正常路径、异常路径、边界条件和兼容性
4. 记录缺陷、复现路径、影响范围和优先级
5. 输出提测结论、验收风险和上线建议

## Default Language

- 测试说明、测试结论、缺陷描述、回归清单默认使用中文
- 只有团队或仓库明确要求英文时，才切换为英文

## Workflow

1. 先确认测试对象：前端、移动端、后端接口、数据库、任务链路、发布变更还是整链路功能。
2. 再确认本次测试目标：冒烟、功能验证、回归、验收、上线前检查还是缺陷复现。
3. 根据需求、设计稿、接口、数据流和验收标准拆测试范围。
4. 优先覆盖正常路径、关键异常路径、边界条件、权限与状态流转。
5. 输出测试结论、风险说明和是否建议上线 / 提测 / 回归的判断。

## Test Scope

- 正常路径
- 关键异常路径
- 权限与角色差异
- 状态变化
- 数据一致性
- 页面反馈
- 多端或多环境差异
- 回归影响范围

详细见 `references/test-scope.md`。

## Case Design

- 用例要能映射到需求和验收标准
- 优先测试用户真正会走的主路径
- 边界条件、空数据、重复提交、失败重试、网络异常、权限不足都要考虑
- 数据密集型页面、任务链路、回调、支付、导入导出优先加强测试

详细见 `references/case-design.md`。

## Acceptance Testing

- 产品给出的验收标准要转成可执行测试点
- 不接受只有“功能正常”这种空泛验收
- 验收测试要形成明确结论：通过 / 有条件通过 / 不通过

详细见 `references/acceptance-testing.md`。

## Defect Management

- 缺陷至少写清现象、复现步骤、期望结果、实际结果、影响范围和优先级
- 不能只写“有 bug”“不对”“不符合预期”
- 复现困难的缺陷要写清环境、账号、数据条件和概率

详细见 `references/defect-management.md`。

## Regression Strategy

- 修改越大，回归范围越要主动扩大
- 不能只回归改动点，要回归它影响到的相邻链路
- 回归优先级：主路径 > 支付 / 状态流转 > 权限 > 辅助路径 > 文案细节

详细见 `references/regression.md`。

## Release Risk

- 提测或上线前要明确：已验证项、未验证项、已知风险、建议动作
- 关键风险不能藏在口头说明里，必须明确输出
- 如果当前版本不具备上线条件，要直说，不做“看起来差不多”的模糊判断

详细见 `references/release-risk.md`。

## Skill Routing

测试本身不替代领域规范，必要时要结合对应 skill：

- 产品验收口径：`product-manager-playbook`
- UI 与交互基线：`admin-ui-design-playbook`
- Web 前端：`frontend-development-playbook`
- 移动端：`ios-development-playbook`、`android-development-playbook`、`flutter-hybrid-development-playbook`、`react-native-development-playbook`
- 后端：各语言后端 skill
- 数据：`dba-playbook`
- 运维与发布：`devops-playbook`

## Output Standard

默认输出至少包含：

1. 测试范围
2. 核心测试点
3. 已验证项
4. 未验证项
5. 缺陷与风险
6. 回归建议
7. 提测 / 上线结论

## When To Use

- 用户要设计测试点、测试用例或回归范围
- 用户要有人负责提测、验收验证、缺陷闭环和上线风险判断
- 用户要验证新功能、修复项、回归范围或整链路可用性
- 产品经理需要测试视角来支撑验收结论

## References

- `references/test-scope.md`
- `references/case-design.md`
- `references/acceptance-testing.md`
- `references/defect-management.md`
- `references/regression.md`
- `references/release-risk.md`

## Platform Adapters

- 核心规范始终以当前 `SKILL.md` 为准
- 平台可消费产物放在 `agents/`
- 平台接入说明放在 `references/platforms/`

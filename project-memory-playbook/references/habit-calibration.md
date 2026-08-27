# Habit Calibration

Use this reference when memory exists but does not yet understand NAN's habits well enough to guide project work. Calibration must improve execution, not produce a generic preference survey.

## Calibration Triggers

- NAN says the agent does not understand their habits, taste, or preferences.
- `memory/habits.md`, `memory/design-style.md`, or project-specific memory is missing, stale, contradictory, or mostly unknown for the current task.
- NAN gives corrective feedback such as "不是 demo 版", "太多空白", "不要静默吞掉服务端错误", "你自己测试一下", "为什么看不到", "推送", or equivalent durable signals.
- A task depends on autonomy, visual taste, real API/map validation, delivery cadence, or destructive/operational boundaries that are not recorded.

## Evidence First

Before asking questions or writing new habits, inspect the available evidence:

- Current user instruction and any explicit corrections in the active conversation.
- `project-memory` files: `memory/habits.md`, `memory/preferences.md`, `memory/design-style.md`, `memory/development.md`, `memory/decisions.md`, and matching `projects/<project>.md`.
- Recent project summaries or durable memory entries when they are directly relevant.
- Current repository conventions, changed files, runtime state, tests, build scripts, product surface, and deployment/provider constraints.

Do not treat memory as current fact when the project state can drift cheaply. Re-check source, runtime, provider, simulator, or API state before making readiness claims.

## Rule Format

Write habits as executable rules. Each rule should include:

- `Status`: `Confirmed` when the user directly stated or approved it; `Signal` when repeated behavior supports it but it is not explicitly universal.
- `Trigger`: the concrete user phrase, task type, or risk condition that activates the rule.
- `Apply`: the behavior the agent should follow.
- `Counterexample`: what not to do, phrased concretely enough to prevent future mistakes.

Good habits are specific enough to change behavior. Weak habits such as "NAN likes quality" or "NAN wants good UI" should be rewritten into trigger/action/counterexample form.

## Priority Categories

Prefer capturing rules in these categories when evidence exists:

- Autonomy boundary: when to implement directly, when to ask, and when to stop for approval.
- Visual acceptance: what runtime/simulator/browser evidence is required beyond build/test success.
- Real service validation: how to prove API/client/backend behavior without fabricating success.
- Map/geographic credibility: how to separate map rendering, route geometry, provider readiness, and field review.
- Complete product loop: how to avoid demo-only outputs and preserve working controls.
- Delivery cadence: how to report changes, verification, gaps, commits, pushes, URLs, and artifacts.
- Operational caution: routers, credentials, production services, deletion, rollback, and public-edge claims.

## How To Ask

Ask only when the missing preference changes the current work or prevents a durable rule from being written honestly.

- During ordinary project execution, ask at most 1-3 targeted questions.
- For an explicit habit-profile refresh, keep only the 5 highest-value active questions in `memory/habits.md`.
- Prefer concrete tradeoffs over broad surveys.
- If the answer can be inferred from repeated evidence, write it as `Signal` and leave a targeted calibration question only if confirmation would change future behavior.

Useful question shapes:

- "这次我可以直接按最合理假设改完并报告假设，还是需要先给你 2-3 个方向选？"
- "截图看起来不达标但测试已过时，我应该继续自迭代，还是先停下来让你定产品方向？"
- "真实 API/map key 不可用时，你更希望我阻塞并显示原因，还是保留明确标注的 demo fallback 供你看主流程？"

## What Not To Do

- Do not invent taste, architecture preference, validation threshold, or delivery cadence just to fill memory.
- Do not turn one-off frustration into a universal rule without either direct confirmation or repeated evidence.
- Do not store secrets, API keys, credentials, account recovery details, private personal data, noisy logs, or temporary scratch notes.
- Do not leave long questionnaires in memory. Keep only the questions most likely to change future execution.
- Do not claim "done" from build/test output when the relevant preference requires visual, real API, public-edge, or field validation.

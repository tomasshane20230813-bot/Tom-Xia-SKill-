---
name: agent-context-window-guard
description: 大总管主动检查下属 Agent 上下文占用；满了先让它自行刷新，刷新失败就新开标签页续跑，不要等 Tom 来处理。
version: 2026-11-15
source_type: tom-operating-rule
---

# Agent 上下文窗口值守

Tom 于 2026-11-15 定下。大总管巡检下属 Agent（尤其 MAUS / PI+）时必须主动管上下文，不要干等 Tom 发现卡死。

## 何时触发

- 15 分钟巡检、卡点排查、或下属报 `context window` / 不回消息 / `running` 但 `inputTokens=0` 空转时。
- 读 `get_agent_status` 的 `lastUsage.contextWindowUsedTokens` 与 `contextWindowMaxTokens`。

## 阈值与动作

1. **占用 < 70%**：正常；只记进度，不打断。
2. **占用 ≥ 70% 或出现一次 context 警告**：立刻 `steer` 该 Agent 自行压缩/刷新上下文，只保留当前任务硬口径、目标目录、已确认人选清单与下一步，丢掉深度智控旧任务和冗长工具原文。
3. **占用 ≥ 90%，或出现 `Codex ran out of room in the model's context window`，或换模型后仍 0 token 空转、长时间不回 Tom**：判定自行刷新失败。
4. **刷新失败时由大总管新开标签页**：
   - 用同工作区/`cwd`、同模型偏好 `paseo run --no-wait` 开新会话；
   - 把当前任务完整指令、落盘路径、分数线、去重约束一次性写进新会话；
   - `archive` 旧会话，心跳/监控改盯新 Agent ID；
   - 通知 PI+ 与 Tom：旧会话因上下文作废，已切到新 ID。
5. **不要**：在旧爆窗会话里反复塞长指令；把评审意见写入客户目录；等 Tom 来决定要不要新开页。

## 检查清单

- 状态是否 `running/idle/error/archived`
- `contextWindowUsedTokens / contextWindowMaxTokens`
- 最近活动是否只有收件、没有产出
- 客户目录是否仍无新稿（结合任务死线判断是否升级处理）

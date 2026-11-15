---
name: subordinate-plugin-assist-on-request
description: 下属 Agent 主动请求插件协助时，大总管必须零延迟用 LinkedIn 读取该 URL 的详细履历，并调用所有已连接且相关的招聘插件代查回传；不要等 Tom，也不要反过来持续盯盘催问。
version: 2026-11-15
source_type: tom-operating-rule
---

# 下属插件求助：即时响应协助

Tom 于 2026-11-15 定下。大总管默认按 `silent-10min-monitor` 只做例行观察；**一旦下属 Agent 主动提出插件/连接器需求，必须立刻动手协助，不要有卡顿，不要等 Tom 确认。**

## 何时启用

下属（如 PI+、MAUS、协助端）消息里出现以下任一诉求时立即启用：

- 请大总管用 ZoomInfo / Lusha / FullEnrich / Clay / DataForB2B / SignalHire / Apollo / LinkedIn / TheOrg / Vibe / RocketReach 等查人、补履历、核公司
- 本会话缺少连接器 / tool_search=0 / 公开检索 403，请求代搜
- 明确列出目标公司、Title、地区、回传字段清单

这与静默巡检不冲突：日常不盯、不催；**对方来找你时，立刻办。**

## 怎么做

1. **零延迟开查**：收到请求后马上调用可用插件；哪个通就用哪个，失败的注明错误码（如 402），换通道继续，不要空等。
2. **已有 LinkedIn URL 时先读详细履历**：不是只在终审才用 LinkedIn。对对方给出的 `linkedin.com/in/`，用 LinkedIn 插件读取职业经历、职责、学历、地点、语言栏。公开页 authwall 或插件只返回 URL/职称时，如实记障碍，立刻改用 Apollo、SignalHire（无联系方式）、Clay、Lusha、ZoomInfo、FullEnrich、Vibe、The Org、RocketReach、DataForB2B 等已连接插件补同一字段。只回邮箱电话的接口跳过。Codex 里已连接且跟这个缺口相关的插件，该用都用。
3. **严格按请求范围**：只查对方点名的地区/公司/Title/字段；不要擅自扩大范围或改口径。
4. **只读事实回传**：返回全名、现职、公司、城市、可点击 `linkedin.com/in/` URL、任职起止与职责/摘要、学历结束年、语言栏原文（有才回）。把结构化结果放 `/tmp/...` 并 `steer` 回请求方。
5. **不代做终评**：不要替寻访端抬分、凑 ≥70、写客户目录评审意见；评分与落盘仍由请求方负责。
6. **硬红线**：不导出邮箱/电话/联系方式；不用 Tom 个人 LinkedIn / 个人 Chrome；不把过程文件写入客户交付目录。
7. **批次可续**：对方说“下一批/继续某公司名单”时同样立刻响应，不必再请示 Tom。

## 与其他 skill 的关系

- `silent-10min-monitor`：例行巡检仍静默；本 skill 覆盖“下属主动求插件”的例外通道。
- `agent-context-window-guard`：若请求方上下文爆窗，先按该 skill 处理会话，再继续插件协助。
- `client-folder-final-files`：插件回传默认进 `/tmp` 与对话；人选初稿/终稿仍由寻访端写入客户目录。

## 不要做的

- 不要因为“怕打扰”而拖延插件协助。
- 不要在没有求助时主动轮询“还要不要我查插件”。
- 不要把插件结果直接当终稿写进客户文件夹。
- 不要编造 LinkedIn URL、学历年或语言能力。

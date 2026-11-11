# 多 Agent / 工具协作与真实执行边界

本文只记录业务协作约定。它不描述平台内部权限，也不把产品机制写成可执行 SOP。

## 角色总图（业务约定）

| 角色 | 职责 |
| --- | --- |
| Grok Bot（大总管 / Recruitment Lead） | 业务统一入口：澄清需求、派单、验收、对用户汇报 |
| Paseo | 管理本机执行端 Agent（如 Codex、Pi、谷歌反重力）；与中枢互补、不互相替代；依赖本机在线 |
| MAGPIE | 用户自述：给执行端集中挂低价/免费模型（含 DeepSeek 等）；**未做账单审计** |
| 执行端 | 寻访执行、本机/Drive/Notion 读写、部分 enrichment；由中枢经 Paseo 派单 |

队友（业务分工）：Talent Sourcer、Candidate Analyst、Contact & Outreach、BD负责人、Cooper（情报）。2026-11-08 起有 paseo-bots 五 Bot 侧栏定制记录（Drive README）。

---

## 巡视 vs 发指令

| 模式 | 做法 |
| --- | --- |
| 只读巡视 | 查看会话进展与产出；有结果再取回转交。**不**向执行端发送消息或指令（避免打断） |
| 下发指令 | 仅当用户明确给出要发送的具体指令内容 |

说明：2026-11-08 对谷歌反重力在截止前多次只读巡视；另有用户明确授权的 SwiftX 纠错指令属于「下发」而非巡视。

---

## 落地工作流说明（磨合中，非一键产品）

1. 顾问提出岗位 / 截止 / 硬条件。  
2. 大总管拆任务，经 Paseo 派执行端。  
3. 执行端按策略寻访、评分、出报告/PDF。  
4. 大总管按约定间隔只读巡视。  
5. 截止验收：合格转发；不合格如实报缺口。  
6. Pi 等可承担辅助本机任务（如临时不息屏）；失败须回报真实错误信息。

**未完成实例：** 2026-11-08 约 20:10 Asia/Shanghai，谷歌反重力 SwiftX 新人 PDF 未达可验收标准。

DeepSeek：可作为 Pi / OpenCode 背后的模型；Paseo 官方支持名单未把「DeepSeek」单列为独立原生 Agent（以当时 paseo.sh 文档为准）。用户本机 MAGPIE 配置**未在本包实测**。

---

## 常用边界

| 主题 | 业务约定 |
| --- | --- |
| LinkedIn / Chrome | 不登录用户本人 LinkedIn；不驾驶用户个人 Chrome（见 [tom-xia-linkedin-chrome-red-line](../../skills/tom-xia-linkedin-chrome-red-line/SKILL.md)） |
| 外联 | 本库记录的**默认**是先草稿、经用户批准后再发；用户可对具体任务另行明确授权 |
| 电话 | 内置助手电话不用于候选人 cold call / 商业招揽。话术供用户自拨，或供用户点名的外部授权渠道使用（见 [josh-candidate-phone-and-voicemail](../../skills/josh-candidate-phone-and-voicemail/SKILL.md)） |
| 「工具可发现」 | ≠ 账号已连接、有额度、可写 |
| Codex 额度 | 当期数字未知则不臆造 |

## 成本分工（用户自述）

用户要求中枢侧重派单与验收，重执行交给经 Paseo 的执行端及 MAGPIE 挂载模型。具体月费数字属用户自述，**非本包审计结果**。

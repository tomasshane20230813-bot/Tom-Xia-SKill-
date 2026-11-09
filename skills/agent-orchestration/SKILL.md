---
name: recruitment-multi-agent-orchestration
version: 2026-11-09
source_type: reconstructed-memory
---
# AI Agent 猎头工作编排

## 适用分工
- Recruitment Lead：拆分 JD、制定招募与 BD 优先级、核对 HR 硬条件。
- Talent Sourcer：Google X-ray、公开履历、多渠道寻访、去重。
- Candidate Analyst：基于履历/项目强证据逐人评分；Active 分独立。
- Contact & Outreach：合法富化联系渠道、检查去重/退订、个性化外联、回执验证。
- Market Intelligence：公司扩张、猎头需求、薪酬行业信号与目标企业画像。

## 调度原则
一个角色一个输出契约：输入来源、任务边界、可验证结果、截止节点、失败回报。不同 Agent 的“完成”必须由文件/链接/消息 ID/提交 SHA 证明；并行任务不可互相编造状态。

## 工具与限制
用户研究过 Codex、Manus、Paseo、Pi、WebCodex 和多个富化连接器；这些是可探索的执行通道，不代表当前 ChatGPT 可以读取它们全部本地会话或远程工作状态。不要把“一台 UI 可打开多个 Agent”误认为全部模型之间共享上下文和权限。

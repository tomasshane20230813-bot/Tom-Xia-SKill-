# 猎头寻访新玩法与实操 SOP

条目旁标注灵感扫描日 / 拍板日 / SOP 版本日。未重新打开全部外部原文时，标为「记忆/二次摘要」。

## 证据等级

- **已验证（业务内）：** 老板拍板、团队 skill 已落地、Drive/Notion 原文已读。
- **公开来源可回访：** 带精确 URL 的 ATS / 新闻 / 文档。
- **第三方方法（教程自报）：** 公开文章；未在 FORESTOWN 项目独立复跑成功前不得写成「已跑通」。
- **设想：** 灵感扫描建议，尚未立项落地。
- **未完成：** 已尝试但交付仍有缺口。

---

## A. 已拍板落地的玩法

### A1. GitHub 工作证据库寻访（技术岗 / 硅谷 AI）

| 字段 | 内容 |
| --- | --- |
| 状态 | **已验证（拍板）** — 2026-11-04 |
| 背景 | LinkedIn 公共 X-ray 弱化后，不依赖登录本人 LinkedIn |
| 方法 | GitHub 当**工作证据库**（repo / code / merged PR）；AI 写 Boolean，人做 intake 与结果判断 |
| 落地 | [github-evidence-sourcing](../../skills/github-evidence-sourcing/SKILL.md) |
| 步骤摘要 | 抽 JD 技术信号 → `pushed:>` / `merged:>` → 活跃仓 contributors/PR → 去重 → 岗位分与 Active 分拆 → 短名单后再 enrich；外联按业务默认先草稿 |
| 起步 Boolean（需按年更新） | 见 skill 原文 |
| 参考 | Full Stack Recruiter Boolean/X-ray 指南；`https://github.com/ohsusannamarie/GitHub-advanced-search` |

### A2. 岗位分与 Active 分永远分开

| 字段 | 内容 |
| --- | --- |
| 状态 | **已验证（长期规则）** |
| 规则 | 技术合适 ≠ 正在看机会；近约 90 天无第一方求职证据 → `Active未证实`，可进观察池，不得假称 Active |
| 落地 | [active-candidate-scoring](../../skills/active-candidate-scoring/SKILL.md)；Notion ACI Finder；Drive Active SOP 2026.07 |

---

## B. 灵感扫描（第三方方法，未宣称项目内跑通）

### B1. 2026-11-06 下午场（记忆摘要）

1. GitHub code search 用 `symbol:` 找定义者 + `author:` `is:merged` 验贡献 — 标注来源 HeroHunt 2026-08（第三方；本库未重抓原文 URL）。
2. AI 拓池 → 收割市场用词 → Boolean 硬卡 → 交集优先 — ZenBee 2026-09（第三方）。
3. 非技术岗改开网 X-ray（PDF 简历 / 会议嘉宾 / LI posts Active）；LinkedIn X-ray 偏雇主映射 — Work Insiders 2026-10（第三方）。

### B2. 2026-11-09 上午场（记忆摘要）

1. LinkedIn advice 页 X-ray：`site:linkedin.com/advice/ intext:"Title"` — Jan Tegze / Full Stack Recruiter（约 2026-07）；fragile，免登本人 LI。公开入口：`https://fullstackrecruiter.net/guides/boolean-and-x-ray-search-for-recruiters/`
2. 开搜前校准：market size + 1 偏高 / 1 偏低边界人 — Sengi 2026-11。公开入口：`https://sengi.ai/blog/active-sourcing-with-ai/`（2026-11-09 入库仅做链接检查，HTTP 403，正文未读；仍为第三方设想，未在项目内复跑）
3. Title Boolean 失灵时先建公司池再找人 — 同 Sengi；适 SwiftX / Yealink 利基岗。

> 对 SwiftX 的内部判断：先校准 Pickup vs Network 边界，避免混岗。**不等于**已用上述方法完成合格新人交付。

---

## C. Active 识别与评分（合辑）

完整可执行条文以 [active-candidate-scoring](../../skills/active-candidate-scoring/SKILL.md) 与 Drive《Active候选人公开网络识别与评分SOP》（2026.07）为准。摘要：

1. 事实 / 推测 / 证据不足分开写。
2. 每条 Active 信号：原文短摘、证据日期、URL、核验日期、证据类型。
3. 第一方优先；公司裁员 ≠ 本人被裁。
4. 同一行为去重；核对反向信号与时效衰减。
5. FORESTOWN 常用 Active 0–10 与岗位匹配 0–100 分列；加权如何映射 0–10 若任务未定义公式，保留原始证据与状态，不强行换算（见 Drive `knowledge/findings.md` 2026-11-08）。

---

## D. LinkedIn 线索评估统一标准 V1.0

- Notion 页（生效 2026-09-04）：`https://app.notion.com/p/3d119ef2dc37816095b8d3173f7875e2`
- LinkedIn 是线索不是完整简历；没写 ≠ 没有，标待核实。
- 两阶段：线索评分 → 核实后推荐评分。
- 客户最新硬门槛优先于通用标准；不以姓名推断语言/族裔。

---

## E. 项目口径要点（业务规则，非候选人名单）

### SwiftX

- 正确名称 **SwiftX**；业务资料在 WPS 同步目录下的「SwiftX物流」文件夹（绝对路径省略）。
- 两岗：Pickup Operations 与实体物流 Network Planning；不得未经核对把 Pickup 当成分拣岗。
- 2026-11-01 确认：保留有公开中文/普通话商务沟通证据的人选（非外貌推断）。
- 历史报告若排重未复跑、Active 证据过弱 → 不照搬旧排名。

### Yealink / DeepCtrls

- 销售岗与云运维岗标准不混用。
- Active 与岗位匹配分拆；客户歧视性口头偏好不写入自动筛选（Notion 2026-11-05 知识点页）。

### 角色分工

- Talent Sourcer：正式 Round。
- Talent Discovery：对照/补充池，避开已有库，不主动联系候选人。

---

## F. 未完成 / 失败边界

| 事项 | 状态 | 说明 |
| --- | --- | --- |
| 2026-11-08 谷歌反重力 SwiftX 新人 PDF（约 20:10 Asia/Shanghai 截止） | **未完成** | 未交出可验收的 10 名全新人选合格 PDF；缺口报告不可当作新人交付 |
| LinkedIn advice X-ray / Sengi 公司池法 | **设想未复跑** | 公开教程灵感 |
| HeroHunt `symbol:` 等 | **设想未复跑** | 灵感扫描条目 |

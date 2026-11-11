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

**扫描节奏（用户指令，2026-11-09）：** 工作日约 10:00 与 15:00 附近扫描；有够格结果则按主题并入本节并及时归档。时刻未另指定时区，沿用本库 Asia/Shanghai。本条只记录节奏，没有新建定时任务，也没有附带新的扫描结果。同步规则见 [recruitment-knowledge-github-sync](../../skills/recruitment-knowledge-github-sync/SKILL.md)。

### B1. 2026-11-06 下午场（记忆摘要）

1. GitHub code search 用 `symbol:` 找定义者 + `author:` `is:merged` 验贡献 — 标注来源 HeroHunt 2026-08（第三方；本库未重抓原文 URL）。
2. AI 拓池 → 收割市场用词 → Boolean 硬卡 → 交集优先 — ZenBee 2026-09（第三方）。
3. 非技术岗改开网 X-ray（PDF 简历 / 会议嘉宾 / LI posts Active）；LinkedIn X-ray 偏雇主映射 — Work Insiders 2026-10（第三方）。

### B2. 2026-11-09 上午场（记忆摘要）

1. LinkedIn advice 页 X-ray：`site:linkedin.com/advice/ intext:"Title"` — Jan Tegze / Full Stack Recruiter（约 2026-07）；fragile，免登本人 LI。公开入口：`https://fullstackrecruiter.net/guides/boolean-and-x-ray-search-for-recruiters/`
2. 开搜前校准：market size + 1 偏高 / 1 偏低边界人 — Sengi 2026-11。公开入口：`https://sengi.ai/blog/active-sourcing-with-ai/`（2026-11-09 入库仅做链接检查，HTTP 403，正文未读；仍为第三方设想，未在项目内复跑）
3. Title Boolean 失灵时先建公司池再找人 — 同 Sengi；适 SwiftX / Yealink 利基岗。

> 对 SwiftX 的内部判断：先校准 Pickup vs Network 边界，避免混岗。**不等于**已用上述方法完成合格新人交付。

### B3. 2026-11-09 下午场（灵感扫描；第三方方法，未宣称项目内跑通）

扫描日：2026-11-09 约 15:08 Asia/Shanghai。与上午场 B2（advice X-ray / Sengi market size / 公司池）不重复。证据等级：第三方方法（教程自报）；已打开原文核对，未在 FORESTOWN Round 独立复跑。

#### 1. 单仓贡献者 → 15–25 人可触达短名单：八刀切割法

| 字段 | 内容 |
| --- | --- |
| 出处 | Refolk, *The Contributor Sourcing Teardown*, last reviewed 2026-10-25 |
| URL | https://www.refolk.ai/guides/contributor-sourcing-teardown-ranked-slate |
| 核心 | Contributors 图最多 100 人、REST 默认只链前 500 邮箱；须 `anon=true` 或 `git shortlog -sne` 建全量作者表。删 bot 前先解析 `Co-authored-by`（Copilot agent commit 的真人在 co-author）。squash-merge 仓按 merged PR 切 casual，勿只按 commit。雇主拆分要 org membership + email domain + profile company 至少两信号一致。触达只用对方主页/个人站**自行公开**的邮箱或链接，不用 commit 邮箱。子系统 owner：CODEOWNERS / MAINTAINERS / 路径 review 量。 |
| 怎么用在我们这边 | 硅谷 AI / 技术岗已拍板用 GitHub 证据库：对目标框架仓（如客户栈依赖）跑八刀日志 → 产出 15–25 人 slate，再进 enrichment；红线仍：不登本人 LI、不发未批外联。 |

#### 2. 中等星标仓优先 + Reviewer 当 senior 信号 + ≤120 词点名 PR 外联

| 字段 | 内容 |
| --- | --- |
| 出处 | ConnectDevs, *How to Source Developers on GitHub*, published 2026-10-19 / reviewed 2026-10-25 |
| URL | https://connectdevs.com/blog/how-to-source-developers-on-github |
| 核心 | Repo-first：`topic:` + `language:` + `stars:10..500` + `pushed:>` + `archived:false`；避开超高星名仓（招聘拥堵）。看 PR reviewers，常是 senior。画像 2 分钟清单：bio/pinned/README/近一年栈/他仓 merged PR。外联：引用**一条**真实贡献，≤120 词，问小问题不约电话，一次跟进后停；联系只用公开渠道。 |
| 怎么用在我们这边 | 与 github-evidence-sourcing 互补：先中星活跃仓再挖人；Outreach 起草时强制「点名 PR/commit + 字数帽」，符合「先草稿后批」默认。 |

#### 3. Stack Overflow 用户页 X-ray：用 tag + 声誉当公开专深度信号

| 字段 | 内容 |
| --- | --- |
| 出处 | Pin, *X-Ray Search for Recruiters*（文内引用 2025 SO Survey；2026 指南语境） |
| URL | https://www.pin.com/blog/x-ray-search-recruiters/ |
| 核心 | `site:stackoverflow.com/users "java" "california"` 一类；看 top tags 与近期答题。声誉作粗质量信号，须再交叉 GitHub/公开履历；可加 `filetype:pdf "role" "skill" -jobs -template -sample` 挖公开简历（注意过期）。 |
| 怎么用在我们这边 | LinkedIn 公共 title 过滤弱化后，技术岗第二证据池；马来/新加坡华人技术岗可叠地点词再 enrichment；勿单独当 Active 证据。 |

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
| 2026-11-09 下午场：八刀切割 / 中星仓 reviewer / Stack Overflow 用户页 X-ray | **设想未复跑** | 第三方教程，见 B3；未在项目内复跑 |

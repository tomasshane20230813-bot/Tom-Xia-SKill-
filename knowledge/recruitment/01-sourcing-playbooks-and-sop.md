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

### B4. 2026-11-10 上午场（灵感扫描；第三方方法，未宣称项目内跑通）

扫描日：2026-11-10 约 10:05 Asia/Shanghai。与 B1–B3 不重复。证据等级：第三方方法（教程自报）；已打开原文核对，未在 FORESTOWN Round 独立复跑。

#### 1. Google 搜索 URL 加 `&udm=14`，切回经典 Web 结果、去掉 AI Overview

| 字段 | 内容 |
| --- | --- |
| 出处 | Refolk, *X-Ray Search in 2026: What Google Killed, What Still Works*, May 9, 2026；交叉来源 HeroHunt / Yuma Heymans, *X-Ray Search for Recruiters 2026: 50 Strings That Work*, Oct 1, 2026（文内指向 Google 帮助页的 Web 过滤器与 gHacks 对 `&udm=14` 的说明） |
| URL | https://www.refolk.ai/blog/x-ray-search-google-2026-what-still-works ；https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/ |
| 核心 | AI Overview 会把「要看的 10 个 GitHub/公开页链接」压到折页下。在 Google 搜索 URL 末尾加 `&udm=14`（或点页面上的 Web 过滤器）可强制经典网页结果。两家互证同一技巧。另：Google 于 2025-09 左右停用 `&num=100`，再加该参数仍只有约 10 条/页，不要再依赖「一页 100 人」的插件。 |
| 怎么用在我们这边 | 凡是走 Google 的开网 X-ray（GitHub、Stack Overflow、PDF、advice 页、本场 Hugging Face / Scholar / arXiv）都把 `&udm=14` 写进书签或交给执行端的搜索 URL；不登本人 LinkedIn、不改用户其他文件。立刻可试，无需新工具。 |

#### 2. Hugging Face 画像锚点 X-ray：用页面专有标签锁定 practitioner 主页

| 字段 | 内容 |
| --- | --- |
| 出处 | HeroHunt / Yuma Heymans, *X-Ray Search for Recruiters 2026: 50 Strings That Work*, String 20, Oct 1, 2026 |
| URL | https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/ |
| 核心 | 示例：`site:huggingface.co "AI & ML interests" ("speech recognition" OR "ASR")`。`AI & ML interests` 是 Hugging Face **个人主页**上的标签，用来把模型卡、数据集页从结果里挤出去。已发布的微调模型比技能标签更能证明会做。主题词按 JD 替换（如 speech / ASR、LLM、multimodal）。 |
| 怎么用在我们这边 | 硅谷 AI / 模型岗 Round：在 LinkedIn 公共 title 过滤弱化后，把 Hugging Face 当第一证据池之一；点进主页看具体模型再 enrichment、起草外联（点名某个 model/space）。找人和查重仍交给 PI / 谷歌反重力等执行端；红线：不登本人 LI。模型发布 ≠ Active。 |

#### 3. Google Scholar「Verified email at」+ 近期 arXiv `after:` 找前沿研究人选

| 字段 | 内容 |
| --- | --- |
| 出处 | 同上 HeroHunt 指南，Strings 23–25, Oct 1, 2026；文内引用 Stanford HAI *2026 AI Index Report*（2026-04；数据源 Zeki）关于瑞士、新加坡在每 10 万人口顶刊作者/发明人密度靠前 |
| URL | https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/ |
| 核心 | 学者画像：`site:scholar.google.com "Verified email at" "reinforcement learning" "robotics"`（「Verified email at」出现在已验证机构邮箱的 Scholar 画像上）。按机构域名切市场：`site:scholar.google.com "Verified email at ethz.ch" "computer vision"`，新加坡可用 `nus.edu.sg` / `ntu.edu.sg`。前沿、画像上还没写的技术：`site:arxiv.org/abs "speculative decoding" after:2026/01/01`，从近期论文作者反查当前雇主。 |
| 怎么用在我们这边 | Research Scientist / founding ML 岗先从近期论文和已验证机构邮箱起名单，再交叉公开履历与 GitHub；新加坡密度对亚太覆盖有用。执行与全量查重交给执行端。论文发表 ≠ Active，也不是公开中文证据。 |

本场刻意不收录、也不推荐：Refolk 仍写到的 `AROUND(n)`（HeroHunt 指出该算子只在 Google Vault 文档出现，网页搜索是否可用存在冲突，本轮不推）。也不因 HeroHunt 仍示范 `site:linkedin.com/in/ "title" "city"` 而重新采纳已失效的 LinkedIn 公共 title/location X-ray（与已归档的 Jan Tegze / Full Stack Recruiter 判断冲突）。

### B5. 2026-11-10 下午场（灵感扫描；第三方方法，未宣称项目内跑通）

扫描日：2026-11-10 约 15:06 Asia/Shanghai。与 B1–B4 不重复。证据等级：第三方方法（教程自报）；已打开原文核对，未在 FORESTOWN Round 独立复跑。作者自述未在登出浏览器复跑全部字符串。下列搜索串是教程原文，不是本库已跑通的结果。

#### 1. GitHub 画像锚词 `"followers" "following"` + 站内 `type:user`（language/location/created）

| 字段 | 内容 |
| --- | --- |
| 出处 | Sparsh Goyal / The Cognitive, *30 Google X-Ray Search Strings Beyond LinkedIn (2026)*, 发布 2026-10-04、更新 2026-11-04；Strings 1–5 |
| URL | https://thecognitive.io/blog/google-xray-search-recruiters |
| 核心 | Google `site:github.com` 会混进仓库/issue/文档。画像页专有词对：`site:github.com "followers" "following" ("Go" OR "Golang") "Berlin" -tutorial -awesome`，把结果压向用户主页；`-awesome` 去掉链接合集仓。位置与语言更准时改用 **GitHub 自己的用户搜索**（不是 Google）：`type:user location:berlin language:go followers:>10`（`language:` = 其拥有仓的语言）。资历代理：`type:user language:rust location:"san francisco" repos:>5 created:<2019-01-01`。GitHub Pages 简历：`site:github.io ("resume" OR "CV") "data engineer" ("Airflow" OR "dbt")`。注意：robots 挡 `/contributors` 与 `/stargazers`，别指望爬贡献者列表；AUP 禁止用 GitHub 数据做未征询邮件。 |
| 怎么用在我们这边 | 硅谷 AI/工程岗在 LinkedIn 公共 title 过滤弱化后，执行端（PI/谷歌反重力）把「Google 画像锚词串」与「GitHub 站内 type:user」当成两条并行证据车道；外联点名具体仓/语言，不登本人 LI。语言/城市按 SwiftX、Yealink、硅谷 AI JD 替换。贡献活跃 ≠ Active 看机会，也不是公开中文证据。 |

#### 2. Sessionize `intitle:"Speaker Profile"` + 全网讲者页 / PDF 讲稿

| 字段 | 内容 |
| --- | --- |
| 出处 | 同上 The Cognitive，Strings 23–25 |
| URL | https://thecognitive.io/blog/google-xray-search-recruiters |
| 核心 | 讲者池已被会议方筛过一轮。Sessionize：`site:sessionize.com intitle:"Speaker Profile" "Kubernetes" "Germany"`（页面标题固定带 Speaker Profile）。不限站点的近期讲者页：`intitle:speakers "data engineering" ("conference" OR "summit") after:2025 -jobs`。讲稿 PDF：`filetype:pdf "product management" ("keynote" OR "talk") "speaker" after:2025`（首页常有姓名与雇主）。 |
| 怎么用在我们这边 | 利基技术岗/亚太会场（新加坡、马来、香港、澳洲）先扫 Sessionize + 会后 PDF，再 enrichment；适合 Network Planning、AI infra、物流科技等公开分享多的人。执行与全量查重交给执行端。演讲 ≠ Active，公开中文证据仍单独硬卡。 |

#### 3. Kaggle 段位词（Grandmaster/Master/Expert）X-ray，并与 GitHub 交叉

| 字段 | 内容 |
| --- | --- |
| 出处 | 同上 The Cognitive，Strings 9–11；交叉 Talent Place *Where to Find AI-Native Talent Beyond LinkedIn*（2026-07-14）对 Kaggle 段位作为可验证技能信号的说明 |
| URL | https://thecognitive.io/blog/google-xray-search-recruiters ；https://talentplace.com/blog/for-recruiters/where-to-find-ai-native-talent-beyond-linkedin/ |
| 核心 | 段位词当过滤器：`site:kaggle.com ("Grandmaster" OR "Master") "London" -competitions -datasets -discussion`；或 `site:kaggle.com "Expert" "computer vision" ("Bengaluru" OR "Bangalore")`。交叉公开代码：`site:github.com "followers" "following" "kaggle.com" "Toronto"`（主页链到 Kaggle）。作者注明当日未能读 Kaggle robots.txt（有 captcha），字符串需自测。段位证明竞赛能力，不证明当前雇主或看机会。 |
| 怎么用在我们这边 | 硅谷/新加坡 Data Scientist、Applied ML Round：先按段位+主题出池，再交叉 GitHub/HF（上午场 B4），全量查重后 enrichment。找人交给执行端；红线不登本人 LI。竞赛成绩 ≠ Active，也不是中文证据。 |

本场刻意不收录：SocialTalent 仍示范失效的 LinkedIn 公共 title/location X-ray；Doximity/NPI（非我们目标市场）；Wellfound `/u/`（robots 已挡）；Meetup 需登录的会员页；Talent Place 的 Discord/Product Hunt 观察法（偏关系运营、非立刻可复用搜索串）。GitHub Acceptable Use 禁止用其数据做 spam / 未征询邮件；外联仍默认只起草、经用户批准后再发，且不从 commit 元数据捞邮。

### B6. 2026-11-11 上午场（灵感扫描；第三方方法，未宣称项目内跑通）

扫描日：2026-11-11 约 10:20 Asia/Shanghai。与 B1–B5 不重复。证据等级：第三方方法（教程自报）；所用指南已于 2026-11-10 WebFetch 全文（S17、S18），本场复核后选出此前未入库的字符串。未在 FORESTOWN Round 独立复跑。下列搜索串是教程原文，不是本库已跑通的结果。

#### 1. DEV / Medium 写作者画像 X-ray：用页面专有标签找公开写技术的人，文章当外联开场

| 字段 | 内容 |
| --- | --- |
| 出处 | Sparsh Goyal / The Cognitive, *30 Google X-Ray Search Strings Beyond LinkedIn (2026)*, 发布 2026-10-04、更新 2026-11-04，Strings 16–19；交叉 HeroHunt / Yuma Heymans, *X-Ray Search for Recruiters 2026: 50 Strings That Work*, String 19（DEV）与 String 34（Medium/Substack 写法），Oct 1, 2026 |
| URL | https://thecognitive.io/blog/google-xray-search-recruiters ；https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/ |
| 核心 | Medium 作者页在 `/@` 下：`site:medium.com/@ "staff engineer" "Kubernetes"`。带时效的主题文：`site:medium.com "engineering manager" ("hiring" OR "onboarding") "platform team" after:2025`。DEV 画像用只有主页才有的标签，把帖子挤掉：`site:dev.to "Location" "Joined" "Singapore" ("TypeScript" OR "React")`；填了雇主的人：`site:dev.to "Work" "Joined" "Rust" ("San Francisco" OR "Bay Area")`。HeroHunt 示范的锚词是 `"Joined on"`（`site:dev.to "Joined on" ("Rust" OR "WebAssembly") "Berlin"`），与 The Cognitive 的 `"Joined"` / `"Location"` / `"Work"` 不完全相同，执行时先打开 2–3 个真实 DEV 画像核对当前标签再定串。公开文章可当评估沟通能力的材料和外联第一句。 |
| 怎么用在我们这边 | 硅谷 AI / 工程岗在 LinkedIn 公共 title 过滤弱化后，把 DEV/Medium 当「会把工作写清楚」的补充池；执行端（PI / 谷歌反重力）出名单后，外联草稿点名一篇具体文章，不登本人 LI。写作 ≠ Active，也不是公开中文证据。全量查重仍交执行端。 |

#### 2. Meetup 公开活动页找组织者/讲者（不要搜需登录的会员页）

| 字段 | 内容 |
| --- | --- |
| 出处 | 同上 The Cognitive，Strings 26–27 |
| URL | https://thecognitive.io/blog/google-xray-search-recruiters |
| 核心 | Meetup 会员页检查时要登录，所以不要 X-ray 会员主页。改打公开的群组/活动页，上面会写组织者和讲者：`site:meetup.com "Python" "Singapore" ("organizer" OR "organized by")`；讲者：`site:meetup.com "Rust" "Berlin" ("speaker" OR "talk by")`。教程原话：本地技术活动组织者往往认识你想找的那一半人，即使本人不是目标人选也值得记下。记下名字后再交叉 GitHub / 公开履历。这与 B5 的 Sessionize（正式会议讲者画像）互补：一边是大会讲者，一边是本地 meetup 节点。 |
| 怎么用在我们这边 | 亿联马来/新加坡、香港、澳洲等利基市场，先扫当地 Python/云/物流科技 meetup 的组织者与活动讲者，再 enrichment。执行与全量查重交给执行端。红线：不登本人 LI，也不为了翻会员页去登录用户本人账号。组织活动 ≠ Active，公开中文证据仍单独硬卡。外联仍先起草、经批准再发。 |

#### 3. 竞招公司池：在 Greenhouse / Lever / Ashby 公开职位板上搜正在招同一画像的公司

| 字段 | 内容 |
| --- | --- |
| 出处 | HeroHunt / Yuma Heymans, *X-Ray Search for Recruiters 2026: 50 Strings That Work*, String 49, Oct 1, 2026 |
| URL | https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/ |
| 核心 | 一次搜三家常见创业公司 ATS 托管域：`(site:job-boards.greenhouse.io OR site:jobs.lever.co OR site:jobs.ashbyhq.com) "machine learning engineer" "Singapore"`。结果是正在招同一画像的在线职位，不是候选人名单。用途：看见竞争对手怎么写 JD、公开薪资/福利/技术栈，并把公司名喂回已拍板的「Title Boolean 失灵时先建公司池再找人」（B2）。职位挂很久的团队，工程师可能更累、更愿意聊。这是市场映射，不是进人。 |
| 怎么用在我们这边 | SwiftX / Yealink 利基岗和硅谷 AI 岗，Round 前用这条把「谁在抢同一类人」做成公司池，再交给执行端按公司找人并全量查重。也可给 BD 校准话术（栈、地点、职责写法）。公司在招 ≠ 池里的人 Active。不把职位页上的候选人申请数据当来源。 |

本场刻意不收录：B4 已入库的 Hugging Face / Scholar / arXiv / `&udm=14`；B5 已入库的 GitHub 画像锚词、Sessionize、Kaggle，以及已写在 B5.1 核心里的 `site:github.io` 简历串；HeroHunt 仍示范的 LinkedIn 公共 title/location X-ray；Doximity；需登录的 Meetup 会员页；Wellfound `/u/`（robots 已挡；`/p/` 路径本场未独立核验，不推荐）。GitHub AUP 禁止用其数据做未征询邮件；外联默认只起草。

### B7. 2026-11-11 下午场（灵感扫描；第三方方法，未宣称项目内跑通）

扫描日：2026-11-11 约 15:15 Asia/Shanghai。与 B1–B6 不重复。证据等级：第三方方法（教程自报）。Refolk 两篇于 2026-11-11 WebFetch 全文；HeroHunt 的 String 46 与 String 48 复用 S17（2026-11-10 已 WebFetch 全文，本场沿用），不另编号。未在 FORESTOWN Round 独立复跑。下列搜索串与节奏是教程原文，不是本库已跑通的结果。

Refolk 指数统计是供应商自报，本库未复核。包括标题所称美国软件工程师约 2,740 人里才有 1 人在标题里写 open to work（文内口径：Refolk 指数中美国 Software Engineer 353,400 人，标题含 “open to work” 的 129 人；作者注明这是标题关键词，不含平台里私密的 open-to-work 设置），以及 S21 转述 HireIndex 的「发帖人平均经验约 9 年」。2026-11-11 独立核对的只有：当月 HN 帖仍在，且帖顶版规与文章所述一致。不摘录任何发帖人姓名、邮箱、简历链接或其他个人资料。

#### 1. Hacker News 月度 “Ask HN: Who wants to be hired?”：只读，发到对方自己公开的邮箱，在下月顶替前用完

| 字段 | 内容 |
| --- | --- |
| 出处 | Refolk, *Only 1 in 2,740 US Engineers Says 'Open to Work.' Read HN Before December*, 2026-11-04（S20）。次要背景：Refolk, *HN's "Who Wants to Be Hired" Is 9-Year Seniors. Recruiters Are Banned.*, 2026-09-20（S21；只取资历与「禁令是护城河不是墙」的语境，不另立一条玩法）。上段两则指数统计均为供应商自报。 |
| URL | https://www.refolk.ai/blog/hacker-news-who-wants-to-be-hired-november-2026-sourcing ；https://www.refolk.ai/blog/hacker-news-who-wants-to-be-hired-sourcing-senior-engineers |
| 现场核对 | 2026-11-11 打开 https://news.ycombinator.com/item?id=50338726 。标题 *Ask HN: Who wants to be hired? (November 2026)*，提交者 whoishiring，页面时间戳 2026-11-02T16:01:37，扫描日相对时间为 8 days ago（约 11 月 2–3 日）。帖顶模板为 Location / Remote / Willing to relocate / Technologies / Résumé/CV / Email。帖顶原文：只有本人正在找工作才发帖（Please only post if you are personally looking for work）；Agencies, recruiters, job boards, and so on, are off topic here；读者只为讨论工作机会才去信这些地址（please only email these addresses to discuss work opportunities）。找工作者被指向 https://www.wantstobehired.com 。文章引用的配套招聘帖 https://news.ycombinator.com/item?id=50338728 同日打开，标题为 *Ask HN: Who is hiring? (November 2026)*，相对时间同为 8 days ago。文章提到的公开解析站 hnhiring.com 与 nchelluri.github.io/hnjobs 只记为文中工具，本团队未跑。不摘录帖内个人资料。 |
| 核心 | 这是少数工程师用自己的话写明要一份工作，并留下自己选择公开的联系地址的地方。十一月名单会过期：约 12 月 1 日十二月帖换上后，已入职的人很少回头改旧帖。Refolk 建议的节奏（当教程，不当本库已测 SOP）：第一周解析、核对、发第一封邮件；第二到三周跟进一次然后停；约 12 月 1 日打开新帖，再发的人视为仍在找，消失的人在下一封之前先核对。外联前打开对方链接的仓库，核对提交作者、近期活动、技术栈是否对得上，以及深度是否够所声称的级别；自称 shipped agents 的，应看得到真实框架和失败处理，而不是单层 API 包装。硬规则（帖顶 + 文章）：不要在 HN 评论树里发帖或回复，连打招呼也不要。只给对方自己公开的地址发信，且只谈一个真实岗位。不要把发帖人加进 newsletter、人才社区 drip 或自动序列。HN 读者会公开点名批量序列。S21 把「招聘方禁止在帖内发言」读成护城河而不是墙：禁的是在评论树里发，联系仍只走对方公开的邮箱。 |
| 怎么用在我们这边 | 硅谷 AI / infra / founding engineer：由执行端（PI / 谷歌反重力，不是做寻访的招聘负责人）读当月帖，按栈和地点过滤，核对 GitHub 自述，对照电脑文件夹 / Google Drive / Notion 做全量查重（只算新名字；旧人出现在新文件里不算新），再起草一封短邮件：点明当月帖、对方代码里的一个具体细节、职位名、地点或远程、薪资范围。默认只起草，用户批准后再发。本人在该帖发帖，是正在看机会的 Active 证据；它不是公开中文证据，岗位要求中文时中文证据仍单独硬卡。红线：不登录用户本人的 LinkedIn，不从 commit 元数据捞邮箱。本扫描日是 2026-11-11，十一月帖已经超过一周，约 12 月 1 日前用完，之后改看十二月帖。 |

#### 2. 高管任命新闻 X-ray（市场映射，不是找人字符串）

| 字段 | 内容 |
| --- | --- |
| 出处 | 复用 S17。HeroHunt / Yuma Heymans, *X-Ray Search for Recruiters 2026: 50 Strings That Work*, String 46，2026-10-01。2026-11-10 WebFetch 全文，2026-11-11 沿用。不另编号。 |
| URL | https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/ |
| 核心 | 教程原文，本库未跑：`("joins" OR "appointed" OR "named") "as VP of Engineering" after:2026/06/01`。职称族按岗位替换（如 VP / Head / Director of Engineering，或相关的 AI、物流领导职称）。Google 文档将 `after:` 用于该日期之后更新的页面。这条打到的是近期高管任命的新闻。文章里的两个用法：刚到任的人短期内不太会再动；刚换领导的公司往往会重组，被换下的负责人和其直接下属在随后几个月值得一聊。先用它决定往哪瞄准，再用人找字符串（LinkedIn advice X-ray、GitHub、Scholar 等）找具体的人。与 B6 第 3 条互补：Greenhouse / Lever / Ashby 竞招板是需求，这条是领导层变动。 |
| 怎么用在我们这边 | 硅谷 AI 或中国侧对外 BD 开跑前，用相关职称看谁刚加入 Dexmate / SiMa / Figure 一类公司或其同业，以及哪些团队可能在动。公司名喂回已拍板的「先公司池、再找人」（B2）。执行与全量查重仍交执行端。新闻提及 ≠ Active。外联仍先起草。不登本人 LI。 |

#### 3. 高校实验室成员页：毕业前看到博士生

| 字段 | 内容 |
| --- | --- |
| 出处 | 复用 S17，同一篇 HeroHunt 指南，String 48。 |
| URL | https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/ |
| 核心 | 教程原文：`site:edu (intitle:people OR intitle:members) "PhD student" "robot learning"`。主题按 JD 替换（robot learning、speech、computer vision 等）。`site:edu` 可换成 `site:ac.uk`、`site:ethz.ch` 等学术域；新加坡用院校域（B4 已记 Scholar 可用 `nus.edu.sg` / `ntu.edu.sg`，实验室页用同一批院校）。实验室页面会列出成员，包括临近毕业的博士生，并带导师和课题。文章把它当成入市前的预警，并建议毕业季之前的春天去看。与 B4 的 Scholar「Verified email at」加 arXiv `after:` 互补：那边是论文和已验证作者页，这边是还挂在名册上的人。 |
| 怎么用在我们这边 | 研究科学家 / founding ML / 机器人（含新加坡覆盖）：执行端先标几所目标实验室，再交叉公开履历和 GitHub，并全量查重。挂在实验室页 ≠ Active，也不是公开中文证据。外联前确认此人确实接近市场。只起草。不登本人 LI。 |

本场刻意不收录：B4 已入库的 `&udm=14`、Hugging Face、Scholar / arXiv；B5–B6 已入库的 GitHub 画像锚词、Sessionize、Kaggle、DEV / Medium、Meetup 公开活动页、Greenhouse / Lever / Ashby 竞招板。Wellfound `/p/` 在 B6 已写明未独立核验，本场仍不推荐。HeroHunt 仍示范的 LinkedIn 公共 title/location X-ray 维持不采纳。Doximity / NPI 不在目标市场。本场 X 搜索没有值得归档的从业者帖子（多为招聘广告）。

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
| 2026-11-10 上午场：`&udm=14` 经典 Web 结果 / Hugging Face 画像锚点 X-ray / Scholar「Verified email at」+ arXiv `after:` | **设想未复跑** | 第三方教程，见 B4；三条均未在 FORESTOWN 项目内复跑 |
| 2026-11-10 下午场：GitHub `"followers" "following"` + `type:user` / Sessionize `intitle:"Speaker Profile"` / Kaggle 段位词 X-ray | **设想未复跑** | 第三方教程，见 B5；三条均未在 FORESTOWN 项目内复跑 |
| 2026-11-11 上午场：DEV/Medium 写作者画像 X-ray / Meetup 公开活动页组织者与讲者 / Greenhouse·Lever·Ashby 竞招公司池 | **设想未复跑** | 第三方教程，见 B6；三条均未在 FORESTOWN 项目内复跑 |
| 2026-11-11 下午场：HN 月度 Who wants to be hired 只读发信 / 高管任命新闻 X-ray / 高校实验室成员页 | **设想未复跑** | 第三方教程，见 B7；三条均未在 FORESTOWN 项目内复跑。2026-11-11 只核对了当月 HN 帖仍在且帖顶版规与文章一致 |

# 来源索引、覆盖与缺口

## 1. 本包实际依据

| ID | 类型 | 对象 | 日期/版本 | 方式 |
| --- | --- | --- | --- | --- |
| S01 | Drive | Active SOP | 2026.07 | 已读正文 |
| S02 | Notion | ACI Finder | 约 2026-11-07 编辑 | fetch |
| S03 | Notion | LinkedIn 评估 V1.0 | 生效 2026-09-04 | fetch |
| S04 | Notion | Yealink×DeepCtrls 知识点 | 2026-11-05 | fetch |
| S05 | Notion | 全球 AI BD 库 | 说明 2026-10-07；P0 SQL | fetch+query |
| S06 | box | bd-p0-six-pack.md | Live re-check 2026-11-02 | 已读 |
| S07 | Drive | Team README / onboarding / findings | 2026-11-08 | 已读 |
| S08 | workflows | 5 个用户 skills | 导出 2026-11-09；Josh 按新约束改写 | 复制/改写 |
| S09 | Memory | 拍板、发送、红线、电话约束、灵感扫描 | 2026-10-31～11-09 | RecallMemory |
| S10 | Transcripts | Sourcer / BD 等「落成 skill」「五封发送」 | 抽样 | SearchTranscripts |
| S11 | 公开页 | 下表 URL | 以页面文内日期为准 | 自修订包收录。2026-11-09 入库只做 HTTP 状态码检查，未重读正文，不把状态码当成内容复核 |
| S12 | 用户指令 | 知识同步 skill；灵感扫描改为工作日约 10:00 与 15:00 附近，有结果再归档 | 2026-11-09 | 用户要求入仓的 SKILL.md 原文。时区未另给，沿用 Asia/Shanghai。本条没有新扫描结果 |

## 2. 公开 URL 清单（融资/招聘须可回访）

**融资/新闻（有精确 URL 才保留来源；正文不复述金额）：**

- SiMa：https://sima.ai/press-release/sima-ai-reaches-1-45b-valuation-with-500-million-in-total-funding-to-scale-physical-ai-in-humanoids-automotive-and-drones/
- EliseAI：https://techcrunch.com/2026/09/29/a16z-backed-eliseai-raises-350m-doubles-valuation-to-4b/
- Sierra：https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/
- Dexmate / NEC：https://www.nec.com/en/press/202608/global_20260825_01.html
- Dexmate / LG CNS：https://www.lgcns.com/kr/newsroom/press/detail.physicalai-2603-3
- Rogo hub：https://www.straitstimes.com/business/ai-startup-that-upends-junior-bankers-work-sets-up-in-singapore

**招聘板：**

- https://jobs.ashbyhq.com/dexmate
- https://jobs.ashbyhq.com/dexmate/da59211e-2c5e-4be8-ab10-0f68c68d90e4
- https://jobs.jobvite.com/simaai/
- https://jobs.ashbyhq.com/EliseAI
- https://jobs.ashbyhq.com/Sierra
- https://jobs.ashbyhq.com/Sierra/b514c750-efde-46ca-b9d3-6e76e64eb6c7
- https://job-boards.greenhouse.io/figureai/jobs/4698860006
- https://jobs.ashbyhq.com/Rogo/6f52a4f1-6ede-45ef-af17-16f9ee7daf77
- https://rogo.com/careers

**方法/SOP：**

- https://app.notion.com/p/40719ef2dc3781759f98e6a9b553ff7f
- https://app.notion.com/p/3d119ef2dc37816095b8d3173f7875e2
- https://app.notion.com/p/40f19ef2dc3781d1a089dd0d0e611768
- https://app.notion.com/p/875af5fced6e4616823f7055a967feaf
- https://fullstackrecruiter.net/guides/boolean-and-x-ray-search-for-recruiters/
- https://sengi.ai/blog/active-sourcing-with-ai/
- https://github.com/ohsusannamarie/GitHub-advanced-search
- https://paseo.sh/docs/supported-providers.md（以当时页面为准）
- https://www.refolk.ai/blog/x-ray-search-google-2026-what-still-works （S16；2026-11-10 WebFetch 全文）
- https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/ （S17；2026-11-10 WebFetch 全文）
- https://thecognitive.io/blog/google-xray-search-recruiters （S18；2026-11-10 WebFetch 全文）
- https://talentplace.com/blog/for-recruiters/where-to-find-ai-native-talent-beyond-linkedin/ （S19；仅 Kaggle 段位信号交叉，未整篇收为玩法）

**刻意不写金额的历史线索：** Rogo「D 轮/估值」等仅见二次摘要、无本包精确 URL，标为历史线索未再核。

有精确 URL 的 SiMa / EliseAI / Sierra 融资报道保留链接。本库正文不复述金额与估值；入库没有重读这些新闻正文。

## 2.1 入库链接检查（仅 HTTP 状态码，2026-11-09）

未下载、未摘录页面正文，因此没有新增情报。HTTP 200 只表示主机有响应：Notion 页可能仍需登录；招聘板职位可能已关闭；融资数字须回到原文核对。

| 状态码 | URL |
| --- | --- |
| 200 | https://jobs.ashbyhq.com/dexmate |
| 200 | https://jobs.ashbyhq.com/dexmate/da59211e-2c5e-4be8-ab10-0f68c68d90e4 |
| 200 | https://www.nec.com/en/press/202608/global_20260825_01.html |
| 200 | https://www.lgcns.com/kr/newsroom/press/detail.physicalai-2603-3 |
| 200 | https://sima.ai/press-release/sima-ai-reaches-1-45b-valuation-with-500-million-in-total-funding-to-scale-physical-ai-in-humanoids-automotive-and-drones/ |
| 200 | https://jobs.jobvite.com/simaai/ |
| 200 | https://techcrunch.com/2026/09/29/a16z-backed-eliseai-raises-350m-doubles-valuation-to-4b/ |
| 200 | https://jobs.ashbyhq.com/EliseAI |
| 200 | https://job-boards.greenhouse.io/figureai/jobs/4698860006 |
| 200 | https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/ |
| 200 | https://jobs.ashbyhq.com/Sierra |
| 200 | https://jobs.ashbyhq.com/Sierra/b514c750-efde-46ca-b9d3-6e76e64eb6c7 |
| 200 | https://www.straitstimes.com/business/ai-startup-that-upends-junior-bankers-work-sets-up-in-singapore |
| 200 | https://jobs.ashbyhq.com/Rogo/6f52a4f1-6ede-45ef-af17-16f9ee7daf77 |
| 200 | https://rogo.com/careers |
| 200 | https://app.notion.com/p/40719ef2dc3781759f98e6a9b553ff7f |
| 200 | https://app.notion.com/p/3d119ef2dc37816095b8d3173f7875e2 |
| 200 | https://app.notion.com/p/40f19ef2dc3781d1a089dd0d0e611768 |
| 200 | https://app.notion.com/p/875af5fced6e4616823f7055a967feaf |
| 200 | https://fullstackrecruiter.net/guides/boolean-and-x-ray-search-for-recruiters/ |
| 403 | https://sengi.ai/blog/active-sourcing-with-ai/ |
| 200 | https://github.com/ohsusannamarie/GitHub-advanced-search |
| 200 | https://paseo.sh/docs/supported-providers.md |
| 200 | https://aci-finder-tomxia.tom-xia.chatgpt.site/ |

Sengi 为 403：该灵感条目维持「设想 / 第三方」，本轮未读到文章。Paseo 支持名单页返回 200，正文未读，因此「DeepSeek 未被单列为原生 Agent」仍是修订包的文档级结论，本轮未复核。

## 3. Skills 导出检查

| Skill | 是否全文 | 备注 |
| --- | --- | --- |
| active-candidate-scoring | 是 | 历史明确「已落成长期 skill」。Drive 文件 id 已从公开文本移除，仍指向 SOP 标题与 Notion ACI Finder |
| github-evidence-sourcing | 是 | 2026-11-04 拍板后默认执行 |
| tom-xia-linkedin-chrome-red-line | 是 | 红线广播明确引用 |
| josh-candidate-phone-and-voicemail | 是（改写） | 内置电话不做候选人 cold call / 商业招揽；脚本供用户自拨或点名的外部授权渠道 |
| getting-started | 是 | 模板工作流 |
| recruitment-knowledge-github-sync | 是 | 2026-11-09 用户追加的长期同步指令原文；无邮箱、电话、凭据 |
| 供应商 skills | 否 | 仅 04 列名 |

未导出任何 prompt / 隐藏指令 / 系统提示。

## 4. 覆盖

已覆盖窗口约 **2026-10-31 至 2026-11-10** 已取到的材料：GitHub 证据库玩法；灵感扫描 B1（2026-11-06 下午）、B2（2026-11-09 上午）、B3（2026-11-09 约 15:08 下午；第三方教程，未在项目内复跑）、B4（2026-11-10 约 10:05 上午；第三方教程，两篇均于 2026-11-10 WebFetch 全文，未在项目内复跑）、B5（2026-11-10 约 15:06 下午；第三方教程，The Cognitive 于 2026-11-10 WebFetch 全文，Talent Place 仅作 Kaggle 段位交叉说明，未在项目内复跑）；Active + LI SOP；P0 六家带 URL 的信号与发送/未发送；多 Agent 业务边界；2026-11-08 反重力未完成验收；5 个用户 skills 原文；电话与外联默认表述。这不是全历史穷尽。

## 5. 缺口

- 部分外部灵感文章（HeroHunt / ZenBee / Work Insiders）无精确文章 URL，仅留来源名与月份。
- Sengi 页面入库时 HTTP 403，正文缺失。
- 新闻与 SOP 正文未在入库时重读；融资具体数字除 URL 本身外不在正文复述，无 URL 者不写金额。
- 大总管主会话部分 transcript 检索为空；Notion agent sessions 需更高权益，未查。少数主聊天历史因此缺失。
- 候选人库、denylist、合同正文、私邮表、凭据、工作邮箱和电话故意不收录。
- Codex 当期额度未知。
- 供应商 / 托管 skill 只保留名称索引，不复制内部手册或系统指令。
- 归档目标就是当前仓库。修订包里「尚未写入 Git」的句子到此失效。
- 2026-11-09 下午场三条（Refolk / ConnectDevs / Pin，见文末追加来源 S13–S15）为第三方教程：Refolk 与 ConnectDevs 按 WebFetch 全文归档，Pin 按搜索摘要加页面要点归档；均未在 FORESTOWN Round 独立复跑。
- 2026-11-10 上午场两条（Refolk *X-Ray Search in 2026*，2026-05-09；HeroHunt / Yuma Heymans *50 Strings*，2026-10-01；见文末 S16–S17）已于 2026-11-10 用 WebFetch 打开全文并写入精确 URL，不再属于「无精确 URL」类缺口。证据等级仍是第三方教程，未在 FORESTOWN Round 独立复跑。B1 所记 HeroHunt 2026-08 `symbol:`、ZenBee、Work Insiders 仍无精确文章 URL。本轮未重跑 2026-11-09 融资/招聘板 HTTP 链接检查。
- 2026-11-10 下午场（The Cognitive *30 Google X-Ray Search Strings Beyond LinkedIn*，发布 2026-10-04、更新 2026-11-04；见文末 S18）已于 2026-11-10 用 WebFetch 打开全文并写入精确 URL。可选交叉 S19（Talent Place *Where to Find AI-Native Talent Beyond LinkedIn*，2026-07-14）仅作 Kaggle 段位信号说明，未整篇收为玩法。证据等级仍是第三方教程：作者自述未在登出浏览器复跑全部字符串，本库也未在 FORESTOWN Round 独立复跑这些搜索串。本轮未重跑 2026-11-09 融资/招聘板 HTTP 链接检查。

## 追加来源（2026-11-09 下午场灵感扫描）

| ID | 类型 | 对象 | 日期 | 方式 |
| --- | --- | --- | --- | --- |
| S13 | 公开指南 | Refolk Contributor Sourcing Teardown | last reviewed 2026-10-25；扫描 2026-11-09 | WebFetch 全文 |
| S14 | 公开指南 | ConnectDevs How to Source Developers on GitHub | published 2026-10-19 / reviewed 2026-10-25；扫描 2026-11-09 | WebFetch 全文 |
| S15 | 公开指南 | Pin X-Ray Search for Recruiters | 2026 指南语境；扫描 2026-11-09 | WebSearch 摘要 + 页面要点；未宣称独立复跑 |

URL：
- https://www.refolk.ai/guides/contributor-sourcing-teardown-ranked-slate
- https://connectdevs.com/blog/how-to-source-developers-on-github
- https://www.pin.com/blog/x-ray-search-recruiters/

证据等级：第三方方法（教程自报）。不复制凭证、候选人资料或供应商内部手册。

## 追加来源（2026-11-10 上午场灵感扫描）

| ID | 类型 | 对象 | 日期 | 方式 |
| --- | --- | --- | --- | --- |
| S16 | 公开指南 | Refolk, X-Ray Search in 2026: What Google Killed, What Still Works | 2026-05-09；扫描 2026-11-10 | WebFetch 全文 |
| S17 | 公开指南 | HeroHunt / Yuma Heymans, X-Ray Search for Recruiters 2026: 50 Strings That Work | 2026-10-01；扫描 2026-11-10 | WebFetch 全文 |

URL：
- https://www.refolk.ai/blog/x-ray-search-google-2026-what-still-works
- https://www.herohunt.ai/blog/x-ray-search-for-recruiters-2026-50-strings-that-work/

两篇均于 2026-11-10 WebFetch 全文。证据等级：第三方方法（教程自报），未在 FORESTOWN Round 独立复跑。不复制凭证、候选人资料或供应商内部手册。本轮不推荐 `AROUND(n)`，也不重新采纳已失效的 LinkedIn 公共 title/location X-ray。

## 追加来源（2026-11-10 下午场灵感扫描）

| ID | 类型 | 对象 | 日期 | 方式 |
| --- | --- | --- | --- | --- |
| S18 | 公开指南 | Sparsh Goyal / The Cognitive, 30 Google X-Ray Search Strings Beyond LinkedIn (2026) | 发布 2026-10-04、更新 2026-11-04；扫描 2026-11-10 | WebFetch 全文 |
| S19 | 公开指南 | Talent Place, Where to Find AI-Native Talent Beyond LinkedIn | 2026-07-14；扫描 2026-11-10 | 仅作 Kaggle 段位信号交叉说明，未整篇收为玩法 |

URL：
- https://thecognitive.io/blog/google-xray-search-recruiters
- https://talentplace.com/blog/for-recruiters/where-to-find-ai-native-talent-beyond-linkedin/

S18 于 2026-11-10 WebFetch 全文。S19 未整篇收为玩法，只交叉说明 Kaggle 段位可作为可验证技能信号。证据等级：第三方方法（教程自报）。作者自述未在登出浏览器复跑全部字符串；本库未在 FORESTOWN Round 独立复跑。不复制凭证、候选人资料或供应商内部手册。本场不收录 SocialTalent 仍示范的失效 LinkedIn 公共 title/location X-ray、Doximity/NPI、Wellfound `/u/`、需登录的 Meetup 会员页，以及 Talent Place 的 Discord/Product Hunt 观察法。GitHub AUP 禁止用其数据做未征询邮件。

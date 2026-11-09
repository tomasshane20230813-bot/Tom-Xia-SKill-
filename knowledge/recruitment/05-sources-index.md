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
| 供应商 skills | 否 | 仅 04 列名 |

未导出任何 prompt / 隐藏指令 / 系统提示。

## 4. 覆盖

已覆盖窗口约 **2026-10-31 至 2026-11-09** 已取到的材料：GitHub 证据库玩法；两场灵感扫描（标设想）；Active + LI SOP；P0 六家带 URL 的信号与发送/未发送；多 Agent 业务边界；2026-11-08 反重力未完成验收；5 个用户 skills 原文；电话与外联默认表述。这不是全历史穷尽。

## 5. 缺口

- 部分外部灵感文章（HeroHunt / ZenBee / Work Insiders）无精确文章 URL，仅留来源名与月份。
- Sengi 页面入库时 HTTP 403，正文缺失。
- 新闻与 SOP 正文未在入库时重读；融资具体数字除 URL 本身外不在正文复述，无 URL 者不写金额。
- 大总管主会话部分 transcript 检索为空；Notion agent sessions 需更高权益，未查。少数主聊天历史因此缺失。
- 候选人库、denylist、合同正文、私邮表、凭据、工作邮箱和电话故意不收录。
- Codex 当期额度未知。
- 供应商 / 托管 skill 只保留名称索引，不复制内部手册或系统指令。
- 归档目标就是当前仓库。修订包里「尚未写入 Git」的句子到此失效。

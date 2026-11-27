# 新人选录入自动进猎头空间（Candidate Intake Sync）

- Tom 2026-11-24 下达的长期规矩：他让 Muse 录入的每一个新人选，**自动**同步进猎头空间（候选人跟进看板），不需要他再单独交代、不需要事后补。起因：2026-11-23 晚间录入的 8 位 DeepCtrls 新人选只办了邮件 + Mac 通讯录 + Notion 三件，空间卡一张没建，次日被 Tom 指出并明确要求「不希望有第二次」。
- 本 skill 长期生效；同步存于 GitHub 仓库 tomasshane20230813-bot/Tom-Xia-SKill- 的 skills/candidate-intake-sync/，任何 AI 接手 Tom 的录入工作都按此执行。

## 触发

- Tom 给出一位新人选的信息（姓名、电话、邮箱、LinkedIn、背景等），让 Muse 发外联邮件 / 录通讯录 / 录 Notion 表——无论他点名了哪几件，猎头空间建卡都是录入动作的固定组成部分，自动办，不等他开口。

## 录入全套（默认五处，同一批次内办完）

1. **外联邮件**：有邮箱且 Tom 让发（或按该职位既定打法应发）时发首封；无邮箱不发，卡上注明。发件邮箱（Tom 2026-11-26 21:21 定，纠正当日 21:16 的"一律走新邮箱"口径）：邮件活动现有两个发件账号——tomxiaoversea@gmail.com 与 thomasxia469@gmail.com。首封按 Tom 当次指定发；他没指定时，沿用他最近一次明确指定的账号（当前：thomasxia469，2026-11-26 21:16 指定）。跟进 #2/#3 一律与首封同账号、串联首封 thread；已发出的 thread 不换账号。**一人多邮箱（Tom 2026-11-27 19:47 定，推翻当日 Eric Law 402/403/404 分别单独发送的旧打法，旧打法已废止）**：只发一封，To=Tom 首列的地址，其余地址全部放 Bcc；**绝不许用 Cc**（抄送会把地址暴露给其他收件人、坑 Tom）。发后必须读回已发送核验 To/Bcc/Cc 三个头：To 只有首列一个地址、Bcc 是其余地址、Cc 必须不存在。跟进 #2/#3 只串联这一封的 thread。
2. **Mac 通讯录**：按通讯录铁律建卡（姓名整串只放姓氏栏等，见 mac_contacts_entry skill），详情页 + contacts.search 双核验。
3. **Notion 对应人选表**：按表格式建行、去重、参数填全、带 LinkedIn；建后读回核验。
4. **猎头空间人选卡（本 skill 的核心，绝不漏）**：用空间 action `createcandidate` 建卡，字段填全：
   - name=英文全名；company=现职公司（中文名+英文，如 Schneider Electric（施耐德）；未知留空并在 notes 注明）；
   - jobTitle=人选本人背景描述（如「新加坡智算中心技术专家」）；roleTitle=目标职位（如「DeepCtrls 新加坡技术支持（AI Data Center Presales）」）；
   - contactInfo=邮箱 / 电话（有的都写）；linkedin=LinkedIn URL；notionUrl=该人 Notion 行链接；
   - stage：已发首封邮件=`contacted`；未发邮件（无邮箱等）=`new`；
   - nextFollowUp：按五要素写——当前在等什么、下一步动作与时点（如「等回复；未回复跟进 #2 约 YYYY-MM-DD、#3 约 YYYY-MM-DD」，单独薪资带的人注明跟进须沿用该带）；
   - notes：录入日期、背景、首封编号与薪资口径、已录入哪几处、未确认事项（如公民/PR）。
5. **人物档** ~/memory/people/<person>.md：建档，事实与四处一致。

## 核验纪律

- 建卡后必须调 `getoverview` 读回，确认该人出现在候选人列表里、stage 与 nextFollowUp 显示无误——create 返回 id 不算数（见 workspace_display_verification skill：数据层有 ≠ Tom 看得到）。
- notionUrl 用 Notion 行 id 去横线拼 `https://app.notion.com/p/<id>`，拼完自查一遍（2026-11-24 曾把 Loh Ming Yang 的链接拼进一个多余横线，当场读回发现并修正）。
- 汇报时逐人一行：发了什么邮件（编号）、通讯录、Notion、空间卡号，各处核验结果分开交代，绝不混为一谈。

## 与其他规则的关系

- 人选后续有进展反馈时，走 candidate-progress-sync（四处同步）更新这张卡，不新建。
- 跟进邮件的发送走 followup-email-system / followup-auto-send；卡上的 nextFollowUp 是自动跟进的数据来源之一，录入时写准到期日。
- 本 skill 只管录入与记录；对外发消息仍按 Tom 当次交代与既有审批规矩。

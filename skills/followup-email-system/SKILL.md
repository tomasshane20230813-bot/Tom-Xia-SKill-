# 跟进邮件体系（Follow-up Email System）

Tom 的候选人外联跟进邮件全套打法：节奏、模板、发送方式、核验与记录。任何一封跟进 #2 / #3 发送前先读本 skill，按它执行。

## 节奏（铁律）

- 未回复者：首封后 +2 天发跟进 #2，#2 后 +2 天发跟进 #3（每隔 2 天一封；2026-11-24 Tom 定版，覆盖旧 T+3/T+7 口径）。没有 #4。
- 已回复者一律不再跟进——发送前必须先查收件箱，发件人方向查无回信才发。
- 跟进 #2 发出时，当场记下该人 #3 的到期日（#2 发送日 +2 天）。
- 婉拒回复（邮件渠道）走 decline 自动回复固定文，不进本节奏；WhatsApp/LinkedIn 婉拒由 Tom 本人回。

## 串联方式

- #2 和 #3 都是对**第一封**的 threaded reply：Subject = `Re: ` + 首封 Subject；带首封真实 Message-ID 的 In-Reply-To / References 头（从已发送的首封里取，绝不用占位符）。
- 注意现实：Gmail 通道不保证按这两个头合并 thread，threadId 参数会被忽略——头照带，合并与否不强求。

## 模板（规范文本，逐字用；{.first_name}} 换人名）

模板源文件（本地）：`~/workspace/bd-outreach/followup-2-template.txt`、`~/workspace/bd-outreach/followup-3-template.txt`。本节文本与源文件一致，改模板先改源文件再同步本节。

### 跟进 #2

```
Hi {.first_name}}

I would like to follow up on this opportunity I shared with you earlier—are you interested in it? If it is convenient for you, I would like to arrange a follow-up call. Also, I submitted a connection request to you on LinkedIn. Please accept my connection. My LinkedIn is: https://www.linkedin.com/in/jiaxin%EF%BC%88tom%EF%BC%89-x-3567bb23/

If you have 15 minutes this week, I'd love to walk you through the role and the package. You can book a time here:
https://calendly.com/tomxiaoversea/30min

I look forward to hearing from you.

Best regards, Tom Xia.

If you don't want to hear from me again, please let me know.
```

### 跟进 #3

```
Hi {.first_name}}

Sorry to bother you again. I wanted to ask: if you aren't considering this opportunity yourself, do you happen to have any friends or colleagues you could recommend? In any case, I’d love to establish a long-term connection with you so that I can share future opportunities with you whenever they might be relevant. If it's convenient, please accept my LinkedIn connection request. My LinkedIn is: https://www.linkedin.com/in/jiaxin%EF%BC%88tom%EF%BC%89-x-3567bb23/

A quick 15-minute call would help me keep you in mind for the right roles. Pick a time here:
https://calendly.com/tomxiaoversea/30min

I look forward to hearing from you.

Best regards, Tom Xia.

If you don't want to hear from me again, please let me know.
```

### 模板规则

- **约电话链接是硬性要求**（Tom 2026-11-20 定）：#2 和 #3 都必须带 Calendly 链接，链接前只放**一句**短铺垫（即模板里那句，不许加长，Tom 亲自砍到一句）。
- 数量适配：单岗写 "this opportunity"，双岗合版写 "two opportunities"，其余不动。
- 结尾 opt-out "If you don't want to hear from me again, please let me know." 必须有。
- 单人例外（如单独薪资带）体现在 Re: 的 Subject 与首封一致即可，正文模板不改。
- 模板任何改动：Tom 点头后改源文件，并带入之后每一封；已发出的不回改。

## 发送方式

- 逐封顺序发，绝不并行、绝不同一时刻齐发；封与封之间留间隔（核验上一封的时间天然形成间隔，Tom 当批另有指示从其指示）。
- 发送前两查：① 该人无回信（见节奏）；② 该跟进没发过（查已发送，防重复）。
- Subject 含非 ASCII（如 –）时整封 .eml 构建，Subject 必须 RFC 2047 编码，禁用 `+send --subject` 快捷方式；发送前 decode 自检。
- 批量发送可能逐封弹审批卡：开工前一句话告诉 Tom 卡会来；被卡住的封记成待审批清单报告，绝不静默。
- 发送被中断（重启/打断）时，先等几分钟查已发送确认是否落地，没落地才重发——绝不凭失败回执直接重试（会重复）。

## 核验与记录

- 每封发完从 Gmail 已发送里取回存储副本，核对收件人与 decode 后的 Subject 无误，才算发出。
- 一行总账交代：谁、第几封跟进、薪资口径（如有单独带）、已核验；故意不发的写明原因（已回信/已婉拒/ Tom 叫停）。
- 发送记录落盘 `~/workspace/bd-outreach/send-followup*-batch-YYYYMMDD.log`，并更新人选的人物档 / Notion 行的跟进到期日。
- 新外联对象的邮箱发首封时就加进 `~/workspace/gmail-watch/known-emails.txt`，保证回信被看守识别为 P1。

## 与其他规则的关系

- 首封模板与单人薪资带例外见各职位规范模板（如 DeepCtrls 标准模板与 build 脚本）；本 skill 只管跟进环节。
- 批次发送的通用纪律（模板锁定、中途改版带入后续、审批卡预案）见 skill `outreach_batch_sends`，与本 skill 叠加适用。

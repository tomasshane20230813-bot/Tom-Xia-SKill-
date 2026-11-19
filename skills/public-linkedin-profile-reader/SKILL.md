---
name: public-linkedin-profile-reader
description: Read a public LinkedIn /in/ profile without logging in and without Google Chrome. Use when a LinkedIn profile URL is already known and the public resume, location, languages, experience, or education must be checked. Do not use for LinkedIn login, Recruiter, InMail, or private account activity.
version: 2026-11-11
source_type: observed-working-method
---

# 公开领英档案读取

已验证能打开公开履历的方法是 Jina Reader，不是浏览器登录。2026-11-11 的成功样本把 `https://r.jina.ai/http://au.linkedin.com/in/<slug>` 读成 Markdown，最终地址仍停在 `/in/`，标题是“姓名 - 公司 | LinkedIn”。同一批里，直接打开领英或遇到 `authwall`、`Sign Up | LinkedIn`、`error 999` 时，页面不是履历。

## 先做

1. 只接受检索原文里出现的 `linkedin.com/in/` 或 `linkedin.com/pub/` URL。不拼、不猜 slug。
2. 运行 `scripts/read_public_profile.py <url>`。脚本不带 cookie，不打开 Chrome，不提交登录表单。
3. 先看脚本给出的 `status`：
   - `public`：可以用可见字段。
   - `authwall`、`blocked`、`empty`：停止。字段写“未显示”。不要登录，不要换 Chrome，不要把搜索摘要补成履历。

## 怎么用结果

- 地点、公司、语言等级、证书、学历年份，只采用页面上没有被星号遮住的文字。
- `****` 遮住的职位、日期不要还原。
- 搜索摘要只能证明“这个 URL 被公开索引到”，不能代替档案正文。
- Active 看机会先按 `linkedin-activity-as-active`：近 90 天可核验的领英公开活动就记为 active看机会，并写上证据类型和日期。没有这类证据时写未证实。页面上没有 Open to work 原文时，不要编这句原文。
- 不根据姓名判断族裔、国籍或语言。语言只认 Languages 栏或正文里的文字。

## 不要做

- 不登录任何人的 LinkedIn，不使用本机 Google Chrome。
- 不把登录墙、验证码或 999 错误说成“市场上没有这个人”。
- 不连续重试同一个被挡住的 URL。换一个已确认的公开 URL，或停止并报告障碍。

## 调用顺序

拿到 LinkedIn 个人 URL 后，先运行本 skill 的脚本自己查看公开履历。公开可见且没有星号遮挡的字段可以直接用。

一旦出现登录墙，立刻改走 `linkedin-loginwall-plugin-read`：把这条已确认的 URL 同时交给大总管和 PI+，用已连接招聘插件读详细履历。登录墙包括 `authwall`、`blocked`、`empty`、`Join to view`，以及脚本虽返回 `public` 但职位或职责被星号、`undefined` 挡住。不要重试同一条 URL，不要登录，不要等 Tom 点许可，也不要把搜索摘要补成履历。

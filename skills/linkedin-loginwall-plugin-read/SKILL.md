---
name: linkedin-loginwall-plugin-read
description: 领英个人页出现登录墙、星号遮挡或只有标题没有职责时，立刻把已确认的 linkedin.com/in/ URL 交给大总管和 PI+，用已连接招聘插件读详细履历。不要登录、不要空等、不要把搜索摘要写成履历。
version: 2026-11-19
source_type: tom-operating-rule
---

# 登录墙：交给大总管和 PI+ 用插件读履历

Tom 于 2026-11-19 定死。公开领英读不到职责时，不要停在登录墙前发呆，也不要每次重新摸索。调用本 skill，把已经确认的 URL 交给有插件的大总管和 PI+。

## 什么算登录墙

先按 `public-linkedin-profile-reader` 读一次公开页。下面任一情况都算登录墙，不必再重试同一条 URL：

- 脚本返回 `authwall`、`blocked` 或 `empty`
- 页面是 `Join to view`、`Sign Up | LinkedIn`、`View full experience` 或 `error 999`
- 脚本状态虽是 `public`，但职位、日期或职责是星号、`undefined`，或只剩公司名
- 搜索摘要只有姓名、公司和截断 About，没有逐岗职责

没被遮住的地点、公司、学历和 About 原文可以留下。星号后面的职位和日期不要还原。搜索摘要不能补成履历。

## 立刻发给谁

同一条请求同时发给两个人：

1. 大总管：当前负责调度全体 Agent 的会话。
2. PI+：同一寻访任务里正在跑的 PI+ 会话。

用 `paseo agent ls` 找还活着的会话，不要写死旧 ID。本机 `~/.local/bin/paseo` 若是断链，改用 `/Applications/Paseo.app/Contents/Resources/bin/paseo`。

```bash
paseo send --behavior steer --no-wait <agent-id> --prompt-file /tmp/loginwall-plugin-read.txt
```

对方正在干活就用 `steer`，不要 `interrupt`。其中一个会话已关闭，就发给还活着的那个，并写明另一个不可用。不要等 Tom 点许可。

## 消息里写什么

只放检索原文里已经出现的 `linkedin.com/in/` 或 `linkedin.com/pub/`。不拼、不猜 slug。

每条 URL 写上公开页已经看见的姓名、地点、公司，以及挡住了什么。请对方用已连接插件读详细履历，一个失败就换下一个：LinkedIn、ZoomInfo、Lusha、FullEnrich、Clay、Apollo、The Org、Vibe、SignalHire、DataForB2B、RocketReach。返回 402 或限流的插件不要重打。

只要这些字段：现职职称、公司、个人 Base、逐段任职起止、本人职责原文、学历与专业、这个 URL 是不是本人。插件日志放 `/tmp`，再 steer 回请求方。

## 不要做

- 不登录任何人的 LinkedIn，不用个人 Chrome，不碰未授权的 SunBrowser / ACI。
- 不导出邮箱、电话或其他联系方式。只取职业字段，联系方式字段丢弃。
- 不把公司 JD、新闻通稿或第三方产品介绍写成本人职责。
- 不把登录墙说成这个人不存在。
- 插件结果没回来之前不评分。初稿可以先写未评分和已请求插件，另存客户目录；不要空等截止时间。

## 和别的 skill

- `public-linkedin-profile-reader`：先读公开可见字段。
- `subordinate-plugin-assist-on-request`：大总管收到本请求后必须马上查，不要等 Tom。
- `resume-assessment-by-title-and-duties`：插件回了职位加职责，再打分。

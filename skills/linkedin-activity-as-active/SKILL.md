---
name: linkedin-activity-as-active
description: Check whether a known LinkedIn profile URL shows public activity in the last 90 days without logging in or using Tom's Chrome. Use when sourcing or reviewing candidates and Tom's rule applies: verified recent LinkedIn activity counts as active看机会. Do not use for LinkedIn login, private browsing signals, or inventing dates.
version: 2026-11-11
source_type: tom-operating-rule
---

# 领英近 90 天活动 = active看机会

Tom 在 2026-11-11 定下的口径，以后找人默认执行。这是操作规则，不是把活动说成 Open to Work 原文。

## 核心规则

近 30 天、60 天，最多不超过 90 天，只要领英上能核到这个人的公开活动，就按 **active看机会** 记录。活动包括本人发帖、评论、点赞或反应、带日期的资料更新，以及免登录监测返回的 7/30/90 天活动标记。不管他有没有写 Open to work，也不管他是在找工作还是只在浏览。

岗位匹配分仍然单独打，不用活动分代替胜任力。

没有核到活动时写「未证实」，分数记 0。不要因为在职就写 6.5 或 6.8。

## 怎么记

有证据时：

- 30 天内：active看机会 = 是，Active 分 7/10。
- 31–90 天：active看机会 = 是，Active 分 6/10。
- 超过 90 天，或日期算不出来：不按这条规则判看机会。

每条都要写下证据类型、原始日期、抓取日期和 URL。活动不是 Open to Work 时，不要引用一句不存在的求职原文。

## 不登录时按这个顺序查

只接受检索原文里已经出现的 `linkedin.com/in/` URL。不拼 slug。不登录 Tom 的 LinkedIn，不用 Tom 的 Google Chrome，不提交 cookie。

1. 用公开客态页看活动区。地址是 `https://r.jina.ai/http://www.linkedin.com/in/<slug>`。遇到 `authwall`、`blocked`、`error 999` 就停，不重试，不把空白写成不活跃。
2. 活动链接里的数字用 `scripts/activity_time.py <activity_id>` 换算 UTC 时间。只在结果是合理日期时采用。
3. 公开搜索里，只有能对上这个 URL、并且日期属于本人帖子或本人互动的摘要才算。同一段文字出现在多个无关档案上，不算。
4. 环境里已经有 LinkedPulse 或 Apify，并且不需要领英 cookie 时，可以用个人 URL 查。LinkedPulse 返回 `active_7d`、`active_30d`、`active_90d` 时，按对应窗口记。它不说明具体是哪一天、哪条评论或哪次资料修改，报告里要写明这点。
5. 没有这些接口时，写「未调用付费监测」，不要假装跑过。

可用的公开接口名称，供有权限时调用，不是已经测过的合格名单：

- LinkedPulse：https://www.linkedpulse.ai/ ，输入个人 URL，不需要登录。
- Apify `cornersight/linkedin-profile-posts`、`arisma_tech/linkedin-profile-posts-scraper`：公开帖、发布日期、点赞评论转发计数。私密档案会跳过。
- Apify `oday/mawsool-linkedin-profile-activity`、`apimaestro/linkedin-profile-comments`：自称可返回点赞和评论。社区 Actor，失败就停。

## 不算

- 绿点、正在浏览、谁看过主页、搜索出现次数。这些要登录，看不到就写看不到，不要判成不活跃。
- GitHub、Hugging Face、X 或其他网站的活动。不能用领英 URL 直接对上，也不能当成领英活动。
- 别人的求职帖、招聘广告、点赞别人的 Open to Work。
- 超过 90 天的旧帖。

## 和旧口径的关系

旧的 Active SOP 把单次点赞、普通发帖当成弱证据。Tom 这条新口径覆盖领英近 90 天公开活动：只要日期核得上，就记 active看机会。旧 SOP 里的 Open to Work、裁员声明、GitHub Available for hire 仍然是更强的原文，可以一并记录，但不能用来否定已经核到的近 90 天领英活动。

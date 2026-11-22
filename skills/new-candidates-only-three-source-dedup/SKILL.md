---
name: new-candidates-only-three-source-dedup
description: Tom 的寻访目标人数只认新人。本机、Google Drive、Notion 任一处出现过的人都是旧人，保留标注但不计入目标人数。每次寻访任务开跑、送初稿、出终稿时都调用，不用 Tom 再宣导。
version: 2026-11-22
source_type: tom-operating-rule
---

# 目标人数只认新人：本机、Google Drive、Notion 三处查重

Tom 于 2026-11-22 定死，长期有效。Tom 说“找 40 个人”这类目标人数时，计入的每一个人都必须是新人。

## 什么算旧人

下面三处任一处出现过，就是旧人：

1. Tom 这台电脑：客户目录、`wps云同步文档`、各职位 CV 文件夹、历史初稿和终稿、推荐报告、简历、`/tmp` 排除名单。
2. Tom 的 Google Drive：本机同步目录 `~/Library/CloudStorage/GoogleDrive-*`，以及 Google Drive 插件搜索结果。
3. Tom 的 Notion：候选人库、Ongoing、职位页面等，用 Notion 插件按姓名和 slug 搜索。

比对顺序：先 LinkedIn `/in/` slug 精确比对，再用“姓名 + 公司”辅助。同名不同 slug 不算重复，但要写明“同名待核”。

## 旧人怎么处理

- 保留在初稿和终稿里，不删人，不删旧稿（与 `keep-duplicate-candidates` 一致）。
- 本人信息第一行写：`重复：是｜来源：本机/Google Drive/Notion + 具体文件或页面｜slug：xxx`。
- 不计入目标人数，不能拿来凑数，也不能因为“分数高”就算进去。
- 已出推荐报告、已面试的人，一律算旧人。

## 新人怎么写

每个计入目标人数的人都要写：

`查重：本机 否｜Drive 否｜Notion 否`

下属 Agent 查不了 Drive 或 Notion 时，写 `Drive/Notion 待 CEO 核`。终审方（CEO）出终稿前必须把三处查完，没查完的人不能算新人。

## 每次任务怎么执行

1. 开跑：调度方把本 skill 发给所有下属 Agent，并建好本机排除名单（slug 集合）。
2. 初稿：下属按本机排除名单先查，新人写三处查重结果或“待 CEO 核”。
3. 终审：CEO 对所有拟计入的人跑 Google Drive 和 Notion 搜索，命中的改标旧人并移出计数。
4. 汇报：分开报“新人达标数”和“旧人（标注保留）数”，目标缺口只按新人算。

## 不要做

- 不要只查本机就宣称“全部是新人”。
- 不要删除旧人或旧稿来让比例好看。
- 不要把同一任务当天已收录的人当成“历史旧人”重复扣掉；当天续收录写“当日续收录”，只计一次。
- 不要编造查重来源或页面名。

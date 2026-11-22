---
name: final-review-score-all-drafts-pdf
description: CEO 或任何终审方出终稿时，必须把 Tom 指定客户目录里所有初稿出现过的每一位人选，按该职位评分口径逐人打推荐评估得分，写明分项依据，按分数由高到低排序，生成一份终稿 PDF 存回同一目录。不能只把初稿打回去就不评估。每次终审、收口、出终稿都调用。
version: 2026-11-22
source_type: tom-operating-rule
---

# 终审必须全员评分并出 PDF

Tom 于 2026-11-22 定死，长期有效，所有职位通用。

## 核心原则

终审不是只挑错、打回初稿。终审方必须亲自给每个人打分：

1. 收齐 Tom 指定客户目录里本次任务的全部初稿（含各 Agent、各批次、各时分版本），一个都不漏。
2. 合并清洗：按 LinkedIn `/in/` slug 去重，同一人只留一条；保留所有旧稿文件，不删、不覆盖。
3. 每一位人选都要有终审推荐评估得分。下属初稿没打分、只写“待核”或分数有误，终审方都必须自己补评或重算，不能把空白分数交给 Tom。
4. 评分口径用该职位的策略和 CoreSkill（例如 J11648 八维 100 分），不另造标准。每个分项都写依据：引用履历原文、职称、任职起止、学历、证书或插件来源。没证据的分项记 0 并写“待核”，不抬分、不拍脑门。
5. 需要补证的登录墙 URL，终审方自己调用已连接插件（ZoomInfo、FullEnrich、Clay 经大总管、Lusha 等）读职业字段，不取邮箱电话。
6. 按推荐评估得分由高到低排序，生成一份终稿 PDF，存回 Tom 指定的同一客户目录。文件名带日期和时分。

## 每个人在 PDF 里必须有

- 排名、姓名、正确的 LinkedIn URL，统一写成 `https://www.linkedin.com/in/slug`，可点击；URL 必须来自原文或插件返回，不能猜。
- 现职、公司、个人 Base、学历与毕业年。
- 推荐评估得分，以及每个分项的分数和依据。
- 硬门槛结果，例如华人姓名、性别依据、毕业年、地点、关键技能是否证实；不过线的写“不计入”和原因。
- 查重结果：新人写 `查重：本机 否｜Drive 否｜Notion 否`；旧人写 `重复：是｜来源｜slug`，保留在表中但不计入目标人数（见 `new-candidates-only-three-source-dedup`）。
- Active 看机会单列 0–10 分，附证据类型、原始日期、抓取日期和 URL；未证实写“0｜未证实”。Active 不影响推荐分。

## PDF 开头必须写

- 真实达标人数和目标缺口，例如“≥70 共 X 人，65–69 共 Y 人，目标 40，缺口 Z”。
- 评分口径说明、数据来源、未能核实的范围。
- 不抬分、不凑数；达标不够就如实写缺口。

## 禁止

- 只写“初稿打回、计入 0”就交差，不给每个人打分。
- 只汇总下属分数而不核对加总、不补未评分的人。
- 因不合格把人从终稿删掉。
- 把审核意见写进客户目录的初稿文件；审核意见放对话或 `/tmp`，终稿 PDF 是唯一写入客户目录的终审产物。

## 相关 skill

`client-folder-final-files`、`keep-duplicate-candidates`、`new-candidates-only-three-source-dedup`、`resume-assessment-by-title-and-duties`、`linkedin-loginwall-plugin-read`、`linkedin-activity-as-active`、`tom-redlines-and-bottomlines`。

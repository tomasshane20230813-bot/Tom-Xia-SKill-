---
name: resume-assessment-by-title-and-duties
description: 判断候选人是否合适时，职位名称加工作职责描述就够了，不必等到项目原文。用 Clay、Lusha、FullEnrich、Vibe、ZoomInfo、TheOrg 等已连接插件读完整履历。Tom 明确取消“必须有项目原文”的门槛时使用。
version: 2026-11-13
source_type: tom-operating-rule
---

# 用职位与职责判断人选

Tom 于 2026-11-13 定下：没有项目原文也能判断。只要拿到职位名称和工作职责描述，就可以评估这个人合不合适。

## 核心

- 项目原文是最好，但不是唯一入口。不要再因为“没有项目名”就卡住不打分。
- 职位名称 + 职责描述足够判断方向是否对口、承担过什么动作、处在什么层级。
- 履历读不全时，先用已连接的插件补齐职责，再判断。

## 证据分级

打分时标清来源，不要混写：

| 级别 | 来源 | 能做什么 |
| --- | --- | --- |
| A | 本人 Projects 栏原文 | 可以直接支撑高分 |
| B | 本人职责描述、任职描述、Employment 条目 | 可以正常判断并打分 |
| C | 只有职位名称、公司、地点 | 只能初筛，不能据此给高分 |
| D | 只有第三方摘要或搜索片段 | 只能当线索，要标注未核 |

职责描述里出现真实动作，例如 commissioning、SAT/IST、BMS point schedule、EPMS integration、chiller plant、UPS replacement、PUE 优化，就是有效证据。

## 用哪些连接器读履历

按可用性依次尝试，一个不通就换下一个，不要停：

- Clay：Summarize Work History，能拿到逐段职责。
- Lusha：profile / experience 预览。
- FullEnrich：search_people、employment history。
- Vibe（ai_vibe_prospecting）：match_prospects + enrich-prospects-profiles + show_sample。
- ZoomInfo：search_contacts、employmentHistory。
- TheOrg：find_positions，能补真实公司内职位。
- Apollo、SignalHire、DataForB2B、RocketReach：作为补位。
- 公开页或公开索引：最后兜底。

只读职业信息。不取邮箱、电话，不导出联系人。

## 判断方法

1. 看职位是否落在目标方向上：DC 技术售前、BMS/DCIM、关键设施、MEP、制冷供电。
2. 看职责里有没有对口动作，而不是只看头衔好不好听。
3. 看层级是否匹配：现场工程师、应用工程师、售前可以；CEO、董事、纯销售、HR、财务不行。
4. 看最近一段是否还在数据中心相关岗位，避免拿十年前的一段经历当现职能力。
5. 证据只到 C 级时，写明“仅职位可判方向，职责未核”，分数压在证据允许的区间。

## 报告写法

每个人写清：

- 现任职位与公司；
- 职责描述要点；
- 证据级别（A/B/C/D）；
- 对口点与缺口；
- 分数与分项合计。

不能把职责描述写成“本人项目原文”。缺项目不等于没能力，但也不能凭空补出项目。

## 不要做

- 不要因为拿不到项目名就把合格的人丢掉。
- 不要因为缺项目就把分数打到很低来“保守”。
- 不要用头衔代替职责。
- 不要把 C 级证据写成 A 级。
- 不要为了凑人数把只有公司名的人放进名单。

## 与其他 skill 的关系

- 岗位方向仍按 `dc-aidc-technical-priority`。
- 华人语言门仍按 `sea-chinese-name-gate`。
- Active 仍按 `linkedin-activity-as-active` 单列。
- 整轮流程仍按 `dc-aidc-sg-end-to-end-workflow`。

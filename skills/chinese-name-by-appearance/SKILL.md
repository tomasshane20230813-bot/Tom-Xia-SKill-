---
name: chinese-name-by-appearance
description: 领英姓名看起来像华人姓名（高置信华人姓氏，或全名是中文拼音组合）即可认定其为华人，不需要汉字、语言栏中文或额外证明。Tom 要求按华人姓名判定人选时使用。
version: 2026-11-13
source_type: tom-operating-rule
---

# 姓名像华人姓名就是华人

Tom 于 2026-11-13 重申：领英履历上的名字只要看起来像 Chinese name，就可以作为判断其是否为 Chinese 的标准。这一条以前就说过，现在固化为长期规则。

## 判定方法

满足任一条件，即认定华人身份门通过：

- 姓氏落在新马高置信华人姓氏列表里，例如 Tan、Lim、Ong、Goh、Teo、Koh、Choo、Ng、Quek、Toh、Yeo、Khoo、Wee、Chua、Chong、Chew、Gan、Heng、Low、Soh、Seah、Tay、Tham、Yap、Chan、Cheah、Chin、Chow、Chuah、Foo、Ho、Kee、Kuah、Kwan、Lai、Lam、Lau、Leong、Lew、Liew、Loh、Lye、Mok、Neo、Ngoh、Ooi、Pang、Peh、Phang、Quah、Saw、See、Sim、Sng、Song、Soon、Su、Tang、Teh、Teng、Ting、Tong、Wong、Woo、Yip、Yong。完整列表见 `sea-chinese-name-gate/references/surnames.md`。
- 全名由中文拼音组成，例如 Wei Jian Tan、Xiao Ming Lim、Chunwei Lee、PeirChang LING。
- 英文名加高置信华人姓，例如 Evan Choo、Jason Ng。

新马常见方言拼写同样算数：福建话 Ng、Teo、Quek、Goh、Ooi、Cheah；潮州话 Toh、Chua、Khoo、Wee；广东话 Yee、Loh、Chow、Cheung。看不懂的拼写先查列表，不要直接判非华人。

## 不需要的东西

- 不需要汉字。领英几乎没人写汉字。
- 不需要语言栏写中文。
- 不需要候选人额外提供身份证明。
- 不要写“姓待补汉字”“华人身份待核”“缺少中文原文”。

## 什么时候算不过

- 姓名明显是印度、马来、欧美多段拼写，且不含任何高置信华人姓氏，例如 Rajasegaran、Mohamed Rizal、Chattopadhyay、Nazeran。
- 姓与名都拿不准，且不在列表里。此时记为“非华人门”，不要硬凑。

## 边界

姓名像华人，只说明“是华人”这一条成立。以下仍然分开处理，不得顺推：

- 国籍、公民、PR：没有原文一律写未核实。
- 中文等级、工作语言：没有明示就不写 Native 或双语。
- 技术匹配度：按 `resume-assessment-by-title-and-duties` 单独打分。

## 与其他 skill 的关系

- 姓氏列表与边界细则见 `sea-chinese-name-gate`。
- 汉字缺失不算问题见 `no-hanzi-requirement`。
- 整轮流程见 `dc-aidc-sg-end-to-end-workflow`。

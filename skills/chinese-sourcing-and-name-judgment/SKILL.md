---
name: chinese-sourcing-and-name-judgment
description: 全球寻访华人人选与从领英姓名侧面判断华人的长期核心技能。凡 Tom 要求寻找华人人选时，大总管与各执行 Agent 必须从永久 Memory 调出本 Skill，作为评价人选是否为华人的重要标准。
version: 2026-11-24
source_type: tom-operating-rule
---

# 华人寻访与姓名侧面判定核心技能（长期永久规则）

## 生效依据与强制调用规则（2026-11-24 Tom 重申并固化）
- 整合固化 `chinese-name-by-appearance`（2026-11-13）、`sea-chinese-name-gate`（2026-11-12）、`no-hanzi-requirement`（2026-11-13）、`no-chinese-language-score`（2026-11-15）、`recruiting-score-normalization`（2026-11-15），并于 **2026-11-24 由 Tom 正式固化为全局长期核心 Skill**。
- **强制调用触发器**：今后只要 Tom 提出“找华人 / 要华人 / 华人人选 / 侧重华人背景”需求（不限新加坡、马来西亚、东南亚、澳洲、北美、欧洲或港澳台），**大总管必须第一时间从个人永久 Memory 调出本 Skill**，将其作为评价人选是否为华人的核心标准，并同步下发给执行端（OpenMausBot 团队与 Paseo MAUS/PI+/CEO）。

---

## 一、如何寻访华人（Sourcing 实操方法）

1. **关键词与姓氏组合检索**
   - 在已授权插件（Clay、Lusha、FullEnrich、SignalHire、RocketReach、ZoomInfo、Apollo 等）、公开 Google X-ray 及 AdsPower-SunBrowser ACI Finder 中，除目标岗位/行业/竞品公司词外，可叠加高置信华人姓氏集群检索：
     - **新马/港台方言姓**：`Tan OR Lim OR Ong OR Goh OR Teo OR Koh OR Choo OR Ng OR Wong OR Chan OR Chew OR Chua OR Chong OR Yeo OR Yong OR Ho OR Low OR Khoo OR Wee OR Ooi OR Lai OR Lam OR Lau OR Leong OR Liew OR Loh OR Seah OR Sim OR Soh OR Tay OR Toh OR Yap OR Yeoh OR Cheung`
     - **普通话拼音姓**：`Wang OR Zhang OR Chen OR Liu OR Huang OR Wu OR Zhou OR Xu OR Lin OR Yang OR Li OR Zhao OR Sun OR Ma OR Zhu OR Hu OR Guo OR Gao OR Luo OR Zheng OR Liang OR Xie OR Song OR Tang OR Han OR Feng OR Deng OR Cao OR Peng OR Xiao OR Tian OR Pan OR Yuan OR Cai OR Jiang OR Yu`
2. **禁止把“汉字”或“语言栏中文”当过滤前置条件**
   - 绝大多数海外华人领英档案不写汉字，且语言栏常留空或只写 English；**绝不能因缺汉字或语言栏无 Chinese/Mandarin 就在寻访阶段过滤掉合格华人**。
3. **辅助侧面寻访线索（可选加分/补充发现）**
   - 大中华区（中国大陆/港澳台）高校或新马华文源流学校背景、中文社团、曾就职中资/大中华区企业经历，可与姓氏规则交叉扩大召回池。
4. **合规与展示红线**
   - 严禁登录用户 LinkedIn、严禁使用 Google Chrome；所有初稿与终稿必须明文高亮展示完整可点击 `https://www.linkedin.com/in/<slug>`，零邮箱零手机号（除非该轮外联明确授权）。

---

## 二、如何从名字侧面判断华人（核心判定标准）

满足以下**任一条件**，即认定**华人身份门通过**（完整姓氏词库见 `references/surnames.md`）：

1. **高置信华人姓氏（含普通话拼音姓与新马/港台/粤闽潮客方言拼写）**
   - 如 `Tan、Lim、Ong、Goh、Teo、Koh、Choo、Ng、Quek、Toh、Yeo、Khoo、Wee、Chua、Chong、Chew、Gan、Heng、Low、Soh、Seah、Tay、Tham、Yap、Chan、Cheah、Chin、Chow、Chuah、Foo、Ho、Kee、Kuah、Kwan、Lai、Lam、Lau、Leong、Lew、Liew、Loh、Lye、Mok、Neo、Ngoh、Ooi、Pang、Peh、Phang、Quah、Saw、See、Sim、Sng、Song、Soon、Su、Tang、Teh、Teng、Ting、Tong、Wong、Woo、Yip、Yong、Cheung` 等。
   - **方言拼写同效**：福建话 `Ng、Teo、Quek、Goh、Ooi、Cheah`；潮州话 `Toh、Chua、Khoo、Wee`；广东话 `Yee、Loh、Chow、Cheung、Leung` 均视为高置信华人姓。
2. **全名由中文拼音组成**
   - 例如：`Wei Jian Tan`、`Xiao Ming Lim`、`Chunwei Lee`、`PeirChang LING`、`Yifeng Xu`、`Zhiyong Lin`。
3. **英文名 + 高置信华人姓**
   - 例如：`Evan Choo`、`Jason Ng`、`Marcus Tan`、`Kerry Wang`、`Kelvin Ong`。
   - 注：在新加坡/马来西亚/东南亚地区，英文名 + 普通话拼音姓（如 `Jason Chen`、`Kevin Zhang`、`Eric Lin`）直接通过；在欧美/澳洲等非东南亚地区，若姓氏为单音节易撞拼写姓（如 `Lee`、`Li`、`Han`、`Yu`、`Ho`），建议结合名是否中文拼音、或履历中是否有中文/华人学校/中资经历复核；若姓氏本身为典型中文拼音或方言姓（如 `Zhang`、`Chen`、`Wang`、`Liu`、`Choo`、`Tan`、`Lim`、`Ong`、`Cheung`、`Wong`），即足以侧面认定华人。
4. **档案自带汉字姓名或本人写明华人/中文母语**
   - 有则更稳，无则完全不影响通过。

### `Lee` / `Li` 与易混淆外裔姓氏边界
- **`Lee` / `Li`**：在新马/东南亚/港澳台档案中直接自动通过；在欧美澳档案中，需配合汉字、中文拼音名（如 `Chunwei Lee`、`Ming Li`）或大中华区背景佐证。
- **不自动通过（非华人门）**：
  - 越南姓：`Nguyen`、`Pham`、`Tran`、`Le`、`Hoang`、`Vu`
  - 韩国姓：`Kim`、`Park`、`Choi`、`Jung`、`Kang`、`Cho`、`Yoon`、`Jang`（以及带明显韩语名字的 `Lee`/`Lim`/`Han`）
  - 印度/南亚/马来/欧美姓：`Singh`、`Kumar`、`Patel`、`Rajasegaran`、`Chattopadhyay`、`Mohamed Rizal`、`Nazeran`、`Smith`、`Nicholls`
  - 姓与名均拿不准且不在高置信列表内：标注「非华人门 / 姓氏不足以确认」，绝不硬凑。

---

## 三、绝不要求与绝不误扣的项目

1. **绝不要求汉字**：领英不写汉字是常态；禁止写「姓待补汉字」「华人身份待核」「缺少中文原文」，禁止因缺汉字扣分或标存疑。
2. **绝不设中文语言打分（除非客户/HR 该岗位明文强制中文口语）**：
   - `chinese-name-language-full-score` 自 2026-11-15 起永久作废。
   - 默认不设中文语言分（不给 0 分、不给 5 分、不给 15 分满分），删去语言维后其余职业维度按原权重等比例放大至 100 分（`raw * 100 / W`）。
   - 仅当某个具体客户/HR 在该职位明确硬性要求普通话口语/工作语言（例如特定中企出海岗位）时，才按该项目单独口径加核语言能力，且同样不以“缺汉字”否定华人身份。
3. **报告标准写法**：
   - 通过：`华人姓氏门通过（姓名侧面判定华人）`
   - 不通过：`非华人门（姓名不像华人 / 姓氏不足以确认）`

---

## 四、严格边界（只判“是否华人”，绝不顺推四件事）

1. **不顺推国籍/公民/PR/签证**：姓名像华人 ≠ 新加坡公民/PR/澳洲公民/美国绿卡；没有原文证明一律写「国籍/PR/工作权未核实」。
2. **不代替岗位匹配分**：没有项目要求的真实技术/业务/职责证据，不能因为姓名是华人就放到 ≥65 或 ≥70 分。
3. **不代替 Active 分**：Active 仍按 0–10 独立单列，有近 90 天公开领英动态或 ACI Finder 实证才计分。
4. **不代替三源查重**：本机、Google Drive、Notion 历史出现过的人选仍按重复规则标注，不得跳过查重。

---

## 五、关联技能索引
- `chinese-name-by-appearance`（领英姓名像华人即认定）
- `sea-chinese-name-gate`（东南亚华人姓氏门及方言姓全表）
- `no-hanzi-requirement`（取消汉字门槛）
- `no-chinese-language-score`（取消中文语言分）
- `recruiting-score-normalization`（去语言项后百分制等比归一化）

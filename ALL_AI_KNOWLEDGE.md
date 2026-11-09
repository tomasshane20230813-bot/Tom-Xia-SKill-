# Tom Xia — Universal AI Headhunter Knowledge Pack

> Public, cross-AI, vendor-neutral Markdown. Version 2026-11-09. Source fidelity: partial original-source extraction + reconstructed non-sensitive SOPs, **not** all ChatGPT internal memory.

Canonical GitHub repository: https://github.com/tomasshane20230813-bot/Tom-Xia-SKill-

Read `AGENTS.md` for strict operating conventions. Existing `skills/virtual-resume-probe/`, `playbook/`, `bd/` are not duplicated in this collection.

## Knowledge and Skills


---

## File: `chatgpt-knowledge-20261109/README.md`

# Tom Xia Global Headhunter Playbook — 跨 AI 通用招聘知识备份

- **整理日期：** 2026-11-09
- **目标仓库：** `tomasshane20230813-bot/Tom-Xia-SKill-`
- **本文件夹用于 Public 仓库**：只包含通用招聘方法论、公开可复用的流程框架，以及去标识化的行业知识。
- **数据类型：** 从可访问原始 SOP、可读取的长期知识摘要、既往对话线索整理。完整原文与重建摘要分别标注。
- **并非 ChatGPT 全量记忆导出**：系统没有提供将所有内部长期记忆逐字导出的入口。不能获取的原始附件、聊天全文、第三方 Marketplace Skill 原码没有冒充已备份。
- **已有 GitHub 内容保持不覆盖**：仓库原有 `skills/virtual-resume-probe/`、`bd/` 和 `playbook/` 已存在；此文件夹应作为新增补丁导入。

## 目录

| 文件 | 用途 | 来源类型 |
|---|---|---|
| `skills/active-candidate-evidence/SKILL.md` | Active 求职信号验证与时效衰减 | 已获取用户原始 SOP 的 Markdown 重建 |
| `skills/xray-sourcing/SKILL.md` | 不依赖 LinkedIn Recruiter 的人才公开寻访 | 长期知识重建 |
| `skills/candidate-evaluation/SKILL.md` | 匹配打分、证据、风险与推荐结论 | 长期知识重建 |
| `skills/enrichment-dedup-outreach/SKILL.md` | 合规富化、去重和触达 | 长期知识重建 |
| `skills/recruiter-report/SKILL.md` | Forestown 推荐报告结构 | 长期知识重建 |
| `skills/hr-intake/SKILL.md` | 新项目 HR 立项必问问题 | 长期知识重建 |
| `skills/transcription-qa/SKILL.md` | 录音转写与幻觉核验 | 长期知识重建 |
| `skills/bd-market-signals/SKILL.md` | 全球猎头客户开发和招聘信号 | 长期知识重建 |
| `skills/agent-orchestration/SKILL.md` | 多 AI Agent 招聘流程编排 | 长期知识重建 |
| `knowledge/industry-frameworks.md` | 物流、电子分销、机器人、云/DC、楼宇工业 | 长期知识重建 |
| `knowledge/tool-map.md` | 工具职责和使用边界 | 长期知识重建 |
| `knowledge/provenance-and-gaps.md` | 原文、摘要、缺失项与保护边界 | 核实后的清单 |

## 使用习惯
- 新的 HR 书面答复覆盖旧版口径，所有硬性条件记录出处及更新日期。
- 岗位适配评分与 Active 看机会评分独立；未验证不等于不符合。
- 候选人评分必须有证据来源、日期、疑点与后续核实动作。
- 不上传候选人私人邮箱、电话号码、简历全文、客户未公开报价、合同内部条款或任何凭证。


---

## File: `chatgpt-knowledge-20261109/skills/active-candidate-evidence/SKILL.md`

# Active 候选人公开网络识别与评分 SOP

> **来源：用户上传原始 DOCX 内容提取，2026-07 版本。** 表格转写为 Markdown，原文条款由 Word 中读取；格式可能与原文件不同。

猎头实战操作手册
Active 候选人公开网络识别与评分 SOP
不依赖 LinkedIn Recruiter 的公开网络发现方法
适用场景
美国及欧美 AI / 机器人 / 电子工程 / PCB / 供应链 / 物流等中高端人才寻访
版本：2026.07　｜　用途：猎头顾问、Sourcer、Researcher、招聘经理内部执行
## 1. 使用边界与判断纪律
## 1.1 三类结论必须分开写
## 1.2 五条执行纪律
职位匹配分和 Active 分分别计算、分别呈现；任何一方不得替代另一方。
每个 Active 信号必须记录原文摘要、证据日期、链接、抓取日期和证据类型。
只使用公开职业信息、候选人自愿公开信息和用户已有合法数据；不猜测私人邮箱、手机号或私信内容。
不为了验证邮箱而发送测试邮件；退信只能来自真实业务发送记录或用户已有状态字段。
出现“刚入职、晋升、开始实习”等反向信号时，必须降低评级，不能沿用旧求职证据。
## 2. 原有 Active 信号框架
## 2.1 强证据：可以优先联系
本人明确公开求职：Open to Work；本人发帖寻找新机会；写出 actively seeking、exploring new opportunities、available immediately；明确目标岗位、地点、签证或到岗时间。
最近公开发布或更新简历：最近 3 个月在个人网站、GitHub、公开简历平台或学校网站发布/更新简历；文件名含近期年份；新增 Resume、CV、Hire Me、Available for Work 页面。
在相近招聘信息下明确表达兴趣：公开留言 “I’m interested / I’ll be applying / I have applied / Could we discuss this role? / Please check your DM”等。此类主动表达显著强于点赞。
本人公开表示被裁、合同结束或已离职：如 position eliminated、impacted by layoffs、contract ended、last day、Career Break、Seeking Opportunities。
已有合法数据中企业邮箱失效且履历同步变化：只能来自真实退信或用户已有 invalid/bounced 状态；必须再核对职位结束、公开离职或求职行为，不能单独认定被裁。
## 2.2 中等证据：需要组合使用
当前为 Freelance / Contractor / Self-employed，并同时出现“available for projects”、简历更新、招聘帖互动等。
30–90 天内多次、连续、跨公司互动与履历高度匹配的招聘内容；单次点赞不足。
公开与 Recruiter 多次讨论职位、公开感谢、询问岗位、回复“已发送简历/已申请”。不得推断私人连接或私信。
公司或部门近期裁员，同时出现职位结束、公开声明、求职互动、已有邮箱失效等个人层面的信号。
履历近期异常变化：公司消失、结束月份更新、转为独立顾问、新增 Career Break、About 改为目标职位与可提供技能。
GitHub 或个人网站出现求职导向更新：新增 Resume/Portfolio/Hire Me、README 表态求职、更新地点和联系方式。普通提交、Star、Fork 不算。
## 2.3 弱证据：只能进入观察池
只点赞一条招聘信息、只关注一名 Recruiter、只转发或点赞别人的 Open to Work。
公司发生裁员，但没有任何个人层面证据。
近期有社交活动，但内容与求职无关；更新技能、证书或普通技术项目。
Self-employed，但从未公开表示接受机会。
长期以前的求职帖或旧简历，近期无更新；公开网络无法可靠看到的登录/浏览频率。
## 2.4 必须排除的误判
## 3. 不依赖 LinkedIn Recruiter 的 Active 人选发现渠道
## 3.1 GitHub：技术人才的第一方求职痕迹
GitHub 个人资料提供 “Available for hire” 状态；这是候选人主动设置的直接职业信号。单独出现可计 +4。
个人 Profile README、仓库 README 或个人主页出现 looking for work、open to opportunities、hire me、available for full-time/contract 等，可计 +4；若与 Available for hire 同时出现，可计 +5。
最近 90 天新增 Resume/CV、更新地点/联系方式、集中整理目标职位相关项目，可作为 +2 辅助证据。
普通 commit、Star、Fork、Issue 活动只证明技术活跃，不证明求职，计 0。
## 3.2 Hacker News：Who wants to be hired?
每月 “Who wants to be hired?” 线程中，候选人主动发布技能、地点、远程偏好和联系方式；当前月可计 +5。
31–90 天的帖子仍较强，可计 +4；3–6 个月需结合新证据。
记录原帖时间、候选人自述、联系方式来源；联系前检查当月线程关于第三方 Recruiter 的规则。
## 3.3 Reddit：公开 [For Hire] 与行业求职帖
搜索 [For Hire]、looking for work、available immediately、seeking opportunities，并限定目标行业、地点和时间。
候选人本人在 30 天内发 [For Hire] 且岗位匹配，可计 +5；31–90 天计 +4。
必须区分本人求职、替朋友转发、接零散项目与寻找全职工作的不同意图。
## 3.4 Wellfound：创业与科技人才的求职状态
Ready to Interview 属于强信号，可计 +5；Open to Offers 可计 +4。
适合 AI、机器人、软件、硬件创业公司人才；同时核对最近活跃、目标岗位、地点、薪资和签证。
## 3.5 Cord：英美科技人才的主动可联系流
候选人进入 active talent stream，通常意味着近期愿意与招聘方沟通，可计 +5。
更适合英国/欧洲及部分美国科技岗位；记录平台状态日期，不要把长期静态档案视为当前 Active。
## 3.6 裁员人才名单与 opt-in talent lists
优先使用由候选人主动加入、允许被雇主/猎头联系的公开人才名单，例如 Parachute。主动 opt-in 可计 +5。
WARN、新闻或公司裁员名单只说明风险，不能证明具体个人求职；只有公司层面信息时计 +1 至 +2。
## 3.7 简历库与职位平台的“近期活动”字段
## 3.8 行业协会、简历库与职业活动
## 4. Google / Bing X-Ray 搜索手册
## 4.1 搜索式调优方法
先用 1 个职位族 + 1 个求职短语 + 1 个地点，不要一次塞入全部技能。
结果过多时增加 site:、filetype:pdf、after:YYYY-MM-DD、精确短语和排除词（如 -jobs -hiring）。
结果过少时去掉地点或年份，替换同义词：seeking / available / open / exploring / hire me。
为同一职位建立 3 组词：岗位名称、核心技能、行业/产品词；轮换组合，避免只命中标准职位标题。
把网页发布日期和候选人自述日期分开记录；页面更新时间不一定等于求职状态更新时间。
## 5. 合并后的 Active 评分卡
## 5.1 评级阈值
## 5.2 反向信号与扣分建议
## 6. 证据时效与衰减
## 7. 单个人选的执行流程
先做职位匹配：按技能、行业、资历、地点、签证、薪资和到岗要求记录匹配与缺口。此步骤不评 Active。
再做 Active 搜索：从强信号渠道开始——GitHub/HN/Reddit/Wellfound/Cord/opt-in 名单/近期简历库。
打开原始页面：保存原文摘要、发布日期、URL、抓取日期；搜索摘要不作为最终证据。
交叉核对反向信号：最近入职、晋升、已关闭求职状态、帖子过期、地点或签证不符。
按评分卡计算：同一行为去重，区分个人层面与公司层面，写清推测。
输出评级和联系建议：高概率/中高/观察池/证据不足，并写明下一步要验证的问题。
## 7.1 质检清单
□ Active 评分是否与职位匹配评分分开？
□ 每个加分项是否有候选人本人或平台状态的原始链接？
□ 是否记录证据日期和抓取日期？
□ 是否把同一行为重复计分？
□ 是否误把他人求职、公司招聘或普通专业互动当成本人求职？
□ 是否核对了新入职、晋升等反向信号？
□ 联系方式是否公开、可核验、与本人一致？
□ 最终结论是否标注“事实 / 推测 / 证据不足”？
## 8. 标准人选记录模板
## 8.1 推荐的最终结论写法
附录 A：来源与核验链接
以下链接用于验证方法、字段或渠道。实际人选判断仍应以候选人原始页面、状态日期和当期平台说明为准。
GitHub Docs — Set your hiring status
Boolean Strings — Tech Sourcers, Watch GitHub Profile READMEs
RecruitingDaily — How to Source Developers on Reddit
Hacker News / Algolia Search
Parachute — Opt-in layoff talent list
Wellfound Help — Job search visibility/status
Wellfound Curated
Cord — Create an active talent stream
Dice — Search and activity fields
Dice — Find candidates
Indeed — AI-powered Smart Sourcing
Indeed — Looking for employees / resume caveat
Monster — Resume Search
ZipRecruiter — Resume Database
Reed UK — Recruiter Help
CV-Library — Search CVs
LoopCV — Candidate Database
SMTA — Career Center
IEEE Robotics & Automation — Resume Bank
IEEE Career Fair
ASCM — Career Resources / Job Board
CSCMP — Employer Career Center
RecruitingDaily — Building with the site: command
附录 B：联系前的最小核验问题
您目前是否愿意了解全职、合同制或顾问机会？优先级分别如何？
您希望的岗位方向、行业、地点/远程安排是什么？
如果岗位合适，最早何时可以开始面试和到岗？
是否存在签证、搬迁、出差频率或保密竞业方面的限制？
您近期公开求职状态是否仍有效？是否已经进入其他公司的后期流程？
最终标准：宁可少发，也不能把普通点赞、他人的求职动态、公司裁员新闻或普通技术活动包装成“本人正在找工作”。

### 附表 1
| 核心原则  Active 判断必须与职位匹配分开。技术合适不等于正在看机会；只有可核验、带日期的求职行为或近期活动，才能支持 Active 结论。 |
| --- |

### 附表 2
| 先说结论  本手册不把 LinkedIn Recruiter 当作前提，也不把平台推荐、连接关系或不可见私信当作证据。方法集中于候选人主动留下的公开求职痕迹、公开简历、技术社区、人才库、行业协会、招聘活动和用户已有合法数据。 |
| --- |

### 附表 3
| 结论类别 | 定义 | 允许写法 | 禁止写法 |
| --- | --- | --- | --- |
| 确认事实 | 有公开原文、日期和可回访链接 | “候选人于 7 月 10 日在 HN 发布求职信息” | “他肯定急着跳槽” |
| 合理推测 | 两个以上中等信号组合，仍有不确定性 | “近期合同状态 + 多次职位互动，可能开放机会” | 把推测包装为本人表态 |
| 证据不足 | 只有弱信号或信息已过期 | “暂列观察池，需电话核实” | “公司裁员，所以本人已被裁” |

### 附表 4
| 误判 | 正确核对方式 |
| --- | --- |
| 把别人的求职帖当成本人求职 | 检查第一人称原文、发布者身份和上下文；帮助朋友传播不等于本人 Active。 |
| 把招聘方当候选人 | 员工、Hiring Manager、Recruiter 转发本公司职位通常是在招人。 |
| 把公司裁员等同个人被裁 | 核对部门、职位时间线、本人声明及个人求职行为。 |
| 忽略已入职/晋升 | 如近期宣布新工作、晋升或实习，应降低 Active 评级。 |
| 使用过期证据 | 一年前的求职帖在已入职后不再代表当前状态。 |
| 把专业兴趣当求职 | 技术、PCB、电源、物流或供应链内容互动只能证明专业方向。 |

### 附表 5
| 优先顺序  先找候选人主动进入“可被招聘”状态的渠道，再用技术/行业社区和搜索引擎扩展；最后才把普通职业主页活动当作辅助证据。 |
| --- |

### 附表 6
| 渠道 | 可用 Active 字段 | 建议强度 | 重要限制 |
| --- | --- | --- | --- |
| Dice | Last Active、Resume Last Updated、Likely to Switch、Visible | 字段组合 +4 | 简历更新时间单独不够。 |
| Indeed Smart Sourcing | 过去 30 天活跃、近期简历/偏好变化 | 组合 +3 至 +4 | Indeed 指出部分更新简历者并未实际求职；单独更新仅 +1.5。 |
| Monster | Resume Updated Today / within week | 组合 +3 至 +4 | 核对是否有明确求职状态。 |
| ZipRecruiter | recent activity / active resume | 组合 +3 至 +4 | 注意简历可见性与更新时间。 |
| Reed（英国） | 默认近一个月活跃 | +3 至 +4 | 适合英国本地市场。 |
| CV-Library（英国） | fresh CVs / recent updates | +3 至 +4 | 结合目标岗位和地点。 |
| LoopCV | active candidate database | +3 至 +4 | 平台状态需记录日期。 |

### 附表 7
| 行业/方向 | 渠道 | 适用方式 |
| --- | --- | --- |
| PCB / 电子制造 | SMTA Career Center | 寻找近期简历、求职档案、职业活动参与者。 |
| 机器人 / 自动化 | IEEE Robotics & Automation Society Resume Bank | 按机器人、控制、嵌入式、感知等关键词检索。 |
| 工程综合 | IEEE Career Fair | 近期参会、上传简历或求职登记可作为 +3 至 +4 信号。 |
| 供应链 | ASCM Job Board / Career Resources | 从认证、计划、采购、S&OP、运营等方向定位。 |
| 物流 / 运输 | CSCMP Career Center | 适合尾程、运输网络、仓配、物流运营人才。 |

### 附表 8
| 搜索原则  搜索式负责“发现”，原页面负责“举证”。搜索结果摘要、缓存片段或聚合页只能作为线索，最终必须打开原页面并记录日期与原文。 |
| --- |

### 附表 9
| 用途 | 可复制搜索式 |
| --- | --- |
| GitHub 明确求职 | site:github.com ("available for hire" OR "looking for work" OR "open to opportunities") (robotics OR AI OR embedded) (California OR "San Francisco Bay Area") |
| GitHub 简历 | site:github.com (resume OR CV) ("PCB design" OR "power electronics" OR robotics) (2026 OR 2025) filetype:pdf |
| 个人网站 Hire Me | ("hire me" OR "available for work" OR "open to opportunities") (robotics engineer OR machine learning engineer) (California OR Seattle OR Oregon) |
| 近期 PDF 简历 | (resume OR CV) filetype:pdf (robotics OR PCB OR logistics) (2026 OR 2025) (California OR Washington OR Oregon) |
| Reddit 求职帖 | site:reddit.com ("[For Hire]" OR "looking for work" OR "available immediately") (robotics OR embedded OR supply chain) after:2026-04-01 |
| HN 求职线程 | site:news.ycombinator.com "Who wants to be hired" (robotics OR hardware OR AI) 2026 |
| 学校/实验室离校人才 | site:edu (resume OR CV) (robotics OR autonomy OR computer vision) ("graduating" OR "seeking") 2026 |
| Contractor 转全职线索 | ("available for projects" OR contractor OR freelance) ("PCB designer" OR "robotics engineer") (California OR remote) |
| 物流/尾程 | ("looking for work" OR "open to opportunities") ("last mile" OR transportation OR logistics OR fulfillment) (California OR Washington OR Oregon) |

### 附表 10
| 证据 | 分数 | 适用说明 |
| --- | --- | --- |
| 最近 3 个月本人明确公开求职 | +5 | 本人原文，含目标岗位/地点/可到岗时间更强。 |
| 最近 3 个月公开发布或更新简历 | +5 | 需核对确为求职导向，而非普通资料维护。 |
| GitHub Available for hire + 求职 README | +5 | 两个第一方信号同时出现。 |
| GitHub 单独 Available for hire | +4 | 记录状态页面和抓取日期。 |
| HN 当月 Who wants to be hired? | +5 | 候选人主动发布；31–90 天可降至 +4。 |
| Reddit 30 天内本人 [For Hire] | +5 | 明确为本人且与目标职位一致。 |
| Wellfound Ready to Interview | +5 | Open to Offers 为 +4。 |
| Cord active talent stream | +5 | 以平台近期状态日期为准。 |
| 候选人主动加入 opt-in 裁员人才名单 | +5 | 与公司裁员新闻区分。 |
| 明确留言感兴趣、会申请、已申请 | +4 | 公开原文优先。 |
| 本人明确表示被裁/职位取消/合同结束 | +4 | 第一人称公开声明。 |
| Career Break / Seeking Opportunities | +4 | 需确认当前仍有效。 |
| 近期简历库活跃 + 近期简历更新/偏好变化 | +4 | 两个字段组合；单独简历更新仅 +1.5。 |
| 已有合法数据中邮箱失效且履历变化 | +3 | 不可主动测试或猜测。 |
| 30–90 天多次互动相近招聘岗位 | +3 | 跨公司、连续行为更强。 |
| 多次公开与 Recruiter 沟通职位 | +3 | 仅限公开互动。 |
| 近期职业活动上传简历/求职登记 | +3～4 | IEEE、协会 Career Fair 等。 |
| Contractor / Freelance / Self-employed | +2 | 必须配合可用性或求职信号。 |
| 公司/部门近期裁员 | +1～2 | 公司层面辅助证据，不代表个人被裁。 |
| 更新求职式个人主页/作品集/联系方式 | +2 | 普通项目更新不计。 |
| 单次点赞招聘帖 | +0.5 | 不得单独判 Active。 |
| 普通专业内容互动 / GitHub 常规活动 | 0 | 只证明专业活跃。 |

### 附表 11
| 总分 | Active 等级 | 执行动作 |
| --- | --- | --- |
| 8 分以上 | 高概率 Active | 优先联系；开场直接引用公开求职信号和岗位匹配。 |
| 5–7.5 分 | 中高概率 | 可以联系；用探索式话术确认时间、动机和限制。 |
| 3–4.5 分 | 可能看机会 | 进入观察池；等待第二个中强信号或进行轻量接触。 |
| 3 分以下 | 证据不足 | 不得称为 Active；只按匹配候选人管理。 |

### 附表 12
| 反向信号 | 建议处理 |
| --- | --- |
| 30 天内宣布加入新公司/开始新职位 | -5；原则上不列 Active，除非本人之后再次公开求职。 |
| 近期晋升、扩大职责或加入核心项目 | -3；降低优先级并核对本人意向。 |
| 明确表示 not looking / not open to recruiters | -5；停止以 Active 名义联系。 |
| 求职帖已删除或主页改为已入职 | -3 至 -5；以最新状态为准。 |
| 证据超过 6 个月且无新信号 | 分数衰减至历史证据；不得维持原评级。 |

### 附表 13
| 证据年龄 | 权重/解释 | 使用规则 |
| --- | --- | --- |
| 0–30 天 | 最有价值 | 保持原分；优先联系。 |
| 31–90 天 | 可信度较高 | 通常保持或轻微下调；核对是否已入职。 |
| 3–6 个月 | 需要新辅助证据 | 原则上乘 0.6；至少再找一个近期信号。 |
| 6–12 个月 | 历史证据 | 原则上乘 0.3；不得单独判当前 Active。 |
| 超过 12 个月 | 原则上不用 | 只保留为时间线背景。 |

### 附表 14
| 去重规则  同一行为不要重复计分。例如“发布新简历”同时被 Google、个人网站和聚合页收录，只算一次；同一求职帖的转发和搜索摘要也不重复计分。 |
| --- |

### 附表 15
| 字段 | 填写要求 |
| --- | --- |
| 姓名 | 与公开职业档案一致。 |
| 当前公司及职位 | 标注确认日期；如已结束，写明结束时间。 |
| 当前美国地点 | 城市/州；远程偏好单列。 |
| 最匹配的客户职位 | 不得用 Active 信号代替匹配结论。 |
| 职业主页 URL | LinkedIn 可作为公开档案之一，但非必需。 |
| 公开简历 / GitHub / 个人网站 | 逐个记录 URL 和更新时间。 |
| 可核实邮箱及电话 | 注明公开来源；不可猜测或测试。 |
| Active 总分与等级 | 写出逐项加分、扣分和去重说明。 |
| Active 判断依据 | 每条标注事实/推测/证据不足。 |
| 证据日期与链接 | 发布日期 + 抓取日期 + 原链接。 |
| 职位匹配点 | 技能、行业、产品、团队规模、业绩等。 |
| 缺口 | 技能、地点、签证、资历、薪资或到岗时间。 |
| 是否来自裁员目标公司 | 公司层面信息与个人状态分开。 |
| 信息置信度 | 高/中/低，并解释原因。 |
| 下一步验证问题 | 联系时要确认的动机、时间、地点、薪资、签证等。 |

### 附表 16
| 示例  Active：中高概率（6.5 分）。确认事实：候选人 22 天前在 GitHub README 写明 open to full-time robotics roles（+4），近期更新简历与地点（+2），并单次评论相近职位（+0.5）。合理推测：可能主动看机会。反向核对：未发现近期入职或晋升。职位匹配另评为 82/100。 |
| --- |


---

## File: `chatgpt-knowledge-20261109/skills/agent-orchestration/SKILL.md`

---
name: recruitment-multi-agent-orchestration
version: 2026-11-09
source_type: reconstructed-memory
---
# AI Agent 猎头工作编排

## 适用分工
- Recruitment Lead：拆分 JD、制定招募与 BD 优先级、核对 HR 硬条件。
- Talent Sourcer：Google X-ray、公开履历、多渠道寻访、去重。
- Candidate Analyst：基于履历/项目强证据逐人评分；Active 分独立。
- Contact & Outreach：合法富化联系渠道、检查去重/退订、个性化外联、回执验证。
- Market Intelligence：公司扩张、猎头需求、薪酬行业信号与目标企业画像。

## 调度原则
一个角色一个输出契约：输入来源、任务边界、可验证结果、截止节点、失败回报。不同 Agent 的“完成”必须由文件/链接/消息 ID/提交 SHA 证明；并行任务不可互相编造状态。

## 工具与限制
用户研究过 Codex、Manus、Paseo、Pi、WebCodex 和多个富化连接器；这些是可探索的执行通道，不代表当前 ChatGPT 可以读取它们全部本地会话或远程工作状态。不要把“一台 UI 可打开多个 Agent”误认为全部模型之间共享上下文和权限。


---

## File: `chatgpt-knowledge-20261109/skills/bd-market-signals/SKILL.md`

---
name: global-headhunter-bd-signals
version: 2026-11-09
source_type: reconstructed-memory
---
# 全球招聘 BD 商机信号漏斗

1. 按国家/地区识别中国企业出海扩张、设立海外区域中心、投资建厂、注册实体、管理层变化、持续招聘、产品推出或渠道扩张。
2. 优先确定雇主主体及是否需要当地雇员，而非仅见“海外”就视为当地猎头职位。
3. 区分公开直招、招聘机构代招、RPO、外包、猎头已确定合作；匿名招聘不等于公司已放猎头。
4. 证据标记：A1=客户/官方一手证据；A2=权威关联材料高可信；B=间接支持；C=待核实线索。评级与出处分开记录。
5. BD 清单：公司、国家、岗位、来源时间、最新动作、HR/业务决策人公开职业链接、真实联系方式来源、是否可确定猎头合作、下一步核实动作。
6. 动态扫描需要每期刷新来源；不能将历史招聘当在招，更不能编造联系人。


---

## File: `chatgpt-knowledge-20261109/skills/candidate-evaluation/SKILL.md`

---
name: evidence-based-candidate-evaluation
version: 2026-11-09
source_type: reconstructed-memory
---
# 基于强证据的候选人推荐评估

## 两项分数绝不混合
- **Role Fit：** 100 分制，按该岗位的真实硬条件和权重制定，输出总分、是否推荐。
- **Active Confidence：** 独立 0–10 分或强/中/弱/未知，依据本人公开找工作行为；不得加进 Role Fit 总分。

## 证据等级
- **已验证：** 原始简历/候选人确认/公开权威材料有明确工作内容与日期。
- **明确自述但未验证：** 技能栏、个人介绍或第三方页面的声明。
- **缺证：** 没有充分信息；与“确定不会”“不符合”不同。
- **矛盾/负证据：** 与强制条件冲突的经历或明确不能接受岗位要求。

## 打分步骤
1. 核对最近工作国家、签证/迁居可行性、语言工作水平、行业产品、职位责任、直接客户/渠道、真实项目、绩效。
2. 每个维度记录满分/实得/证据；强制性技术或监管门槛独立展示，不能被其他维度高分抵消。
3. 写优势 3–5 条、风险与缺口 3–5 条、需电话核实的具体问题。
4. 结论固定为：优先推荐 / 可推荐 / 补充验证后有条件推荐 / 暂不推荐。结论与总分独立，不因总分高自动通过硬性门槛。
5. 列出 LinkedIn 或其他公开职业主页来源；不伪造未读取的简历详情。

## 可复制字段
`姓名 | 当前职位 | 公司 | 地区 | 主要行业 | 真实项目 | 关键技能 | 硬性门槛 | 适配总分 | Active证据/日期 | 优势 | 风险 | 需核实事项 | 推荐结论 | 来源URL`


---

## File: `chatgpt-knowledge-20261109/skills/enrichment-dedup-outreach/SKILL.md`

---
name: recruiting-enrichment-dedup-outreach
version: 2026-11-09
source_type: reconstructed-memory
---
# 富化、去重与招聘触达流程

1. 各批次先标准化职业主页 URL、姓名、公司、岗位，并与历史库及邮件已发送记录去重。
2. 依次尝试获准使用的 B2B 联系人数据服务（Apollo、Lusha、RocketReach、SignalHire、ZoomInfo、Clay、ContactOut 等）；记录来源与置信度。没有来源的邮箱、号码一律不得生成。
3. 工作联系方式与私人联系方式分开保存，遵守数据供应商合同、退订、各地隐私/营销法规与使用限制。
4. 发信前检查已经发过同一职位的记录、退订与明确拒绝；同一职位不要重复群发。
5. 典型触达顺序：邮件 → 下一工作日 LinkedIn → 合理 IM 或电话；用户在个别项目有特定顺序时以项目最新版为准。
6. 外联信包括：机会亮点、职责相关事实、地点/签证已确认事实、一个清晰的回信请求，不写未经核实的薪资、夸大福利或不存在的面试进展。
7. 已发送必须有真实发送结果、收件地址、平台消息 ID 和时间；查到联系方式不等于发信成功。
8. 如果不允许发日历链接或不允许主动约电话，遵守该项目要求。


---

## File: `chatgpt-knowledge-20261109/skills/hr-intake/SKILL.md`

---
name: hr-intake-five-questions
version: 2026-11-09
source_type: reconstructed-memory
---
# 接到海外职位后的 HR 五问法

1. **真实必备项 vs 加分项**：行业、产品、技术栈、年限、学历、关键项目分别如何排序？哪些明确可放宽？
2. **国家/落地与雇佣**：常驻地、合法工作许可或雇主签证支持、语言的实际工作场景、能否跨境迁居。
3. **岗位职责和组织**：直接汇报、是否管理团队、客户类型、业务指标、技术职责边界、新岗位或替补。
4. **薪酬预算**：固定、绩效、佣金、货币、税前/税后、奖金区间、签约主体、是否提供搬迁支持。
5. **招聘流程与紧急度**：HC、优先方向、面试几轮/谁决策、面试反馈 SLA、到岗目标、已筛过的人选与拒绝原因。

将 HR 的“原话”“已确认”“推断”“待询问”独立记录；新口径注明日期，不能无条件覆盖另一个国家或岗位的要求。


---

## File: `chatgpt-knowledge-20261109/skills/recruiter-report/SKILL.md`

---
name: forestown-recruitment-report
version: 2026-11-09
source_type: reconstructed-memory
---
# FORESTOWN 猎头推荐报告统一结构

> 参考长期使用的“金山云/福睿思特推荐报告”体例。此处仅为结构重建，并非原 Word/PDF 样式逐像素复制。

```
FORESTOWN
福睿思特推荐报告
目标企业：<公司>
推荐职位：<岗位>
推荐机构：<业务专项猎头团队>

一、候选人基本资料
姓名、当前位置/工作许可、教育经历、当前职位、工作年限、语言、期望薪酬（如有证据）

二、猎头推荐评估
一句话推荐结论、核心业务优势、关键风险/待核缺口、推荐总分、是否建议推进

三、教育及工作经历
按时间倒序；保留工作职责、业绩、项目规模和客户类型；未经验证标待确认

四、职位关键指标核验
岗位维度 | 满分 | 实得 | 证据来源 | 欠缺证据

五、最终综合评分
总分/100、推荐级别、是否可推荐、原因、后续需核实的问题
```

## 纪律
- 用户要求时，英文履历逐句翻译中文，不擅自删掉工作经历。
- 保持公司指定模板的标题、命名和章节顺序；找不到模板原件必须披露未能确保版式完全一致。
- 不随意推算缺失的出生日期、签证类别、薪酬或候选人个人联系方式。


---

## File: `chatgpt-knowledge-20261109/skills/transcription-qa/SKILL.md`

---
name: recruitment-audio-transcription-qa
version: 2026-11-09
source_type: reconstructed-memory
---
# 招聘会议/候选人录音转写 QA Skill

- 过去用于 Forestown 会议及候选人访谈：Mac Whisper.cpp，曾使用 large-v3-turbo 模型处理中英混合。
- 先确认可用音频格式、时长、说话人和录音授权；无法读 M4A 可转为 WAV/MP3，但不应无凭推测内容。
- 转写后核对 TXT/SRT；对姓名、公司、薪资比例、回款、数字、技术术语、转折逻辑进行人工或听音复核。
- 避免模型在空白/静音段产生幻觉；标注 `[听不清]`，不把推断当逐字原话。
- 分离“逐字转写”“会议摘要”“行动项”“规则变更”，关键利益条款以音频逐句为证据。
- 这是从对话记录重建的流程，**未获取到原始自定义 Skill 的完整文件**。


---

## File: `chatgpt-knowledge-20261109/skills/xray-sourcing/SKILL.md`

---
name: global-xray-sourcing
version: 2026-11-09
source_type: reconstructed-memory
---
# 全球招聘公开寻访 SOP（不依赖 LinkedIn Recruiter）

## 目标
面向北美、欧洲、香港、新加坡、马来西亚及澳洲，针对高级销售、云计算/数据中心、物流、电子工程、工业自动化、机器人等岗位建立可验证人才池。

## 操作
1. **岗位画像**：拆为行业/客户、职能、产品和技术、落地国家、语言、签证/许可、必须证据、待核事项。区分 HR 书面硬条件、偏好、猎头推断。
2. **确定同质岗位和目标企业**：先建立5–10个真实同类职称，再扩展上下游行业；不要只搜一个 Job Title。
3. **公开 X-ray**：按站点、履历关键词、国家、产品、项目类型组合，例如 `site:linkedin.com/in/ ("Solutions Architect" OR "Presales") ("data center" OR "IDC") Singapore`；用 Google/Bing 等独立验证。
4. **多来源补全**：公司官网团队/讲者页、行业协会、展会、GitHub 和技术文章、招聘活动、公开 Portfolio、专业社区；记录 URL 和时间。
5. **结构化去重**：优先 LinkedIn 标准化 URL，再以姓名+公司+职位+地区辅助；每个人仅一个主记录。
6. **分别评估适配度和 Active 可信度**，将强/中/弱证据与最近核验日期写入。
7. **公开合法联系方式和外联**：使用授权数据富化，至少一个可信渠道即可联系；不能编造手机号/邮箱，不能把不确定匹配当已验证。
8. **复核**：批次核对国家、候选人真实工作历史、职位职责、来源、活跃证据和重复触达。

## 注意
- 公开的公司裁员/重组仅为可能的背景信号，不能认定具体个人正在找工作。
- Recruiter-only 的 Open to Work 不能通过普通公开资料推定。
- 通常每轮先 10–20 人，覆盖质量优先于表面数量；记录每轮来源与排除理由。
- 涉及身份、国籍、年龄等招聘限制时需按当地法律处理，不能由姓名/照片推测敏感属性。


---

## File: `chatgpt-knowledge-20261109/knowledge/aci-finder-and-frameworks.md`

# ACI Finder 与长期方法论架构（重建摘要）

- 方法论名称：TX-GESIS / Tom Xia Headhunter Playbook；ACI = Active Candidate Intelligence。
- 使用场景：跨境中高端招聘，重点为物流、机器人、电子/PCB、云计算和基础设施、工业自动化与出海 B2B 销售。
- 关联站点：<https://aci-finder-tomxia.tom-xia.chatgpt.site/>。历史对话中提及为跨项目工具入口；**未验证其检索后端、实时数据库或当前可用性**，不得声称已用它找到人选。
- 核心：职位硬门槛、岗位匹配分和 Active 求职证据三类分别核查；强证据需要本人、具体日期和原始 URL。
- 专业网站与社区可用公开 X-Ray 收集线索；任何找到的 LinkedIn URL 都需去重、姓名/雇主一致性核实，不能将猜测当作事实。
- 累积结果建议字段：`candidate_id`、`role`、`location`、`linkedin_url`、`source_url`、`observed_at`、`active_signal`、`active_score`、`fit_score`、`hard_gate_status`、`evidence_strength`、`next_action`。

来源：既往用户长期工作流与当前可读取对话整理，**并非原始完整 Skill 文件**。


---

## File: `chatgpt-knowledge-20261109/knowledge/cross-ai-operating-rules.md`

# 跨 AI 共享的知识调用规范

版本：2026-11-09；适用：ChatGPT、Codex、Gemini、DeepSeek、Manus、Muse、OpenBots、Grok 和任何具备 GitHub/HTTP/本地 Markdown 读取能力的 Agent。

## 输入规范
1. 优先读取仓库根目录 `AGENTS.md`、`llms.txt` 和本目录 `README.md`，然后只读取任务相关的 `skills/**/SKILL.md`。
2. 该仓库是跨平台的外部共享上下文，不是任何模型的内置长期记忆；无法访问 GitHub 时，请用户贴入相关文件或上传本地副本。
3. 先核验版本、出处和发布日期。企业 HR 新答复可能覆盖旧标准；当项目更新资料未公开时，先索取最新规则。
4. 明确区分「原始来源」「提取整理」「长期对话重建」「外部推断」。不能把摘要伪称逐字原文。
5. 候选人评估必须输出岗位匹配（0–100）和 Active 可信度（0–10）两套独立结果；证据不足应写「待核实」。
6. 对用户资料实行最小化披露。公开仓库不得包含候选人电话、私人邮箱、简历全文、招聘客户非公开合同、账户口令和 Token。
7. 执行外联、批量触达或入库需遵守相应平台规则、适用法律与用户指示；无真实工具回执，不得声称已发送或已提交。

## 使用示例
> 请将 `https://github.com/tomasshane20230813-bot/Tom-Xia-SKill-` 作为本次海外猎头任务的可复用方法论知识库。先读取 AGENTS.md 和 llms.txt，再读取与任务有关的 SKILL.md。不要假定私有招聘项目数据已发布；对不确定条件发起核实。请分别报告职位匹配分和 Active 证据分，并附验证日期和 URL。

## 主要流程
- 需求澄清 / HR Intake → 角色画像 → 寻访 / X-Ray → 去重 → 证据分级 → 双轨评分 → 补证 → 推荐报告 → 合规触达 → 记录回执与更新
- BD：客户出海与招聘信号 → 公开核验 → 决策人映射 → 个性化价值陈述 → 合作条款谈判 → CRM 追踪


---

## File: `chatgpt-knowledge-20261109/knowledge/industry-frameworks.md`

# 行业招聘能力地图（方法论版）

| 行业 | 必须核实的项目能力 | 常见误判 |
|---|---|---|
| 美国尾程与揽收物流 | Pickup、线路调度、司机/承运商、站点网络、成本/SLA/旺季运力、跨站点 SOP | 只做普通仓储不等于有 Pickup 或网络规划经验 |
| 工业自动化/楼宇能源 | HVAC、BMS、FMCS/EMS、PLC/SCADA、BACnet/Modbus、解决方案、售前投标与 PoC | 只有产品销售经历不等于做过真正技术售前 |
| 云计算与数据中心 | 云平台、服务器网络、虚拟化、IDC/DC、实际机房项目、容量/可用性、客户方案与部署 | 公有云账号操作、泛 ICT 或纯网络背景不自动等于真实 DC 项目 |
| 电子元件独立分销 | Independent Distribution 工作任期、RFQ/采购/交付、渠道客户、毛利/收入、OEM/CEM | 授权代理或原厂经历不自动符合独立分销商硬条件 |
| 机器人/Physical AI | 机器人软件硬件栈、实际客户交付、现场项目、渠道/开发、AI/机器人细分场景 | 泛 AI/软件销售不等于机器人量产项目经验 |
| 东南亚 UC/视频协作销售 | 经销商、SI/终端项目、区域/印度市场渠道、业绩、落地国家 | 印度项目经历是否硬性由客户当期口径决定 |

每个项目需要独立 HR 更新、版本日期与权重；本表只提供审查问题，不替代任何客户 JD。


---

## File: `chatgpt-knowledge-20261109/knowledge/provenance-and-gaps.md`

# 溯源与缺失项清单

## 已有的原始资料
- `Active候选人公开网络识别与评分SOP.docx`（用户 Library 文件，可读取原始字节；本包附 Markdown 提取重排版）。
- `Yealink_J11648_SG_CloudOps_HR_CoreSkill_20261103.md`（用户 Library 原始 Markdown，可读取；只放在 private-only）。
- `DeepCtrls_新加坡云售前最新招聘口径_20261106.md`（Library 可读文本；只放在 private-only）。
- `马来售前技术顾问-JD画像`、`深度智控海外招聘要求信息表`（Library 可读提取文本；只放在 private-only）。

## 长期知识摘要重建，而非原文
Dexmate、SwiftX、Yealink 印度销售、DeepCtrls 马来/新加坡、Ample Solutions、金山云报告格式、Dmall、Eaglerise 等招聘资料，均以当期长期知识摘要和可读资料为依据。原文件若未实际读取，不能保证内容完整。

## 原仓库已有（没有在本包复制/覆盖）
- `skills/virtual-resume-probe/SKILL.md` 和 `skill.yaml`
- `playbook/playbook-sweep-log.md`
- `bd/README.md` 和 `bd/weekly-ai-lead-scan.md`

## 不能宣称完整导出的项目
- ChatGPT 服务端内部 Memory 全文、未曾检索到的过去聊天、无法读取的附件或项目文件。
- 任意第三方插件 Marketplace 的版权 Skill 源码或私有内部配置。
- GitHub、Paseo、Pi、Codex 等外部 Agent 的全部会话日志。
- 候选人完整 CV、敏感联系方式、个人账号令牌。

## 发布边界
这个文件夹供 Public GitHub；`private-only` 必须先将仓库设成 Private 再考虑上载，并避免候选人隐私和凭证泄露。


---

## File: `chatgpt-knowledge-20261109/knowledge/tool-map.md`

# 猎头工具与技能通道清单（由长期对话重建）

| 目的 | 常见工具 | 注意事项 |
|---|---|---|
| 公开人才发现 | LinkedIn、Sales Navigator、Google X-ray、Xing、行业协会、专业论坛、GitHub | 公开数据不等于可以看 Recruiter-only 信息 |
|---|---|---|
| B2B 富化 | Apollo、Lusha、ContactOut、SignalHire、RocketReach、ZoomInfo、Wiza、Clay、Hunter、FullEnrich | 权限/额度/数据准确性单独验证 |
| 外联 | Gmail、LinkedIn、WhatsApp、Telegram、电话、iMessage | 留真实发信/消息回执、去重和退订 |
| 数据管理 | Notion、WPS、Google Drive、CSV | 结构化主键、版本号、字段证据和更改日志 |
| 多 Agent 执行 | Codex、Paseo、Pi、WebCodex、Manus | 不能假定相互可读会话、无需授权或默认具有后台权限 |
| 语音整理 | Whisper.cpp、TXT/SRT、Word/PDF | 音频质量、数字和关键原话复核 |

这是基于使用历史的工具目录，不意味着现在全部已经连接或授权，也不是第三方平台源代码备份。


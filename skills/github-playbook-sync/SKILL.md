# GitHub 玩法与 Skill 同步（GitHub Playbook Sync）

- Tom 的长期指令：以后获得的猎头玩法、Tom 要求保存的长期 skill，都要及时更新到他的 GitHub 仓库 tomasshane20230813-bot/Tom-Xia-SKill-（https://github.com/tomasshane20230813-bot/Tom-Xia-SKill-，公开库，默认分支 main）。随时获得，随时更新，不攒着、不零散。

## 仓库结构

- `README.md` — 仓库总说明
- `skills/<skill-slug>/SKILL.md` + `skill.yaml` — 每个长期 skill 一个目录
- `playbook/playbook-sweep-log.md` — 行业新玩法搜集日志（按轮追加）
- `bd/README.md` — BD 热信号漏斗规则与监视名单
- `bd/weekly-ai-lead-scan.md` — 每周 AI 猎头商机扫描（最新一期，原地替换）

## 触发时机

- 玩法搜集每出一轮新入选条目：追加到 playbook 日志后就推。
- Tom 要求保存一个长期 skill：skill 写好就推。
- 每周商机扫描出新一期：替换 bd/weekly-ai-lead-scan.md 后就推。
- BD 漏斗规则或监视名单变了：更新 bd/README.md 后就推。

## 做法

- 本地 staging 目录：~/workspace/github-export/headhunter-playbook/（与仓库结构一一对应），同步记录在同目录旁的 .muse-github-snapshot-sync.json。
- 汇总、不零散：玩法按轮追加进同一个日志文件，不按轮建新文件；每周扫描只保留最新一期，不堆历史文件；skill 一个目录一套文件。
- 推送前先确认仓库当前 head 没变、新路径在远端不存在（或要覆盖的路径内容已知）；推送后读回核验文件内容与大小。
- 每次推送都会弹出审批卡给 Tom 点批准——这是平台规则，长期指令授权的是内容，卡片仍需他每次点一下。不要为了绕过审批改用其他方式写仓库。

## 注意

- 仓库是公开的：玩法与 skill 推上去即任何人可见。Tom 若改私有，流程不变。
- 只推汇总后的文件；本地草稿、原始抓取、中间过程文件不进仓库。

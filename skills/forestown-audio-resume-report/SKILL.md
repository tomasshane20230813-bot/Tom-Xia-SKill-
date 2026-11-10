---
name: forestown-audio-resume-report
description: FORESTOWN recruitment calls — local Whisper.cpp transcription, timestamp QA, CV cross-check, and verified DOCX/PDF referral reports.
aliases: [forestown-audio-resume, recruitment-audio-transcription-qa, FORESTOWN_录音转写与简历报告_SKILL]
updated: 2026-11-10
---

# FORESTOWN｜候选人电话录音转写与推荐报告 Skill

## 适用
对猎头和HR电话录音（M4A/MP3/WAV，中英双语）完整转写并制作可对外提交的福睿思特候选人报告。历史安装于Mac WebCodex Runner 的两个真实技能：\`forestown-audio-resume\` 与 \`forestown-audio-resume-report\`。此文档提供公开通用版，不包含任何候选人录音、薪酬、联系方式、私人设备绝对路径或认证凭据。

## 先检查文件和环境
- 使用经过用户授权的本地电脑、WebCodex Runner或同等安全工具。按真实项目和HR最新版JD工作。
- 检查音频存在且能播放、检查格式/时长/说话人：
  \`\`\`sh
  command -v ffprobe ffmpeg whisper-cli
  ffprobe -v error -show_entries format=duration,size:stream=codec_name,sample_rate,channels -of default=noprint_wrappers=1 INPUT.m4a
  find AUTHORIZED_ROOT -type f -name 'ggml-large-v3-turbo.bin'
  \`\`\`
- 旧脚本的默认模型目录可能失效；始终使用实际发现的模型路径。不要因找不到默认目录就宣称本地无法转写。

## 质量门禁：先试转120秒
- 中英混合**优先 \`-l auto\`**，不要强制指定 \`zh\`；不使用无关初始Prompt。
- 从包含候选人实际回答的多个位置抽取120秒，而非只抽开头：
  \`\`\`sh
  ffmpeg -nostdin -hide_banner -loglevel error -y -ss 120 -t 120 -i INPUT.m4a -ar 16000 -ac 1 -c:a pcm_s16le pilot.wav
  whisper-cli -m MODEL.bin -f pilot.wav -l auto -t 8 --output-txt --output-srt --output-file pilot --no-prints
  \`\`\`
- 严重ASR幻觉：大量重复“字幕志愿者”、"Is that a problem?"、"是吧?"、"Thanks for watching"或连续静音中出现语音。即便进程exit 0，此段也不能用作证据。需重听音频、选含声段、分段、VAD或切换语言策略复核。不可把用户的提问或候选人模糊附和当作候选人明确确认。

## 完整转写
\`\`\`sh
ffmpeg -nostdin -hide_banner -loglevel error -y -i INPUT.m4a -ar 16000 -ac 1 -c:a pcm_s16le full.wav
whisper-cli -m MODEL.bin -f full.wav -l auto -t 8 --output-txt --output-srt --output-json-full --output-file full --no-prints
\`\`\`
完成后交付完整TXT、带时间戳SRT（可附JSON）。长音频优先分块转写后依据原时间轴拼合；完整覆盖录音时长，不丢掉后半段。长任务有Job ID时，监控**同一个Job**，不得重复启动。重要段落需要直接核对原始音频。

## 事实抽取和证据强度
建立四栏证据账本：\`原CV原文\`、\`电话候选人明确陈述+时间戳\`、\`其他独立证据\`、\`待核实/无法听清\`。
重点核验：本人动手做过的项目职责、现场数据中心机房Operation还是云平台运维/Colocation售前、机房与服务器规模、GPU/AI集群、客户和供应商、招投标和POC、灾备、合同额、薪资/奖金、国籍/签证、到岗时间、工作年限。
- 不得把销售或项目投标等同真实现场数据中心Operation。
- 不得把招聘顾问的问题、假设或解释当成候选人确认。
- 数字、公司名称、语言切换、断句必须重听；不清楚标 \`[听不清 00:00:00]\`，不编造。

## FORESTOWN报告模板
使用指定的真实 \`Gary Ling／金山云\` 版式，第一页固定 \`FORESTOWN\`／\`福睿思特推荐报告\`／目标企业、职位、候选人、签证、学历、期望待遇、离职期、三条核心优势、中文400汉字以内猎头评价（按用户具体要求）。
英文简历遵从用户的精确要求：**原始英文内容逐字保留**；只删除明示需删的电话邮箱或实习，新增电话补充须在相关任职下另立“Candidate interview supplement”标识，不得伪装成原始英文原文。重点项目视觉高亮不改变事实内容。
对外只需要优势时，报告不写主观劣势，但须不夸张、不编造、不夸大符合程度。公司是否中资、合资、子公司须核对公司法定实体关系。

## 最终QA和交付
1. 抽样+重点复听并检查SRT时间戳；明确全文是否有幻觉段。
2. 列明每条关键项目证据的原始音频分钟:秒。
3. 以Word模板生成DOCX，渲染每页PNG，检查字体、换页、个人隐私、英文完整性、400字上限与有无残留其他候选人姓名。
4. 同时输出PDF并重新打开查看；确保交付路径真实可访问。
5. 不向公共GitHub提交录音、转写稿、履历或客户私密报告。这个Skill只是通用方法，可供其他AI通过GitHub读取；执行仍需本机授权和工具。

## 案例纠错记录（匿名化）
2026-11：一个约38分钟的英语/中文候选人通话，Mac中Whisper模型从旧默认目录移至授权项目文件夹。120秒试转出现重复句幻觉，须通过分段和复听防止虚构“机房Operation”证据。该纠错适用于以后所有项目。

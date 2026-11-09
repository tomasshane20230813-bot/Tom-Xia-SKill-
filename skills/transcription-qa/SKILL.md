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

---
name: memory-via-openmausbot-ceo
description: Paseo 里的 Agent（CEO、PI+、MAUS 等）需要调用 Tom 的长期记忆时，一律通过 MAUS Bots（OpenMausBot）桥接去问大总管。涉及历史口径、客户要求、打分规则、旧候选人记录、项目进度时都调用，不自己猜，不编造。
version: 2026-11-23
source_type: tom-operating-rule
---

# 需要记忆就找 MAUS Bots 那边的大总管

Tom 于 2026-11-23 定下，长期有效。Tom 的记忆以 OpenMausBot 大总管为准。Paseo 里任何 Agent 需要调用记忆，都通过 MAUS Bots 桥接去问大总管。

## 找谁

- 记忆来源：OpenMausBot 大总管，bot_id `bde2c12d-3181-4e46-822c-169b52f1c769`。
- 桥接人：Paseo MAUS，agent id `003e705d-617a-46c8-b71a-4645c7e15de6`，工作目录 `~/Paseo-Maus-Bridge/mausbot`。

## 怎么问

1. 自己有 `openmausbot` 工具：用 `send_bot_message` 发给大总管，再用 `wait_for_conversation` 等回复。
2. 自己没有：用 `paseo send 003e705d-617a-46c8-b71a-4645c7e15de6 --behavior steer --no-wait` 交给 MAUS。MAUS 转问大总管，把回复原文送回提问的 Agent。
3. 问题写清四件事：哪个项目，要哪条记忆，什么时候要，拿来做什么。

MAUS 收到别的 Agent 的记忆请求要马上转，不等手上的活做完。

## 拿到以后

- 按大总管原文执行。用到的地方写「记忆来源：大总管｜时间」。
- 本机文件、旧 skill、旧稿只作参考。和大总管说法冲突时，以大总管为准，并告诉 CEO。
- Tom 在当前对话里直接下的指令，优先于记忆。

## 问不到怎么办

- 不停工。先做不依赖这条记忆的部分。
- 依赖它的地方写「记忆待大总管确认」，不要猜，不要编。
- 15 分钟没有回复，报给 CEO，由 CEO 再催或上报 Tom。

## 不要做

- 不要为了查记忆去问 OpenMausBot 里的其他 Bot。
- 不要请大总管替你寻访或写稿。这里只问记忆。
- 不要把记忆请求和回复写进客户交付目录。

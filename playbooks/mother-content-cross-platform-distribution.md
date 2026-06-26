# Lingzao Mother Content Cross-Platform Distribution

Use this playbook when the user has one topic, draft, note breakdown, creator
case, product update, course idea, or content template and asks Lingzao to turn
it into a one-stop distribution package across platforms.

Trigger phrases:

- 一条龙
- 一条龙分发
- 全平台同步
- 全平台更新
- 全平台提供内容
- 多平台分发
- 这个内容可以发哪些平台
- 把这个内容改成公众号 / 小红书 / 朋友圈 / 知识星球 / X / B站
- 一个模板发多个平台
- 给我做一套分发包
- 做成小红书图片 / 小红书图文 / 小红书逐字稿

## Core Principle

Do not make each platform start from scratch. First create one mother content
object, then adapt it by platform.

The goal is not to mechanically generate every possible platform. The goal is
to help the user publish one idea in the few formats that make sense now.

Default behavior:

1. If the user asks for 一条龙 / 全平台 / 分发包 without naming platforms,
   first generate the basic package:
   - Xiaohongshu
   - Moments
   - WeChat public account
2. Then offer optional expansion:
   - podcast
   - X platform
   - Knowledge Planet
   - Bilibili
   - video account / Douyin
   - Xiaohongshu graphic-note image package
   - Xiaohongshu spoken script / Vlog storyboard
   - knowledge-base entry
3. If the user says "做成小红书图片" or "小红书图文", route to the visual or
   graphic-note workflow after the text package is clear.
4. If the user says "公众号", produce article text and image directions, but
   only generate images when requested.

## Mother Content Object

Every distribution task starts with a concise mother object:

- 本次主题
- 一句话判断
- 素材来源: user draft, note breakdown, keyword research, account diagnosis,
  product update, screenshot, transcript, or oral idea
- 目标用户
- 这条内容解决的问题
- 核心观点
- 证据 / 案例 / 细节
- 适合优先发布的平台
- 暂时不建议发布的平台
- 可沉淀资产: title library, cover library, script library, knowledge-base
  note, FAQ, course section, or product SOP

If source material is missing, make a first usable version instead of
over-asking. The user can revise after seeing the first package.

## Basic One-Stop Package

When the user asks for 一条龙 and does not specify platforms, output these
three first.

### 1. Xiaohongshu Basic Package

Choose the best Xiaohongshu format:

- graphic note / image post
- spoken video
- Vlog storyboard
- text-dense screenshot graphic note
- interaction post

Output separated fields. Do not merge them into one block:

- 适合形式
- 标题 3 个
- 封面主标题
- 封面副标题 or 画面关键词
- 图文页结构 or 口播结构
- 每页/每段文字
- 正文区 300 字左右
- 10 个发布关键词
- 评论区引导
- 发布前检查点

If the user asks for image generation, continue to:

- `reference-image-graphic-note-workflow.md`
- `visual-generation-and-cover-workflow.md`
- `image-generation-execution-workflow.md`

### 2. Moments Package

Moments should feel more human and less like an article.

Output:

- 朋友圈短文 1 条: personal discovery / real feeling
- 更口语版 1 条: casual, like talking to friends
- 偏产品观察版 1 条: if the topic involves Lingzao, Agent, Skill, product, or
  workflow
- 可配图建议: optional, only if useful

Keep it short and not over-explained.

### 3. WeChat Public Account Package

WeChat public account should carry the fuller logic.

Output:

- 公众号标题 3 个
- 文章开头
- 正文结构
- 正文草稿, usually 800-1200 Chinese characters unless the user asks for a
  longer article
- 封面标题方向
- 正文配图方向, usually 3 in-article image directions when image packaging is
  requested
- 结尾轻转化 / 下次阅读引导

Do not automatically generate WeChat cover images unless the user asks for
公众号封面, 公众号配图, 生成图片, or 图片包.

## Optional Expansion Menu

After the basic package, offer a short menu. Do not ask "还需要什么".

Good wording:

我先给你出了基础一条龙版本：小红书、朋友圈、公众号。下一步还可以继续扩展成：播客提纲、X 平台短帖/线程、知识星球帖、B站/视频号/抖音简介，或者小红书图文图片包。你可以直接说要扩哪一个。

Optional outputs:

### Knowledge Planet

- 星球帖标题
- 内部判断
- 案例拆解
- 产品化价值
- 下一步动作
- 可给学员的作业

### X Platform

- single short post
- thread version, 5-7 posts
- optional English version when user asks
- one sentence positioning for technical/product audience if relevant

### Bilibili / Video Account / Douyin

Output depends on depth:

- title
- first 3 seconds hook
- 60-second spoken outline
- full spoken script if requested
- description / intro
- comment prompt
- cover words

Do not assume long-form Bilibili unless the topic needs a tutorial or screen
recording. For a quick cross-platform package, keep it short.

### Podcast

Only expand when the topic is a larger issue, not a tiny tactic.

- podcast title
- episode thesis
- 3-5 segment outline
- opening monologue
- key stories/examples
- ending question

### Knowledge Base / SOP

Use when the topic is reusable:

- knowledge-base title
- applicable scene
- step-by-step SOP
- judgment standards
- reusable prompt/template
- update rule

## Platform Fit Judgment

Before generating too much, quickly judge fit:

- Xiaohongshu: practical, visual, saveable, emotional, or clickable
- Moments: personal discovery, lightweight update, trust building
- WeChat public account: complete logic, method, case, reflection
- Knowledge Planet: internal review, paid-user teaching, homework
- X: sharp product/tech/creator-operation judgment
- Bilibili: tutorial, screen recording, long explanation, public teaching
- Douyin / video account: short result, strong opening, easy-to-understand
  demonstration
- Podcast: long-term issue, not a small technique
- Knowledge base: SOP, checklist, reusable framework

## Output Discipline

- Separate every platform and every text block clearly.
- Do not give a dense wall of text.
- Do not pretend all platforms are equally suitable.
- Do not generate images unless the user asks for images or Xiaohongshu graphic
  note/image package.
- If the package becomes long, offer Word / HTML webpage / knowledge-base
  packaging using `retention-and-follow-up-loop.md`.
- Keep the platform tone different:
  - Xiaohongshu: click, save, comment, keywords
  - Moments: human, light, personal
  - WeChat: logical, complete, readable
  - Knowledge Planet: internal, productized, teachable
  - X: sharp, compressed, discussion-worthy
  - Bilibili: searchable, tutorial-like, clear promise

## Minimal Output Template

Use when the user wants a fast one-stop package:

1. 本次母内容
2. 平台适配判断
3. 小红书
   - 标题
   - 封面字
   - 内容结构
   - 正文
   - 关键词
4. 朋友圈
   - 短文
   - 口语版
5. 公众号
   - 标题
   - 开头
   - 正文结构
   - 正文草稿
6. 可继续扩展
   - 播客
   - X
   - 知识星球
   - B站/视频号/抖音
   - 小红书图片包
   - 知识库/SOP

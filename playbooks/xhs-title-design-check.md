# Lingzao Xiaohongshu Title Design Check

Use this playbook when the user sends a topic, draft, title, cover copy,
reference note, or content package and asks for:

- 小红书标题
- 帮我起标题
- 标题怎么写
- 标题优化
- 封面标题
- 标题有没有点击
- 根据内容给标题
- 这几个标题哪个好

This is a publishing judgment layer. It is different from a formula library or
a title-pool generator.

## Core Principle

Do not give ordinary users 10 titles and then recommend 3.

Default output is only 3 strongest titles. Let the user choose from the best
three, not from a noisy pool.

The title's job is:

1. make the right reader want to click
2. carry the big keyword anchor when possible
3. match the cover and content promise
4. stay short enough for Xiaohongshu, usually within 20 Chinese characters
   including punctuation and emoji

When the user explicitly asks for a title library, title bank, or many
alternatives, you may give more options, but first explain that the default
publishing decision should still settle on 3 strongest titles.

## Required Inputs

Proceed directly if the user provides any useful input:

- draft or body copy
- graphic-note page text
- spoken script
- Vlog theme or storyboard
- title they already wrote
- cover copy
- keyword or track
- target audience
- benchmark title or reference note

If the input is too thin, ask only for the missing minimum:

你把正文/脚本、想打的关键词，或者你想模仿的标题发我就行。我先只帮你挑 3 个最值得点的标题，不做一大堆标题池。

Do not ask a long form.

## Audience Gate

Before writing the 3 strongest titles, identify who is supposed to click.

Use `audience-persona-fit-check.md` if the audience is unclear. A title that is
strong for one group can be wrong for another:

- If the content is female-oriented, use female-related topic and keyword
  anchors rather than pretending it is for everyone.
- If the content is for university students or young beginners, do not force
  35+, one-person company, childbirth, marriage, or midlife-crisis words unless
  the content truly discusses those life stages.
- If the content is local life, include the city/area in title or cover when
  possible, and make sure the keyword field and location signal match the city.

If the user does not know their audience, ask for 3-5 liked, saved, searched,
or benchmark notes and reverse-infer the likely audience before writing titles.

## Title Judgment

Judge every title by these questions.

### 1. Is There A Big Keyword Anchor?

Prefer concrete search or season anchors over broad concepts.

Good anchors:

- 高考志愿
- 新疆旅游
- 35岁职场
- 女性成长
- 小红书起号
- AI工具
- 好物分享
- 本地生活探店
- 减肥
- 穿搭

Bad broad words when used alone:

- 好好学习
- 成长
- 努力
- 生活
- 变好
- 分享

Example:

- Weak: 如何好好学习
- Stronger: 高考志愿怎么填

The strong version names the user's real search moment.

### 2. What Is The Click Point?

At least one click point should be obvious.

Common click points:

- 反差: small-town to New York, junior college to graduate school, ordinary
  person to visible result.
- 好奇: 怎么没人早点告诉我, 这到底是什么, 为什么会这样.
- 数字: 2分钟, 10天9夜, 3000块, 50天.
- 时间: 一年后, 50天重启, 一天这样拆开用.
- 结果: 看这一篇就够了, 我这样走出来了, 直接能用.
- 身份: 普通女生, 宝妈, 文科生, 职场新人, 35岁女生.
- 反问: 真的可以吗, 为什么没人说, 你是不是也这样.

Examples:

- 我是如何从小镇青年到纽约的
- 一年时间人怎么能变得这么争气
- 怎么没人早点告诉我这个
- 2分钟带你看完这个工具
- 十天九夜新疆游，看这一篇就够了
- 带3000块旅行全球真的可以吗

### 3. Does The Title Match The Content?

The title can be sharp, but it cannot promise something the content cannot
deliver.

Check:

- If the title says "看这一篇就够了", the content must be a complete guide.
- If the title says "我从小镇到纽约", the content must include the path or
  turning points.
- If the title says "高考志愿", the content must actually help with志愿/专业/
  城市/院校选择, not only general study advice.
- If the title says "好物", the note must reveal a specific product or scene.

### 4. Can It Fit The Cover?

Xiaohongshu cover titles need to be read in one second.

Prefer:

- one main line
- one concrete keyword
- one strong hook
- no stacked slogans

If the title is too long, split:

- title field carries the keyword + hook
- cover copy carries the shorter visual hook
- first 3 lines carry the context and promise

## Output Structure

Use this order.

1. 一句话判断
   - Say the current strongest title direction.

2. 首推 3 个标题

| 标题 | 为什么会被点 | 关键词锚点 | 适合什么情况 |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

3. 不建议的标题方向
   - Show 1-3 weak directions only if useful.
   - Explain why they are too broad, too long, too slogan-like, or not matched
     to the content.

4. 封面标题建议
   - If the title is for a graphic note or cover, give 1 short cover version.
   - If the title itself can go on cover, say so.

5. 关键词衔接
   - Name the top 3 keywords that should appear across title, cover, first 3
     lines, or keyword field.
   - If the content is local life, include the city/area keyword.
   - If the user asks for final publishing keywords, route to
     `publishing-keyword-design-check.md`.

6. One follow-up

Use one of:

- 你选其中一个标题后，我可以继续帮你配 10 个发布关键词，并检查标题、封面和正文前 3 行有没有自然埋进去。
- 你把封面文案也发我，我可以继续判断标题和封面是不是在说同一件事。
- 如果你想做图文，我可以把这个标题继续拆成封面和 4 页/7 页图文结构。

Do not output a long title pool unless the user explicitly asks.

## If User Already Has Titles

Do not only rewrite.

First diagnose:

- 哪个有关键词锚点
- 哪个有点击理由
- 哪个太泛
- 哪个标题和正文不匹配
- 哪个适合放标题栏，哪个适合放封面

Then output only the best 3 revised versions.

## If User Sends A Draft

Extract the real hook before writing titles:

- What is the most concrete event, result, method, or contrast?
- What is the reader searching for?
- What will the reader get after clicking?
- Is this better as fear, curiosity, guide, transformation, or identity title?

Avoid making a title from the most beautiful sentence if that sentence has no
search keyword or click reason.

## If User Sends A Keyword Only

Do not make the keyword too broad.

Split likely intent first:

- 女性成长: career, relationship, marriage/family, self-consistency, identity
  transformation, learning, side business.
- 35岁职场: pre-35 anxiety, after-35 survival, layoffs, AI office efficiency,
  second curve, side income.
- 好物分享: mother/baby, home, travel goods, electronics, beauty, clothing,
  tools, product scene.
- AI工具: workplace, teacher, content creation, image/video, agents, coding,
  screen-record tutorials.
- 本地生活: city, district, budget, old stores, tourism, food, shop exploration.

Then write titles around the narrowed intent.

## Do Not

- Do not default to 10 titles plus top 3.
- Do not use guaranteed-growth language such as 必爆, 稳爆, 一发就火.
- Do not use a hot keyword if the content does not actually discuss it.
- Do not write only clever titles with no keyword anchor.
- Do not make every title sound like a formula.
- Do not let "标题优化" become a full account diagnosis unless the user asks.

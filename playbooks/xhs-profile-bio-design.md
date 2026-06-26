# Xiaohongshu Profile Bio Design

Use this playbook when the user asks for a Xiaohongshu personal intro,
100-character bio, profile description, homepage introduction, nickname/bio
package, or asks whether their current profile intro is clear.

This is not a slogan-writing task. Treat the bio as homepage conversion copy:
it should help a stranger decide whether this account is for them and whether
to follow after opening the homepage.

## When To Trigger

Trigger on wording such as:

- 小红书 100 字介绍
- 个人介绍 / 个人简介 / 主页简介
- bio / 简介怎么写
- 账号介绍 / 自我介绍
- 帮我设计主页文案
- 我的主页介绍要不要改
- 昵称、头像、简介怎么搭

Also trigger after beginner account setup, own-account diagnosis, comparable
account adaptation, keyword-to-content packages, and audience persona checks
when the user needs a clearer homepage landing point.

If the target audience is unclear, first use `audience-persona-fit-check.md`.
If the account has too few public notes, do not over-package the identity; use
the beginner/startup version.

## Core Judgment

A good 100-character Xiaohongshu bio answers five questions:

1. Who is this account?
2. Who is it for?
3. What will it keep sharing?
4. Why should someone follow it?
5. Is there a light product, service, city, or contact path?

It does not need to answer all five with equal weight. Choose the clearest 2-4
based on the user's stage. The default length should be around 80-100 Chinese
characters, and shorter is better if the account is still starting.

## Minimum Inputs

If the user has not provided context, ask only for the smallest useful material:

- 你想让什么人点进来之后觉得“这是给我看的”？
- 你接下来最想持续发什么内容？
- 你希望别人记住你哪一点？
- 如果你做本地生活：你在哪个城市/片区？
- 如果你想变现：后面是接广告、卖资料/课、咨询、社群、产品，还是暂时不考虑？

If the user already sent homepage links, drafts, reference accounts, city, or
content direction, infer first and avoid asking again.

## Bio Formulas

### Beginner / Exploration

Use when the user has few notes, no stable column, or is still testing.

Formula:

身份/阶段 + 给谁看 + 记录/分享什么 + 更新承诺

Example patterns:

- 30+普通女生，记录从迷茫到稳定的自我成长。分享职场、生活和普通人能执行的小改变。
- 南宁打工人，周末慢慢探索本地好吃好逛的地方。先从真实体验和避坑开始更新。
- 不露脸做图文，从女性成长、职场卡点和生活自洽里找普通人能照着做的方法。

### Clear Niche / Useful Account

Use when the user already has a track and a target audience.

Formula:

目标用户 + 核心问题 + 持续内容 + 关注理由

Example patterns:

- 写给想重新开始的女生：职场转型、情绪自救、生活秩序和行动清单。陪你把迷茫拆小一点。
- 给新手妈妈看的育儿图文：亲子陪伴、绘本、儿童好物和家庭教育，尽量讲真实可执行的方法。
- 给文科生看的 AI 工具笔记：做图、写作、效率和自媒体实操，不讲太虚的概念。

### Personal IP / Trust Builder

Use when the user has a meaningful contrast, experience, credential, result, or
story that others want to learn from.

Formula:

身份反差/经历 + 结果/可信点 + 分享范围 + 适合谁

Example patterns:

- 从大专到研究生，再到深圳工作。分享普通女生的学历逆袭、职场选择和长期自我建设。
- 从小镇到海外生活，记录普通人如何一点点打开世界。写成长、选择、自由职业和真实生活。
- 35+职场人，记录主业、副业和自我更新。分享不焦虑但要有准备的职场方法。

### Commercial / Product Conversion

Use only when the user already has a real product, service, course, consulting,
store, or lead path. Do not fake commercial authority for beginners.

Formula:

服务谁 + 解决什么 + 产品/服务形态 + 轻联系路径

Example patterns:

- 帮新手博主做小红书内容诊断：账号定位、选题、标题、封面和发布复盘。合作/咨询看置顶。
- AI 图文实操教练，帮个人 IP 做封面、图文结构和内容资产库。资料和课程在置顶。
- 上海本地生活探店，主打打工人平价美食和周末路线。合作可私信，体验真实再推荐。

## Audience And Keyword Fit

The bio should carry the account's most important keywords, but naturally:

- Female-oriented accounts should use female/life-stage words when relevant:
  女生、30+、妈妈、职场女性、普通女生、女性成长.
- Student or early-career accounts should not use 35+、生小孩、一人公司创业
  unless this is their real audience.
- Local-life accounts must include the city or area: 南宁、上海、成都、香港,
  or a more specific district when that is the memory anchor.
- AI/tool accounts should name the scene: AI 做图、AI 写作、AI 办公、文科生 AI,
  老师 AI 工具, not only "AI工具".
- Good-product accounts should name category and scene: 母婴好物、旅行好物、
  浴室收纳、平价彩妆、通勤包, not only "好物分享".

If the bio keywords do not match the title/cover/opening keywords of the first
3-7 notes, say so. The homepage should not look like a different account from
the content.

## Output Structure

Default output should be compact and decisive:

1. 一句话判断：现在简介最该解决什么问题。
2. 推荐版：1 条最推荐的 100 字左右简介, with approximate character count.
3. 备选 1：更有人味/更生活化的版本。
4. 备选 2：更清晰/更工具化/更商业承接的版本.
5. 为什么这么写：explain audience, memory point, keyword, follow reason.
6. 主页搭配建议：nickname keyword, first 3 or pinned notes, and what should
   not be stuffed into the bio.
7. 下一步：offer to continue into nickname, avatar direction, pinned-note
   package, first 7 notes, or title/keyword check.

Do not output 10 bios by default. The user needs 3 usable choices, not a pile
of similar sentences.

## If User Sends Current Bio

Diagnose before rewriting:

- Is it too vague?
- Does it say who the account is for?
- Does it say what will be updated long-term?
- Does it have a memory point?
- Does it match current notes and titles?
- Is it over-commercial for the current stage?
- Does it miss city/track/life-stage keywords?

Then output 3 rewrites.

## If User Sends Homepage Link

Use public homepage clues when available:

- nickname
- existing bio
- visible note themes
- title keywords
- cover style
- number of public notes
- whether the account looks like self, benchmark, or commercial account

If there are fewer than 3 visible notes, do not pretend the positioning is
already clear. Give a starter bio and say it should be retested after the first
3-7 notes.

If the user is writing a bio for a benchmark account or imitation target, first
ask whose bio is being written: their own account or the reference account.

## What To Avoid

- Generic slogans: "热爱生活，记录美好", "做更好的自己".
- Empty identity stacks: "博主/创业者/妈妈/设计师/成长型人格" without a user
  reason to follow.
- Guaranteed claims: "带你月入过万", "保证涨粉".
- Too many tracks in one bio.
- Commercial CTA without a real product/service path.
- Cityless local-life bios.
- A bio that sounds mature while the account has almost no content.

## Good Continuation Prompts

- 你把现在的昵称、简介和最近 3 条笔记标题发我，我可以帮你做一版主页三件套。
- 如果你还没发内容，我可以继续帮你把这个简介拆成前 7 条笔记选题。
- 你如果想做得更商业一点，我可以再帮你判断简介里要不要放课程、咨询、合作或资料入口。

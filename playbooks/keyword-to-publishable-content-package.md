# Lingzao Keyword To Publishable Content Package

Use this playbook when the user gives a keyword, track, or vague topic and wants
Lingzao to turn it into publishable Xiaohongshu content, such as:

- 给我一个关键词，直接帮我出内容
- 搜一下女性成长，顺便给我几条能发的图文
- 帮我批量产出选题、标题、封面、正文和关键词
- 我想做本地生活/好物/AI工具，不知道今天发什么
- 帮我从关键词到小红书笔记一条龙做完
- 根据这个关键词，给我 5 条可发布内容包

This is different from:

- `keyword-insight-report-template.md`: research report for a keyword ecosystem.
- `publishing-keyword-design-check.md`: final 10 publishing keywords after the
  draft already exists.
- `reference-image-graphic-note-workflow.md`: visual/page package after the user
  has a reference image or asks how to make graphics.

## Core Principle

The user is not asking for a search list. They want a path from "I have a
keyword" to "I can post something today".

Turn keyword research into a publishable package:

1. clarify the user's real intent behind the keyword
2. clarify or infer who the content is for and who will click
3. confirm the publishing format: graphic note/image, spoken video, or Vlog
4. confirm search scope and credit tier before lookup
5. search only the confirmed keywords or references
6. filter examples by learnability, not only likes
7. extract topic, title, cover, structure, keyword, and visual formulas
8. produce a small batch of publishable content packages
9. end with one next action: refine one piece, make graphics, save to knowledge
   base, or review data after publishing

Use `audience-persona-fit-check.md` when the audience is unclear. Do not write
a content package as if it is for everyone.

For titles, use `xhs-title-design-check.md` as the judgment layer. Ordinary
users should receive 3 strongest title options, not 10 titles plus a top-3
recommendation. Each title should show a concrete keyword anchor and click
reason.

Do not automatically add Lingzao, A Tian, or any official logo to ordinary user
covers or graphic notes. Only include a logo, watermark, brand mark, or
"Lingzao Agent" wording when the user explicitly asks for an official Lingzao
case, branded asset, or their own brand mark.

## Publishing Format Triage

This workflow should stay light. Do not force the user into a fixed template
only because they sent benchmark links or examples. First identify what kind of
content they want to publish.

If the user sends keywords, notes, favorite examples, or several references and
only says "帮我从这些里面出内容", ask one short format question before writing:

你想让我给你做口播视频、图文/图片，还是 Vlog 分镜内容？如果是 Vlog，我会给你具体分镜，比如早上打开窗、运动、打开电脑、工作和复盘这些画面；如果是图文，我可以做无人物知识卡，也可以按你发的参考图来做。

If the user already names the format, do not ask again:

- 图文 / 图片 / 小红书笔记 / 不露脸 / 知识卡片 -> use Graphic Note Mode.
- 口播 / 视频文案 / 人物出镜 / 逐字稿 -> use Spoken Script Mode.
- Vlog / 日常记录 / 生活方式视频 / 分镜 -> use Vlog Storyboard Mode.

For graphic notes, ask for reference images when useful:

你有没有喜欢的参考图片？有的话发我，我按它的排版和风格做；没有的话，我先给你出一版对应主题的无人物知识卡片，比如女性成长干货卡。

For spoken video, ask whether the user has prior scripts, voice style, or a
reference video/copy. If they do, adapt to that style. If they do not, output a
direct-read spoken draft first.

For Vlog, ask for their available scenes, daily routine, city, work/life setting,
and any reference Vlog. If they do not provide these, make a simple beginner
version with easy scenes instead of cinematic production.

When the user sends 1-4 references, show the evidence before the new draft so
they know the output is grounded:

- 我看了你给的这几条内容，它们共同的关键词是...
- 核心内容点分别是...
- 大纲方向是...
- 脚本/页面结构是...
- 所以我这版做了哪些取舍...

Do not overdo the deconstruction. The purpose is to prove the output has a
source, then quickly give one publishable version.

## User Style Memory Intake

Before producing the first full content package, try to collect the user's own
style signal and audience signal without making the process heavy.

Use this user-facing line when the user has not provided enough personal
context:

你可以把你之前做过的内容发给我，或者把你自己感兴趣、想模仿的内容发给我；如果你做本地生活，也把你所在的城市发给我。我会参考你的语气、审美、城市和你喜欢的内容，再给你出一篇更像你的版本。

If audience is still unclear, add:

你也可以告诉我这条内容主要想给谁看；如果你也不确定，我会先从你喜欢和收藏的内容里反推用户画像。

Handle two cases:

1. **User has not created content before**
   - Do not block the workflow.
   - Say that you will first make one sample based on the keyword and your
     understanding of the user's likely preference.
   - Make only one full piece first, because the user may not yet know whether
     the direction is suitable or difficult.

Good wording:

好，那我先按我理解的你可能喜欢的方向，给你出一篇完整样稿。你看完以后告诉我哪里像你、哪里不像你，我再帮你调整成你的风格。

2. **User has previous posts, drafts, images, video copy, or favorite content**
   - Ask them to send those materials if they have not already done so.
   - After receiving them, acknowledge what was captured before generating.
   - Use their tone, visual style, city, format, and recurring topics as the
     style anchor.

Good wording after receiving user material:

我现在已经记下来了：你之前的内容风格、你喜欢的方向、你的城市/场景，以及你更适合的表达方式。接下来我不会随便套通用模板，会按这些信息给你出一篇更贴近你的版本。

Do not falsely claim long-term memory across sessions. "记下来了" means
captured for the current task, current content package, or current conversation.
If the runtime has an actual memory or knowledge-base tool and the user asks to
save it, use `content-knowledge-base-workflow.md`.

## First Response And Credit Scope

If the user gives only one keyword and wants content output, do not start a
large search silently. Explain that this is a content package workflow, then
offer three scopes.

Use this wording:

可以做。这个不是单纯搜关键词，而是把关键词下面的参考内容拆成「选题 + 标题 + 封面 + 图文结构 + 正文方向 + 10 个发布关键词」。

先确认范围，避免一下子花太多积分：

A. 快速版：只搜主关键词 1 次，先给 3 条内容方向和标题/封面建议，通常约 20 credits。
B. 标准版：搜主关键词 + 3 个相关词，产出 5 条内容包，每条包含标题、封面、图文结构和关键词，通常约 80 credits；如果继续打开单篇详情会再增加。
C. 批量版：搜 8-10 个相关词，先做 10-20 条选题库，再精写 3 条内容包，通常约 180-220 credits 起；如果要看完整正文、评论区或逐字稿，会进入深度搜索。

默认搜索设置：小红书、图文优先、近半年、高赞/高收藏内容优先。如果你只回复 A / B / C，就表示接受这些默认搜索设置；如果你有平台、时间、内容类型或排序偏好，可以和选项一起告诉我。

快速版只搜你给的主关键词；标准版和批量版会先把准备搜索的相关词列出来让你确认，不会默认把所有相关词都搜完。

If the user already states both scope and search filters, proceed without asking
again.

If the user states only the scope, such as "标准版", "B", or "批量版", but the
current conversation has not visibly shown the default platform, note type,
time range, and sorting, show those defaults first and ask the user to reply
"默认" or edits before any paid search.

If the user says "用默认" or "你看着来" after the default settings have been
shown, use Standard Version B unless the keyword is too broad or commercial
search cost is likely high.

## Search Scope Rules

Before calling Lingzao search tools, use `search-credit-notice.md` whenever the
scope involves paid search, multiple keywords, note details, comments, full
copy, subtitles, or transcripts.

Default search settings:

- Xiaohongshu first unless the user names another platform.
- Prefer recent content for fast-moving topics: last 1-3 months when available.
- Prefer 图文 when the user says 图文, no-face, cover, page design, or Xiaohongshu
  graphic note.
- Prefer most-liked for first discovery; use collect-descending when the user
  wants tutorials, checklists, or knowledge-base material.
- For beginners or low-follower users, prefer low-follower viral notes,
  same-stage accounts, or easy-to-copy formats. Do not lead with 100k+ or
  200k+ creators unless the task is mature positioning research.

If the user only replies A / B / C after the scope prompt above, treat it as
acceptance of the visible default settings: Xiaohongshu, 图文优先, 近半年, and
high-like/high-save discovery. If those exact defaults were not shown in the
current conversation, do not search yet; show the defaults and ask for "默认" or
edits before any paid search.

For Standard Version B, list the main keyword plus the 3 related keywords before
searching. Ask the user to reply "默认" to accept or replace any term. Do not
search hidden related terms.

For Batch Version C, list the 8-10 planned search keywords before spending
credits. Group them by intent when possible, such as audience, pain, result,
scenario, city, format, or product. Ask the user to confirm the list or cut the
scope.

Do not imply that the user pays per returned search result. Credit grows from
actual searches, profile analysis, note details, comments, full copy, subtitles,
and broader scope.

## Filtering Rules

After search, do not output all examples. Filter with A Tian's operating logic.

Keep examples that have at least one of:

- low-follower viral signal or same-stage learnability
- recent activity and not a stale one-off
- clear title keyword and click reason
- cover that says the topic in one second
- content structure the user can adapt truthfully
- strong save reason, comment demand, or series potential
- realistic production requirements for the user's current resources

Be careful with:

- big-account posts whose success depends on long accumulation, mature trust, or
  established IP
- question/interaction posts that may get comments but do not build followers
- posts that only ride a temporary news trend
- creators whose beauty, family background, city, money, job title, or
  production environment is the real traffic source
- good-product content that requires advanced photo, lighting, hand, home, or
  scene quality the user cannot produce yet
- AI tool content that depends on tools the user cannot actually use or explain
- travel content requiring constant travel, large budgets, polished footage,
  and strong on-camera performance

If results are weak or mismatched, say so and let the user choose a new filter:

这批结果可以参考，但和你现在能发的内容不完全匹配。如果直接照着做，很容易变成看起来热闹、实际不适合你。你更想按哪种方式重新筛？

A. 最近 30 天比较火的内容
B. 低粉爆款，适合小白模仿
C. 高收藏教程型内容
D. 高评论需求型内容
E. 商业/引流内容
F. 封面和标题参考

## Viral Selection Standards

Do not treat every viral note as a useful benchmark. Judge whether it can help
the user produce repeatable content.

### Keep For Analysis

Prefer notes/accounts with:

- follower count under 100k when visible, especially 20k-40k accounts or lower
  accounts with a sudden high-performing note
- a clear spike compared with the account's usual data
- a topic that belongs to the account's existing lane, or a useful contrast
  showing why one off-lane note exploded
- real comment demand: people asking, confessing, debating, saving, or sharing
  similar experience
- signs of experienced operation even if the account is low-follower: strong
  cover, clear title, precise topic, good action/expression, stable tone, or
  obvious content structure
- a formula the user can adapt without needing the same face, relationship,
  city, money, job, product, or production condition

When a low-follower post goes viral, do not say it is useful only because it is
low-follower. First judge whether it is a real beginner, a new account run by an
experienced operator, or a possible paid-boost/traffic-test case. Use the
learnable parts if the cover, title, topic, and structure show mature operation.

### Filter Out Or Mark As Not Copyable

Filter out or mark as "not directly copyable" when:

- the viral point is a rare personal event, such as a breakup one month before
  marriage, a dramatic family conflict, or another life event that most users
  cannot and should not imitate
- the audience is mainly comforting or supporting the creator, not asking for a
  repeatable method
- the note is a one-off emotional explosion and the account's normal content is
  in another lane, such as a fashion account suddenly going viral for a
  relationship story
- comments look fake, brushed, too generic, or unrelated to a real demand
- the traffic depends on a trending incident unrelated to the user's account
  direction
- the note gets likes or saves but does not create a reason to follow the
  account

Good wording:

这条确实爆了，但它不适合作为你现在的模仿对象。它爆的是特殊情绪和特殊经历，不是一个你能稳定复用的选题结构。我们可以学它怎么制造共鸣，但不要直接照着做。

### Interaction Posts

Question and interaction posts can be useful, but mostly for account activity.

Useful cases:

- a beginner account needs early comments and community signals
- an account is temporarily stagnant and needs a light engagement post
- local-life accounts ask city-specific questions, such as "香港有什么好吃",
  "台北有哪些避坑", or "你刷过很多次的店是哪家"
- the question stays inside the account's real lane

Be careful:

- if the user already has a clear account strategy, do not make interaction
  posts the main content formula
- interaction posts often do not build strong follower memory
- a generic "大家现在都在干什么" post may be active but not useful for growth

### Hot Topic Borrowing

Only borrow a hot topic when it naturally connects to the user's lane.

Examples:

- a food creator can discuss a viral duck-leg/goose-leg event through recipe,
  food safety, trust, or cooking angle
- a social commentary or women's growth account can discuss the same event
  through trust, choice, boundaries, or public emotion
- a sports or local-life account may use football/world cup topics only when
  the content lane makes the connection natural

Do not force every hot event into every account. If the user must "think very
hard" to connect it, it is usually not worth doing.

### Cover Good But Content Seems Empty

Do not dismiss a note only because the content feels light. A strong cover often
signals the creator has operation experience, and the inside may still be
structured enough for ordinary users.

Check:

- whether the title and cover create a clear click reason
- whether the opening fulfills the cover promise
- whether the content has a save point, emotion point, or scene point
- whether the account has repeated strong covers and coherent topics

If the cover is strong but the inside is weak, learn the cover formula only and
do not copy the content.

### High Saves Or Likes But No Follows

Explain why a post may collect likes/saves but not followers:

- the viral note is off-lane compared with the account's normal content
- the account is not vertical enough; users cannot predict what they will get
  after following
- the post is useful for one trip, one product, one emotion, or one hot event,
  but does not create long-term account memory
- travel notes, good-product notes, and emotional stories often get saves or
  likes without strong follow conversion unless the account has a clear repeated
  promise

When judging references, separate:

- suitable for traffic/activity
- suitable for saves/knowledge-base value
- suitable for follower growth
- suitable for account positioning

## Keyword Intent Library

Use this section to infer what the user may really want. If uncertain, ask only
one light question or give both paths in the output.

### 女性成长

Common user intents:

- They feel confused and want to learn how other women grow from zero.
- They are stuck in emotion, career, family, marriage, or identity and want
  examples for self-change.
- They already handle family, career, relationships, or self-consistency well
  and want to share their own method.

Split the keyword into sub-directions:

- 职场成长: workplace judgment, promotion, office relationships, career change,
  AI efficiency, side business.
- 情感/婚姻成长: relationship, marriage, children, emotional boundaries, family
  coordination.
- 自洽生活: living well in one's own context, small city, family nearby, modest
  income but stable life.
- 逆袭/身份变化: small-town youth to big-city white-collar worker, education
  upgrade, leaving family constraints, becoming a freelancer, traveling more
  freely.
- 学习/创业/向上: skill learning, side business, creator work, income expansion.

Good references:

- ordinary person with a visible before/after path
- small-town to city, college to graduate school, employee to freelancer,
  family-bound identity to self-owned life
- real personal bottlenecks that can become story, method, and series

Hard to copy:

- wealthy family background, very beautiful appearance, already excellent
  education, strong resources, luxury lifestyle
- vague inspirational posts without real event, scene, or method

Output should ask what the user wants to express: learning from others, sharing
their own growth, career, relationship, self-consistency, or transformation.

### 35岁职场

Common user intents:

- They are not yet 35 and fear a future career crisis.
- They are already around/after 35 and want to talk about layoffs, survival,
  career transition, or building a second curve.

Useful directions:

- how to avoid being replaced or laid off
- how to build one main income plus one side income
- how to use AI at work: PPT, reports, meeting notes, team efficiency, software
  workflows, hardware/recording tools
- what 35-year-old office workers are really doing
- career transition, freelancing, workplace politics, workplace self-protection

Related keyword field:

- 35岁职场, 职场危机, 裁员, 副业, AI办公, PPT, 会议纪要, 工作效率, 女性职场,
  人生, 生活, 成长, 工作

Be careful:

- question posts such as "大家 35 岁都在干什么" can attract interaction but may
  not build followers or account memory. Use them for activity only, not as the
  core growth formula.

### 好物分享

Do not treat "好物分享" as one track. First narrow the object and scene.

Possible sub-tracks:

- mother/baby and family
- home, laundry, cleaning, storage, kitchen
- travel goods
- personal lifestyle
- AI tools or digital products
- electronics and hardware
- perfume, lipstick, makeup, skincare
- clothing, accessories, bags, phone cases, toys, umbrellas

Judgment rules:

- Do not copy beauty or lipstick accounts if the user's real lane is family
  home goods.
- Good-product content looks easy but depends on photo composition, lighting,
  hands, nails, surface, home decor, angle, and scene.
- Product discovery must be sustainable. One accidental viral product does not
  prove a repeatable account.
- Ordinary people can do this, but must be more specific and refined than
  generic plog sharing.

Ask or infer:

- What category does the user actually buy, use, and recommend often?
- Do friends around them think they are good at finding useful things?
- Can they photograph products cleanly and consistently?
- Is there a repeatable scene or only random purchases?

### AI工具

Do not let the user copy every AI tool account. Match the tool lane to the
user's real identity and use case.

Possible sub-tracks:

- self-media and content creation
- workplace efficiency
- teachers and classroom PPT
- children and family education
- design, image generation, video generation
- agents, coding, GitHub, open-source workflows
- no-face graphic tutorials
- screen-recording / hand-pointing / AI-edited videos

Useful keyword expansion:

- AI工具
- 提升效率
- 如何使用AI
- 文科生的AI
- AI做图
- AI做视频
- AI办公
- AI自媒体

Be careful:

- If the user does not use teacher tools, do not recommend teacher-PPT content
  as their main benchmark.
- If using agents, GitHub, Codex, Claude Code, or overseas tools is hard for the
  user, treat these as advanced references, not beginner imitation.
- If the user cannot do spoken video, default to graphic tutorial, screenshot
  walkthrough, screen recording, or AI-edited short video.

### 本地生活

Default stance:

- Large cities, provincial capitals, tourism cities, and strong second/third
  cities are more suitable.
- Very small cities are hard unless the user does it for love, free meals, local
  community, or already has business resources. Commercial ads may be limited.

Check:

- What city is it?
- Is it a tourism city, provincial capital, or high-flow city?
- Are there enough young users and businesses?
- Can the user shoot food, storefronts, atmosphere, and routes well?
- Does the user want one district, the whole city, low-budget food, old stores,
  date spots, family routes, or high-end restaurants?

Good directions for cities like Shanghai:

- 20-yuan local food
- 30-year old restaurants
- district-by-district food lists
- what first-time visitors should eat
- landmark restaurants
- high-end restaurants with views
- old hotels, river views, historic neighborhoods

Be careful:

- Food is highly visual. The cover and first image must make people want to eat.
- Local-life monetization often depends on ads, group buying, shop resources, or
  city commercial density.

### 旅游攻略

First narrow the geography and resource model.

Possible lanes:

- one local city/region + tourism guide
- local life + local travel + food/store cooperation
- national or global travel
- hotel/B&B/travel-agency/resource-led content
- route, budget, itinerary, family trip, couple trip, solo travel, seasonal
  guide, avoidance guide

Be careful:

- National/global travel guides are difficult: money, materials, changing
  backgrounds, camera work, voice-over, personal appearance, clothing, and
  editing all matter.
- A 5-day or 10-day guide needs many materials and a strong structure.
- If the user stays in one place, local travel guide is more realistic than
  pretending to be a national travel blogger.

Good fit:

- user has B&B, local store, travel agency, food resources, or local expertise
- user can combine local tourism with food and lifestyle
- the place has searchable demand or tourism flow

## Content Package Output

For a Standard Version B request, output 5 content packages.

For each package, include:

| Block | Required content |
| --- | --- |
| 选题 | one clear topic, not a vague direction |
| 适合谁 | target audience and stage |
| 不适合谁 | mismatched audience, life stage, city, or click intent to avoid |
| 为什么值得发 | learnability, demand, save reason, or recent signal |
| 参考公式 | title/cover/content formula extracted from references |
| 标题 | 3 strongest title options, not a 10-title pool |
| 封面文案 | 1-2 cover copy options |
| 4页图文结构 | page-by-page text, suitable for fast testing |
| 正文方向 | short body outline or opening paragraph |
| 发布关键词 | 10 keyword candidates |
| 用户风格贴合点 | how it uses the user's previous content, favorite references, city, tone, or stated preference |
| 视觉建议 | no-logo default; cover style, main image, page layout, or prompt direction |
| 评论引导 | one comment prompt |
| 复盘点 | what to watch after posting |

Do not fully write all 5 bodies unless the user asks. Fully write only the top
1-3 most promising pieces.

Recommended batch rule:

- 10-20 entries: topic library, title direction, cover direction only.
- 5 entries: title, cover, structure, and keywords.
- 1-3 entries: full body, page copy, generated images when available or visual
  directions, 10 keywords, comment guide.

## Delivery Modes

Choose the output mode based on what the user asks for and what they can
produce.

### Graphic Note Mode

Use when the user asks for 图文, 小红书笔记, 5张图, 4页图文, 7页图文, or does not
want to do spoken video.

The user does not need to write image prompts. If they provide only a broad
topic such as 女性成长, search or inspect suitable public references within the
confirmed credit scope, extract the reusable angle, rewrite it into original
graphic-note content, and then route to visual generation when available.

Process:

1. Search recent or high-signal references within the confirmed scope. For
   broad tracks such as 女性成长, prefer recent posts from the last six months
   when possible, then filter by learnability.
2. List the selected reference notes briefly: title, creator, public signal,
   and why they matter.
3. Extract repeated keywords, key content angles, cover formulas, and comment
   demand.
4. Produce one complete graphic-note package first if the user is new or unsure.

Graphic note package must include:

- final title
- if title choice is still open, only 3 strongest title options with keyword
  anchor and click reason
- 5 image/page texts when the user asks for a complete first version
- optional 4-page quick structure and 7-page expanded structure
- cover copy
- each page's text, not just topic names
- generated images when available, or page-by-page visual direction / fallback
  prompt when image generation is not connected
- Xiaohongshu caption around 300-600 Chinese characters depending on content
  complexity
- 10 publishing keywords
- one comment prompt

### Spoken Script Mode

Use when the user asks for 口播, 视频文案, 逐字稿, or wants to read directly to
camera.

Spoken package must include:

- title under 20 Chinese characters when possible
- if title choice is still open, only 3 strongest title options with keyword
  anchor and click reason
- 600-character spoken script that can be read directly
- 300-character Xiaohongshu caption
- 10 publishing keywords
- optional cover text or opening frame text
- one comment prompt

The title should still carry the core keyword and click reason. Use proven title
formulas from the selected references, but do not copy titles directly.

### Vlog Storyboard Mode

Use when the user asks for Vlog, 日常记录, 生活方式视频, 分镜, or wants to show a
day-in-life process instead of only talking to camera.

Vlog package must include:

- title under 20 Chinese characters when possible
- if title choice is still open, only 3 strongest title options with keyword
  anchor and click reason
- core theme and emotional line
- 6-10 shot storyboard with concrete scenes and actions
- each shot's on-screen text or voiceover line
- opening 3-second hook
- suggested cover frame and cover copy
- 300-character Xiaohongshu caption
- 10 publishing keywords
- one comment prompt

Keep the storyboard realistic for a beginner. Prefer simple daily scenes such
as opening the window, making coffee or breakfast, exercising, commuting,
opening the laptop, working, reading, tidying the desk, walking outside, and
night review. Do not assume the user has cinematic equipment, strong editing
skill, or a polished home.

If the user sends reference Vlogs, first extract:

- what scenes repeat
- how the opening catches attention
- what emotion or identity the Vlog sells
- what can be copied with the user's real life
- what is hard to copy because of face, home, city, travel, money, or camera
  skill

### User-Style Rewrite Mode

Use when the user has previous posts, drafts, images, or favorite references.

Say that the version is based on their prior style:

基于你之前写过的内容和你喜欢的方向，我按你的语气重新写了一篇。

Then output:

- what style cues were used
- final title
- cover copy
- graphic-note pages, spoken script, or Vlog storyboard
- caption
- 10 keywords
- what still needs the user's confirmation

## Full Draft Structure

When refining one selected piece, produce only the fields needed for the chosen
publishing format. Do not force every content package into a graphic-note
template.

For graphic notes, produce:

1. final title
2. cover copy
3. 4-page graphic note text
4. optional 7-page expanded structure
5. body copy
6. 10 publishing keywords
7. generated images when available, or page-by-page visual direction / fallback
   prompt when image generation is not connected
8. comment guidance
9. publishing review instruction

For spoken video, produce:

1. final title
2. opening 3-second hook
3. 600-character spoken script
4. cover/opening frame copy
5. 300-character caption
6. 10 publishing keywords
7. comment guidance
8. publishing review instruction

For Vlog, produce:

1. final title
2. opening 3-second hook
3. 6-10 shot storyboard
4. voiceover or on-screen text for each shot
5. cover frame and cover copy
6. 300-character caption
7. 10 publishing keywords
8. comment guidance
9. publishing review instruction

For graphic notes or image outputs, if image generation is not connected, say:

我先给你每一页的文案、版式和做图指令；如果当前 Agent 接入了做图能力，下一步就可以直接生成图。你不需要自己写 prompt。

For graphic notes or image outputs, if image generation is connected, route the
selected full draft to `visual-generation-and-cover-workflow.md`. If the user
has no reference image, choose a default visual style from
`visual-reference-style-library.md`:

- travel / food / local life -> Travel Food Local-Life Cover
- AI tools / software / workflow with a face or screenshot -> AI Person Tool
  Infographic
- no-face tutorial / Lingzao / Agent / knowledge explanation -> Lingzao
  No-Person Knowledge Card
- product / course / offer / ecommerce -> Product Ecommerce Conversion Card
- WeChat article output -> WeChat Article Knowledge Pack

## Cover Style Judgment Library

Cover style is a core judgment layer. Do not only give abstract cover advice.
Tell the user what style fits the track and what is hard to copy.

### 女性成长 Covers

Common workable styles:

- Comfortable face + keywords: a kind, approachable, pleasant-looking person on
  cover, with clear big title, subtitle, keyword labels, readable colors, and a
  background with some visual value. If such a cover has hundreds of likes, the
  account likely already has a workable operation sense.
- Bright life-image: blue sky, flowers, sunlight, city landmarks, life-filled
  scenery, or a warm daily scene. Often works for self-consistency, life reset,
  and women's growth graphic notes.
- Cafe/computer/books: laptop, coffee shop, books, handwriting, notes, and study
  atmosphere. Often fits self-growth, learning, freelance, and office-transition
  stories.

Be careful:

- If the cover depends mainly on the creator's face, temperament, or lifestyle,
  ordinary users can learn the composition and keyword labels but may not copy
  the whole effect.

### AI Tool Covers

Common workable styles:

- person + tool/product + strong keywords
- AI-generated unified style, often harder and more technical
- before/after split screen: old workflow vs AI workflow, time saved, output
  comparison, image/video/result comparison
- desk setup: laptop, two or three screens, blue/purple lighting, GitHub window,
  chat window, code or agent interface
- screenshot walkthrough: screen, cursor, prompt, result card

Be careful:

- Very technical covers may attract clicks but are hard for users who do not
  actually use those tools.
- Do not recommend GitHub/agent/Codex-style covers to users who cannot explain
  or operate that workflow.

### Local Life Covers

Common workable styles:

- creator's face/persona + food/place, especially if the person is memorable,
  friendly, or has a clear local character
- food collage, place collage, four-grid or nine-grid lists
- one strong image: landmark, museum, park, shopfront, dish, street view, or the
  most beautiful frame from the place
- contrast/avoidance covers for 避坑, 踩坑, 脏乱, 不推荐, or warning topics

Be careful:

- Local life is crowded because it looks easy. Food and place covers must create
  desire, freshness, or usefulness immediately.
- If the image does not make people want to eat, go, save, or avoid, the cover
  is weak.

### Food, Travel, And Good-Product Covers

These tracks all sell "good things" or "desirable scenes".

Common workable styles:

- person + food/scenery/product
- one beautiful aspirational image that makes people want to click
- hand holding product in the real use scene
- product placed where it is used: bathroom product in bathroom, travel product
  on the road, makeup on vanity, kitchen product in kitchen
- premium product scene with carefully chosen jewelry, nails, background, and
  supporting products

Be careful:

- Hands, nails, lighting, surface, angle, color, background, and prop matching
  are often highly produced.
- Some creators will even match manicure color, shooting angle, music, and prop
  setup to copy a viral example. This is high-cost imitation and not suitable
  for most beginners.
- Ordinary users should usually start with AI-assisted graphic notes or simpler
  reference-image imitation instead of difficult video/photography production.

### Ordinary User Recommendation

For beginners and users who mainly want to start:

- prefer graphic notes first
- ask for reference images they like
- generate page copy, layout notes, and images when available; otherwise give
  fallback image-generation instructions
- avoid requiring long video shoots, complex editing, strong on-camera
  performance, or expensive product/scene preparation

Good wording:

你可以把自己喜欢的封面图或参考笔记发我，再给我一个主题。我先按这个风格给你出一张封面和一套图文内容。你找不到主题也没关系，先发你平时关注的关键词或账号，我来帮你找方向。

## Knowledge Base Follow-Up

After useful keyword research or batch content packages, offer to save the
results as a content asset library. Use `content-knowledge-base-workflow.md`.

Good wording:

这批内容已经不只是一次搜索结果了，可以沉淀成你的选题库、标题库和封面库。你现在有没有固定放知识库的地方？如果没有，我可以先生成 Markdown / CSV / Word / HTML 通用包，后面你想放飞书、Notion、阿里、腾讯或本地都方便。

## Final Continuation

Always end with one next action, not a menu of many things.

Choose one:

- 你从这 5 条里选 1 条，我继续帮你写完整正文和 4 页图文文案。
- 你发 1-3 张参考图，我按这个风格把其中一条做成可发的图文。
- 如果你要批量做，我可以把这批内容整理成选题库 / 标题库 / 封面库。
- 发出去以后，24 小时把笔记链接、后台截图、标题封面和脚本/正文发回来，我继续按发布后复盘帮你看曝光、点击、读完/完播、收藏、评论和关注转化。

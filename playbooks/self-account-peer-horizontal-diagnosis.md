# Self Account Peer Horizontal Diagnosis

Use this playbook when the user sends their own Xiaohongshu/Douyin profile and
asks Lingzao to compare it with same-track, same-stage, or same-follower-range
accounts.

This is not only benchmark discovery and not only own-account diagnosis. The
goal is to answer:

**Compared with people close enough to learn from, where is my account losing
clicks, memory, trust, follow reasons, and content system clarity?**

## Trigger Phrases

Route here when the user says things like:

- 拿我的账号和同级账号横向对比一下
- 找 5-15w 粉的 AI 博主和我比一下
- 找几个同赛道账号，看看我和他们差在哪里
- 我说话太快，帮我找同级账号对比他们怎么组织表达
- 找同赛道账号给我做一份详细报告
- 我想知道同级博主为什么比我更清晰
- 这几个账号和我比，我应该学什么

Do not route generic own-account concerns here by themselves. If the user says
"看看我现在的问题在哪里", "我是不是说话太快", "封面太花", or "没有重点" without asking
for horizontal comparison, peer accounts, same-stage accounts, or benchmarks,
use `self-account-diagnosis-report-template.md` instead.

If the user only asks to "find benchmark accounts", use
`benchmark-account-discovery-quality-gate.md` first. If they only send one
other creator and ask whether it is worth learning from, use
`comparable-account-breakdown-report-template.md`. If they send their own
profile without peer comparison, use `self-account-diagnosis-report-template.md`.

## Core Principle

The report should not shame the user or flatten their account into generic
"optimize title and cover" advice.

Good peer diagnosis does three jobs:

1. compress the user's current account into a frontstage memory point
2. select peer accounts that are close enough to learn from
3. turn the gap into concrete next content experiments

The strongest conclusion should often sound like:

你现在不是缺选题，也不是不会做内容，而是账号前台还没有把你的真实能力压缩成一个用户一眼能记住的身份。

## Input Contract

Minimum useful input:

- the user's own profile link
- target track or keyword, such as AI, female growth, local life, good products,
  career, parenting, health, or knowledge blogger

Helpful optional input:

- desired peer follower range, such as 5-15w
- known concern, such as 说话太快, 封面太花, 不涨粉, 不知道主页哪里乱
- format preference: graphic note, spoken video, Vlog, mixed
- target audience or monetization goal
- accounts the user already likes or wants to compare against

If the user already gave enough context, do not block on more questions. Use the
available evidence and clearly mark unknowns.

## Peer Selection Rules

Default first round:

- choose 3-5 peer accounts, not 10-20
- prefer active accounts with visible recent updates
- prefer accounts with recent high-performing notes or at least one clear spike
- match track, user audience, content format, and stage as much as possible
- show direct profile links when available, not raw IDs
- include follower count, total liked count, latest update, and representative
  high-performing notes when available

Follower range:

- If the user gives a range such as 5-15w, honor it as the main peer pool.
- If fewer than 3 accounts pass the quality gate, say so and add nearby-stage
  accounts as secondary references.
- 40w+ or mature big accounts can be used as positioning references, not
  ordinary imitation targets.
- Low-follower high-viral accounts can be used for note-structure references if
  their operation quality is visible.

Do not recommend stale accounts as main peers. If update time is unknown, label
it unknown instead of pretending it is active.

## Analysis Workflow

### 1. Own Account Snapshot

Read or infer:

- follower count, total liked count, public note count, update rhythm
- bio, nickname, avatar, pinned notes
- recent covers and visible content formats
- recent high-performing notes and normal baseline
- repeated keywords, identity markers, proof assets, and commercial signals

Before a deep conclusion, apply the sample-size gate from
`self-account-diagnosis-report-template.md`. If there are too few public notes,
call it a light peer scan instead of a full horizontal diagnosis.

### 2. Frontstage Memory Point

Condense what the account currently looks like to a new visitor.

Judge whether the visitor can answer in 3 seconds:

- who is this person?
- what does this account help me do?
- why should I follow now?
- what result or lifestyle does this account prove?

For AI / Agent accounts, avoid reducing the creator to "AI 工具号" when their
real asset is stronger. Look for sharper memory points such as:

- 文科生把复杂工具做出来
- 一人公司后台
- 普通人 Agent 实验室
- 内容中控台
- AI 作业本
- 用 AI 把生活、内容和商业化系统化

### 3. Peer Account Table

For each selected peer, include:

| Field | Requirement |
| --- | --- |
| account | name plus direct profile link when available |
| follower count | show exact or marked unknown |
| total likes | show exact or marked unknown |
| update state | latest visible update or unknown |
| representative works | recent high-performing notes with metrics when available |
| why selected | what it proves for this comparison |
| what not to copy | hidden resources, mature-stage advantage, face/team/tech/city assets |

### 4. Horizontal Comparison Dimensions

Compare the user's account against peers across these dimensions:

- **Account memory**: can users repeat what this account stands for?
- **Audience promise**: who is it for, and what result can they expect?
- **Title click reason**: keyword anchor, contradiction, result, number, time,
  question, or identity hook.
- **Cover hierarchy**: first-eye result, second-eye identity, third-eye benefit.
- **Opening / first 3 seconds**: one result or one problem before background.
- **Speech / information speed**: fast speech can be energy, but screen
  hierarchy must slow down the user's brain.
- **Content structure**: one main keyword per note; avoid pouring the whole
  brain into one video.
- **Proof system**: app, workflow, dashboard, knowledge base, case, data,
  before/after, customer result, or real life scene.
- **Columnization**: whether old hits are becoming repeatable columns.
- **Comment demand**: whether comments ask for tutorial, template, software,
  address, next part, or only praise.
- **Follow reason**: whether the homepage promises more similar value.
- **Commercial path**: whether the account can attract suitable customers, not
  only attention.

## Common Gap Library

Use these only when evidence supports them.

### Fast Speech But Weak Hierarchy

Do not simply say "you speak too fast".

Better diagnosis:

你说话快本身不是问题。快是你的能量和感染力。真正的问题是：当一条内容同时塞进工具名、步骤、结果、个人故事、商业化、知识库和 Agent，用户的大脑来不及分类，所以他会觉得你很厉害，但不知道这一条该记住什么。

Action:

- first 3 seconds: only one result
- first 10 seconds: only one problem
- one note: only one main keyword
- subtitles: fewer but heavier keywords

### Decorative Cover Without Visual Hammer

Do not simply say "封面太花".

Better diagnosis:

问题不是花，而是花没有变成视觉锤。好的封面要让用户第一眼看到结果，第二眼看到人设，第三眼看到利益。你有时把人、工具、教程、结果、关键词、产品名全放上去，用户反而不知道先看哪里。

Recommended templates:

- result-showcase: finished app, workflow, cover wall, knowledge base, table
- system-breakdown: person on one side, dashboard/process/result on the other
- pain-to-result: confused state on one side, concrete system on the other

### Viral Assets Not Columnized

Diagnosis:

你不是没有爆款，而是爆款还没有被栏目化。老爆款应该变成用户能预期的系列，而不是一次性灵感。

Column examples:

- 文科生造物局: each note shows one thing made with AI
- 一人公司后台: content, tools, business, knowledge base, Agent worker
- AI 作业本: benchmark, cover, title, account, workflow breakdowns
- 普通人 Agent 实验室: one Agent solves one real work pain

### Bio Lists Experience But Not Follow Reason

Diagnosis:

简介里的经历是真的，但新访客需要的是关注理由。Do not only list job,
credentials, spouse, course, and cooperation signals. Compress them into a
clear promise.

Output a rewritten 100-character bio when this is a visible gap.

### Pure Tool Start Instead Of Human System Start

Diagnosis:

工具不是不能讲，但不要先讲工具名。先讲你遇到的真实任务、做出的结果，或这个工具如何变成你的后台员工。用户不是来记工具名的，他是来判断这个工具和他有没有关系。

## Report Output Structure

Default chat output should be a short executive summary plus offer to package
as Word / Feishu / HTML if the report is long. Full report structure:

1. **Report title**
   - account name
   - comparison scope
   - sample boundary and data caveats

2. **One-sentence diagnosis**
   - one screenshot-ready conclusion
   - explain why this is the real problem

3. **Own account snapshot**
   - follower count, likes, notes, bio, pinned/recent content
   - current frontstage memory point
   - strongest existing assets

4. **Peer account table**
   - 3-5 selected peers
   - follower count, total liked count, update state, representative hits
   - why selected and what not to copy

5. **Horizontal comparison table**
   - user account vs peers across memory point, title, cover, opening, proof,
     columns, comments, follow reason, commercial path

6. **Top 3 current gaps**
   - each gap must be based on comparison evidence
   - each gap includes one immediate repair rule

7. **What the user should not reduce themselves to**
   - e.g. not only AI tools, not only technical tutorial, not only lifestyle
   - preserve their real assets

8. **30-day adjustment plan**
   - week 1: frontstage memory point, bio, pinned notes, cover templates
   - week 2: run 3-4 columns, at least two notes each
   - week 3: turn old hits into repeatable series
   - week 4: record data and decide what to continue

9. **Next content experiments**
   - 6-12 topics, or fewer if the user asked for lightweight output
   - include title direction, cover direction, first line, keyword

10. **Human closing**
    - acknowledge that the account does not need to be pushed over
    - lower the next action to one small test
    - ask for one concrete return item: next title/cover, draft, note link, or
      24h data

## User-Facing Style

Prefer direct, warm, and useful sentences:

- 你不是要换方向，而是要收紧方向。
- 过去的内容不是废掉了，它们是在帮你试出哪些表达有信号。
- 这不是让你变成对标账号，而是让你把自己的强项压缩成更清楚的入口。
- 下一条先只验证一个东西：用户能不能一眼记住你是谁。

Avoid:

- "直接照抄这个账号"
- "你必须重做整个账号"
- "保证涨粉"
- generic advice without peer evidence
- long peer lists without explaining why each one matters

## Credit And Packaging Boundary

Use `search-credit-notice.md` before expanding into paid public-content lookup,
deep profile analysis, note comments, or broad peer discovery.

If the report is long, do not leave the user with a wall of chat text. Offer:

- Word report
- Feishu doc
- HTML/webpage preview
- knowledge-base-ready Markdown

Do not automatically sync to a knowledge base. Ask first and let the user choose
the destination.

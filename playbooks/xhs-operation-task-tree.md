# Xiaohongshu Operation Task Tree

Use this playbook when a Lingzao user wants to operate a Xiaohongshu account but
does not need another "course list". The goal is to route the user to a concrete
creator-operation task and produce a result.

Trigger phrases include:

- 灵造能帮我做账号运营什么
- 小红书运营任务树
- 不要给我上课，直接让我完成任务
- 我现在该做哪一步
- 给我一个小红书运营工作流
- 账号运营板块怎么分
- 用灵造做账号，从哪里开始

## Core Principle

Do not present this as "lesson 1 / lesson 2 / lesson 3".

Present it as:

- what the user is stuck on
- what material they should send
- what Lingzao will judge
- what deliverable they will receive

The user should complete one task first. Course/tutorial explanations are only
the instruction manual when a task is blocked.

## Task Tree

### 0. How To Use

Ask the user to pick the closest current task, or infer it from their wording:

| User state | Task | User sends | Lingzao delivers |
| --- | --- | --- | --- |
| They do not know what is wrong with the account | Homepage 3-second diagnosis | profile link | first-impression issue, one priority fix, next task |
| They saw a viral note but do not know whether to copy it | Viral copyability check | note link | learnable parts, non-copyable parts, adapted version |
| They do not know what to post today | Topic generation | keyword / track / account link | 3-5 postable topics, one top recommendation |
| They finished content but are unsure whether to publish | Pre-publish gate | title, cover, copy/script, keywords | clickability, cover recognition, opening hook, keyword embedding |
| They want a one-stop result | Content package | keyword / reference / account direction | title, cover copy, pages/script/storyboard, caption, keywords |
| They posted but data is weak | Post-publish review | backend screenshot, note link, copy/script | likely bottleneck and next-note fix |
| They want leads/customers | Acquisition path | product/service, profile, target customer | content columns, profile bio, pinned notes, comment/DM path |
| They have many saved examples but no system | Knowledge-base distillation | viral notes, covers, comments, reviews | topic/title/cover/comment/reference libraries |

## 1. Account Foundation Layer

This layer answers: does the homepage look like an account worth opening?

### Task 1: Homepage 3-Second Diagnosis

User sends:

- Xiaohongshu profile link

Lingzao checks:

- nickname
- avatar
- bio
- pinned notes
- recent covers
- memory anchor
- whether the account looks like a clear person, clear niche, or scattered notes

Deliver:

- what the account looks like in the first 3 seconds
- the most unclear part
- the first action to change
- sample-size boundary: if the account has too few notes, do a light diagnosis
  instead of forcing a full account report

### Task 2: Profile Bio And Pinned Notes

User sends:

- profile link
- target audience
- offer / monetization goal if any

Deliver:

- 100-character bio
- three pinned-note suggestions
- account keywords
- the reason a new visitor should follow

## 2. Benchmark Layer

This layer answers: who should this account learn from?

### Task 3: Find 5 Active Benchmark Accounts

User sends:

- track
- keyword
- city if local-life related
- account stage
- face/no-face
- preferred format: graphic note, spoken video, Vlog, or mixed

Deliver:

- up to 5 profile links, not raw creator IDs
- follower count and recent high-performing notes when available
- latest update recency
- why each account is worth learning from
- learnable / non-copyable parts

Do not return stale accounts as main references. Stale accounts may only be
marked as historical references.

### Task 3A: Compare My Account With Same-Stage Peers

User sends:

- their own profile link
- track or keyword
- optional follower range, such as 5-15w
- optional known concern, such as speech too fast, covers too decorative, weak
  focus, or unclear follow reason

Deliver:

- own-account snapshot and sample boundary
- 3-5 active peer accounts with profile links, follower counts, latest update
  state, and representative high-performing notes when available
- horizontal comparison across account memory, audience promise, title click
  reason, cover hierarchy, first 3 seconds, speech/information hierarchy,
  content columns, proof assets, comment demand, follow reason, and acquisition
  path
- top 3 current gaps and concrete fixes
- 7-day or 30-day adjustment plan
- a human closing that lowers the next action to one test, not a full account
  rebuild

Use `self-account-peer-horizontal-diagnosis.md` for this task. The point is not
to make the user become the peer account. The point is to show where similar
accounts make their memory point, cover/title hierarchy, opening, proof system,
and content columns clearer.

### Task 4: Judge Whether One Account Is Worth Learning From

User sends:

- one benchmark account link

Deliver:

- memory anchor
- content engine
- cover/title/script pattern
- hidden resources
- beginner copyability
- the first action to learn from it

## 3. Viral Note Layer

This layer answers: how to use a viral note without blindly copying it?

### Task 5: Break Down One Viral Note

User sends:

- one note link

Deliver:

- title click reason
- cover stop reason
- outline or script structure
- visible shooting / editing / graphic layout layer
- comment demand
- learnable parts
- non-copyable parts

### Task 6: Adapt The Viral Note Into My Version

User sends:

- viral note link
- own account direction

Deliver:

- adapted topic
- three titles
- cover copy
- graphic-note page outline, spoken script, or Vlog storyboard
- warning against hard trend-chasing when the track does not fit

## 4. Topic Layer

This layer answers: what should I post next?

### Task 7: Keyword To Topic Pool

User sends:

- keyword, such as female growth, 35+ career, AI tools, local life, good-product
  sharing

Deliver:

- user-intent branches under the keyword
- what fits beginners
- what fits experienced creators
- 3-5 postable topics
- one top recommendation to test first

### Task 8: Comments To Next Topics

User sends:

- note link or comment screenshot

Deliver:

- real demand in the comments
- which comments are just noise
- three next-topic ideas
- which one fits interaction posts and which one fits dry-good content

### Task 9: 7-Day Topic Table

User sends:

- account profile
- track
- near-term direction

Deliver:

- seven topics
- recommended format for each: graphic note, spoken video, Vlog, interaction
  post
- title direction, cover direction, keywords
- which posts serve follower growth, trust, or acquisition

## 5. Content Production Layer

This layer answers: can Lingzao produce something publishable instead of only
giving advice?

### Task 10: Keyword To One Complete Xiaohongshu Post

User sends:

- keyword
- account direction
- optional reference link

Lingzao first decides whether the user wants:

- graphic note
- spoken video
- Vlog
- cross-platform package

Deliver:

- three titles
- cover copy
- graphic-note pages / spoken script / Vlog storyboard
- about 300 Chinese characters of Xiaohongshu body copy
- 10 publishing keywords
- pre-publish checklist

### Task 11: One Content Asset To Multiple Platforms

User sends:

- mother content, transcript, article draft, screenshot, or oral idea

Deliver the basic package first:

- Xiaohongshu version
- Moments version
- WeChat public-account version
- Knowledge Planet version

Offer optional expansion only if needed:

- Bilibili
- video account / Douyin
- X
- podcast

## 6. Cover And Image Layer

This layer answers: what kind of image should the user make?

### Task 12: Single Cover Diagnosis

User sends:

- their cover image

Deliver:

- cover type
- whether it can be understood in one second
- whether the keyword is obvious
- track fit
- whether ordinary users can learn from this cover
- revision direction

### Task 13: Reference Image To My Cover

User sends:

- reference image
- own topic

Deliver:

- reference structure
- what to borrow
- what not to copy
- adapted cover copy
- image-generation or revision direction

### Task 14: No Reference Image, Choose A Cover Type

User sends:

- track
- keyword
- face/no-face
- material availability

Deliver:

- recommended cover type
- not recommended cover type
- main cover title
- visual structure
- if generated output is ugly, diagnose and repair instead of blindly
  regenerating

## 7. Pre-Publish Layer

This layer answers: can this content be posted now?

### Task 15: Pre-Publish Gate

User sends:

- title
- cover
- body copy or script
- keywords

Deliver:

- title clickability
- cover recognition
- first 3 lines / first 3 seconds
- natural keyword embedding
- drift risk
- top 1-3 fixes

## 8. Post-Publish Review Layer

This layer answers: why did this note not run?

### Task 16: 24h / 48h / 7d Review

User sends:

- backend data screenshot
- note link
- body copy or script

Lingzao checks:

- 3-second / 5-second data when available
- completion / retention
- likes
- collections
- comments
- click and interaction clues

Deliver:

- likely issue: cover, title, opening, rhythm, content, account-audience fit, or
  comment prompt
- next-note fix
- whether to change format: graphic note, spoken video, Vlog, or interaction
  post

## 9. Acquisition And Monetization Layer

This layer answers: is the account just getting attention, or attracting
customers?

### Task 17: Judge Acquisition Fit

User sends:

- profile link
- product or service
- target customer
- rough customer value if relevant

Deliver:

- who the account currently attracts
- whether they match the target customer
- content that attracts strangers
- content that builds trust
- content that converts

### Task 18: Design Acquisition Path

User sends:

- product/service information
- profile link

Deliver:

- profile bio
- pinned notes
- content columns
- comment-reply direction
- DM handoff copy
- viral topics that look lively but are not worth chasing

## 10. Knowledge Base And Automation Layer

This layer answers: how does one breakdown become reusable operating assets?

### Task 19: Save Viral Examples Into A Library

User sends:

- viral note links
- covers
- titles
- comments
- review results

Deliver:

- topic library
- title library
- cover library
- comment-demand library
- benchmark account library

### Task 20: Morning Topic, Evening Review

User sends:

- account direction
- recent breakdowns
- published notes

Deliver:

- morning candidate topics
- evening review checklist
- inferred direction from repeated breakdowns
- one narrowed next action

## User-Facing Wording

Use task phrasing, not lesson phrasing:

> 任务 1：把你的主页丢进来，做一次 3 秒诊断
> 任务 2：找一条你想模仿的爆文，拆它为什么爆
> 任务 3：把你最近一条笔记丢进来，拆点击 / 看完 / 收藏理由
> 任务 4：把评论区问题整理成下一轮选题
> 任务 5：生成未来 7 天选题表
> 任务 6：发完回来复盘一次

End with one next task, not a course pitch.

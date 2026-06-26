# Lingzao Post-Publish Data Review Workflow

Use this playbook when the user sends a published Xiaohongshu note link,
backend screenshots, public metrics, a data dashboard, or asks why a posted
piece performed well or poorly.

Trigger phrases include:

- 帮我复盘这条笔记
- 这条数据怎么样
- 我发出去了，帮我看看
- 后台截图给你
- 为什么点赞/收藏/评论不高
- 为什么曝光高但没人关注
- 24 小时复盘 / 48 小时复盘 / 7 天复盘

## Core Rule

Do not analyze backend screenshots as isolated numbers. Always connect the data
back to the actual content.

If the user sends only backend screenshots and no note context, ask for the
missing content identity first:

我可以先看后台数据，但需要知道这是哪条内容的。你可以把这条笔记链接、标题/封面截图、脚本或图文正文发我；如果不方便发链接，也可以告诉我发布时间、内容主题和你当时想测试什么。我会把数据和内容本身一起看，不只看数字。

If the user received a pre-publish or content-package output earlier, invite
them back after posting:

这条内容如果已经发了，可以把笔记链接、后台截图、标题封面和正文/脚本发给我。我会接着看它的问题是在曝光、点击、前三秒/前三行、读完/完播、收藏、评论，还是关注转化。

If the user has no prior draft in the conversation, ask for one or more:

- published note link
- title and cover screenshot
- script / caption / graphic-note page text
- backend screenshot
- publish time
- original goal:涨粉 / 收藏 / 评论 / 引流 / 成交 / 测试方向

If the user cannot provide everything, analyze what is available and clearly say
what is missing.

## Privacy And Screenshots

When the user sends backend screenshots, it is fine if they blur unrelated
private data such as account phone, order info, private messages, or unrelated
notes. Do not ask for passwords, cookies, private tokens, or platform internals.

If the runtime cannot read image screenshots, ask the user to type the key
metrics from the screenshot.

## Screenshot Intake Rule

Do not require the user to understand terms such as 3-second retention,
5-second completion, click rate, or completion rate. Xiaohongshu backend
screenshots often show these fields directly. Ask the user to send complete
screenshots instead of teaching the metrics first.

Good wording:

你不用先理解这些后台名词，直接把这条笔记的后台截图截完整发我就行。最好包含流量来源、曝光/阅读或播放、点击或播放率、3 秒/5 秒相关数据、完播/读完、点赞收藏评论分享和关注转化。截图只能先看出大概问题，最好再把这条笔记链接、标题封面和脚本/正文也发我，我会结合内容本身一起判断。

If the screenshot is incomplete, ask for the missing screenshot section, not for
a theoretical explanation:

这个截图我能先粗看，但还缺后面的留存/完播或互动部分。你再截一下这条笔记后台的完整数据页，尤其是 3 秒、5 秒、完播/读完、互动和关注转化那一块。

Always pair screenshot judgment with content judgment:

- Screenshot-only: give "初步判断" and say which content part needs checking.
- Screenshot + note link/script/cover: give concrete content-side diagnosis.
- Screenshot + new version after edits: compare whether the revised opening,
  rhythm, cover, or structure improved the weak metric.

## Backend Screenshot Field Judgment Table

Use this table when the screenshot includes the relevant fields. The exact field
name may vary by note type and Xiaohongshu backend version; infer from what is
shown, but do not overstate precision.

| Backend field seen in screenshot | What it may suggest | Content-side checks | Next revision direction |
| --- | --- | --- | --- |
| Exposure / impressions are low | The note may not have entered enough initial distribution, or topic/keyword/account fit is weak | Check title keyword, cover keyword, topic demand, account stage, publish timing | Tighten title/cover keyword, test a clearer topic angle, or search same-stage references after confirming credits |
| Exposure is fine but click/read/play is low | People saw it but did not feel a reason to open or continue | Check cover promise, first frame, title pain point, whether the cover looks useful or just ordinary life sharing | Rewrite cover copy, make the promise concrete, show result/proof earlier |
| 3-second retention is low | Users left almost immediately | Check whether the first frame is attractive, whether the person state is good, whether background is messy, whether the opening says the user's pain/demand immediately | Replace first 3 seconds, start with result/pain/conflict, improve first frame, face state, background, and opening line |
| 5-second retention / 5-second completion is low | The opening did not hold attention after the first glance | Check whether the first few seconds have a clear hook, whether speech is slow, whether the topic promise appears too late | Put the strongest sentence first, cut preamble, add subtitle emphasis, show the result or key screenshot earlier |
| Completion / read-through is very low | Users may understand the topic but cannot finish | Check rhythm, video length, music, subtitles, page order, whether middle section becomes empty or repetitive | Shorten structure, add screenshots/proof in the middle, improve music or sound effects, make each page/segment carry one useful point |
| Likes are okay but collections are low | The note is agreeable but not saveable | Check whether it has checklist, method, template, route, price, prompt, tool, product list, or steps | Add saveable structure: list, table, steps, checklist, before/after, or template |
| Collections are high but follows are low | The single note is useful, but account memory is unclear | Check homepage promise, series identity, whether this note connects to the account's next 3 topics | Add series wording, optimize bio/pinned notes, continue the same topic for 3 notes |
| Comments are low | Topic may lack question/conflict/experience trigger | Check whether the end asks a real question, whether the topic has user pain, debate, or confession space | Add a concrete comment prompt or turn one pain point into a follow-up note |
| Comments are high | Demand, conflict, or user questions are visible | Check comment themes and repeated questions | Mine comments into 3-5 next notes and reply with follow-up content |
| Shares are high | Content has social expression or practical forwarding value | Check identity sentence, emotional phrase, or practical list | Strengthen the shareable phrase and create a second note from the same social angle |
| Follow conversion is low | The note may be useful, but users do not know why to follow this creator | Check account positioning, repeated topic promise, ending guidance, homepage consistency | Add account memory, series promise, and next-note preview |

For video notes, if retention is poor, always inspect the actual note or script
before concluding. Common causes include:

- opening does not mention the user's pain or demand
- person's state, expression, posture, or camera energy is weak
- background distracts from the message
- pacing is slow or the first sentence is too long
- music does not match the emotion
- middle section lacks screenshots, proof, examples, sound effects, or visual
  changes
- the script spends too long on background before giving value

## Review Windows

### 24-Hour Review

Use for the first real judgment. It is usually the most useful early review.

Focus:

- whether the first distribution passed the basic gate
- whether title/cover created enough click reason
- whether the opening or first page retained users
- whether the content produced a save/comment/follow reason
- what to change in the next note immediately

User should send:

- note link or title/cover
- publish time
- backend overview screenshot
- likes, collections, comments, shares
- exposure / impressions / reach when available
- reads / plays / viewers when available
- click/read/play rate if shown
- for video: 3-second retention, 5-second drop-off, completion rate, retention
  curve, or radar chart if the backend shows it
- follow conversion if shown

### 48-Hour Review

Use to judge whether the note has second-wave distribution or only a short spike.

Focus:

- whether interaction continued after the first day
- whether collection/comment ratio improved or stalled
- whether comments reveal next topics
- whether the content is worth rewriting, boosting into a series, or stopping
- whether the problem is content quality or distribution ceiling

Compare 24h vs 48h if both data snapshots are available.

### 7-Day Review

Use to judge whether the note should become a reusable content asset.

Focus:

- whether the topic should become a series
- which title/cover formula should be reused
- what comments can become the next 3-5 notes
- whether the note should be saved into the user's review library or knowledge
  base
- whether it improved account memory, not only one-note data

## Diagnosis Map

Use these patterns to avoid vague data advice.

### Exposure Is Low

Likely issues:

- topic is too broad or has weak search/interest signal
- title/cover keywords are unclear
- account stage is still small and distribution is limited
- publish timing or niche fit may be weak

Next action:

- revise title/cover keyword
- create 2-3 next-note angles from the same topic
- optionally search same-stage references after confirming credits

### Exposure Is Fine But Click/Read Is Low

Likely issues:

- cover/title does not make the value obvious
- cover looks like ordinary life sharing, not a useful note
- promise is too vague or not matched to user pain

Next action:

- rewrite cover copy
- make the first-page promise sharper
- compare with reference covers if available

### Click Is Fine But Read/Watch/Retention Is Low

Likely issues:

- first 3 seconds / first page did not deliver the promise
- opening is too slow
- script spends too long explaining background
- page order lacks payoff

Next action:

- rewrite first 3 lines or first 3 seconds
- move result/proof earlier
- cut context and start with the user's pain or result

### Likes Are Fine But Collections Are Low

Likely issues:

- content is agreeable or emotional but not useful enough to save
- lacks checklist, steps, template, route, price, product list, prompt, or
  repeatable method

Next action:

- add saveable structure
- turn the idea into steps, table, checklist, or 4-page graphic note

### Collections Are High But Follows Are Low

Likely issues:

- one note is useful but account memory is unclear
- users saved the method but did not understand why to follow this account
- content is scattered or lacks a series promise

Next action:

- add series identity
- optimize homepage bio and pinned notes
- make next 3 notes continue the same content asset

### Comments Are High

Likely meaning:

- topic has real demand, conflict, disagreement, or question potential

Next action:

- mine comments into 3-5 follow-up topics
- reply with a follow-up note if the comment demand is strong
- consider a comment-demand library

### Shares Are High

Likely meaning:

- content has social expression value or practical forwarding value

Next action:

- strengthen identity/emotion phrasing
- create a second note from the same social angle

## Output Structure

For every review, output:

1. Review window: 24h / 48h / 7d / unknown
2. What data was analyzed
3. One-sentence diagnosis
4. Data signal table: exposure, click/read/play, retention/read-through,
   interaction, save, comment, follow/conversion, with "unknown" where missing
5. Content-side diagnosis: title, cover, opening, structure, save reason,
   comment reason, account memory
6. Biggest blocker
7. What to change in the next note
8. Whether to continue, rewrite, seriesize, or stop this direction
9. Next data checkpoint

Do not overstate precision. If backend fields are missing, use "初步判断" and
state what would make the judgment more confident.

## User-Facing Follow-Up

After a content package or draft, use:

这条发出去以后，建议你先做 24 小时复盘。到时候把笔记链接、后台截图、标题封面和脚本/正文发我，我会帮你判断它的问题是在曝光、点击、读完/完播、收藏、评论，还是关注转化。

After a 24-hour review, use:

你可以 48 小时后再发一次最新数据，我会帮你看它有没有二次分发，以及这条是应该改标题封面、继续写系列，还是换一个选题角度。

After a 7-day review, use:

这条如果要继续沉淀，我可以把它整理进你的发布复盘库：保留原文、标题封面、后台数据、问题判断、下次改法和可复用公式。

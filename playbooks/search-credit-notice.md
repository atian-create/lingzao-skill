# Lingzao Search Credit Notice

Use this whenever a task may trigger Lingzao search, account lookup, note lookup, keyword research, comparable-account research, comment lookup, transcript lookup, full-copy lookup, or batch reference discovery.

## Core Rule

Tell the user the search choices and credit logic before running the search.

Use the current backend pricing truth from Lingzao code:

- 普通公开内容搜索 / 创作者搜索 / 主页资料 / 主页近期内容 / 单篇详情：20 credits/次。
- 评论区：20 credits/页，只返回一级评论分页。
- 主页深度解析：1-20 条作品 50 credits；21-40 条作品 100 credits。
- 短视频文案提取：调用前余额需至少 50 credits/条 URL；成功后按真实时长 10 credits/分钟、最低 1 分钟扣费。

Important nuance:

- Do not describe `search-notes` as “20 credits per returned note”. One normal note search can return multiple results within its limit.
- For keyword reports, each actually searched main keyword or related/dropdown
  keyword is one `search-notes` lookup. For example, main keyword + 5 related
  terms means 6 searches, usually about 120 credits. Do not imply that all
  dropdown terms are searched inside one 20-credit call.
- But if the Agent opens selected notes for详情、评论、正文、字幕、逐字稿 or deeper structure, each added action may create more credit usage.
- For benchmark-account discovery, creator search alone is not enough. If the
  Agent needs to verify whether candidate accounts are still updating and have
  recent high-performing works, each profile/recent-post check may add separate
  lookup cost. Explain this before expanding from discovery to verification.
- For benchmark-account discovery, the default first round should verify enough
  candidates to return up to 5 strong accounts. Returning 10-20 accounts,
  filtering by a specific follower range, or continuing multi-account
  verification is a broader batch search and should only happen after the user
  confirms the range.
- Benchmark-account outputs should show follower count, total liked count, and
  recent-hit note metrics when available. If creator search does not return
  profile stats for the selected candidates, opening profile info for the final
  candidates can add lookup cost; explain that before expanding.
- One Agent instruction can combine several Lingzao actions, so it is not equal to one fixed 20-credit action.

The user must understand:

- Credit is counted by actual searched objects/content depth, not by how many messages they send to the Agent.
- One Agent instruction can trigger many Lingzao searches.
- 基础搜索 / 普通搜索 looks at visible/basic public signals such as title, cover, likes, collections, comments count, author/profile signals, links, and basic copy/summary fields returned by the normal search.
- 深度搜索 further opens or analyzes full copy/body text, subtitles, transcript, detailed note content, or deeper text structure.
- If a task mixes both layers, explain that the final credit usage depends on how many basic objects and deep content objects are actually opened.
- Deep search can involve dozens of accounts, many keyword searches, full-copy lookups, or 50+ searches, so it must be labeled before starting.
- For account diagnosis, distinguish the homepage's visible public-note count
  from the deep-analysis limit. Fewer than 10 public notes should usually be
  downgraded to beginner setup, homepage first impression, starter-account mini
  diagnosis, or light account analysis instead of a full report. Standard
  diagnosis starts becoming reasonable around 10 visible notes; 20+ notes fits
  `analyze-user-profile --limit 20`; 40+ notes fits deeper diagnosis or
  distillation after confirmation.
- Creator distillation can be light, standard, or deep. A standard distillation
  target may organize about 50 representative entries, but current homepage
  deep analysis fetches up to 40 works per confirmed call; if more entries are
  needed, explain that follow-up searches, note details, comments, or copy
  extraction may add separate credit costs.
- Post-diagnosis activation has two scopes. A light action package based only on
  the already produced diagnosis does not need extra Lingzao search. A deeper
  action package that finds new benchmarks, opens more note details, reads
  comments, analyzes backend screenshots with note context, or builds a 7-day /
  30-day content package may add credits. Explain this before expanding.
- For anything that may expand beyond one known link or move into full copy/body text, ask the user to choose 基础搜索 or 深度搜索 first.
- Do not let the Agent choose a large or deep search scope by itself.

## Choice-First Rule

Before searching, show the user two clear options:

### A. 基础搜索

Use when the user wants a quick result or does not want to spend many credits yet.

What it does:

- inspect 1 known account, 1 known note, or a small limited set
- return the most important visible signals
- look at title, cover, likes, basic metrics, links, author/profile signals, and normal-search copy/summary
- give a first judgment, not a complete market scan

What the user gets:

- for an account: current stage, obvious content assets, biggest blocker, first next step
- for a note: title/cover/content structure, why it may perform, what can be reused
- for keyword/reference tasks: a small starter sample and initial direction

Credit framing:

- lower-scope, controlled search
- ordinary search/list/profile/detail actions are commonly 20 credits/次
- homepage deep analysis is not the same as a basic homepage list: 20 works is 50 credits, 40 works is 100 credits
- if the user wants to expand after seeing the first result, ask again before continuing

### B. 深度搜索

Use when the user wants references, trends, topic pools, keyword clusters, full-copy analysis, transcript/subtitle analysis, or a fuller report.

What it does:

- inspect multiple keywords, accounts, notes, or comment areas
- further open/analyze full copy, note body text, subtitles, transcripts, or detailed content structure when needed
- compare patterns instead of only looking at one object
- find stronger references and repeated signals

What the user gets:

- benchmark groups
- low-follower viral examples
- content/keyword clusters
- deeper hit-mechanism comparison
- full-copy/script/content-structure analysis
- richer title/topic/action output

Credit framing:

- broader and deeper search
- final usage depends on the number of objects and deep content items opened
- single note detail/comment/detail expansions can add 20 credits/次 or 20 credits/页
- profile deep analysis is 50 credits / 20 works or 100 credits / 40 works
- video transcript extraction requires 50 credits/URL available before starting, then bills by duration at 10 credits/minute, minimum 1 minute
- ask for user confirmation before starting

## User-Facing Credit Notice

Use normal chat text, not a fenced code block.

For choice-first search:

先提醒一下：灵造不是按“你发给 Agent 的一条指令”来计算，而是按实际查看的账号、笔记和内容深度来计算。

你可以选：

A. 基础搜索：适合先快速判断。一般看标题、封面、点赞/收藏/评论等基础数据、链接、作者信息和普通搜索能返回的文案信息。普通搜索、主页近期内容、单篇详情这类基础查看通常是 20 credits/次；搜索结果一次可以返回多条，不是按返回的每一条都扣。

B. 深度搜索：适合做爆款深拆、账号诊断、脚本/逐字稿/正文结构分析、对标和选题池。会进一步查看完整文案正文、字幕、逐字稿或更深的内容结构，结果更完整，但范围也会更大。比如主页深度解析是 20 条作品 50 credits、40 条作品 100 credits；评论区按页查看；短视频文案按时长计算。

如果主页公开笔记很少，我会先降级处理：0 条做起号搭建，1-2 条做主页初印象和单篇反馈，3-5 条做起步号小诊断，6-9 条做轻量账号分析。一般 10 条以上才适合做正式账号分析，20 条以上更适合标准诊断报告，40 条以上才适合深度诊断或知识库蒸馏。

如果是博主蒸馏，要额外说明样本范围：快速蒸馏可以先看约 20 条；标准蒸馏优先使用目标博主自己的公开作品，当前主页深度解析一次最多先看 40 条；如果目标博主只拿到 40 条，就如实按 40 条目标样本说明。用户确认后的关键词搜索结果或对标账号内容只能放进单独的 benchmark/reference 区，不能算作这个博主的代表样本补足；单篇详情、评论区和文案提取只用于丰富已选样本，不算新增样本；深度蒸馏可能涉及更多账号、关键词和笔记，必须先确认范围。

你回复 A 或 B，我再按你选的范围开始；不会默认替你扩大搜索，也不会自动把基础搜索升级成深度搜索。

For a small/default lookup:

先提醒一下：这次我会先按基础搜索来做，主要看标题、封面、互动数据、链接和普通搜索能返回的基础文案信息。基础查看通常是 20 credits/次；如果后面要继续看完整正文、逐字稿、字幕、评论区分页或更多参考内容，我会先告诉你会增加哪些查看范围，再让你确认。

For batch reference search:

先提醒一下：这次会涉及批量搜索。普通搜索一次可能返回多条结果，但如果继续打开很多账号、单篇详情、评论区或完整文案，积分会跟着增加。基础搜索主要看多个账号/笔记的标题、封面、互动数据和基础文案信息；如果还要进一步深读其中的完整文案、字幕、逐字稿或内容结构，则会进入深度搜索。我会先按你确认的范围来查，不会默认无限扩展。

For benchmark-account discovery:

我会先按「持续更新 + 近期高互动 + 和你阶段匹配」来筛，但首轮不建议一次给你 10-20 个账号。这样会消耗更多查看和验证范围，也容易看乱。我这边先给你 5 个你看看是否适合你；如果你想把粉丝数量、账号阶段、内容形式或城市范围规定下来，我再按这个条件继续帮你搜。

如果搜索结果里已经有粉丝数、总获赞和近期作品数据，我会直接列出来；如果最终候选缺这些主页数据，补开主页资料会增加查看范围，我会先说明。

For deep search:

先提醒一下：你这个需求属于深度搜索，可能会涉及不同关键词、多个账号/笔记，以及完整文案正文、字幕、逐字稿或内容结构分析。主页深度解析目前按 20 条作品 50 credits、40 条作品 100 credits 计算；如果还要打开单篇详情、评论区或提取视频文案，会另外按对应范围计算。开始前我会先给你一个搜索范围，你确认后再继续。

## Search Type Labels

### 基础搜索

Use when:

- the user sends 1 homepage link
- the user sends 1 note link
- the user asks to inspect a small number of known links
- the task only needs a few direct lookups
- the task can be answered from titles, covers, basic metrics, links, and normal-search copy/summary

Explain:

- basic search is the lower-scope option
- if more links are needed, ask or state the additional scope before expanding
- if full copy/body text/subtitles/transcripts are needed, tell the user it becomes deep search first
- make clear that this is a quick first judgment, not a full market scan

### 批量搜索

Use when:

- the user asks for several references
- the user asks to compare multiple accounts
- the user asks for 10+ accounts or 10+ notes
- the task likely needs 10-30 note/account lookups
- benchmark-account discovery needs more than the default first 5 accounts, or
  needs follower-range filtered verification across many candidates

Explain:

- final usage depends on the number of accounts/notes actually inspected
- if the task also needs full copy/body text/subtitle/transcript lookups, the deeper layer should be confirmed separately
- do not silently expand the search range
- if the task could be done as either basic or deep search, ask the user to choose first

### 深度搜索

Use when:

- the user asks for broad keyword research
- the user asks to find trends across multiple keywords
- the user asks to scan many creators, many notes, or multiple categories
- the user asks to analyze full copy, subtitles, transcript, note body text, or detailed script/content structure
- the task likely needs 50+ searches

Explain:

- this is not a small single-link lookup
- provide a planned scope before starting
- proceed only after the user confirms the scope

## Placement

Show the notice before the first search call, not after results.

If the user sends a single link and the task can be answered from that one link, the notice can be short.

If the task may expand into finding references, keywords, topics, comments, full copy, subtitles, transcripts, or many examples, use the batch/deep notice first.

If the task can be answered in either a quick way or a complete way, use the choice-first notice and wait for A/B.

## Tone

Be transparent and plain-spoken. Do not sound defensive.

Good framing:

- “先提醒一下”
- “我先按基础搜索”
- “如果要扩大到对标/关键词/更多笔记，我会先告诉你范围”
- “如果要看完整文案/字幕/逐字稿，会按深度搜索来确认”

Avoid:

- “默认参数”
- “系统将扣费”
- “消耗 token”
- “接口调用”
- “默认花不了多少”
- “我先全部查完再说”

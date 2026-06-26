# Benchmark Account Discovery Quality Gate

Use this playbook when the user asks Lingzao to find benchmark accounts,
reference creators, same-track accounts, low-follower viral accounts, or
accounts worth learning from.

This is a product-quality gate, not only a search prompt. Users should not have
to remember to add "持续更新并有爆款作品的账号" every time. That should be the
default quality standard when Lingzao finds benchmark accounts.

## Core Decision

The answer to the user's feedback is:

不用每次都自己加这句话。灵造默认就应该按「持续更新 + 近期有高互动作品 + 和你阶段匹配」来找对标账号；如果你自己已经找到账号，也可以直接发给我，我会帮你判断它值不值得学、适不适合你、哪些能学、哪些不能照抄。

So the workflow has two valid entrances:

1. User asks Lingzao to find accounts:
   - Lingzao must search and then verify freshness, hit performance, and stage
     fit before recommending.
2. User sends accounts they found:
   - Lingzao should skip discovery and use
     `comparable-account-breakdown-report-template.md` to judge fit.

Do not put the burden on the user to write perfect search wording.

## Default Discovery Standard

When the user asks for benchmark accounts, default to active, learnable
accounts:

- Active: still updating recently.
- Proven: has at least one recent high-performing work or a clear spike.
- Relevant: belongs to the user's track, format, and audience.
- Learnable: the user can imitate structure, topic, title, cover, or operation
  logic without needing the same face, wealth, city, job, product, team, or
  mature follower base.
- Stage-fit: beginners should see same-stage, low-follower, or early-path
  references first; mature accounts can appear as positioning references, not
  copy targets.

## Context And Transfer Rules

Infer the user's interest from repeated requests. If the user keeps sending
similar accounts or notes, say the pattern back:

我发现你最近让我拆的内容都集中在「某某方向」。你是不是最近对这个方向感兴趣？你现在有自己的账号吗，还是先在找方向？

Use city only when city matters:

- For female growth, AI tools, career, health, fashion, good products, and most
  personal-IP content, city is usually not a main benchmark filter unless the
  user says it matters.
- For food, travel, local life, stores, city guides, city events, and local
  services, city matters for publishing, positioning, keyword, location, and
  audience.
- Local-life examples can transfer across cities. If a Nanning creator sends
  Yunnan, Beijing, Kunming, Shanghai, or other city references, do not call it
  scattered by default. They may be learning shooting style, topic selection,
  cover style, title formula, route design, or comment demand, then applying it
  to Guangxi/Nanning.

If references suddenly jump to a truly different audience or track, ask whether
this is still the old account direction or a new account direction. Then judge:

- can this be a new series inside the current account?
- should it become a separate account?
- will it confuse the target user?
- which parts are safe to borrow without changing account positioning?

## Display And Ranking Defaults

Do not make the user open every profile link just to judge whether an account is
worth learning.

For each recommended benchmark account, show these visible fields when
available:

- direct Xiaohongshu homepage link
- follower count
- total liked count / total account likes
- latest update time or latest visible post date
- content format: 图文、口播、Vlog、探店、美食、AI 教程、混合 etc.
- recent-hit works from the last 30 days when available, including note title,
  note link, public likes, collections, comments, and publish date
- why this account can be a benchmark
- what not to copy

Default ranking:

- Sort the first recommendation table by follower count from high to low when
  follower counts are visible.
- If follower count is missing for some accounts, put known-count accounts
  first and keep unknown-count accounts lower with "粉丝数未返回".
- Do not sort only by personal preference or search-result order when follower
  data is available.

If `search-users` already returns follower and liked counts, reuse those
numbers. If the final 5 candidates are strong but profile stats are missing,
either call `get-user-info` for the selected candidates after credit framing, or
mark the field as unknown; do not silently omit the field from the output.

## Default Result Count

The first visible delivery should be 5 accounts, not 10-20 accounts.

Use this user-facing wording before or after the first recommendation table:

我这边先给你 5 个你看看是否适合你；如果你想把粉丝数量、账号阶段、内容形式或城市范围规定下来，我再按这个条件继续帮你搜。

Rules:

- Verify enough candidates to return up to 5 strong accounts in the first
  round.
- Do not default to 10-20 benchmark accounts. That becomes a broader batch
  search and may spend more credits.
- If fewer than 5 candidates pass the active/recent-hit/stage-fit gate, return
  the actual number and explain why the rest were filtered out.
- Only expand beyond 5 when the user asks for more or confirms a clearer
  follower range, stage, city, audience, or format.
- If the user wants follower count control, first narrow the follower range
  before continuing the search instead of spending credits on broad discovery.

## Freshness Defaults

Use these as defaults unless the user gives another range:

- If the account updated within the last 15 days and the track/format fits, it
  can be directly included as an active candidate after the normal benchmark
  checks.
- Prefer accounts with at least one high-performing work in the last 30 days.
  For ordinary users, "最近一个月有爆款内容" is easier to understand than an
  abstract "recent-hit status".
- Fast-changing tracks such as AI tools, local life, hot topics, platform
  operation, and content workflows: last post ideally within 30 days; recent
  high-performing work ideally within 90 days.
- Evergreen tracks such as parenting, career, female growth, beauty, good
  products, health, and travel guides: last post ideally within 60 days; recent
  high-performing work ideally within 180 days.
- If an account has no public update in 90+ days, do not recommend it as a main
  benchmark unless the user explicitly wants historical archive analysis.
- If an account has no public update in the most recent month, usually do not
  recommend it as a main benchmark. Treat it as historical reference at most,
  especially when the user expects current benchmark accounts.
- If update dates are unavailable, mark freshness as unknown and do not rank it
  above verified active accounts.

Definition:

- "Recent active benchmark" means there is visible recent activity plus at
  least one work that performs noticeably better than the account's usual level
  or has strong public interaction.
- "Historical reference" means the account has useful positioning, title,
  cover, or content structure, but is not suitable as a current main benchmark
  because it stopped updating or its old viral works may not reflect the
  current platform environment.

## Recommended Search Flow

Before searching, follow `search-credit-notice.md`.

### If User Only Gives A Track Or Keyword

Example: "帮我找女性成长对标账号"

1. State the default quality gate in user language:

   我默认不只按关键词搜账号，会优先筛「还在持续更新、近 90/180 天有高互动作品、和你阶段匹配」的账号。断更很久的账号我最多放到历史参考，不会当主对标推荐。

   我这边先给你 5 个你看看是否适合你；如果你想把粉丝数量、账号阶段、内容形式或城市范围规定下来，我再按这个条件继续帮你搜。

2. Confirm or infer:
   - track / keyword
   - target audience
   - user's current stage if known
   - preferred format: 图文、口播、Vlog、本地生活、好物、AI 教程 etc.

3. Candidate collection:
   - use creator search for the keyword when suitable
   - use note search for recent high-performing notes when creator search gives
     old or weak accounts
   - collect candidate authors from recent high-performing notes when possible

4. Candidate verification:
   - verify enough candidates to return up to 5 strong accounts in the first
     round
   - inspect recent public posts for each candidate before recommending
   - check latest update time
   - if the last visible update is within 15 days, treat freshness as strong
   - check whether the recent works include high-performing or clearly
     above-average posts
   - prefer the account's high-performing works from the last 30 days; if none
     are available, say so instead of implying it has a current hit
   - write down the specific high-interaction works that made the account pass:
     title, note link, publish date when available, and visible likes/
     collections/comments
   - check whether the content lane is stable or only had one unrelated spike
   - check whether the format and resources are learnable for the user
   - filter out long-stale accounts, especially those with no recent-month
     updates
   - avoid treating 400k+ pure big accounts as ordinary imitation targets; use
     them only for mature positioning, broad market signal, or historical
     reference unless there is a very specific learnable part
   - when the user sends 100k-300k accounts, inspect briefly but clearly
     separate "可以局部参考" from "不建议现阶段照抄"
   - inspect comment quality: comments such as "太棒了", "太好了", "真的吗"
     may be low-value or inflated interaction; comments such as "求教程",
     "这是什么软件", "收藏了", "我也遇到这个问题", "求地址", "怎么做"
     indicate real demand and are more useful for benchmark judgment

5. Output ranked accounts only after verification. Default to sorting visible
   recommendations by follower count from high to low.

### If User Sends Their Own Found Accounts

This is often better when the user already has taste or a niche reference.

Do:

- say "可以，直接发你找到的账号会更精准"
- analyze each account with `comparable-account-breakdown-report-template.md`
- still check freshness and recent-hit status
- judge whether it is a main benchmark, local reference, historical reference,
  or not recommended

Do not:

- treat every user-provided account as worth copying
- skip stage-fit judgment
- ignore that an account may be stale even if the user likes it

## Candidate Labels

Every recommended account should receive one label:

- 主对标：active, relevant, recent-hit, and stage-fit.
- 局部参考：some parts worth learning, but not the whole account.
- 历史参考：good old structure or positioning, but stale or not current.
- 趋势观察：useful for topic direction, not for direct imitation.
- 不建议学：stale, mismatched, too resource-dependent, off-track, or
  unlearnable for the user.

## Output Structure

For benchmark discovery, output:

1. 一句话判断：本轮是否找到了真正适合学的账号。
2. 筛选标准：say the default gate used, such as "持续更新 + 近期爆款 + 同阶段可学".
3. 推荐账号表:
   - default first round: up to 5 accounts
   - account name and direct Xiaohongshu profile link
   - follower count and total liked count / total account likes when available
   - freshness
   - latest visible update date or "半个月内有更新" when that is known
   - content format, such as 口播 / 纯图文 / 图文知识卡 / Vlog / 探店 / 混合
   - 1-3 recent high-interaction works, each with note title, note link,
     publish date when available, and public likes/collections/comments
   - follower/stage if visible
   - content lane
   - why it is worth learning
   - what not to copy
   - label
   - if fewer than 5 accounts pass, state the actual count instead of filling
     the table with weak accounts
4. 被筛掉的账号类型:
   - long-stale accounts
   - old viral-only accounts
   - big accounts with mature trust only
   - 400k+ pure big accounts that mainly rely on mature IP and accumulated
     trust
   - accounts with uncopyable face/resource/city/product/team advantages
   - accounts whose interaction looks inflated or low-intent
   - one-off emotional viral notes that are hard for an ordinary creator to
     repeat
5. 下一步:
   - analyze one selected account
   - compare with user's own account
   - turn selected benchmarks into 7-day topics/title/cover package
   - save to content knowledge base
   - if the recommended accounts share the same format, offer a format-specific
     follow-up search

## If Results Are Weak

Do not pretend weak results are good.

Say:

这批搜索里有账号能参考，但真正适合当主对标的不多。主要问题是：有些账号断更，有些只有旧爆款，有些和你的阶段不匹配。我建议下一轮改成按「近期爆款笔记反查作者」或放宽/收窄关键词继续找。

Then offer:

- change keyword
- narrow by format
- narrow by city/audience/life stage
- search recent high-performing notes and reverse-find authors
- let user send accounts they already like

## Emotional Virality And Long-Term Keywords

Do not copy one-off emotional events just because they are viral. A breakup,
marriage, family conflict, or dramatic personal event can receive support and
encouragement, but it may not be repeatable or appropriate for the user's
account.

However, do not reject all emotional content. In long-term demand tracks such
as female growth, career anxiety, self-worth, emotional stability, parenting,
or relationship boundaries, emotional value plus clear keyword coverage can be
a real repeatable content model. Judge whether the account repeatedly covers
the same demand with title, cover, state, keywords, and structure, not whether
one story happened to explode.

## Good User-Facing Wording

Use this when replying to ordinary users:

你不用每次都加“持续更新并有爆款作品”这句话。以后我帮你找对标账号时，会默认优先筛：最近还在更新、近 90/180 天有高互动作品、和你当前阶段更接近的账号。断更很久的账号我会标成“历史参考”，不会当主对标推荐。

如果你自己已经收藏了几个喜欢的账号，也可以直接发给我。这样会更精准，因为我可以直接判断：它值不值得你学、你能学哪一部分、哪些是它自己的脸/资源/城市/粉丝基础，不能照抄。

When showing results, use direct links:

- Show the creator's Xiaohongshu homepage link, not only the creator ID.
- Show follower count and total liked count when available, so the user can
  judge stage-fit without opening the profile.
- Show the high-interaction note links, not only note IDs.
- Show public likes/collections/comments for the specific recent-hit notes.
- If only an ID is available from the raw result, convert it into a readable
  Xiaohongshu profile URL when the platform is Xiaohongshu.
- Raw IDs can stay in JSON/internal data, but they should not be the visible
  user-facing deliverable.

When most recommended accounts are the same format, summarize that plainly:

这 5 个里面大部分是口播型账号，适合学选题、标题和表达节奏；如果你想做纯图文，我可以继续帮你找一批纯图文/知识卡账号。

Use the same logic for other formats:

- If most are 口播, offer pure graphic-note or no-face graphic references.
- If most are 图文, offer口播/Vlog references if the user wants to show up on
  camera.
- If most are local-life video探店, offer pure photo/card-style local-life
  accounts if the user cannot shoot video.

When the user asks for more after the first 5, narrow the next search before
expanding:

如果这 5 个里面方向对了，我可以继续帮你按粉丝量筛，比如 1000-5000 粉、5000-3 万粉、3-10 万粉；也可以按图文/口播/Vlog/本地城市继续找。这样会比一次性给你 10-20 个更省积分，也更容易找到真正能模仿的账号。

## Do Not

- Do not recommend long-stale accounts as main benchmarks.
- Do not return 10-20 benchmark accounts by default; first deliver up to 5
  strong accounts.
- Do not treat account search results as final recommendations before checking
  recent posts.
- Do not use "viral" if the account's only strong works are too old for the
  current task.
- Do not return creator IDs as the main visible result. Users need direct
  creator homepage links and specific high-interaction works.
- Do not omit follower count, total liked count, and recent-hit note metrics
  when the data is available.
- Do not mix口播、图文、Vlog accounts without telling the user what formats were
  found and whether a format-specific follow-up search is needed.
- Do not hide that additional account verification can add searches/credits.
- Do not spend credits on a broad follower-range search before the user has
  confirmed the desired range or stage.
- Do not over-filter until no references remain; if there are few active
  accounts, say so and offer another search strategy.

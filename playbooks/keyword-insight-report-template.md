# Lingzao Keyword Insight Report Template

Use this playbook when the user wants a report or structured insight around one
keyword, such as:

- 帮我分析“云南旅游”这个关键词
- 给我做一个关键词洞察报告
- 这个关键词下面用户都在看什么
- 这个关键词有哪些下拉词 / 相关词 / 选题机会
- 帮品牌 / 企业 / 机构 / 文旅 / 产品团队看关键词内容机会
- 搜某个关键词，看看大家都是怎么做的

This is different from beginner topic discovery. Beginner topic discovery helps
one creator decide what to post. Keyword insight reports help a user understand
the public content ecosystem around a keyword and turn it into content,
marketing, product, or campaign decisions.

## Core Principle

A keyword report is not one search result list. It is a scoped research
deliverable:

- one main keyword
- a controlled set of related/dropdown keywords
- visible public note samples
- content type classification
- user demand map
- representative examples
- opportunity list
- action advice for the user's business or account

Do not silently search every related word. Confirm scope before searching.

## Current Capability Boundary

Lingzao Skill currently exposes `search-notes` for keyword searches. If an
explicit dropdown/suggestion API is not available in the current runtime, treat
dropdown words as a keyword expansion list created from:

- the user's own words
- visible search phrases provided by the user
- domain judgment
- prior keyword trees in `beginner-account-start-and-topic-radar.md`
- search-result titles and repeated terms from confirmed searches

Each confirmed keyword that is actually searched is one `search-notes` lookup.
Do not imply that all dropdown words are free.

## First Response

If the user gives only one keyword and says they want insights, do not start
searching immediately. First explain the scope choices and credit logic.

Use this user-facing wording:

可以做。关键词洞察报告不是只搜一次关键词，而是看“主关键词 + 相关词/下拉词 + 代表性高互动内容”，再总结内容类型、用户需求和选题机会。

先提醒一下积分：普通关键词搜索是按实际搜索的关键词次数算，不是按你发一条指令算。比如只搜“云南旅游”一次，通常是 20 credits；如果再搜 5 个相关词，就是 6 次搜索，约 120 credits。搜索结果一次可以返回多条笔记，不是按返回的每条都扣。只有继续打开单篇详情、评论区、逐字稿或更深内容结构时，才会继续增加。

先选平台、范围和搜索过滤项：

- 平台：小红书 / 抖音。搜索关键词不能从词本身推断平台，所以开始前必须确认平台。
- 搜索过滤项：开始前也要确认排序、内容类型和时间范围；如果用户想省事，可以明确接受默认值 `sort=general`、`note_type=不限`、`time_filter=不限`。不要在用户未确认过滤项或默认值前开始批量搜索。

A. 快速洞察：主关键词 + 3 个相关词，先看内容类型和机会方向，预计约 80 credits。
B. 标准报告：主关键词 + 8-10 个相关词，再挑代表样本做分类，预计约 180-220 credits；如果继续打开 5-10 条单篇详情，会再增加约 100-200 credits。
C. 深度报告：15-30 个相关词 + 代表笔记详情 + 评论区需求，适合企业/品牌/机构做策略，通常会到 800 credits 以上，开始前我会先列搜索范围让你确认。

你回复“平台 + A/B/C + 过滤项”，比如“小红书 A，排序按点赞，视频笔记，一周内”，或“抖音 B，接受默认过滤项”，我再开始；如果你只回复 A/B/C，我会先追问平台和过滤项，不会默认把所有下拉词都搜完，也不会默认替你选平台、排序、内容类型或时间范围。

## Scope Tiers

### A. Quick Insight

Use when the user wants a first look or is sensitive to credits.

Search scope:

- main keyword
- 3 related keywords
- for Xiaohongshu, usually `sort=most_liked`; use `collect_descending` only
  when the user cares most about saved/collected content
- for Douyin, use `sort=most_liked` or `popularity_descending`; do not use
  `collect_descending` or `comment_descending`
- for Douyin, note type must be `不限`, `视频笔记`, or `图文笔记`; do not pass
  `直播笔记`
- for Xiaohongshu, choose note type and time range based on user goal; for
  Douyin, choose only the supported note types above and choose time range based
  on user goal; if unclear, ask before calling

Estimated credits:

- 4 `search-notes` lookups x 20 credits = about 80 credits
- no note detail by default

Output:

- 一句话判断
- 关键词基础判断
- 3-5 high-signal examples from search result lists
- content type map
- user demand map
- 5 topic opportunities
- whether it is worth expanding into a full report

### B. Standard Report

Use when the user wants a report similar to the "云南旅游" document.

Search scope:

- main keyword
- 8-10 related/dropdown keywords
- representative results from each keyword
- optional 5-10 note details if titles/cover/basic metrics are not enough

Estimated credits:

- 9-11 `search-notes` lookups = about 180-220 credits
- optional 5-10 `get-note-detail` lookups = about 100-200 extra credits
- typical range: about 180-420 credits, depending on whether details are opened

Output:

- Word / HTML / Markdown report when document tooling is available
- keyword conclusion
- high-interaction sample table
- content type insight
- user demand map
- representative examples with links
- opportunity list
- action advice for the user's account, brand, product, or team

### C. Deep Report

Use for enterprise, brand, institution, campaign, product, tourism, education,
or large-content planning.

Search scope:

- main keyword
- 15-30 related keywords
- selected note details
- selected comments pages when comment demand matters
- optional creator/account checks when the keyword is account-led

Estimated credits:

- 16-31 `search-notes` lookups = about 320-620 credits
- 10-30 note details = about 200-600 extra credits
- 5-10 comment pages = about 100-200 extra credits
- typical range: about 800-1400 credits when it includes details and comments

Output:

- full keyword landscape
- related keyword tree
- content type distribution
- user demand and conversion-intent map
- low-follower viral opportunities if relevant
- title/cover/formula library
- representative note cards
- competitor/content gap map
- 30-day content plan
- export-ready knowledge-base table if needed

## Related Keyword Logic

Build related keywords in layers. Do not dump a huge keyword list.

### Layer 1: Direct Dropdown / Phrase Variants

Examples:

- 云南旅游
- 云南旅游攻略
- 云南旅游避坑
- 云南旅游路线
- 云南旅游自由行
- 云南旅游预算

### Layer 2: Audience / Scenario

Examples:

- 云南亲子游
- 云南情侣游
- 云南毕业旅行
- 云南带娃
- 云南第一次去

### Layer 3: Geography / Sub-Destination

Examples:

- 大理旅游
- 丽江旅游
- 香格里拉旅游
- 泸沽湖攻略
- 腾冲旅行
- 西双版纳亲子游

### Layer 4: Commercial / Decision Intent

Examples:

- 云南包车
- 云南民宿
- 云南旅拍
- 云南报团避坑
- 云南自由行花费

Only search the layers that match the user's goal.

## Report Structure

Use this structure for formal keyword insight reports.

1. Cover
   - report title
   - keyword
   - target audience or client
   - date

2. One-Sentence Conclusion
   - what the keyword really represents
   - why it matters commercially or strategically

3. Keyword Basic Judgment
   - main keyword
   - searched related keywords
   - sample source and search filters
   - suitable clients/users
   - core value

4. High-Interaction Sample Table
   - title
   - content type
   - creator
   - likes
   - collections
   - date
   - source keyword
   - link

5. Content Type Insight
   - content type
   - sample count or qualitative weight
   - user signal
   - why it works
   - what the user/company should do

6. User Demand Map
   - user group
   - what they search
   - content bridge
   - commercial opportunity, if relevant

7. Representative Notes
   - screenshot/cover if available and renderable
   - title
   - creator
   - public metrics
   - why this example matters
   - source link

8. Topic Opportunity List
   - 10-20 practical topics for standard/deep reports
   - title direction
   - cover direction
   - content angle
   - suitable account/brand type

9. Action Advice
   - for creator accounts: next content tests
   - for brands/products: content funnel and conversion bridge
   - for institutions/government: public communication, user concern handling,
     and service information
   - for tourism/local life: route, budget, map, avoidance, seasonal and
     audience segmentation

10. Knowledge-Base Follow-Up
   - ask whether the report should be saved into a content asset library
   - use `content-knowledge-base-workflow.md`

## Analysis Rules

### Do Not Only List Hot Notes

A keyword report must answer:

- What are users actually trying to decide?
- Which content types create likes?
- Which content types create saves?
- Which content types create comments or conversion?
- Which topics are visually attractive but commercially weak?
- Which topics are less viral but more useful for business?

### Distinguish Likes And Saves

For many keywords:

- high likes may come from emotion, beauty, shock, or identity
- high saves often mean planning, decision, tutorial, checklist, route, budget,
  or resource value

For commercial keyword reports, saves and comments may matter more than likes.

### Separate Content Traffic From Business Value

Example:

- scenery posts may attract clicks
- route/budget/avoidance posts may drive saves and inquiries
- comments may expose purchase or service questions

Do not tell a company to only imitate viral visual posts if those posts do not
support conversion.

### Use Active Time Ranges

When the user cares about current trends, prefer recent results and active
signals. If the available top examples are old, say so and search recent
variants if the user confirms more scope.

## Output Tone

For individual creators:

- practical
- directly usable
- focused on what to post next

For enterprise/brand/institution:

- more report-like
- more explicit about audience, decision, conversion, and content funnel
- avoid creator-only language like "人设" unless relevant

For tourism/local life:

- separate visual planting from route/decision content
- include route, budget, geography, season, transportation, hotel area,
  avoidance, crowd type, and local service opportunities

## Follow-Up

After the report, do not let it end.

Good endings:

- 这份关键词报告可以继续沉淀成你的内容资产库。你现在有没有固定放知识库的地方？如果没有，我可以先生成 Markdown / CSV / Word / HTML 通用包，后面你想放飞书、阿里、腾讯、Notion 或本地都方便。
- 如果你想继续做下一层，我可以把这个关键词下面的高收藏标题、封面公式和评论区需求单独拆成一份选题库。
- 如果你是企业/机构，我可以继续把这份报告改成 30 天内容计划和 10 条可直接发布的选题。

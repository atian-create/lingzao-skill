# Lingzao Content Knowledge Base Workflow

Use this playbook when the user wants to turn saved notes, public creator links,
keyword results, viral examples, drafts, or reference accounts into a reusable
personal knowledge base or content asset library.

Also use it proactively after Lingzao has helped the user collect several
references, topics, accounts, note links, title examples, cover examples, or
rewritten drafts. The user may not say "knowledge base"; Lingzao should notice
that the user is accumulating useful material and offer a place to put it.

This is not a separate crawler product. It is a user-owned organization
workflow: Lingzao helps the agent read public content signals, summarize what
can be learned, and produce structured notes that the user can keep in Feishu,
Notion, Markdown, Word, Sheets, or a local folder.

## Trigger Phrases

Route here when the user says:

- 把收藏夹变成知识库
- 做自己的知识库
- 小红书爆款知识库
- 内容资产库
- 选题库 / 标题库 / 封面库 / 案例库
- 整理成飞书知识库 / 本地知识库 / Notion
- 把这些链接沉淀下来
- 我想学习这些账号 / 笔记
- 蒸馏一个博主 / 蒸馏这个账号
- 把这个博主整理成知识库
- 提取这个博主的选题、文案、封面、关键词
- 我收藏很多但不知道怎么用
- 帮我把对标内容变成可以复用的资料

Also route here after outputs such as:

- a keyword/topic search that returns many useful references
- a comparable-account breakdown with learnable examples
- a low-follower viral-note search
- a title/cover/formula pack
- a batch draft rewrite
- a user-provided list of saved notes or accounts

If the request is mainly about finding topics, also use
`beginner-account-start-and-topic-radar.md`.

If the request is about drafts after learning references, also use
`draft-rewrite-and-benchmark-workflow.md`.

## Product Boundary

Keep the wording inside this boundary:

- We can create user-owned structured notes, tables, outlines, and report files.
- We can summarize public links the user provides or searches they confirm.
- We can preserve source links, public metrics, titles, creator names, tags, and
  transformed learning notes.
- We can make a Feishu-ready / Notion-ready / Markdown-ready structure for the
  user to paste or import.
- We can generate download-ready files when the runtime supports file creation,
  such as Markdown, CSV, HTML, Word, or a zipped local folder.
- We can write directly into a destination only when that destination's
  connector, CLI, or authenticated tool is available in the current runtime.
- We can give the user a reusable update prompt for the next time they actively
  ask Lingzao to refresh the knowledge base.

Do not promise:

- server-side searchable databases of public platform content
- full archive crawling
- raw data export
- bulk image/video downloads
- automatic long-running monitoring
- Feishu plugin or automatic Feishu sync
- direct sync to Alibaba, Tencent, Feishu, Notion, or any other knowledge-base
  product when no connector/authenticated tool is available
- copying full articles, full scripts, or another creator's original content
  into a reusable library

When useful, say:

这里更适合做成“你自己的内容资产库”：保留链接、标题、封面观察、爆款机制、可学点、不可照抄点和你自己的改写方向。不要把别人的全文整段搬进来，重点是把它转成你能学习、能发、能复盘的结构。

## Proactive Save Prompt

Use this after the user has collected useful material, even if they did not ask
for a knowledge base.

Do not ask a vague question like "还需要什么". First ask whether the user
already has a place to store knowledge, then route to the next step:

这批内容已经不只是一次搜索结果了，建议沉淀成你的内容资产库。你现在有没有固定放知识库的地方？

A. 有，比如飞书 / Notion / 语雀 / 阿里 / 腾讯知识库：我可以先按它适合导入的结构整理。
B. 还没有：我建议先生成通用下载包，包含 Markdown / CSV / Word / HTML，后面你想放到哪里都方便。
C. 先不确定：我先在对话里给你轻量表格和下次补库指令，等结构对了再导出。

If the user has already said the destination, skip this prompt and use the
matching export mode.

## Intake Logic

### If User Sends Links

Classify the links first:

- creator homepage links -> 对标账号库 / 账号拆解库
- Xiaohongshu creator homepage links with "蒸馏" intent -> 博主蒸馏库
- Douyin creator homepage links with "蒸馏" intent -> explain that full profile
  distillation is not currently supported; ask for specific Douyin post links or
  a keyword, then build a post-level / keyword-level reference library instead
- note links -> 爆款笔记库 / 标题封面库 / 结构库
- mixed links -> 综合案例库
- draft links or own notes -> 发布复盘库

Then ask only the next useful scope question if unclear:

你这批链接更想整理成哪一种？

A. 选题库：以后不知道发什么时直接来翻。
B. 标题/封面库：专门学习点击理由和视觉表达。
C. 对标账号库：长期看哪些账号值得学、哪些不能照抄。
D. 发布复盘库：把你自己发过的内容、数据和改法沉淀下来。
E. 博主蒸馏库：把一个博主的选题、文案结构、关键词、封面风格和可模仿点整理出来。

If the user already states the library type, do not ask again.

After choosing the library type, ask whether the user already has a knowledge
base destination only if it matters:

整理完以后，这批内容要放到哪里？你现在有没有固定的知识库，比如飞书、Notion、语雀、阿里或腾讯知识库？如果还没有，我建议先生成通用下载包，之后你想导入哪里都方便。

### If User Has No Links

Do not start with a long form. Ask for the smallest useful input:

你可以先发 3-10 条你最近收藏、喜欢、想模仿的小红书链接；如果暂时没有链接，也可以发一个关键词，比如“女性成长图文”“35岁职场”“AI工具”“本地生活探店”。我先帮你做第一版内容资产表。

If a search is needed, use `search-credit-notice.md` before searching.

### If User Says They Have Many Saved Items

Do not ask them to paste hundreds of links. Start with a sample:

先不用一下子整理全部收藏。你先给我 10 条最想学、最常回看的链接，我会先做一个样板知识库。等结构对了，再按同一模板继续补。

## Search And Credit Scope

Before any Lingzao lookup, choose the scope:

Before a creator distillation, explain the sampling logic in plain language.
Users should know why a set of references was selected; otherwise they may
think Lingzao randomly picked posts or spent credits on an opaque search.

Do not say "I will simply crawl everything" or "I will only take the top 50
likes." Likes are useful, but old viral posts and accidental hot-topic posts can
mislead the user. A good distillation balances proven posts with current
behavior, save value, comment demand, and commercial/series signals.

If the current tool can fetch fewer items than the target sample, state the
actual available count clearly. For example: "标准蒸馏目标是 50 条代表内容；当前
主页深度解析一次最多可先看 40 条，我会先基于这 40 条做第一版。如果你确认
继续，我们可以用确认后的关键词搜索或对标账号搜索做单独的补充参考区，但不
把这些外部内容算进这个博主的代表样本。单篇详情和评论区只用于丰富已选样本，
也不算新增样本。"

### Creator Distillation Modes

Use these modes when the user wants to distill one Xiaohongshu creator/account.
Do not use these profile-based modes for Douyin creator homepages. For Douyin,
fall back to confirmed post links, keyword searches, note details, comments, or
video-copy extraction, and label the output as a post-level or keyword-level
reference library rather than a full creator profile distillation.

#### Quick Distillation

Use for first-pass learning or when credits should be controlled.

Target sample:

- about 20 representative posts when available
- prioritize recent high-signal posts and obvious top performers
- do not open details/comments/transcripts unless needed and confirmed

Output:

- one creator research card
- 5-8 recurring topics or keywords
- 3-5 title/cover observations
- 3 learnable parts
- 3 non-copyable parts
- 3 user-adaptation directions

Good wording:

我可以先做快速蒸馏，先看大约 20 条代表内容，判断这个博主值不值得继续学。结果会比较轻：定位、关键词、爆款原因、封面规律、能学和不能照抄。

#### Standard Distillation

Use when the user wants a knowledge-base asset that can be saved.

Target sample:

- about 50 representative entries when available
- explain that "50" means a balanced sample, not only the 50 highest likes
- if only 40 profile posts can be fetched in the current command, disclose the
  real count and keep the target creator sample at that real count unless more
  posts from the same creator are available
- if the user wants broader context, put confirmed keyword searches or
  comparable-account searches into a separate benchmark/reference section; do
  not count those external results as samples from the target creator
- use note details, comments, or transcripts only to enrich selected entries;
  do not count those lookups as additional creator samples

Recommended mix:

| Segment | Count | Purpose |
| --- | ---: | --- |
| High-interaction posts | 20 | Understand proven viral mechanisms. |
| Recent posts | 15 | See what the creator is doing now and avoid stale examples. |
| High-save posts | 5 | Extract knowledge value, tutorial value, and reusable structure. |
| High-comment posts | 5 | Read user demand, objections, and follow-up questions. |
| Commercial/series posts | 5 | Understand conversion, recurring columns, and long-term assets. |

If one segment is not available, fill the gap with the most representative
remaining posts and say why.

Good wording:

标准蒸馏默认整理 50 条代表内容，不是随机抓，也不是只看点赞最高。我会综合高赞、近期、高收藏、高评论和商业/系列内容，帮你看出这个博主真正值得沉淀的选题、文案结构、关键词、封面风格、爆款公式和你能模仿的地方。

#### Deep Distillation

Use only after scope confirmation. This can involve many searches or follow-up
lookups.

Target sample:

- 100+ entries only when the user explicitly wants a long-term benchmark or
  industry library
- may combine profile analysis, keyword searches, selected note details,
  comment demand, and multiple related creators

Output:

- creator evolution map
- topic and keyword tree
- title/cover/style library
- content-structure formulas
- comment-demand map
- commercial bridge observations
- user adaptation roadmap
- export-ready Markdown/CSV/Word/HTML package when file tools are available

Good wording:

深度蒸馏适合长期对标或做行业资料库，会比标准蒸馏多看关键词、评论区、系列栏目和商业承接。开始前我会先给你搜索范围，你确认后再继续，不会自动把范围扩到几十个账号或上百条内容。

## Creator Distillation Assets

When distilling a creator, extract the following assets. Do not only summarize
copy. The value is to turn public content into a user-owned learning system.

1. **Account Positioning**: who this creator is, who they serve, what problem
   they repeatedly solve, and what makes them memorable.
2. **Audience and Demand**: who follows, why they save, what they ask in
   comments, and what kind of emotional or practical need appears.
3. **Topic System**: high-frequency topics, recurring columns, series
   potential, stale topics, and new directions.
4. **Copy Structure**: hook, body sequence, story/proof/tutorial steps, save
   point, ending, and any repeatable formula.
5. **Core Sentences**: short learning notes, not full copied scripts. Extract
   useful claims, angles, and reusable sentence patterns.
6. **Keyword System**: title keywords, cover keywords, body keywords, audience
   words, pain words, scene words, emotional words, and search words.
7. **Cover Style**: color, font, layout, person/object/scene, first-screen
   message, keyword placement, series markers, and visual consistency.
8. **Viral Mechanism**: why posts perform: emotional identity, practical save
   value, trend, conflict, reverse story, tutorial utility, or comment demand.
9. **Commercial/Conversion Signals**: course, community, product, consulting,
   affiliate, store, lead generation, ad/product placement, or enterprise
   conversion clues when visible.
10. **Learnable vs Non-Copyable**: separate what the user can learn now from
    what depends on the creator's face, city, resources, stage, authority, or
    existing fan trust.
11. **User Adaptation**: how to change the same formula into the user's own
    track, stage, resources, and content format.

Recommended output blocks:

- 博主研究卡
- 样本选择说明
- 高频关键词树
- 选题库
- 文案结构库
- 封面风格库
- 爆款机制库
- 评论区需求库
- 可模仿点 / 不能照抄点
- 改成用户自己版本的方向
- 是否建议同步到知识库

## Mismatch And Refinement

If the collected results do not fit the user's target, do not force a weak
analysis. Explain the mismatch and let the user choose a new filter.

Good wording:

这批内容和你的目标不完全匹配。不是不能分析，而是如果直接沉淀进知识库，后面可能不好用。你更想按哪种方式重新筛？

A. 最近 30 天比较火的内容：看当前趋势。
B. 低粉爆款：适合小白或起步号模仿。
C. 高收藏内容：适合做知识库和教程库。
D. 高评论内容：适合挖用户需求和下一批选题。
E. 商业/引流内容：适合看变现和承接。
F. 封面和标题参考：适合做图文、标题、视觉模板。

If the user chooses a filter, continue with that filter and summarize the new
scope before spending more credits.

### Light Knowledge Base

Use for 3-10 user-provided links or one small keyword sample.

Output:

- source list
- simple tags
- why it is worth saving
- title/cover/content structure observation
- what the user can learn
- one adaptation idea

Credit stance:

- controlled basic lookups first
- do not open every detail/comment/transcript unless user confirms

### Deep Knowledge Base

Use when the user wants a fuller library, cross-keyword trend comparison, full
copy/script structure, comments demand, or a larger report.

Output:

- keyword clusters
- low-follower viral examples
- account/reference groups
- title and cover formula groups
- comment demand map
- rewrite directions
- export-ready table / document

Credit stance:

- confirm scope before expanding
- separate basic search objects from deep content objects
- do not silently scan dozens of accounts or notes

## Destination And Export Modes

The safest default is to create a universal export package. Direct sync is a
convenience layer, not the core promise.

### Feishu Mode

Use when the user wants Feishu.

If a Feishu document/wiki/sheets connector or authenticated CLI is available in
the current runtime, create:

- one Feishu doc as the readable knowledge-base report
- one Feishu sheet/table as the living asset library when table creation is
  available
- source links and public metrics in an appendix/table

If no Feishu tool is available, do not claim direct sync. Generate a
Feishu-ready package:

- `.docx` or Markdown report
- `.csv` table for the asset library
- optional `.html` preview
- clear section titles that can be pasted into Feishu

Good wording:

我可以先生成飞书可导入的版本。如果当前 Agent 环境有飞书授权工具，我就直接写入飞书；如果没有，我会给你 Word / Markdown / CSV，你可以导入或复制到飞书。

### Local Folder Mode

Use when the user wants a local knowledge base or does not know where to put it.

Recommended folder:

content-library/
- README.md
- sources.csv
- topics.md
- titles.md
- covers.md
- structures.md
- accounts.md
- publishing-review.md
- assets/

Recommended downloadable package:

- Markdown files for long-term reading
- CSV table for sorting/filtering
- HTML preview for easy viewing
- Word report if the user wants to share it
- ZIP folder if the runtime supports creating archives

Good wording:

如果你不知道放哪里，先放本地最稳。我可以给你一个本地知识库文件夹：Markdown 负责长期沉淀，CSV 负责筛选，HTML/Word 负责查看和分享。

### Other Knowledge-Base Products

Use for Alibaba, Tencent, Notion, Yuque, or other products.

Do not depend on a specific product import behavior unless the current runtime
has a confirmed connector or the user provides the product's import rules.

Default to universal formats:

- Markdown for knowledge-base pages
- CSV for structured tables
- Word for shareable reports
- HTML for preview
- ZIP for download and manual import

Good wording:

阿里、腾讯、Notion、语雀这类知识库，最稳的是先做通用包：Markdown + CSV + Word/HTML。哪一个平台能直接导入，就导入哪一种；以后如果你们要做深度集成，再单独接对应平台的 API 或授权工具。

### Chat-Only Mode

Use when the user does not want files yet.

Output a small table and a reusable next prompt:

- current library type
- 3-5 structured entries
- one update prompt

Good wording:

那我先不生成文件，先给你一个轻量版内容资产表。等你觉得结构对了，再导出成飞书、本地文件夹或通用下载包。

## Knowledge Base Entry Schema

Use this schema when turning public content into user-owned notes.

Required fields:

| Field | Meaning |
| --- | --- |
| Source Type | 账号 / 笔记 / 评论 / 关键词 / 自己发布内容 |
| Source Link | 原始链接，方便回看 |
| Title / Creator | 标题和作者名 |
| Sample Segment | 高互动 / 近期 / 高收藏 / 高评论 / 商业或系列 / 用户手动提供 |
| Track | 女性成长 / 职场 / 好物 / 本地生活 / 健康 / 穿搭 / AI / 其他 |
| Audience | 谁会被它吸引 |
| User Pain | 它击中了什么问题、情绪或需求 |
| Save Reason | 为什么值得收藏 |
| Title Formula | 标题用了什么点击理由 |
| Cover Formula | 封面用了什么视觉和信息锚点 |
| Content Structure | 内容怎样展开 |
| Comment Demand | 评论区暴露了什么需求；没有评论数据时留空 |
| Learnable Parts | 可以学什么 |
| Non-Copyable Parts | 不能照抄什么 |
| My Adaptation | 用户自己的改写方向 |
| Status | 学习中 / 可改写 / 已发布 / 待复盘 |
| Tags | 关键词标签 |
| Next Prompt | 下次继续用它能问什么 |

Do not include raw internal fields or internal response payloads.

## Asset Library Types

### Creator Distillation Library

Use when the user wants to learn one creator or turn a creator into a knowledge
base.

Capture:

- sample selection logic and actual sample count
- account positioning and memory point
- audience and demand
- topic system and recurring columns
- copy structures and reusable sentence patterns
- keyword system across title, cover, body, comments, and search
- cover style and visual consistency
- viral mechanisms
- commercial or conversion signals when visible
- learnable parts and non-copyable parts
- how the user can adapt the formulas into their own account

Always include a "sample explanation" before the analysis:

本次不是随机抓取。我会说明这个博主样本来自高互动、近期、高收藏、高评论、商业/系列内容中的哪几类；如果该博主可获取样本不足 50 条，我会如实标注实际样本数。关键词搜索结果或对标账号内容只能放在单独的补充参考区，不并入这个博主的代表样本。单篇详情和评论区只用来补充已选样本的结构、用户需求和证据，不把它们算作新增样本。

Do not turn the creator's full copy into a private clone library. Extract
structure, formulas, keywords, and learning notes instead.

### Topic Library

Use when the user often asks what to post.

Group by:

- audience
- pain point
- scene
- keyword
- title angle
- content format
- difficulty
- commercial possibility

Output should include 10-20 usable topics only after enough examples exist. For
a small first pass, give 3-7 topics and say it is the first sample.

### Title Library

Use when the user wants headline references.

Capture:

- trigger word
- audience word
- conflict
- result
- time number
- identity label
- emotional word
- search keyword

Always include why the title works, not just the title itself.

### Cover Library

Use when the user wants cover inspiration or graphic-note production.

Capture:

- main visual
- first-viewport text
- color / font / layout
- information density
- whether the cover tells the topic in one second
- whether it can be copied by the user at their current level

If cover images are available in results, show them in the final user-facing
output when the runtime supports images. If not, describe the cover clearly and
preserve the source link.

### Content Structure Library

Use when the user wants to learn why content performs.

Capture:

- opening hook
- body sequence
- proof / story / tutorial steps
- save point
- comment prompt
- commercial bridge, if any

### Comment Demand Library

Use when the user wants to mine comments.

Capture:

- repeated questions
- objections
- confessions
- buyer intent
- follow-up topics
- words the audience uses themselves

Do not imply full comment crawling. Only use available top-level comments and
confirmed pages.

### Account Reference Library

Use when the user wants benchmark accounts.

Capture:

- account memory point
- direct Xiaohongshu profile link, not only raw creator ID
- stage and follower level if visible
- recent update status
- whether the account is a main benchmark, local reference, historical
  reference, trend observation, or not recommended
- high-performing note patterns
- specific high-interaction works with title, note link, visible metrics, and
  why each one is worth saving
- whether the high-performing works are recent or old archive cases
- learnable parts
- dangerous imitation points
- matching user stage

For beginners, prefer same-stage or low-follower viral references over mature
large accounts, unless the task is to understand mature positioning.

If the user asks Lingzao to find benchmark accounts for a knowledge base, use
`benchmark-account-discovery-quality-gate.md` first. Do not save long-stale
accounts into the main benchmark list without marking them as historical
references.

In exported knowledge-base tables, raw IDs may be stored as hidden/internal
fields only when useful. The visible fields should be direct profile links,
note links, titles, metrics, labels, and learning notes.

### Publishing Review Library

Use when the user sends their own published notes or data.

Capture:

- title / cover / topic
- visible public metrics
- backend screenshot insights if user provides screenshots
- expected goal
- actual result
- what to keep
- what to change next

If the user does not provide backend data, do not invent exposure, click-through,
read completion, or follow conversion. Say they can send screenshots for a
deeper review.

## Output Formats

### Chat Output

For a first answer, keep chat concise:

- 一句话判断
- 这批内容适合沉淀成什么库
- 先整理出的 3-5 个资产
- 你现在可以怎么用
- one next prompt

Do not dump a huge table into chat unless the user asks for it.

### Markdown / Word / HTML Report

Use a report when the user asks for a formal deliverable.

Recommended structure:

1. 封面：知识库名称、方向、日期、一句话判断
2. 总览：这批内容主要在讲什么、适合沉淀成什么资产
3. 样本选择说明：实际分析了多少条，分别来自高互动、近期、高收藏、高评论、商业/系列内容中的哪几类
4. 标签地图：赛道、关键词、人群、问题、形式
5. 代表案例卡：链接、标题、作者、可学点、不可照抄点
6. 标题/封面/结构公式
7. 可直接改写的选题
8. 后续补库规则
9. 附录：来源链接、公开指标和样本分组

Word and HTML should match in structure when both are generated. HTML can be a
preview; Word is the shareable deliverable.

### Download Package

Use when the user wants to download or move the library across products.

Generate the most portable package the runtime can create:

- `README.md`: how this knowledge base is organized
- `sources.csv`: source links, creators, visible metrics, tags, status
- `topics.md`: topic library
- `titles.md`: title formulas
- `covers.md`: cover formulas and screenshot/cover notes
- `structures.md`: content structures
- `accounts.md`: benchmark account notes
- `publishing-review.md`: user's published-note review records
- `report.html`: visual preview when useful
- `report.docx`: shareable version when document tooling is available

Do not create a fake download link. If files are created locally, provide the
actual file path. If files cannot be created in the current runtime, provide the
copyable structure and say it can be exported when file tools are available.

### Spreadsheet / Table

Use when the user wants a living asset library.

Columns:

- 日期
- 来源类型
- 链接
- 标题
- 作者
- 赛道
- 人群
- 痛点
- 标题公式
- 封面公式
- 内容结构
- 可学点
- 不能照抄
- 我的改写
- 状态
- 下次复盘

## Follow-Up Hooks

End with one next step, based on the user's action:

If they sent links:

你可以继续发 5-10 条同方向链接，我会按同一个结构补进这份内容资产库，并帮你看哪些适合改写成你的下一批选题。

If they have no links:

你先从收藏夹里挑 3 条最想学的内容发来，我会先给你做一个小样板：选题、标题、封面、结构和你自己的改写方向。

If they want ongoing use:

我可以给你一条“下次更新知识库”的固定指令。以后你每次主动发新链接或关键词，就能按同一套表格继续补，不用重新想怎么问。

If they ask whether it can become Feishu/local knowledge base:

可以先做成飞书/Notion/本地 Markdown 都能用的结构化表格和文档。现在先不承诺自动同步插件，重点是把你的收藏变成能学习、能改写、能复盘的内容资产。

If they have just received a topic/reference/title/cover output:

这批内容已经可以沉淀了。你要不要把它变成一份内容资产库？可以选飞书、本地文件夹，或者先生成 Markdown / CSV / Word / HTML 通用下载包，之后再导入你常用的知识库。

## Quality Bar

A good knowledge-base answer should make the user feel:

- 原来我收藏的东西不是乱的，是能归类的。
- 我知道每条内容为什么值得学。
- 我知道哪些只是看起来火，不能直接照抄。
- 我知道下一条可以怎么改成自己的。
- 我下次还可以继续把链接发回来补库。

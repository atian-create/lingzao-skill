# Lingzao Publishing Keyword Design Check

Use this playbook after the user has a Xiaohongshu draft, title, cover copy,
caption, graphic-note outline, or finished content and asks for:

- 发布关键词
- 关键词怎么填
- 小红书关键词栏
- 帮我配 10 个关键词
- 关键词埋点
- 检查标题/封面/正文有没有带关键词
- 这篇内容发出去应该打什么词

This is different from `keyword-insight-report-template.md`.

- Keyword insight report = research the public content ecosystem around one
  keyword before deciding content strategy.
- Publishing keyword design = package one finished or nearly finished piece of
  content before posting.

If the user asks for a broader "发之前帮我看看" or "这篇能不能发" check, use
`pre-publish-readiness-check.md` first. This playbook is the keyword layer
inside that final gate.

## Core Principle

Do not turn every keyword request into a search.

Default to a light publishing check when the user already has content:

- inspect only the user's current title, cover copy, opening, body, and planned
  keywords
- output at most 10 final publishing keywords
- explain why each keyword fits this piece
- check whether the important keywords are naturally present in the content
- offer one next step

If the title itself is not decided yet, route through
`xhs-title-design-check.md` first or include only 3 strongest title options
inside the keyword check. Do not generate a 10-title pool before keyword
selection.

Only use Lingzao search when the user explicitly wants recent hot terms,
low-follower viral references, platform examples, keyword ecosystem research, or
industry trend validation. Before searching, use `search-credit-notice.md`.

## Audience Gate

Before selecting the final 10 keywords, identify the intended audience. Use
`audience-persona-fit-check.md` if unclear.

Keywords must match who the note is for:

- Female-oriented notes should carry relevant female identity, life stage,
  problem, or scene words when truthful.
- Student/young-beginner notes should not be stuffed with 35+, one-person
  company, childbirth, marriage, or midlife-crisis terms unless the content
  truly discusses those groups.
- Local-life notes should include city/area words and, when useful, visitor or
  local-resident intent. The title, cover, opening, keyword field, and platform
  location should point to the same city when possible.

## Required Inputs

Proceed directly if the user provides any useful combination of:

- title
- cover copy
- first 3 lines
- body draft
- note outline
- planned keywords
- target audience or track
- benchmark note/account

If the content is too thin to judge, ask for only the missing minimum:

你把标题、封面文案、正文前 3 行和准备放的关键词发我就行。我先不搜索，只帮你做这一篇的 10 个发布关键词和关键词埋点检查。

Do not ask a long form.

## Keyword Types

Classify candidate keywords into these five types.

| Type | Purpose | Examples |
| --- | --- | --- |
| 行业词 | Tell the platform and reader the content lane. | 小红书运营, AI工具, 女性成长, 本地生活 |
| 大众词 | Match what ordinary users understand and search. | 自信, 内耗, 副业, 穿搭, 减肥 |
| 人群/场景词 | Clarify who this is for or when they need it. | 30岁女生, 宝妈, 职场新人, 周末去哪 |
| 痛点/结果词 | Capture the user's problem or desired outcome. | 涨粉慢, 不会选题, 显瘦穿搭, 情绪稳定 |
| 长尾/爆款词 | More specific phrases that carry stronger intent. | 35岁重新开始, 低粉爆款, 小红书图文起号 |

Use "爆款词" carefully. If no search was run, say "可测试的爆款感长尾词"
instead of claiming they are proven hot terms.

## 10-Keyword Selection Rule

Xiaohongshu publishing keywords are limited, so final output must be selective.

Recommended mix:

- 2 industry words
- 2 audience/scenario words
- 2 pain/result words
- 2 大众 words
- 1-2 long-tail or viral-style words
- 0-1 series/format word if the content needs it

Do not use 10 generic big words.

Bad:

- 成长, 努力, 自律, 女性, 变好, 清醒, 独立, 生活, 人生, 幸福

Better:

- 女性成长, 30岁女生, 情绪稳定, 内耗, 普通人逆袭, 自我提升, 重新开始, 职场转型, 生活自洽, 35岁

But only use words that match the actual content.

## Natural Embedding Check

"自然" means the keyword matches the real content and appears in a reader-safe
way. It does not mean forcing every keyword into every sentence.

Check four locations:

1. Title
   - The main keyword or a close synonym should appear.
   - Example: if final keyword is "小红书起号", the title can say "新手做小红书",
     "从0做小红书", or "起号".
   - For local life, the city/area keyword should usually appear unless the
     cover carries it more clearly.
2. Cover copy
   - The cover should show the topic, audience, or result at a glance.
   - It can use fewer words than the title but cannot point to another topic.
3. First 3 lines
   - The opening should include audience + problem + promise when possible.
   - Example: "如果你刚开始做小红书，不知道该发什么..."
4. Keyword field
   - The 10 keywords should not all be broad labels.
   - They should connect to the title, cover, and opening.
   - They should match the intended audience and exclude mismatched life-stage
     or city words.

Use these labels:

- 已自然埋入：exact keyword or clear synonym appears in a key location.
- 需要补一句：the topic is present, but a keyword should be added to title,
  cover, or first 3 lines.
- 不建议使用：keyword is attractive but the content does not truly discuss it.

## Output Structure

Use this order.

1. 一句话判断
   - Say whether the current keyword direction is clear or scattered.

2. 内容所属赛道
   - State the likely track and audience.
   - If uncertain, say what clue is missing.

3. 最终 10 个发布关键词

| 关键词 | 类型 | 为什么适合这篇 |
| --- | --- | --- |
| ... | 行业词 | ... |

4. 关键词埋点检查

| 位置 | 判断 | 建议 |
| --- | --- | --- |
| 标题 | 已自然埋入 / 需要补一句 / 不建议使用 | ... |
| 封面文案 | ... | ... |
| 正文前 3 行 | ... | ... |
| 关键词栏 | ... | ... |

5. 建议替换词
   - List 3-8 words to avoid or replace when useful.
   - Explain briefly.

6. 可直接改的一版
   - Give revised title if needed.
   - Give revised cover copy if needed.
   - Give revised first 3 lines if needed.
   - Do not rewrite the full note unless the user asks.

7. 备用关键词
   - Give 10-20 backup words only if useful.
   - Group them by category, not as a random pile.

8. One follow-up

Use one of:

- 如果你愿意，我可以继续帮你检查标题、封面文案和正文前 3 行，把这 10 个关键词埋得更自然。
- 如果标题还没定，我可以先帮你从这篇内容里挑 3 个最值得点击的标题，再配最终 10 个发布关键词。
- 如果你想知道这些词最近有没有爆款参考，我可以再按“基础搜索/深度搜索”帮你查近期同类内容。
- 你发我最终版标题和封面，我再帮你做一次发布前最后检查。

## If User Has No Keywords Yet

Output:

- 10 final keywords
- why these 10 are enough
- where the top 3 should appear in title/cover/opening
- one sentence warning if the content is too broad

Good wording:

我先按你这篇内容本身来配，不做额外搜索。这里的关键词不是越热越好，而是要让平台和用户都知道：你在讲什么、讲给谁、解决什么问题。

## If User Already Has Keywords

Do not replace everything blindly.

Separate:

- 保留：matches the content and should stay
- 替换：too broad, too far from the content, or duplicates another keyword
- 补充：missing audience, pain, result, or long-tail phrase

Then give the final 10.

## If User Wants Recent Hot Keywords

This becomes keyword research, not only publishing packaging.

Before searching, say:

如果只是给这一篇配关键词，我可以不搜索，直接根据标题、封面和正文来做。
如果你想知道最近这个赛道哪些词更容易出爆款，就需要做关键词搜索：我会先选主词和相关词，按你确认的范围查，不会默认把所有下拉词都搜完。

Then use `search-credit-notice.md`.

After search, still return only 10 final publishing keywords for the user's
current piece, plus a separate "research-backed candidates" list.

## If Content And Keywords Do Not Match

Be direct but not harsh.

Say:

这 10 个词里有些词本身可能有流量，但它们不是这篇内容真正讲的东西。硬放进去会让标题、封面、正文和关键词栏各说各话，反而不利于系统和用户理解。

Then:

- identify the mismatch
- choose a narrower content promise
- rewrite title/cover/opening lightly
- produce a cleaner 10-keyword set

## Do Not

- Do not promise that keywords will make a note go viral.
- Do not stuff unrelated hot words into the final 10.
- Do not say "爆款词" if no search or evidence was used.
- Do not ask users to provide full backend data for this light check.
- Do not turn a publishing keyword request into a formal keyword insight report
  unless the user asks for market/industry/related-keyword research.
- Do not use fenced code blocks for normal keyword tables or rewritten title
  suggestions.

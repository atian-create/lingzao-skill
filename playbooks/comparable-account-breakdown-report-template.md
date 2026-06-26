# Lingzao Comparable Account Breakdown Report Template

Use this template when the user chooses B / says this is someone else's Xiaohongshu account / wants to learn from, imitate, or benchmark another creator.

The goal is not to praise the account. The goal is to tell the user:

- whether this account is worth learning from
- what exactly can be learned
- what cannot be copied
- whether the account matches the user's current stage, resources, face/camera ability, product, industry, or content direction
- which early-path signals matter more than the account's current mature form
- how to adapt the account into the user's own version

If the task is to find benchmark accounts rather than analyze a user-provided
account, use `benchmark-account-discovery-quality-gate.md` first. Do not
recommend account-search results as final benchmarks until recent public posts,
update status, recent high-performing works, and stage fit have been checked.

## Output Form

Default light deliverable:

1. Chat: short decision summary.

Default deep-report deliverable:

1. HTML preview: browser-friendly visual report for quick reading and internal review.
2. Word document: official shareable deliverable that the user can send to friends, clients, or team members.

When a full comparable-account report is generated, create both HTML and Word whenever tooling is available. They must come from the same report source. Word is the official shareable deliverable; HTML is the browser preview. If only one format can be created, explain why and prefer Word.

Do not generate a full Word/HTML report by default after one light lookup. First give the short decision summary. If the user wants a full report, explain that it becomes a deeper comparable-account breakdown and may require more Lingzao searches/credits because it needs to inspect more notes and possibly deeper content.

User-facing upgrade explanation:

如果你只想先判断这个账号值不值得学，我可以先按轻量拆解给你结论；如果你想生成正式报告，就会进入深度拆解。我会同时给你 HTML 预览和 Word 文档：HTML 方便你先看结构，Word 方便你转发给朋友、客户或团队。深度拆解会多看它的近期内容、代表爆款、封面标题、内容结构、可学和不可照抄部分，必要时还会继续看单篇正文、评论区或同阶段对标。

积分上也先说清楚：轻量看一个主页近期内容通常属于基础查看；正式报告如果要用主页深度解析，20 条作品是 50 credits，40 条作品是 100 credits。如果继续打开单篇详情或评论区，会按对应查看范围另外计算。我会先确认范围，不会直接替你扩大搜索。

The deep report should clearly tell the user what they will get:

- 一页总览：这个账号值不值得学、适合谁、最大可学点、最大风险
- 爆款内容地图：哪些内容明显高于平均表现
- 封面标题拆解：封面怎么吸引点击，标题用什么关键词
- 爆款机制：为什么能火，用户为什么点赞/收藏/评论
- 可学和不可照抄：哪些能学，哪些依赖资源/人设/粉丝基础
- 用户适配判断：小白、起步号、成熟号分别怎么学
- 改成你的版本：7 天选题、标题方向、封面文案、内容结构
- 附录：代表笔记链接、公开互动数据、必要的截图/封面说明
- 对比入口：如果用户也发自己的账号，继续生成“我和对标账号的差距 / 相似度 / 可学习点”对比

When showing accounts or notes, use direct Xiaohongshu links in user-facing
tables. Do not make the user copy raw creator IDs or note IDs. For a benchmark
account, include the profile link and the representative high-interaction note
links that support the judgment.

If the deeper report would require more scope than the user has confirmed, ask for confirmation before continuing. Do not silently expand from a short account breakdown into a full report.

Use the same visual standard as the own-account diagnosis report:

- Visual base: `tttt马上就发财` report.
- Judgment tone: `阿甜报告`.
- Clarity: `桃谷小仙` report.

## One-Page Decision Summary

The first page should answer quickly:

- 这个账号值不值得学
- 适合谁学
- 不适合谁学
- 最值得学的 3 个点
- 最容易误学的 3 个点
- 用户应该学它的早期路径，还是只观察成熟形态

Use this core decision pattern:

这个账号不是简单“照着发就能复制”，它真正可学的是 X；但如果你没有 Y 条件，就不要直接模仿 Z。

## Chat Feedback Structure

Before generating a full report, give a short decision-style chat answer. The chat answer should not be a long report.

Use this order:

1. 一句话判断：这个账号值不值得学，为什么
2. 账号类型：它是什么类型的账号，靠什么被记住
3. 最强爆点：它的爆款主要来自情绪、实用、身份、人设、视觉、趋势、产品，还是评论区需求
4. 可学的 3 个点：选题、标题、封面、内容结构、表达、人设、商业承接里最值得学的部分
5. 不能照抄的 3 个点：外貌/场景/阅历/资源/粉丝基础/产品/行业条件/成熟账号红利
6. 用户适不适合学：按用户阶段判断。如果用户没有说自己的阶段，先用默认分层判断小白、起步号、成熟号分别怎么学
7. 应该学哪个版本：学它早期路径、成熟形态、爆款公式、栏目结构，还是只观察趋势
8. 改成你的版本：给 3 个可以马上测试的方向，每个方向包含标题方向 + 封面文案 + 内容结构
9. 一个下一步问题：引导继续拆单篇笔记、找低粉对标、或生成 7 天选题

The first chat answer should feel like:

这个账号可以学，但不能直接照抄。它真正可学的是“记忆点 + 爆款结构 + 封面标题表达”，不是它现在的成熟粉丝量和人设光环。

## Feedback Modules

### 1. 值不值得学

Do not only say “值得学”.

Choose one:

- 很值得学：它有清楚记忆点、可复用爆款结构、稳定内容主线
- 可以局部学：某些标题/封面/栏目值得学，但整体人设或资源不可复制
- 只适合历史参考：账号长期断更或爆款太旧，适合看定位/结构，不适合作为当前主对标
- 不建议直接学：账号依赖强资源、强外貌、强场景、强粉丝基础或强产品条件
- 只适合观察趋势：适合看选题趋势，不适合作为直接对标

### 2. 它靠什么被记住

Analyze the memory anchor:

- 人是谁：身份、经历、外貌、职业、年龄、城市、关系状态
- 讲什么：固定问题、固定人群、固定场景、固定利益点
- 怎么讲：口播、图文、清单、故事、教程、情绪金句、采访、测评
- 看完记住什么：一句话锚点

If the account has no clear anchor, say it directly.

### 3. 爆款来源

Classify the main hit mechanism:

- 情绪爆款：让用户觉得“这说的是我”
- 实用爆款：解决一个具体问题
- 身份爆款：某个身份/年龄/职业/人生阶段被看见
- 趋势爆款：踩中平台或行业热点
- 视觉爆款：封面、场景、人物、前后对比非常强
- 评论区爆款：评论区不断暴露新需求，可以二次生产
- 产品爆款：内容背后有清楚产品或商业承接

### 4. 可学部分

Always separate learnable parts:

- 选题：它一直在解决什么问题
- 标题：标题用了什么关键词和点击理由
- 封面：画面主体、文字信息、颜色、系列感
- 结构：开头、证明、转折、结尾、收藏点
- 表达：语气、身份、情绪浓度、故事感
- 账号主线：哪些栏目可以系列化
- 商业承接：内容如何自然引向产品/服务/社群/咨询

For monetization analysis, use `monetization-path-judgment-library.md`. Do not only say the account can "接广告"; judge whether it is more likely using brand ads, product sales, small courses, paid materials, community, consulting, precise lead generation, store conversion, or enterprise product conversion.

### 5. 不能照抄部分

Be strict here. Many users误学就是因为只看到表面。

Common non-copyable parts:

- 长相、气质、镜头表现
- 城市、旅行、职场、家庭、关系等场景资源
- 过去经历和故事沉淀
- 粉丝基础和成熟账号信任感
- 产品、供应链、企业资源
- 高成本拍摄/剪辑/团队能力
- 大博主的成熟表达，小白直接模仿会像低配版

### 6. 用户阶段适配

If the user's stage is unknown, give stage-specific advice:

- 小白：只学标题/封面/选题，不学成熟人设；优先找低粉爆款和早期内容
- 5000 粉以下：学一个栏目结构，连续测 7-14 天，不要一次学全套
- 1-3 万粉：学系列化、评论区复用、爆款复盘
- 3 万粉以上：学破圈、形式升级、产品化承接
- 企业/机构：只学用户问题和内容结构，不套个人 IP 人设

Freshness is part of stage fit. If an account has stopped updating for a long
time, mark it clearly as historical reference or trend archive. Do not present
it as a current main benchmark unless the user explicitly wants to study old
positioning or archive cases.

### 7. 改成你的版本

Always convert analysis into usable tests:

For each adaptation direction, include:

- 方向名
- 适合的人群/账号阶段
- 标题方向
- 封面文案
- 内容结构
- 为什么这样改

Example format:

| 方向 | 标题方向 | 封面文案 | 内容结构 | 为什么适合你 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### 8. 下一步承接

End with only one follow-up question.

Preferred endings:

- 你要不要我继续找 3 个同领域但粉丝更低、最近一个月还在更新的账号，判断哪个更适合你学？
- 你要不要发它最火的一条笔记，我继续拆标题、封面、结构和评论区需求？
- 你要不要我把这个账号改成你的版本，直接给你 7 天选题 + 标题 + 封面文案？
- 你想不想我继续拆这个账号的变现方式？我可以帮你判断它是靠广告、课程、社群、咨询、精准引流，还是产品销售。
- 你要不要我继续做成一份 HTML + Word 对标账号拆解报告？这会进入深度拆解，我会多看它的爆款、封面标题、正文结构和可复制/不可复制部分，最后给你一份可以预览、也可以转发的可视化报告。
- 你现在有没有自己的账号？如果这是你参考的账号，也可以把你的主页链接发来，我可以继续做“你的账号 vs 这个对标账号”的差距、相似度和可学习点对比。

## Complete Report Structure

For a client-facing comparable-account breakdown, include these sections by default:

1. 封面：对标账号名 + 一句话判断 + 报告日期
2. 一页总览：值不值得学、适合谁、最大可学点、最大风险
3. 账号记忆点：别人为什么会记住它
4. 用户画像：谁会关注它、为什么收藏、为什么评论、可能为什么付费
5. 爆款内容地图：最近/代表性高表现内容、标题、封面、互动信号、内容类型
6. 爆款机制深拆：2-3 条代表内容，拆标题点击点、封面点击点、收藏理由、评论需求、可复用公式
7. 封面与视觉系统：画面主体、文字信息、颜色/字体/构图、系列感、可学与不可抄
8. 内容主线：账号核心栏目、可延展栏目、已经成熟但不适合小白直接模仿的栏目
9. 可学部分：选题、标题、封面、结构、表达、人设、产品承接
10. 不可照抄部分：资源、外貌/场景、阅历、粉丝基础、商业条件、平台阶段
11. 用户适配判断：按用户阶段给出是否适合学，以及该学什么版本
12. 改成你的版本：3-5 个可测试方向，每个方向给标题、封面文案、内容结构
13. 下一步行动：是否继续找同阶段低粉对标、是否拆单篇笔记、是否生成选题/标题包
14. 自己账号对比入口：询问用户是否有自己的账号链接，继续做差距、相似度和内容匹配度分析

For each recommended benchmark in the report appendix, include:

- creator name
- direct Xiaohongshu homepage link
- freshness / latest update signal
- 1-3 representative high-interaction works with title, note link, public
  likes/collections/comments, and why this work is worth learning
- label: main benchmark, local reference, historical reference, trend
  observation, or not recommended

## Stage Fit Rules

Always judge stage fit:

- 小白 / 5000 粉以下：不要直接学 10 万粉以上账号的成熟形态。优先看它早期内容、同领域低粉爆款、同阶段账号。
- 5000-3 万粉：可以学内容结构和栏目，但要改成自己的资源条件。
- 3 万粉以上：可以学习破圈、系列化、产品化、商业承接和内容形式升级。
- 企业/机构号：不要套个人 IP 逻辑，重点看产品表达、客户问题、场景证明、投放承接。

## Cover And Screenshot Rules

If cover images are available and can render reliably:

- show the main representative covers
- place cover analysis in a separate section
- do not only mention cover features inside paragraphs

If images cannot render reliably:

- do not leave blank image boxes
- use note title, note link, public metrics, and concise visual notes instead

## Adaptation Rules

Do not only say “可以模仿”.

Translate the account into the user's possible version:

- original account's structure
- why it works
- what condition it requires
- user's safer adaptation
- one test title
- one cover text
- one content structure

## Final Continuation

End with one next step:

- 是否要继续找 3 个同阶段、低粉但近期爆过的账号，帮你判断哪个更适合学？
- 是否要单独拆它最强的一条笔记，把标题、封面、结构和爆款公式拆出来？
- 是否要把这个账号改成你的版本，直接生成 7 天选题 + 标题 + 封面文案？
- 你现在有没有自己的账号？如果这是你参考的账号，可以把你的主页链接也发来，我可以继续做“你的账号和它差在哪里、相似在哪里、你最该学哪一部分”的对比报告。

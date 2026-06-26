# Lingzao Visual Generation And Cover Workflow

Use this playbook when the user asks Lingzao to make images, covers, graphic
notes, visual cards, WeChat article images, product/ecommerce visuals, or when a
keyword-to-content workflow reaches the image-generation step.

When image generation is available, use
`image-generation-execution-workflow.md` after this route-selection playbook.
This file decides what should be generated; the execution workflow turns the
brief into images, checks whether the output is ugly/crowded/generic, and
creates repair instructions when needed.

Trigger phrases include:

- 帮我做封面
- 帮我做图
- 生成小红书图片
- 做成小红书图文
- 做 4 页 / 7 页图文
- 我没有参考图，直接帮我出封面
- 按这个参考图做
- 公众号封面 / 公众号配图 / 正文配图
- 产品介绍图 / 课程图 / 电商图 / 付费资料图

## Core Rule

The user should not be stuck at "image prompt" when the runtime can generate
images.

- Do not make ordinary users write image prompts. Prompts are an internal
  fallback or implementation detail. The user-facing deliverable is a cover,
  graphic-note pages, page copy, and Xiaohongshu caption.
- If the user provides reference images, use them as the visual anchor and
  generate or prepare images in the same structural style, without direct
  copying.
- If the user provides only a keyword, broad topic, or one note direction, turn
  it into publishable graphic-note content first, then generate or prepare the
  images.
- If the user has no reference image, select a default style from
  `visual-reference-style-library.md` based on topic, material, and publishing
  channel.
- If image generation is available in the current Agent environment, create the
  image after the style and page text are ready, then run the visual quality
  gate from `image-generation-execution-workflow.md` before returning the
  result.
- If image generation is not available, return page copy, layout notes, and a
  complete fallback prompt package. Do not make it sound like the user must
  write the prompt.

## Current Graphic-Note Generation Loop

Use this path when the user wants Lingzao to make a Xiaohongshu graphic note
from a keyword or content direction, such as "女性成长", "帮我做一篇图文", or
"根据这些内容出一套图片".

1. Confirm the publishing format if unclear: graphic note/image, spoken video,
   or Vlog storyboard.
2. If graphic note/image is confirmed, use `keyword-to-publishable-content-package.md`
   to search or inspect public references within the confirmed credit scope.
3. Distill the references into reusable angles: keywords, core point, cover
   promise, page structure, and comment demand.
4. Rewrite the angle into the user's own publishable graphic-note content. Do
   not copy another creator's full text or exact layout.
5. Produce the image content:
   - final title
   - cover copy
   - 4-page or 5-page graphic-note text by default
   - page-by-page visual direction
   - generated images when the runtime has image generation
6. Produce a Xiaohongshu caption of about 300 Chinese characters plus 10
   publishing keywords and one comment prompt.

For this path, the user does not need to provide a reference image. A reference
image is useful only when the user wants a specific visual style. Otherwise,
select a no-reference style from `visual-reference-style-library.md` and move
forward.

## Intake

Collect only what changes the visual route. Do not make the user answer a long
design questionnaire.

### Minimal Intake Gate For One-Sentence Poster Requests

If the user only says "给我做一张某某海报图", "帮我做个封面", "做一张好看的图",
or provides only a broad topic with no reference, color, platform, exact
on-image text, or material, do not generate immediately. One vague sentence is
not enough to make a useful image; direct generation usually creates a generic
or ugly poster.

Ask these two questions first, in this order:

1. 你有没有参考图？可以发 1-3 张你喜欢的小红书封面、海报或图文截图。
2. 你有没有想要的配色？比如明亮白底、绿色清爽、黑金高级、蓝色科技感。

If the answer is still underspecified, ask at most one more route-changing
question: use/platform/size, exact on-image text, or people/no-people. Keep the
question short and practical; do not turn it into a design questionnaire.

Proceed without asking only when the user already gave enough anchors, such as:

- reference image + topic
- topic + platform/format + color direction
- topic + exact on-image text + product/photo/material
- article/draft + requested WeChat/Xiaohongshu image package

Important inputs:

- platform: Xiaohongshu / WeChat / other
- format: cover only / 4-page note / 7-page note / WeChat 1+3 image pack /
  product page set
- topic or keyword
- reference image, if available
- user material: face photo, product photo, screenshot, food/place/travel photo,
  article draft, product offer, city, prior content style
- whether the user wants people/no people

If the user has no reference image, say:

没关系，如果你没有参考图，我可以按你的主题给你选一个默认视觉风格。但你先告诉我有没有想要的配色，或者你想让它更像“小红书封面 / 公众号海报 / 产品介绍图”哪一种，这样成功率会高很多。

If the user has a reference image, say:

我会参考这张图的排版、信息层级、颜色和点击理由，但不会照抄它的文字、logo、作者专属素材和完全相同构图。

## Route Selection

Use `visual-reference-style-library.md` for style choice.

### A. Reference-Image Route

Use when the user uploads or points to reference images.

Output:

1. reference-image visual diagnosis
2. what can be learned: title position, image subject, color, font, information
   density, icon/card system, page rhythm
3. what cannot be copied: logo, exact layout, original photo, creator face,
   brand assets, exact title
4. adapted cover/page structure for the user's topic
5. generated images when available, or fallback image-generation instructions

### B. No-Reference Xiaohongshu Cover Route

Use when the user gives only a keyword/topic and asks for a cover or graphic
note.

Default routes:

- travel / food / local life -> Travel Food Local-Life Cover
- AI tool / tutorial / workflow + face/screenshot -> AI Person Tool Infographic
- no-face tutorial / Lingzao / Agent / knowledge explanation -> Lingzao
  No-Person Knowledge Card
- product / course / offer / ecommerce -> Product Ecommerce Conversion Card

If the user gives no face, screenshot, or product image, prefer a no-person
knowledge card or AI-assisted graphic note instead of inventing a fake
personal-photo cover.

If the topic is broad, such as 女性成长, first search or inspect a small set of
recent/high-signal references after credit confirmation, then turn the extracted
angle into a graphic-note package. Do not ask the user to provide an image
prompt.

### C. WeChat Article Image Route

Use when the user asks for WeChat public account images.

Default:

- 1 cover + 3 horizontal in-article images
- use Lingzao branded mode for Lingzao / Skill / account diagnosis official
  content
- use A Tian knowledge mode only for A Tian personal article content or when the
  user explicitly wants that IP mode

### D. Product Conversion Route

Use when the user has an offer/product/course/paid material and wants product
images.

Do not invent prices, promises, scarcity, or guaranteed results. If those fields
are missing, make a neutral product-introduction page and leave commercial
claims out.

## Xiaohongshu Graphic Note Structures

### 4-Page Fast Test

Use for ordinary users, no-reference image generation, and quick publishing.

1. Cover: one strong audience/pain/result sentence
2. Why this matters: the user's real stuck point or scenario
3. Method/result: 2-4 steps, examples, or reference angles
4. Today post this: 3 actions, comment prompt, or next topic

### 7-Page Teaching Version

Use when the topic needs more explanation.

1. Cover
2. Problem diagnosis
3. Input / preparation
4. Method steps
5. Examples / comparison
6. Action checklist
7. Comment prompt / next step

## Internal Prompt / Generation Rules

Every generated page, image-generation instruction, or fallback prompt must
include:

- platform and aspect ratio
- selected style group
- main visual subject
- exact on-image text
- text hierarchy: title, subtitle, labels, bottom bar
- layout: top label, main image, card modules, icons, page number
- color and font direction
- what must not appear

For Xiaohongshu, use vertical 3:4 or 4:5 unless the user asks otherwise.

For WeChat, use wide 900:383 or 1080:460.

For product conversion cards, use vertical 3:4 or 4:5, with one product promise
and one CTA-style area only when the user provides an offer.

## Quality Gate

Before returning generated images, page copy, or fallback prompts, check the
basic route quality here, then use `image-generation-execution-workflow.md` for
generated-image repair when actual images exist.

- Can a user understand the topic in one second?
- Is the biggest text readable and short?
- Does the image have a save/click reason, not only decoration?
- Is the visual style suitable for the user's current resources?
- Is the route honest about what can be generated from the user's materials?
- Are local reference paths kept internal?
- Are logos, brand marks, and IP characters used only when appropriate?

## User-Facing Continuations

Use one concrete next step:

- 你把这张参考图发我，我按它的结构给你做 4 页版。
- 你没有参考图也可以，我先按你的关键词搜一小批参考内容，提炼后直接给你生成一版无人物知识卡图文和 300 字发布文案。
- 你把产品/课程/咨询内容发我，我给你做一套产品介绍图。
- 你发出去以后，24 小时把笔记链接、后台截图、标题封面和脚本/正文发回来，我帮你复盘标题封面有没有带来点击，以及内容有没有读完/完播和收藏理由。

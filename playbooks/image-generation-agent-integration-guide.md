# Lingzao Image Generation Agent Integration Guide

Use this guide when Lingzao needs to expose image generation to domestic Agent
runtimes, CLI wrappers, or other non-OpenAI-native environments.

This guide is model-agnostic on purpose. Do not expose the provider/model name
to ordinary users unless the product explicitly decides to make it public. The
user-facing promise is:

- Lingzao can make Xiaohongshu covers and graphic notes.
- Lingzao can make WeChat article image packs.
- Lingzao can make product/course/service cards.
- Lingzao can use reference images without copying them.
- Lingzao can diagnose ugly generations and repair them.

## What Should Be Added To PR / Implementation

Implementers should wire image generation as a stable Lingzao capability, not as
a raw prompt field.

Minimum Agent-facing capability:

- command/tool name: `generate-image` or equivalent
- input: structured generation brief
- output: image URLs/files plus metadata and repair notes
- errors: friendly user-facing guidance, not provider stack traces

Minimum supported user flows:

1. topic -> cover
2. topic -> 4-page Xiaohongshu graphic note
3. topic -> 7-page teaching graphic note
4. reference image + topic -> adapted cover/graphic note
5. article draft -> WeChat 1 cover + 3 in-article images
6. product/course/service info -> conversion card set
7. ugly image -> diagnosis + repair generation
8. account links/recent notes + interaction goal -> interaction prompt cover
   plus account-relevant comment topics
9. long draft/research/transcript -> text-dense screenshot graphic note with
   keyword extraction and page rhythm
10. room/desk/home-scene material + life-stage topic -> room-as-identity
    lifestyle cover and series direction

## Stable Agent Call Contract

Domestic Agents should not have to understand model parameters. They should
pass a compact, structured brief.

### Pre-Generation Clarification Gate

Domestic Agent wrappers must not treat a one-sentence poster request as a ready
generation brief. If the user only says "给我做一张某某海报图", "帮我做个封面",
or "做一张好看的图", the wrapper should pause before creating a paid
generation job and ask for visual anchors.

Ask these first:

1. 你有没有参考图？可以发 1-3 张你喜欢的封面/海报/图文截图。
2. 你有没有想要的配色？比如明亮白底、绿色清爽、黑金高级、蓝色科技感。

If those are missing, ask at most one additional route-changing question:
platform/size, exact on-image text, people/no-people, or material/product photo.
Do not expose this as a long design form. The goal is to prevent low-information
prompts from producing generic or ugly paid images.

Minimum viable brief before generation:

- topic or theme
- platform/format or aspect ratio
- visual direction: reference image, color palette, style group, or real
  material
- exact on-image text or a clear statement that Lingzao should choose the text

If the minimum brief is not met, return `next_action: send_reference_or_color`
or a similar friendly state instead of starting generation.

Recommended input fields:

- `platform`: `xhs`, `wechat`, `product`, `other`
- `format`: `cover`, `graphic_4`, `graphic_7`, `wechat_1_3`, `product_set`
- `style_group`: one of the style groups in
  `visual-reference-style-library.md`
- `topic`
- `audience`
- `image_purpose`: `click`, `save`, `teach`, `explain`, `convert`, `article`,
  `comment`
- `aspect_ratio`
- `output_count`
- `main_visual_subject`
- `on_image_text`: short title, subtitle, labels, page text
- `materials`: optional reference image, face photo, product photo, food/place
  photo, screenshot, logo, article draft
- `reference_mode`: `structure`, `style`, `layout`, `color`, `none`
- `negative_constraints`
- `quality_gate`: whether to review and repair after generation

Recommended output fields:

- `images`: URL/file/path list
- `format`
- `style_group`
- `brief_used`
- `quality_review`: pass/fail and reasons
- `repair_brief`: present when the first generation is weak
- `caption`: for Xiaohongshu packages when relevant
- `keywords`: 10 publishing keywords when relevant
- `next_action`: post, regenerate, send reference image, or send 24h data

If the provider returns only a raw image URL, Lingzao should wrap it with the
metadata above before showing the result to the Agent/user.

## Good Image Standards

A good Lingzao image is not simply beautiful. It must be useful for the
publishing task.

### Good Xiaohongshu Cover

- The topic is understandable in one second.
- The largest title is short, readable, and carries a keyword or click reason.
- There is one clear visual subject or one strong knowledge-card structure.
- The cover matches the track: local life, food, AI tool, female growth,
  product, course, or WeChat article.
- The image has a save/click reason, not only decoration.
- Text hierarchy is clear: title, subtitle, labels. No dense paragraphs.
- The style looks like content a Xiaohongshu user would click, not a generic AI
  poster.

### Good Face-Led Video Cover

- The person's face, expression, gesture, or identity matches the keyword.
- The keyword is obvious and creates a click impulse, such as self-media
  money, fast AI learning, time, immediate gain, expert prediction, or child
  perspective.
- If the person is not visually distinctive, the cover adds information density
  through top-bottom split screen, four-grid, diagonal cut, or proof scene.
- The proof scene supports the claim: editing timeline, software UI, output
  preview, street scene, classroom, product, or other concrete context.
- The user's homepage can support more face-led content, not only one random
  face cover among unrelated graphic notes.
- The cover gives viewers a reason to believe there will be similar content
  after they follow.

### Good Interaction Prompt Cover

- The cover asks one question or throws one prompt that a specific audience
  wants to answer.
- The emoji/sticker/yellow-face expression matches the title emotion; it is not
  a random decoration.
- The highlighted words are the comment triggers, not random emphasis. Examples
  include "夯爆了", "姐妹迷上", "有意思", "非常帅", a city name, a track word,
  or a community identity.
- The topic connects to the user's recent notes, city, track, audience, or next
  content plan.
- The image is simple enough to understand in one second, but the comment
  question is sharp enough that users want to open the comment section.
- The result includes not only the cover, but also 5-10 related interaction
  topics the user can rotate without breaking the account direction.

### Good Text-Dense Screenshot Graphic Note

- It looks like a useful article/platform screenshot, but it has been edited
  for Xiaohongshu scanning.
- Page 1 can be understood in 1-2 seconds: topic, audience, keyword, and benefit
  are visible immediately.
- Users can scan the page by keywords instead of reading every line. The biggest
  keywords are bolded, highlighted, underlined, colored, or placed at strong
  line starts.
- The first two pages carry the click/save/follow reason: page 1 makes the
  promise; page 2 proves there is substance.
- The dense text comes from real distilled content: outline, workflow, conflict,
  list, numbers, observation, or examples. It is not filler paragraphs.
- The style is repeatable for account starting: same background family, font
  hierarchy, highlight color, title zone, and body rhythm.

### Good Room-As-Identity Lifestyle Cover

- The room is used as proof of the creator's choices, not as random background.
- The title names a life-stage reversal, lifestyle promise, or new narrative:
  "才32岁", "独居幸福感", "自己的房间", "人生才刚开始", or similar.
- The visible objects support the story: books, desk, tablet, e-reader, screens,
  chair, bed, lamp, notes, clothes, or other daily-use items.
- The cover can become part of a series because the homepage has a repeatable
  room angle and memory anchor.
- Commercial objects can appear naturally only when they belong to the life
  scene, such as chairs, tablets, e-readers, lamps, screens, desk tools, books,
  organizers, or bedding.
- The generation or visual direction separates what ordinary users can learn
  from what is hard to copy: real space, reading habit, device resources,
  previous operation ability, humor, relationship story, saved money, or other
  hidden resources.

### Good Graphic Note

- Each page has only one job.
- The page order is clear: cover -> problem -> method -> action.
- The user can save it and come back later.
- It has enough structure: steps, checklist, comparison, examples, or workflow.
- Inner pages are not just resized covers.

### Good WeChat Image Pack

- 1 cover + 3 horizontal images by default.
- The cover carries the article promise.
- The three inner images are simpler than the cover and support the article:
  problem, method, action/result.
- Official Lingzao visuals use brand style only for official Lingzao content.

### Good Product/Conversion Card

- It says who it is for.
- It explains what problem it solves.
- It shows what is inside.
- It does not invent price, scarcity, guarantee, testimonial, or income result.

## What Is Not A Good Image

Reject or repair these:

- It is pretty but users do not know why to click.
- It has too many words on the cover.
- It looks like a stock poster or generic AI poster.
- It uses one muddy color palette without hierarchy.
- It has fake UI, fake screenshots, fake data, fake metrics, or fake comments.
- It uses Lingzao/A Tian logo on ordinary user content.
- It copies a reference image too directly.
- It ignores the user's material and invents a fake person/product/place.
- It uses a face-led cover when the person has no expression, no identity
  signal, no authority, no proof scene, and no plan to keep showing up.
- It changes a graphic-note account into face-led content only because one
  viral reference had a person on the cover.
- It uses an interaction-post cover with a random emoji that does not match the
  question.
- It creates a viral-looking interaction prompt that is unrelated to the
  account's existing or planned content.
- It copies a stale interaction topic without checking whether people are still
  discussing it.
- It gets comments but gives the user no follow-up content path.
- It turns text-dense screenshot style into an unreadable wall of words.
- It uses raw screenshots without extracting keywords or rebuilding the first
  page for 1-2 second scanning.
- It hides the actual topic in paragraph three instead of making the keyword
  visible on page one.
- It invents fake platform metrics, timestamps, comments, account names, or
  engagement numbers to imitate a screenshot.
- It treats a room-as-identity cover as ordinary interior decor and loses the
  life-stage narrative.
- It creates a beautiful room that the user cannot actually keep showing, so
  the account has no repeatable memory anchor.
- It ignores hidden non-copyable resources behind a room account, such as
  devices, books, money, free time, operation experience, or personal story.
- It turns an educational note into a hard sales ad.
- It makes local-life/food/travel content without real place/food/route
  material unless the user is explicitly making an AI-assisted knowledge card.
- Chinese text is unreadable, distorted, or too small.

## How To Use Reference Images

Reference images should be treated as visual evidence, not a template to copy.

Before generation, extract:

- title placement
- main subject position
- color relationship
- information density
- page rhythm
- label/sticker/card system
- why the image is clickable
- what is creator-specific and cannot be copied

Borrow:

- composition logic
- hierarchy
- card structure
- contrast pattern
- page rhythm

Do not borrow:

- original title
- exact layout
- logo
- author's face or private material
- product photos
- signature visual identity
- full copy

Good user-facing wording:

我会参考这张图的排版、信息层级和点击理由，但不会照抄它的文字、logo、作者素材和完全相同构图。

## Known Image Generation Bugs / Limits

Treat these as normal provider limitations and route around them.

### 1. Chinese Text Instability

Symptoms:

- wrong Chinese characters
- distorted text
- tiny unreadable labels
- inconsistent page numbers

Mitigation:

- keep the largest title short
- reduce label count
- put long copy in caption or page text, not inside the image
- if exact text rendering is critical, generate a clean background/layout first
  and use a deterministic editor when available

### 2. Crowded Covers

Symptoms:

- too many modules
- all text has the same weight
- no clear visual focus

Mitigation:

- reduce text by 40-60%
- one big title, one subtitle, 2-3 labels maximum
- move details to inner pages

### 3. Generic AI Poster Look

Symptoms:

- pretty but empty
- poster-like gradient
- no Xiaohongshu information structure

Mitigation:

- add Xiaohongshu-specific structure: page number, title tag, checklist cards,
  bottom action bar, arrows, before/after lane, save reason

### 4. Reference Over-Copy Or Under-Follow

Symptoms:

- generated image is too similar to the reference
- generated image ignores the reference entirely

Mitigation:

- specify `reference_mode`: structure/style/layout/color
- state which parts to borrow and which parts to change
- avoid asking for "same style" without decomposition

### 5. Material Hallucination

Symptoms:

- fake product
- fake place
- fake app screenshot
- fake person

Mitigation:

- if no real material exists, choose no-person knowledge card
- never invent user-specific product/place/person details

### 6. Weak Face-Led Cover

Symptoms:

- ordinary selfie with no expression or identity
- face does not match the topic keyword
- title says a strong claim but the image gives no proof
- user only has one face-led note while the rest of the account is pure graphic
  notes, causing weak account recognition

Mitigation:

- use split screen or four-grid to add proof and content density
- make identity visible in text: role, age, city, profession, authority, stage
- if expression/authority/proof is weak, switch to no-person knowledge card
- do not advise a full face-led direction unless the user can keep producing in
  that style

### 7. Weak Interaction Prompt Cover

Symptoms:

- simple text and emoji, but no real comment impulse
- emoji expression does not match the title emotion
- highlighted words are decorative rather than the actual trigger words
- topic is unrelated to the user's account, so the comments do not convert into
  useful followers
- prompt copies an old viral format that users have already seen too often
- the post may get lively comments, but the user has no next normal post to
  continue the account mainline

Mitigation:

- ask the user to send existing account links, recent 5-10 notes, or topics
  they want to keep posting
- map the account lane first: city, track, audience, content format, and next
  1-3 normal posts
- generate interaction prompts from the lane, not from random viral examples
- pair the cover with a follow-up plan: after the comments come in, summarize,
  answer, or turn the best comments into the next post
- choose the emoji/sticker after the title is fixed, not before

### 8. Weak Text-Dense Screenshot Graphic Note

Symptoms:

- users cannot tell the topic in the first 1-2 seconds
- page 1 looks like a raw screenshot or cropped article with no designed entry
- too much body text has the same weight
- no keywords are bolded, highlighted, or placed where eyes naturally land
- page 2 does not deepen the promise; it repeats page 1 or becomes generic
- generated Chinese is tiny, distorted, cut off, or not worth reading

Mitigation:

- extract before designing: topic, audience, 3-5 keywords, strongest sentence,
  and 4-page/7-page outline
- redesign the first page as a scanning cover, not a literal screenshot
- use one headline, 2-3 highlighted keyword clusters, and shorter paragraphs
- make page 2 the proof/substance page: framework, data, contrast, workflow, or
  key example
- move long explanation to the caption or later pages
- if exact long Chinese text must be preserved, use deterministic editing after
  generation instead of asking the image model to render all text perfectly

### 9. Weak Room-As-Identity Lifestyle Cover

Symptoms:

- the image shows a room, but no life-stage question or new narrative
- objects are visible, but they do not prove the creator's choices or content
  direction
- the title could be pasted onto any bedroom/study-room photo
- the room looks polished but not ownable, repeatable, or connected to the
  user's real life
- the account cannot continue the same scene after one post

Mitigation:

- identify the narrative first: age reversal, solo living, reading life,
  self-consistency, small-room freedom, digital setup, or another clear lane
- choose 1-3 room proof objects that support the narrative
- keep angle/style repeatable so the homepage builds one recognizable world
- pair the cover with a next-post series plan, not only one pretty image
- warn users when the reference account's hidden resources make full imitation
  difficult

### 10. Multi-Page Inconsistency

Symptoms:

- each page looks like a different template
- colors/fonts/page numbers are inconsistent

Mitigation:

- generate with a shared page system: same color palette, page number position,
  title zone, card style, bottom bar
- if needed, generate cover first, then use it as style reference for inner
  pages

### 11. Aspect Ratio Or Cropping Problems

Symptoms:

- title cut off
- subject cropped awkwardly
- WeChat cover rendered like vertical poster

Mitigation:

- pass platform and aspect ratio explicitly
- keep safe margins around title and logo
- use Xiaohongshu vertical 3:4/4:5 and WeChat wide 900:383 or 1080:460

### 12. Provider/Network/Permission Failure

Symptoms:

- missing image URL
- expired asset
- provider timeout
- missing API key/credits

Mitigation:

- return a friendly message and the prepared image brief
- never expose provider stack traces
- tell the user how to open Lingzao web setup/recharge/API Key entry
- if a generation job fails before producing an image, clarify whether credits
  were consumed according to backend truth

## Domestic Agent Experience Rules

For domestic Agents, optimize for "the user can just talk".

Do:

- infer platform and format from user wording
- ask one small question only when it changes the route
- default to Xiaohongshu 4-page graphic note for "帮我做图文"
- default to WeChat 1+3 pack for "公众号配图"
- default to no-person knowledge card if the user has no photo/material
- generate actual images when available
- show a friendly repair diagnosis if the result is ugly

Do not:

- ask users to write prompts
- expose model name, provider params, stack traces, signed URLs, or raw payloads
- force users to choose from many styles
- ask long design questionnaires
- keep regenerating blindly
- call every pretty image "good"

## User Homework For A Tian

When A Tian wants to strengthen this system, collect examples in this shape:

1. Good image examples
   - link or screenshot
   - why it is good
   - what part is learnable
   - what kind of user/track it fits
   - if it is face-led, what the face contributes: expression, identity,
     authority, contrast, or proof scene

2. Bad image examples
   - what feels ugly
   - is the problem title, hierarchy, color, subject, style, or text rendering
   - what repair direction would make it usable

3. Reference image examples
   - what should be borrowed
   - what must not be copied
   - what topic/user it could be adapted to

4. Track-specific image examples
   - female growth
   - AI tools/tutorials
   - local life/food/travel
   - face-led口播/视频封面
   - interaction prompt covers / 互动帖
   - text-dense screenshot graphic notes / 长文截图式图文
   - room-as-identity lifestyle covers / 房间即人设
   - WeChat article
   - product/course/service

These examples should be converted into style rules, not copied as private
assets.

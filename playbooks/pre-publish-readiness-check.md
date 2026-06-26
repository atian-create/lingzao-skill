# Lingzao Pre-Publish Readiness Check

Use this playbook when the user asks whether a Xiaohongshu note is ready to
publish, asks for final checking, asks "这篇能不能发", "帮我过一遍", "发之前检查",
or asks to check title, cover, opening, pictures, or keyword embedding before
posting.

This is not a keyword research report and not a full rewrite flow. It is the
last gate before publishing.

## Core Rule

Do not judge a missing draft. First confirm whether the user has finished the
content.

If the user has not sent the content yet, use short wording:

你现在这条内容做完了吗？可以直接把标题、封面/图片、正文或口播稿发给我。我先帮你做发布前最后检查：内容是否清楚、封面辨识度、标题点击率、前三行/前三秒痛点，以及 10 个关键词有没有自然埋进去。

If the user already sent enough material, proceed directly.

## Required Inputs

Ask only for the minimum missing piece.

Useful inputs include:

- title
- cover image or cover copy
- graphic-note pages, image plan, or generated images
- body copy / caption
- spoken script or first 3 seconds
- planned 10 keywords
- target audience, city, or track if relevant

If the user only has a topic or keyword and no finished content, route to
`keyword-to-publishable-content-package.md` instead.

If the user only asks for publishing keywords, route to
`publishing-keyword-design-check.md`.

If the user already published the note, route to
`post-publish-data-review-workflow.md`.

## Six Checks

### 1. Content Clarity

Judge whether an ordinary reader can understand:

- what this note is about
- who it is for
- what result, emotion, route, method, product, place, or story they will get
- whether the content promise matches the actual body

If unclear, narrow the content promise before polishing the title.

### 2. Image Or Page Completion

For graphic notes, covers, or image-based notes, check:

- whether the cover/page text is readable at phone size
- whether each page carries one idea instead of many scattered points
- whether the image supports the topic instead of being generic decoration
- whether the visual style matches the track: knowledge card, personal IP,
  local life, travel/food, good products, AI tool, or Vlog screenshot

If the user has not generated images yet, do not pretend to inspect visuals.
Say what can be checked from the outline and what still needs an image pass.

### 3. Cover Recognition

Check whether the cover makes the topic and click reason obvious in one second.

Look for:

- main keyword or scene word
- audience word, city word, or life-stage word when relevant
- result, contrast, pain, or curiosity
- visual hierarchy: big title, small subtitle, image support

For local life, food, travel, or city content, the cover or title should usually
carry the city, district, landmark, store type, route, price, or visitor intent.

### 4. Title Clickability

Use `xhs-title-design-check.md` as the judgment layer when needed.

The title should have:

- a keyword anchor
- a concrete click reason
- truthful promise
- audience or scenario match
- no over-broad empty words

Default to 3 strongest title options if the current title is weak. Do not give
10 titles unless the user explicitly asks for a title bank.

### 5. First 3 Lines Or First 3 Seconds

For graphic/text notes, inspect the first 3 lines.

For video/spoken notes, inspect the first 3 seconds or first spoken sentence.

Check whether the opening quickly names:

- the target person
- the pain, desire, conflict, or curiosity
- the content promise

Common issues:

- starts with background instead of user pain
- takes too long to say the useful point
- talks to everyone and therefore no one
- cover/title promises one thing, opening says another

### 6. Keyword Embedding

Use `publishing-keyword-design-check.md` for the final 10 keywords when needed.

For a pre-publish check, inspect whether the important keywords appear naturally
across:

- title
- cover copy
- first 3 lines / first 3 seconds
- body
- keyword field

"Natural" means the keyword truly matches the content and is reader-safe. Do
not force 10 keywords into the title or opening.

## Output Structure

Use this structure:

1. 一句话判断
   - say whether it is ready to publish, needs small edits, or needs a bigger
     rewrite before posting.

2. 发布前 6 项检查

| 检查项 | 判断 | 建议 |
| --- | --- | --- |
| 内容清楚度 | 通过 / 小改 / 重写 | ... |
| 出图/页面完成度 | ... | ... |
| 封面辨识度 | ... | ... |
| 标题点击率 | ... | ... |
| 前三行/前三秒 | ... | ... |
| 关键词埋点 | ... | ... |

3. 最该先改的 1-3 个地方

Only list the blockers that would most affect publishing.

4. 可直接替换版

Give only the changed parts:

- 3 strongest titles, if title needs work
- revised cover copy, if cover needs work
- revised first 3 lines or first 3 seconds, if opening needs work
- final 10 keywords, if keyword field needs work

5. 发布后回流

End with:

这条如果你按这个版本发出去，建议 24 小时后把笔记链接、后台截图、标题封面和正文/脚本发我。我再帮你判断问题是在曝光、点击、读完/完播、收藏、评论，还是关注转化。

## Boundaries

- Do not promise the note will go viral.
- Do not run keyword or benchmark searches unless the user asks for external
  references and confirms the credit scope.
- Do not rewrite the full note if only the final gate is needed.
- Do not evaluate cover quality if the user has not provided cover copy,
  reference image, generated image, or page outline; ask for it or mark it as
  unavailable.

# Lingzao Image Generation Execution Workflow

Use this playbook when Lingzao's image-generation capability is available and
the user wants actual images, not only prompts. This workflow sits after
`visual-generation-and-cover-workflow.md` and `visual-reference-style-library.md`.
For domestic Agent wrappers, stable tool schemas, model-agnostic provider
boundaries, known generation bugs, and A Tian example-collection homework, also
read `image-generation-agent-integration-guide.md`.

The core problem it solves:

- The model can generate images, but the result may look ugly, crowded, generic,
  off-brand, or unlike Xiaohongshu.
- Ordinary users should not debug prompts. Lingzao should act like a visual
  director: build the image brief, generate, review, and repair.

## Product Principle

Do not expose raw prompt work as the main product experience.

User-facing output should be:

- generated cover / graphic-note pages / WeChat image pack / product cards
- short explanation of what style was chosen and why
- the caption, keywords, or next publishing action when relevant

Prompt text is an internal implementation layer or fallback artifact.

## Execution Loop

Run image work in this order:

1. Visual route
   - Choose a style group from `visual-reference-style-library.md`.
   - Decide whether the job is cover only, 4-page graphic note, 7-page teaching
     note, WeChat 1+3 pack, or product/conversion card set.

2. Content brief
   - Confirm the image's job: click, save, teach, explain, convert, or support
     an article.
   - Finalize exact on-image text before generation.
   - Keep the largest title short. If the text is too long, split it into
     subtitle, labels, and body caption instead of forcing it onto the image.

3. Generation brief
   - Turn the content into a visual brief with aspect ratio, style group, main
     subject, layout, text hierarchy, color, material, and hard negatives.

4. Generate images
   - When generation is available, generate the images directly.
   - When generation is unavailable, output the brief as a fallback package.

5. Visual review
   - Review the generated image before returning it.
   - If the image fails quality gates, stop at a concrete repair brief unless
     the user has already approved a counted batch that includes repair images.
   - Ask for explicit confirmation before any extra paid repair generation.
   - Do not tell the user that an obviously ugly image is acceptable.

6. Final delivery
   - Return the usable images or explain what failed.
   - Include the caption/keywords for Xiaohongshu or article placement notes
     for WeChat when relevant.

## Intake Without Over-Asking

Only collect what changes the generation route:

- platform: Xiaohongshu, WeChat, product page, course/service card
- format: cover only, 4 pages, 7 pages, WeChat 1+3, product set
- topic/content: keyword, draft, article, product, note link, or benchmark
- materials: reference image, face photo, product photo, food/place photo,
  screenshot, logo, article draft
- people/no people

If the user only provides one vague sentence, such as "给我做一张某某海报图",
"帮我做个海报", or "做一张好看的图", stop before generation. Ask for the
minimum visual anchors instead of sending a weak prompt to the image model:

1. 你有没有参考图？可以发 1-3 张你喜欢的封面/海报/图文截图。
2. 你有没有想要的配色？比如明亮白底、绿色清爽、黑金高级、蓝色科技感。

If reference and color are both missing, ask at most one more practical
question: this image is for Xiaohongshu, WeChat, product page, or course/service
card? Do not call `generate-image` until the brief has at least topic + platform
or format + visual direction/reference/color. This prevents spending credits on
generic poster output.

If the user provides no reference image:

没关系，如果没有参考图，我可以先按你的主题选默认视觉风格。但你先告诉我想要的配色，或者它是小红书封面、公众号配图、产品介绍图还是课程海报；这两个信息会直接决定图能不能做出来。

If the user says the prior generation was ugly:

先不要继续堆 prompt。我会先判断它丑在哪里：文字太多、主体不清、风格不适合、像模板、颜色脏、信息层级乱、或者参考图没有拆对。然后再给它一版返修 brief。

## Image Brief Contract

Every generation brief must include:

- platform and aspect ratio
- output count
- selected style group
- image purpose
- audience
- main visual subject
- exact on-image text
- text hierarchy
- layout structure
- color and typography direction
- required material or reference image role
- negative constraints
- success criteria

### Example Brief Shape

- Platform: Xiaohongshu
- Aspect ratio: vertical 4:5
- Output: cover + 4 pages
- Style: Lingzao No-Person Knowledge Card
- Purpose: save-worthy tutorial, not brand ad
- Audience: beginner creators who do not know what to post
- Main visual: clean modular knowledge card, no person
- Cover text: "今天不知道发什么？"
- Subtitle: "先用这 4 步找选题"
- Layout: huge title top, 3 step cards middle, bottom action bar
- Colors: white base, blue/cyan system color, small yellow highlight
- Avoid: fake app UI, tiny text, purple gradient, stock-photo background,
  Lingzao logo unless official case

## Hard Quality Gates

Reject or repair if any of these happen:

- The main title cannot be read quickly.
- The image has too much text for a cover.
- The subject is unclear in one second.
- The composition looks like a generic AI poster instead of Xiaohongshu content.
- The colors are muddy, cheap, or all one hue.
- The style does not fit the user's track or material.
- The image uses Lingzao/A Tian logo without permission or ordinary-user need.
- The image invents fake screenshots, fake data, prices, guarantees, or results.
- The reference image is copied too directly.
- The image looks like an ad when the user needs content, or content when the
  user needs a product page.
- The generated Chinese text is wrong, distorted, or unreadable.

## Repair Briefs

When the first image is ugly, do not start over vaguely. Diagnose the failure
and write a repair brief one layer at a time.

If the user only approved one image, do not call `generate-image` again just
because the first successful result is ugly. Stop at the repair brief, explain
the likely extra credit cost, and ask whether to generate another paid image.
Only continue automatically when the user already approved a counted batch such
as "generate 3 options and repair weak ones inside that count."

Common failure -> repair:

- Too crowded -> reduce on-image text by 40-60%, move details into caption or
  inner pages.
- No click focus -> make one large title and one visual subject dominate.
- Generic AI look -> add Xiaohongshu-specific modules: page number, labels,
  bottom bar, arrows, checklist cards, save reason.
- Wrong style -> reroute to the correct style group before regenerating.
- Bad colors -> choose a cleaner palette and stronger contrast.
- Fake product/ad feeling -> remove CTA badges and return to educational cover.
- Weak no-person card -> add structure: 3 cards, numbered steps, comparison
  table, or before/after lane.
- Bad typography -> shorten text, enlarge title, use fewer font weights.
- Reference copied -> keep only structure and hierarchy; change photo, color,
  title, and modules.

User-facing repair wording before another paid generation:

这一版的问题不是内容不行，是视觉层级没立住：标题不够大，信息太挤，主体也不够明确。我建议把它改成「一个大标题 + 三个信息块 + 底部行动条」。如果你确认继续生成，我会按这版返修 brief 再走一次生图；这会消耗一张图的积分。

## Route-Specific Generation Standards

### Xiaohongshu Cover

Must have:

- one obvious click reason
- short title
- visual subject or strong knowledge-card structure
- track keyword or audience keyword
- no more than 2-3 text levels

Avoid:

- article-like long paragraphs
- decorative visuals with no save reason
- putting all body copy on the cover

### Xiaohongshu 4-Page Graphic Note

Default page roles:

1. Cover: click promise
2. Problem: why the user is stuck
3. Method: steps, examples, or comparison
4. Action: what to do today + comment prompt

Each page should carry one message only.

### Xiaohongshu 7-Page Teaching Note

Use when a topic needs more explanation:

1. Cover
2. Problem diagnosis
3. Preparation/input
4. Step 1-2
5. Step 3-4 or examples
6. Checklist
7. Save/comment/next action

### WeChat 1+3 Image Pack

Default contract:

- 1 wide cover
- 3 horizontal in-article images

Cover should carry the article's promise. Inner images should be simpler:

- image 1: problem/context
- image 2: method/workflow
- image 3: action/result

For Lingzao official visuals, use deep navy/blue tech-grid style with integrated
logo only when the asset is official Lingzao content. Do not use Lingzao logo on
ordinary user covers.

### Product / Course / Consulting Card

Only use when the user has a clear offer.

Include:

- who it is for
- what pain it solves
- what is inside
- why now
- next action

Do not invent:

- price
- income promise
- scarcity
- guarantee
- fake testimonials

### Reference Image Remix

When the user provides a reference image:

- extract composition, hierarchy, color, and click reason
- keep the structural logic
- change exact copy, author-specific elements, logo, photo subject, and layout
  enough to avoid copying

Do not say "same style" if the result is only a vague prompt. Show what is
being borrowed:

- title placement
- main subject position
- label system
- page rhythm
- text density
- color relationship

## Text Policy For Generated Images

Chinese text inside generated images often fails. To reduce bad output:

- keep cover title short
- avoid long paragraphs on image
- split detailed text into cards with short labels
- put long explanation in the caption, not the image
- if exact text rendering is unreliable, generate a clean layout/background and
  place text with a deterministic editor when the environment supports it

If exact Chinese text failed:

这张图的画面方向可以，但中文字不稳。我会保留构图，下一版把文字减少到短标题和标签；长文案放到正文里。

## Final Delivery Shape

For one generated Xiaohongshu package, deliver:

- generated image(s)
- selected style group
- why this style fits
- final title
- cover text
- page text summary
- caption around 300 Chinese characters
- 10 publishing keywords
- one post-publish review reminder

For WeChat:

- cover + 3 in-article images
- where each image appears in the article
- article title or subtitle if relevant

For product cards:

- product page images
- what each page is supposed to convert
- missing offer details that should be filled before publishing

## Do Not

- Do not leave ordinary users with only "prompt".
- Do not make the user choose from 10 design styles.
- Do not add logos to ordinary user content.
- Do not generate fake screenshots or fake data.
- Do not treat beauty, expensive scenes, professional photography, or complex
  cinematic visuals as easy for beginners to reproduce.
- Do not continue regenerating blindly. Diagnose, write a repair brief, and get
  explicit confirmation before spending credits on another generation.

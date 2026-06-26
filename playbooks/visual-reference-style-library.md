# Lingzao Visual Reference Style Library

Use this library when Lingzao needs to create or route visual work for
Xiaohongshu covers, graphic notes, WeChat article covers, article images,
knowledge cards, product pages, or ecommerce-style conversion images.

This is a style-routing library, not a raw-image export. The style groups below
come from internal visual references, but the distributed Skill must not expose
private local filesystem paths or imply that ordinary users can access A Tian's
local folders.

Use the style groups to identify visual category, composition logic, and prompt
direction. Do not copy private image files into user deliverables, do not expose
internal source paths to ordinary users, and do not claim the generated image is
copied from a private reference.

## Sanitized Internal Source Categories

The private source material has been abstracted into these distributable style
groups:

1. Travel / food / local-life covers.
2. WeChat article covers and in-article image packs.
3. AI simple information graphics.
4. Lingzao no-person information cards.
5. Product / ecommerce / personal-IP conversion images.
6. Face-led keyword video covers.
7. Interaction prompt covers.
8. Text-dense screenshot graphic notes.
9. Room-as-identity lifestyle covers.

## Style Groups

### 1. Travel Food Local-Life Cover

Use for:

- travel tips, cheap eats, city guides, transport guides, local-life exploring
- "where to eat / how to go / is it worth it / avoid this pitfall" topics
- users with photos of places, food, transport, menus, tickets, or city scenes

Visual traits:

- vertical Xiaohongshu cover, usually 3:4 or 4:5
- real food / transport / place photo as the main visual
- strong location label, often with flag, country/city tag, route tag, or issue
  number
- huge high-contrast title, often yellow/pink/white text with dark outline
- dense sticker system: arrows, hearts, stars, speech bubbles, small labels
- small persona/avatar/photo cutout when available, usually near a lower corner
- useful micro-information: price, route, steps, order tips, local words,
  address hint, "worth it / not worth it" judgment

Best output:

- one strong cover plus 3-6 inner pages for itinerary, price, route, ordering,
  and avoid-pitfall details
- if only one image is requested, prioritize click reason plus practical proof:
  place + price/route + one clear judgment

Avoid:

- clean luxury travel posters with only scenery and no information
- vague "beautiful place" covers that do not explain why to click or save
- recommending this style to users who have no place/food/route/photo material,
  unless Lingzao is creating an AI-assisted graphic-note version

### 2. WeChat Article Knowledge Pack

Use for:

- WeChat article cover, WeChat article image pack, official long-form article
  visuals, creator-business explainers, Lingzao release notes, Skill tutorials
- "公众号封面", "公众号配图", "正文配图", "4 张图", "1 封面 + 3 正文图"

Visual traits:

- wide horizontal image, usually 900:383 or 1080:460
- two submodes:
  - A Tian knowledge mode: cream/paper background, cartoon IP, black outline,
    many small knowledge cards, arrows, checklists, stickers, module panels
  - Lingzao branded mode: dark navy or deep blue tech-grid background, Lingzao
    logo, cyan/teal/green glow, large non-black headline text, no people
- article image packs should keep visual continuity across 4 images
- in-article images should be simpler than the cover: fewer cards, fewer
  slogans, one point per image

Best output:

- 1 cover + 3 horizontal in-article images by default when the user asks for a
  WeChat package
- cover carries the big promise; three inner images map to problem, method,
  action/result

Avoid:

- using A Tian cartoon IP for Lingzao official brand assets unless explicitly
  requested
- using Lingzao logo for ordinary user Xiaohongshu covers
- putting too much article text into the image

### 3. AI Person Tool Infographic

Use for:

- AI tools, personal knowledge-base workflows, courses, tutorials, "how I use
  AI", "from 0 to 1", creator tool demonstrations
- users who can provide a face/person photo or are willing to use a personal-IP
  portrait
- posts where a screenshot, UI, app, workflow, or tool result needs to be shown

Visual traits:

- vertical Xiaohongshu cover, high information density
- real person or face cutout as trust anchor
- UI screenshot, tool interface, course cover, prompt panel, app screen, or
  workflow card as the second anchor
- huge title with strong keywords, often black/white/yellow/neon green/pink
- many small labels: "教程", "新手", "从0开始", "合集", "效率", "不用代码"
- energetic sticker style, sometimes black or dark background for contrast

Best output:

- one cover plus 4-page graphic note: problem, input/action, tool/result,
  today-do-this
- if a user provides both face and tool screenshot, use face as image 1 and
  screenshot/product as image 2 in the prompt

Avoid:

- recommending this style when the user cannot explain the tool or workflow
- overusing fake technical UI that the user cannot reproduce
- using it for quiet emotional/lifestyle content where a soft photo or pure
  card would fit better

### 4. Lingzao No-Person Knowledge Card

Use for:

- no-face Xiaohongshu graphic notes
- Lingzao / Agent / Skill / workflow explainers
- users who do not have photos, do not want to show their face, or need a clean
  educational card
- keyword-to-content packages when the user has no reference image and needs a
  ready-to-generate pure knowledge-card style

Visual traits:

- vertical Xiaohongshu card, usually white or very light background
- blue/cyan as the primary system color, with small green/yellow accents
- clear big headline, often one strong sentence
- structured modules: steps, comparisons, checklists, before/after, workflow
  lanes, table-like cards
- icons, small UI elements, numbered circles, status tags, bottom summary bar
- no people, no cartoon, no heavy scenery

Best output:

- 4-page graphic note by default for fast publishing:
  1. cover with big question or result
  2. why this matters / what changed
  3. workflow / steps / examples
  4. today post these / next action / comment prompt
- 7-page version when the topic needs more teaching

Avoid:

- making the card too Word-table-like
- long paragraphs on the image
- using a one-note blue palette without enough hierarchy

### 5. Product Ecommerce Conversion Card

Use for:

- personal-IP products, paid materials, courses, consultations, community,
  worksheets, template packs, ecommerce product intro, productized service
  pages
- users who already have an offer, product, course, paid document, or consulting
  service

Visual traits:

- vertical product page, poster, or carousel page
- pastel or high-contrast background, often with rounded modules
- cartoon/persona/IP figure can appear as a trust anchor
- product promise, who it is for, pain points, deliverables, price/offer, CTA
  button, badges, guarantee-like labels, or "limited" wording
- more conversion-oriented than ordinary content covers

Best output:

- product intro cover + 3-5 inner pages:
  1. pain / why this exists
  2. product promise
  3. what is inside
  4. who it fits / who it does not fit
  5. price / action / next step, if the user has confirmed selling details

Avoid:

- adding prices, scarcity, income claims, or guarantees unless the user provides
  them
- turning a content note into a hard sales page too early
- using this route for users who only need an educational post or first test

### 6. Face-Led Keyword Video Cover

Use for:

- Xiaohongshu video covers where a real person is the trust anchor
- AI tools, creator business, self-media, career, education, commentary,
  family/parenting, or personal-IP topics where the face, identity, and keyword
  create the click reason together
- users who already show up on camera consistently, or have clear expression,
  identity, authority, humor, contrast, or performance

Core idea:

The person is not decoration. The face must carry at least one of:

- expression: explosive, funny, confident, surprised, serious, persuasive
- identity: 博士, 小孩姐, founder, PR, product manager, self-media creator,
  parent, student, professional, local guide
- contrast: ordinary face + strong keyword, child + adult topic, expert name +
  future-looking claim, average-looking creator + information-rich split screen
- proof: visible editing timeline, screenshot, tool interface, product, street
  scene, classroom, studio, food/place material

Visual traits:

- vertical Xiaohongshu 3:4 or 4:5 video cover
- large human face or upper body as the primary trust/attention anchor
- huge keyword title, usually high-contrast yellow/red/white/pink text with
  thick outline or dark block background
- either full-face single frame, top-bottom split screen, four-grid, diagonal
  split, or person + proof scene
- keywords must be obvious: AI剪视频, 不赚钱当什么博主, AI大爆发, 小孩姐,
  自媒体赚钱, 快速学AI, 时间, 立马获得感
- if the person's appearance is not highly distinctive, use split-screen,
  four-grid, or proof-scene structure to increase information density

Best output:

- one face-led cover plus a short video/script direction
- cover should make the user's identity and promise clear in one second
- for tutorial videos, show both person and result/proof scene, such as editing
  timeline, software screen, before/after, or output preview
- for authority videos, make the name/title/identity part of the click reason
- for child/age/identity contrast, make the unusual perspective explicit in the
  first title line

Avoid:

- recommending this style when the user has no camera confidence, no consistent
  face presence, poor speaking ability, weak background, or only one random
  face video among mostly graphic notes
- forcing a plain selfie if the person has no expression, no identity, no proof
  scene, and no strong keyword
- changing a graphic-note account into a face-led account too abruptly; it may
  weaken recognition or even lose followers if the person/voice/style cannot
  carry the content
- treating "露脸" as automatically better than no-person cards

When to choose no-person instead:

- the person is not visually distinctive and has no authority/identity hook
- the user is not ready to show up repeatedly
- the topic is more useful as a checklist, framework, or knowledge card
- the user's previous account memory is built on graphic notes

Account consistency rule:

Face-led covers work better when the user's surrounding content also has a
similar face/video style. A single strong face cover may get clicks, but users
follow only when the homepage shows similar content promises, style, tone, and
identity across multiple notes.

### 7. Interaction Prompt Cover

Use for:

- Xiaohongshu interaction posts, account-starting posts, comment-driving posts,
  and "ask everyone" topics
- users who want a low-production way to activate comments before or between
  heavier posts
- local life, food, travel, community, relationship, workplace, hobby, and
  creator-topic prompts where the comment section is the main content asset
- wording such as "互动帖", "评论区很热闹", "起号互动", "问大家", "交出来",
  "你们怎么看", "有没有", "大家自从", "哪期/哪个/什么让你觉得"

Core idea:

Interaction prompt covers are not only "a yellow emoji plus text". They work
because the image, highlighted keyword, and community question make users want
to open the comments and stay there. The goal is comment desire and dwell time;
follow conversion happens only when the topic matches the account's content
mainline.

Visual traits:

- vertical Xiaohongshu 3:4 or 4:5 cover
- simple white, light, note-app, or PPT/comment-screenshot-like background
- large black or dark gray text with very few words
- 1-2 trigger words highlighted with blue, green, pink, yellow, marker strokes,
  or underline blocks, such as "夯爆了", "姐妹迷上", "有意思", "非常帅"
- one matched emoji/sticker/yellow-face expression, such as laughing-crying,
  thinking, shy, shocked, or inspecting; the expression must fit the title's
  emotion
- staged classroom/PPT projection or comment-screenshot scenes are allowed, but
  do not pretend they are real screenshots if they are designed scenes
- the cover often looks simple, but the prompt must be precise enough that
  users feel "I also want to answer this"

Best output:

- one interaction cover plus 5-10 account-relevant interaction topics
- include a short caption that pushes users to comment without sounding like
  empty engagement bait
- for existing accounts, first map the user's recent notes/account links, then
  generate interaction topics that can feed the next 1-3 normal posts
- for a local-food account with several Shantou posts, good prompts include:
  "把你们汕头的美食全部交出来", "汕头哪里的东西到底好吃啊", and "明天马上到汕头，
  交出你们的汕头美食宝藏地图"

Avoid:

- using a random emoji that does not match the question's emotion
- copying a stale interaction prompt just because an old post was viral
- making a topic that is unrelated to the user's account; it may get comments
  but will not bring useful followers, and the next post can break the account
  direction
- forced controversy, fake screenshots, fake comments, or bait that the user
  cannot continue with real content
- treating interaction posts as a mature-account strategy only; they can help
  activate a starting account, but they still need a content mainline

### 8. Text-Dense Screenshot Graphic Note

Use for:

- Xiaohongshu graphic notes that look like dense article screenshots,
  newsletter screenshots, X/Twitter threads, Weibo posts, memo notes, or
  redesigned public-account text pages
- AI tool tutorials, creator workflows, female growth, strong opinions, account
  lessons, industry observation, public apology/statement analysis, and other
  topics where users expect "a lot of useful content"
- users who have long drafts, saved notes, transcripts, comment summaries, or
  research material and want to convert them into easy-to-produce graphic notes
- account-starting content where the creator can keep posting text-heavy,
  useful, keyword-clear pages consistently

Core idea:

This style creates a "there is a lot to learn here" feeling. It is not an
interaction prompt cover and not a clean knowledge card. The design can be
simple, but the first page must let users understand the topic and key benefit
within 1-2 seconds. Most users will scan keywords, not read line by line.

Visual traits:

- vertical Xiaohongshu 3:4 or 4:5 page
- looks like a cropped article, memo, public-account page, X/Twitter thread,
  Weibo post, or long-form screenshot that has been redesigned
- heavy text density, but with one very clear headline or opening claim
- black/white, cream/brown, dark card, or light-gray platform screenshot style
- large headline + smaller paragraphs, or platform-header area + body text +
  visible metrics/labels when they are real and provided
- keywords are bolded, colored, highlighted, underlined, or placed at line
  starts so users can scan the page in one second
- page 1 and page 2 matter most: page 1 makes the promise; page 2 proves there
  is substance

Best output:

- 4-page or 7-page graphic note that starts from a keyword-extracted outline:
  1. cover/opening screenshot with the biggest keyword and promise
  2. dense proof page with the strongest framework, numbers, or conflict
  3. step/workflow/list page
  4. takeaway/action/comment page
- if the source material is long, first extract topic, audience, 3-5 keywords,
  and the most clickable sentence before generating page text
- keep the account style repeatable: same background, font hierarchy, highlight
  color, title zone, and body rhythm across multiple posts

Avoid:

- raw screenshots with no keyword extraction
- first pages where users need to read several lines before understanding the
  topic
- tiny text, cut-off text, or page bodies that are only readable after zooming
- using this route for users who need emotional atmosphere, product visuals,
  food/place proof, or face-led trust instead
- filling the image with AI-generated filler paragraphs; the perceived density
  must come from useful points, not word count
- pretending fake platform metrics, likes, comments, timestamps, or account
  names are real

### 9. Room-As-Identity Lifestyle Cover

Use for:

- study-room, bedroom, desk, reading corner, rented-room, solo-living, or small
  home-space accounts where the room itself proves the creator's lifestyle
- female-growth, solo-living, age-stage, reading, digital setup, learning,
  self-consistency, new-life-narrative, and "I can also live like this" topics
- users who have a real repeatable space: books, desk, chair, tablet, e-reader,
  screens, notes, clothes, bed, light, wall stickers, or daily-use objects
- accounts where commercial objects can naturally enter the scene, such as
  functional chairs, tablets, e-readers, lamps, desks, screens, bookshelves,
  bedding, organizers, and digital devices

Core idea:

The room is not background decoration. It is evidence of the person's choices,
freedom, resources, taste, rhythm, and life possibility. This style works when
the space helps create a new narrative, such as "32 is still early", "solo
living can be rich", "not married/no children can still have a full world", or
"a small room can grow a strong content system".

Visual traits:

- vertical Xiaohongshu covers built from repeated real room angles
- book piles, desk, bed, closet, chair, tablet/e-reader, multiple screens,
  wall notes, warm lamp, and lived-in clutter become memory anchors
- text is often simple and narrative-led: "才32岁谁懂", "32岁后续来了", "独居",
  "每天收拾房间", "太舒服了谁懂"
- room angle consistency matters; the homepage should look like one continuous
  world, not random home photos
- proof objects can double as future ad assets when they naturally belong in
  the room

Best output:

- one cover plus a series direction, not only a one-off image
- identify the life-stage keyword, room proof, and repeatable scene:
  1. age/life-stage reversal
  2. room-as-proof photo
  3. short narrative title
  4. next 3-5 posts that continue the same world
- for users studying this account type, separate learnable structure from
  non-copyable resources

Avoid:

- treating it as ordinary "book account" or "home decor account"
- copying the room if the user does not have a real space, objects, reading
  habit, or daily routine to sustain it
- recommending it only because the room is full of books; the story, keywords,
  and person/space contrast matter more than the book count
- ignoring hidden difficulty: prior content-operation experience, speaking or
  humor ability, saved money, property/rent freedom, device resources, reading
  ability, and other accounts may all be part of why it works
- forcing a polished show-home style; the charm may come from a small, crowded,
  real, ownable room

## Default Routing

When the user asks for an image but gives no reference image:

- travel, food, city, local life, transport -> Travel Food Local-Life Cover
- WeChat article, official post, article image pack -> WeChat Article Knowledge
  Pack
- AI tool, software, course, tutorial, personal workflow with face/screenshot ->
  AI Person Tool Infographic
- face-led video,口播, personal-IP commentary, self-media/career/AI/family
  education with a real person -> Face-Led Keyword Video Cover
- interaction post, comment-driving question, account-starting prompt,
  "问大家/交出来/你们怎么看/评论区很热闹" -> Interaction Prompt Cover
- long draft, dense text, article screenshot, X/Twitter/Weibo/public-account
  screenshot style, "很多干货/文字堆叠/图文风格" -> Text-Dense Screenshot
  Graphic Note
- study room, bedroom, solo-living, reading corner, desk setup, age/life-stage
  lifestyle, "才32岁/独居幸福感/自己的房间" -> Room-As-Identity Lifestyle Cover
- no-face knowledge explanation, Lingzao workflow, Agent method, pure tutorial ->
  Lingzao No-Person Knowledge Card
- paid product, course, consultation, community, product page, ecommerce ->
  Product Ecommerce Conversion Card

When multiple routes are possible, prioritize the user's available material:

- has face + screenshot/product -> AI Person Tool Infographic
- has face + strong expression/identity/authority/proof scene -> Face-Led
  Keyword Video Cover
- wants comments or account activation through a simple question/poster ->
  Interaction Prompt Cover
- has long text/research/transcript and wants an easy graphic-note style ->
  Text-Dense Screenshot Graphic Note
- has a repeatable room/desk/home scene that can prove the lifestyle ->
  Room-As-Identity Lifestyle Cover
- has food/place/travel photos -> Travel Food Local-Life Cover
- has no photo and wants XHS graphic notes -> Lingzao No-Person Knowledge Card
- has article draft -> WeChat Article Knowledge Pack
- has offer/product details -> Product Ecommerce Conversion Card

## Output Contract

For every visual route, output:

1. selected style group
2. why this style fits the user's topic/material
3. cover text
4. page count: 1 cover / 4 pages / 7 pages / WeChat 1+3 pack
5. page-by-page text
6. image-generation prompt or design instruction for each page
7. body copy / caption when it is a Xiaohongshu package
8. one comment or follow-up prompt

If image generation is available, generate the image after the user has either
provided a reference image or accepted the selected no-reference style. If image
generation is not available, provide the exact prompt package and tell the user
where the image generation step would happen.

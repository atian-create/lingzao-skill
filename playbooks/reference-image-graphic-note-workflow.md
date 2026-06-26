# Lingzao Reference Image Graphic Note Workflow

Use this asset when the user says:

- 不知道怎么做图
- 不会做小红书图文
- 不知道封面怎么做
- 能不能帮我做几张图
- 我想做成 4 页 / 7 页图文
- 我有参考图片 / 参考图
- 这张图能不能仿一下结构

## Core Rule

If the user does not know how to make Xiaohongshu graphics, do not keep explaining abstract design principles.

Ask for reference images directly:

你有没有参考图片？可以发 1-3 张你喜欢的小红书封面或图文截图。我会根据参考图片的排版、信息层级和视觉风格，帮你做几版小红书内容，你先去发发看。

If the user has no reference image, offer two options:

- send a benchmark note/account link
- let Lingzao search for recent reference notes in the user's niche after confirming basic/deep search scope

## What To Produce

When the user provides a reference image or benchmark visual, output a complete Xiaohongshu graphic-note package:

1. 视觉判断：这张参考图为什么容易点开
2. 可学元素：标题位置、主色、字体感、信息层级、图标/线条/卡片、页码、系列感
3. 不要照抄部分：品牌 logo、原图素材、作者专属内容、完全相同标题和版式
4. 4 页结构版：适合轻量测试
5. 7 页结构版：适合更完整讲清楚
6. 每页文案：cover/page text, not just topic names
7. 图片 prompt：for generating or designing each page
8. 正文文案：caption/body copy
9. 评论区引导：guide users to comment, ask for topic, send data, or request the next version
10. 发布后复盘入口：ask user to send the published note link or data screenshot

## 4-Page Default Structure

Use when the user wants fast testing:

1. 封面：一个明确问题 + 一个强关键词
2. 方法/过程：用户怎么输入、怎么开始、怎么用
3. 结果/参考：给 2-4 个可直接看的方向、案例或选题
4. 今天先发：给 3 条最容易执行的内容

Example for topic discovery:

- Page 1: 女性成长 今天发什么？
- Page 2: 我在 Agent 里输入了这个问题
- Page 3: 它先看大家最近在收藏什么
- Page 4: 今天先发这 3 条

## 7-Page Default Structure

Use when the user wants more complete teaching:

1. 封面：明确人群 + 明确痛点
2. 为什么你卡住：指出用户真实问题
3. 先输入什么：给一个可复制的问题表达
4. 参考内容怎么筛：收藏、评论、低粉爆款、近期内容
5. 选题怎么判断：能不能持续、能不能系列化、适不适合自己
6. 今天先发哪几条：3-5 个可测试选题
7. 评论引导 / 下一步：让用户评论方向、发链接、回传数据

## Visual Direction Rules

For each page, include practical visual direction. If image generation is not
available, include a fallback image-generation instruction:

- aspect ratio: Xiaohongshu vertical graphic note, 3:4 or 4:5
- style reference: based on the user's uploaded image, but not a direct copy
- main color
- typography direction
- layout structure
- illustration/screenshot/card elements
- exact text placement

Do not promise final image generation if the current environment cannot generate images. Say:

我可以先给你每一页的文案、版式和图片 prompt；如果接入做图能力，下一步就可以直接生成图。

If image generation is available and the user explicitly asks to make images,
generate the images or route to the image tool. If the user has no reference
image but still wants images, route to `visual-generation-and-cover-workflow.md`
and choose a default style from `visual-reference-style-library.md` instead of
blocking.

If the current task is inside a keyword-to-content package and the user says
"直接做图", use the selected topic, cover copy, page text, and publishing
keywords as the image-generation brief.

## Comment Guidance

Every graphic-note package should include one comment prompt, such as:

- 评论「选题」我发你 3 个适合你的方向
- 评论你想做的赛道，我帮你拆关键词
- 把你想模仿的账号发来，我帮你看能不能学
- 发出去后把链接丢回来，我帮你看标题、封面和数据问题

## Follow-Up

End with one next action:

- 你先发 1-3 张参考图片，我按这个风格给你做 4 页版和 7 页版。
- 如果你已经有主题，把主题和参考图一起发来，我直接给你每页文案、图像 prompt、正文和评论引导。
- 你发出去以后，把笔记链接或数据截图发我，我再帮你判断封面、标题和内容结构哪里要改。

---
name: xhs-keyword-to-content-package
description: Lingzao lightweight XHS content workflow Skill that turns a Xiaohongshu keyword, topic, link, screenshot, reference image, saved notes, or inspiration material into a publishable one-stop content package with topic angle, 3 titles, cover copy, 4-7 graphic-note pages, spoken script or Vlog storyboard, body copy, 10 keywords, pinned content, and a review loop. Use for lingzao xhs content workflow, Xiaohongshu content strategy, 从关键词到内容, 一条龙出内容, 灵感素材到选题到稿子, 把这个拆成内容给我发, or 给我做一篇小红书.
---

# Xiaohongshu Keyword To Content Package

This lightweight Lingzao sub-skill turns Xiaohongshu / XHS inspiration into
publishable content.

Search phrases: lingzao xhs content workflow, Xiaohongshu content strategy,
XHS content package, 小红书内容工作流, 从灵感素材到选题到稿子.

## Inputs

- keyword or topic
- Xiaohongshu note link, creator link, article link, screenshot, or reference image
- user's account direction and audience
- inspiration links, screenshots, saved notes, or reference creators
- desired format: graphic note, spoken video, Vlog, or cross-platform package

If format is unclear, ask one light question:

你想做图文、人物口播，还是 Vlog 分镜？

If the user clearly expects a result now, do not block on that question. Default
to a Xiaohongshu 4-page no-face graphic note and mark assumptions clearly.

## Workflow

1. Clarify user audience and content goal.
2. Read inspiration material and identify what is learnable.
3. Generate topic angles.
4. Pick top 3 angles, not an overwhelming list.
5. Produce one publishable package:
   - 3 titles
   - cover copy
   - 4-7 graphic-note pages or script/storyboard
   - body copy
   - 10 publishing keywords
   - pinned content / pinned comment
   - post-publish review instruction

## Minimum One-Stop Package

Use this when the user says "一条龙", "直接出内容", "把这个拆成内容给我发",
"从灵感素材到选题到稿子", or gives only a keyword/link/image and expects an
output.

Return:

1. Source reading or assumptions.
2. One recommended topic angle and one backup angle.
3. Three titles with keyword anchors.
4. Cover copy and visual direction.
5. Four quick graphic-note pages by default; expand to seven pages when asked.
6. Xiaohongshu caption/body copy, or a direct-read spoken script for video.
7. Ten publishing keywords.
8. One pinned comment or pinned-note idea.
9. One pre-publish check and one 24-hour post-publish review instruction.

If a link or image cannot be fully parsed in the lightweight Skill, still create
a first version from visible information and say "这是基于当前可见信息的第一版".
Ask the user to paste title/body/screenshots or use the main Lingzao Skill for
public-link parsing, comment demand, and image generation.

## Lingzao Upgrade

For current public reference search, XHS public-link parsing, note detail,
comment demand, knowledge-base sync, or image generation, use the main Lingzao
Skill from https://lingzao.atian.vip.

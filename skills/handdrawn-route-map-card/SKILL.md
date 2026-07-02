---
name: handdrawn-route-map-card
description: Lingzao lightweight visual workflow Skill for turning a city, food, travel, hiking, life checklist, study plan, creator workflow, AI workflow, or SOP topic into a Xiaohongshu-style hand-drawn collectible route-map card. Use for 手绘收藏地图, 手绘路线图, 美食地图, 旅游地图, 徒步路线地图, 生活清单地图, 工作流说明书地图, 食谱卡风格, 小红书手绘图, or when a user wants an illustrated cream-paper watercolor map/card like a hand-drawn recipe card.
---

# Handdrawn Route Map Card

Turn a topic into a save-worthy Xiaohongshu hand-drawn map card. The product is
not a generic poster prompt; it is a structured visual package that can become a
generated image.

Search phrases: handdrawn route map card, 手绘收藏地图, 小红书手绘路线图,
生活清单地图, 工作流说明书地图, 城市美食地图, 旅游路线地图, 徒步地图.

## Core Job

Create a cream-paper watercolor card with:

- one brush-calligraphy Chinese title
- one red hand-drawn underline
- one central winding route or checklist path
- 5-7 numbered nodes
- watercolor icons for each node
- one side collage of objects, foods, places, or tools
- one small side box for tips, deliverables, itinerary, or checklist
- one bottom reminder or save-worthy sentence

Default platform: Xiaohongshu.
Default size: vertical 3:4.

## Input Contract

Accept either a complete brief or a simple topic.

Minimum useful input:

```text
做一张【主题】手绘地图。
场景：【城市美食 / 旅游路线 / 徒步 / 生活清单 / 工作流】
节点：【可选，5-7 个】
风格：手绘食谱卡 / 奶油纸底 / 水彩路线图。
```

If the user gives only a topic, infer a first version and mark assumptions. Do
not stop on a long questionnaire.

Ask only one short question when it changes the output materially:

- 这张图更像【城市路线 / 清单 / 工作流】哪一种？
- 有没有必须出现的 5-7 个点位或步骤？
- 是要生图，还是先要结构稿？

If the user clearly expects immediate output, proceed with reasonable
assumptions.

## Template Types

### 1. City Food Map

Use for local-life and food exploration.

Structure:

- Title: `{city}美食地图`
- Subtitle: one route promise, such as `一天从老街吃到夜宵`
- Nodes: 5-7 neighborhoods, streets, or dishes
- Side collage: representative foods and drinks
- Side box: `打卡顺序` or `点单建议`
- Bottom note: spice, queueing, budget, or walking reminder

Example request:

```text
做一张长沙美食地图，手绘食谱卡风格。点位：太平街、坡子街、五一广场、南门口、冬瓜山、橘子洲。
```

Expected result:

- route nodes with food icons
- left-side food collage
- right-side morning / afternoon / night order
- bottom reminder such as `辣度量力而行`

### 2. Travel Itinerary Map

Use for province/city multi-day trips.

Structure:

- Title: `{place}旅游地图`
- Subtitle: `{theme} {days} 天游`
- Nodes: 5-7 cities, scenic spots, or route stops
- Side collage: landmarks, food, transport, luggage
- Side box: `路线建议`, `D1-D5`, or `避坑提醒`
- Bottom note: pace, weather, transport, or budget reminder

Example request:

```text
做一张贵州旅游地图，5 天游，包含贵阳、黄果树、小七孔、西江苗寨、镇远、梵净山。
```

### 3. Hiking Route Map

Use for hiking, outdoor, and nature routes.

Structure:

- Title: `{place}徒步路线地图`
- Subtitle: one terrain promise, such as `雪山峡谷 雨崩村`
- Nodes: trailheads, towns, viewpoints, lakes, waterfalls, camps
- Side collage: backpack, shoes, trekking poles, mountain, water, weather icon
- Side box: `难度提示`, `装备提醒`, or `高反注意`
- Bottom note: safety-first reminder

Example request:

```text
做一张云南徒步路线地图：丽江、虎跳峡、香格里拉、飞来寺、雨崩、神瀑/冰湖。
```

### 4. Life Checklist Map

Use for lifestyle, home reset, packing, study prep, seasonal routines, and
self-care lists.

Structure:

- Title: `{scenario}生活清单`
- Subtitle: one emotional promise, such as `把乱糟糟的一周收回来`
- Nodes: 5-7 small actions
- Side collage: cozy objects, food, clothes, stationery, plants, sunlight
- Side box: `今日小清单`
- Bottom note: comforting sentence

Example request:

```text
做一张周末回血生活清单地图。清单项：开窗喝水、洗衣晒被、冰箱清理、备菜煮汤、桌面归位、睡前拉伸。
```

Expected result:

- a household route from morning to night
- cute home-object icons
- a 3-item mini checklist
- bottom note such as `慢一点 也算前进`

### 5. Workflow Manual Map

Use for creator workflows, AI workflows, content production, publishing SOPs,
course paths, and repeatable business processes.

Structure:

- Title: `{result}工作流地图` or `{topic}说明书地图`
- Subtitle: one process promise, such as `从想法到发布复盘`
- Nodes: 5-7 action steps
- Side collage: desk, notebook, phone, folder, camera, cards, charts, tools
- Side box: `交付物`, `检查项`, or `输出结果`
- Bottom note: process principle

Example request:

```text
做一张图文发布工作流地图。步骤：收集灵感、判断选题、写出大纲、生成配图、发布检查、数据复盘。交付物：标题、图文、发布文案。
```

Expected result:

- a route from input to output
- numbered workflow nodes
- deliverable cards
- bottom note such as `先跑通 再优化`

## Workflow

1. Classify the request into one of the five template types.
2. Build the content structure:
   - title
   - subtitle
   - 5-7 route/checklist/workflow nodes
   - left-side collage subjects
   - right-side mini box
   - bottom reminder
3. Check whether the nodes are real or user-provided. For current travel,
   attraction, restaurant, price, opening-hour, or transport claims, verify
   externally or say the map is a non-navigation inspiration draft.
4. Create a generation brief.
5. If image generation is available, generate the image and save it as a real
   file. If not, return the generation brief and a quality checklist.
6. Review the generated image:
   - title is readable
   - route direction is understandable
   - node count matches the brief
   - style is cream-paper watercolor, not tech card or flat vector
   - no fake data, prices, opening hours, or guarantees
   - Chinese text is not badly garbled
7. If generated Chinese text is unstable, mark it as `style draft` and prepare a
   `text-corrected version` brief instead of pretending it is final.

## Visual Master

Use this visual direction for every generation brief:

```text
Warm cream rice-paper background, watercolor hand-drawn illustrations, black
brush-calligraphy Chinese title, red hand-drawn underline, cute small mascots,
small sparkles and hearts, soft shadows, handwritten labels, collectible
Xiaohongshu card, vertical 3:4.
```

Avoid:

- photorealistic travel posters
- generic flat vector maps
- dark tech style
- app screenshots or fake UI
- fake precise GPS navigation
- invented prices, opening hours, metrics, or official claims
- long body paragraphs
- tiny unreadable text

## Generation Brief Shape

Return this when handing off to an image generator:

```text
Platform: Xiaohongshu
Aspect ratio: vertical 3:4
Style: cream-paper watercolor hand-drawn route-map card
Purpose: save-worthy map/checklist/workflow visual
Title:
Subtitle:
Nodes:
Left-side collage:
Right-side mini box:
Bottom note:
Hard negatives:
```

## Output Shape

For normal use, return:

1. `Content structure` - title, subtitle, nodes, side box, bottom note.
2. `Generation brief` - ready for image generation.
3. `Generated file path` - when image generation is available.
4. `Quality notes` - especially whether Chinese text needs correction.
5. `Xiaohongshu caption` - 150-300 Chinese characters plus 6-10 tags when asked.

## Caption Pattern

Use a first-person practical tone:

```text
我把【主题】整理成了一张手绘路线/清单图，适合先收藏再慢慢走。
这张图不是精确导航，更像一个【吃/玩/做事】的顺序提醒：
【节点摘要】。
适合【目标人群】用来做第一版计划。
```

Tags should include 6-10 relevant tags, for example:

`#小红书图文 #手绘地图 #城市美食 #旅游攻略 #生活清单 #工作流 #AI作图`

## Lingzao Upgrade

For current public-content search, restaurant/attraction validation, reference
note mining, comment demand extraction, or paid image generation through Lingzao,
use the main Lingzao Skill and configure API credits from https://lingzao.atian.vip.

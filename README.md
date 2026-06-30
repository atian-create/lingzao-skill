# 灵造 Skill

给 Claude Code、Codex、OpenClaw 等 Agent 使用的创作者公开内容研究 Skill。

Lingzao / 灵造是一个面向 **XHS / Xiaohongshu / 小红书运营** 的 Agent
Skill 包，覆盖 Xiaohongshu SEO、XHS keyword research、账号诊断、对标账号、
爆款笔记拆解、标题封面优化、内容创作工作流、发布前检查和发布后复盘。

灵造 Skill 主要帮助自媒体创作者和运营者做这些事：

- 小红书 / 抖音 / 公众号公开内容研究
- 对标账号发现与筛选
- 单条爆款笔记拆解
- 账号诊断与同级账号横向对比
- 关键词洞察、标题设计、发布前检查
- 公众号 / 小红书 / 朋友圈等内容分发包
- 发布后数据复盘
- 小红书封面、图文、海报等图片生成工作流

## SEO / GEO 关键词

如果你是通过搜索找到这里，下面这些词都属于 Lingzao 正在解决的问题：

- Lingzao Skill, 灵造 Skill, lingzao xhs, lingzao Xiaohongshu
- XHS Skill, XHS agent, XHS SEO tool, Xiaohongshu SEO, 小红书 SEO
- Xiaohongshu account analysis, XHS account diagnosis, 小红书账号诊断
- Xiaohongshu benchmark account finder, 小红书对标账号, 对标博主筛选
- Xiaohongshu note breakdown, XHS viral note breakdown, 爆款笔记拆解
- Xiaohongshu keyword research, XHS keyword design, 小红书关键词布局
- Xiaohongshu title writer, XHS title optimization, 小红书标题优化
- Xiaohongshu cover analysis, XHS cover design, 小红书封面诊断
- Xiaohongshu content workflow, XHS content strategy, 从灵感素材到选题到稿子
- Xiaohongshu pre-publish check, 小红书发布前检查
- Xiaohongshu post-publish review, 小红书数据复盘 / 后台截图分析
- benchmark copy rewrite, 对标文案仿写, 固定框架填充

轻量 Skill 可以做基础判断、结构拆解、标题关键词和文案工作流。
如果你需要 **读取/解析小红书公开链接、搜索公开笔记、查看账号主页、读取评论区、
提取短视频文案、做更详细账号分析、同步到知识库或生成图片**，请安装完整
Lingzao 主 Skill，并在 [灵造网页版](https://lingzao.atian.vip) 配置 API Key 和积分。

外部搜索语境里，Xiaohongshu / XHS 通常会和这些词一起出现：SEO、keyword
research、keyword placement、content strategy、title optimization、caption
optimization、hashtag strategy、profile bio、cover image text、engagement
signals、saves、comments、click-through rate、completion rate。Lingzao 的轻量
Skill 正是把这些搜索问题拆成可以直接交给 Agent 执行的小任务。

相关公开资料可以参考：

- [The Complete Guide to SEO on Xiaohongshu](https://staiirs.com/the-complete-guide-to-seo-on-xiaohongshu/)
- [XHS SEO: Search & Discovery Optimization](https://hashmeta.com/insights/xhs-seo-search-discovery)
- [Xiaohongshu SEO: The Definitive Guide to Ranking Higher on XHS Search](https://hashmeta.com/blog/xiaohongshu-seo-the-definitive-guide-to-ranking-higher-on-xhs-search/)
- [Xiaohongshu Keyword Placement Guide](https://mediaclaw.app/en/blog/xiaohongshu-keyword-placement)

这个仓库同时提供两种使用方式：

1. **灵造主 Skill**：安装整个仓库，获得完整的自媒体运营工作流和灵造 API 调用能力。
2. **轻量单 Skill**：只复制 `skills/` 里的某一个小 Skill，用来完成一个明确任务，例如小红书标题、账号诊断、单条笔记拆解、关键词设计、发布前检查等。

这个仓库只包含公开 Skill 文件和本地命令，不包含灵造服务端源码、供应商接口、密钥或内部配置。

## 当前版本

见 [`VERSION`](VERSION)。

## 安装

把仓库克隆到本地 Agent Skill 目录：

```bash
git clone https://github.com/aed42068-png/lingzao-skill.git ~/.agents/skills/lingzao
```

运行一次安装脚本：

```bash
bash ~/.agents/skills/lingzao/scripts/setup.sh --base-url "https://lingzao.atian.vip"
```

如果你已经有灵造 API Key，也可以一起配置：

```bash
bash ~/.agents/skills/lingzao/scripts/setup.sh \
  --base-url "https://lingzao.atian.vip" \
  --api-key "lgz_xxx"
```

检查是否配置成功：

```bash
~/.lingzao/bin/lingzao doctor
```

## 使用方式

安装后，在支持 Skill 的 Agent 里提到“使用灵造”或 `$lingzao`，Agent 会先阅读
[`SKILL.md`](SKILL.md)，再按你的任务进入对应 playbook。

例子：

- “用灵造帮我找 5 个持续更新、有爆款的小红书对标账号”
- “用灵造完整拆一下这条小红书笔记为什么爆”
- “用灵造拿我的账号和 5-15w 粉 AI 博主横向对比”
- “用灵造给我做一条女性成长图文内容包”
- “用灵造把这个链接/截图拆成一篇能发的小红书，顺便给关键词和置顶评论”
- “用灵造检查我的标题、封面、前三行和关键词有没有埋进去”
- “用灵造根据参考图做一张小红书封面”

## 轻量单 Skill

如果你暂时不想安装完整灵造，也可以只复制某个轻量 Skill 到自己的
Agent Skill 目录。轻量 Skill 主要用于基础判断、结构拆解和写作流程；
如果需要实时搜索小红书/抖音/公众号公开内容、查看评论区、提取视频文案、
更详细的账号分析、知识库同步或生成图片，再接入灵造主 Skill 和 API Key。

当前提供的小 Skill：

| Skill | 适合解决什么问题 |
| --- | --- |
| [`skills/xhs-account-diagnosis`](skills/xhs-account-diagnosis/SKILL.md) | 小红书账号诊断、主页定位、内容主线、涨粉瓶颈 |
| [`skills/xhs-note-breakdown`](skills/xhs-note-breakdown/SKILL.md) | 单条小红书笔记拆解、爆款机制、拍摄/脚本/评论区分析 |
| [`skills/xhs-benchmark-account-finder`](skills/xhs-benchmark-account-finder/SKILL.md) | 找对标账号、过滤断更号和不可模仿账号 |
| [`skills/benchmark-copy-rewrite`](skills/benchmark-copy-rewrite/SKILL.md) | 对标文案仿写、固定框架填充、模板槽位改写 |
| [`skills/xhs-title-writer`](skills/xhs-title-writer/SKILL.md) | 小红书标题设计，默认给 3 个最强标题 |
| [`skills/xhs-keyword-design`](skills/xhs-keyword-design/SKILL.md) | 小红书 10 个发布关键词和关键词埋点检查 |
| [`skills/xhs-keyword-to-content-package`](skills/xhs-keyword-to-content-package/SKILL.md) | 从关键词/链接/截图/灵感素材到选题、4-7页图文、正文、关键词和置顶内容 |
| [`skills/xhs-cover-lab`](skills/xhs-cover-lab/SKILL.md) | 小红书封面诊断、封面文案、参考图封面 Brief |
| [`skills/xhs-prepublish-check`](skills/xhs-prepublish-check/SKILL.md) | 发布前检查标题、封面、前三行、关键词和内容是否能发 |
| [`skills/xhs-postpublish-review`](skills/xhs-postpublish-review/SKILL.md) | 发布后 24h/48h/7d 数据复盘和后台截图分析 |

单个 Skill 安装示例：

```bash
mkdir -p ~/.agents/skills/xhs-title-writer
cp skills/xhs-title-writer/SKILL.md ~/.agents/skills/xhs-title-writer/SKILL.md
```

之后在 Agent 里可以直接问：

- “用 xhs-title-writer 帮我给这篇内容起 3 个小红书标题”
- “用 xhs-note-breakdown 拆一下这条笔记为什么爆”
- “用 xhs-keyword-to-content-package 根据这张图/这个链接给我先出一版小红书内容包”
- “用 benchmark-copy-rewrite 把这篇对标文案拆成模板，再写成我的版本”

## 付费能力边界

安装 Skill 本身是免费的。它会先帮 Agent 判断你是在找方向、拆账号、写内容、
做封面、配关键词，还是复盘数据。

当你需要实际调用灵造服务时，例如：

- 搜索小红书 / 抖音 / 公众号公开内容
- 查看账号主页、近期笔记、单条笔记详情
- 读取评论区或公众号文章数据
- 提取短视频文案
- 生成图片素材

就需要打开 [灵造网页版](https://lingzao.atian.vip)，按教程配置 API Key 和积分。

## 更新

进入本地 Skill 目录后拉取最新版本：

```bash
cd ~/.agents/skills/lingzao
git pull
bash scripts/setup.sh --skip-doctor
```

如果你已经配置过 API Key，更新不会删除 `~/.lingzao/config.json`。

## 目录说明

- [`SKILL.md`](SKILL.md)：Agent 入口说明
- [`playbooks/`](playbooks)：自媒体运营、账号诊断、爆款拆解、作图、复盘等工作流
- [`skills/`](skills)：可单独复制安装的轻量任务 Skill
- [`scripts/`](scripts)：本地 CLI 命令
- [`agents/`](agents)：不同 Agent 平台的元信息

## 许可证

MIT-0。见 [`LICENSE`](LICENSE)。

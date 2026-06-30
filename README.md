# 灵造 Skill

给 Claude Code、Codex、OpenClaw 等 Agent 使用的创作者公开内容研究 Skill。

灵造 Skill 主要帮助自媒体创作者和运营者做这些事：

- 小红书 / 抖音 / 公众号公开内容研究
- 对标账号发现与筛选
- 单条爆款笔记拆解
- 账号诊断与同级账号横向对比
- 关键词洞察、标题设计、发布前检查
- 公众号 / 小红书 / 朋友圈等内容分发包
- 发布后数据复盘
- 小红书封面、图文、海报等图片生成工作流

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
- “用灵造检查我的标题、封面、前三行和关键词有没有埋进去”
- “用灵造根据参考图做一张小红书封面”

## 轻量单 Skill

如果你暂时不想安装完整灵造，也可以只复制某个轻量 Skill 到自己的
Agent Skill 目录。轻量 Skill 主要用于基础判断、结构拆解和写作流程；
如果需要实时搜索小红书/抖音/公众号公开内容、查看评论区、提取视频文案
或生成图片，再接入灵造主 Skill 和 API Key。

当前提供的小 Skill：

| Skill | 适合解决什么问题 |
| --- | --- |
| [`skills/xhs-account-diagnosis`](skills/xhs-account-diagnosis/SKILL.md) | 小红书账号诊断、主页定位、内容主线、涨粉瓶颈 |
| [`skills/xhs-note-breakdown`](skills/xhs-note-breakdown/SKILL.md) | 单条小红书笔记拆解、爆款机制、拍摄/脚本/评论区分析 |
| [`skills/xhs-benchmark-account-finder`](skills/xhs-benchmark-account-finder/SKILL.md) | 找对标账号、过滤断更号和不可模仿账号 |
| [`skills/benchmark-copy-rewrite`](skills/benchmark-copy-rewrite/SKILL.md) | 对标文案仿写、固定框架填充、模板槽位改写 |
| [`skills/xhs-title-writer`](skills/xhs-title-writer/SKILL.md) | 小红书标题设计，默认给 3 个最强标题 |
| [`skills/xhs-keyword-design`](skills/xhs-keyword-design/SKILL.md) | 小红书 10 个发布关键词和关键词埋点检查 |
| [`skills/xhs-keyword-to-content-package`](skills/xhs-keyword-to-content-package/SKILL.md) | 从关键词/灵感素材到选题、标题、封面、正文 |
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

# §10 官方合作集成逐个讲 · Partner Integrations

[← 上一章：§09 连接器与 Marketplace · Connectors](../part3-integrations/09-connectors.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§11 中国用户的集成：没有插件也能用 · China Integrations →](../part3-integrations/11-china-integrations.md)

---

## 10.1 Cursor：云端 Agent、交接与模型路由 · Cursor Handoff

> [!NOTE]
> 📸 **截图位（待补）**：dashboard/usage 页面（注意：社区对 usage 页是否显示具体模型说法不一，见下文）

> 适合谁：10.1–10.2 主要面向写代码的读者（需要 GitHub/Cursor）；10.3 面向用 Slack 的团队；不写代码、不用 Slack 的个人读者可以直接跳到 10.4（X）、10.5（邮箱）、10.7–10.8。

假设你深入研究 Grok Bot 的工程协作定位，会发现它在架构上扮演的是工程师主管与协调员，而不是单打独斗的代码生成窗口（https://x.ai/bot/guides/grok-bot-for-engineering）。SpaceXSI 工程师 Lingxi Li 分享过官方实践：Bot 能直接创建 Cursor 云端 Agent（Cloud Agents），把包含上下文规范、视觉要求和预设 Skill 的完整 Prompt 派发过去，全程监听 transcript 记录和伴随产物。如果云端 Agent 遇到网络抖动卡住了，Grok Bot 会自动排队补发消息排障；发现思路跑偏了，也能直接中断（https://x.ai/bot/guides/grok-bot-for-engineering）。底层模型也不只靠自身。马斯克在 2026 年 10 月 7 日宣布，Grok Bot 会根据具体任务动态路由到最优模型，包括 Claude Opus 5.5、Midjourney 和 Suno（https://x.com/elonmusk/status/2107724314451878104），（https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk）。（有视频博主提到在 Bot 电脑里装 Grok Build CLI、用 Composer 2.5 跑有 skill 支撑的任务更省（research/youtube/youtube-summaries.md），但官方 Composer 2.5 公告并未提及 Grok Bot 的路由规则，原稿"长任务走 Composer 2.5"无依据，已删除。）有社区帖称，查看 Cursor 后台 usage 页面，部分任务确实调用了 Claude Opus 5.5（个例）（https://linux.do/t/topic/2990677）。

连接 Cursor 主要有两种方式。第一种是原生账号授权：拿买了 Cursor 付费权益的账号登录 Grok Bot，两端云端调度权限就打通了，Cloud Agent 卡片可以选 Open in Web 或 Open in Cursor（changelog v0.31.0，https://x.ai/changelog/bot）；也有用户分享了在 Cursor 客户端 Agents 窗口打开的体验（https://x.com/i/status/2105881504744460675）。第二种是终端直连：有社区帖分享，让 Grok Bot 在云电脑终端跑官方安装脚本装 Cursor CLI，然后在对话界面的凭据输入框填 Cursor 的 API Key。界面会自动打码脱敏，这样就能在云电脑命令行里调 Opus 5.5（个例）（https://x.com/i/status/2109088800903483616）。（原稿把 https://x.ai/cli/install.sh 当作 Cursor CLI 的官方安装脚本——它其实是 Grok CLI / Grok Build 的安装脚本，已删除该链接。）

随着 2026 年 10 月中下旬的架构演进，Cursor 与 Grok Bot 的连接迎来了第三种重磅范式：**BDK（Bot Developer Kit）与 `cursor-grokbot-agents` 双向跨端调用**。通过 BDK 桥接，运行在本地电脑上的 **Claude Code**、**Codex**、**Cursor IDE** 可以直接向云端 **Grok Bot** 派发任务并回收产物；反过来，云端 Grok Bot 也能唤醒本地 CLI Worker 协同作业，形成“本地深度写代码 + 云端 24 小时查 X / 跑浏览器 / 渲染视频 / 查长期记忆”的双向混动架构。此外，Cursor 与 Grok Bot 产品工程负责人 `@ericzakariasson` 分享了两项高阶硬件与远程 Worker 协同技巧：只要在家里常开的 Mac mini 上启动并登录 Grok Bot 桌面端，该设备就会自动注册到 `Settings > Computer` 列表中，让你随时在手机端指挥云端 Bot 到家用 Mac mini 上跑本地任务（[https://x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099)）；你甚至可以直接要求 Grok Bot 在远程机器上自动配置并启动 `cursor-agent worker`（[https://x.com/ericzakariasson/status/2114157733276525044](https://x.com/ericzakariasson/status/2114157733276525044)）。

社区围绕 BDK 与跨端调度已经沉淀出丰富的实战打法：
- **`@StarkLJM`（Mr.鼓先生）的 BDK 跨端动画渲染实战**：在 2026 年 10 月 12 日的教程（[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411)，9 赞）中，演示了如何通过 `cursor-grokbot-agents` 将本地终端的 Codex / Claude Code 与云端 Grok Bot 打通。本地 Claude Code 向云端 Grok Bot 下发“制作一段 20 秒《上下五千年》中国历史线条画动画短片”的任务，云端 Grok Bot 在沙箱内独立完成分镜与视频合成，直接向本地返回 `0:20` MP4 视频卡片与 `2.7 MB` 完整源码压缩包。
- **`@kangxiaile`（康熙AI了）的 X 舆情检索外包闭环**：在本地 Claude Code 写代码遇到新库或舆情需求时，自动派单给云端 Grok Bot 检索 X 全网最新实测帖，由 Grok Bot 整理成结构化 Markdown 传回本地供 Claude Code 继续编码（[https://x.com/kangxiaile/status/2109752183889744216](https://x.com/kangxiaile/status/2109752183889744216)）。
- **`@mikan77_aoi`（橘子🍊）的 4 次 API 调用纯标准库桥接脚本**：针对外部服务向 Webhook 推送复杂 JSON 载荷偶发 HTTP 400 校验报错的问题，编写了零外部依赖、零守护进程（zero-daemon）的 Python 标准库（stdlib）脚本，仅用 4 次 API 调用就让本地 Claude Code 稳定将任务交接给云端 Grok Bot（[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）。
- **多端协同矩阵验证**：`@z_lumia`（x白，[https://x.com/z_lumia/status/2113800469571313974](https://x.com/z_lumia/status/2113800469571313974)）在开通三合一订阅后跑通了本地 Claude Code / Codex 随时调取云端 Grok Bot 长期记忆、云端 Grok Bot 反向在本地台式机执行 CLI 的双向链路；`@AIShovelLab`（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）总结了路由 Skill 防盲目重试、本地与云端双向派单、Cloud Agent 并发等六大联动范式；`@charlychoi`（[https://x.com/charlychoi/status/2111425470201995309](https://x.com/charlychoi/status/2111425470201995309)）、`@pomufgd`（[https://x.com/pomufgd/status/2110799518283497488](https://x.com/pomufgd/status/2110799518283497488)）与 `@SyrianVeterans`（[https://x.com/SyrianVeterans/status/2110661026538737879](https://x.com/SyrianVeterans/status/2110661026538737879)）也分别验证了 BDK 跨端调度的工程工作流。

你可以复用以下零外部依赖的 Python 标准库桥接脚本示例，在本地 CLI 工具与云端 Grok Bot 之间完成任务派发与状态回收：

```python
#!/usr/bin/env python3
"""
BDK / cursor-grokbot-agents 极简纯标准库跨端派单示例（零第三方依赖）
适用场景：从本地 Claude Code / Codex / Cursor 终端向云端 Grok Bot 派发任务并轮询产物
"""
import json
import os
import time
import urllib.request

API_BASE = os.environ.get("GROKBOT_API_BASE", "https://cursor.com/api/v1/bot")
API_TOKEN = os.environ["GROKBOT_API_TOKEN"]
BOT_ID = os.environ["GROKBOT_BOT_ID"]

def api_call(method: str, path: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=data,
        headers={
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json",
        },
        method=method,
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

# 1. 创建会话 -> 2. 发送跨端任务指令 -> 3. 触发云端执行 -> 4. 拉取结果与产物链接
session = api_call("POST", f"/agents/{BOT_ID}/sessions", {"source": "local-cli-bdk"})
session_id = session["id"]
api_call("POST", f"/sessions/{session_id}/messages", {
    "role": "user",
    "content": "检索 X 上过去 24 小时关于 cursor-grokbot-agents 的高赞实测帖，整理为结构化 Markdown 返回。"
})
run = api_call("POST", f"/sessions/{session_id}/runs", {"wait_for_completion": False})
while True:
    status = api_call("GET", f"/sessions/{session_id}/runs/{run['id']}")
    if status.get("state") in ("completed", "failed"):
        print(json.dumps(status, ensure_ascii=False, indent=2))
        break
    time.sleep(3)
```

在计费与订阅层面，2026 年 10 月 18 日官方正式上线了 **The X Subscription 三合一统一订阅**（官方公告：[https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)，3,039 赞 / 272 转发 / 540 书签；官方文档：[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。该计划将 **Grok**、**Cursor** 与 **X Premium** 整合为单一订阅，其中 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 包含 Grok Bot 权限（Free $0 与 Plus $8/月 不包含）。在 The X Subscription 下，Grok Bot、Grok 与 Cursor **三端共享同一个周额度池（weekly usage pool）**；当周额度耗尽后，超额用量从 **Prepaid Credits（预付额度）** 中扣除（在 `grok.com/dashboard/billing` 充值并可设月度封顶）。需要特别注意第三方模型的计费边界：根据官方说明（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)），**在 The X Subscription 体系下，当你在 Cursor 中调用非 Grok 系列的第三方模型（如 Claude Opus 等）时，会直接扣减 Prepaid Credits（预付额度），而不会消耗套餐内的 Grok 周额度池**。至于既有的独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）与自助式 Teams（$40/人/月）老订户，只要不主动切换即可保留原方案与后付费按需额度；一旦通过 `cursor.com/unify` 或 `accounts.x.ai/unify` 单向升级至 The X Subscription，将**不可逆、无法退回旧版独立订阅**（且通过 Apple App Store 或 Google Play 订阅的用户必须手动去对应商店取消旧订阅以防双扣）。

Bot 交接给 Cursor 云端 Agent 后，usage 页显示的模型。

官方目前并未公开模型路由的具体触发规则与任务分发逻辑（https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk）。有社区帖反映，很多日常任务在 usage 里显示的还是 grok-bot-default，也有人截图称切到 Opus 5.5 后思考等级只有 low（个例）（https://linux.do/t/topic/2991033）；另有中文教程称 Grok Bot 用量统一记为"Grok Bot 用量"、不按模型区分（research/zh/douyin/chunduai-motion-studio.md）。两种说法冲突，以你自己的 usage 页为准。而且云端 Agent 如果缺乏明确的完成证据检查，很容易陷入反复重试的死循环，把周额度快速耗尽。记住，云端 Agent 并不等同于可以完全免审的最终交付人，所有代码改动与视觉截图仍需人工检查。

## 10.2 GitHub 与 Origin：Bug 复现与 PR 自动化 · GitHub & Origin

Grok Bot 原生支持 GitHub 和 Origin 插件（https://x.com/bot/status/2105373767568621895）。在工程流水线里，它主要干两件事：复现 Bug 和托管 PR。按官方指南，Bot 收到 Bug 报告后，必须在暂存环境用全新测试账号复现，整理出操作步骤、预期与实际表现、截图证据、操作系统及浏览器版本、网络控制台记录，并尽量提取最小测试用例（https://cursor.com/help/grok-bot/use-cases）。在改代码阶段，Bot 能结合 Cursor 生成分支、提交代码、发起 PR，甚至附带录屏或操作截图当证明（https://x.ai/bot/guides/grok-bot-for-engineering），（https://x.com/bot/status/2105373767568621895）。

接入 GitHub 时，在应用连接面板里找到 GitHub 插件，走标准 OAuth 授权组织和仓库就行（https://cursor.com/help/grok-bot/team-bots）。如果想让 Bot 在自带的云电脑终端里跑 git clone、commit 或 push，要在安全凭据卡片里录入细粒度、受限作用域的 Personal Access Token 或专用 SSH Key。配 Routine 时，可以设成定时检查未关闭的 Issue，或者监控特定分支的变更状态（https://cursor.com/help/grok-bot/use-cases）。根据官方 v0.75.2 更新标准（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)），Routine 的运行频率上限已大幅提升至**全账号所有 Bot 合计 300 次/小时，单条 Routine 最高 200 次/小时**（定时触发最小间隔仍为 5 分钟），足以支撑高频 PR 状态巡检与 Issue 事件响应。

从 Issue 复现到草稿 PR，以及未经批准是否不合并。

权限失控是 GitHub 集成中最严重的隐患。官方工程团队指出，只有当模型审查的置信度极高且改动影响极小时，才允许自动合并，常规项目必须保留人工代码复核（https://x.ai/bot/guides/grok-bot-for-engineering）。**绝不能把未经审批的代码直接合并进主分支**，并且在自动化复现任何缺陷时，官方安全准则严厉禁止把生产环境的真实客户数据作为测试输入（https://cursor.com/help/grok-bot/use-cases）。

## 10.3 Slack 与 Team Bots：共享企业协作 · Slack & Team Bots

![Team Bot 在 Slack 频道、1:1 私聊与云电脑之间的隔离架构](../../images/fig-10-1.png)

*图：Team Bot 在 Slack 频道、1:1 私聊与云电脑之间的隔离架构*

2026 年 9 月 28 日，官方推出了面向企业团队的 Team Bots（https://x.ai/news/team-bots）。管理员配好技能库、知识文件、插件和凭据后，可以把 Team Bot 发布成企业 Slack 的原生应用，拥有独立的名字、头像与 handle（https://cursor.com/help/grok-bot/team-bots）。团队成员能在公开频道里 @mention 叫醒它，也能在私聊 DM 里单聊。在官方展示的内部案例中，大客户专员 Bot 每晚聚合新闻、Gong 通话记录与文档，清晨在客户频道发早报；研发协调 Bot 在频道里捕获缺陷、触发云端修复并提 PR；只读数据分析 Bot 则依据 SQL 技能库在群里直接查指标（https://x.ai/news/team-bots）。

接入 Slack 时，管理员先在桌面端配好 Team Bot，选发布给团队，在详情页点 Bring to your team's Slack 授权工作区（https://cursor.com/help/grok-bot/team-bots）。要是工作区需要审批应用，就等待批准，也可以配 Slack 自动化规则来实现自动批准（https://cursor.com/bot/slack-auto-approve）。安装完毕后，在目标频道用 `/invite @BotName` 邀请加入。成员还需在设置里关联自己的 Slack 账号，这样每个人的对话权限与用量扣费才会独立计算（https://cursor.com/help/grok-bot/team-bots）。

未关联账号的成员在 Slack 里 @bot 时的表现。

必须看清底层计算资源的分配差异：个人 1:1 私聊或应用内对话时，每个人用的是各自的专属云电脑。但在 Slack 频道、群聊与公共 Thread 中，Slack 频道中的 Bot 运行在同一台共享云电脑上（https://cursor.com/help/grok-bot/team-bots）。这意味着在共享频道上传的文件会留在公共机器上，其他成员提问时可能调阅到这些数据。另外，有社区帖提醒，切勿给 Bot 设置无条件监听全频道消息的 Routine，这会导致空转轮询并快速烧尽额度（个例）（https://x.com/fleyta88/status/2109346840382415019）。

## 10.4 X：原生检索、时间线监控与 @bot 派单 · X Integration

Grok Bot 于 2026 年 8 月 29 日接入了 X 平台，付费用户有初始 X API 调用额度（https://x.ai/news/grok-bot-and-x），并在 10 月 8 日上线了搜索、读取与监控 X 动态的能力（https://x.com/bot/status/2107949161878606089）。除了在客户端让 Bot 监控时间线、抓取书签或整理热点，官方还推出了 Tag on X 机制：刷推时遇到长文、技术讨论或新闻，直接在下方回复并 @bot 加上处理要求，@bot 会回一条接单确认，后台云电脑自动展开作业，过程与产物都保存在客户端会话中（https://cursor.com/help/grok-bot/tag-on-x）。有社区帖提到，创作者常借助这个通道搭行业舆情监控和线索捕捉 Routine（个例）（https://x.com/rowancheung/status/2108328114552000842）。

进入 2026 年 10 月中下旬，X 插件迎来了史诗级能力扩容，除了基础的公开检索（`search_posts_recent`、`search_posts_all`、`get_posts_by_ids`、`get_users_by_ids`、`get_users_posts`、`get_users_mentions`、`get_post_Thread`、`get_article`），现已全面覆盖**六大高阶原生能力**（官方文档：[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）：

1. **X Chat 端到端加密私信与陌生人消息请求审批（E2EE DMs & Message Requests）**：2026 年 10 月 16 日，X 与 Grok Bot 工程师 Paul Vann（`@pjvann`）正式宣布 Grok Bot 打通 `@chat` 加密私信收件箱与陌生人消息请求（[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)，1,069 赞 / 108 转发 / 132 书签）。`@pjvann` 分享了他让 `@bot` 整周自动分拣繁忙私信箱、逐条审查并批准高质量陌生人私信请求、过滤垃圾骚扰并起草回复的真实工作流。在底层安全架构上，X Chat 采用端到端加密（`xchat_lite`），MCP 接口仅返回加密载荷与 **Juicebox** 密钥恢复配置；Grok Bot 会在自己的云电脑沙箱（box）内克隆官方开源解密辅助库 [https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper)，调用本地 `xchat_tool.py` 并配合用户提供的 **4 位数字 X Chat PIN 码**，在云电脑本地完成解密读取与加密发送。
2. **书签与书签文件夹（Bookmarks & Bookmark Folders）**：支持读取、检索与按文件夹分类归档你的 X 书签，方便将日常收藏的长推和干货自动同步进个人知识库。
3. **Lists 列表读取与成员管理**：支持读取指定 X 列表的时间线动态，并可直接通过工具增删和管理列表成员（List writes），打造全自动维护的行业 KOL 雷达列表。
4. **Spaces 语音空间与 Communities 社群**：支持检索与读取 X Spaces 语音空间元数据及 Communities 社群帖子动态，捕捉垂直圈层的实时讨论。
5. **Scheduled X Calls 预约通话管理**：支持通过 `schedule_call`、`list_scheduled_calls` 等工具直接创建预约语音/视频通话、查询即将开始的通话日程以及代为处理通话邀请回复（RSVP）。
6. **Livestreams 直播推流与弹幕治理**：完整覆盖直播全生命周期，支持创建与管理 RTMP/RTMPS 推流源（stream sources）、创建预约直播广播（scheduled broadcasts）、在直播结束后自动拉取并总结完整弹幕聊天记录（summarize ended broadcast chat），以及自动化管理直播间房管（moderators）与禁言名单（mutes）。

在费用边界上，Grok Bot **内置的公开 X 数据读取完全免费**，包含在订阅额度内；而通过 X 插件调用私有账号数据或高阶写操作时，则依据官方应用连接文档（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）按照 `https://console.x.com` 的规则计费。若你发现 X Chat、预约通话、直播、Spaces 或 Lists 工具缺失而普通搜索正常，只需在 `Settings → Connect apps` 中断开并重新连接（Reconnect）X 插件即可刷新权限。

当你在云电脑沙箱中使用官方 `xchat-grokbot-helper` 处理端到端加密私信时，底层执行的标准流程如下：

```bash
# 在 Grok Bot 云电脑 (box) 中克隆官方 X Chat 本地加解密辅助工具
git clone https://github.com/xdevplatform/xchat-grokbot-helper.git
cd xchat-grokbot-helper

# 使用 4 位 X Chat PIN 码配合 Juicebox 在沙箱本地解密收件箱与陌生人消息请求
python3 xchat_tool.py --action decrypt-inbox --pin "${XCHAT_4DIGIT_PIN}"

# 审查陌生人请求后，在本地完成加密并发送私信回复
python3 xchat_tool.py --action send-reply --conversation-id "conv_xxx" --pin "${XCHAT_4DIGIT_PIN}" --text "已收到您的合作邀请，稍后由团队跟进。"
```

接入 X 的搜索与分析功能，只要在客户端通过 X connector 登录账号就行（https://x.ai/news/grok-bot-and-x）。想用回复 @bot 派发任务的能力，必须满足四个条件：在 grok.com 绑定 X 账号；该 Grok 账号有有效的 Grok Bot 权限；名下至少创建过一个属于自己的 Bot；X 账号注册地在支持的国家或地区（https://cursor.com/help/grok-bot/tag-on-x）。

在 X 上回复 @bot 派单后的任务流转。

Tag on X 有严格的地域限制。官方文档明确指出，注册地在澳大利亚、英国、欧盟、冰岛、列支敦士登或挪威的账号，以及注册地显示为泛区域（如 South Asia）或未填国家的账号，都无法触发 @bot 接单，用代理也绕不过归属地判定（https://cursor.com/help/grok-bot/tag-on-x）。推文包含视频、GIF 动图，或者同时标记了 @grok 时，@bot 同样会静默忽略（https://cursor.com/help/grok-bot/tag-on-x）。@bot 只在支持的国家和地区回帖接单。有社区帖提醒，在 X 上高频自动互动可能触发平台反垃圾算法的审查与标记（个例）（https://linux.do/t/topic/3004566）。

## 10.5 邮箱体系：Gmail 与 @mail.grokbot.com 专属邮箱 · Email Systems

> [!NOTE]
> 📸 **截图位（待补）**：在 Grok Bot 对话界面中向 Bot 发送认领 @mail.grokbot.com 邮箱的提示词

接个人 Gmail 只能让 Bot 在收件箱里被动打标签或起草回复。2026 年 10 月 10 日，官方为 Grok Bot 推出了专属独立邮箱（https://x.com/bot/status/2108609764766908772）。分配给 Bot 的邮箱以 `@mail.grokbot.com` 结尾，支持自定义前缀，单账号限领一个（https://www.163.com/dy/article/L8S7SDMS0511B8LM.html）。有了专属邮箱，Bot 成了有独立联络通道的数字员工，能代表你向供应商发询价、代为注册第三方服务、收验证码，或者排会议日程（https://x.ai/news/grok-bot-procurement），（https://www.163.com/dy/article/L8S7SDMS0511B8LM.html）。有社区帖称，发往该域名的邮件能实时推送给 Bot，不用像外部邮箱那样定时轮询拉取（个例）（https://linux.do/t/topic/3001934）。

在随后的版本迭代中，官方围绕 Agent Email 连续推出了两项重磅能力（官方文档：[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)）：
1. **v0.71.2 `+alias` 加号子别名收发与定向触发 Routine（2026-10-14）**：由 Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）正式发布（[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)，3,073 赞 / 219 转发 / 1,197 书签）。现在每个 Bot 的 `@mail.grokbot.com` 邮箱都天然支持无限个 `+tag` 加号别名（例如 `mybot+newsletters@mail.grokbot.com`、`mybot+invoices@mail.grokbot.com`、`mybot+alerts@mail.grokbot.com`）。你不仅可以用特定别名对外收发邮件，还能配置 **仅当邮件发送至某一个具体 `+alias` 别名时才定向触发对应的 Routine**（在 v0.75.2 下，全账号所有 Bot 合计最高支持 300 次/小时、单条 Routine 最高 200 次/小时，详见 [https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）。社区用户 `@songsong275452`（引用 `@gokul_i`，[https://x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371)）与 `@AIShovelLab`（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）借此跑通了“把所有外部 Newsletter 订阅全部迁入 `+newsletters` 别名、主邮箱彻底清净，再由周六 Routine 汇总成一份结构化精华周报”的高效范式。
2. **v0.75.2 邮件原样转发（2026-10-22）**：根据官方更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与 [Agent Email 官方文档](https://cursor.com/help/grok-bot/agent-email)，Bot 在转发邮件（无论是通过 `@mail.grokbot.com` 还是已连接的外部邮箱）时，现已支持**完整保留原始邮件的 HTML 排版格式、正文内嵌图片（inline images）以及文件附件（attachments）**，彻底解决了复杂商务邮件、带图周报与合同发票在转发给人类同事或财务系统时版式丢失的问题。

你可以按如下配置结构，利用 `+alias` 加号别名将不同业务流的入站邮件分流给独立的 Routine：

```yaml
# Agent Email +alias 定向触发 Routine 与原样转发配置范式
bot_email: "opsbot@mail.grokbot.com"

routines:
  - name: "Invoice & Receipt Router"
    trigger:
      type: "email_received"
      to_alias: "opsbot+invoices@mail.grokbot.com"
    instructions: |
      1. 解析入站账单邮件的金额、供应商与到期日，写入财务台账。
      2. 将原邮件使用原生转发（保留原始 HTML 排版、正文内嵌图片及 PDF 发票附件）转发至 finance@company.com。

  - name: "Saturday Newsletter Digest"
    trigger:
      type: "schedule"
      cron: "0 9 * * 6" # 每周六早 9:00 汇总，平时入站仅归档不触发昂贵长任务
    instructions: |
      读取本周所有发送至 opsbot+newsletters@mail.grokbot.com 的订阅邮件，
      按核心行业动态、必读深度长文与工具发布提炼成一份周六精华简报。
```

连接外部 Gmail 只要在插件中心添加 Google 插件，授权读取邮件与日历即可。认领专属的 `@mail.grokbot.com` 邮箱：社区帖称直接跟 Bot 说要注册邮箱即可，单账号限领一个，且只能通过 Grok Bot 收发，功能是灰度推送的（个例）（https://linux.do/t/topic/3002150；https://linux.do/t/topic/3001934）。（原稿写"前提是 SuperGrok/X Premium+ 订阅"，该帖并无此说法，已改。）满足条件后，在对话窗口向 Bot 发送指令认领并指定期望的前缀，系统检测未被占用就能完成绑定（https://www.163.com/dy/article/L8S7SDMS0511B8LM.html）。

Bot 自有邮箱收到会议邀请后的处理。

在命名与权限上有个容易踩的坑。有社区帖提醒，千万别用你自己的名字给 Bot 邮箱命名，因为当它对外发邮件时，名字如果与真人一致，在抄送和协同中会引发身份混乱（个例）（https://x.com/petergyang/status/2108624122339287335）。此外，社区反馈专属邮箱只能通过 Grok Bot 收发（https://linux.do/t/topic/3002150）；是否开放 IMAP 等标准协议，官方未说明（CSDN 上"Grok Bot 专属邮箱 IMAP/SMTP 实战"之类文章发布日期混乱，属于 SEO 搬运，勿信）。有社区帖反映早期测试中个别邮件出现过未及时触发动作的情况（个例）（https://x.com/petergyang/status/2108412799684915576）。对外发送真实邮件前，必须严格人工审批。

## 10.6 Notion · Notion

Notion 不只用来抓取或生成单篇笔记，官方把它当成长周期的结构化状态看板（https://x.ai/bot/guides/grok-bot-for-engineering）。模型上下文有限，长周期任务如果全堆在单次会话里肯定会丢信息。官方团队的做法是：多个工程师 Bot 共享一个 Notion 数据库，每 30 分钟轮询一次 PR 状态，自动筛查 CI 失败、安全告警与合并冲突，在看板中推进任务阶段（https://x.ai/bot/guides/grok-bot-for-engineering）。有社区帖展示过在 15 分钟内用 Grok Bot 搭出自媒体数据看板（个例）（https://x.com/op7418/status/2108545983647023493），也有社区帖分享了让 Bot 把长文抓取排版成 PDF 存入 Notion 的用法（个例）（https://x.com/KinGao476942/status/2100073265716928662）。

接入 Notion 时，在插件列表中选 Notion 做 OAuth 授权。在权限配置窗口里，要精确勾选允许该 Bot 读写的具体页面或数据库，不要盲目授权整个工作区。完成授权后，先在 Notion 建好包含明确字段（例如标题、状态、URL、更新时间）的 Database，把链接告知 Bot，让它把读写规范存成复用 Skill。

Bot 向 Notion 数据表写入内容的格式。

权限给得太宽容易造成页面污染，提示词不够精准时，模型可能会修改其他无关页面。另外，如果有人改动了数据库的列字段，没做容错处理的 Routine 会直接报错。记住，用 Notion 数据库作为 Bot 上下文溢出时的外挂看板，不要试图依赖短期对话记忆去维持几周前的任务进展（https://x.ai/bot/guides/grok-bot-for-engineering）。

## 10.7 Shopify · Shopify

2026 年 10 月 9 日，官方宣布推出 Shopify 电商集成插件（https://x.com/bot/status/2108228871938359347）。Bot 能直接查询未处理订单与履约状态、监控低库存商品清单，还能针对促销策略批量更新商品标题、描述与 SEO 关键词（https://x.com/bot/status/2108228871938359347）。有社区帖提到，配合云电脑定时任务，可以让 Bot 结合社媒舆情巡检竞品价格与差评，针对性优化自家店铺（个例）（https://x.com/Hensen1016/status/2108025562048483583）。

接入时，在应用市场选 Shopify 插件，输入店铺二级域名完成 OAuth 登录授权。日常下发指令时，建议把商品上架与修改规则写进 Bot 的系统设定。如果需要批量上架或覆盖属性，一定要在提示词里强制要求先出修改预览，严禁直接提交。

Shopify 测试店铺的库存查询与商品描述草稿。

电商后台的数据直接关乎资金结算与订单履约。模型批量修改数值时偶有幻觉，价格、计量单位或库存一旦填错，损失很难挽回。所以日常运营中，涉及改价和库存变更必须坚持草稿优先，人工审核后才能同步线上。另外，有社区帖指出，外部平台的半公开数据检索召回率不稳定，不能直接单凭它做经营决策（个例）（https://x.com/Hensen1016/status/2108025562048483583）。

## 10.8 Finance（Plaid 只读）与财务隔离 · Finance & Plaid

![Shane Mac 银行数据跨 Bot 泄露路径与共享云电脑风险](../../images/fig-10-2.png)

*图：Shane Mac 银行数据跨 Bot 泄露路径与共享云电脑风险*

2026 年 9 月 27 日，官方推出了 Finance 金融连接能力，通过 Plaid 协议只读连接银行账户、信用卡与投资组合（https://x.com/bot/status/2103936247995752705）。有社区帖提到，可以向专属财务 Bot 询问未来 10 天即将发生的扣款总额、分析日常支出明细，或者参考跨账户资金调拨（个例）（https://x.com/B_doong2daddy/status/2105711764641833238）。

接入时，在插件中心点击 Finance 插件，在 Plaid 弹窗里选银行并完成双重认证。从协议层面看，Plaid 仅提供只读凭据，Bot 无法直接发起转账交易，也不能修改银行账户设置。

除了只读查账，Grok Bot 在 **v0.71.2（2026-10-14）** 中正式打通了主动结账支付链路，支持在结账环节调用 **Link 与 X Money** 完成付款（需用户审批），详见官方更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与工作流技术文档（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。根据官方说明，Bot 执行结账支付（Checkout / Payment）时的调用优先级顺序依次为：**Vault（内置加密保险箱） → 聊天内 Secure Form（掩码安全表单） → Link / X Money → Take over screen（人工接管屏幕）**（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。社区用户 `@gofordylan` 实测晒单发现，当使用 X Card 经由 Grok Bot 完成消费后，账单交易流水中会自动显示一枚专属的 **Grok Bot 小徽章**，方便一眼区分哪些消费是由 Bot 代理完成的（[https://x.com/gofordylan/status/2110726444485607797](https://x.com/gofordylan/status/2110726444485607797)）。更重要的是，针对用户对 AI 代购与绑卡安全的顾虑，Elon Musk（`@elonmusk`）于 2026 年 10 月 15 日公开发帖做出了极其硬核的赔付承诺（[https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445)，17,221 赞 / 1,686 转发 / 2,128 书签）：*"This works well. If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole."*（如果 Grok Bot 在代购时出错或泄露了你的银行卡——迄今从未发生过——SpaceX 将全额赔付。）

Plaid 只读连接后的支出汇总与日志脱敏。

这里出现过一起真实的数据泄露事故——XMTP Labs CEO Shane Mac 银行数据泄露事件（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。Mac 把个人银行账户连入 Grok Bot 当财务助理，以为只读权限很安全。但同一个账号下的所有 Bot 共用同一台云电脑与文件系统（https://cursor.com/help/grok-bot/computer-and-apps）。按 Mac 本人的解释，另一个 Bot 因此拿到了财务数据，Grok Bot 以他的名义把包含健身房会费、装修开销和刷卡支出的月度审计发进了公司 Slack 频道（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。**只读权限绝对不等于数据不会被转发泄露**，个人银行账户绝不能与包含团队协作工具的账号共用同一套运行环境。

## 10.9 1Password、Microsoft Teams 与 Salesforce 等企服生态 · Enterprise Services

2026 年 9 月 17 日，官方支持了 1Password 集成，Bot 可以在云电脑浏览器中受控调用指定保险库的账号密码登录，真实凭据留在密码管理器中（https://x.com/bot/status/2100335532597502311）。企业管理员在 cursor.com/dashboard/bot 开通 Grok Bot（https://x.ai/news/grok-bot-for-enterprise）；后台的 Setup Checklist 包含插件、Slack 或 Microsoft Teams、网络设置等步骤，Routine 也可以由 Microsoft Teams 消息触发（changelog 8/12、9/16，https://x.ai/changelog/bot）。（原稿称企业公告写了"统一部署 Salesforce 插件同步 CRM、配置 Teams 插件发早报"，公告原文没有这些内容，已改。）

在早期版本接入 1Password 时，需要在客户端单独建一个专用共享保险库（例如命名为 `Grok Bot` 或 `Shared with Grok Bot`）并配置 Service Account 令牌，只把允许 Bot 使用的凭据移进去（https://learngrokbot.com/plugins）。随后在 Grok Bot 中关联扩展，每次 Bot 尝试提取密码并执行自动填充时，系统都会向用户弹出单独的审批确认卡（https://x.com/bot/status/2100335532597502311）。企业版管理员可以在 Team Marketplace 管理团队可用的插件、配置网络策略（https://cursor.com/docs/grok-bot/teams-and-enterprises）。

到了 **2026 年 10 月 22 日（v0.75.2）与 10 月 23 日（v0.75.5）**，官方在凭据安全与个人设备生态上完成了三次重大跃升（官方文档：[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)、[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)、[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）：

1. **1Password Brokered Sign-in（1Password for Agents，v8.12.42+ 免共享库逐次授权登录）**：2026 年 10 月 22 日，1Password 官方发布 `"1Password for Agents"` 架构并将 Grok Bot 作为首发合作伙伴（`@1Password` 官宣帖：[https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)，10,507 赞 / 1,076 转发 / 7,122 书签；`@bot` 官宣帖：[https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874)，3,663 赞 / 276 转发 / 964 书签）。在新版 **Brokered approval** 模式下，你**不再需要新建共享密码库（shared vault）或配置 Service Account 令牌**。只需在本地设备安装并解锁 **1Password v8.12.42 或更高版本**，通过 `Settings → Connect apps → 1Password → Connect` 绑定；当 Bot 需要登录网站时，会弹出 **Review in 1Password**，你在手机或电脑的 1Password App 内用指纹/面容或 Passkey 逐次批准，凭据即直接注入云端浏览器，Bot 全程看不到明文密码。注意该模式默认读取已连接账号下的 **Personal / Private vault（个人/私有库）**，此前使用旧版共享库方案的用户只需在 `Settings → Connect apps` 中 Disconnect 再 Reconnect 即可切换至新版。社区用户 `@oxpsats`（偶像派作手，[https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670)）利用 1Password 授权彭博社（Bloomberg）会员凭据，让 Bot 自动登录突破付费墙研读海外财经研报；`@JCOMBuilds`（[https://x.com/JCOMBuilds/status/2112997408510452123](https://x.com/JCOMBuilds/status/2112997408510452123)）则每天早晨按 iPhone Action Button 语音呼出助理 Bot `"Eve"`，自动调用 1Password 凭据为妻子下单星巴克。
2. **内置 Grok Bot Vault（v0.75.5 加密只写保险箱）与“一密一宅”黄金法则**：官方于 2026 年 10 月 23 日上线 `Settings → Vault`（`@bot` 官宣帖：[https://x.com/bot/status/2113754107861532677](https://x.com/bot/status/2113754107861532677)，9,398 赞 / 767 转发 / 2,756 书签；官方文档：[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)），支持加密只写（write-only）存储 **Logins（账号密码与 2FA/TOTP）**、**Cards（银行卡，支持移动端摄像头 Scan 扫卡识别）** 与 **Contact info（收货地址与电话）**，支持从 1Password、Chrome、Safari、Firefox、Bitwarden、LastPass 批量导入 **5 MB 以内的 CSV**，并支持为每个条目添加 Bot 可读的明文 **Hint**（如 `"Corporate Amex"`）。官方技术文档（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）明确了登录时的调用优先级：**已保存的浏览器会话 → Vault → 1Password → 聊天内 Secure Form → 人工接管屏幕**。**务必警惕的核心风控边界**：根据官方文档（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）记载以及社区博主 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）与 `@JianWeiSignal`（见微｜Signal，[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)）的重点提醒，**保存在 Vault 中的银行卡在结账调用 `BrowserSecureFill` 自动填充时，不会触发单独的逐笔 Vault 弹窗确认**（仅受通用购买审批规则约束）；若你希望每笔消费都亲手确认卡号，切勿将主力信用卡常驻保存在 Vault 中。对此，`@martinpaulweiss`（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）提出了广受好评的 **“一密一宅（One home per secret）”拆分法**：日常网站登录与 2FA 全部放在 1Password；Grok Bot Vault 仅存放特定限额卡与收货地址；新注册的临时账号暂存 Vault，事后统一迁入 1Password。
3. **iOS 原生 Calendar / Reminders / Contacts 直连（v0.75.2）**：根据官方更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与移动端指南（[https://cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)），Grok Bot iPhone 客户端在获得系统授权后，可直接读写手机本地原生的 **Calendar（日历）**、**Reminders（提醒事项）** 与 **Contacts（通讯录）**。社区用户 `@TyeInBloom`（[https://x.com/TyeInBloom/status/2113767679588770271](https://x.com/TyeInBloom/status/2113767679588770271)）将 iOS 原生三件套、1Password 逐次授权登录、iPhone Action Button 一键语音以及 `"Hey Siri"` 专职 Bot 快捷指令组合在一起，打造出全功能随身 AI 秘书。

1Password 专用库登录时的审批与日志脱敏。

有社区帖提到，曾有用户在多 Bot 群聊里误输入明文密码，导致同一群组的所有 Bot 全部捕获到了凭据（个例）（https://x.com/i/status/2107339523038331338）。**绝不能在共享群聊中向 Bot 发送明文凭据**，任何外部访问必须通过专用的密码库或环境变量 Secrets 管理。在对接 Salesforce 等关键业务数据库时，如果后台未设置严格的字段级只读策略，Bot 误操作可能会覆盖销售阶段与客户线索。此外，在企业级安全治理上，根据官方安全文档（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)），管理员在配置云端虚拟机出站域名白名单（如 `*.domain.com:443`）时，现可勾选 **`Apply to MCP servers`** 将网络白名单强制同步至所有 MCP 服务器调用，并可配置自然语言团队 Auto-Review 规则（设为 `Block` 或 `Require approval`）以及通过 `cursor.surface=grok_bot` 过滤 OpenTelemetry 审计遥测事件。

---

[← 上一章：§09 连接器与 Marketplace · Connectors](../part3-integrations/09-connectors.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§11 中国用户的集成：没有插件也能用 · China Integrations →](../part3-integrations/11-china-integrations.md)

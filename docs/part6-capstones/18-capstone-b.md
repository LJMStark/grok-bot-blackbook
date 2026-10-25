# §18 研发场景：Bot + Cursor 云端 Agent + GitHub · Capstone B

[← 上一章：§17 从零搭一个“中文内容工作室” · Capstone A: Building a Chinese Content Studio](../part6-capstones/17-capstone-a.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§19 额度去哪了 · Where Usage Goes →](../part7-saving/19-usage.md)

---

> **适合谁**：有代码仓库、会用 GitHub 的开发者或技术负责人。**前提条件**：Cursor 账户可用云端 Agent（Cloud Agents）、GitHub 仓库已连接；Notion 看板和 Private Worker 是可选项。不写代码的读者可以跳过本章，或者只看 18.7 的"人工终审"原则。

## 18.1 研发舰队编制：五位专职 Bot 与一位运维管家 · Engineering Fleet Roster

假设你翻看官方工程指南就会发现，如果试图让一个万能 Bot 既读前端需求、又调后端接口、还顺便修部署脚本，轮次稍微一长，上下文就会被琐碎日志挤爆，前脚定好的架构规范后脚就忘得一干二净。SpaceXSI 工程师 Lingxi Li 给出的解法是**拆分为专职工程师舰队**（https://x.ai/bot/guides/grok-bot-for-engineering）。Grok Bot 的本质是一台带独立电脑的工程实习生，能替你管编码智能体，还会慢慢学你的工作习惯。Lingxi Li 的团队常驻了五位专职工程 Bot：Baltata 管移动端共享层与 iOS、Shaoruru 管桌面端与 CI 流水线、Hogan 管底层基建与权责不明的问题、Craig 管 Android 端、Quill 管测试套件与安全框架（https://x.ai/bot/guides/grok-bot-for-engineering）。

每个专职 Bot 都有独立记忆和有限的上下文窗口，只盯单一领域时，规范抓得最准（https://x.ai/bot/guides/grok-bot-for-engineering）。官方团队公布的数据显示，用这套工作流，Lauren 一个月交付了超过 2000 个 Pull Request；Balta 和 Shaoru 四周内用 Grok Bot 搭出了 Grok Bot 自己的骨架；Lingxi Li 也在三周内单凭 Grok Bot 做完了 iOS 初版（https://x.ai/bot/guides/grok-bot-for-engineering）。官方市场上已经沉淀出可直接导入的模板，包括 Lingxi 的 Engineer Bot、Nightly Audit Engineer，Eric Zakariasson 的 Projects Manager，以及 Cursor 官方的 SWE（https://x.ai/bot/guides/engineering）。

除了写代码的 Bot，编制里最关键的角色是不写业务代码的运维管家 Jenny（https://x.ai/bot/guides/grok-bot-for-engineering）。Jenny 每天清晨 5 点找每位工程 Bot 一对一沟通，对操作手册，排查卡点。哪个 Bot 犯了错，Jenny 就介入做根因复盘，更新规则手册并广播给全员，防止同一个错误犯两次（https://x.ai/bot/guides/grok-bot-for-engineering）。为了防止多 Bot 互相唤醒空耗上下文，工程群聊必须遵守安静交接规范。Cursor 团队员工建议在配置里写死约束：只有需要对方采取行动时才发消息，不许回收到、感谢或琐碎进度报备，任务完成后只发一份最终摘要（https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。

![工程 Bot 编制分工与运维架构（Jenny + 业务工程师 + 专职 Audit）](../../images/fig-18-1.png)

*图：工程 Bot 编制分工与运维架构（Jenny + 业务工程师 + 专职 Audit）*

> [!NOTE]
> 📸 **截图位（待补）**：五位专职工程 Bot 与运维 Bot Jenny 的协作群聊与配置文件

## 18.2 从 Issue 到复现包：把 Bug 关进沙箱 · Bug Triage & Reproduction

GitHub 仓库收到新缺陷报告时，直接让大模型进源码库翻找修补，很容易引发代码幻觉。官方用例给出的标准解法是让专门的排查角色先接手，把不可靠的用户反馈转成一份**规范化复现包**（https://cursor.com/help/grok-bot/use-cases）。排查角色需要连上工单系统、预发沙箱、受控浏览器和抓包工具，在受控的临时测试账号下复现问题，严禁碰线上真实客户数据；测试凭据必须走安全审批交接，不能直接贴在聊天框里（https://cursor.com/help/grok-bot/use-cases）。此前社区就发生过在全员群聊里误发密码导致密钥暴露的事故（https://x.com/i/status/2107339523038331338）。

在官方公开的客服与工程联动标杆案例中（https://x.ai/news/grok-bot-customer-support），自 2026 年 8 月 14 日 Cursor 并入 SpaceX SuperIntelligence（SpaceXSI）后，全球用户客服工单量瞬间暴增 175%。官方为此构建了由五位专职 Bot 组成的舰队：Intake Triage Bot（分诊接待 Bot）、Billing & Refund Bot（账单与退款 Bot）、**Technical Repro Bot（技术复现 Bot）**、Incident Batch Bot（事故批处理 Bot）与 Product Feedback Synthesizer Bot（产品反馈聚类 Bot）（https://x.ai/news/grok-bot-customer-support）。其中，**Technical Repro Bot** 专门承接所有疑似代码 Bug 的工单，在独立云沙箱中完成自动化环境还原与最小复现验证，配合 Product Feedback Synthesizer Bot 每天从海量对话中抽取并聚类超过 20,000+ 个产品反馈数据点直接转化为研发工程工单，帮助官方在零新增客服招聘（节省约 200 名人力）的前提下将单票解决成本压降至 $0.20–$0.30（https://x.ai/news/grok-bot-customer-support）。

Grok Bot 设计师 Peng Zheng（`@pengzheng_`）也分享了官方内部设计与工程团队的日常 Bug 分拣复现工作流（[https://x.com/pengzheng_/status/2110245240863178793](https://x.com/pengzheng_/status/2110245240863178793)，86 赞、5 转发、108 书签）：内部团队每天让 Grok Bot 自动盯守反馈渠道与 GitHub Issues，对新上报的 UI 异常或交互缺陷先在云电脑里跑通复现并截屏取证，随后直接拉起 Cursor Cloud Agents 修改代码，最后在沙箱内对比修复前后的 UI 表现完成闭环。

收到缺陷 Issue 后，直接向 Bot 派发官方定义的初始任务提示词：

```text
Read this bug report and reproduce it in staging using a fresh test account. Return exact steps, expected and actual behavior, screenshots, browser and OS details, relevant console or network notes, and a minimal test case if possible. Do not use production customer data.
```

Bot 在沙箱内跑完后，会输出一份包含完整操作步骤、预期与实际表现对比、系统环境参数、控制台报错堆栈和最小复现用例的交付包（https://cursor.com/help/grok-bot/use-cases）。这份材料既是后续编码智能体的输入依据，也是衡量修复是否成功的基准线。

待在实际工程代码库中验证从 GitHub Issue 抓取到生成复现包的完整用时与准确率。

> [!NOTE]
> 📸 **截图位（待补）**：GitHub Issue 详情页与被打上 bug 标签的初始待办

> [!NOTE]
> 📸 **截图位（待补）**：复现专职 Bot 在云电脑沙箱中抓取的报错日志与浏览器控制台

> [!NOTE]
> 📸 **截图位（待补）**：Bot 生成的规范化 Bug 复现包与前后表现对照

## 18.3 调度 Cursor 云端 Agent：提示词与本地 Worker · Cloud Agent Dispatch

工程 Bot 拿到复现包后，自身不用在桌面开编辑器一行行敲代码，而是作为调度者去唤起 Cursor 云端 Agent（https://x.ai/bot/guides/grok-bot-for-engineering）。Lingxi Li 介绍，每个工程 Bot 都能创建 Cursor 云端 Agent、实时读运行转录、审查 PR 附带的测试证据，遇到卡点就排队追加消息或打断重跑，不用工程师在多个 Agent 之间反复切屏盯梢（https://x.ai/bot/guides/grok-bot-for-engineering）。借助这种调度机制，团队能将过去手工管 15 个云端 Agent 的上限拓展到**同时并行管理超过 200 个云端 Agent**（https://x.ai/bot/guides/grok-bot-for-engineering）。

派发编码任务时，工程 Bot 会按具体场景挂载专属技能，比如用于视觉优化的 `/lingxi-design`、用于代码规范审计的 `/react-native-best-practices`、用于架构评审的 `/lingxi-review`，或者用于产品决策的 `/lingxi-product`（https://x.ai/bot/guides/grok-bot-for-engineering）。如果开发环境需要特定内网访问、企业 VPN 或特殊机器配置，官方支持将闲置的 Mac mini 接入为 Cursor Cloud Private Worker。由 Grok Bot 直接调度该本地节点运行云端 Agent，调动本地 iOS 模拟器并回传实时运行截图（https://x.ai/bot/guides/grok-bot-for-engineering）。官方提到，这省掉了过去为了保持环境常驻而在家里专门配置主机跑开源工具的麻烦（https://x.ai/bot/guides/grok-bot-for-engineering）。

Cursor / Grok Bot 产品工程负责人 Eric Zakariasson（`@ericzakariasson`）在 2026 年 10 月 24 日与 10 月 25 日连发两帖（[https://x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099)、[https://x.com/ericzakariasson/status/2114157733276525044](https://x.com/ericzakariasson/status/2114157733276525044)），详解了家用常开 Mac mini 的远程节点注册与 Worker 部署方案：第一，只需在家里常开的 Mac mini 上启动并登录 Grok Bot 桌面端，这台机器就会自动注册到 `Settings > Computer` 设备列表中，此后无论你在外地用手机还是轻薄本向任何云端 Bot 下达指令，Bot 都可以远程在你的家用 Mac mini 上执行本地编译与测试任务；第二，你可以直接在聊天窗口里要求 Grok Bot 在该远程机器上自动配置并启动 `cursor-agent worker` 守护进程，一行手敲配置都不用写即可完成私有算力节点的挂载。

工程 Bot 发起云端编码调度的参考提示词结构如下：

```text
Create a Cursor cloud agent for this reproduction pack. Invoke /react-native-best-practices for code standards. Require proof showing before vs. after screenshots and passing test logs. If the agent hits environment flakiness, send a follow-up to unblock it immediately.
```

除了由云端 Grok Bot 向下调度 Cloud Agent 与本地 Mac mini，2026 年 10 月中旬起社区全面跑通了基于 **BDK（Bot Developer Kit）与 `cursor-grokbot-agents` 技能**的**跨端双向调用架构**：让运行在本地电脑上的编码 Agent（Claude Code、Codex、Cursor IDE）与云端 Grok Bot 互相派单、各展所长：

1. **本地 CLI 向云端 Grok Bot 派发多媒体与全网检索重任（`@StarkLJM` & `@kangxiaile`）**：作者 Mr.鼓先生（`@StarkLJM`）在实战教程（[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411)）中演示了如何通过 BDK（`cursor-grokbot-agents`）打通本地终端里的 Codex / Claude Code 与云端 Grok Bot——当本地 Claude Code 负责主工程编写时，直接向云端 Grok Bot 下发“制作一段 20 秒《上下五千年》中国历史线条画动画短片”的子任务，云端 Grok Bot 在沙箱中独立完成分镜绘制与视频合成，直接向本地返回渲染好的 `0:20` MP4 视频卡片与 `2.7 MB` 的完整源码压缩包。开发者 `@kangxiaile`（康熙AI了，[https://x.com/kangxiaile/status/2109752183889744216](https://x.com/kangxiaile/status/2109752183889744216)）则利用 Grok Bot 独有的免费原生 X 检索优势，构建了“本地 Claude Code 写代码遇到新库或舆情需求 → 派单给云端 Grok Bot 搜索 X 全网最新实测帖 → Grok Bot 整理成结构化 Markdown 传回本地 → Claude Code 读取后继续写代码”的闭环。
2. **三合一订阅下的双向互调与六大联动范式（`@z_lumia` & `@AIShovelLab`）**：`@z_lumia`（x白，[https://x.com/z_lumia/status/2113800469571313974](https://x.com/z_lumia/status/2113800469571313974)）在开通 The X Subscription 三合一订阅后打通了完整双向链路：本地的 Claude Code 和 Codex 随时发消息向云端 Grok Bot 调取长期记忆与全网调研报告；反过来，云端 Grok Bot 也能直接下发指令在本地台式机上执行 CLI 命令。`@AIShovelLab`（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）则将这套 Grok Bot + Claude Code / Codex 组合拳总结为六大核心联动范式：用路由 Skill 阻止盲目重试、本地与云端双向聊天派单、语音随身派活、Cloud Agent 并发执行、单 Bot 端到端内容流水线，以及利用 `+alias` 邮箱后缀精准触发 Routine（v0.75.2 起 Routine 频率上限已提升至全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时，定时最小间隔为 5 分钟，详见 https://cursor.com/help/grok-bot/routines）。
3. **4 次 API 调用纯标准库 Python 脚本绕过 Webhook 400 报错（`@mikan77_aoi`）**：当本地工具或外部服务向 Grok Bot 的 Webhook 推送复杂代码或长 JSON 载荷时，常常会因为格式校验严格而遭遇 HTTP 400 报错。`@mikan77_aoi`（橘子🍊，[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）编写了一个零外部依赖、零守护进程（zero-daemon）的纯 Python 标准库（`urllib.request` + `json`）桥接脚本，仅通过 **4 次 API 调用**（鉴权获取会话 → 创建/定位目标 Bot 线程 → 投递结构化任务指令 → 拉取执行回执）就能让本地 Claude Code 绕过 Webhook 限制，稳定地将任务交接给云端 Grok Bot：

```python
#!/usr/bin/env python3
"""Zero-dependency stdlib bridge: Local Claude Code / CLI -> Cloud Grok Bot (4 API calls)"""
import json, os, sys, urllib.request

API_BASE = os.environ["GROKBOT_API_BASE"]      # e.g. https://cursor.com/api/bot/v1
API_TOKEN = os.environ["GROKBOT_API_TOKEN"]
BOT_ID = os.environ["GROKBOT_TARGET_BOT_ID"]

def api_call(method: str, path: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=data,
        headers={"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"},
        method=method,
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def handoff_to_grokbot(task_prompt: str) -> dict:
    # Call 1: Verify bot status & session context
    bot_info = api_call("GET", f"/bots/{BOT_ID}")
    # Call 2: Create a fresh isolated conversation thread to avoid context bloat
    thread = api_call("POST", f"/bots/{BOT_ID}/threads", {"title": task_prompt[:60]})
    thread_id = thread["id"]
    # Call 3: Dispatch structured task message
    msg = api_call("POST", f"/threads/{thread_id}/messages", {"text": task_prompt})
    # Call 4: Poll / fetch initial run receipt
    return api_call("GET", f"/threads/{thread_id}/runs/{msg['run_id']}")

if __name__ == "__main__":
    print(json.dumps(handoff_to_grokbot(sys.stdin.read().strip()), ensure_ascii=False, indent=2))
```

4. **云电脑内安装 Codex CLI + 完成时 Webhook 唤醒实现零轮询耗电（`@AbhisheKumarA7`）**：除了调用外部机器，开发者 `@AbhisheKumarA7`（Abhishek Kumar，[https://x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578)）展示了另一种极客解法——直接在 Grok Bot 的云电脑（cloud computer）内部安装 Codex CLI，并配置一条任务完成时的 **Webhook**。当耗时漫长的重度代码构建与重构任务在后台跑完时，由脚本主动触发 Webhook 唤醒 Grok Bot 验收交付，全程**零轮询（zero polling token waste）**：

```bash
# Run heavy coding task in cloud box background & wake Grok Bot via Webhook only on completion
nohup bash -c '
  codex exec --full-auto "Refactor auth module and run full pytest suite" < /dev/null > /tmp/codex_run.log 2>&1
  EXIT_CODE=$?
  curl -sS -X POST "$GROKBOT_ROUTINE_WEBHOOK_URL" \
    -H "Content-Type: application/json" \
    -d "{\"event\":\"codex_done\",\"exit_code\":$EXIT_CODE,\"log_path\":\"/tmp/codex_run.log\"}"
' >/dev/null 2>&1 &
```

待验证本地 Mac mini 配置为 Private Worker 后的 iOS 模拟器截图回传延迟。

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 对话流中调用 Cursor Cloud Agent 的派发指令与参数卡片

> [!NOTE]
> 📸 **截图位（待补）**：Cursor Cloud Agent 实时运行转录（Transcript）与命令执行输出

> [!NOTE]
> 📸 **截图位（待补）**：云电脑 Private Worker（本地 Mac mini）运行 iOS Simulator 的实时画面

## 18.4 Opus 5.5 路由与多模型分工栈 · Opus 5.5 Routing & Model Stack

研发流程中若让高单价模型全程跑格式化或编译报错轮询，额度很快就会耗尽。2026 年 10 月 7 日，Elon Musk 在 X 上公开宣布，Grok Bot 正在接入竞争对手的顶尖模型作为后端，包括 Anthropic 的 Claude Opus 5.5、Midjourney 与 Suno 等接口，根据具体任务的达成概率动态选择最适配的模型（https://x.com/elonmusk/status/2107724314451878104；报道见 https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk）。Musk 当时并未公开各类任务具体如何分发到外部模型的规则（https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk）。

为什么必须在“对话路由层”与“重度编码执行层”之间划清界限？中文社区关于 Grok Bot 真实体验的一场高赞争鸣揭示了底层原因：博主 `@Khazix0918`（数字生命卡兹克，[https://x.com/Khazix0918/status/2111709708226797737](https://x.com/Khazix0918/status/2111709708226797737)，285 赞、4 转发、54 书签）吐槽如果直接把默认聊天窗口当成重度苦力裸用，常会遇到默认路由的轻量对话模型“不思考、张嘴就来、查都不查直接回复”的问题；对此，开发者 `@object_nullll`（[https://x.com/object_nullll/status/2111717423837778173](https://x.com/object_nullll/status/2111717423837778173)）一针见血地给出了架构解答：**Grok Bot 的对话层（conversational layer）设计初衷是收集上下文、对齐验收标准、编写结构化 Prompt，并将重度执行任务委派给 Cursor Cloud Agents（`CloudAgent`）或云电脑上的 CLI Workers，绝不能把轻量对话路由模型当成直接写复杂代码的苦力**。开发者 `@realbenzh`（Ben Zhang，[https://x.com/realbenzh/status/2111295936635015631](https://x.com/realbenzh/status/2111295936635015631)）的飞书 + Linear + 邮箱研发流正是这一原则的写照：先把飞书（Feishu）、Linear、电子邮箱和团队文档全部接入 Grok Bot 汇总完整业务上下文，在聊天窗里与 Bot 对齐交付目标和验收标准（acceptance criteria），随后让 Grok Bot 通过 CLI 交互式驱动 `@orca_build` 完成重度构建交付。

在实际研发分工上，社区开发者摸索出一套**多模型分层协作栈**（https://x.com/i/status/2101944767412129920）。在日本开发者的工作流中，先由 Grok Bot 负责网络调研与架构规划，再交由 Claude Code 进行编排，核心开发由 Cursor Projects 承接，日常杂务继续交由 Grok Bot 推进（https://x.com/i/status/2101944767412129920；另见 https://x.com/i/status/2103438409553604976）。在 Opus 5.5 支持接入后，社区帖称（个例，https://x.com/i/status/2109300337203183940）分工模式可细化为：Grok Bot 充当工作助理与架构拆解者，Opus 5.5 负责攻克算法难点与前端交互实现，Sonnet 5.5 负责编写单元测试与集成测试；另一社区帖称（个例，https://x.com/i/status/2108990316644847920）由 Bot 拆分工单后让 Opus 解决重难点，轻量模型处理常规修补，没有人工审批绝不自动合入。发起任务时，社区帖称（个例，https://x.com/i/status/2109265867859177552）可直接通过指令呼叫：

```text
Use Cursor cloud agent with Opus 5.5 to implement the core logic for this issue. Keep auxiliary tests and style checks on standard models. Do not merge until human review is complete.
```

更有甚者，开发者 `@kaelanyiu`（Kaelan Yiu，[https://x.com/kaelanyiu/status/2114213605566742884](https://x.com/kaelanyiu/status/2114213605566742884)）搭建了一个每隔几天自动跑分动态选型的**“模型评测元 Bot（Meta-Evaluator Bot）”**：该 Bot 定时对当前各大前沿大模型运行一轮真实业务代码基准测试，并根据实测得分动态修改其他干活 Worker Bots 在未来几天内通过 CLI 调用的底层模型配置，实现模型路由的优胜劣汰。

需要特别注意的计费边界是：在官方于 2026 年 10 月 18 日推出的 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，详见 https://cursor.com/help/grok-bot/plans 与 https://cursor.com/help/the-x-subscription/overview）体系下，Grok Bot、Grok 与 Cursor 共享同一个包含在套餐内的 Grok 周额度池；但**当你在 Cursor 或 Cloud Agent 中调用非 Grok 系列的第三方模型（如 Claude Opus 5.5 / Sonnet 5.5 等）时，会直接扣减你在 `grok.com/dashboard/billing` 中充值的 Prepaid Credits（预付额度），而不会消耗套餐内的 Grok 周额度池**（https://cursor.com/help/grok-bot/plans）。

待实际调用 Cursor 云端 Agent 并观测是否成功路由至 Opus 5.5 及其单次 PR 额度消耗。

![Opus 5.5 与多模型分工栈拓扑（Grok Bot 架构 → Opus 5.5 编码 → Sonnet/快模型 测试）](../../images/fig-18-2.png)

*图：Opus 5.5 与多模型分工栈拓扑（Grok Bot 架构 → Opus 5.5 编码 → Sonnet/快模型 测试）*

> [!NOTE]
> 📸 **截图位（待补）**：后台模型路由面板中调用 Claude Opus 5.5 的请求记录

## 18.5 自动化闭环：视觉比对、Notion 看板与代码审查 · Feedback Loop & Review

编码智能体把代码写完只是流水线的前半程，没有严格反馈闭环的自动化只会带来大量垃圾变更。Lingxi Li 强调，维系工程 Bot 团队运转的核心是**给予完整的反馈闭环**（https://x.ai/bot/guides/grok-bot-for-engineering）。云端 Agent 可以截取屏幕图像，Grok Bot 则利用其多模态能力核验界面改动是否符合要求。视觉呈现与预期不符时，Bot 会直接驳回并督促 Agent 重新修改（https://x.ai/bot/guides/grok-bot-for-engineering）。官方团队甚至将 SpaceXSI 的语音 API 接入云端 Agent 的系统音频输入输出，利用语音信号与转录文本自动化测试端到端语音交互能力（https://x.ai/bot/guides/grok-bot-for-engineering）。环境偶发波动导致 Agent 停滞时，工程 Bot 会主动介入纠偏（https://x.ai/bot/guides/grok-bot-for-engineering）。

为了突破单次上下文窗口的限制，也让人无需翻阅漫长聊天记录即可掌握全局进展，团队设置所有工程 Bot 共同维护一个共享 Notion 数据库看板（https://x.ai/bot/guides/grok-bot-for-engineering）。每隔 30 分钟，工程 Bot 会轮巡一次数据库，对其中的每个 Pull Request 执行三项硬性检查：验证 Bugbot 评论与安全扫描结果是否属实、检查 CI 流水线是否报错、排查合并冲突（https://x.ai/bot/guides/grok-bot-for-engineering）。一旦发现异常，Bot 立即向云端 Agent 发送纠错指令，并将 Notion 看板上的状态重置回进行中；三项检查全部通过后，任务状态切为待评审，并自动触发代码审查（https://x.ai/bot/guides/grok-bot-for-engineering）。审查评估置信度极高且影响范围很小的 PR 会被自动合并；一旦涉及关键变动，则等待工程师人工复核（https://x.ai/bot/guides/grok-bot-for-engineering）。

随着 2026 年 10 月 22 日官方 **v0.75.2** 版本正式推出原生 **Pages（Canvas）** 功能（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)；官方发布帖见 [https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)，6,544 赞、567 转发、2,008 书签），研发团队除了使用外部 Notion 数据库外，还可以直接让主控工程 Bot 在客户端内部创建并维护一张实时热更新的 **研发冲刺看板 Page（底层由 `WriteCanvas` / `EditCanvas` 驱动）**。该看板常驻于对应 Bot 右侧信息栏的 **Library（资料库）** 中，支持设置 `Only you`、`Your team`（团队管理员可在 `Dashboard → Grok Bot → Bot capabilities` 中统一管控）或 `Anyone with the link` 三级分享权限（https://x.ai/changelog/bot）。参照社区开发者 `@melvindvivas` 打造的幕僚长 `Activity Dashboard` 范式（[https://x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882)，1,087 赞、1,687 书签；提示词拆解见 [https://x.com/melvindvivas/status/2113676938820895045](https://x.com/melvindvivas/status/2113676938820895045)），你可以要求所有专职工程 Bot 在推进 Issue 复现、Cloud Agent 编码与 PR 审查时同步更新同一张 Page 的四大视图：**时间线视图（Timeline view）**、**进行中任务（Tasks in progress）**、**已完成任务（Completed tasks）** 以及 **等待人工合并审批的 PR（Items waiting for human approval）**。

此外，如果你采用“本地 Claude Code + 云端 Grok Bot”双栈协同，还可以使用社区验证的**共享 Obsidian Vault 工程日志方案**。继 `@itsvlady`（Vlady，[https://x.com/itsvlady/status/2110803638671020277](https://x.com/itsvlady/status/2110803638671020277)，352 赞、55 书签）晒出重度 Vibe-Coder 的月度双栈账单（$120 Claude Code + $55 Grok Bot）后，开发者 `@frogchan9o1`（[https://x.com/frogchan9o1/status/2110883156891140416](https://x.com/frogchan9o1/status/2110883156891140416)）分享了一套极具性价比的“$20 Claude Code + $30 The X Subscription Premium”架构：让本地 Claude Code 与云端 Grok Bot **共用同一个 Obsidian Vault 知识库目录**，将每一次 Bug 排查报告、架构决策记录（ADR）、终端执行日志以及依赖包安装清单全部以标准 Markdown 沉淀在同一套目录中，实现跨智能体生态的零摩擦上下文共享。

待验证 Notion 数据库 30 分钟轮询脚本触发自动合并低风险 PR 的稳定性。

![研发场景端到端闭环流水线（Issue → 复现 → 云端 Agent → 核验 → PR → 人工合并）](../../images/fig-18-3.png)

*图：研发场景端到端闭环流水线（Issue → 复现 → 云端 Agent → 核验 → PR → 人工合并）*

> [!NOTE]
> 📸 **截图位（待补）**：主工程 Bot 根据排查结果创建工作项并指派到 Notion 看板

> [!NOTE]
> 📸 **截图位（待补）**：Cursor Cloud Agent 提交的 Pull Request 页面及附加测试证据

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 多模态比对前后 UI 截图并自动驳回样式偏差的评注

> [!NOTE]
> 📸 **截图位（待补）**：共享 Notion 数据库看板中各 PR 状态在 30 分钟轮巡下的变迁

## 18.6 凌晨三点代码巡检与 P0 应急通道 · Nightly Audits & P0 Process

工程师离线休息时，云端常驻算力正好转去常规治理。官方工程团队设立了**凌晨三点的夜间代码巡检例程**（https://x.ai/bot/guides/grok-bot-for-engineering）。每天凌晨 3 点，工程 Bot 会自动启动，清理代码库中的无用死逻辑、优化代码结构、加速客户端加载速度并压缩产物体积。清晨工程师会收到一批清洗干净的 Pull Request，代码重构变成了日常例行机制（https://x.ai/bot/guides/grok-bot-for-engineering）。除常规清理外，这套机制还衍生出多种巡检模式：排查遗留漏洞的安全巡检、防止构建时间膨胀的 CI/CD 耗时巡检、填补单语言发布漏洞的国际化巡检、消除 iOS 与桌面端功能差异的双端对齐巡检，以及汇总过去 24 小时已合并 PR 的进度追赶巡检（https://x.ai/bot/guides/grok-bot-for-engineering）。

日常巡检之外，面对严重线上故障，团队配置了专门的 P0 紧急干预流程（https://x.ai/bot/guides/grok-bot-for-engineering）。云端 Agent 在启动开发实例、安装环境与运行测试套件时往往较耗时，一旦某个任务被打上 P0 标签，工程 Bot 就会启动高频临时 Routine，每隔 5 分钟检查一次 Agent 的运行转录，分析其推演逻辑，并在 Agent 出现卡顿或无谓消耗时间时主动纠偏引导（https://x.ai/bot/guides/grok-bot-for-engineering）。Lingxi Li 特别提醒，这种高频主动干预机制消耗 Token 的速度远超常规操作，必须严格限定在真正的紧急场景下启用（https://x.ai/bot/guides/grok-bot-for-engineering）。

Lingxi Li 最喜欢的夜间提示词原文只有一句："You have six hours tonight. Build whatever you want. Have fun!"（https://x.ai/bot/guides/grok-bot-for-engineering）。下面是本书在这句话基础上加了清理范围和 PR 要求的改写版：

```text
You have six hours tonight. Clean up dead logic, optimize bundle size, and improve startup latency across our active components. Package each distinct improvement into a clean PR with passing tests. Do not merge anything.
```

待在私有代码库中运行 3:00 a.m. 巡检 Routine 并记录无效死代码清理 PR 的采纳率。

> [!NOTE]
> 📸 **截图位（待补）**：凌晨 3 点 Nightly Audit 专职 Bot 发起的无用代码清理 PR

> [!NOTE]
> 📸 **截图位（待补）**：P0 紧急任务触发时 5 分钟转录监控的实时干预卡片

## 18.7 人工终审、合并红线与真实额度核算 · Human Gate & Usage Economics

无论自动化链路多么完善，涉及核心业务边界时绝不能交出最终控制权。官方安全规范明确规定，不可逆操作必须保留人工确认，后台由 Bot 触发的操作审批卡约在 10 分钟后自动过期失效（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。大影响范围的代码合并、生产数据库变更以及关键凭证权限，都必须留在**人工审查关卡**前（https://x.ai/bot/guides/grok-bot-for-engineering）。在企业级合规层面，根据官方安全架构文档（https://cursor.com/docs/grok-bot/security），团队管理员不仅可以用自然语言编写团队专属的 Auto-Review 审查规则（设为 `Block` 直接阻断或 `Require approval` 要求人工审批），还能配置云端沙箱的出站网络域名白名单（格式如 `*.domain.com:443`）并勾选 **`Apply to MCP servers`** 强制约束所有 MCP 服务器流量。

研发流水线落地的另一大硬约束是成本核算。自 2026 年 10 月 18 日起，官方正式推出 **The X Subscription 三合一统一订阅**（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、中文版 [https://cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)、总览 [https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)；`@bot` 官方公告见 [https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)），将 **Grok**、**Cursor** 与 **X Premium** 整合为单一订阅计划，其中包含 Grok Bot 权限的三个档位分别为 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）**（Free $0 与 Plus $8/月档位不含 Grok Bot）。与此同时，根据官方定价与账单说明，既有独立订阅的 Cursor 付费个人方案分为 Pro（20 美元/月）、Pro+（60 美元/月）与 Ultra（200 美元/月），团队方案为 Teams（40 美元/人/月）（https://cursor.com/pricing；https://cursor.com/help/grok-bot/plans）。老订户只要不主动迁移，仍可保留原有旧版独立 Cursor 档位与定价，或通过 `Settings > Usage & Billing > Manage Plan > Get Access with Grok` 关联个人 SuperGrok（社区整理对应档位为 SuperGrok 30 美元/月、SuperGrok Plus 100 美元/月、SuperGrok Heavy 300 美元/月，见 https://penchan.co/ai/grok/grok-bot/）及 X Premium+ 账号（多账号额度不叠加，自动取周额度上限更高的一档生效，见 https://cursor.com/help/grok-bot/faqs）。但务必注意：**一旦你在 `cursor.com/unify` 或 `accounts.x.ai/unify` 中主动将旧版独立计划升级合并为 The X Subscription，该切换是单向不可逆的，无法再退回旧版独立订阅计划**（https://cursor.com/help/grok-bot/plans）。

新旧两套订阅体系在额度消耗与第三方模型扣费上存在关键差异（https://cursor.com/help/grok-bot/plans）：
- **在全新的 The X Subscription 体系下**：Grok Bot 与 Grok、Cursor **共享同一个周额度池（one weekly usage pool）**，每周固定重置且不结转；当周额度池耗尽，或在 Cursor / Cloud Agent 中调用**非 Grok 系列的第三方模型（如 Claude Opus 5.5 等）**时，系统会直接扣减你在 `grok.com/dashboard/billing` 的 `Additional usage credits` 模块中预先充值的 **Prepaid Credits（预付额度）**（支持开启 Auto Top-up 自动充值并设置独立的月度额外消费封顶上限 Monthly additional usage limit）。
- **在尚未迁移的旧版独立 Cursor 计划下**：Grok Bot 自带独立的每周用量池，官方未公布具体额度数字（https://cursor.com/help/grok-bot/plans）。第三方文档记录指出，Bot 触发的 Cursor 云端 Agent 会计入 Cursor 套餐自身的用量（https://learngrokbot.com）。每周额度耗尽后，若开启后付费按需计费（On-demand billing），可在 `Settings > Usage & Billing > On-demand monthly limit`（或 `cursor.com/dashboard > Spending > Monthly Limit`）中将月度封顶上限设为无、固定金额或无限制（https://x.ai/changelog/bot；https://cursor.com/help/grok-bot/plans）。

在真实额度消耗方面，官方论坛中员工曾披露，高负荷运转的 Bot 每一轮对话都需要重新读取完整上下文，每步约消耗 8 万至 9 万 Token，且多 Bot 协作中约有三分之一的交互属于 Bot 之间的相互唤醒空转（https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。社区帖称（个例，https://x.com/miniyarov/status/2105428357273800799）在 Cursor Pro 档位下，每条交互消息大约消耗 1% 的周额度；如果配置了无休止的 5 分钟轮询 Routine，单月空转消耗可达数百美元（https://x.com/fleyta88/status/2109346840382415019）。社区用户 `@charlie_pmp`（Charlie，[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）也提醒，升级到 The X Subscription 后由于 Grok Bot、Grok App 与 Cursor IDE 三端共用同一个周额度池，任何高频冗余的后台 Routine 都会直接挤占你白天在 Cursor 里写代码的周额度。工程落地的省额原则非常明确：每个独立缺陷修复任务必须开启全新对话以切断臃肿上下文、多 Bot 间严禁无意义的客套回复、以窄范围事件驱动（如 GitHub / Codex 完成时 Webhook 或专属邮箱 `+alias` 加号别名触发）替代高频轮询，高危合并动作始终收口在人工最终确认。

待记录一个标准 Issue-to-PR 全流程在 Cursor Pro 与 Pro+ 方案下的周额度百分比消耗。

> [!NOTE]
> 📸 **截图位（待补）**：人工审查高风险代码变更并最终确认合并的审批卡片

> [!NOTE]
> 📸 **截图位（待补）**：Dashboard/usage 界面展示的周额度与 Cursor Cloud Agent 消耗曲线

---

[← 上一章：§17 从零搭一个“中文内容工作室” · Capstone A: Building a Chinese Content Studio](../part6-capstones/17-capstone-a.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§19 额度去哪了 · Where Usage Goes →](../part7-saving/19-usage.md)

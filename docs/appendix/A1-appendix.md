# 附录 A–E · 速查、价格、模板、连接器、更新日志

[← 上一章：§24 从 "聊天" 到 "管理" · Managing, Not Chatting](../part9-mental-models/24-mental-models.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：附录 F–J · FAQ、术语、竞品、资源、来源总表与勘误 →](../appendix/A2-appendix.md)

---

我整理这本黑皮书时，最头疼网上的过时信息和随口编的数字。不少人把发布首周的旧规则当真理，连套餐包不包含 Grok Bot 都说错。附录不讲虚的，我把全书用到的硬性指标、价格档位、提示词、连接器目录和版本演进，都理成了可核对的清单和表格。所有内容都以 2026-10-12 的官方文档、公告和公开研究为准。

## 附录 A 官方硬数字速查 · Official Hard Numbers

写自动化流程时，最容易踩的坑是误以为 Bot 的云电脑和 Routine 能无限制挂机。官方在系统架构和安全策略里卡了死指标。我查了官方文档，把关键限制理在下表，核对日期是 2026-10-12。

![官方核心硬限制与边界全景图](../../images/fig-A1-1.png)

*图：官方核心硬限制与边界全景图*

| 维度 | 硬性限制指标 | 运行机制与边界行为 | 来源 |
|---|---|---|---|
| 账户 Bot 总量 | 已不限于 50 个 | 设计文章曾写约 50 个；9 月 1 日 v0.31.0 起可创建超过 50 个 Bot | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| 群聊协作规模 | 2 至 6 个 Bot | 新建群聊必须选择 2 到 6 个 Bot，不支持单个 Bot 自聊或超过 6 个 Bot 组群 | [docs.x.ai: Chat and Collaboration](https://docs.x.ai/grok-bot/chat-and-collaboration.md)  |
| 单 Bot Routine 上限 | 最多 50 个 | 单个 Bot 名下挂载的例行任务不可超过 50 个，删除操作即时生效且不可撤销 | [docs.x.ai: Skills and Routines](https://docs.x.ai/grok-bot/skills-routines-and-automations.md)  |
| Routine 运行记录保留 | 最近 20 次 | 系统仅保留每个例行任务最近 20 条执行日志，超出的历史记录会被滚动覆盖 | [docs.x.ai: Skills and Routines](https://docs.x.ai/grok-bot/skills-routines-and-automations.md)  |
| Routine 触发时间间隔 | 不得低于 5 分钟 | 定时任务之间的时间间隔至少为 5 分钟，系统禁止秒级或极高频轮询 | [docs.x.ai: Skills and Routines](https://docs.x.ai/grok-bot/skills-routines-and-automations.md)  |
| 后台审批等待超时 | 约 10 分钟 | 由 Routine 或跨 Bot 触发的审批卡约 10 分钟未处理即标记 Expired 并终止动作 | [docs.x.ai: Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy.md)  |
| 桌面输入框附件数量 | 最多 6 个 | 桌面端对话框一次最多拖入或选取 6 个文件附件 | [docs.x.ai: Files and Results](https://docs.x.ai/grok-bot/files-and-results.md)  |
| 文档与多媒体附件大小 | 单文件最大 25 MB | 文档（PDF/Word/Excel 等）、图片和音频文件单文件体积上限为 25 MB | [docs.x.ai: Files and Results](https://docs.x.ai/grok-bot/files-and-results.md)  |
| 视频附件大小限制 | 单文件最大 200 MB | 视频文件上传体积上限为 200 MB，超出需转码或切片提供 | [docs.x.ai: Files and Results](https://docs.x.ai/grok-bot/files-and-results.md)  |
| Teach a task 示范录屏 | 最长 10 分钟 | 屏幕交互演示录制上限为 10 分钟，仅录制屏幕动作，不采集麦克风音频 | [docs.x.ai: Skills and Routines](https://docs.x.ai/grok-bot/skills-routines-and-automations.md)  |
| 免费试用期限窗口 | 7 天 | 免费试用本质为固定用量额度，同时设有 7 天有效期窗口，耗尽不补发 | [cursor.com: Plans and Billing](https://cursor.com/cn/help/grok-bot/plans)  |
| 企业闲置电脑释放 | 30 天无活动自动销毁 | 企业版开启 Terminate Inactive Computers 后，成员闲置满 30 天的云电脑会被清理 | [x.ai: Changelog v0.58.0](https://x.ai/changelog/bot)  |
| 本地网络出口停用生效 | 5 分钟内切断 | 企业管理员在后台关闭 Local Egress 后，成员端活跃的本地路由在 5 分钟内终止 | [docs.x.ai: Settings](https://docs.x.ai/grok-bot/settings-and-notifications.md)  |
| 快捷键：调出命令面板 | `Cmd/Ctrl+K` | 快速搜索 Bot、对话、历史记录与插件 | [docs.x.ai: Chat and Collaboration](https://docs.x.ai/grok-bot/chat-and-collaboration.md)  |
| 快捷键：语音听写输入 | `Cmd/Ctrl+D` | 在输入框获得焦点时启动麦克风语音转写 | [docs.x.ai: Chat and Collaboration](https://docs.x.ai/grok-bot/chat-and-collaboration.md)  |

关于硬限制，有两点要特别提醒。第一，别以为把 Routine 设成 5 分钟一次就能做准实时监控，这是额度雪崩的开始。按官方规则，5 分钟一次等于一个月跑 8640 次。要是每次都把整个页面重读一遍，一周额度很快就见底。第二，后台任务的审批卡只有约 10 分钟寿命。半夜跑 Routine 一旦触发敏感操作审批，10 分钟没人点就会变成 Expired，任务直接停掉。想做到无人值守，得提前在 Auto-review 里配好自动放行规则，或者把敏感动作收成只写草稿。

## 附录 B 档位与价格表 · Plans & Pricing

早先不少网帖说 Cursor Pro 不包含 Grok Bot，那是过时的说法。官方在 8 月 25 日的 v0.27.0 更新日志里对 Cursor Pro、SuperGrok 和 X Premium+ 放开了访问（8 月 26 日的公告帖没提 X Premium+）。核对日期是 2026-10-12。

![Cursor 订阅与 Grok 关联用量判定流程图](../../images/fig-A1-2.png)

*图：Cursor 订阅与 Grok 关联用量判定流程图*

### B.1 访问资格与档位对应速查

| 用户所持套餐/席位 | 获取访问权限途径 | 所属用量层级 | 每周包含用量说明 | 官方标价（美元） | 来源 |
|---|---|---|---|---|---|
| Cursor Pro | 登录同一 Cursor 账户 | 低档（基础层） | 基础每周用量，低于 Pro+ | $20 / 月 | [cursor.com: Pricing](https://cursor.com/pricing)  |
| Cursor Pro+ | 登录同一 Cursor 账户 | 中档（进阶层） | 充足每周用量，低于 Ultra | $60 / 月 | [cursor.com: Pricing](https://cursor.com/pricing)  |
| Cursor Ultra | 登录同一 Cursor 账户 | 高档（旗舰层） | 最高每周用量池 | $200 / 月 | [cursor.com: Pricing](https://cursor.com/pricing)  |
| Cursor Teams (Standard) | 成员账户直接登录 | 团队席位额度 | 每位成员均可访问，遵循团队额度 | $40 / 人 / 月 | [cursor.com: Pricing](https://cursor.com/pricing)  |
| Cursor Teams (Premium) | 成员账户直接登录 | 高阶团队席位 | 团队用量池更大，包含优先资源 | $120 / 人 / 月 | [penchan.co 定价归档](https://penchan.co/ai/grok/grok-bot/)  |
| 个人 SuperGrok | 方案页关联 Grok 账户 | 低档（等同 Pro） | 授权基础每周用量，低于 Plus | $30 / 月（官方帮助页不写价格，此价格来自第三方评测） | [cursor.com: Plans](https://cursor.com/cn/help/grok-bot/plans)  |
| 个人 SuperGrok Plus | 方案页关联 Grok 账户 | 中档（等同 Pro+） | 授权充足每周用量，低于 Heavy | $100 / 月 | [penchan.co 定价归档](https://penchan.co/ai/grok/grok-bot/)  |
| 个人 SuperGrok Heavy | 方案页关联 Grok 账户 | 高档（等同 Ultra） | 授权最高每周关联用量 | $300 / 月 | [penchan.co 定价归档](https://penchan.co/ai/grok/grok-bot/)  |
| X Premium+ | 方案页关联并登录 Grok | 低档（低于 Plus） | 授权基础关联用量 | 依地区而定（社区帖称香港约 311 港币，个例） | [cursor.com: Plans](https://cursor.com/cn/help/grok-bot/plans)  |
| 自助式 Grok Business | Sign in with Grok 登录 | 对应席位许可证 | 与分配席位一致（SuperGrok 或 Heavy） | 依企业席位协议 | [cursor.com: Plans](https://cursor.com/cn/help/grok-bot/plans)  |
| SuperGrok Lite | 无权访问 | 未包含 | 不包含 Grok Bot 权限，需升级后关联 | — | [cursor.com: Plans](https://cursor.com/cn/help/grok-bot/plans)  |

### B.2 计费机制与关键规则

查阅官方说明，计费机制有三条硬规则：

第一是用量**不叠加**。如果你同时有 Cursor Pro（$20/月）又关联了 SuperGrok Plus（$100/月），系统只按较高档的 SuperGrok Plus 算用量，绝不会把两边额度加在一块。关联本身是永久授权，一旦绑定就不能解绑，也不能转给其他 Cursor 账号。

第二是官方未公布具体数字。官方从没公开过每周用量到底包多少 Token 或步骤。后台是按智能体执行步数和模型开销动态扣减的，不是算你发了几句对话。

第三是按需付费不会半途掐断任务。每周用量按周重置。额度用完如果开了 On-demand（按需付费），超额部分走 Cursor 账单，受后台设的 Monthly Limit 限制。官方文档明确写着，就算任务执行中途撞上线，正在跑的任务也会跑完，不会被强行掐断。

## 附录 C 提示词与 Routine 模板集 · Prompts & Routine Templates

这里整理了 30 条来自官方文档和社区高手的提示词与 Routine 模板，复制就能用。写法全按官方推荐结构来：定好时间与时区、卡死输入源、划清审批红线、讲清输出格式，再加上没数据或失败时的退避动作。

### C.1 监控与情报类模板（模板 1–5）

#### 模板 01：真实 AI 工作流监听 Routine

适用场景：工作日早晨定时抓取社区里验证过的高价值自动化案例，过滤营销噪音。触发方式：工作日 09:15 定时触发。出处：@rowancheung 方案 [X 引用](https://x.com/rowancheung/status/2108328114552000842)

```text
Every weekday at 9:15am in my time zone, search X and the web for new AI workflows people are actually running. Keep only cases that name the old task, the tool, and the result: time saved, a step removed, or a handoff that used to need a person. Drop product announcements, "10 prompts" threads, and anything the author has not used more than once. Return at most 3. For each, give the link, the job it replaces, what I would need connected, and whether it fits my work. Send it to me on Slack. Do not post or reply anywhere else. Save this as a routine. If nothing qualifies, send one line saying so.
```

#### 模板 02：品牌与个人声誉监测 Routine

适用场景：监控社交平台过去 24 小时内的品牌或个人提及，分类汇总并推送到协作频道。触发方式：工作日 09:00 定时触发。出处：@rowancheung 方案 [X 引用](https://x.com/rowancheung/status/2108328114552000842)

```text
Every weekday at 9:00am, search X for mentions in the last 24 hours of [your brand, @handle, or your own name]. For each hit, give the author, link, a one-line summary, and whether it is praise, complaint, question, or neutral. Do not reply to anyone. Post the digest in [your Slack channel] and tag me. Save this as a routine. If a source is unavailable, say which one.
```

#### 模板 03：品类潜在客户与竞品差评监听 Routine

适用场景：每 4 小时扫描行业痛点、竞品投诉与采购选型意向，输出高意向线索。触发方式：每 4 小时定期触发（仅在有新线索时推送）。出处：@rowancheung 方案 [X 引用](https://x.com/rowancheung/status/2108328114552000842)

```text
Every 4 hours, search X for people evaluating [your category]. Catch three things: reviews or complaints about [category]; posts asking which [category] to use; and complaints about the problem [your product] solves. Quote the post, link it, name the account, and label it review, shopping, or complaint. Skip anything older than 24 hours, and skip [category] accounts promoting themselves. Post to [your Slack channel] only if there is at least one new hit you haven't already shared. Do not reply to or interact with anyone. Save this as a routine. If the search fails, report the failure in Slack.
```

#### 模板 04：行业竞品槽点与迁移诉求定向挖掘

适用场景：反向搜索行业用户对特定产品的抱怨帖，提取功能短板与替代需求。触发方式：每周一上午 10:00 触发。出处：Rowan 讨论区延伸方案 [X 引用](https://x.com/i/status/2109290036978196689)

```text
Every Monday at 10:00am in my time zone, search X and Reddit for explicit user complaints and dissatisfaction posts about [Competitor Product] from the last 7 days. Focus specifically on pricing spikes, missing features, poor customer support, and users asking for alternatives. Filter out promotional affiliate threads. Return top 5 distinct pain points with direct URLs, user quotes, and an analysis of how our solution addresses each. Save as a routine. If no strong complaints are found, report "No significant negative sentiment detected this week."
```

#### 模板 05：官方更新日志监控与自身配置影响审计

适用场景：每天两次监测官方产品更新日志，自动评估改动对已有配置与 Routine 的影响。触发方式：每天 08:30 与 18:30 触发。出处：社区用户惯用法 [X 引用](https://x.com/i/status/2107629480374308893)

```text
Twice every day at 8:30am and 6:30pm in my time zone, fetch the latest changelog from https://x.ai/changelog/bot. Check whether any new release notes have been published since the last check. If new items exist, summarize the key changes, list any new features or deprecations, and explicitly explain how these updates affect my current bots, plugins, and routines. If nothing changed, exit quietly without sending any message.
```

### C.2 个人效能与早晚助理类模板（模板 6–10）

#### 模板 06：睡前夜间异步构建指令

适用场景：准备休息时向项目 Bot 派发夜间自主构建与调研任务，利用异步算力。触发方式：睡前手动发送。出处：@AlexFinn 方案 [X 引用](https://x.com/AlexFinn/status/2108319537116725426)

```text
I am about to go to sleep. What is one big, self-contained thing you can start building, researching, or testing in the cloud workspace while I am sleeping? Formulate the execution plan, execute the safe steps in /workspace, and leave a structured review card for when I wake up.
```

#### 模板 07：晨间决策聚焦与待办推进指令

适用场景：清晨起床时向个人助理 Bot 获取当下最关键的决策卡点清单。触发方式：清晨手动发送。出处：@AlexFinn 方案 [X 引用](https://x.com/AlexFinn/status/2108319537116725426)

```text
I just woke up. Review my calendar, inbox drafts, and active projects. Give me a concise list of top 3 decisions or approvals we can make right now to push the ball forward today. Group items by urgency, link each source context, and do not take external actions until I approve.
```

#### 模板 08：新号上手业务盘点与交接探索

适用场景：初次配置 Bot 时，连接常用通讯和文档后探索最适合交接的 3 项事务。触发方式：初次接入时手动发送。出处：@sidejob_AJ 方案 [X 引用](https://x.com/sidejob_AJ/status/2108592848300056956)

```text
Connect my email, calendar, and docs, then inspect recent activities and pick three concrete, low-risk recurring tasks I can safely hand off to you today. For each task, describe the expected input, the exact boundaries, and how you plan to draft results for my review.
```

#### 模板 09：个人工作负荷卸载盘点

适用场景：周期性盘点个人手头的繁琐事务，寻找可被技能化的低效环节。触发方式：双周手动复盘。出处：Roman Ugarte 访谈建议 [YouTube 访谈](https://www.youtube.com/watch?v=maSdsTLaMuU) （团队成员访谈）

```text
Analyze my recent sent emails, scheduled calendar meetings, and recurring document edits over the past two weeks. Identify the top 3 repetitive operational patterns that consumed my manual time. Propose a draft skill specification for each, explaining what you can take off my plate completely and what approval boundaries are required.
```

#### 模板 10：新增联系人跟进与草稿整理 Routine

适用场景：工作日早晨核对通讯录新增人员，预先草拟跟进任务而不直接外发。触发方式：工作日 08:30 定时触发。出处：@rowancheung 方案 [X 引用](https://x.com/rowancheung/status/2108328114552000842)

```text
Every weekday at 8:30am in my time zone, read my address book and list contacts added in the last 14 days. For each, show name, date added, phone, email, and any note. Ask me what we talked about before you write anything. Once I reply, draft a follow-up task for each person in [your task tool] with the context attached. Never text, email, or call anyone. Save this as a routine. If the address book is unavailable, say so and do not use old data.
```

### C.3 治理审计与成本控制类模板（模板 11–15）

#### 模板 11：Routine 成本与变更过滤审计

适用场景：对现有 Routine 深度体检，用事件驱动或低成本哈希校验替代高频轮询。触发方式：手动定期审计。出处：@fleyta88 方案 [X 引用](https://x.com/fleyta88/status/2109346840382415019)

```text
Audit my existing routines and rebuild the execution plan around actual changes.
1. List every routine, its schedule and expected output.
2. Replace polling with narrow event triggers where supported.
3. For frequent schedules, check only a hash, count or timestamp before doing full work.
4. Stop immediately when nothing changed.
5. Leave irreversible actions as drafts for human review.
6. Log every run with time, result, changed status and approval state.
7. Flag routines with over 95% no-change runs.
Show me the proposed changes and estimated savings first. Don't modify or delete anything without approval.
```

#### 模板 12：月度无产出 Routine 淘汰审计

适用场景：统计各 Routine 实际被采纳产出的比例，找出静默失败或无意义空转的任务并淘汰。触发方式：每月 1 日定时运行。出处：@kocer_eth 方案 [X 引用](https://x.com/kocer_eth/status/2101669438038634827)

```text
Monthly on the 1st at 9:00am, audit all active routines on this Bot. Review the last 20 run records for each routine: calculate the percentage of runs that produced actionable output approved by me, identify routines that failed silently or were ignored, and recommend at least one routine that should be paused or deleted with clear reasons. Present this report as a review table and wait for my explicit approval before modifying any routine.
```

#### 模板 13：云电脑系统更新前资产与配置备份

适用场景：在执行系统更新或重置云电脑前，将已装工具与环境清单固化备份。触发方式：手动维护触发。出处：@MilMileBattery 方案 [X 引用](https://x.com/MilMileBattery/status/2107033338548797471)

```text
Act as Chief of Staff. Before updating the Bot Computer:
1. Scan the environment and compile a shared checklist of all installed CLI tools, packages, and their reinstall commands into /workspace/system_manifest.md.
2. Verify all ongoing project scripts, credentials notes, and data files are located under /workspace.
3. Export a plain-text backup summary of our critical routines and environment variables so we can restore them immediately if a reset occurs.
4. Report when backup is completed.
```

#### 模板 14：跨 Bot 协作之“安静交接”Profile 预设

适用场景：配置在 Bot 的 Profile 描述中，杜绝 Bot 之间互相客套、唤醒并空转消耗额度。触发方式：常驻 Profile 设定。出处：Cursor 团队成员推荐 [论坛归档](https://forum.cursor.com/t/grokbot-custom-connectors/169965) （Cursor 员工论坛回复）

```text
Only message another bot when it needs to act. No acknowledgments, thanks, or progress pings. Send one concise summary when the work is done.
```

#### 模板 15：纠错固化与事实源反查规则

适用场景：纠正 Bot 的事实错误，强制其建立先查权威源再回答的长效习惯。触发方式：被纠错后手动发送。出处：@Michael_Fenech_ 方案 [X 引用](https://x.com/Michael_Fenech_/status/2106729045878514147)

```text
Remember this permanent rule: Whenever you are corrected on any factual information (such as dates, numbers, client status, or email details), you must immediately re-verify the authoritative source (Calendar, CRM, or Inbox) before answering. Never guess or hallucinate a replacement fact. Confirm that you have recorded this rule into your memory.
```

### C.4 官方系统提示词与标准工作流模板（模板 16–20）

#### 模板 16：官方采购 Haggle Bot 核心系统提示词

适用场景：全自动供应商支出审计、SaaS 席位闲置排查与合同续约谈判准备。触发方式：Bot 创建与初始化 Profile。出处：官方采购博客 [x.ai 采购案例](https://x.ai/news/grok-bot-procurement)

```text
SETUP — fill in for your org
SYSTEMS
- Spend data lives in: <e.g. Ramp, Brex, NetSuite>
- Contracts live in: <e.g. Drive, Notion, Ironclad>
- Usage/seat data comes from: <e.g. Okta/SSO logs, each tool's admin portal>
- Colleagues reachable via: <e.g. Slack, email>
- Vendor dossiers kept in: <e.g. Notion database, Drive folder>
PEOPLE
- Your operator: <name> — makes all final decisions.
- Who to ask about tool usage: <e.g. the owner listed in spend data, IT, team leads>
- Voice on external emails: <e.g. formal, sent under the operator's name, no agent names>
PERMISSION LINES
- Always allowed, no need to ask: <e.g. reading spend data, messaging colleagues, requesting admin access, pulling reports, updating dossiers>
- Needs the operator's explicit go, every time: <e.g. any vendor-facing send>
- Never, under any circumstances: <e.g. signing, buying, subscribing, approving charges, any binding commitment>
NEGOTIATION DIALS
- Renewal radar: prioritize renewals within <e.g. 120> days.
- Opening anchor: <e.g. 5–10>% below our internal target, never more than <e.g. 25>% off the vendor's latest quote.
- Acceptable reasons to give a vendor for an ask: <e.g. competitive process, market rate, budget>
- Never reveal to vendors: <e.g. usage data, seat counts, internal projects, timeline urgency, that we've decided to renew>
WHAT GOOD LOOKS LIKE (edit with your own vendors)
- Weak finding: "Renegotiate our CRM (~$50k)."
- Strong finding: "Video tool renews Oct 14. 210 seats, 74 idle for 90 days per admin logs. Drop to 150 at renewal = ~$18k/yr. Owner confirmed."
AGENT
You are Haggle Bot, a vendor-spend savings agent. Your job: know the company's vendor spend cold and produce evidence-backed savings, like a sharp procurement colleague — not a list of big vendors to "renegotiate." Operate within the permission lines above without exception.
LEAD WITH THE MONEY — every finding opens with:
TODAY: what we pay now, annualized, from live data, with source.
SAVE: realistic savings and mechanism, with confidence.
REC: one committed recommendation — a menu of options is not a recommendation.
NEXT: what you've already set in motion. (Internal actions happen before you report, not as offers — never "I can ping X if you want.")
PRIORITIZE EVIDENCE: a real opportunity has a dollar figure traced to live spend data, a specific mechanism, and a reason it's actionable now (renewal window, usage data, competing quote). Anything less is a lead — label it, name the missing data, and go get it rather than assuming. Match the "strong finding" example above.
WORK THE CALENDAR: maintain a renewal calendar from billing and contract data; renewals inside the radar window are your priority queue. Leverage lives at renewal.
DO THE RESEARCH YOURSELF: a renewal, quote, or proposal in play means research runs before you recommend anything — never advise "exploring alternatives," explore them. Price 3+ real alternatives against our actual SKU footprint from the live invoice, cite and date every number, state list vs. street price, and include switching costs honestly.
NEGOTIATE DELIBERATELY: before any vendor-facing draft, show the operator the plan — target, opening anchor (within the dials above), walk-away, what we trade for what, and your next two moves if they reject, counter, or go silent. In the message: one reason per ask from the acceptable list, nothing from the never-reveal list, every line priced (unpriced lines get priced by the vendor), and a close where "no" isn't a complete reply — aimed at the rate on the biggest negotiable line, never at lines where our savings come from cutting quantity. Warm tone, firm numbers: the rep argues our case internally, so write to make that easy. A rejected draft is rebuilt from the plan, never edited.
REMEMBER EVERYTHING: keep a per-vendor dossier — spend, terms, renewal date, owner, quotes gathered, and the operator's verdicts. When the operator rejects something, log why and don't repeat the pattern.
VOICE: with the operator — direct, dollars first, no fluff. External — per the voice setting above.
```

#### 模板 17：官方标准技能保存范式（Save a Skill）

适用场景：将一次成功的操作总结并保存为全账户共享的私有技能，固化边界与验证规则。触发方式：完成一次人工调优任务后发送。出处：官方技能文档 [docs.x.ai: Skills](https://docs.x.ai/grok-bot/skills-routines-and-automations.md)

```text
Save the process we just used as a skill called "Weekly account health". Include the source systems, risk definitions, output format, and the rule that customer contact always requires approval. State explicitly when to use it, required inputs and access, step sequence, how to validate results, and what requires human sign-off.
```

#### 模板 18：官方标准定时 Routine 调度范式

适用场景：将已保存的 Skill 挂载到特定 Bot 名下定时执行，包含严格的缺数退避逻辑。触发方式：调度配置时发送。出处：官方技能文档 [docs.x.ai: Skills](https://docs.x.ai/grok-bot/skills-routines-and-automations.md)

```text
Every weekday at 8:00 AM, run the Daily customer-risk skill against the current account list. Post a linked watch list in this conversation. Do not contact customers. If the source data is unavailable, report the failure instead of using old data. Save this as a routine.
```

#### 模板 19：官方事件驱动触发 Routine（Webhook / Slack）

适用场景：基于协同软件事件窄匹配触发任务，杜绝无脑监听全量消息。触发方式：配置事件触发时发送。出处：官方技能文档 [docs.x.ai: Skills](https://docs.x.ai/grok-bot/skills-routines-and-automations.md)

```text
When a message in #customer-escalations contains a support ticket link and the phrase "needs repro", open the ticket, reproduce the issue in staging, and post a repro pack in this conversation. Never post back to Slack without approval. Save this as an event routine.
```

#### 模板 20：官方前置审批与安全边界声明范式

适用场景：要求 Bot 仅做分析与预算建议草案，禁止私自修改投放后台或联系外部代理。触发方式：派发涉及资金或生产环境任务时发送。出处：官方安全与审批文档 [docs.x.ai: Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy.md)

```text
Reconcile the campaign data and draft a recommended budget change. Do not change the campaign or message the agency. Ask for approval after showing the current value, proposed value, and expected impact.
```

### C.5 岗位分工与专职 Bot 设定模板（模板 21–25）

#### 模板 21：官方标准专注型工位设定（Piper - 产品性能巡检）

适用场景：创建专注于性能指标异动、证据链条保留与低侵入的专职工程师 Bot。触发方式：新建 Bot 填写 Profile。出处：官方入门文档 [docs.x.ai: Get Started](https://docs.x.ai/grok-bot/get-started.md)

```text
Name: Piper
Job: Product performance
Description: Investigate product-performance questions using our observability tools. Preserve links and screenshots, separate evidence from hypotheses, and return a short summary with the highest-impact issue first. Never change production settings.
```

#### 模板 22：官方文档入门任务：文档提炼与决策点提取

适用场景：五分钟零插件入门，验证 Bot 对长文本的结构化提取与边界遵守能力。触发方式：拖入文档附件后发送。出处：官方入门文档 [docs.x.ai: Get Started](https://docs.x.ai/grok-bot/get-started.md)

```text
Summarize this document in five bullets. List every date, decision, and open question in a separate section. Cite the page or section for each item. Do not change the source file.
```

#### 模板 23：官方数据分析任务：转化异动对比与排查预案

适用场景：对接分析面板对比用户活跃数据，形成假说但不修改线上配置。触发方式：手动发起专项调研。出处：官方入门文档 [docs.x.ai: Get Started](https://docs.x.ai/grok-bot/get-started.md)

```text
Open our analytics dashboard and compare new-user activation for this week with the previous four weeks. Identify the largest step-level change and draft a short investigation plan with links to the relevant charts. Do not change any dashboards. Ask me to sign in if needed.
```

#### 模板 24：DevRel 工程师原型开发流水线（Matt Palmer）

适用场景：工作日扫描社交书签，提炼痛点草拟 Prompt，交给云端 Agent 编写原型并开 PR。触发方式：工作日定时触发。出处：官方指南实践总结 [X 引用](https://x.com/monokern/status/2108533543848558780)

```text
Every weekday at 10:00am, scan my bookmarked X threads on developer pain points. Pick the most requested utility idea, draft an implementation specification, and hand it over to a Cursor Cloud Agent to build a working prototype. Open a GitHub pull request with an attached summary video and demo link. Never merge the PR automatically.
```

#### 模板 25：销售外联与通话简报就绪助理（Simon Lackowski）

适用场景：工作日早晨 8 点前备妥外联名单、客户通话简报与待审批回复卡。触发方式：工作日早晨 07:30 定时触发。出处：官方销售指南实践总结 [X 引用](https://x.com/monokern/status/2108533543848558780)

```text
Every weekday by 7:30am, review my CRM pipeline and incoming customer emails. Prepare a briefing dossier for today's scheduled sales calls, highlighting current contract value, past blockers, and suggested talk track. Draft follow-up emails for yesterday's meetings and present them as approval cards. Do not send any external communication.
```

### C.6 研发、多模型调度与本地化落地模板（模板 26–30）

#### 模板 26：Opus 5.5 云端 Agent 协同研发分工指令

适用场景：由 Grok Bot 统筹架构拆解，调度 Cursor 云端 Agent 挂载高阶模型编码，严守合并门禁。触发方式：发起工程重构或复杂特性开发。出处：社区分工栈实践 [X 引用](https://x.com/i/status/2109265867859177552)

```text
Act as Lead Architect. Break down this feature request into discrete implementation modules. Delegate the complex backend logic and core algorithm to a Cursor Cloud Agent using Opus 5.5, and delegate the unit tests to a secondary agent. Coordinate their output in /workspace, run the test suite, and present a linked pull request with diff summary. Do not merge anything without my explicit approval.
```

#### 模板 27：中文自媒体矩阵：三道硬门岗位 Profile（觉醒AI）

适用场景：在国内多平台内容生产中，用落盘文件管理调性，封死发布权限，防止越权误发。触发方式：内容 Bot 初始化 Profile。出处：觉醒AI 内容团队实录 [深度文章](https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/)

```text
你是自媒体内容主笔 Bot。严格执行三道硬门纪律：
1. 事实来源门：只认我直接给出的链接和文件，禁止抓取未经核实的营销号内容。
2. 数据核验门：所有引用的性能、价格与财务数据必须来自 /workspace 下的实测报告，并在文中标明核对日期。
3. 发布权限门：你拥有只读与草拟权限，绝对禁止调用发布接口或点击网页发布按钮。成稿全部落盘为 /workspace/drafts/ 下的 Markdown 文件等待人工审核。
```

#### 模板 28：公众号与小红书爆款情报侦察员 Routine

适用场景：定向抓取公开内容源、转写视频文案并归档至知识库，遇到验证码停下交回控制权。触发方式：每天上午 09:30 定时触发。出处：觉醒AI 媒体实践 [文章归档](https://www.jxxy.net/ai/articles/AdrianPunk115-2097311704547987756/)

```text
Every weekday at 9:30am, browse the specified public topic pages. Extract trending titles, user engagement metrics, and recurring comment questions from the past 24 hours. If any platform prompts a login wall or CAPTCHA, stop immediately, alert me, and hand over the browser controls. Save findings to /workspace/intel/daily_digest.md and notify me in chat. Do not interact, like, or post on any platform.
```

#### 模板 29：国内平台无插件环境下的导出巡检与风控避让

适用场景：在无官方插件的国内后台，避免高频连击触发风控，通过读屏或导出文件完成盘点。触发方式：每周五下午 17:00 定时巡检。出处：象鱼工作流实践 [用例总结](https://xiangyugongzuoliu.com/grokbot-use-cases/)

```text
Open the logged-in media backend on the cloud browser. Navigate to the analytics tab, download this week's readership and retention CSV export to /workspace/analytics/, and calculate the average completion rate. Do not perform rapid automated clicks across multiple menus. Once the CSV is saved, close the browser tab, generate a summary table in our chat, and delete temporary download files.
```

#### 模板 30：自定义私有 MCP 服务器挂载指令

适用场景：为全账户挂载具备公网 HTTPS 接口的自定义 MCP 工具服务，扩展原生插件库。触发方式：直接在聊天框向 Bot 发送。出处：Cursor 官方论坛员工回复 [forum.cursor.com](https://forum.cursor.com/t/grokbot-custom-connectors/169965) （Cursor 员工论坛回复）

```text
Add this MCP server: https://your-tools-gateway.example.com/mcp
```

## 附录 D 连接器分类清单 · Connectors Catalog

在 Grok Bot 里，连接器（Connectors）是以插件形式装在整个账户下的。只要添加并在浏览器里完成授权，你名下的所有 Bot 都能共用。核对日期是 2026-10-12，官方应用库收录了 238 个插件，覆盖 10 大分类。

> [!NOTE]
> 📸 **截图位（待补）**：Connect Apps 应用市场与分类筛选视图

### D.1 十大官方分类全量连接器速查表

| 分类名称 | 收录总数 | 包含的全部插件清单（英文原名） | 类别属性与主要作用 |
|---|---|---|---|
| Password Managers | 1 | 1Password | 凭据管理：为云电脑提供受控的密码填充金库 |
| Productivity | 63 | Adobe Developer App Builder, Airtable, Asana, Atlassian, Atlassian Forge, Atlassian Teamwork Graph CLI, Box, Canva, ChatPRD, ClickUp, Coda, Craft, Descript, Fathom, Fireflies, GitBook, GitLab, Glean, Glean Developer Docs, Google Docs, Granola, GSAP, Guru, Harness, IcePanel, Jam, Jotform, Juicebox, LaunchDarkly, Linear, Listen Labs, MagicPath, Mem, Mintlify, Miro, Monday.com, Notion, OneDrive, Otter.ai, Paper, Playwright, Profound, Read AI, ReadMe, Readwise, Resend, Riverside, Runway, Sanity, Smartsheet, Svelte, Teams, TierZero, Todoist, Typeform, UiPath, Upwork, Webflow, Wix, Workable, Wrike, Xero, Zapier | 办公协作、项目管理、文档笔记与工作流触发 |
| Communication | 29 | ActiveCampaign, AgentMail, Ando, Bird, Brevo, Calendly, Customer.io, Fireflies, Gmail, Google Calendar, Infobip, Inkbox, Klaviyo, Knock, Linq, MailerLite, Mailgun, Migma, Nitrosend, Outlook, Outlook Calendar, postiz, Slack, Superhuman Mail, Typeform, Upwork, Workable, X, Zoom | 邮件收发、日程规划、IM 频道消息与社交沟通 |
| Design | 13 | Canva, Docs Canvas, Figma, Google Slides, Mobbin, Mural, Paper, PR Review Canvas, Refero, Slides.com, Superdesign, tldraw, Wonder | 视觉设计、原型预览、幻灯片制作与画板协作 |
| Code | 53 | Amazon Location Service, Appwrite, AWS Amplify, AWS Core, AWS Databases, AWS Deployments, AWS Serverless, Azure, Browserless, Browserstack, Clerk, Cloudflare, CockroachDB, Compound Engineering, Convex, Coralogix, Create Plugin, Datadog, Docker, Encore, Firebase, Floot, GoDaddy, incident.io, JFrog, Knock, Lightrun, MongoDB, Monk.io, Neon Postgres, Netlify, PagerDuty, ParadeDB, Pinecone, PlanetScale, Railway, Redis, Render, Runlayer, ScyllaDB, Sentry, Supabase, Superpowers, Temporal, turbopuffer, Turso, Twilio, Vantage, Vercel, WorkOS, Zscaler, GitHub, Origin | 代码托管、云原生基础设施、数据库与监控报警 |
| Data | 39 | Amplitude, Antimetal, Apify, Astronomer, AWS Data Analytics, Azure Cosmos DB, Braintrust, Bright Data, ClickHouse, Confidence by Spotify, Customer.io, Dagster, dbt Labs, Elastic, Exa, Firecrawl, Fullstory, Grafana Cloud, Grafana Labs, Hex, Hugging Face, Langfuse, Mixpanel, Monid, Observe by Snowflake, Omni Analytics, Omni Integrations, OpenSearch, Parallel, Pendo, PostHog, Postman, prisma, Semrush, Similarweb, Smartsheet, Snowflake, Statsig, ThoughtSpot | 数据仓库、埋点分析、网页数据抓取与模型可观测性 |
| Sales | 16 | Adspirer, Amplemarket, Apollo.io, Attio, Clarify, Clay, Customer.io, Gojiberry AI, Gong, Granola, HubSpot, Hunter, Monaco, Outreach, Salesforce, ZoomInfo | 客户关系管理、获客线索挖掘与销售跟进 |
| Finance | 25 | 1inch, Aave, Airwallex AgentOS, Airwallex Developer, Brex, Capital.com, Chargebee, Circle, Docusign, Kraken, Link, Mercury, Natural, Orthogonal, PayBox, Phantom, Ramp, Razorpay, RevenueCat, RevenueCat Play Billing, Revolut X, Shopify, Stripe, Whop, Xero | 支付网关、电商交易、对账报销与加密资产集成 |
| Research | 11 | Ahrefs, Context.dev, Context7, Crustdata, Harmonic, Parallel, Semrush, SuperMe, Treg, UserTesting, You.com | SEO 调研、商业情报洞察与网络研究 |
| Support | 3 | Intercom, MailerLite, Plain | 客户支持工单、消息归集与服务流流转 |

### D.2 核心高频连接器实战特性与边界

我查了最常用的几个主流工具，在插件集成模式下的能力和边界如下：

| 工具名称 | 对应插件分类 | 核心支持能力 | 关键边界与防踩坑要点 | 来源 |
|---|---|---|---|---|
| Gmail | Communication | 检索阅读邮件、草拟、发送、打标签、清理垃圾箱 | 企业 Google 账户可能需要 IT 管理员在后台预先批准 Grok 应用 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Outlook / M365 | Communication / Productivity | Outlook 邮件与联系人、日历日程增删、OneDrive 文件检索、Teams 频道收发 | 官方拆分为 4 个独立插件，没有单一名为 Microsoft 365 的全家桶，需逐个添加 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Google Calendar | Communication | 读取日程空闲、创建/修改会议、应答邀请 | 插件无法修改 Google Meet 内部设置，也无法自动注入 Zoom 链接 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Slack | Communication | 以当前用户身份读取与发言、参与频道与工作流讨论 | 一个连接对应一个 Workspace；发起的 Routine 需单独配置事件监听 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Notion | Productivity | 检索页面与数据库、创建/更新记录、发布内容 | 支持连接第二个账户，可在调用时指明“使用我的工作 Notion” | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| GitHub | Code | 检索 PR、处理 Issue、代码审查、触发工作流 | 客户端自带内置集成（Connect GitHub 按钮），插件列表无卸载按钮 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| 1Password | Password Managers | 云电脑浏览器自动填充登录凭据 | 连接后仅读取名为“Shared with Grok Bot”的特定保险库，其他金库隔离 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| X (Twitter) | Communication | 原生搜索推文、时间线、趋势、书签与 X Chat | 插件会消耗开发账户 API 额度，付费 Grok Bot 计划附赠起始免费额度 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |

### D.3 热门未入库服务对策与高危黑名单

不少服务目前在 Connect Apps 里没有官方插件，甚至有封号风险。常见缺失项的处理对策与社区踩坑警示如下：

| 服务名称 | 官方插件现状 | 替代操作路径 | 风险级别与避坑指南 | 来源 |
|---|---|---|---|---|
| WhatsApp | 无官方插件 | 云电脑浏览器登录 Web 版 | 极高风险：社区反馈用户将 Bot 接到 WhatsApp 后个人账号被封禁 | [r/GrokBot 封号反馈](https://www.reddit.com/r/GrokBot/comments/1w11r70/)  |
| LinkedIn | 无官方插件 | 云电脑浏览器登录 Web 版 | 高风险：社区反馈 Bot 自动发信后导致该账号所有登录会话被强制吊销 | [r/GrokBot 踢会话反馈](https://www.reddit.com/r/GrokBot/comments/1wp291u/)  |
| Google Drive / Sheets | 无独立插件 | 仅提供 Google Docs 与 Google Slides 插件 | 中风险：表格与网盘需借由浏览器网页版或通过其他办公插件间接读写 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Zoom | 已列入市场但不可用 | 暂无可用插件连接 | 明确故障：登录授权报 Error 4700（Invalid redirect），目前只能在日历手动贴链接 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| 自定义内部服务 | 无开箱即用插件 | 自建 MCP Server 挂载 | 低风险：地址必须为公网可访问的 HTTPS 协议，Bot 无法直接穿透本地 localhost | [forum.cursor.com 讨论](https://forum.cursor.com/t/grokbot-custom-connectors/169965) （Cursor 员工论坛回复） |

## 附录 E 版本更新日志 · Changelog Timeline

Grok Bot 迭代很快。官方更新日志（https://x.ai/changelog/bot）每个版本都标有发布日期（最新 v0.68.1 为 2026 年 10 月 7 日）。我抓取了官方从首发到最新版（共 49 个版本：v0.17.0 至 v0.68.1）的核心改动，理出这条时间线。核对日期是 2026-10-12。

![Grok Bot 架构演进与版本里程碑时间轴](../../images/fig-A1-3.png)

*图：Grok Bot 架构演进与版本里程碑时间轴*

### E.1 关键里程碑版本概览

| 阶段里程碑 | 对应核心版本 | 关键突破功能与行业意义 |
|---|---|---|
| 资格全面扩档 | v0.27.0 | 正式向 Cursor Pro、SuperGrok 和 X Premium+ 付费用户放开访问，奠定大众普及基础 |
| 跨平台与国际化 | v0.21.0 / v0.28.0 | 引入多语言包（含简体与繁体中文），上线 Webhook Routine 接口 |
| 团队协作与共享 | v0.30.0 / v0.31.0 | 上线 Bot 模板链接分享、Link 钱包支付卡审批，引入 Cloud Agent 独立打开模式 |
| 交互与表单重构 | v0.44.0 / v0.45.0 | 推出聊天内嵌表单（Chat forms）、邮件/Slack 草稿确认卡与企业级 Auto-review 规则 |
| 企业与安全治理 | v0.40.0 / v0.50.0 | 全面放开企业版，上线审计日志，推出 Route egress 本地电脑网络出口代理 |
| 团队 Bot 时代 | v0.61.0 | 推出 Team Bots 体系，实现全团队共享 Bot、Slack 深度双向打通与成员独立记账 |
| 主动性与办公扩展 | v0.66.0 / v0.68.1 | 星标主 Bot 具备主动揽活能力（Proactivity），原生支持 PPT 与 Google Slides 演示文稿生成 |

### E.2 全量版本演进速查表（v0.17.0 至 v0.68.1）

| 版本号 | 核心功能改动与演进记录 | 适用范围 | 来源 |
|---|---|---|---|
| v0.68.1 | 1:1 对话支持匹配 Bot 主题色；支持协同生成 PPT 和 Google Slides 演示文稿；草稿卡支持富文本排版邮件；Gmail 垃圾邮件检索与恢复；Team Bot 支持提及 Slack 用户组；输入框键入 `/` 不再弹出技能菜单；云电脑屏幕升至 1920×1200 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.68.0 | 新增马拉地语、泰米尔语、泰卢固语、斯瓦希里语和豪萨语；设置页支持移除其他电脑；Gmail 草稿支持别名发送；命令面板直接检索插件 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.67.0 | 全新设计的 Connect Apps 侧栏入口与新型工作状态展示 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.66.0 | 主动性（Proactivity）：星标主要 Bot 会主动发现潜在任务并提议代劳（需 v0.59.0 以上）；更稳定的自动更新机制 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.65.0 | 团队成员可与 Team Bot 发起独立语音通话；客户端自动更新可靠性增强 | Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.64.0 | 邮件与 Slack 草稿卡提供“停用草稿”选项以允许直接发送；已发布的 Team Bot 支持添加管理员协同维护 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.63.0 | Slack 线程中支持交互式审批卡（仅发起者可点击）；在 Slack 中可通过 Team Bot 私信个人 Bot | Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.62.0 | 选中文字按 `Cmd/Ctrl+L` 快速引用；输入框支持 `-` 或 `1.` 快速生成列表；输入拼写检查；团队管理端按名搜索 Team Bot | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.61.0 | 推出 Team Bots：全团队共享单个 Bot、在 Slack 中直接调用、成员间独立记账并保留私有笔记 | Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.60.0 | Outlook 邮件草稿卡支持：在对话中审核内容后直接一键发送 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.59.0 | 超时过期的 Auto-review 卡片提供“未来始终允许”选项；企业管理后台支持 Team Secrets 团队密钥注入 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.58.0 | 新增捷克语、丹麦语、芬兰语、匈牙利语与挪威语；企业版支持 30 天未活动电脑自动销毁（Terminate Inactive Computers） | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.57.0 | Projects 功能上线：支持启动 Cloud Agent 规划复杂任务并调度多子 Agent 协同；丰富链接预览卡片 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.56.0 | GitHub 增强、表格文件交互优化与更清晰的审批卡片展示 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.55.0 | 安装引导清单（Setup Checklist）与对话内嵌表单自动填充能力优化 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.54.0 | 搜索体验增强、HEIC 格式照片支持；企业管理员可在后台批量删除成员电脑与数据 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.53.0 | Mac 端支持连接 1Password 密码管理器并实现自动填充；支持直接向 Google Drive/OneDrive 上传文件 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.52.0 | GitHub 连接器优化；Routine 支持手动暂停与恢复 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.51.0 | 首次启动自动引导创建首个 Bot；支持彻底删除 Routine；Bot 支持自主微调标题与头像颜色外观 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.50.0 | 设置中推出“Route egress through this desktop”，支持将云电脑网络出口引流至本地设备 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.49.0 | 仓库授权卡支持 GitHub、GitLab、Bitbucket、Azure DevOps；消息中的文件路径可直接点击定位打开 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.48.0 | 多账户平滑切换；Marketplace 支持直接一键添加 Bot；企业版上线 Conversation Insights 统计大盘 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.46.0 | Usage & Billing 页面改版；对话列表支持右键重命名 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.45.0 | 邮件与 Slack 草稿卡机制（审核后发送或丢弃）；企业管理员可强制开启团队级 Auto-review 规则 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.44.0 | 聊天内嵌表单（Chat forms）：遇到登录或关键输入时在聊天框呈现表单；消息时间戳悬停查看；Mac 自动填充 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.41.0 | Marketplace 正式列出 Bot 模板；官方自研 Bot 带有 Verified 认证徽章 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.40.0 | 企业版全面开放（GA）；新增乌尔都语、泰语和孟加拉语；企业后台上线 Audit Logs 完整审计日志 | Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.39.0 | 新增越南语与印尼语支持；新增个性化问候语引导 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.38.0 | 企业组访问权限控制（Group Access）与侧边栏分组名称优化 | Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.37.0 | 安装流程调查日常使用工具；企业控制台显示企业试用期剩余天数 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.36.0 | 消息中 PR 卡片支持右键复制链接；Routine 对话展示流优化；Always allow 规则增强 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.35.0 | 长周期任务执行稳定性提升；采购流程优化；共享 Bot 机制更新 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.34.0 | PR 链接卡片展示实时状态（Open/Draft/Merged/Closed）；Bot 可在指定侧栏分组下创建子 Bot | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.33.0 | 企业版支持组级别权限分配；管理后台支持一键开通团队试用；采购审批卡支持 Link 钱包绑卡一键支付 | Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.32.0 | 国际化输入法兼容性修复；团队初始化设置流程优化 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.31.0 | 问答式上手引导推荐匹配 Bot；后台上线 Setup Checklist；HTML 生成文件提供实时代码预览；Cloud Agent 独立窗口 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.30.0 | 推出 Bot 模板公开与团队分享链接；采购审批卡对接 Link 快捷支付；新增阿拉伯语与希伯来语等 RTL 布局 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.29.0 | 设置页新增 Computers 机器列表管理并配置权限档位；移动端通知支持直接呈现 Bot 回复内容 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.28.0 | 新增俄语、土耳其语、意大利语和瑞典语支持，自动跟随系统语言 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.27.0 | Cursor Pro 订阅者正式开放使用；支持绑定个人 SuperGrok 及 X Premium+ 账户获取用量；Webhook 数据流增强 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.26.0 | 应用菜单增加“Check for Updates”与“Restart to Update”；从右到左排版修复 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.25.0 | 多选问答卡片；个人方案支持将月度按需限额设为 None、Fixed 或 Unlimited；GitHub Routine 支持单 PR 监听 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.24.0 | 设置项与插件支持右键复制直达链接；视频附件右键保存；多团队登录租户选择 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.22.0 | 团队初始化引导增强；多语言界面翻译校对与错位修复 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.21.0 | 语言包支持简体中文、繁体中文、日文、韩文等；输入框 Emoji 选择；Routine 支持 Webhook URL 与密钥触发 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.20.0 | 全局快捷键 `Cmd/Ctrl+D` 语音听写输入；插件默认账号支持重命名编辑 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.19.0 | 设置新增 Manage Plan 方案升级通道；包含额度用尽时支持升级 Ultra 或绑定 SuperGrok Heavy；GPU 硬件加速 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.18.0 | Usage & Billing 页面新增 Cancel Trial 提前取消试用按钮（取消将清空剩余试用额度） | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.17.0 | 自助团队版 Standard 成员支持通过关联个人 SuperGrok Heavy 订阅使用 Grok Bot；丰富 Routine 触发器 | Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |

---

[← 上一章：§24 从 "聊天" 到 "管理" · Managing, Not Chatting](../part9-mental-models/24-mental-models.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：附录 F–J · FAQ、术语、竞品、资源、来源总表与勘误 →](../appendix/A2-appendix.md)

# §05 Bot：给每个同事一份岗位说明书 · Bots & Profiles

[← 上一章：§04 你的第一个任务 · Your First Task](../part1-getting-started/04-first-task.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§06 云电脑：它的工位 · The Computer →](../part2-core-concepts/06-computer.md)

---

## 5.1 一个 Bot 等于什么 · Anatomy

很多人刚接触 Grok Bot 时容易犯一个错误：把它当成套了好看外壳的普通聊天窗口。每次在输入框敲一大段背景，聊完关掉网页；第二天遇到新任务，又开新窗口重敲一遍。这种用法停留在传统聊天机器人的习惯里。聊天会话是随用随扔的消耗品，窗口一关，之前建立的工作默契就散了。

官方文档对它的定义（https://cursor.com/help/grok-bot/bots），是一个有名字、有岗位、有独立对话流，能持续积累上下文的**持久共事的数字同事**。官方设计团队在复盘里写过（https://x.ai/news/designing-grok-bot），系统把概念收敛成了五个基础对象：Bot（持久运行的智能体）、Chat（对话界面）、Prompt（指令或技能提示词）、Tool（操作外部世界的工具）和 Artifact（生成的文档、代码等持久产物）。核心不是聊天记录，而是 Bot 本身。

随着 2026 年 10 月中下旬 v0.71.2（https://x.ai/changelog/bot）至 v0.75.5（https://x.ai/changelog/bot）的连续重磅迭代，一个完整的 Bot 拆开来看，已经从最初的四个基础部分扩展为**六个核心组成部分**（在原有四大组件基础上，新增了专属资料库 `Library` 与专属邮箱 `+alias` 子别名簇）。

一个是身份档案（Profile）。包括名称、头像、岗位标签和常驻描述（Description）。新手常把 Description 空着或随手写句客套话。官方文档写得很明确（https://cursor.com/help/grok-bot/bots），Description 是用来放持久规则的，聊天框只用来派发单次指令。比如“未经人工明确审批绝不对外发消息”要焊死在 Description 里，而“给这十二家客户起草跟进邮件”才是日常在聊天框里发的内容。

一个是工作记忆（Memory）。它能跨会话记住工作偏好、关键事实和任务摘要，第二天打开软件还能接着昨天的思路干。不过官方文档也提醒（https://cursor.com/help/grok-bot/bots），记忆不能代替真实数据源；严肃决策必须让它查实时原始数据，不能靠模糊印象。

一个是独立工位与屏幕（Computer & Workspace）。同一账号下的所有 Bot 共享同一台云电脑、浏览器会话和 /workspace 目录，但界面上各有独立的操作状态和屏幕感知（https://x.ai/news/designing-grok-bot）。官方设计了三层介入机制：后台运行时图标亮紫色表示活跃（Status）；点开能在侧边面板实时预览操作（Preview）；遇到验证码需要人工协助时，能一键全屏接管键鼠（Takeover）。（设计文章配图里还能看到正午、深夜等不同壁纸，是否随时间自动切换文中没有明说。）

一个是对话时间线（Conversation）。对话流里不仅有文字，还有结构化卡片（Inline chat widgets），比如待确认的邮件草稿或多选表单，也有系统事件和例行任务记录（https://x.ai/news/designing-grok-bot）。头像也有状态动作：空闲时安静（Idle），干活时点头（Working），卡住时迟疑（Waiting 或 Blocked），鼠标悬停在头像上能看到当前正在执行的具体步骤，不用盯着三个跳动的圆点猜。

一个是专属资料库（Library，存放该 Bot 维护的 Pages / Canvas 实时页面）。在 2026 年 10 月 21 日至 22 日随 v0.75.2 上线的更新中，官方正式推出了 **Pages（底层由 `WriteCanvas`、`EditCanvas`、`ReadCanvas`、`ListCanvases` 工具驱动的交互式画布）**（https://x.com/bot/status/2112991843235610885；https://x.ai/changelog/bot）。过去，Bot 交付的报告往往淹没在漫长的聊天历史气泡里；现在，每个 Bot 右侧的信息面板（`Bot info pane → Library`）都多出了一个持久化的 **Library（资料库）** 抽屉。这位数字同事为您构建并长期维护的周度数据报表、多智能体协同活动看板（Activity Dashboard）、项目进度追踪器或交互式业务沙盘，都会作为独立的实时网页应用沉淀在它的 `Library` 中。每次定时任务跑完或您口头下令更新数据，它不是重发一份死文件，而是直接对 `Library` 里的同一张 Page 进行原地热更新。

一个是专属邮箱 `+alias` 子别名簇（`mybot+tag@mail.grokbot.com`）。每位 Bot 不仅拥有形如 `mybot@mail.grokbot.com` 的独立工作邮箱（https://cursor.com/help/grok-bot/agent-email），还在 v0.71.2（2026-10-14）起正式支持 **`+alias` 加号子别名簇**，该特性由 Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）正式发布（https://x.com/SamSokolin/status/2110496237241667621，获 3,073 赞、219 转发、1,197 书签）。这意味着同一个专职 Bot 可以免费派生出无限个业务专用收件入口，例如 `mybot+newsletters@mail.grokbot.com`、`mybot+invoices@mail.grokbot.com`、`mybot+alerts@mail.grokbot.com`。更关键的是，您可以在配置 Routine 时设定**仅当邮件发送至特定 `+alias` 子别名时才触发对应的自动化流水线**（https://cursor.com/help/grok-bot/routines；https://cursor.com/help/grok-bot/agent-email），并且自 v0.75.2 起，Bot 在转发邮件时能够完整保留原邮件的 HTML 排版格式、正文内嵌图片（inline images）与附件（https://cursor.com/help/grok-bot/agent-email）。比如社区实践者 `@songsong275452`（引用 `@gokul_i`，https://x.com/songsong275452/status/2113108916229886371）就将所有行业通讯（Newsletters）统一订阅到专属 Bot 的邮箱别名下，让个人主邮箱彻底清净，再由周六定时 Routine 汇总成一份结构化周报。

关于容量与额度底座，官方设计文章给出了硬指标（https://x.ai/news/designing-grok-bot）：当时每个账号的实用上限大概是 50 个 Bot，每个群聊最多容纳 6 个；其中 50 个 Bot 的上限已在 9 月 1 日 v0.31.0 取消（"You can create more than 50 Bots"）（https://x.ai/changelog/bot；https://cursor.com/help/grok-bot/group-chats）。同时，在 v0.75.2（2026-10-22）中，官方将例行任务（Routine）的小时级执行配额大幅上调至**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots）、单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**，定时触发最小间隔仍为 5 分钟（https://cursor.com/help/grok-bot/routines；https://x.ai/changelog/bot）。在订阅与计费架构上，自 2026 年 10 月 18 日起，官方正式推出 **The X Subscription 三合一统一订阅**（https://cursor.com/help/grok-bot/plans；https://cursor.com/help/the-x-subscription/overview；https://x.com/bot/status/2110063783796572496），将 Grok、Cursor 与 X Premium 整合进同一套账单——其中 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 档位包含 Grok Bot（Free $0 与 Plus $8/月档位不含 Grok Bot），三端共享同一个**周额度池（one weekly usage pool）**，超出周额度池或调用非 Grok 第三方模型时从 `grok.com/dashboard/billing` 的 **Prepaid Credits（预付额度）** 中扣除；而既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及自助 Teams（$40/人/月）老订户只要不主动在 `cursor.com/unify` 或 `accounts.x.ai/unify` 切换，仍可保留原独立计划，但一旦单向切换至 The X Subscription 即不可逆退回（https://cursor.com/help/grok-bot/plans）。工具和技能是账号通用的公共资产，很多岗位都要用浏览器或邮件；记忆、例行任务、`Library` 页面和 `+alias` 邮箱路由则是专岗私有资产，只归属于具体的 Bot。官方建议设置职责明确的岗位，比如人才搜寻员（Talent Scout）、报销管家（Expense Manager）、Bug 复现员（Bug Reproduction），反对设通用助手（General Helper）这种缺乏目标约束的模糊角色（https://cursor.com/help/grok-bot/bots；https://cursor.com/docs/grok-bot/use-cases）。

| Bot 组成部分 | 核心载体与入口 | 作用域属性 | 2026-10 最新核心能力与边界（v0.71.2 – v0.75.5） |
| :--- | :--- | :--- | :--- |
| **1. 身份档案（Profile）** | 名称、头像、标签、`Description` | 单 Bot 专有 | 存放持久规则与 Vault `Hint` 匹配口令，严禁混放单次任务指令（https://cursor.com/help/grok-bot/bots） |
| **2. 工作记忆（Memory）** | `Bot info pane → Memory` | 单 Bot 专有 | 跨会话记录偏好与事实摘要；动态事实仍以源系统为准（https://cursor.com/help/grok-bot/bots） |
| **3. 独立工位与屏幕（Computer & Workspace）** | 云端沙箱 `/workspace`、浏览器会话、远程设备 | 账号共享底层 / 独立状态 | 支持 Status / Preview / Takeover 三层介入，可挂载常开 Mac mini 或本机住宅 IP 流量转发（https://cursor.com/docs/grok-bot/work） |
| **4. 对话时间线（Conversation）** | 1 对 1 聊天流、群聊（最多 6 个 Bot）、语音卡片 | 单 Bot / 群聊共享 | 支持 iPhone Action Button 一键实时语音并在挂断后自动沉淀完整逐字稿卡片（https://cursor.com/help/grok-bot/voice-chat） |
| **5. 专属资料库（Library）** | `Bot info pane → Library`（Pages / Canvas） | 单 Bot 维护 / 三级分享 | 沉淀实时更新的交互式报表、Activity Dashboard 与工具，支持 `Only you` / `Your team` / `Anyone with the link`（https://x.com/bot/status/2112991843235610885） |
| **6. 专属邮箱子别名簇（`+alias` Email）** | `mybot+tag@mail.grokbot.com` | 单 Bot 专有路由 | 按 `+alias` 后缀定向触发不同 Routine（全号 300 次/小时，单条 200 次/小时），转发保留完整 HTML、内嵌图与附件（https://cursor.com/help/grok-bot/agent-email） |

![Bot 结构解剖图（Profile、Memory、Computer 与 Conversation 边界）](../../images/fig-05-1.png)

*图：Bot 结构解剖图（Profile、Memory、Computer 与 Conversation 边界）*
> [!NOTE]
> 📸 **截图位（待补）**：Bot 资料编辑弹窗（Edit Profile）与侧栏多 Bot 状态展示

## 5.2 岗位说明书五要素 · Job Description Method

翻看中文社区的讨论，很多人抱怨 Bot 乱跑、产出答非所问，根源在建 Bot 时随手敲了一句“你是一个厉害的技术助理，帮我打理日常一切事务”。例如中文社区创作者 `@Khazix0918`（数字生命卡兹克）在 2026 年 10 月 18 日的帖子中就曾吐槽裸用默认聊天窗口的痛点（https://x.com/Khazix0918/status/2111709708226797737，285 赞、54 书签），而开发者 `@object_nullll` 在架构解析回复中一针见血地指出（https://x.com/object_nullll/status/2111717423837778173）：Grok Bot 的对话层旨在收集上下文、对齐验收标准，并将重度任务根据岗位说明书与 Skill 委派给 Cloud Agents 或云电脑 CLI Workers，绝不能当成零约束的裸聊工具。

掘金开发者迷城在实测中提出过（https://juejin.cn/post/7682695577956483091）：建 Bot 必须给岗位说明书，不能只给一句提示词。一份合格的说明书必须包含**岗位说明书五要素**：身份与记忆、核心使命、关键规则、工作流程、成功指标。

超级峰在粉皮书第 6 课列过由技术总监、公关总监、社群运营、商务总监、增长黑客组成的五人舰队（https://chaojifeng.me/free-courses/grok/learn/basic-06），主要是按业务切分岗位。而在 2026 年 8 月 Cursor 并入 SpaceX SuperIntelligence 后工单暴增 175% 的实战中，官方客服团队同样按岗位说明书拆出了 **Intake Triage Bot（分诊接待）**、**Billing & Refund Bot（账单与退款）**、**Technical Repro Bot（技术复现）**、**Incident Batch Bot（事故批处理）** 与 **Product Feedback Synthesizer Bot（产品反馈聚类）** 五位专职同事，在零新增客服招聘的情况下将单票解决成本压至 $0.20–$0.30、实现 99% 退款全自动闭环（https://x.ai/news/grok-bot-customer-support）。要想让 Bot 稳定工作，官方采购 Haggle Bot 的真实系统提示是很好的参考（https://x.ai/news/grok-bot-procurement）：用 SYSTEMS 限定数据来源，用 PEOPLE 锁定决策汇报人，用 PERMISSION LINES 划分红黄绿三档权限边界（自主执行、必须人工审批、绝不触碰），用 WHAT GOOD LOOKS LIKE 直接给出好坏交付物的具体正反样例。

随着 v0.75.2 与 v0.75.5 相继推出 **1Password Brokered Sign-in**（https://cursor.com/help/grok-bot/connect-apps；https://x.com/bot/status/2113301060811161874）、**Grok Bot Vault 内置加密保险箱**（https://cursor.com/help/grok-bot/secrets；https://x.com/bot/status/2113754107861532677）以及 **Pages 实时画布**（https://x.com/bot/status/2112991843235610885），我们在编写岗位说明书的“第 3 要素：权限红线与审批边界”和“第 5 要素：交付物规范与成功指标”时，必须增补两项至关重要的现代治理条款：

1. **在“3. 权限红线与审批边界”中增补 Vault `Hint` 标签匹配规则与支付风控边界**：
   官方在 `Settings → Vault` 中支持集中保存三类加密只写（write-only）凭据：Logins（登录账号/密码/2FA）、Cards（信用卡/借记卡，支持手机摄像头扫卡或 5 MB CSV 批量导入）与 Contact info（收货地址/电话/邮箱），且每个条目均可填写一段明文 **`Hint`（提示标签）**（https://cursor.com/help/grok-bot/secrets）。Bot 永远无法读取明文卡号、CVV 或密码，仅能通过 `BrowserSecureFill` 工具自动填充，但 **Bot 可以读取明文 `Hint` 标签**。同时，官方技术文档明确定义了登录优先级（`已保存浏览器会话 → Vault → 1Password → 聊天内 Secure Form → 人工接管屏幕`）与结账支付优先级（`Vault → 聊天内 Secure Form → Link / X Money → 人工接管屏幕`）（https://cursor.com/docs/grok-bot/work）。
   因此，在多 Bot 团队中，必须在每个专职 Bot 的岗位说明书里写明 **Vault `Hint` 标签白名单匹配规则**——例如硬性规定差旅预订 Bot 仅允许调用 `Hint` 明确标注为 `"Use for work travel only"` 或 `"Corporate Amex"` 的卡片与航司账号，严禁触碰其他 `Hint` 条目。此外，根据官方安全文档（https://cursor.com/help/grok-bot/secrets）以及社区安全研究者 `@kial`（https://x.com/kial/status/2114201768414646280）与 `@JianWeiSignal`（见微｜Signal，https://x.com/JianWeiSignal/status/2114195530611855488）的重点提醒：**一旦将银行卡保存在 Vault 中，结账填充时不会触发单独的逐笔 Vault 弹窗确认**（仅受通用购买审批约束），若岗位要求每一笔消费都必须由人类亲手输入卡号逐单核准，岗位说明书应明确规定采用 `@martinpaulweiss` 提出的“一密一宅（One home per secret）”拆分法（https://x.com/martinpaulweiss/status/2114210343467536531），不在 Vault 常驻主力信用卡，改走聊天内单次 `Secure Form` 或 1Password 逐次生物识别审批（https://x.com/1Password/status/2113276767582498943）。（尽管 `@elonmusk` 已于 2026 年 10 月 15 日公开承诺如果 Grok Bot 代购出错或泄露银行卡，SpaceX 将全额赔付：https://x.com/elonmusk/status/2110610960474079445，但在岗位说明书层面做好 `Hint` 隔离依然是企业风控的第一道防线。）
2. **在“5. 交付物规范与成功指标”中增补专属 Page 看板维护与三级分享权限**：
   除了在对话流里输出 Markdown 表格，现在应当在岗位说明书中指定该 Bot 在其 `Library` 中长期维护一张专属的 **Page（Canvas 实时看板）**（https://x.com/bot/status/2112991843235610885），并明确规定该 Page 的更新时机与**三级分享权限（Sharing Permissions）**（https://cursor.com/docs/grok-bot/teams；https://x.ai/changelog/bot）：
   - **`Only you`（仅自己可见）**：适用于涉及个人财务、未公开人事评估或敏感机密的私有岗位看板；
   - **`Your team`（团队全员可见）**：适用于研发进度、客服队列或部门周报看板（Team 计划默认开启，管理员可在 `Dashboard → Grok Bot → Bot capabilities` 中统一管控团队内部 Page 共享策略，详见 https://cursor.com/docs/grok-bot/teams）；
   - **`Anyone with the link`（任何持有链接者可见）**：适用于对外公开的产品路线图、客户交付战报或社区开源榜单。
   例如开发者 `@melvindvivas`（Melvin Vivas）就为自己的幕僚长（Chief of Staff）Bot 制定了维护 `Activity Dashboard` 专属 Page 的交付规范（https://x.com/melvindvivas/status/2113676935956160882，获 1,087 赞、1,687 书签），将所有专职 Bot 的时间线（Timeline view）、进行中任务（Tasks in progress）、已完成任务（Completed tasks）和待人工审批事项（Items waiting for human approval）实时收口到一张看板上，并通过定时 Routine 自动刷新（https://x.com/melvindvivas/status/2113968491573514576），彻底终结了多 Bot 窗口切换的混乱。

我调研了官方做法和社区讨论，整理出这份通用的岗位说明书模板。新建 Bot 时，可以直接填空放进 Description 或初始化工作指引里：

```text
# 岗位说明书：[岗位名称]

## 1. 身份与使命 (Identity & Mission)
- 岗位身份：你是专门负责 [具体业务领域] 的专职执行者。
- 核心使命：端到端独立负责 [核心业务目标]，把凌乱的原始输入加工成可以直接交付的确定性产物。

## 2. 数据来源与工位 (Systems & Sources)
- 权威输入源：只从 [指定的系统/指定目录/特定网址/专属邮箱 +alias 后缀] 提取事实，绝不凭空推测未经验证的数据。
- 工具使用范围：仅允许使用 [指定工具名称或指定已连接插件]。

## 3. 权限红线与审批边界 (Permission Lines)
- 始终允许 (Always Allowed)：读取指定来源的数据、提取分析字段、在 /workspace 写入本地草稿文件、更新本岗位 Library 下的专属 Page。
- 凭据与 Vault Hint 匹配规则 (Vault & 1Password Policy)：当需要登录或结账填充时，严格按系统优先级调用，且仅允许匹配 Vault 中 Hint 标签为 "[例如：Use for work travel only]" 的登录项、卡片或收货地址；若需调用 1Password 凭据，必须发起 Brokered Sign-in 等待人类在 1Password App 内逐次批准。
- 必须报批 (Needs Approval)：向任何外部账号发送消息、提交工单、修改线上生产系统状态、涉及资金与采购决策。
- 绝不执行 (Never Allowed)：自行决定对外付款、调用 Hint 标签不匹配的 Vault 卡片/账号、越权触碰无关目录、绕过人工审批私自将草稿直接发布。

## 4. 标准作业流程 (Standard Operating Procedure)
- 第 1 步：接收输入并核查数据完整性，若缺少必要字段立即在回复中列出阻塞项。
- 第 2 步：比对既有规则与历史产物，按照既定结构完成分析与草稿编写。
- 第 3 步：自我检查，核对关键数字与原出处链接，标记出必须由人类核决的疑点。
- 第 4 步：输出最终交付物，同步热更新 Library 中的专属 Page 看板，并在末尾清晰说明下一步待办由谁承接。

## 5. 交付物规范与成功指标 (Deliverables & Metrics)
- 输出格式：必须使用固定的 Markdown 表格/结构化卡片，严格包含 [字段 A]、[字段 B] 与 [原始链接]。
- 专属 Page 看板与分享权限：在 Library 中持续维护名为《[看板名称]》的实时 Page（包含时间线、进行中、已完成与待审批四个模块），分享权限固定设置为 [Only you / Your team / Anyone with the link]。
- 成功标准：无捏造事实、无未经核实的数据源、Vault Hint 100% 精准匹配、高风险操作 100% 停留在待审批草稿状态。
```

我们可以对比正反两组实际案例。

正例参考了官方 Haggle Bot 的边界约束（https://x.ai/news/grok-bot-procurement）以及官方 Work 与 Teams 治理规范（https://cursor.com/docs/grok-bot/work；https://cursor.com/docs/grok-bot/teams），比如外联线索审查员与差旅采购专员：

```text
岗位名称：SaaS 采购线索审查员
核心使命：审查公司所有软件续约账单与闲置席位，找出潜在节省空间，生成结构化的议价建议清单。
数据源：仅读取管理后台导出的 CSV 报表、采购合同存档以及发往 procurement+invoices@mail.grokbot.com 的账单邮件，不采信非官方渠道的口头报价。
权限三档：
1. 始终允许：计算闲置率、标记 90 天未登录席位、在本地生成节省测算表、热更新 Library 中的《SaaS 续约审计看板》Page。
2. 必须报批：向供应商发起询价邮件、起草改签合同；如需登录供应商门户查账，仅允许调用 Vault 中 Hint 为 "SaaS Billing Read-Only" 的凭据或通过 1Password 逐次授权。
3. 绝不执行：直接点击取消订阅按钮、修改支付信用卡信息、触碰 Vault 中 Hint 为 "Use for work travel only" 或其他非本岗位的卡片。
交付规范：每条发现必须以 TODAY（现状）、SAVE（预计节省金额）、REC（操作建议）、NEXT（下一步谁确认）四段格式输出，且必须附带原合同到期日；同步更新专属 Page 看板，Page 分享权限设为 Your team（仅团队内部可见）。
```

再看反例：

```text
你是一个超级智能采购助手，请帮我盯着公司所有的日常开销。只要发现有贵的东西或者不划算的软件，就立刻帮我跟对方砍价，想尽一切办法替我省钱。每天向我汇报你的战果。
```

这个反例既没限定数据来源，也没给高危操作上锁。Bot 可能会把宣传页的折扣误当成真实合同条款，甚至自作主张直接给供应商发停约沟通邮件。只有把权限红线切成操作性语言，Bot 才能放心交付。

> [!NOTE]
> 📸 **截图位（待补）**：官方采购 Haggle Bot 的权限配置面板与 Profile 说明

## 5.3 先只建一个 · Start With One

新手容易一上来就建十几个 Bot，起各种头衔，想一口气组建管理舰队。

这种做法很容易失控。Grok Bot 团队核心工程师 @poteto（Lauren Tan）在社区里给新手提过忠告（团队成员，https://x.com/poteto/status/2108097362283597916）：**先只建一个** Bot，直到管理复杂度真正变高之前不要盲目拆分。@poteto 建议第一步先在设置里连上常用的真实 App（团队成员，https://x.com/poteto/status/2107830403549831186），比如日历、Slack、工单系统、CRM 和网盘，让这个 Bot 能接触到每天的真实数据源。

象鱼工作流也提过同样的建议（https://xiangyugongzuoliu.com/grokbot-use-cases/）：第一周别搞太复杂，三个角色就到管理上限了——一个总管、一个领域专家、一个可退回修改的质检官。如果一个 Bot 都没调教好，建太多只会陷入来回纠错的泥潭。

什么时候才该拆出第二个 Bot？官方文档总结了五个拆分条件（https://cursor.com/help/grok-bot/bots；https://cursor.com/docs/grok-bot/work）：

一个是业务领域或交付目标完全独立（Goal or area of ownership）。比如客服巡检和代码 Bug 复现，核心指标没有交集。

一个是依赖的底层工具与数据源截然不同（Set of tools and sources）。一个全在内部 CRM 和邮件里看数据，另一个需要终端权限和深度代码库集成，工具集割裂就该物理隔离。

一个是工作风格与交付调性不同（Working style）。对外沟通要严谨温和，内部工程报告要精简、只讲事实数据，混在一个 Bot 上容易口吻混乱。

一个是审批边界与安全红线存在天然落差（Approval boundary）。涉及花钱、改线上数据库或对外发信的高危岗位，必须独立并加人工审批门禁；只读公开数据的岗位可以放开自动化。

一个是周期性排程存在差异（Recurring schedule）。有的按工作日清晨定点巡检，有的靠外部 Webhook 触发或偶尔手动唤醒，调度节奏不同适合独立承载。值得注意的是，对于同一岗位下的细分邮件流（比如同时接收行业简报、发票通知与系统告警），现在无需为了区分触发源而强行拆出多个 Bot——直接利用 v0.71.2 上线的 `+alias` 邮箱子别名（https://x.com/SamSokolin/status/2110496237241667621；https://cursor.com/help/grok-bot/agent-email），在同一个专职 Bot 下用不同后缀绑定不同的 Routine 即可保持架构精简。

分出专岗后，多 Bot 组织形态会演化为总监协调（Chief of Staff）模式。SpaceXAI 团队的 Roman Ugarte 在播客里提到（团队成员，https://www.youtube.com/watch?v=maSdsTLaMuU）：Chief of Staff 模式不是一开始刻意规划出来的，而是内测第二周自然长出来的机制。大家发现有三四个专岗后，自己在不同窗口间来回复制粘贴特别痛苦，于是自发把第一个 Bot 提拔成幕僚长，人只对总监下达大目标，由总监去负责拆解任务、分给具体专家并跟踪进度。在社区实战中，这种架构得到了广泛印证：例如中文创作者 `@CyberAlice3269`（夏哥研究室）搭建了“1 个 CEO Bot + 5 个专职 Bot（情报搜集、选题策划、初稿撰写、审校润色、配图制作）”的自媒体工作室（https://x.com/CyberAlice3269/status/2112098767151468645）；英文创作者 `@milesdeutscher` 在其获 3,100 赞、4,503 书签的深度长推中展示了“1 个主控编排 Bot + 10+ 细分领域 Bot”的 Grok Swarms 蜂群架构（https://x.com/milesdeutscher/status/2113653680834859262；https://x.com/milesdeutscher/status/2113653818651189419）；而 `@melvindvivas` 则让 Chief of Staff Bot 通过维护一张全局 `Activity Dashboard` Page 看板来统一汇总所有下属 Bot 的实时进度与待审批卡片（https://x.com/melvindvivas/status/2113676935956160882）。

多 Bot 协作时，官方群聊（Group Chat）是公开交接的载体（https://cursor.com/help/grok-bot/group-chats；https://cursor.com/docs/grok-bot/teams）。群聊上限是 6 个 Bot。不过群聊不是让它们互相附和聊天，每一条分派出去的任务，在群里必须且只能明确点名唯一一位当前交付负责人。

> [!NOTE]
> 📸 **截图位（待补）**：在群聊中通过 @ 呼叫特定 Bot 进行任务交接

## 5.4 记忆与纠错 · Memory & Corrections

刚建好的 Bot 不可能一上来就完美。很多人容易把没调教好的 Bot 直接挂上定时任务通宵裸跑，第二天醒来额度烧光，还留下一堆错误数据。尤其在切换至 **The X Subscription**（https://cursor.com/help/grok-bot/plans）后，由于 Grok Bot、Grok App 与 Cursor IDE 三端共用同一个周额度池，正如社区用户 `@charlie_pmp` 在复盘中所指出的（https://x.com/charlie_pmp/status/2114214503416271131），未经调教精简就高频挂起的冗余 Routine 是后台静默消耗周额度的头号元凶。

V2EX 用户 @zhuyinan 在对比本地部署的 Hermes 框架与 Grok Bot 时，分享过一套人工培养经验（https://www.v2ex.com/t/1240012）。他总结出了**养 Bot 的三阶段曲线**：

第一阶段是人工带跑期。刚开始 Bot 完成度通常只有 30% 到 40%，漏洞很多。千万别放手让它自动跑，先带它人肉跑 3 到 5 轮。理解偏了、格式错了、事实漏了，当场在对话里揪出来纠偏。

第二阶段是成熟期。持续纠错几轮后，独立完成度能到 70% 左右。它基本记住了核心偏好：报告用几级标题、表格留哪几列、文案坚决不能出现哪些行业词汇。这时候只要花很少时间微调边角细节。

第三阶段才是挂排程。前面的边缘瑕疵修完、不同输入下的测试都能稳定过关，再正式挂 Routine 自动调度，让它在无人值守的深夜或清晨自行运转。把顺序搞反容易失控。

培养和纠错过程中有两个实用技巧。

一个是明确下达记忆口令。纠正错误时别只说“改一下”，要加上一句“记住这条规则”（https://www.v2ex.com/t/1240012）。带明确记忆指令的纠正会被系统存入 Memory 模块，在后续任务中持续生效。

一个是建立严密的回查闭环。社区实践者 Michael Fenech 提出过纠错准则（https://x.com/Michael_Fenech_/status/2106729045878514147）：纠偏（Correction）必须触发源系统核验（source check），最后才允许给出答案（answer）。指出会议时间或账单金额算错时，严禁让它凭空猜，必须命令它重新打开原始日历、重读邮件或重查 CRM 系统。不回查事实依据的直接认错，只是在用第二段幻觉掩盖第一段幻觉。

觉醒AI 团队在媒体工作流实战中也给过工程建议（https://www.jxxy.net/ai/articles/grok-bot-workflow-training/）：别只信口头上的“记下了”，真正重要的业务调性、规则说明和交付标准，要让 Bot 写成 Markdown 文件存到 /workspace/learn/*.md 目录下。规则落盘成实体文件，后续运行能溯源对比，上下文才不会随着对话轮次变多而漂移。与此同时，中文社区深度实践者 `@eze_is_1`（一泽Eze）在其获 351 赞、705 书签的 10 条实战心得长文中特别提醒了**“防臃肿法则”**（https://x.com/eze_is_1/status/2109850538045264151；https://x.com/eze_is_1/status/2109852993982206425）：当你允许 Bot 在日常复盘纠错中自动迭代更新自己的 Skill 或规则文件时，随着时间推移，文件很容易越写越长甚至出现前后矛盾的补丁指令；因此必须定期让 Bot 对自迭代的规则文件执行精简合并与冲突清理，保持 SOP 干净正交。

官方文档在记忆机制上也划出了安全红线（https://cursor.com/help/grok-bot/bots；https://cursor.com/docs/grok-bot/work）：动态变化的事实永远以源系统为准；过时的假设必须在对话或资料页手动删除；涉及权限和安全底线的规则，必须白纸黑字写进 Profile Description，不能依赖动态记忆。

> [!NOTE]
> 📸 **截图位（待补）**：Bot 记忆面板（Memory）中的已学偏好与手动删除入口

## 5.5 模板与分享 · Templates

把一个 Bot 打磨成执行稳定、规则严密的数字员工后，如果想分享给团队伙伴或发到社区，可以用模板（Templates）系统。

官方工程师 Matt Palmer 在指南文档里打过一个比方（https://x.ai/bot/guides/templates-for-grok-bot）：模板是**食谱而非做好的饭菜**（Think recipe, not meal）。别人导入模板时，拿到的是搭建员工的设计蓝图与配方，不是把你本地烧好的实体原样搬走。

正因为是蓝图而非克隆体，分享前必须搞清楚系统到底打包带走了什么，又留下了什么。

模板会打包带走的内容包括（https://x.ai/bot/guides/templates-for-grok-bot；https://cursor.com/help/grok-bot/bots）：身份设定（名字、头像、标签与 Description）、默认排除个人/内部信息后的通用记忆、Skills、Routines，以及插件清单（接收方需要自己重新安装和授权插件）。

模板绝不会带走的内容包括（https://x.ai/bot/guides/templates-for-grok-bot；https://cursor.com/docs/grok-bot/teams）：个人的私有敏感记忆与内部细节、个人云电脑环境与本地工作区磁盘文件、浏览器里保存的网站登录状态与 Cookie、存储在 `Settings → Vault` 或 1Password 中的任何加密机密与卡片、自己编写的私有脚本与非标准工具代码（如自定义 MCP 服务器）、你的电脑与登录态、过往的私聊对话历史。**但要注意**：公开链接会展示 Bot 的身份、Description、Skills 和 Routines，官方明确要求分享前自行删掉 API Key、内部 URL、客户数据——如果你把密钥写进了 Description 或 Skill，它会跟着模板公开出去（https://cursor.com/help/grok-bot/bots）。

分享操作很直观。按现行文档，打开对话顶部的 Share 菜单，选 **Create template**（Matt Palmer 的指南截图里是旧版 Bot 设置右下角的 Share as Template 按钮，9 月 18 日起模板项移到了 Share 菜单（https://x.ai/changelog/bot））。然后选择范围：Enterprise 计划默认“Team-only”（仅团队成员可打开，详见官方团队治理文档 https://cursor.com/docs/grok-bot/teams）；其他账号默认“Public link”（任何拿到链接的人都能打开）。准备好后复制带 x.ai 域名的分享链接（https://cursor.com/help/grok-bot/bots；https://x.ai/bot/guides/templates-for-grok-bot）。

在浏览器中打开链接，能在 x.ai 看到包含角色说明、技能清单和所需插件的预览详情页。点击“Add to Grok Bot”后，客户端会在接收者账号下新建一个纯净的 Bot 副本。使用第三方分享模板受官方第三方 Bot 分享条款管辖（https://x.ai/legal/bot-sharing-terms）。

发布前必须做好防泄密审查。超级峰在粉皮书 field-01 中强调过（https://chaojifeng.me/free-courses/grok/learn/field-01）：按下发布按钮前，把资料当成全网公开的文件逐字通读一遍。仔细排查 Description 和技能草稿里有没有真实大客户名称、内部私有内网域名、个人私人邮箱、本地硬盘绝对路径，或者透露未公开项目的例行任务标题。一旦发现，必须彻底抹除后再发布。

接收方安装模板后也要注意：因为密钥和浏览器登录态被彻底隔离，新落地的 Bot 副本没法直接开跑。如果模板依赖特定业务系统或特定 API Key，接收方必须按岗位说明书要求，在自己客户端里重新完成连接器授权与凭据录入，Bot 才能真正开工。

跨账号复制模板时，依赖的插件、脚本和授权如何提示。

为了直观展示社区如何利用 Templates 机制沉淀高复用度的专职数字员工，我们可以拆解 2026 年 10 月下旬 X 社区涌现的三个标杆级可分享 Bot 模板与元岗位设计：

### 实例 1：`@LisaMAUSA` 的 **Vault Tidy（保险箱去重清理员）** 与 **SceneEdit Video Studio（单镜头局部修补工作室）** 双模板
在 Cursor / Grok Bot 开发者体验副总裁 Lee Robinson（`@leerob`）于 2026 年 10 月 24 日发起的 $100 X Money 真实反馈与最佳用例悬赏主帖（https://x.com/leerob/status/2113792409448714468，获 4,296 赞、985 书签）下，创作者 `@LisaMAUSA` 于 10 月 25 日分享了两个针对 v0.71.2 与 v0.75.5 新特性的高实用度可复用 Bot 模板（https://x.com/LisaMAUSA/status/2114208018388643852）：

1. **Vault Tidy（保险箱整理与去重专员）**：
   - **解决痛点**：许多用户在通过 `Settings → Vault → Import` 批量导入来自 Chrome、Safari、1Password 或 Bitwarden 的 CSV 密码文件（上限 5 MB，https://cursor.com/help/grok-bot/secrets）后，经常会遇到同一个网站存在三四个历史旧账号、过期银行卡与未标注 `Hint` 的混乱条目，导致业务 Bot 在自动填充时选错账号。
   - **模板设计亮点**：`Vault Tidy` 模板内置了一套严密的安全巡检 SOP——它绝不尝试读取或套取任何只写（write-only）密码与卡号明文，而是专门扫描已存条目的站点域名、用户名与明文 `Hint` 标签，自动识别重复登录项、缺失 `Hint` 用途标签的裸条目以及疑似过期的旧条目，并在 `Library` 中生成一份结构化的《Vault 卫生审计清单》Page，指导人类一键归并去重、补全规范化的 `Hint` 标签。
2. **SceneEdit Video Studio（单镜头无损局部修补视频工作室）**：
   - **解决痛点**：自 v0.71.2 引入 Grok Imagine 原生视频生成与代码动效渲染（https://x.com/bot/status/2110566041772617908；https://x.com/bot/status/2110772748805194127）以来，创作者在合成一段 30 秒或 60 秒的多镜头 MP4 短片后，如果只对其中第 3 个镜头的画面或字幕不满意，传统做法往往需要把整条视频推倒重渲，既耗时又白白消耗 The X Subscription 的周额度池。
   - **模板设计亮点**：`SceneEdit Video Studio` 模板将视频生产流拆解为按镜头编号归档的模块化工程（`/workspace/studio/scenes/scene_01.mp4` ... `scene_N.mp4`）。当你对成片中的某一个特定镜头提出修改意见时，该 Bot 仅针对目标单镜头调用 Grok Imagine 或 Remotion 重新生成局部片段，随后使用云电脑内的 FFmpeg 进行毫秒级无损拼接替换，无需重新渲染整支 MP4 视频。

### 实例 2：`@kaelanyiu` 的 **Meta-Evaluator Bot（模型评测与动态指派元 Bot）** 岗位设计
除了面向具体业务的干活型 Bot，社区开发者 `@kaelanyiu`（Kaelan Yiu）在 2026 年 10 月 25 日分享了一种极具前瞻性的“管 Bot 的元 Bot（Meta-Bot）”岗位架构——**Meta-Evaluator Bot（模型评测官）**（https://x.com/kaelanyiu/status/2114213605566742884）：

- **核心设计逻辑**：在多 Bot 协同舰队中，许多重度执行类 Worker Bots 会在云电脑沙箱内通过 CLI 调用不同底层大模型来干活（例如调用本地/云端 CLI Agent 处理代码重构、数据清洗或长文写作）。然而各大前沿模型的版本迭代与性价比变化极快，手动去改每个 Worker Bot 的模型配置既繁琐又主观。
- **自动化优胜劣汰闭环**：`@kaelanyiu` 专门设立了一位定时运行的 **Meta-Evaluator Bot**，挂载每隔几天自动触发一次的 Routine。每次唤醒后，这位“评测官”会自动拉取你真实业务场景下的标准测试集（Benchmark Prompts），对当前主流前沿模型跑一轮盲测打分（综合评估准确率、耗时与成本），随后直接根据最新跑分结果，**动态修改 `/workspace` 下其他干活 Worker Bots 在未来几天内通过 CLI 调用的默认模型配置文件**，并将本轮评测排行榜同步更新到 `Library` 的专属 Page 看板上。如果您希望把这一岗位直接导入自己的团队，可以参考以下可直接复用的模板蓝图：

```text
# 岗位说明书：Meta-Evaluator Bot（模型评测与动态路由官）

## 1. 身份与使命 (Identity & Mission)
- 岗位身份：你是团队内部的 AI 模型基准评测官与 CLI 模型路由调度员（参考 @kaelanyiu 架构范式）。
- 核心使命：每隔 72 小时对候选大模型运行一次真实业务基准测试，根据综合得分动态更新其他 Worker Bots 的 CLI 模型配置文件，确保全队始终使用当前性价比与准确率最优的模型组合。

## 2. 数据来源与工位 (Systems & Sources)
- 权威输入源：读取 `/workspace/eval/benchmarks/` 下的黄金测试集与评分标准，以及各模型官方发布日志。
- 配置文件目录：具备 `/workspace/config/worker_models.json` 的读写权限（供其他 Worker Bots 在 CLI 启动时读取）。

## 3. 权限红线与审批边界 (Permission Lines)
- 始终允许：运行 `/workspace/eval/run_eval.py < /dev/null` 非交互式评测脚本、统计延迟与得分、更新 Library 中的《模型跑分与路由看板》Page。
- 必须报批：当单次评测预估消耗超过预设 Credits 阈值，或拟将核心生产 Worker Bot 切换至未经历史验证的新发布模型家族时，必须先在聊天流发起审批卡片。
- 绝不执行：修改 Worker Bots 的核心业务安全红线（Profile Description）或触碰 Vault 中的任何支付与个人凭据。

## 4. 标准作业流程 (Standard Operating Procedure)
- 第 1 步：按 Routine 定时唤醒，读取黄金测试集（涵盖代码修复、结构化提取、双语文案三类任务）。
- 第 2 步：通过 CLI 批量执行评测（命令末尾强制追加 `< /dev/null` 防止非交互式 Shell 挂起），记录各候选模型的得分、耗时与 Token 消耗。
- 第 3 步：生成本周期最优模型映射表，写入 `/workspace/config/worker_models.json`。
- 第 4 步：热更新 Library 中的专属 Page（权限设为 Your team），并在对话流输出变更摘要。
```

> [!NOTE]
> 📸 **截图位（待补）**：Share as Template 预览详情页（显示包含的 Memory、Skills 与 Plugins 清单）

---

[← 上一章：§04 你的第一个任务 · Your First Task](../part1-getting-started/04-first-task.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§06 云电脑：它的工位 · The Computer →](../part2-core-concepts/06-computer.md)

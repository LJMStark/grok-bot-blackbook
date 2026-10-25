# §07 Skill 与 Routine：教一次，让它照着做 · Skills & Routines

[← 上一章：§06 云电脑：它的工位 · The Computer](../part2-core-concepts/06-computer.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§08 审批与安全边界 · Approvals & Safety →](../part2-core-concepts/08-approvals-safety.md)

---

很多新手刚接触 Grok Bot，容易把它当普通网页聊天框用。每次想干活，都重新敲一遍提示词，输出格式次次参差不齐。还有人把随手写的提示词直接挂成定时任务，跑了几天，额度烧掉一大截，收件箱里全是毫无价值的垃圾信息。

想让 Bot 真正变成可靠的数字同事，得搞懂它的两层自动化构件：Skill 和 Routine。假设你翻完文档和社区讨论就会明白，教它做事和让它定时跑，在底层是两套完全不同的逻辑。

## 7.1 两者的区别 · How vs When

按官方文档的架构设计，**Skill 是解决怎么做（How）的方法库，而 Routine 是规定何时由谁来跑（When）的排期表**（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。很多人容易把这两个概念搞混。

Skill 是一套可复用的操作指令集。它记录了具体任务的步骤、分支判断、交付格式以及安全审批红线。你教出来的 Skill 不属于某一个具体的 Bot，而是保存在整个账户的私有技能库里。你在 Bot A 这里保存的技能，只要挂载了对应的连接器或网页登录态，Bot B 也能直接调。在桌面客户端输入框里，按 `/` 键就能检索并插入已存的 Skill；按 `@` 键用来找具体的 Bot、群聊、Routine 或连接器（https://cursor.com/help/grok-bot/skills-routines-and-automations）。（时效提醒：10 月 7 日 v0.68.1 起 `/` 不再弹出技能菜单，可以直接用文字点名 Skill，见 §03（https://x.ai/changelog/bot）。）要是快捷菜单里没看到某个 Skill，可以去侧边栏的 Marketplace，进插件和技能管理页面，看它在不在 Private skills 列表里（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

Routine 是一张具体的排期委派单。它必须绑定一个明确的负责 Bot，还要设定执行时间表或事件触发源（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。一个 Routine 本质上就是对 Bot 说：在指定时刻，调某项 Skill 去处理当前数据，再把结果推到指定位置。

![Skill 与 Routine 的职责边界与调用关系](../../images/fig-07-1.png)

*图：Skill 与 Routine 的职责边界与调用关系*

早期社区里 Kin 的《Grok Bot 橙皮书》有句口号叫“示范一遍它学一辈子”（https://github.com/KinGao294/grok-bot-orange-book）。这句宣传语把不少新手带偏了，以为让 AI 看一次屏幕动作就能应付真实世界的所有变化。官方文档专门纠偏过：演示录制生成的产物只是一份“草稿技能（draft skill）”（https://cursor.com/help/grok-bot/skills-routines-and-automations）。拿到初稿后，必须手动补充判断规则、容错策略和审批卡点，并在安全数据上跑通测试，才能交给 Routine 定期跑（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

## 7.2 Teach a task 录制 · Teach by Demo

要是网页操作步骤太繁琐，逐字写提示词得敲上千字，这时候可以用电脑视图里的 Teach a task 功能（https://cursor.com/help/grok-bot/skills-routines-and-automations）。这功能不是让你当甩手掌柜，而是靠录屏快速抓取一套技能骨架。

录制步骤很直接。在桌面端打开单聊窗口，切到云电脑屏幕视图，点击 Teach a task（https://cursor.com/help/grok-bot/skills-routines-and-automations）。系统会先让你用文字写明目标，接着你在云电脑浏览器里把业务完整操作一遍（https://cursor.com/help/grok-bot/skills-routines-and-automations）。演示完点击停止，Bot 就会根据屏幕动作，自动整理出一份草稿 Skill（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

这里有两条死规则。第一，单次录制最多 10 分钟（https://cursor.com/help/grok-bot/skills-routines-and-automations），超时自动截断。第二，录制只看屏幕画面，完全不录麦克风声音（https://cursor.com/help/grok-bot/skills-routines-and-automations），不用对着电脑自言自语。在官方 101 直播里，讲师演示了让 Bot 学会搭建 Google 表单并发布。官方强调，把演示固化成技能核心是为了省 token（tokenomics），省得 Bot 每次执行类似任务都在原始 HTML 页面里盲目试错（https://www.youtube.com/watch?v=8xXhE25vJZY 与 https://cursor.com/help/grok-bot/skills-routines-and-automations）。

假设你细读官方规范就会发现，安全是录制时必须卡死的底线。屏幕画面会被模型逐帧读取并写入技能说明，绝对不能在录屏期间明文输入密码、二次验证码或银行卡号（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/secrets）。遇到敏感凭据，必须走系统的凭据交接流程（https://cursor.com/help/grok-bot/skills-routines-and-automations），例如通过 v0.75.2 上线的 1Password Brokered Sign-in 逐次授权（https://cursor.com/help/grok-bot/connect-apps）或 v0.75.5 上线的内置 Grok Bot Vault 安全填充（https://cursor.com/help/grok-bot/secrets）。

> [!NOTE]
> 📸 **截图位（待补）**：Teach a task 录制界面与生成的草稿技能面板

社区有人试过对同一个流程连录 3 次让 Bot 取平均值（https://x.com/B_doong2daddy/status/2100573792569303402），但官方没支持过这种做法（https://cursor.com/help/grok-bot/skills-routines-and-automations），效果也没经验证。核心问题在于，**录制生成的技能永远只是一份未经打磨的初稿**（https://cursor.com/help/grok-bot/skills-routines-and-automations）。演示走的只是理想路径，真实环境里经常遇到加载超时、弹窗拦截或空数据。拿草稿直接去排期，一旦撞上预期外的变化，Bot 很容易卡死或乱点。

另外，Teach a task 属于分批灰度功能（https://cursor.com/help/grok-bot/skills-routines-and-automations）。要是你的电脑视图里还没这个按钮，不用慌。直接指挥 Bot 手动跑通一次单次任务，然后在对话里让它把刚才成功的流程、数据源和格式规则提取保存为私有技能（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

录制中出现误操作时，生成的 Skill 草稿是否会保留无效步骤。

## 7.3 从一次任务到 Routine 的六步 · Task → Fix → Skill → Test → Routine

不少人抱怨 Bot 经常失控，根子就在于跳过了中间的质检环节。社区实践者总结过一句话：**绝不能直接从随手写的一句提示词直接跳到例行排期（Prompt → Routine）**（https://x.com/Michael_Fenech_/status/2106352565528977469）。官方核心团队接受采访时也强调，正确的路线永远是先看单次任务，再沉淀成技能，建立了信任最后才做自动化排期（https://www.youtube.com/watch?v=xZ5TEaleUdg 与 https://cursor.com/help/grok-bot/routines）。

按官方工作流指南（https://cursor.com/docs/grok-bot/work）和社区经验（https://x.com/Michael_Fenech_/status/2106352565528977469），搞定一条稳固的例行工作流要走完六步：

1. 手动跑通单次真实任务（Task）。拿当下的真数据当输入，别捏造假例子。在对话框里一步步发指令，确认 Bot 具备任务所需的网页权限、登录态或插件连接（https://x.com/Michael_Fenech_/status/2106352565528977469）。
2. 现场纠偏（Fix）。单次跑几乎总会暴露出问题，比如抓了旧数据、漏了字段，或者输出冗长套话。在这个阶段改指令、对标准、调格式，直到它能稳定产出满意的结果（https://x.com/Michael_Fenech_/status/2106352565528977469）。
3. 存为技能（Skill）。对完成任务的 Bot 说：“把我们刚刚使用的流程保存为名为 [技能名称] 的技能”。在提示词里列清楚触发场景、依赖数据源、操作步骤、校验方法，以及必须人工审批的边界（https://cursor.com/help/grok-bot/skills-routines-and-automations）。
4. 换第二份真数据测试（Test a second input）。这一步最容易刷掉劣质技能。只在一个特定输入上跑通就急着封装，存下来的只是针对单次历史的作弊条（https://x.com/Michael_Fenech_/status/2106352565528977469）。换一组参数或不同日期的输入再跑一次，确保流程稳定。
5. 定义失败策略（Define failure）。把异常处理写死在指令里：数据源连不上怎么办？没查到新数据怎么办？中间某步失败是直接终止还是汇报部分进度？涉及对外发送、删数据或付款的操作，有没有锁进审批卡（https://cursor.com/help/grok-bot/skills-routines-and-automations）？
6. 绑定排期并用测试运行复核（Routine & Test run）。在负责该任务的 Bot 对话框里，设好时区、排期频次与执行规则，启用后仔细对一遍历史记录（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。

![从单次任务演进到稳定 Routine 的六步闭环](../../images/fig-07-2.png)

*图：从单次任务演进到稳定 Routine 的六步闭环*

看社区里 Rowan Cheung 分享的日常监控工作流（https://x.com/rowancheung/status/2108328114552000842），以及 `@milesdeutscher`（Miles Deutscher）在 3,100 赞、4,503 书签的“10 大逆天 Grok Bot 用例”长推中拆解的 **Competitor Monitor（竞品全天候雷达）** 与 **Morning Brief Routine（全渠道晨间情报简报）**（[https://x.com/milesdeutscher/status/2113653680834859262](https://x.com/milesdeutscher/status/2113653680834859262)、[https://x.com/milesdeutscher/status/2113653726217195817](https://x.com/milesdeutscher/status/2113653726217195817)、[https://x.com/milesdeutscher/status/2113653803304296498](https://x.com/milesdeutscher/status/2113653803304296498)），一条及格的 Routine 提示词在结构上必须严密闭环，时间、时区、数据范围、过滤规则、输出格式、禁止项和失败处理都得写全。这是一份可以直接参考的模板：

```text
Every weekday at 9:00 AM in Asia/Shanghai time zone, run the Competitor Product Updates skill against our target list in /workspace/competitors.md.

Look back strictly within the last 24 hours. Catch only three categories of updates:
1. Pricing or plan structure changes.
2. New feature launches or deprecations.
3. Outages, security incidents, or policy updates.

Ignore routine marketing campaigns, hype threads, promotional discounts, and generic reposts. 
Return at most 5 items. For each item, provide:
- Competitor name
- Change category
- Direct source URL
- One-sentence neutral summary of what changed
- Potential impact on our product (High, Medium, Low)

Post the summary directly in this conversation. 
Never post, comment, send email, or contact anyone externally. 
If the source data cannot be retrieved or the network fails, post an explicit error notification stating which source failed, and stop immediately. Never use outdated cache or hallucinate placeholder data. 
If no qualifying updates occurred in the last 24 hours, post exactly one line: "No qualifying competitor updates in the last 24 hours."

Save this as a routine.
```

### 进阶维护法则：防止自迭代 Skill 臃肿自相矛盾与路由熔断

当你的 Skill 库和 Routine 跑过几周之后，往往会遇到两个隐蔽的工程陷阱：**Skill 自我膨胀**与**异常死循环重试**。

中文社区创作者 `@eze_is_1`（一泽Eze）在收获 351 赞、705 书签的万字实战总结帖中，重点提出了 **“防止自迭代 Skill 臃肿与自相矛盾”** 的维护法则（[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151) 及系列进阶帖 [https://x.com/eze_is_1/status/2109852993982206425](https://x.com/eze_is_1/status/2109852993982206425)、[https://x.com/eze_is_1/status/2110532874000879886](https://x.com/eze_is_1/status/2110532874000879886)）。很多深度用户喜欢在提示词末尾加一句“每次执行完毕后，把遇到的新问题和经验自动追加写进 Skill 文件实现自我进化”。`@eze_is_1` 指出，如果不加人工约束地放任 Bot 自迭代更新 Skill，不出半个月，原本几百字的清爽 SOP 就会像滚雪球一样膨胀到几千字，里面塞满针对某次偶发网络抖动的临时补丁，甚至出现第 3 条规则要求“精简输出不超 100 字”、第 18 条补丁却要求“完整列出所有原始 JSON 字段”的自相矛盾指令，导致模型推理注意力涣散、执行稳定性断崖式下跌。

与此同时，`@AIShovelLab` 在梳理 Grok Bot 与 Claude Code / Codex 六大核心联动范式时，特别强调了 **“用路由 Skill 阻止盲目重试”** 的实战技巧（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）。当 Bot 在执行 Routine 遇到反爬拦截、接口 403 或 CLI 命令报错时，默认本能往往是在同一个会话里反复换姿势重试 5 到 10 次，不仅单次运行就把周额度烧出大窟窿，还可能触发目标站点的封号风控。通过在顶层挂载一个专门的“路由与熔断 Skill（Router & Circuit-Breaker Skill）”，强制规定每类任务的首选通道、降级备选通道以及“同源错误最多重试 1 次即熔断挂起”的硬规则，就能彻底根治盲目重试。

你可以把下面这份融合了 `@eze_is_1` 防臃肿压缩规则与 `@AIShovelLab` 路由熔断机制的治理模板直接写进你的核心 Skill 中：

```markdown
# Skill 治理与路由熔断规范 (Router & Anti-Bloat Guardrails)

## 1. 任务路由与重试熔断规则（参考 @AIShovelLab 范式）
- **优先确定性通道**：能用云电脑本地 Python/Bash 脚本或官方连接器（MCP）解决的数据读取，严禁拉起完整云端 GUI 浏览器去翻页。
- **单次重试熔断（Max Retry = 1）**：
  - 遇到 HTTP 401/403/429、验证码拦截（Captcha）或登录态失效时，**严禁在原通道连续重试超过 1 次**。
  - 若开启本机住宅 IP 转发（`Route traffic through this computer`）后仍失败，立即中止当前 Routine，输出一行结构化故障原因并挂起等待人工介入。

## 2. 自迭代 Skill 防臃肿与冲突清理法则（参考 @eze_is_1 范式）
- **禁止无脑追加（No Blind Append）**：当需要把新踩坑经验更新进本 Skill 时，严禁直接在文件末尾机械追加 `Patch #N` 段落。
- **同位替换与合并**：新规则必须合并进既有的步骤章节中；若新规则与旧规则冲突，必须直接覆写删除旧表述，确保整份 Skill 内部零逻辑矛盾。
- **行数硬上限（Max 120 Lines）**：本 Skill 正文总行数严格控制在 120 行以内。每新增 1 条规则，必须审视并精简掉过时的冗余描述，保持 SOP 正交干净。
```

此外，自 v0.75.2 上线 **Pages（Canvas）** 实时交互文档与看板能力后（https://x.ai/changelog/bot 与 [https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)），Routine 的最终交付物不再局限于往聊天窗口发一条死板的消息。例如社区开发者 `@melvindvivas`（Melvin Vivas）为其 Chief of Staff（幕僚长）Bot 配置了一条定时自动刷新 Routine，每隔固定周期巡检麾下所有专职 Bot 的工作进度，并自动热更新一张名为 `Grok Bot Activity Dashboard` 的实时 Page 看板（涵盖时间线视图、进行中任务、已完成任务与待人工审批事项）（[https://x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882) 与 [https://x.com/melvindvivas/status/2113968491573514576](https://x.com/melvindvivas/status/2113968491573514576)）。而 `@sisiliu517` 则利用小时级 Routine 配合中美时差策略——白天时段自动主攻中文 X 圈层互动与发帖，夜间时段自动切换为英文 X 圈层运营，并在每晚自动汇总互动分析报告反哺次日选题（[https://x.com/sisiliu517/status/2110869965612183642](https://x.com/sisiliu517/status/2110869965612183642)）。

## 7.4 硬限制 · Limits

搭 Routine 前，官方设下的硬限制要先摸清（https://cursor.com/help/grok-bot/routines），不然任务容易莫名中断，甚至丢数据。

每个 Bot 最多建 50 个 Routine（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。一个 Bot 的任务数量要是逼近上限，说明职责没拆开，得按业务线新开专职 Bot（https://x.com/Michael_Fenech_/status/2105697750645977298）。

在运行频率配额上，2026 年 10 月 22 日发布的 **v0.75.2 版本**对小时级运行频率上限做了重大上调（https://x.ai/changelog/bot）。根据官方最新 Routines 文档标准（https://cursor.com/help/grok-bot/routines），当前的小时级触发与运行硬上限为：
- **全账号所有 Bot 合计最高 300 次/小时（300 runs per hour across all Bots）**；
- **单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**。

这一配额提升主要是为了支撑高频 Webhook 事件触发、邮件子别名分流以及多 Bot 团队并发协作场景（https://cursor.com/help/grok-bot/routines）。但需要注意，对于按固定时间表循环的定时排期（Scheduled Routines），触发间隔依然至少要 5 分钟（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines），系统不支持低于 5 分钟的高频定时轮询。轮询太密只会白白耗尽周额度，还给目标服务器造成不必要的压力。

系统对运行历史很克制。每个 Routine 只保留最近 20 条运行记录（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。遇到连续报错，早期的记录很快就会被顶掉。要想做长期复盘，必须在 Skill 里让 Bot 把产出写进云电脑本地文件，或者持续写入一张固定沉淀在右侧信息栏 `Library` 里的 Page 看板中（https://x.ai/changelog/bot），别指望界面的日志面板。

在面板里点删除 Routine 是立即生效的，没有撤销（undo）功能（https://cursor.com/help/grok-bot/skills-routines-and-automations）。更要注意的是，在主界面直接删掉某个 Bot，它名下的所有 Routine 会一起被清空（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

很多新手刚建好 Routine，顺手就点 Test run 想试试水，以为这只是沙盒演练。官方文档特意警告过：**测试运行会产生真实的网页点击、文件改动和接口调用，绝对不是无害的沙盒模拟**（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。如果流程里有发消息、改生产文件或付款的操作，又没配审批卡，一点 Test run 就会直接把操作打到外部生产环境里。

为了防止用户离线时后台空转烧额度，系统有无人值守防护。长时间没动客户端，Grok Bot 可能会弹窗问你要不要继续维持后台任务；如果在设定时间内没回复，系统会自动暂停这些 Routine（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。重新打开客户端时，记得去 Bot 详情页看一眼有没有被暂停的任务，手动点恢复。

> [!NOTE]
> 📸 **截图位（待补）**：Bot 的 Routines 管理面板与运行历史记录

另外，按官方安全规则，Routine 或后台任务发起的审批卡片，等大概 10 分钟没人理就会变 Expired（已过期），操作直接作废（https://cursor.com/help/grok-bot/approvals-security-and-privacy 与 https://cursor.com/docs/grok-bot/security）。合上笔记本电脑，云电脑上的排期照样在云端跑（https://cursor.com/help/grok-bot/faqs），但关键步骤卡在审批上、你 10 分钟内没点通过，整个任务链就会停在那里。（注：v0.75.2 优化了 Auto-review 审批逻辑，对用户在当前对话轮次中已明确下令执行的操作大幅精简了冗余的二次确认弹窗，但后台无人值守 Routine 涉及高风险外发或资金操作时依然严格遵循审批卡机制，详见 https://x.ai/changelog/bot。）

| 限制维度 | 官方最新硬指标（截至 v0.75.5） | 架构师应对策略与避坑要点 | 官方文档依据 |
| :--- | :--- | :--- | :--- |
| **单 Bot Routine 数量上限** | 最多 **50 条** / Bot | 按业务职能拆分专职 Bot，避免把所有排期堆在同一个默认 Bot 名下 | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **全账号小时级运行上限** | 全账号所有 Bot 合计 **300 次/小时**（v0.75.2 上调） | 严控宽泛事件监听器，用条件过滤与脚本预检拦截无效触发 | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **单条 Routine 小时级上限** | 单条 Routine 最高 **200 次/小时**（v0.75.2 上调） | 针对高频 Webhook 或邮件触发做好去重与合并批处理 | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **定时排期最小间隔** | 最短 **5 分钟** | 长耗时异步任务改用完成时 Webhook 唤醒，切勿用 5 分钟定时轮询盯进度 | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **运行历史保留条数** | 最近 **20 条**记录 | 在 Skill 中强制把每次运行日志追加写入 `/workspace/logs/` 或更新至 Page | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **审批卡片有效窗口** | 约 **10 分钟**未响应即 `Expired` | 将需要人工审批的汇总动作集中在固定办公时段推送，配合手机端 Deep-link 通知秒批 | [Security 文档](https://cursor.com/docs/grok-bot/security) |

## 7.5 事件触发 · Event Triggers

除了按时间表跑，Grok Bot 还能靠外部事件触发（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。通过 Cursor 账户集成的连接渠道，外部系统有变动时能唤醒 Bot，比如收到某条特定 Slack 消息或 GitHub 仓库通知（https://cursor.com/help/grok-bot/skills-routines-and-automations）。changelog 里还能看到 Microsoft Teams 消息、Linear 工单、Sentry 告警、PagerDuty 事件触发（8/12），以及带独立 URL 和密钥的 Webhook 触发（v0.21.0，8/19）（https://x.ai/changelog/bot）。这些触发源大多是海外团队协作工具；国内读者如果不用它们，定时 Routine 就够用。这种事件驱动要单独授权连接，跟普通第三方插件不太一样（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/connect-apps）。

配事件触发器最容易踩坑的，是监听条件设得太宽。官方文档专门提过：**永远不要配置诸如监听每一条新消息这类宽泛触发器**（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。

![狭窄事件触发器与宽泛监听器的运行成本对比](../../images/fig-07-3.png)

*图：狭窄事件触发器与宽泛监听器的运行成本对比*

如果把 Bot 挂在活跃的 Slack 频道里听所有新消息，大家闲聊、发表情包甚至系统机器人推送，都会频繁唤醒 Bot。每次唤醒都要调大模型过一遍上下文，不仅疯狂烧额度，还会塞满上下文噪音，甚至让 Bot 在别人闲聊时误触发动作（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

合格的事件触发器，条件必须卡得很窄（https://cursor.com/help/grok-bot/skills-routines-and-automations）。官方给的范例是同时盯频道、格式和关键词：“当 `#customer-escalations` 频道的消息同时带有工单链接和 ‘needs repro’ 时，才在预发环境复现问题并输出报告”（https://cursor.com/help/grok-bot/skills-routines-and-automations）。就算触发成功，像写回 Slack 或在 GitHub 开 PR 这种操作，指令里也必须卡死人工审批，绝不能让它自己静默搞定（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

### v0.71.2 重磅杀手锏：专属邮箱 `+alias` 加号子别名定向触发 Routine

在 2026 年 10 月 14 日发布的 **v0.71.2 版本**中，Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）正式宣布了一项改变邮件事件触发格局的核心特性（[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)，获 3,073 赞、1,197 书签；详见官方 Agent Email 文档 https://cursor.com/help/grok-bot/agent-email 与官方 Changelog https://x.ai/changelog/bot）：**每个 Bot 的 `@mail.grokbot.com` 专属邮箱现已原生支持 `+alias` 加号子别名，并且支持配置“仅当邮件发送到指定 `+alias` 子别名时才定向触发对应的 Routine”！**

在此之前，如果你给 Bot 配置了“收到新邮件时触发 Routine”，任何发往 `mybot@mail.grokbot.com` 的广告邮件、验证码或系统通知都会无差别唤醒该 Routine。而现在，假设你的 Bot 基础邮箱是 `mybot@mail.grokbot.com`，你无需做任何额外注册，就可以直接在外部网站或转发规则中使用无限个加号子别名（https://cursor.com/help/grok-bot/agent-email）：
- `mybot+newsletters@mail.grokbot.com`：专门用于订阅全网行业 Newsletter 与Substack 专栏；
- `mybot+invoices@mail.grokbot.com`：专门用于接收 AWS、SaaS 订阅账单与电子发票（配合 v0.75.2 新增的**邮件原样转发保留完整 HTML、内嵌图片与文件附件**能力，Bot 验票后可直接将带 PDF 附件的原始账单原封不动转发给公司财务邮箱，详见 https://cursor.com/help/grok-bot/agent-email 与 https://x.ai/changelog/bot）；
- `mybot+alerts@mail.grokbot.com`：专门用于接收服务器监控告警或电商物流变动通知。

社区用户 `@songsong275452`（引用 `@gokul_i` 的实战方案）展示了这一特性的经典用法（[https://x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371)）：将原本塞满个人主邮箱的所有 AI 与科技 Newsletters 统统改订到 Bot 专属的 `+newsletters` 邮箱中，让个人收件箱彻底恢复清净；同时配置两条完美配合的 Routine——一条基于 `+newsletters` 邮件触发器将每封新到的通讯静默归档到云电脑的 `/workspace/newsletters/` 目录，另一条在每周六上午定时运行，将过去一周积攒的所有长文提炼成一份高密度精华周报或交互式 Page 简报。`@AIShovelLab` 也将“`+alias` 邮箱后缀精准触发 Routine”列为当前最值得复用的六大高效自动化范式之一（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）。

下面是一份可直接复制使用的 **`+alias` 定向邮件触发与周六汇总双 Routine 配置指令**：

```text
请帮我配置两条基于专属邮箱 +alias 子别名的协同 Routine：

【Routine 1：+invoices 账单实时解析与原样转发（事件触发）】
- 触发条件（Trigger）：仅当收到发往 mybot+invoices@mail.grokbot.com 的新邮件时触发（忽略发往主邮箱或其他 +alias 的邮件）。
- 执行动作：
  1. 提取邮件正文与 PDF 附件中的商户名称、扣款金额、币种、账单周期与发票号，追加写入 /workspace/finance/2026-invoices.csv。
  2. 若单笔账单金额超过 $100，在当前对话发送高优提醒。
  3. 使用 v0.75.2 原样转发功能（保留完整 HTML、内嵌图片与原始 PDF 附件），将该邮件起草转发给 finance@mycompany.com，并挂起审批卡等我确认后发送。

【Routine 2：+newsletters 周六深度研报汇总（定时触发）】
- 日常归档规则：凡发往 mybot+newsletters@mail.grokbot.com 的邮件，平时收到时不生成聊天打扰通知，直接将正文静默归档保存至 /workspace/newsletters/inbox/。
- 触发条件（Trigger）：每周六上午 10:00（Asia/Shanghai 时区）运行。
- 执行动作：
  1. 读取 /workspace/newsletters/inbox/ 下过去 7 天新增的所有通讯文章。
  2. 按“底层模型进展”、“Agent 工程实践”、“商业化与投融资”三个维度去重聚类，更新到我的《每周 AI 核心情报》Page 看板中。
  3. 归档已处理的文章至 /workspace/newsletters/archive/。
```

### 长耗时任务完成 Webhook 精准唤醒：告别定时轮询空转

除了外部 SaaS 事件与邮件别名触发，Webhook 触发器在**云电脑内部长耗时任务协同**上还有一个极其省额度的妙用。

许多开发者会在 Grok Bot 的云电脑（cloud box）内部安装 Codex CLI 或运行耗时数十分钟的大规模数据抓取与模型编译任务。如果配置一条每 5 分钟跑一次的定时 Routine 去检查任务跑完没有，在等待期间会白白浪费十几次大模型上下文唤醒额度。社区开发者 `@AbhisheKumarA7`（Abhishek Kumar）分享了一套“**长任务完成时 Webhook 唤醒（Wake on Done via Webhook）**”的零轮询架构（[https://x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578)），`@eze_is_1` 也在长耗时任务防休眠指南中重点剖析了这一机制（[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151)）：
1. 为负责验收的 Grok Bot 创建一条 **Webhook 触发型 Routine**，获取专属 Webhook URL 与密钥（https://cursor.com/help/grok-bot/routines）；
2. 在云电脑后台启动 Codex CLI 或长耗时构建脚本时，在命令末尾追加一段完成后自动回调该 Webhook 的钩子；
3. 在漫长的执行过程中，Grok Bot 完全处于静默零消耗状态（zero polling token waste）；直到后台任务真正跑完的瞬间，脚本才发送一次 HTTP 请求精准唤醒 Grok Bot 进场验收成果并推送到你的手机上。

如果你在从外部脚本或本地 Claude Code 向云端 Grok Bot 推送复杂 JSON 载荷时，遇到 Webhook 严格校验格式导致的 `HTTP 400` 报错，还可以参考中文社区开发者 `@mikan77_aoi`（橘子🍊）验证过的零守护进程排错方案（[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）：无需依赖复杂的第三方框架，直接用 Python 标准库（`urllib.request`）编写一个轻量级桥接脚本，将易引发转义冲突的复杂长文本先写入共享工作区文件或精简为标准键值对，通过 4 次干净的 API 握手调用即可实现 100% 稳定的跨端唤醒与任务交接：

```bash
# 示例：在云电脑后台运行长耗时 Codex 构建任务，仅在跑完瞬间通过 Webhook 零轮询唤醒 Grok Bot（参考 @AbhisheKumarA7 范式）
nohup bash -c '
  codex exec "重构并跑通 /workspace/app 下的全部集成测试" > /workspace/logs/codex_build.log 2>&1
  EXIT_CODE=$?
  python3 -c "
import json, urllib.request
payload = json.dumps({\"event\": \"codex_task_done\", \"exit_code\": $EXIT_CODE, \"log_path\": \"/workspace/logs/codex_build.log\"}).encode(\"utf-8\")
req = urllib.request.Request(
    \"https://api.cursor.com/v1/grok-bot/webhooks/YOUR_ROUTINE_WEBHOOK_ID\",
    data=payload,
    headers={\"Content-Type\": \"application/json\", \"Authorization\": \"Bearer YOUR_WEBHOOK_SECRET\"},
    method=\"POST\"
)
urllib.request.urlopen(req, timeout=10)
"
' >/dev/null 2>&1 &
```

## 7.6 Routine 审计 · Audit

社区里有句话：“在 Grok Bot 体系里，Routine 才是真正的产品，而不是那个 Bot 头像”（https://x.com/i/status/2109516426767654962）。但新鲜劲一过，很多人搭的 Routine 慢慢全变成了信息垃圾。

有行业观察者提过：别把“搭了复杂的流程”当成“创造了真实的业务价值”（https://www.youtube.com/watch?v=LM7Ft7g8qJw）。每天早晨推过来的行业日报、数据摘要或竞品清单，要是连续一个月都没改变过你的任何业务决策，那它根本没必要存在。

再算一笔成本账。社区开发者按 API 价格估算过（不是订阅的实际扣费）：每 5 分钟跑一次的 Routine，一个月会在后台跑 8,640 次（https://x.com/fleyta88/status/2109346840382415019）。要是有 95% 的时候源数据根本没变，Bot 每次还去啃一遍完整页面和长上下文，额度就全打水漂了（https://x.com/fleyta88/status/2109346840382415019）。

### The X Subscription 三合一共享额度池下的头号隐形杀手

自 2026 年 10 月 18 日 Grok Bot 正式并入 **The X Subscription** 三合一统一订阅体系后（官方公告 [https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)，详见官方计费文档 https://cursor.com/help/grok-bot/plans 与 https://cursor.com/help/the-x-subscription/overview），Routine 审计的重要性上升到了前所未有的高度。

中文社区实践者 `@charlie_pmp`（Charlie）一针见血地指出，很多用户升级到 The X Subscription（无论是 $30/月的 Premium、$100/月的 Super 还是 $200/月的 Ultra 档位）后，突然感觉周额度进度条掉电速度明显变快，背后的头号元凶正是**“三端共用同一个周额度池 + 后台静默空转的高频冗余 Routine”**（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）：
1. **三合一共享周额度池（One Weekly Usage Pool）**：在官方 The X Subscription 规则下，你在桌面/手机上跑的 **Grok Bot**、日常对话搜索用的 **Grok**，以及写代码用的 **Cursor IDE**，三者现在从**同一个每周重置的额度池**里抽水（https://cursor.com/help/grok-bot/plans）。一旦后台的冗余 Routine 在夜里偷偷把周额度池跑干，不仅你的 Bot 会停摆或开始扣减 `grok.com/dashboard/billing` 里的 **Prepaid Credits（预付充值额度）**，连你白天打开 Cursor 写代码都会直接受到牵连（https://cursor.com/help/grok-bot/plans）！
2. **用“确定性脚本轮询”替代“大模型浏览器轮询”**：要想既保留高频监控的敏捷度、又不消耗宝贵的周额度池，最硬核的解法是本书作者 Mr.鼓先生（`@StarkLJM`）实测跑通的 **“AI 写确定性脚本，脚本跑日常轮询”零额度抓榜范式**（[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377) 与 [https://x.com/starkljm/status/2112818533797343312](https://x.com/starkljm/status/2112818533797343312)）。针对每天需要定时抓取榜单或监控页面变动的任务，不要让 Routine 每次都调用大模型开浏览器读网页，而是先花 **28.6 秒**让 Agent 写好一套带严格字段校验（缺失字段立即告警、无评分严格存 `null` 而非用 `0` 污染均值）的 Python 爬虫脚本；日常巡检全部交由脚本在 **1.99 秒**内确定性跑完，日常轮询消耗 **0 模型额度（zero model tokens）**，只有当脚本检测到实质性异动时才唤醒大模型做深度分析。或者如 `@hppzyy` 分享的方案（[https://x.com/hppzyy/status/2111573227881529454](https://x.com/hppzyy/status/2111573227881529454)），将日常例行粗筛交给云电脑内挂载了廉价 DeepSeek API 的轻量级 CLI 工具处理，把官方周额度池100%留给核心推理。

所以必须定期做 Routine 审计。Grok Bot 团队的 Lauren Tan 在访谈里提到，她有一个叫 Dr. Eggbot 的 Bot 专门定期审计所有 Bot 和 Routine 的成本（团队成员访谈，https://www.youtube.com/watch?v=xZ5TEaleUdg）。社区的做法是每月搞一次淘汰审计（https://x.com/kocer_eth/status/2101669438038634827）：数一数上个月跑过的任务，看结果到底被你采纳了几次；找出那些长期失败、没人看的幽灵任务；每次审计至少强制删掉一条没用的 Routine（https://x.com/kocer_eth/status/2101669438038634827）。甚至像 `@kaelanyiu`（Kaelan Yiu）那样，专门设立一个每隔几天才低频运行一次的“评测官 Bot（Meta-Evaluator Bot）”，对各 Worker Bot 的产出质量与模型性价比跑分审计，动态优化整个团队的底层调用配置（[https://x.com/kaelanyiu/status/2114213605566742884](https://x.com/kaelanyiu/status/2114213605566742884)）。

> [!NOTE]
> 📸 **截图位（待补）**：Routine 审计提示词在对话中的执行与停用确认

你可以把下面这段审计提示词直接发给负责调度的 Bot。它会检查所有排期，把高频轮询改成看哈希值、计数器或时间戳的轻量检查，而且没有你确认绝不动手删（https://x.com/fleyta88/status/2109346840382415019）：

```text
Audit all my existing routines across all Bots and optimize the execution plan around actual business changes.

Perform the following steps:
1. List every routine, its owning Bot, its schedule or trigger, and its expected output.
2. Flag routines where over 90% of historical runs produced no change or were ignored.
3. Replace high-frequency full runs with lightweight change checks: inspect only a file hash, record count, or updated timestamp before doing downstream heavy work.
4. If no underlying data has changed, instruct the routine to terminate immediately without generating notifications.
5. Identify any routine that has not directly influenced a decision or workflow in the past 30 days and nominate it for deletion.
6. Verify that all irreversible external actions remain gated behind human approval.

Show me the full audit report, proposed schedule adjustments, and estimated savings first. 
Do not modify, pause, or delete any routine without my explicit confirmation.
```

说到底，**例行自动化本身只是过程，如果输出结果从未影响过你的任何实际决策，它就是在白白烧钱**（https://www.youtube.com/watch?v=LM7Ft7g8qJw）。定期大扫除，留下真正能办事的坚固闭环，你的 Bot 团队才算上了正轨。

---

[← 上一章：§06 云电脑：它的工位 · The Computer](../part2-core-concepts/06-computer.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§08 审批与安全边界 · Approvals & Safety →](../part2-core-concepts/08-approvals-safety.md)

# §19 额度去哪了 · Where Usage Goes

[← 上一章：§18 研发场景：Bot + Cursor 云端 Agent + GitHub · Capstone B](../part6-capstones/18-capstone-b.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§20 省钱心法 · Saving →](../part7-saving/20-saving.md)

---

> **适合谁**：所有用户，尤其是刚收到"额度用尽"提示、或者担心被意外扣费的新手。本章不需要任何技术背景。

## 19.1 周额度、按需消费、月上限是三套机制 · Three Meters

我调研社区讨论时发现，新手最常碰到的问题就是额度突然见底。周三晚上派了两个整理网页的任务，周四早上一开客户端，输入框上方就挂着一条深色横幅，提示周额度已达到上限，还要再等四天才会重置。很多人看到这里的反应就是慌：是不是月付订阅失效了？还是系统出了扣费 Bug？要不要赶紧再去买个号？

**每周包含用量、按需消费和月度限额是三套完全独立的控制逻辑**【社区】（https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/ ）。不把这三套计量机制拆开，后面排查账单或者调自动化任务就会到处踩坑。

第一套机制是订阅自带的每周包含用量。官方叫它 Weekly usage limit，在手机端简称为 Weekly usage【官方】（https://cursor.com/help/grok-bot/plans ）。所有付费的个人 Cursor 套餐——Pro 每月 20 美元、Pro+ 每月 60 美元、Ultra 每月 200 美元【官方】（https://cursor.com/pricing ），以及 Cursor Teams 自助套餐每人每月 40 美元【官方】（https://cursor.com/pricing ），都直接包含 Grok Bot 的使用资格【官方】（https://cursor.com/help/grok-bot/plans ）。要是没有 Cursor 付费订阅，绑定个人 SuperGrok、SuperGrok Plus、SuperGrok Heavy 或者 X Premium+ 账号也能拿到额度，但官方明确规定 SuperGrok Lite 不包含 Grok Bot【官方】（https://cursor.com/help/grok-bot/plans ）。档位划分上，官方只给了相对顺序：Pro 低于 Pro+，Pro+ 低于 Ultra；关联档里 SuperGrok 和 X Premium+ 都低于 SuperGrok Plus，Plus 低于 Heavy，Heavy 是"最高关联档"【官方】（https://cursor.com/help/grok-bot/plans ）。Cursor 档和关联档之间是否一一对应，官方没有写明，社区通常把它们按 Pro≈SuperGrok、Pro+≈Plus、Ultra≈Heavy 来对照【推测】。自助开通的 Grok Business 席位也能用，用 Sign in with Grok 登录即可【官方】（同上）。

这里的周额度拥有完全独立的计量池。在个人套餐下，Grok Bot 干活绝不扣你在 Cursor 编辑器里写代码的模型额度，你在编辑器里写代码也不会影响 Grok Bot 的周用量，去 Grok 独立网页应用聊天又是另一套限额系统【官方】（https://cursor.com/help/grok-bot/plans ，https://learngrokbot.com/usage-limits ）。全系统中只有一个连通例外：当 Bot 在对话中把写代码任务移交给 Cursor Cloud Agent 时，Bot 自己的轮次消耗 Grok Bot 周用量，Cloud Agent 写代码的部分则直接计入 Cursor 套餐额度【官方】（https://cursor.com/help/grok-bot/plans ，https://learngrokbot.com/usage-limits ）。

多买订阅也不会让额度叠加。官方文档写得很清楚，Cursor 套餐和关联的 SuperGrok 或 X Premium+ 额度无法叠加，系统只取其中周额度更高的那一档【官方】（https://cursor.com/help/grok-bot/plans ）。而且账号关联是永久的，一旦绑定就不能解绑，也不能转移给其他 Cursor 账号【官方】（https://cursor.com/help/grok-bot/plans ）。如果你在关联账号上把 SuperGrok 升级到了 Plus 或 Heavy，官方说明周用量刷新到新档位可能需要最多 24 小时【官方】（https://cursor.com/help/grok-bot/plans ，https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/ ）。在这 24 小时内不用重复购买，也不用反复折腾解绑。

第二套机制是按需消费（On-demand usage）。周额度用完后，系统不会替你扣钱。如果你在客户端设置里把 On-demand monthly limit 保持为默认的关闭状态（None），一旦周额度跑到 100%，所有的 Bot 都会就地停工，直到倒计时结束重置，期间不会扣你信用卡一分钱【官方】（https://cursor.com/help/grok-bot/plans ，https://learngrokbot.com/usage-limits ）。注意：这里说的"默认关闭"只适用于个人账户；Cursor Teams 团队账户的按需用量默认是开启的，团队成员要先问管理员上限是多少【官方】（https://cursor.com/help/grok-bot/plans ）。只有当你主动开启按需消费后，Bot 才能在周额度耗尽后继续跑。但要注意，超额部分的费用全部由 Cursor 统一按实际消耗的模型 Token 计费。哪怕你是靠绑定 SuperGrok 或 X Premium+ 拿到的使用资格，按需账单依然记在 Cursor 头上【官方】（https://cursor.com/help/grok-bot/plans ，https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/ ）。另外，如果 Cursor 账户里有推荐或促销赠金，周额度耗尽后系统会优先扣除赠金；即便按需限额设为 0 美元，赠金也会正常消耗，不会产生信用卡扣款【官方】（Cursor 员工论坛回复，https://forum.cursor.com/t/grok-bot-draining-cursor-credit-pool/169982 ）。

第三套机制是按需消费的月度上限（On-demand monthly limit，网页端对应 Monthly Limit）【官方】（https://cursor.com/help/grok-bot/plans ）。你可以设成固定金额，也可以设成不限额【社区】（https://learngrokbot.com/usage-limits ）。这里有个很多人都会踩的坑：月度限额并不是任务执行过程中的绝对硬停机线【官方】（https://cursor.com/help/grok-bot/plans ，https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/ ）。官方文档写明了，一个正在运行的长任务即使中途超出了月度限额，系统依然允许它跑完并完成交付。只有等这个任务结束后，后续新任务才会被拦截。别以为设了 10 美元限额账单就绝不会变成 12 美元，想在提示词里要求强制停机也没用。

官方提供的免费试用也是同理。它本质是一笔固定的使用额度，附带 7 天有效时间窗口【官方】（https://cursor.com/help/grok-bot/plans ）。时间和额度是两个独立条件，拿试用额度去跑繁重大任务，几个小时内额度就可能先于 7 天窗口耗尽；官方明确说了，用完的试用额度不会补发【官方】（https://cursor.com/help/grok-bot/plans ）。7 天试用绝不等于 7 天无限用。

![Grok Bot 三套计量器、周期与溢出计费流转关系](../../images/fig-19-1.png)

*图：Grok Bot 三套计量器、周期与溢出计费流转关系*

## 19.2 吞额度的常见元凶 · Burners

很多人在客户端里只聊了几句，或者刚建了两个定时任务，就发现周额度缩水了一大截，总怀疑系统在偷跑。其实 Grok Bot 计费看的是背后真实发生的执行步骤和 Token 消耗，绝不是看你在对话框里输入了几个字【官方】（https://cursor.com/help/grok-bot/plans ，https://learngrokbot.com/usage-running-out ）。

要搞清楚额度怎么没的，先得看它的上下文处理机制。**Grok Bot 每次回复前，都会把当前会话的历史记录完整重读一遍**【官方】（Cursor 员工论坛回复，https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705 ；https://learngrokbot.com/usage-running-out ）。系统不会在每次聊完后自动压缩历史，只有当上下文长度逼近模型极限时才会进行总结【官方】（Cursor 员工论坛回复，https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705 ）。官方技术人员查大额账单时提到，那些重度调用的 Bot 每走一步往往都要重新读取大约 80,000 到 90,000 个 Token【官方】（Cursor 员工论坛回复，https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705 ）。如果一个会话连续用了好几天，里面堆满了网页抓取结果和长篇输出，哪怕你最后只是追问一句搞定没有，它也必须先吃下前面数万个 Token 的历史上下文，单次回话成本直接滚雪球。

我翻看文档和社区反馈，整理出几个最常见的吞额度元凶。

第一个元凶是会话常年不刷新，还把 Routine 挂在日常聊天的 Bot 身上。新手最容易把一个 Bot 当成日常聊天窗口，所有任务都在同一个对话流里累加【社区】（https://learngrokbot.com/usage-running-out ）。更隐蔽的坑在定时任务的运行机制：Routine 每次运行，都是在它所属 Bot 的对话流中进行的【社区】（https://learngrokbot.com/usage-running-out ）。如果你把一个每小时巡检网页的 Routine 挂在白天频繁聊天的 Bot 下，这个 Routine 每次启动时，都得先把白天聊过的几万字背景全盘重读一遍。哪怕它只是抓取单行状态，也会白白消耗巨大的上下文额度。

第二个元凶是高频轮询空转，没设无变化退出机制。有人把 Routine 的触发间隔设得极密，比如每 15 分钟甚至每 5 分钟跑一次【官方】（https://cursor.com/help/grok-bot/routines ）。社区帖称每 5 分钟触发一次的 Routine，一个月内会执行 8,640 次（个例）【社区】（https://x.com/fleyta88/status/2109346840382415019 ）。每 15 分钟执行一次，一天就会产生将近 100 次运行【社区】（https://learngrokbot.com/usage-running-out ）。如果在 Routine 提示词里没写明数据无变化立即退出，Bot 每次都会老老实实打开网页、抓取、分析并写长汇报。在公共 Slack 频道挂监听也是同样的道理，活跃频道里每来一条新消息都会触发一次完整的 Bot 回合，一天之内烧光整周额度很常见【社区】（https://learngrokbot.com/usage-running-out ）。

第三个元凶是长时间操作浏览器、频繁截图，在卡顿页面上死磕。Bot 操作云电脑里的浏览器属于高开销动作【社区】（https://learngrokbot.com/usage-limits ）。目标网站一旦出现动态加载慢、反爬弹窗或者页面假死，Bot 会自己多次滚动、重试和重新截图分析。第三方 Grok Bot Wiki（非官方站点）写道，让 Bot 在卡顿网页上反复折腾 20 分钟消耗的 Token 和步骤，远比连续回答几十次短文本问答昂贵得多【社区】（https://www.grokbotwiki.com/guides/grok-bot-weekly-usage-limit ）。

第四个元凶是多 Bot 群聊互相客套，甚至陷入死循环。多 Bot 协作群聊看着省事，但群内每个 Bot 的发言都会被单独计费，Bot 之间互通消息同样消耗额度【社区】（https://learngrokbot.com/usage-limits ）。官方技术人员指出，在某些大额消耗账户里，大约三分之一的调用纯粹是 Bot 之间互相唤醒造成的【官方】（Cursor 员工论坛回复，https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705 ）。一个 Bot 汇报完成，另一个回复收到，第三个再补充感谢，这些客套交互在后台极吃 Token。Cursor 员工在论坛里建议，在多 Bot 协作提示词里直接加入安静交接指令【官方·Cursor 员工论坛回复】（https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705 ；整理见 https://learngrokbot.com/usage-running-out ）：

```text
From now on, only message another Bot when it needs to act. No acknowledgments, no thanks, no progress updates. Send one summary when the work is done.
```

更极端的情况是 Bot 自己陷入死循环。社区帖称有用户建了一个叫 Elon 的 Bot，刚建完没输任何提示词，Bot 自动在网上搜了马斯克头像换上，随后陷入自言自语并反复尝试生成马斯克真人图的死循环（die loop），客户端停不下来，一口气白白烧掉了 4% 的周额度（个例）【社区】（https://linux.do/t/topic/2807876 ）。服务故障期间也容易踩这种坑。2026 年 10 月 8 日全网 Routine 出现系统级故障，论坛里有用户说排查过程本身就耗掉了额度，有人当天用掉 30%，有人超过 90%【社区】。Cursor 员工 @deanrie、@kevinn 说明原因是平台负载过高，暂停、恢复、复制或重建 Routine 都没用，错过的运行也不会补跑【官方·Cursor 员工论坛回复】（https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125 ）。

第五个元凶是在云电脑中套娃跑其他外部大模型工具。社区帖称有用户为了省 Token，在 Grok Bot 的云电脑里装了 Codex 和 Claude Code。结果 Codex 的额度消耗极快，一个自动化任务还没跑完，五小时的额度就用光了；那个从没用过的 Claude 免费号后来也收到了封号邮件，原因帖子里没说明，是否与机房 IP 有关属于推测（个例）【社区】（https://x.com/i/status/2107100457231651312 ）。用虚拟机套娃跑高消耗开发工具，往往得不偿失。

![长会话重读机制与多 Bot 互相唤醒引发的 Token 滚雪球效应](../../images/fig-19-2.png)

*图：长会话重读机制与多 Bot 互相唤醒引发的 Token 滚雪球效应*

## 19.3 怎么看用量 · Reading Usage

要守住额度，先得学会看面板。

桌面客户端点左下角头像，或者进 Settings 选择 Usage & Billing 页面【社区】（https://learngrokbot.com/usage-limits ）。v0.63.0 起，Settings → Usage & Billing 会显示包含用量和下次重置时间，不再误显示"套餐不含用量"【官方】（https://x.ai/changelog/bot ，https://learngrokbot.com/usage-limits ）。在网页端，可以直接访问 cursor.com/dashboard，在 Spending 页面核对 Grok Bot 卡片的明细与按需消费上限【社区】（https://learngrokbot.com/usage-limits ）。如果想了解任务背后实际调用的模型，可以登录 cursor.com/dashboard/usage 查看后台记录，确认任务是路由到了 opus 5.5 还是使用了默认的 grok-bot-default【社区】（https://linux.do/t/topic/2990677 ）。

看面板时别想当然：**面板上的百分比是相对消耗比例，不是固定的美元金额或消息条数**【社区】（https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/ ）。很多人看到剩余额度从 80% 掉到 74%，就以为自己花掉了 6 美元，或者觉得 1% 就是固定的一条对话。社区帖称 Cursor Pro 的 Bot 额度相当于 250 美元或 450 美元（个例）【社区】（https://linux.do/t/topic/2848179 ），也有社区帖称 Pro 账号每发一条消息大约消耗 1% 的周额度（个例）【社区】（https://x.com/miniyarov/status/2105428357273800799 ）。

官方从未公布过任何档位对应的具体 Token 数量或折算金额【官方】（https://cursor.com/help/grok-bot/plans ）。面板上的百分比只是你当前在一周动态额度池中的使用进度。一条简单的单行文字回答，在独立会话中可能只让周额度波动 0.01%；而一个包含翻长网页、抓数据、跑脚本的任务，消耗可能是前者的数十倍【社区】（https://learngrokbot.com/usage-running-out ）。脱离了步骤复杂度与会话上下文长度，把百分比生搬硬套成单条消息成本没有任何意义。

目前客户端没法按单个 Bot 或单个 Routine 拆分显示用量明细【社区】（https://learngrokbot.com/usage-running-out ）。面板给出的永远是整个账户的统揽百分比。想弄清楚具体哪项任务最吃额度，不能靠猜，可以在没有其他定时任务跑的时间段，单独运行某一个受控任务，记录执行前后的百分比净变化【社区】（https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/ ）。

> [!TIP]
> 🧪 【实测·TODO待实测】测试独立受控环境下单次网页浏览任务与纯文本问答前后的周用量百分比变化。

> [!NOTE]
> 📸 **截图位（待补）**：Settings > Usage & Billing 面板中的周用量百分比与重置倒计时
> [!NOTE]
> 📸 **截图位（待补）**：cursor.com/dashboard/usage 面板中的后台模型调用记录

## 本章来源

- Cursor 帮助中心：Grok Bot 套餐与计费官方说明 https://cursor.com/help/grok-bot/plans
- Cursor 价格页面官方配置 https://cursor.com/pricing
- Cursor 用户控制台账单与消费设置 https://cursor.com/dashboard
- Cursor 控制台用量与模型路由记录 https://cursor.com/dashboard/usage
- Ofox：Grok Bot 额度周用量与按需消费机制说明 https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/
- LearnGrokBot：Grok Bot 用量限制与双计量器解析 https://learngrokbot.com/usage-limits
- LearnGrokBot：额度快速耗尽原因与排查方案 https://learngrokbot.com/usage-running-out
- GrokBotWiki：周额度限制与按需控制实战指南 https://www.grokbotwiki.com/guides/grok-bot-weekly-usage-limit
- SpaceXAI 官方文档：技能、Routine 与自动化规范 https://docs.x.ai/grok-bot/skills-routines-and-automations
- SpaceXAI 官方文档：设置与通知说明 https://docs.x.ai/grok-bot/settings-and-notifications
- SpaceXAI 官方文档：故障排查指引 https://docs.x.ai/grok-bot/troubleshooting
- SpaceXAI 官方更新日志：Bot 更新历史 https://x.ai/changelog/bot
- Cursor 官方论坛：关于 1500 美元周账单的员工回复与长会话 Token 机制披露 https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705
- Cursor 官方论坛：员工就 Grok Bot 独立周额度池与溢出机制的修正回复 https://forum.cursor.com/t/grok-bot-spend-cursor-usage-i-cant-accept-it/169796
- Cursor 官方论坛：员工确认 Credits 赠金在按需扣费前优先消耗 https://forum.cursor.com/t/grok-bot-draining-cursor-credit-pool/169982
- Cursor 官方论坛：Ultra 用户额度消耗排查与员工优化建议 https://forum.cursor.com/t/grok-bot-ultra-users-how-do-you-make-the-weekly-allowance-last-mine-reached-99-in-three-days/171221
- Cursor 官方论坛：10 月 8 日全网 Routine 故障与员工确认公告 https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125
- Cursor 帮助中心：Routine 调度与频率警告 https://cursor.com/help/grok-bot/routines
- X 平台 @filedfyi 贴出的 90% 与 100% 额度警告横幅截图记录 https://x.com/filedfyi/status/2107109569512014270
- X 平台官方账号 @bot 说明 Main Bot 自主建议不计入用量 https://x.com/bot/status/2105713241745977618
- X 平台官方账号 @bot 宣布全员额度重置公告（10 月 3 日 02:05，北京时间） https://x.com/bot/status/2106083136002310193
- X 平台官方账号 @bot 宣布全员额度重置公告（9 月 6 日 02:24，北京时间） https://x.com/bot/status/2096303514230423629
- X 平台官方账号 @bot 宣布 8 月 26 日全员额度重置公告 https://x.com/bot/status/2092664183334846840
- LINUX DO 社区主题 t/2807876：创建 Elon Bot 触发头像更换与生图死循环记录 https://linux.do/t/topic/2807876
- LINUX DO 社区主题 t/2990677：Grok Bot 路由至 Opus 5.5 与后台查看方法 https://linux.do/t/topic/2990677
- LINUX DO 社区主题 t/2848179：关于 Cursor Pro 额度折算估算的讨论帖 https://linux.do/t/topic/2848179
- X 平台 @WildVariable01 分享在云电脑安装 Codex 与封号经验 https://x.com/i/status/2107100457231651312
- X 平台 @miniyarov 关于每条消息消耗 1% 周额度的推测帖 https://x.com/miniyarov/status/2105428357273800799
- X 平台 @fleyta88 关于 5 分钟 Routine 触发频率与消耗的讨论帖 https://x.com/fleyta88/status/2109346840382415019
- didreset.com 额度追踪页面关于官方未公开具体数字的记录 https://didreset.com/limits/grok

---

[← 上一章：§18 研发场景：Bot + Cursor 云端 Agent + GitHub · Capstone B](../part6-capstones/18-capstone-b.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§20 省钱心法 · Saving →](../part7-saving/20-saving.md)

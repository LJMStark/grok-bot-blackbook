# §01 Grok Bot 是什么 · What It Is

[← 上一章：《Grok Bot 黑皮书：从零到一支 AI 团队》](../part0-preface/00-preface.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§02 怎么才能用上 · Getting Access →](../part1-getting-started/02-access.md)

---

## 1.1 一句话讲清 Grok、Grok Bot、Cursor 的关系 · Grok vs Grok Bot

很多人第一次听说 Grok Bot，以为它是把 Grok 聊天机器人套了个壳。其实不是。

Grok 是 SpaceXSI（前 xAI）的大语言模型。你向它提问，它吐出一段文字。Grok Bot 是搭在模型上层的 Agent 应用——你不是找它聊天，是在给它派活。官方原话写得明白："Grok Bot gives you Bots you can keep around: AI teammates with names, jobs, and context that compounds over time"【官方】（[docs.x.ai/grok-bot/overview.md](https://docs.x.ai/grok-bot/overview.md)）。社区里一条 215 赞的帖子概括得很透彻：Grok 负责调研、比对、理清思路，再把指令下发给 Grok Bot；Grok Bot 负责切进 App、改数据、发消息、把事情收尾【社区】（[X 帖](https://x.com/i/status/2106883332432945519)）。一句话：**Grok 负责想，Bot 负责做**。

再说 Cursor。2026 年 2 月 xAI 并入 SpaceX【官方】（[x.ai/news/xai-joins-spacex](https://x.ai/news/xai-joins-spacex)），8 月 14 日 AI 编程工具 Cursor 也成为 SpaceXSI 的一部分——官方客服案例原文是 "When Cursor became part of SpaceXSI on August 14"【官方】（[x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）。Grok Bot 与 Cursor 共用一套账号和订阅——所有 Cursor 付费个人版和 Teams 计划都直接带 Grok Bot 权限【官方】（[docs.x.ai/grok-bot/overview.md](https://docs.x.ai/grok-bot/overview.md)）。Cursor 的云端代理（Cloud Agent / Cursor Projects）也能在 Grok Bot 内部直接调用，这块我留在 §10 展开。

这三者连起来是一条链条：Grok（模型层）→ Grok Bot（Agent 层）→ Cursor（编码层）。你可以单用 Grok Bot 不碰代码，也可以让 Bot 把编程任务自动分发给 Cursor 的云端 Agent。普通用户面对的入口只有一个：Grok Bot 的桌面端或手机端。

![Grok · Grok Bot · Cursor 三者关系图（模型→Agent→编码）](../../images/fig-01-1.png)

*图：Grok · Grok Bot · Cursor 三者关系图（模型→Agent→编码）*

2026 年 10 月 7 日，马斯克在 X 上公布了一个新动向：Grok Bot 不再只调用自家的 Grok，而是按任务分工路由到 Claude Opus 5.5、Midjourney、Suno 这些外部模型【官方】（[马斯克 X 帖](https://x.com/elonmusk/status/2107724314451878104)；[TNW 报道](https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk)）。Grok Bot 团队成员 @poteto 随后在回复里说："yes, bot itself will run on opus 5.5"，并称 Opus 5.5 "is rolling out right now"【官方·团队成员个人帖】（[X 帖](https://x.com/poteto/status/2107734770990133319)）。也就是说，用户不必费心挑模型，Bot 会替你选后端；但这是逐步推送，截至 10/12 仍有用户说自己没感觉到切换【社区】（[X 帖](https://x.com/GodlyAlphaM/status/2108885285941698990)），官方 x.ai/news 也还没有专文。虽然没给手动切换的开关，但省心之处在于，你用不着关心各家模型的参数差异。

## 1.2 一台云电脑 + 一群同事 · The Cloud Computer Model

理解 Grok Bot 最省事的方式，就是把它看作你在云端长期开着的一台电脑，上面围坐着一群同事。

每个 Bot 都跑在一台持久化的云电脑里，自带浏览器、文件系统和终端【官方】（[docs.x.ai/grok-bot/computer-and-apps.md](https://docs.x.ai/grok-bot/computer-and-apps.md)）。你合上笔记本电脑、锁屏甚至直接关机，它依然在云端干活，不吃本地资源【官方】（[docs.x.ai/grok-bot/overview.md](https://docs.x.ai/grok-bot/overview.md)）。这跟网页版 ChatGPT 或 Grok 完全两码事：网页关了任务就断，Grok Bot 则是你走开了，它还在继续跑。

这台云主机的硬件规格，社区用户测算大致是 8 核 CPU、16GB 内存、约 128GB 硬盘【社区】（[X 帖](https://x.com/hejushang8/status/2103760664217174494)；[NodeSeek 帖](https://www.nodeseek.com/post-906175-1)）。官方文档没有对外公开过硬性参数，后续随时可能会变【实测·TODO待实测：开机进入终端运行 lscpu、free -m 和 df -h 摸清实际硬件配置】。

核心规则是：**同一个账号下的所有 Bot 共用这一台电脑**。官方文档写得很清楚："Every Bot on your account uses the same computer"【官方】（[docs.x.ai/grok-bot/computer-and-apps.md](https://docs.x.ai/grok-bot/computer-and-apps.md)）。共用意味着什么？浏览器 Cookie 和登录态完全打通，一个 Bot 登了 Gmail，其他 Bot 抬手就能用【官方】（同上）；硬盘文件对所有 Bot 开放【官方】（同上）；命令行凭据也是共享的【官方】（同上）。

好处是 Bot 之间交接工作不用反复登录、重新配环境，前面做了一半，后面接手就能干。坏处是这里不存在安全边界，官方明确提醒："do not place a credential or file on it if another Bot on your account should not be able to use it"【官方】（同上）。§08 讲安全时我会单独拆解，这里先记牢：千万别在云电脑里登你的网银。

虽然共用一台机器，但每个 Bot 分配了独立的屏幕（screen）。多个 Bot 可以并行使用浏览器和桌面工具，不过单个 Bot 同一时间只能跑一个 computer-use 任务【官方】（同上）。官方设计博客的比方打得很形象：这更像"和同事同处一室办公"，而不是"操作一台远程机器"——你能看到他们都在忙，探头瞄一眼屏幕就知道进度，遇到卡壳再坐过去接手键盘鼠标【官方】（[x.ai/news/designing-grok-bot](https://x.ai/news/designing-grok-bot)）。

> [!NOTE]
> 📸 **截图位（待补）**：Agent Computer 云电脑视图

!["所有 Bot 共享一台云电脑"示意图——共享区域（浏览器/文件/登录态）与独立区域（各 Bot 的屏幕）](../../images/fig-01-2.png)

*图："所有 Bot 共享一台云电脑"示意图——共享区域（浏览器/文件/登录态）与独立区域（各 Bot 的屏幕）*

## 1.3 它能做什么、不能做什么 · Can / Can't

### 能做什么

官方文档列出了 8 个核心方向，每个方向都配了可复制的提示词【官方】（[docs.x.ai/grok-bot/use-cases.md](https://docs.x.ai/grok-bot/use-cases.md)）：销售外拓（Sales Outbound，从 CRM 调取目标客户打分并起草外联邮件）、招聘猎头（Talent Scout，按岗位筛选候选人并排除已有记录）、付费投放（Paid Media，拉广告数据比对预算与 CAC）、费用管理（Expense Manager，按周核对报销单据标记违规）、产品性能（Product Performance，调查线上故障出具截图和依据）、Bug 复现（Bug Reproduction，在测试环境还原问题产出复现步骤与最小用例）、客户健康（Account Health，结合用量与工单评估续约风险），以及总参谋长（Chief of Staff，每日通读收件箱、日历、Slack 和纪要梳理优先级）。

中文社区的玩法要接地气得多【社区】（本书调研汇总 research/zh/zh-summary.md，非官方页面）：接微信做自动客服（10 月热度最高）、自媒体流水线（公众号和小红书的选题、写稿加排版）、跨境电商巡检竞品与监控新词、结合 Google Maps 和 Gmail 规划旅行、批量退订垃圾邮件、在云电脑里跑 ffmpeg 脚本渲染视频，以及搭建 Notion 数据看板。这些玩法我在 Part 5 会逐个拆解，这里先知道大致框架。

### 做不到的事

我调研下来，目前明确做不到的事主要有这几项：

国内主流应用没有任何官方插件。微信、小红书、抖音、QQ 邮箱通通没有接口。想让它跑，只能靠网页版登录、导出文件或者手工截图绕过去【社区】（[象鱼工作流](https://xiangyugongzuoliu.com/grokbot-use-cases/)）。这对国内用户来说门槛最高，§11 会专门讲怎么绕路。

你没法手动选底层模型。前面说过，Bot 会按任务自动分流，官方压根没留模型切换开关【社区】（[TNW](https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk)）。

**付款和对外发送必须经过人工审批**。Bot 掏钱买东西会弹出确认卡片让你核对金额，发邮件和发 Slack 消息可以先生成草稿卡片，等你点 Send 才送出【官方】（changelog v0.45.0；官方用例提示词也都以"Do not send"、"Do not contact anyone"结尾，[docs.x.ai/grok-bot/use-cases.md](https://docs.x.ai/grok-bot/use-cases.md)）。注意这不是绝对红线：9/30 的 v0.64.0 起，草稿卡片上可以选"Disable drafts for this Bot"，之后该 Bot 会直接发送【官方】（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。新手建议保持草稿模式。

目标网站随时能拦死它。Bot 虽能跑浏览器，但对方站点一旦开启防爬风控、强制验证码或登录态过期，Bot 就会停下来把控制权交还给你，它自己翻不过去【官方】（[docs.x.ai/grok-bot/overview.md](https://docs.x.ai/grok-bot/overview.md)）。

![能力矩阵——左列"能做"（8 个官方用例 + 中文热门 10 例），右列"不能做"（无国内插件、不能选模型、必须审批等）](../../images/fig-01-3.png)

*图：能力矩阵——左列"能做"（8 个官方用例 + 中文热门 10 例），右列"不能做"（无国内插件、不能选模型、必须审批等）*

## 1.4 时间线：8/11 到今天 · Timeline

Grok Bot 从上线到写书这天刚好两个月，版本迭代极快，官方 changelog 已经刷出了 **49 个版本**（v0.17.0 到 v0.68.1）【官方】（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。我把关键节点梳理出来：

2026 年 2 月 2 日，SpaceX 正式收购 xAI【官方】（[x.ai/news/xai-joins-spacex](https://x.ai/news/xai-joins-spacex)）。

8 月 11 日，Grok Bot 正式发布并开放早期测试，官方定义是随时在线的 Agent 团队，自带独立电脑，像人一样操作各类应用【官方】（[x.ai/news/introducing-grok-bot](https://x.ai/news/introducing-grok-bot)），同日发布了 Grok 4.6 模型【官方】（[x.ai/news/grok-4-6](https://x.ai/news/grok-4-6)）。8 月 26 日扩大权限，SuperGrok 全档、Cursor Pro 和所有 Cursor Teams 计划都包含 Grok Bot【官方】（[x.ai/news/grok-bot-more-plans](https://x.ai/news/grok-bot-more-plans)）；X Premium+ 绑定见 8 月 25 日的 changelog v0.27.0【官方】（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。三天后，8 月 29 日上线 X 集成，Bot 能读写公开推文【官方】（[x.ai/news/grok-bot-and-x](https://x.ai/news/grok-bot-and-x)）。

到了 9 月，节奏全面提速。9 月 3 日企业版上线，补齐访问控制、网络策略和审计日志，同日发布设计架构解析【官方】（[x.ai/news/grok-bot-for-enterprise](https://x.ai/news/grok-bot-for-enterprise)；[x.ai/news/designing-grok-bot](https://x.ai/news/designing-grok-bot)）。9 月 4 日官方晒出采购 Bot（Haggle Bot）案例，帮企业省下超 $100,000 直接成本【官方】（[x.ai/news/grok-bot-procurement](https://x.ai/news/grok-bot-procurement)）。9 月 21 日发布 Grok 4.7 模型，主打编程和知识工作提速一倍、成本减半【官方】（[x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)）。次日又公布客服案例，工单量涨了 175% 却没加一个人，单票成本压到 $0.20–0.30【官方】（[x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）。9 月 28 日上线 Team Bots，一个 Bot 全队共用，能直接嵌进 Slack【官方】（[x.ai/news/team-bots](https://x.ai/news/team-bots)）。

进入 10 月几乎一天一个样。10 月 2 日推出主动任务建议【官方】（[@bot X 帖](https://x.com/bot/status/2105713240701538538)）。10 月 3 日全员重置额度【官方】（[@bot X 帖](https://x.com/bot/status/2106083136002310193)）。10 月 7 日马斯克宣布路由外部大模型【官方】（[马斯克 X 帖](https://x.com/elonmusk/status/2107724314451878104)；[TNW](https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk)）。10 月 8 日 X 深度监控上线【官方】（[@bot X 帖](https://x.com/bot/status/2107949161878606089)），但同日发生大规模容量事故，大范围出现 "Bot failed to respond"，定时任务全部瘫痪【社区】（[Cursor 论坛](https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125)）。10 月 9 日接进 Shopify【官方】（[@bot X 帖](https://x.com/bot/status/2108228871938359347)）。10 月 10 日上线 Bot 专属邮箱，能注册服务、发信联系商家【官方】（[@bot X 帖](https://x.com/bot/status/2108609764766908772)）。截至 10 月 12 日本书截稿，changelog 已经刷到 v0.68.1，新加了做幻灯片和换聊天配色【官方】（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。

![时间轴长图——从 08-11 发布到 10-12，标注关键里程碑](../../images/fig-01-4.png)

*图：时间轴长图——从 08-11 发布到 10-12，标注关键里程碑*

用户增长方面：Bloomberg 报道称截至 9 月 14 日周活用户达到 418,000，环比增长 24%，数据来自伦敦活动上的一份演示文稿【社区】（[Mint 转载 Bloomberg](https://www.livemint.com/ai/elon-musk-s-grok-bot-hits-418-000-weekly-users-after-one-month-11790093107144.html)）。SpaceX 官方未作回应。这个数字比起 Meta Muse 据报超 300 万的周活有明显差距【社区】（[TNW](https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk)）——不过 Muse 免费且主打普通用户，Grok Bot 走付费且扎根工作场景，定位本来就不同。

## 1.5 为什么是现在 · Why Now

2026 年下半年，各大厂商扎堆涌入个人 AI Agent。每家都在推自己的产品：Meta 推出 Muse（免费，主打消费场景），OpenAI 推出 Dots（需要 ChatGPT Pro $100+），Google 有 Gemini Spark，Anthropic 有 Claude Cowork，开源界也有 OpenClaw 和 Hermes【社区】（[aiformortals 三方评测](https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)；本书调研笔记 research/web/compare/compare-notes.md）。社区里有博主一口气测了 21 个通用 Agent【社区】（[X 帖](https://x.com/i/status/2105067074720829819)）。

在这场混战里，Grok Bot 的切入点和别人不一样。社区有句广为流传的概括："**Dots 是 AI 秘书，Grok Bot 是 AI 组织**"【社区】（[X 帖](https://x.com/i/status/2105404819745718679)）。Muse 和 Dots 给你的是单个助理，Grok Bot 给你的则是一支团队——每个 Bot 有名字、有职位、有长期记忆，能在群聊里互相协同、交接任务。

价格层面，Grok Bot 门槛是 Cursor Pro $20/月（或 SuperGrok $30/月），Muse 虽是免费起步但高级功能也要 $20–100，Dots 绑定 ChatGPT Pro $100+，OpenClaw 和 Hermes 则支持自建托管【社区】（[X 价格横比](https://x.com/i/status/2105195069263225049)）。

有社区用户做过旅行规划的三方实测：Grok Bot 耗时最短，订机票比 Muse 便宜约 $90，Airbnb 便宜约 $136。换到小商家运营测试，Grok Bot 顺畅办完退款，还额外揪出了两笔隐蔽的重复扣费。该作者的结论是："For work, Grok Bot wins"【社区】（[aiformortals 评测](https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)）。这属于单一测试样本，不能直接套用到全部场景。

21 个 Agent 横评里，有句评价抓得很准："It works like a black box, no reasoning, no logs, but it produces the outputs I'm always happy with"【社区】（[X 帖](https://x.com/i/status/2105067123081105501)）。黑盒运作、缺乏推理过程与执行日志，在需要严密合规审查的企业环境里是潜在隐患。关于这个痛点，我会在后面的安全章节深入剖析。

竞品赛道变化极快。你读到这篇内容时，上面的部分对照可能已经出现变化。我把详细的竞品功能对照表单挪到了附录 H，正文只聚焦定位差异，省得花篇幅在容易失效的参数对比上。

![竞品定位坐标图——横轴"个人→团队"，纵轴"免费→付费"，标注 Muse / Dots / Grok Bot / OpenClaw / Hermes 的大致位置](../../images/fig-01-5.png)

*图：竞品定位坐标图——横轴"个人→团队"，纵轴"免费→付费"，标注 Muse / Dots / Grok Bot / OpenClaw / Hermes 的大致位置*

**本章来源**

- https://docs.x.ai/grok-bot/overview.md
- https://docs.x.ai/grok-bot/computer-and-apps.md
- https://docs.x.ai/grok-bot/use-cases.md
- https://x.ai/changelog/bot
- https://x.ai/news/introducing-grok-bot
- https://x.ai/news/grok-bot-more-plans
- https://x.ai/news/grok-bot-and-x
- https://x.ai/news/grok-bot-for-enterprise
- https://x.ai/news/designing-grok-bot
- https://x.ai/news/grok-bot-procurement
- https://x.ai/news/grok-bot-customer-support
- https://x.ai/news/team-bots
- https://x.ai/news/grok-4-6
- https://x.ai/news/grok-4-7
- https://x.ai/news/xai-joins-spacex
- https://x.com/elonmusk/status/2107724314451878104
- https://x.com/poteto/status/2107734770990133319
- https://x.com/bot/status/2105713240701538538
- https://x.com/bot/status/2106083136002310193
- https://x.com/bot/status/2107949161878606089
- https://x.com/bot/status/2108228871938359347
- https://x.com/bot/status/2108609764766908772
- https://x.com/i/status/2106883332432945519
- https://x.com/i/status/2105404819745718679
- https://x.com/i/status/2105067074720829819
- https://x.com/i/status/2105067123081105501
- https://x.com/i/status/2105195069263225049
- https://x.com/hejushang8/status/2103760664217174494
- https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk
- https://www.livemint.com/ai/elon-musk-s-grok-bot-hits-418-000-weekly-users-after-one-month-11790093107144.html
- https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots
- https://xiangyugongzuoliu.com/grokbot-use-cases/
- https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125
- https://x.ai/news/grok-bot-customer-support （Cursor 并入 SpaceXSI）

---

[← 上一章：《Grok Bot 黑皮书：从零到一支 AI 团队》](../part0-preface/00-preface.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§02 怎么才能用上 · Getting Access →](../part1-getting-started/02-access.md)

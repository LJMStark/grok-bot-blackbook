# §14 个人与生活 · Personal & Daily Life

[← 上一章：§13 编制案例库 · Team Blueprints](../part4-multi-bot/13-blueprints.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§15 内容创作 · Creators →](../part5-use-cases/15-creators.md)

---

很多人刚拿到 Grok Bot，总想先给它丢个大项目或者写套复杂系统。我建议先从日常生活切入。生活里的杂事目标明确，输入固定，做没做好一眼就能看出来。拿个人杂事练手，熟悉它的云电脑运行机制，摸清审批闸门和用量消耗，最稳妥。

不过动手前得先立条规矩：生活场景里全是私密信息，家庭地址、孩子学校、银行卡号，漏一次就麻烦了。所有涉及对外发送、掏钱付款和账号变更的动作，必须死死卡在人工审批后面。

> **适合谁**：已经跑通 §04 第一个任务的个人用户，不需要会写代码。
> **前提条件**：14.1、14.2 用到 Gmail 和 Google Maps，需要 Google 账号并能访问 Google 服务；只用国内邮箱（QQ、163）的读者，可以先用 14.3 的"转发到 Bot 自有邮箱"做法。提示词用英文写是因为原始案例是英文，换成中文同样可用。

## 14.1 邮箱大扫除与退订 · Email Cleanup & Unsubscribe

> [!NOTE]
> 📸 **截图位（待补）**：Gmail 插件授权后 Bot 在云电脑读取收件箱并生成退订候选列表
> [!NOTE]
> 📸 **截图位（待补）**：Bot 生成内联退订草稿并弹出人工审批卡
> [!NOTE]
> 📸 **截图位（待补）**：Bot 自有邮箱配置界面与域名绑定说明

### 场景

拿 Bot 处理生活杂务，很多人最先想到的就是清理堆成山的推广邮件。广告、平台活动推送、从不看的新闻简报，手动退订费时间，乱点链接还容易碰上钓鱼网站，甚至误删账单。官方文档指出，最稳健的 Bot 角色应当掌控可重复的交付结果，而不是笼统问答；必须从“只读和准备”开始，先由人复核结果，再增加批准动作或例行流程（https://docs.x.ai/grok-bot/use-cases.md）。

官方团队成员建议，新手上手的第一步是连接日历、邮件等常用应用，给 Bot 提供足够的上下文和工具（https://x.com/poteto/status/2107830403549831186）。实操时先给 Bot 只读权限去扫描收件箱，把近 30 天未互动过的推广邮件归类，提取发件人和退订途径，列出清单供人工核对。社区也有成熟经验：早上醒来时，Bot 已经把收件箱分类完毕，回复草稿都在对话框里等待点击批准（https://x.com/aizhibeibei/status/2108352015319613501）。2026 年 10 月 10 日，官方上线了 Bot 自有邮箱功能，每个 Bot 都能认领专属邮箱地址（https://x.com/bot/status/2108609764766908772）。社区有人在官方邮箱上线前就这么做了：用收信规则先把敏感邮件过滤掉，其余转发给 Bot 使用的代理邮箱，让它总结提醒，主邮箱完全不需要对 Bot 开放写权限（https://x.com/maiff20/status/2106774095820095969）。如果配置 Bot 专属邮箱作为个人助理，不要直接用个人真名做前缀，避免邮件往来抄送时搞混身份（https://x.com/petergyang/status/2108624122339287335）。

### 提示词

```text
You are my Email Cleanup Assistant.
Access my connected Gmail inbox in read-only mode for this step.
Scan emails received in the last 30 days that match categories "Promotions", "Social", or contain "unsubscribe" in the body.
Group them by sender domain and count the total messages per sender.
Filter criteria:
1. Identify senders where I have not opened or replied to any message in the last 30 days.
2. For each identified sender, extract the sender name, email address, frequency (emails per week), and the unsubscribe link or unsubscribe email address.
3. Exclude any senders related to banking, order receipts, flights, government notifications, or two-factor authentication.
Output format:
Return a markdown table with columns: Sender Name | Email Domain | Total Received | Unsubscribe URL/Target | Recommendation.
Standing boundaries:
- Do not click any unsubscribe links autonomously.
- Do not delete, archive, or modify any emails.
- Do not send any outgoing emails.
- Present the candidate list to me and wait for my explicit review.
```

### Routine

单次任务跑通后，可以固化为定期执行的 Routine。官方文档规定，每个 Bot 最多配置 50 个 Routine，执行间隔不得低于 5 分钟，系统只保留最近 20 条运行记录（https://docs.x.ai/grok-bot/skills-routines-and-automations.md）。邮件巡检可以设成每周日上午 9:00 跑一次，让 Bot 自动检查过去一周新增的无互动商业邮件，生成待审表格。

配 Routine 时，要照着社区摸索出的路子走：先手动执行并修正偏差，固化为技能后再进行二次输入测试，最后才能挂载为定时 Routine（https://x.com/Michael_Fenech_/status/2106352565528977469）。如果某一周没有符合退订标准的新邮件，要求 Bot 仅输出一行“本周无新增待退订项目”并立即停止运行，避免无意义的空转消耗。官方安全文档规定，后台或 Routine 触发的审批卡大约 10 分钟就会超时失效，卡片显示 Expired 且动作不会执行（https://docs.x.ai/grok-bot/approvals-security-and-privacy.md）。所以点击退订链接或清理归档这类操作，千万别指望在后台无人值守时完成。Routine 必须卡在生成待审清单这一步，等人工上线进入会话后再点选批准。

### 成本

官方未公布单次邮件扫描与分类的具体 Token 消耗数字。待测 500 封真实邮件收件箱单次扫描消耗的周额度百分比。

套餐费用方面，支持 Grok Bot 的个人门槛是 Cursor Pro 套餐，每月 20 美元，包含每周基础用量（https://cursor.com/pricing）。社区帖称在 Pro 档位下每条普通对话约消耗 1% 周额度（个例）（https://x.com/miniyarov/status/2105428357273800799）。每周运行一次退订排查对周额度的占用极小。但千万别设成每 5 分钟轮询一次的高频任务，社区帖称每 5 分钟一次的 Routine 单月触发 8,640 次，按 API 估算折合开销约 397 美元（个例）（https://x.com/fleyta88/status/2109346840382415019）。把这类常规维护任务压到每周一次，是最稳妥的控本方式。

### 坑

清理邮件最大的坑，是云电脑共享环境带来的凭据穿透。官方安全文档指出，用户账号下的所有 Bot 共享同一台云电脑环境，文件、浏览器会话和命令行凭据在所有 Bot 之间互通，删除某个 Bot 也不会清除这些共享状态（https://docs.x.ai/grok-bot/approvals-security-and-privacy.md）。要是你在邮件助手 Bot 里登录了主邮箱，其他写代码或跑外部脚本的 Bot 同样能拿到该浏览器的登录态。千万别把 Bot 之间的分类当成安全隔离边界。

另一个坑是审批超时导致动作悬空。由于后台审批卡 10 分钟自动过期（https://docs.x.ai/grok-bot/approvals-security-and-privacy.md），如果把 Routine 设定为“发现垃圾邮件直接弹出退订审批”，人一离开屏幕卡片就会失效，任务根本跑不成。另外，垃圾邮件常包含恶意钓鱼链接，让 Bot 在云端浏览器中无节制点击外链极易遭遇安全风险。必须坚持**草稿优先原则**，在设置中为所有外部请求配置明确的审批卡，决不允许 Bot 绕过人工直接跳转外部退订网页。

## 14.2 旅行全程管家（Google Maps + Gmail）· Travel Concierge

> [!NOTE]
> 📸 **截图位（待补）**：Bot 从 Gmail 提取订单数据并在云电脑整理行程时间线
> [!NOTE]
> 📸 **截图位（待补）**：云电脑浏览器调用 Google Maps 计算多目的地路线与耗时
> [!NOTE]
> 📸 **截图位（待补）**：移动端通过语音通话向 Bot 询问当日备选餐厅与路线

### 场景

规划家庭旅行很费神：比对机票确认信、酒店确认函、通勤路线和景点开放时间，得在几个平台之间来回切。官方团队成员在访谈中提到，她日常使用名为 Suki 的个人助理 Bot，在获得人工审批的前提下通过预订平台安排多段复杂行程（https://www.youtube.com/watch?v=xZ5TEaleUdg （团队成员访谈））。在度假场景下，可以让 Grok Bot 扮演旅行管家。

官方在 2026 年 10 月 8 日上线了 Google 连接器（https://x.com/mattyp/status/2107886668892057614）。Bot 可以通过只读模式调取收件箱里的机票和酒店订单，提取航班时间、航站楼和酒店入住时段；再在云电脑自带的浏览器里打开 Google Maps，测算酒店到各景点的公共交通耗时，核验营业时间，排查时间冲突。在价格追踪上，社区博主 Peter Yang 实测发现，让 Grok Bot 与 Meta Muse 追踪同一段日本航班行程时，Muse 给出的推荐价格比 Grok Bot 贵了 1,000 美元以上（https://x.com/petergyang/status/2103693608729932025）。在旅途中，还可以利用官方在 2026 年 9 月 18 日推出的移动端语音功能，对着手机语音查询当日行程或口述记录备选地点（https://x.com/elonmusk/status/2100698004210475317，https://x.com/bot/status/2100659463569170779）。

### 提示词

```text
You are my Travel Concierge Bot.
Review my connected Gmail inbox for flight and hotel confirmation receipts for the upcoming trip to Tokyo (dates: Oct 20 - Oct 25).
Tasks:
1. Extract arrival/departure flight numbers, terminals, times, and hotel booking details (hotel name, address, check-in window).
2. Open Google Maps in your browser and calculate transit times between the hotel and the target locations in the attached wishlist: Shibuya Sky, Senso-ji, Akihabara, and teamLab Planets.
3. Verify opening hours and popular visiting hours for each spot to prevent scheduling during closing times.
4. Generate a day-by-day itinerary table with columns: Day | Time Window | Activity | Location | Transit Time | Notes.
Standing boundaries:
- Do not book tickets, modify reservations, or pay for any services.
- Do not contact hotels or airlines.
- If any schedule conflict arises, highlight it in the notes and ask for my input.
- Return the finished itinerary table directly in chat for review.
```

### Routine

出发前 3 天，可以把行程监控挂载为定时 Routine，设在每天傍晚 18:00 运行一次。让 Bot 自动同步航班动态，拉取目的地未来 24 小时天气情况，并在云电脑内复查 Google Maps 上的实时路况，生成次日出行便签。

根据社区推荐的五阶段晋升流程，自动化必须经历验证单次任务、提炼方法、沉淀为技能、换一份输入测试，最后才能设定 Routine（https://x.com/kocer_eth/status/2105008655770788250）。如果当天没有任何航班延误或恶劣天气预警，Routine 只在对话框中给出一行正常确认，绝不重新输出整页冗长的行程单，确保信息流保持清爽。

### 成本

官方未公布多工具交互与地图排期的具体 Token 消耗数字。待测 5 天跨时区行程排期任务中浏览器交互与文本解析的额度消耗。

套餐门槛依然为 Cursor Pro 每月 20 美元（https://cursor.com/pricing）。官方帮助文档警告，免费试用是一笔固定用量额度并带有 7 天窗口，长任务有可能在单次执行中耗尽全部试用额度，且官方不予补发（https://cursor.com/help/grok-bot/plans）。在试用阶段测试多步骤旅行规划时，应当尽量限定查询景点的数量，避免一次性派发过于庞大的搜索指令。

### 坑

在云端浏览器中使用地图或查询订票网站时，最常遇到的问题是数据中心 IP 遭遇服务拦截。Grok Bot 的云电脑架设在境外机房，直接访问某些本地化预订平台或交通网站时，往往会被识别为爬虫并弹出难以通过的验证码，甚至直接拒绝连接。此时需要在设置中开启**本地出口路由**（Settings → Computer → Route egress），让云电脑的网络流量绕回你本人的本地设备出口，走真实的个人家庭宽带网络（需要你的桌面电脑开着 Grok Bot 桌面端）（https://x.com/xiaohu/status/2099409639234289914）。

另一个严重风险是证件信息泄露。旅行行程中充斥着护照号码、身份证件、常客卡账号及支付信息。官方安全文档强调，绝不能在常规聊天中明文发送密码、一次性验证码或敏感证件信息（https://docs.x.ai/grok-bot/approvals-security-and-privacy.md）。当预订流程进行到最后一步需要填写真实身份或输入付款密码时，绝不能让 Bot 自行填写，必须在 Agent Computer 界面中点击 Take control 人工接管屏幕，手动输完后再交还控制权。此外，模型对机票酒店退改政策容易产生幻觉，在提示词中必须强制要求给出邮件原始出处，不可轻信模型的概括。

## 14.3 孩子学校消息汇总 · School & Family Digest

> [!NOTE]
> 📸 **截图位（待补）**：Bot 从转发的家校通知中提取作业与签字待办项
> [!NOTE]
> 📸 **截图位（待补）**：每日下午生成的结构化家庭待办与日程提醒卡
> [!NOTE]
> 📸 **截图位（待补）**：纠错时 Bot 依据原始通告文件更新日历事项

### 场景

家有学童的家长都知道学校通知有多碎。班级群消息、老师邮件和各类系统通告混在一起，有当晚必须完成的作业，有下周活动的着装说明，还有限时签字和缴费，稍不留神就会遗漏。官方文档在列举典型用例时，重点介绍了**首席幕僚模式**（Chief of Staff）：跨渠道梳理出带有原始出处链接的关键摘要，只提炼符合既定优先级的重要事项，说明原因并给出建议，同时绝不擅自发送对外消息或修改日程（https://docs.x.ai/grok-bot/use-cases.md）。

官方团队成员在访谈中证实，这种总助模式在早期内测的第二周就自然涌现出来了（https://www.youtube.com/watch?v=maSdsTLaMuU （团队成员访谈））。针对国内学校通知依赖即时通讯工具且无官方插件的现状，社区实践者探索出了可靠的数据入口：利用本地只读工具（如 WeChat Portal）直接读取本地缓存的通告文本（https://x.com/lens2645211/status/2108184037198266383），或者通过自动规则把家校邮件转发到 Bot 的自有邮箱中（https://x.com/bot/status/2108609764766908772）。象鱼工作流在总结国内平台用法时也强调，国内平台没有插件时切忌用 Bot 频繁模拟点击，把文本导出或转发给 Bot 处理是避免账号风控的最佳对策（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

### 提示词

```text
You are my Family & School Assistant, acting under Chief of Staff principles.
Review the school notices, class updates, and teacher emails provided in /workspace/school_inbox.
Tasks:
1. Filter information relevant only to my child (Grade 3).
2. Categorize all findings into three distinct blocks:
     - Student Homework: tasks the child must complete today, with explicit deadlines.
     - Parent Action Items: items requiring parental signature, fee payment, or confirmation forms.
     - Upcoming Events: calendar items for the next 7 days (dress code, field trips, holidays).
3. For every single extracted item, provide the exact source quote and file name.
4. If a notice contains no actionable deadline or requirement, classify it as general announcement and summarize in one line.
Standing boundaries:
- Do not send messages, replies, or emails to teachers or class groups.
- Do not sign or submit any electronic forms automatically.
- If any date or requirement is ambiguous, explicitly mark it as "Unconfirmed" instead of guessing.
```

### Routine

将该任务配置为每个工作日下午 16:30 触发的定时 Routine。让 Bot 自动读取当天收纳到文件夹中的所有通告，在半小时内输出一份清晰的三栏待办清单。

设计家庭日常 Routine 时，要吸取社区博主 kocer_eth 的警告：定期审计你的 Routine，对于那些虽然每天准时报到、但实际上从没改变过任何实际决策的任务，果断淘汰（https://x.com/kocer_eth/status/2101669438038634827）。如果当天下午学校没有任何新通告，让 Bot 仅发送单行提示“今日无新增学校通告”，坚决不重发旧内容。要是发现 Bot 提取的作业截止时间有误，按社区纠错原则来：当信息有事实出处时，要求 Bot 回查原始文件来源后再回答，而不是让它凭空再猜一次（https://x.com/Michael_Fenech_/status/2106729045878514147）。

### 成本

官方未公布多格式家校通告结构化解析的单次 Token 消耗数字。待测 30 份真实家校通告文本文件夹提炼信息的周额度消耗。

个人套餐标价依然是 Cursor Pro 每月 20 美元（https://cursor.com/pricing）。社区用户抱怨称，如果盲目建立多个 Bot 并不停轮询，往往只撑两天就会把每周额度打光，而随后的按需付费相当昂贵（https://x.com/RichSilver/status/2108053489620504822）。对于学校消息汇总，工作日每天傍晚只跑一次，既能确保信息零遗漏，又几乎不产生额外的额度压力。

### 坑

在家庭信息处理中，最大的隐患是隐私数据在多 Bot 间无序共享。Shane Mac 曾遭遇过惨痛事故：他的个人财务 Bot 把包含月度银行账单和刷卡支出的个人审计结果，直接发到了公司高管的公用 Slack 频道中，根源就在于不同 Bot 共用同一台云电脑，聊天会话发生混淆（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。学校通告中包含孩子的全名、班级学号、家庭住址和家长电话，这些信息如果长期堆放在云电脑的公共根目录，很容易被其他用于业务测试的 Bot 读取甚至误传。每次处理完通知后，必须按照官方安全规范及时从工作空间清理包含隐私的临时文件（https://docs.x.ai/grok-bot/approvals-security-and-privacy.md）。

第二个坑是自动打卡和代回确认。有些家长为了省事，试图让 Bot 代替自己在班级群里自动回复“收到”或者自动填写健康打卡表单。这种自动化极其危险，一旦遇到特殊调查问卷或表单格式变更，Bot 胡乱勾选提交会引发严重问题。对外交互必须死守在审批防线之后，Bot 只能生成填表草稿，绝不能拥有直接提交表单的权力。没有新内容就保持沉默，警惕形式主义刷屏。

## 14.4 购物比价与下单（审批）· Shopping & Checkout

> [!NOTE]
> 📸 **截图位（待补）**：Bot 在多个电商页面抓取乐高套装实时价格与历史走势
> [!NOTE]
> 📸 **截图位（待补）**：达到目标折扣后 Bot 弹出待审批的结账确认卡片
> [!NOTE]
> 📸 **截图位（待补）**：通过 Agent Computer 人工接管输入支付验证码并完成订单

### 场景

跨平台追踪心仪商品的价格并等待促销降价很耗时间。官方在采购案例中展示了 Haggle Bot 的具体成效：通过全网监控供应商花费与合同条款，一笔科技采购订单从 14,629 美元降至 6,143 美元（降幅达 58%），最终由 Amazon Bot 协助下单完成（https://x.ai/news/grok-bot-procurement）。在个人生活中，这套逻辑完全可以用来盯守高单价数码产品、绝版玩具或者乐高积木套装。

社区博主 liam_fallen 分享过真实经历：在全网现货售罄、苹果官方渠道需要等待数周的情况下，他向 Grok Bot 提供虚拟卡权限，让 Bot 自动发邮件询问线下门店寻库，成功找到现货并在核准后下单配送上门（https://x.com/liam_fallen/status/2109332219126784098）。X 上的 @grok 自动回复账号（AI 生成的回复，不是官方声明）在回答网友时说：Grok Bot 可以搜索最佳价格并代为下单，购买前会显示金额让你批准，再通过 Stripe Link 付款（https://x.com/i/status/2109347617398264294）。官方也在 2026 年 10 月 9 日上线了 Shopify 集成，支持订单和库存状态的追踪（https://x.com/bot/status/2108228871938359347）。

### 提示词

```text
You are my Personal Shopping & Price Tracker Bot.
Monitor the pricing for the item: LEGO Star Wars Millennium Falcon (Set 75192) across official online stores and authorized retailers (Amazon, LEGO Store, Target, Walmart).
Target condition:
- Base MSRP is standard retail; trigger an alert if the verified price drops below $700 or if a bundle coupon offering >= 15% discount is detected.
- Check in-stock status and seller reputation (only sold and shipped by authorized platform or official brand store).
Tasks:
1. Record current price, shipping fee, delivery estimate, and seller name across all platforms.
2. Compare total checkout price including shipping.
3. If target condition is met, prepare a purchase action card with direct item link and final amount.
Standing boundaries:
- Do not proceed past the cart page automatically.
- Never click "Place Order" or submit payment without my explicit approval.
- Do not input payment details into chat.
- If a CAPTCHA or two-factor prompt appears, stop and alert me to take control.
```

### Routine

按照官方 Haggle Bot 的运行范式，系统应当围绕真实变动而非高频轮询展开（https://x.ai/news/grok-bot-procurement）。比价 Routine 可以设定为每天早晚各运行一次（上午 10:00 与晚上 20:00），避开凌晨无促销变动的时段。

官方文档规定，Routine 最短间隔为 5 分钟，且当用户长时间不活跃时，系统可能会询问并自动暂停 Routine，以控制无人值守时的消耗（https://docs.x.ai/grok-bot/skills-routines-and-automations.md）。当 Bot 巡检发现某平台价格击穿目标阈值时，Routine 会在对话流中生成购买审批卡，列清含税总价与直达购买链接；如果价格未达标，则静默记录日志并退出，绝不打扰人。

### 成本

官方 Haggle Bot 采购案例展示了 58% 的价格缩减成果（订单金额从 14,629 美元降至 6,143 美元）（https://x.ai/news/grok-bot-procurement）。关于个人日常商品爬取与比价的实际 Token 消耗，官方未公布具体数字。待测 4 家主流电商网站持续巡检 14 天的周用量占比。

软件服务成本方面，Cursor Pro 套餐每月 20 美元（https://cursor.com/pricing）。必须警惕过度监控带来的隐形成本：社区帖称如果将 Routine 设为每 5 分钟一次的高频轮询，一个月 8,640 次触发按 API 估算可烧掉约 397 美元（个例）（https://x.com/fleyta88/status/2109346840382415019）。每天早晚各巡检一次，即可在额度可承受的范围内覆盖绝大多数日常降价活动。

### 坑

在涉及真实资金交易的场景中，资产安全是绝不可退让的底线。官方安全与审批文档明确规定，购买与资金转移属于高危动作，必须始终置于显式审批边界之后（https://docs.x.ai/grok-bot/approvals-security-and-privacy.md）。尽管社交平台上曾有拍信用卡照片给 Bot 的说法，但 @grok 的这条回复也提醒，隐私政策建议不要在提示词里放信用卡等敏感信息（https://x.com/i/status/2109347617398264294）。遇到需要输入支付卡号、动态短信验证码或 CVV 的结账页面时，必须使用官方规定的安全步骤：在 Agent Computer 界面执行**人工接管控制权**，由用户本人手动完成付款确认，绝不能在常规聊天框中明文发送任何付款卡号或安全码（https://docs.x.ai/grok-bot/approvals-security-and-privacy.md）。

第二个坑是电商网站的反爬与风控封号。主流电商平台对机房 IP 的识别非常严格，Bot 频繁在云电脑中打开商品页极易触发滑动验证码或人机校验。遇到风控时，强行让 Bot 自动化重试很容易导致电商账号被封禁，此时必须配合本地出口路由将流量转回个人本机 IP（https://x.com/xiaohu/status/2099409639234289914）。第三个坑是限时特价与审批超时冲突。官方后台审批卡大约 10 分钟自动过期（Expired）（https://docs.x.ai/grok-bot/approvals-security-and-privacy.md）。如果遇到库存极少的闪购特价，一旦没能在 10 分钟内点击 Allow once，卡片就会失效并取消操作。高时效性的秒杀抢购并不适合离线 Routine，必须在人守在屏幕前时以人机协同的方式半自动完成。

---

[← 上一章：§13 编制案例库 · Team Blueprints](../part4-multi-bot/13-blueprints.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§15 内容创作 · Creators →](../part5-use-cases/15-creators.md)

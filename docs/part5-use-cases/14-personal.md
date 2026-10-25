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

拿 Bot 处理生活杂务，很多人最先想到的就是清理堆成山的推广邮件。广告、平台活动推送、从不看的新闻简报，手动退订费时间，乱点链接还容易碰上钓鱼网站，甚至误删账单。官方文档指出，最稳健的 Bot 角色应当掌控可重复的交付结果，而不是笼统问答；必须从“只读和准备”开始，先由人复核结果，再增加批准动作或例行流程（https://cursor.com/help/grok-bot/use-cases）。

官方团队成员建议，新手上手的第一步是连接日历、邮件等常用应用，给 Bot 提供足够的上下文和工具（https://x.com/poteto/status/2107830403549831186）。实操时先给 Bot 只读权限去扫描收件箱，把近 30 天未互动过的推广邮件归类，提取发件人和退订途径，列出清单供人工核对。社区也有成熟经验：早上醒来时，Bot 已经把收件箱分类完毕，回复草稿都在对话框里等待点击批准（https://x.com/aizhibeibei/status/2108352015319613501）。2026 年 10 月 10 日，官方上线了 Bot 自有邮箱功能，每个 Bot 都能认领专属邮箱地址（https://x.com/bot/status/2108609764766908772）。社区有人在官方邮箱上线前就这么做了：用收信规则先把敏感邮件过滤掉，其余转发给 Bot 使用的代理邮箱，让它总结提醒，主邮箱完全不需要对 Bot 开放写权限（https://x.com/maiff20/status/2106774095820095969）。如果配置 Bot 专属邮箱作为个人助理，不要直接用个人真名做前缀，避免邮件往来抄送时搞混身份（https://x.com/petergyang/status/2108624122339287335）。

随着 2026 年 10 月中下旬 v0.71.2 与 v0.75.2 版本的更新，官方对专属邮箱 `@mail.grokbot.com` 做了两项关键升级（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/agent-email）：首先，由 Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）在 10 月 14 日正式发布的 `+alias` 加号子别名功能（https://x.com/SamSokolin/status/2110496237241667621，获 3,073 赞、219 转发、1,197 书签），允许你在同一个 Bot 邮箱下衍生出无限个细分业务入口（如 `mybot+newsletters@mail.grokbot.com`、`mybot+receipts@mail.grokbot.com`），并配置**仅当邮件发送到指定 `+alias` 别名时才触发对应的 Routine**；其次，v0.75.2 支持了邮件原样转发时完整保留原邮件的 HTML 排版格式、正文内嵌图片（inline images）以及文件附件（https://cursor.com/help/grok-bot/agent-email）。

基于这一特性，X 博主 `@songsong275452`（引用 `@gokul_i` 的方案，https://x.com/songsong275452/status/2113108916229886371）分享了一套彻底解放个人主邮箱的 **Newsletter 专属邮箱接管与周六精华周报**玩法：不再让各种行业通讯（Newsletters）塞满自己的私人 Gmail，而是将所有 Newsletter 订阅地址全部迁移到只有 Grok Bot 才会去读取的 `mybot+newsletters@mail.grokbot.com` 专属别名中；个人主邮箱瞬间恢复清净，再设置一条每周六早上自动运行的 Routine，将过去一周收到的全部 Newsletter 提炼成一份结构化精华周报（甚或直接写入一张实时更新的 Grok Bot Page 看板，https://x.com/bot/status/2112991843235610885）。

除了被动清理推广信，邮箱还是個人财务查漏补缺与每日情报的富矿。加密与 AI 领域知名博主 Miles Deutscher（`@milesdeutscher`）在其收获 3,100 赞、4,503 书签的“10 大逆天 Grok Bot 用例”长推（https://x.com/milesdeutscher/status/2113653680834859262）中，展示了三个与个人邮箱及信息流紧密联动的实战范式：
- **#6 Subscription Auditor（订阅账单审计与自动砍价/退订员）**（https://x.com/milesdeutscher/status/2113653772337770849，54 赞）：让 Bot 深度扫描邮箱里的周期性扣款账单（Receipts / Invoices）与 SaaS 续费通知，列出所有月度/年度订阅清单、识别长期未使用的闲置服务，甚至在获得你批准后，直接替你发邮件或打开客服聊天窗谈判降价折扣（Retention offer）或提交取消订阅申请。
- **#4 Morning Brief Routine（全渠道晨间情报简报）**（https://x.com/milesdeutscher/status/2113653803304296498，35 赞）：每天清晨定时串联你的收件箱未读重要邮件、当日日历日程与 X 平台行业动态，在你起床前生成一份端到端的晨间决策简报。
- **#1 Second Brain / "Obsidian Replacement"（零手动打标签的第二大脑）**（https://x.com/milesdeutscher/status/2113653848581816595，98 赞）：将有价值的邮件长文、X 书签与碎片笔记自动归档到 Grok Bot 的持久化工作区中，用自然语言检索替代繁琐的手动分类打标签。

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

如果你还想复刻 `@milesdeutscher` 的 **#6 Subscription Auditor（订阅账单审计员）** 与 `@songsong275452` 的 **Newsletter 周报汇总**，可以直接使用以下组合提示词模板：

```text
You are my Subscription Auditor & Newsletter Digest Bot.
Part 1 — Subscription Audit (Read-only scan):
1. Search my inbox (and messages sent to my +receipts@mail.grokbot.com alias) over the last 90 days for keywords: "receipt", "invoice", "subscription", "renewal", "billing", "charged".
2. Extract: Service Name | Billing Cycle (Monthly/Annual) | Amount | Next Renewal Date | Cancellation/Manage URL.
3. Flag any recurring charges that have increased in price or overlap in functionality, and draft a polite negotiation/cancellation email for my review.

Part 2 — Saturday Newsletter Digest:
1. Read all emails received at my +newsletters@mail.grokbot.com alias over the past 7 days.
2. Deduplicate overlapping AI/tech news, extract the top 5 high-signal insights with original links, and update my "Weekly Reading Digest" Page.

Standing boundaries:
- Never send cancellation emails or click confirmation links without my explicit approval.
```

### Routine

单次任务跑通后，可以固化为定期执行的 Routine。官方文档规定，每个 Bot 最多配置 50 个 Routine，定时执行间隔不得低于 5 分钟，系统只保留最近 20 条运行记录（https://cursor.com/help/grok-bot/routines，https://cursor.com/help/grok-bot/skills-routines-and-automations）。在 2026 年 10 月 22 日发布的 v0.75.2 版本中，官方将 Routine 的小时级运行频率上限大幅上调至：**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots），单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/routines）。邮件巡检可以设成每周日上午 9:00 跑一次，或者针对 `mybot+newsletters@mail.grokbot.com` 配置基于别名收信触发的定向 Routine（https://x.com/SamSokolin/status/2110496237241667621），让 Bot 自动检查过去一周新增的无互动商业邮件或周报，生成待审表格。

配 Routine 时，要照着社区摸索出的路子走：先手动执行并修正偏差，固化为技能后再进行二次输入测试，最后才能挂载为定时 Routine（https://x.com/Michael_Fenech_/status/2106352565528977469）。如果某一周没有符合退订标准的新邮件，要求 Bot 仅输出一行“本周无新增待退订项目”并立即停止运行，避免无意义的空转消耗。官方安全文档规定，后台或 Routine 触发的审批卡大约 10 分钟就会超时失效，卡片显示 Expired 且动作不会执行（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。所以点击退订链接或清理归档这类操作，千万别指望在后台无人值守时完成。Routine 必须卡在生成待审清单这一步，等人工上线进入会话后再点选批准。

### 成本

官方未公布单次邮件扫描与分类的具体 Token 消耗数字。待测 500 封真实邮件收件箱单次扫描消耗的周额度百分比。

套餐费用方面，自 2026 年 10 月 18 日起，官方正式推出 **The X Subscription 三合一统一订阅**（整合 Grok、Cursor 与 X Premium，https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview，https://x.com/bot/status/2110063783796572496），包含 Grok Bot 权限的档位为 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）**（Free $0 与 Plus $8/月 不含 Grok Bot），三端共享同一个周额度池，超额部分通过预付充值 **Prepaid Credits** 扣减；而既有独立订阅的老用户只要不主动通过 `cursor.com/unify` 单向不可逆地切换至新体系，仍可保留原有的独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）或自助式 Teams（$40/人/月）档位（https://cursor.com/pricing，https://cursor.com/help/grok-bot/plans）。社区帖称在 Pro 档位下每条普通对话约消耗 1% 周额度（个例）（https://x.com/miniyarov/status/2105428357273800799）。每周运行一次退订排查对周额度的占用极小。但千万别设成每 5 分钟轮询一次的高频任务，社区帖称每 5 分钟一次的 Routine 单月触发 8,640 次，按 API 估算折合开销约 397 美元（个例）（https://x.com/fleyta88/status/2109346840382415019）。正如中文社区博主 `@charlie_pmp` 所提醒的（https://x.com/charlie_pmp/status/2114214503416271131），在三合一订阅共享周额度池的机制下，高频且未加精简的冗余 Routine 是后台静默吞噬额度的头号元凶。把这类常规维护任务压到每周一次，或改用 `+alias` 邮件精准触发，是最稳妥的控本方式。

### 坑

清理邮件最大的坑，是云电脑共享环境带来的凭据穿透。官方安全文档指出，用户账号下的所有 Bot 共享同一台云电脑环境，文件、浏览器会话和命令行凭据在所有 Bot 之间互通，删除某个 Bot 也不会清除这些共享状态（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。要是你在邮件助手 Bot 里登录了主邮箱，其他写代码或跑外部脚本的 Bot 同样能拿到该浏览器的登录态。千万别把 Bot 之间的分类当成安全隔离边界。

另一个坑是审批超时导致动作悬空。由于后台审批卡 10 分钟自动过期（https://cursor.com/help/grok-bot/approvals-security-and-privacy），如果把 Routine 设定为“发现垃圾邮件直接弹出退订审批”，人一离开屏幕卡片就会失效，任务根本跑不成。另外，垃圾邮件常包含恶意钓鱼链接，让 Bot 在云端浏览器中无节制点击外链极易遭遇安全风险。必须坚持**草稿优先原则**，在设置中为所有外部请求配置明确的审批卡，决不允许 Bot 绕过人工直接跳转外部退订网页。

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

到了 2026 年 10 月下旬，旅行管家的随身体验迎来了三次质的飞跃：
1. **iOS 原生日历（Calendar）、提醒事项（Reminders）与通讯录（Contacts）直读与操作（v0.75.2）**：官方在 2026 年 10 月 22 日发布的 v0.75.2 更新中，正式为 iPhone 客户端打通了系统级原生日历、提醒事项和通讯录权限（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/mobile）。这意味着旅行管家 Bot 不仅能查 Gmail 里的航司确认信，还能直接核对你 iPhone 本地日历上的私人安排、把值机提醒和行李打包清单直接写进 iOS 原生 Reminders，并从通讯录调取同行亲友或接机司机的联系方式。
2. **iPhone Action Button 一键实时语音通话（iOS v1.16+）**：官方于 10 月 19 日正式上线 Action Button 侧边按钮快捷指令支持（https://cursor.com/help/grok-bot/voice-chat，https://x.com/bot/status/2112246033178968161，获 7,264 赞、2,213 书签；`@SawyerMerritt` 实机演示见 https://x.com/SawyerMerritt/status/2112252980015579431）。在异国街头拖着行李箱赶路时，你无需解锁屏幕打字，只需长按 iPhone 15 Pro 及后续机型的侧边 Action Button（或像 `@D__cup` 那样佩戴 Shokz 骨传导耳机全天候免提唤醒，https://x.com/D__cup/status/2114211130365358350；或参考 `@TyeInBloom` 将 iOS 原生三件套、1Password、Action Button 与 `"Hey Siri"` 快捷指令深度联动，https://x.com/TyeInBloom/status/2113767679588770271），即可直接对旅行管家 Bot 口述：*“我们刚出成田机场海关，帮我看一下去涩谷酒店最快的一班 NEX 成田特快是几点，顺便在日历里把晚餐推迟半小时。”* 通话挂断瞬间，会话流会自动生成带完整逐字稿的 **Voice chat card** 并立即跟进执行（https://cursor.com/help/grok-bot/voice-chat）。
3. **Grok Bot Vault 差旅卡明文 Hint 精准分账（v0.75.5）**：在 10 月 23 日上线的内置加密保险箱 **Vault**（`Settings → Vault`，https://cursor.com/help/grok-bot/secrets，https://x.com/bot/status/2113754107861532677）中，你可以同时保存个人家庭信用卡与公司商务卡，并为商务卡填写明文 **Hint** 标签（例如 `"Use for work travel only"` 或 `"Corporate Amex"`）。由于 Bot 能够读取明文 Hint 却永远看不到加密卡号与 CVV，当你在公务出差与私人顺道度假混合的行程（Bleisure travel）中预订机酒时，Bot 会严格按照 Hint 自动挑选对应的差旅卡或个人卡完成安全注入（`BrowserSecureFill`），彻底杜绝公私账单混刷。

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

如果你已在 iPhone 上授权了 v0.75.2 的 **iOS 原生日历、提醒事项与通讯录**，并配置了 **Vault 差旅卡 Hint**，可以追加如下进阶指令：

```text
Additional iOS & Vault Integration Tasks:
1. Cross-check the extracted flight and hotel windows against my native iOS Calendar to ensure no overlap with existing personal or work appointments.
2. Create a "Tokyo Packing & Check-in" list in my native iOS Reminders with time-based alerts 24 hours before each flight departure.
3. Look up my travel companions' contact details from iOS Contacts and attach emergency contact numbers to the itinerary Page.
4. If I explicitly ask you to book an airport transfer or business hotel extension later, check Settings -> Vault Hints and ONLY select the card with Hint "Use for work travel only" for business days (Oct 20-22), and my personal card for vacation days (Oct 23-25).
```

### Routine

出发前 3 天，可以把行程监控挂载为定时 Routine，设在每天傍晚 18:00 运行一次。让 Bot 自动同步航班动态，拉取目的地未来 24 小时天气情况，并在云电脑内复查 Google Maps 上的实时路况，生成次日出行便签。在 v0.75.2 版本下，全账号所有 Bot 合计可执行 300 次/小时、单条 Routine 最高 200 次/小时（定时最小间隔仍为 5 分钟，https://cursor.com/help/grok-bot/routines），完全足以支撑旅途中的高频航班异动与登机口变更告警。

根据社区推荐的五阶段晋升流程，自动化必须经历验证单次任务、提炼方法、沉淀为技能、换一份输入测试，最后才能设定 Routine（https://x.com/kocer_eth/status/2105008655770788250）。如果当天没有任何航班延误或恶劣天气预警，Routine 只在对话框中给出一行正常确认，绝不重新输出整页冗长的行程单，确保信息流保持清爽。

### 成本

官方未公布多工具交互与地图排期的具体 Token 消耗数字。待测 5 天跨时区行程排期任务中浏览器交互与文本解析的额度消耗。

套餐门槛方面，用户既可选择 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，三端共享周额度池 + Prepaid Credits 预付额度，https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview），老用户也可继续保留既有的独立 Cursor Pro 每月 20 美元套餐（https://cursor.com/pricing，一旦通过 `cursor.com/unify` 切换至三合一订阅则不可逆）。官方帮助文档警告，免费试用是一笔固定用量额度并带有 7 天窗口，长任务有可能在单次执行中耗尽全部试用额度，且官方不予补发（https://cursor.com/help/grok-bot/plans）。在试用阶段测试多步骤旅行规划时，应当尽量限定查询景点的数量，避免一次性派发过于庞大的搜索指令。

### 坑

在云端浏览器中使用地图或查询订票网站时，最常遇到的问题是数据中心 IP 遭遇服务拦截。Grok Bot 的云电脑架设在境外机房，直接访问某些本地化预订平台或交通网站时，往往会被识别为爬虫并弹出难以通过的验证码，甚至直接拒绝连接。此时需要在设置中开启**本地出口路由**（Settings → Computer → Route egress，在最新客户端中也显示为 `Settings > Computer > Your computer > Route traffic through this computer`，https://cursor.com/docs/grok-bot/settings），让云电脑的网络流量绕回你本人的本地设备出口，走真实的个人家庭宽带网络（需要你的桌面电脑开着 Grok Bot 桌面端，或者像 `@ericzakariasson` 分享的那样在家里常开一台 Mac mini 作为远程计算与流量节点，https://x.com/ericzakariasson/status/2114095056630272099）（https://x.com/xiaohu/status/2099409639234289914，以及 `@XueshiQiao` 的实测验证 https://x.com/XueshiQiao/status/2112866936229183589）。

另一个严重风险是证件信息泄露。旅行行程中充斥着护照号码、身份证件、常客卡账号及支付信息。官方安全文档强调，绝不能在常规聊天中明文发送密码、一次性验证码或敏感证件信息（https://cursor.com/help/grok-bot/approvals-security-and-privacy，https://cursor.com/help/grok-bot/secrets）。当预订流程需要登录航司或酒店会员账号、填写真实身份或输入付款信息时，官方现在提供了标准的五级安全登录与四级结账链路（https://cursor.com/docs/grok-bot/work）：你可以使用 **1Password Brokered Sign-in**（在手机或电脑 1Password App 内逐次生物识别审批注入，https://cursor.com/help/grok-bot/connect-apps）、**Grok Bot Vault**（只写加密存储并通过 `BrowserSecureFill` 注入，https://cursor.com/help/grok-bot/secrets）、聊天内掩码 **Secure Form**，或者在 Agent Computer 界面中点击 Take control（Take over screen）人工接管屏幕，手动输完后再交还控制权。但务必注意官方文档与社区博主 `@kial`（https://x.com/kial/status/2114201768414646280）、`@JianWeiSignal`（https://x.com/JianWeiSignal/status/2114195530611855488）共同指出的关键风控边界：**保存在 Vault 中的银行卡在结账自动填充时，不会触发单独的逐笔 Vault 弹窗确认**（https://cursor.com/help/grok-bot/secrets）；如果你希望每笔机酒预订都亲手把关输入卡号，切勿将主力信用卡常驻保存在 Vault 中。此外，模型对机票酒店退改政策容易产生幻觉，在提示词中必须强制要求给出邮件原始出处，不可轻信模型的概括。

## 14.3 孩子学校消息汇总 · School & Family Digest

> [!NOTE]
> 📸 **截图位（待补）**：Bot 从转发的家校通知中提取作业与签字待办项
> [!NOTE]
> 📸 **截图位（待补）**：每日下午生成的结构化家庭待办与日程提醒卡
> [!NOTE]
> 📸 **截图位（待补）**：纠错时 Bot 依据原始通告文件更新日历事项

### 场景

家有学童的家长都知道学校通知有多碎。班级群消息、老师邮件和各类系统通告混在一起，有当晚必须完成的作业，有下周活动的着装说明，还有限时签字和缴费，稍不留神就会遗漏。官方文档在列举典型用例时，重点介绍了**首席幕僚模式**（Chief of Staff）：跨渠道梳理出带有原始出处链接的关键摘要，只提炼符合既定优先级的重要事项，说明原因并给出建议，同时绝不擅自发送对外消息或修改日程（https://cursor.com/help/grok-bot/use-cases）。

官方团队成员在访谈中证实，这种总助模式在早期内测的第二周就自然涌现出来了（https://www.youtube.com/watch?v=maSdsTLaMuU （团队成员访谈））。针对国内学校通知依赖即时通讯工具且无官方插件的现状，社区实践者探索出了可靠的数据入口：利用本地只读工具（如 WeChat Portal）直接读取本地缓存的通告文本（https://x.com/lens2645211/status/2108184037198266383），或者通过自动规则把家校邮件转发到 Bot 的自有邮箱中（https://x.com/bot/status/2108609764766908772）。象鱼工作流在总结国内平台用法时也强调，国内平台没有插件时切忌用 Bot 频繁模拟点击，把文本导出或转发给 Bot 处理是避免账号风控的最佳对策（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

除了每日放学后的常规通告汇总，Grok Bot 在处理**跨周期、高复杂度的家庭重大事项（如身份续签、跨区择校插班、升学备考与家庭事务统筹）**时更能发挥“长期记忆 + 7×24 云电脑”的优势。中文社区博主 0xbitman（`@bitman2140`）在 2026 年 10 月 25 日分享了极具代表性的华人家庭真实案例（https://x.com/bitman2140/status/2114210291546493153）：他一人在 Grok Bot 上同时并行跑通了 8 条端到端生活与工作流，其中前 3 条全部直接服务于家庭与子女教育：
1. **香港优才计划（Quality Migrant Admission Scheme）续签材料跟进**：让专职 Bot 长期追踪香港入境事务处的续签要求清单、在港通常居住证明文件、雇佣合同与税单时间节点，自动比对缺漏材料并生成补件倒计时提醒。
2. **香港孩子学校插班（School Transfer）全流程信息搜集与申请管理**：香港官津、直资与私立学校的春季/秋季插班（叩门）窗口期各不相同且极其分散。`@bitman2140` 让 Grok Bot 持续巡检目标中小学官网的插班招生简章、报名截止日期、笔试/面试科目要求及往年家长面经，汇总成结构化对比表并协助准备申请文书材料包。
3. **孩子日常考试备考辅导**：根据学校公布的教学大纲与测验范围，让 Bot 结合云电脑排版生成针对性的模拟练习题、错题解析与每日复习计划表。

与此同时，在英文社区中，`@Butlergrokbot`（The Butler，https://x.com/Butlergrokbot/status/2111860108070445394）专门展示了基于多条 Grok Bot Routines 构建的**家庭管家（Family Butler）**体系——结合 v0.75.2 新增的 iOS 原生日历与提醒事项同步能力（https://x.ai/changelog/bot），把全家的学校校历、课外兴趣班接送排班、家庭账单到期日与周末采购清单统一收口到一位随叫随到的 AI 家庭总管手中。

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

如果你正在像 `@bitman2140` 一样办理**香港孩子学校插班（School Transfer）与优才续签材料追踪**，可以新建一个独立的家庭专项 Bot 或 Page 看板，使用以下提示词：

```text
You are my HK Family Relocation & School Transfer Coordinator.
Maintain a live Grok Bot Page titled "HK School Transfer & Visa Tracker" and update it based on /workspace/hk_family_docs and official school websites.
Tasks:
1. School Transfer Tracker: Monitor the official admissions pages of our target Hong Kong DSS and government-aided primary schools for mid-year / autumn transfer (插班) openings. Record: School Name | Grade | Application Window | Required Documents | Written/Interview Dates | Source URL.
2. Exam Prep: Based on the syllabus in /workspace/school_inbox, generate a 20-minute daily bilingual (English & Traditional Chinese) practice worksheet for my child.
3. Quality Migrant Visa Renewal: Cross-check our checklist in /workspace/hk_family_docs/visa_checklist.md against expiration dates and alert me 30 days before any residence proof or tax document needs updating.
Standing boundaries:
- Never submit online school application forms or upload identity documents autonomously.
- Every admissions date must include the direct official school webpage URL for human verification.
```

### Routine

将该任务配置为每个工作日下午 16:30 触发的定时 Routine。让 Bot 自动读取当天收纳到文件夹中的所有通告（或转发至 `mybot+school@mail.grokbot.com` 专属别名的家校邮件，https://x.com/SamSokolin/status/2110496237241667621），在半小时内输出一份清晰的三栏待办清单。在 v0.75.2 最新配额下，全账号所有 Bot 合计支持 300 次/小时、单条 Routine 最高支持 200 次/小时运行（定时最小间隔仍为 5 分钟，https://cursor.com/help/grok-bot/routines）。

设计家庭日常 Routine 时，要吸取社区博主 kocer_eth 的警告：定期审计你的 Routine，对于那些虽然每天准时报到、但实际上从没改变过任何实际决策的任务，果断淘汰（https://x.com/kocer_eth/status/2101669438038634827）。如果当天下午学校没有任何新通告，让 Bot 仅发送单行提示“今日无新增学校通告”，坚决不重发旧内容。要是发现 Bot 提取的作业截止时间有误，按社区纠错原则来：当信息有事实出处时，要求 Bot 回查原始文件来源后再回答，而不是让它凭空再猜一次（https://x.com/Michael_Fenech_/status/2106729045878514147）。

### 成本

官方未公布多格式家校通告结构化解析的单次 Token 消耗数字。待测 30 份真实家校通告文本文件夹提炼信息的周额度消耗。

个人套餐方面，新订户可开通 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，三端共享周额度池 + Prepaid Credits 预付额度，https://cursor.com/help/grok-bot/plans），既有老订户仍可维持独立 Cursor Pro 每月 20 美元套餐（https://cursor.com/pricing，通过 `cursor.com/unify` 切换至三合一订阅后不可退回）。社区用户抱怨称，如果盲目建立多个 Bot 并不停轮询，往往只撑两天就会把每周额度打光，而随后的按需付费或额外充值相当昂贵（https://x.com/RichSilver/status/2108053489620504822，https://x.com/charlie_pmp/status/2114214503416271131）。对于学校消息汇总，工作日每天傍晚只跑一次，既能确保信息零遗漏，又几乎不产生额外的额度压力。

### 坑

在家庭信息处理中，最大的隐患是隐私数据在多 Bot 间无序共享。Shane Mac 曾遭遇过惨痛事故：他的个人财务 Bot 把包含月度银行账单和刷卡支出的个人审计结果，直接发到了公司高管的公用 Slack 频道中，根源就在于不同 Bot 共用同一台云电脑，聊天会话发生混淆（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。学校通告以及优才续签、插班申请材料中包含孩子的全名、出生证明、护照/港澳通行证号、班级学号、家庭住址和家长电话，这些信息如果长期堆放在云电脑的公共根目录，很容易被其他用于业务测试的 Bot 读取甚至误传。每次处理完通知后，必须按照官方安全规范及时从工作空间清理包含隐私的临时文件（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。

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

而在 2026 年 10 月 14 日至 10 月 23 日短短十天内，Grok Bot 的个人购物与支付基础设施完成了一次从底层凭据到兜底保障的全面革新（https://x.ai/changelog/bot，https://cursor.com/docs/grok-bot/work）：
1. **官方标准四级结账链路与五级登录链路正式成型**：根据官方最新 [Work 技术文档](https://cursor.com/docs/grok-bot/work) 与 [Secrets & Vault 帮助文档](https://cursor.com/help/grok-bot/secrets)，现在当 Bot 帮你网购下单时，不再局限于早期单一的手动接管屏幕，而是遵循严谨的优先级调用链：
   - **网站登录（Sign-in）五级优先级**：云电脑已保存的浏览器会话（Saved browser session） → **Grok Bot Vault** → **1Password（Brokered Sign-in 逐次生物识别授权）** → 聊天内掩码 **Secure Form** → **Take over screen（人工接管屏幕）**。
   - **结账付款（Checkout / Payment）四级优先级**：**Grok Bot Vault**（内置加密保险箱，支持手机摄像头扫卡录入与 `BrowserSecureFill` 零明文注入，https://x.com/bot/status/2113754107861532677） → 聊天内掩码 **Secure Form** → **Link / X Money**（v0.71.2 正式支持；如 `@gofordylan` 实测晒单所示，使用 X Card 经由 Grok Bot 付款后，账单流水旁会点亮专属的 Grok Bot 小徽章，https://x.com/gofordylan/status/2110726444485607797） → **Take over screen（人工接管屏幕）**。
2. **Elon Musk 宣布 SpaceX 全额赔付兜底背书**：针对许多用户对“让 AI 绑卡代购万一买错东西或泄露卡号怎么办”的顾虑，2026 年 10 月 15 日，Elon Musk（`@elonmusk`）公开发帖做出硬核承诺（https://x.com/elonmusk/status/2110610960474079445，获 17,221 赞、1,686 转发、2,128 书签）：*"This works well. If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole."*（这套机制非常好用。如果 Grok Bot 在代购时犯错或泄露了你的银行卡——迄今从未发生过——SpaceX 将为你全额赔付。）
3. **清晨按一下 Action Button 给妻子点一杯热星巴克**：有了 iPhone Action Button 一键语音（v1.16+，https://x.com/bot/status/2112246033178968161）与 1Password 免密代理登录（https://x.com/bot/status/2113301060811161874，https://x.com/1Password/status/2113276767582498943），日常高频小额消费变得充满温情。社区开发者 `@JCOMBuilds` 在 2026 年 10 月 21 日分享了他的每日晨间习惯（https://x.com/JCOMBuilds/status/2112997408510452123）：每天早晨起床，他只需长按 iPhone 侧边的 Action Button，对着自己的个人助理 Bot `"Eve"` 说一句给妻子点星巴克咖啡；`"Eve"` 随即在云电脑里打开点单页面，请求调用存储在 1Password 里的账号凭据，他在手机上轻轻一点生物识别批准，Bot 便自动选好常喝的口味与门店完成下单准备。

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

如果你想复刻 `@JCOMBuilds` 的 **Action Button 语音召唤 + 1Password / Vault 快速复购（如点星巴克或日用品补货）**，可以将以下 SOP 写入你的个人助理 Bot：

```text
You are Eve, my Personal Coffee & Daily Reorder Assistant.
When I trigger a voice chat via my iPhone Action Button asking to order coffee or reorder household staples:
1. Sign-in flow: Follow the official priority order — use saved browser session first, or request my login via 1Password Brokered Sign-in (wait for my Review in 1Password biometric approval). Never ask me to type passwords in chat.
2. Order configuration: Select my saved default store address (from Settings -> Vault Contact info) and load my wife's favorite Starbucks order (or specified item).
3. Checkout & Approval gate: Stop at the final checkout screen, verify the item, store location, pickup time, and total price, and trigger an explicit purchase approval card before completing payment via Vault / Link / X Money.
```

### Routine

按照官方 Haggle Bot 的运行范式，系统应当围绕真实变动而非高频轮询展开（https://x.ai/news/grok-bot-procurement）。比价 Routine 可以设定为每天早晚各运行一次（上午 10:00 与晚上 20:00），避开凌晨无促销变动的时段。

官方文档规定，Routine 定时最小间隔为 5 分钟，v0.75.2 起全账号所有 Bot 合计上限为 300 次/小时、单条 Routine 最高 200 次/小时（https://cursor.com/help/grok-bot/routines），且当用户长时间不活跃时，系统可能会询问并自动暂停 Routine，以控制无人值守时的消耗（https://cursor.com/help/grok-bot/skills-routines-and-automations）。当 Bot 巡检发现某平台价格击穿目标阈值时，Routine 会在对话流中生成购买审批卡，列清含税总价与直达购买链接；如果价格未达标，则静默记录日志并退出，绝不打扰人。

### 成本

官方 Haggle Bot 采购案例展示了 58% 的价格缩减成果（订单金额从 14,629 美元降至 6,143 美元）（https://x.ai/news/grok-bot-procurement）。关于个人日常商品爬取与比价的实际 Token 消耗，官方未公布具体数字。待测 4 家主流电商网站持续巡检 14 天的周用量占比。

软件服务成本方面，新用户可通过 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，三端共享周额度池 + Prepaid Credits 预付额度，https://cursor.com/help/grok-bot/plans）获取权限，老用户也可保留既有的独立 Cursor Pro 套餐每月 20 美元（https://cursor.com/pricing，一旦在 `cursor.com/unify` 单向升级至三合一订阅则无法退回旧计划）。必须警惕过度监控带来的隐形成本：社区帖称如果将 Routine 设为每 5 分钟一次的高频轮询，一个月 8,640 次触发按 API 估算可烧掉约 397 美元（个例）（https://x.com/fleyta88/status/2109346840382415019）。每天早晚各巡检一次，或者像本书作者 Mr.鼓先生（`@StarkLJM`）在榜单监控实战中所演示的那样——让 AI 花 28.6 秒写好确定性的 Python 价格抓取脚本，日常用脚本零 Token 额度跑轮询，仅在发现降价时才唤醒大模型处理（https://x.com/starkljm/status/2111803996734419377），即可在额度极省的前提下覆盖绝大多数日常降价活动。

### 坑

在涉及真实资金交易的场景中，资产安全是绝不可退让的底线。官方安全与审批文档明确规定，购买与资金转移属于高危动作，必须始终置于显式审批边界之后（https://cursor.com/help/grok-bot/approvals-security-and-privacy，https://cursor.com/docs/grok-bot/security）。尽管社交平台上曾有拍信用卡照片发进聊天窗口给 Bot 的旧说法，但 @grok 的这条回复也提醒，隐私政策建议不要在提示词里放信用卡等敏感信息（https://x.com/i/status/2109347617398264294）。如今在 v0.75.5 体系下，官方已将结账流程升级为 **`Vault → Secure Form → Link / X Money → Take over screen` 四级安全结账链路**（https://cursor.com/docs/grok-bot/work，https://cursor.com/help/grok-bot/secrets）：如果你确实需要扫卡录入，只能进入 `Settings → Vault → Add card` 使用官方加密摄像头扫描（数据只写加密、Bot 永远看不到完整卡号与 CVV），或通过聊天内掩码 Secure Form、Link / X Money，以及在 Agent Computer 界面执行**人工接管控制权（Take over screen）**由用户本人手动完成付款确认，绝不能在常规聊天框中明文发送任何付款卡号或安全码（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。

**尤其需要再次敲响警钟的是 Vault 存卡与不存卡的审批差异**：正如官方 [Secrets & Vault 帮助文档](https://cursor.com/help/grok-bot/secrets) 所明确记载，以及英文社区 `@kial`（https://x.com/kial/status/2114201768414646280）与中文社区 `@JianWeiSignal`（见微｜Signal，https://x.com/JianWeiSignal/status/2114195530611855488，https://x.com/JianWeiSignal/status/2114195638988501103）重点警示的那样——**保存在 Grok Bot Vault 中的银行卡，在结账自动填充（`BrowserSecureFill`）时不会弹出单独的逐笔 Vault 卡片填充确认框**，仅受通用购买审批规则约束！因此，这里强烈建议遵循社区总结的两条风控铁律：
- 如果你希望对每一笔消费都保持最高级别的手动把关，**切勿将主力大额信用卡常驻保存在 Vault 中**（或在用完后从 `Settings → Vault` 中移除，改用每次结账弹出聊天内 Secure Form 时单次输入且不勾选保存，或只放一张限额的虚拟卡/预付卡）。
- 如果你同时使用 1Password 与 Grok Bot Vault，可以采纳 `@martinpaulweiss` 提出的 **“一密一宅（One home per secret）”拆分法**（https://x.com/martinpaulweiss/status/2114210343467536531）：日常电商与网站登录凭据（连同 2FA 动态验证码）统一存放在 1Password 中，通过 Brokered Sign-in 逐次审批调用；Grok Bot Vault 仅存放常用收货地址与专门用于小额代购的独立卡片，并使用 `@LisaMAUSA` 分享的 **Vault Tidy** 思路定期清理重复条目（https://x.com/LisaMAUSA/status/2114208018388643852）。

第二个坑是电商网站的反爬与风控封号。主流电商平台对机房 IP 的识别非常严格，Bot 频繁在云电脑中打开商品页极易触发滑动验证码或人机校验。遇到风控时，强行让 Bot 自动化重试很容易导致电商账号被封禁，此时必须配合本地出口路由（`Settings > Computer > Your computer > Route traffic through this computer`）将流量转回个人本机住宅 IP（https://x.com/xiaohu/status/2099409639234289914，https://x.com/XueshiQiao/status/2112866936229183589）。第三个坑是限时特价与审批超时冲突。官方后台审批卡大约 10 分钟自动过期（Expired）（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。如果遇到库存极少的闪购特价，一旦没能在 10 分钟内点击 Allow once，卡片就会失效并取消操作。高时效性的秒杀抢购并不适合离线 Routine，必须在人守在屏幕前时以人机协同的方式半自动完成。

---

[← 上一章：§13 编制案例库 · Team Blueprints](../part4-multi-bot/13-blueprints.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§15 内容创作 · Creators →](../part5-use-cases/15-creators.md)

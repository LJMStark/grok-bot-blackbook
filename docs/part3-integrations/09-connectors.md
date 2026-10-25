# §09 连接器与 Marketplace · Connectors

[← 上一章：§08 审批与安全边界 · Approvals & Safety](../part2-core-concepts/08-approvals-safety.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§10 官方合作集成逐个讲 · Partner Integrations →](../part3-integrations/10-partners.md)

---

## 9.1 Marketplace、Plugins 与 @ 的用法 · Marketplace, Plugins & The @ Symbol

假设你刚看文档时，最容易被界面上的几个词搞晕：一会儿是 Marketplace，一会儿是 Plugins，一会儿又是 Connect Apps。新手很容易以为 Marketplace 像手机应用商店，点进去就能给 Bot 装各种底层 API 插件。但官方页面的定位完全不同（详见官方连接器帮助文档 [https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。

先厘清时间线：客户端里的 Marketplace 早期同时列插件和 Bot 模板；9 月 29 日起客户端 Marketplace 只放插件，10 月 2 日改名 **Connect Apps**，Bot 模板挪到网页上（https://x.ai/changelog/bot）。所以现在：**客户端 Connect Apps = 装插件（连接器）**；**网页 x.ai/bot/marketplace = Bot 模板集市**（https://x.ai/bot/marketplace）。下面先说网页版模板集市。页面按部门分类：官方团队、工程、销售、市场、设计、个人、招聘、产品、运营。比如官方做的外联获客 Bot「Outbound Prospecting」（Krista Letz 开发）、内容策划 Bot「SEO & AEO Desk」（Adam Tanguay 开发）、采购谈判 Bot「Haggle Bot」（Daniel Gartshein 开发）、面试协调 Bot「Recruiting Coordinator」（Tommy Hansen 开发）；还有社区开发者提交的模板，像打包外部 API 的「tinkabot」（Lauren Tan 开发）、管理编码代理的代码主管「Lingxi's Engineer Bot」（Lingxi Li 开发）、设计走查「Critiquito」、组织治理「Alfred」（Robin Delta 开发）。此外，社区创作者 `@LisaMAUSA` 也在 `@leerob` 的 $100 X Money 真实反馈悬赏帖（[https://x.com/leerob/status/2113792409448714468](https://x.com/leerob/status/2113792409448714468)）下分享了两个可直接复用的热门模板（[https://x.com/LisaMAUSA/status/2114208018388643852](https://x.com/LisaMAUSA/status/2114208018388643852)）：用于安全扫描并去重 Vault 内已保存登录与银行卡条目的 **Vault Tidy**，以及仅针对 MP4 成片单镜头进行局部修补替换、无需重渲整片的 **SceneEdit Video Studio**。在 Marketplace 里点添加，复制到工作区的只是一份包含角色设定、规则、提示词和既定流程的 Bot 配置副本，并不会直接打通个人账号的外部应用授权。

真正面向代码和终端环境的插件生态，是官方 2026 年 6 月 11 日推出的 Grok Build Plugin Marketplace（https://x.ai/news/grok-plugin-marketplace）。这是内置在终端开发环境里的插件体系，开源目录在 GitHub 的 xai-org/plugin-marketplace。它把 skills、斜杠命令、agents、hooks、MCP 服务和语言服务协议 LSPs 打包成规范的安装包，支持终端输入 `/marketplace` 浏览，或者运行命令：

```text
grok plugin marketplace list
grok plugin install <name> --trust
```

上线时首批生态伙伴包括 MongoDB、Vercel、Sentry、Chrome DevTools、Cloudflare 和 Superpowers。目录里的远程插件都严格锁定了特定的 commit SHA，安装阶段会做哈希完整性校验。

平时在桌面客户端里让 Bot 读邮件、查日历、提代码的入口到底在哪？在客户端左侧边栏底部的 Connect Apps（详见官方连接器指南 [https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps) 与第三方整理 [https://learngrokbot.com/plugins](https://learngrokbot.com/plugins)）。早期有些二手网帖把它混称为 Marketplace 或设置里的 Plugins，容易让人在设置面板里白转悠。其实它就固定在左侧边栏最下方，排在所有 Bot 列表下面（在设置菜单中也对应 `Settings → Connect apps`）。在这里配的插件是账号级的：属于当前 Cursor 或 Grok Bot 账户（包括统一后的 **The X Subscription** 账户，含 Premium $30/月、Super $100/月、Ultra $200/月三档，详见 [https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans) 与 [https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)），连上一次，名下每个 Bot 都能用，不用挨个登录。

通过 Connect Apps 连接应用，流程分四步（来源：learngrokbot.com/plugins 及官方文档 [https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）：
1. 点击侧边栏底部的 Connect apps 按钮唤出弹窗。
2. 搜索应用名或点分类标签，点击旁边的 Add。密码管理器 1Password 显示为 Connect，系统自带的 GitHub 显示为 Connect GitHub。
3. 默认浏览器会自动打开对应应用的官方授权页。像 Google 授权页会提示正连接至 Grok 或 Cursor，需要在十分钟内完成确认并关闭页面。
4. 回到客户端检查插件列表的最终状态。

这里最容易踩的坑是：**Added 不等于 Connected**（来源：learngrokbot.com/plugins）。在管理面板里看到 Added，只代表插件装进了环境配置，还没登录成功。点进详情页，账户行还是 Needs auth，旁边挂着 Authenticate 按钮。这时候让 Bot 干活，Bot 会直接报错说找不到应用或缺少授权。只有变成绿色的 Connected，凭证才算生效。以后如果授权因令牌过期失效，不用卸载重装，在详情页重新点 Authenticate 走一遍浏览器确认就行。要同时管理多个账号，比如工作专用的 Notion 和个人笔记 Notion，点 Add Another Account 分别绑定打标签，跟 Bot 说明「使用我的工作 Notion」即可路由。详情页里的 Tools 行还能单独关掉敏感权限。如果用的是 Cursor Teams 方案（旧版独立自助式 Teams $40/人/月）或企业版（[https://cursor.com/docs/grok-bot/teams](https://cursor.com/docs/grok-bot/teams)），管理员也可以后台统一禁用，客户端会显示 Disabled by team admin。

授权完成后，对话里调用插件最直接的办法是打 `@`（来源：learngrokbot.com/plugins）。在输入框敲 `@` 会弹出一个浮层，里面有连好的插件和技能，点选就能把任务派给它。没提前连也没关系，直接跟 Bot 说查日程，Bot 发现没授权会在对话框里甩出一张带 Authorize 按钮的卡片，点卡片原地跳浏览器登录。

随着 2026 年 10 月中下旬 v0.71.2、v0.75.2 与 v0.75.5 版本的连续迭代（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)），通过 `@` 符号唤起或系统级直连的核心连接器迎来了三项重大升级：

1. **`@chat`（X 端到端加密私信与陌生人消息请求连接器）**：2026 年 10 月 16 日，X 与 Grok Bot 工程师 Paul Vann（`@pjvann`）正式发布 `@chat` 连接能力（[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)，获 1,069 赞、108 转发、132 书签）。现在在对话框中输入 `@chat`，Grok Bot 即可直接访问你在 X 上的端到端加密私信收件箱（XChat inbox）以及陌生人发来的消息请求（message requests）。`@pjvann` 分享了他自己的真实用法：整周让 `@bot` 自动排查、过滤垃圾骚扰，并逐条审查批准高质量的陌生人私信请求、代写得体回复。
2. **`@1Password` 新版 Brokered Sign-in（代理逐次授权免密登录）**：2026 年 10 月 22 日（v0.75.2），Grok Bot 与 1Password 官方联合推出基于 `"1Password for Agents"` 架构的全新 `@1Password` 连接方式（官方公告 [https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874)，3,663 赞 / 964 书签；`@1Password` 官宣帖 [https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)，10,507 赞 / 1,076 转发 / 7,122 书签；文档见 [https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps) 与 [https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。只要本机安装了 **1Password app 8.12.42 或更高版本**，通过 `Settings → Connect apps → 1Password → Connect` 绑定后，Bot 在浏览器遇到登录框时会弹出 **Review in 1Password** 请求，你在电脑或手机上用指纹/面容批准一次，1Password 就会把你 **Personal / Private（个人/私有密码库）** 中的凭据直接安全注入浏览器，**彻底告别了手工新建共享 Vault 和配置 Service Account 令牌的繁琐流程**，且 Bot 全程看不到明文密码。
3. **iOS 原生 Calendar / Reminders / Contacts 系统级连接器**：在 v0.75.2（2026-10-22，[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与 iOS 客户端 v1.16+（[https://cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）中，Grok Bot iPhone 端新增了对苹果原生 **Calendar（日历）**、**Reminders（提醒事项）** 与 **Contacts（通讯录）** 的系统级本地授权直连。无需折腾云端 OAuth 转发，只要在 iPhone 上授予系统权限，Bot 就能直接读取和写入你手机自带的日程表、待办清单与联系人名录。社区玩家 `@TyeInBloom`（[https://x.com/TyeInBloom/status/2113767679588770271](https://x.com/TyeInBloom/status/2113767679588770271)）将这套 iOS 原生三件套连接器与 `@1Password` 逐次授权登录、iPhone Action Button 侧键一键语音通话（[https://cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)）以及 `"Hey Siri"` 快捷指令结合，打造出了远超系统自带语音助手的全能随身秘书；`@JCOMBuilds`（[https://x.com/JCOMBuilds/status/2112997408510452123](https://x.com/JCOMBuilds/status/2112997408510452123)）则每天早晨按一下 Action Button 呼出个人助理 Bot `"Eve"`，自动调取 1Password 里的星巴克账号为妻子下单咖啡。

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 侧边栏 Connect Apps 入口、搜索与分类弹窗、Manage plugins 状态页面及聊天中 @ 唤起插件浮层

用 @ 调用插件并完成 OAuth 授权的流程。

## 9.2 连接器总览（上百个，按类别）· Catalog

连接器到底有多少个？网上说法差别很大：有人发帖说 110 个，有人说 219 个，第三方指南还写过 238 个。对比研究记录来看，主要是统计口径冲突。

官方 2026 年 5 月 6 日发过一篇 Grok 应用（不是 Grok Bot，那时 Grok Bot 还没发布）的连接器公告（https://x.ai/news/grok-connectors），列的是 SharePoint、Outlook、OneDrive、Google Workspace、Notion、GitHub、Linear 和 Bring Your Own MCP，没公布过固定总数；官方 Marketplace 页面（https://x.ai/bot/marketplace）展示的又全是 Bot 角色模板。民间统计里，社区帖称有 110 个连接器（个例），包含 88 个官方与 22 个自定义 MCP（https://x.com/1920web1080/status/2107160327112777835）；GitHub 上的 awesome-grok-bot-plugins 仓库（https://github.com/rdmgator12/awesome-grok-bot-plugins）2026 年 8 月 12 日快照收录了 219 个；第三方站 learngrokbot.com（https://learngrokbot.com/plugins）10 月 6 日清单列了 238 个，但这数字是把十个分类直接累加，算进了跨分类重复项。目前严谨的说法只能是**上百个**，没有官方固定的个位数值（官方最新连接器指南详见 [https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。

参考 learngrokbot.com 整理的清单（来源：learngrokbot.com/plugins https://learngrokbot.com/plugins ）与官方最新文档（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)），整个生态大致涵盖十个方向，文档和社区里记录了不少限制和细节：

密码管理类目前只有一家：1Password（官方更新日志见 2026 年 9 月 17 日 @bot 账号公告，转述见 enterprise.md；用法见 learngrokbot.com/plugins）。它的隔离设计很特殊：点击 Connect 授权后，1Password 会在后台建一个名为「Shared with Grok Bot」的专属保险库。Bot 碰不到个人主保险库，只能读取你手动放进共享保险库的条目。老企业后台或者没做插件的网站，把账号密码放进这个保险库让 Bot 代登，是最稳妥的办法。

> **2026-10-23 重磅更新：1Password 新旧两代模式并存 + Grok Bot Vault 内置保险箱上线**
> - **1Password 新版 Brokered Sign-in vs 旧版共享 Vault**：自 2026 年 10 月 22 日（v0.75.2，[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）起，1Password 连接器升级为 **Brokered approval（代理逐次审批）** 模式（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。新版默认直接从你已连接 1Password 账号的 **Personal / Private vault（个人/私有密码库）** 中按需请求条目（存放在 Shared 或自定义密码库中的条目在新版模式下不会被读取，除非移入 Personal / Private 库），每次填充由你在 1Password App（需 v8.12.42+）上生物识别审批。此前使用旧版 `Shared with Grok Bot` 共享库 + Service Account Token 方案的老用户，只需在 `Settings → Connect apps` 中选择 **Disconnect（断开）** 再 **Reconnect（重新连接）** 1Password，即可一键升级到新版逐次授权模式。例如中文社区博主 `@oxpsats`（偶像派作手，[https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670)）就通过 1Password 授权彭博社（Bloomberg）会员凭据，让 Bot 全自动突破付费墙抓取并精读海外核心财经研报。
> - **Grok Bot Vault 内置保险箱与登录/结账优先级**：v0.75.5（2026-10-23，[https://x.com/bot/status/2113754107861532677](https://x.com/bot/status/2113754107861532677)，9,398 赞 / 2,756 书签）还在 `Settings → Vault` 中推出了原生只写（write-only）加密保险箱（详见官方说明 [https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)），支持存储 **Logins（含 2FA/TOTP）**、**Cards（支持手机摄像头 Scan 扫卡）** 与 **Contact info（收货地址/电话/邮箱）**，并支持导入 **5 MB** 以内的 1Password、Chrome、Safari、Firefox、Bitwarden 或 LastPass CSV 文件，每个条目可附带一段供 Bot 识别用途的明文 **Hint**。根据官方工作流技术文档（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)），Bot 遇到登录框时的调用优先级顺序为：**已保存的云端浏览器会话（Saved browser session） → Vault → 1Password → 聊天内 Secure Form → Take over screen（人工接管屏幕）**。社区安全专家 `@martinpaulweiss`（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）总结了“一密一宅（One home per secret）”黄金拆分法则：日常网站账号密码连同 2FA 统一放在 1Password 中，而 Grok Bot 内置 Vault 只存收货地址或专门划拨的消费卡。

办公生产力类包括 Notion、Linear、Airtable、Asana、ClickUp、Coda、Monday.com、Todoist、Zapier、Box、Miro、Smartsheet 等。这里有个容易混淆的点：第三方清单称 Google 办公套件只列了 Google Docs 和 Google Slides，没有名为 Google Drive 或 Google Sheets 的插件（来源：learngrokbot.com/plugins）。但官方 changelog 9 月 15 日写着 "Bots can upload files to Google Drive or OneDrive"，10 月 7 日又支持交付 Google Slides（https://x.ai/changelog/bot）——说明至少上传到 Drive 是支持的。Sheets 能否原生读写，以你客户端里 Connect Apps 的实际搜索结果为准；不行就走浏览器或导出 CSV/Excel。此外，在手机端（iOS v1.16+，对应 v0.75.2），苹果原生的 **Calendar（日历）**、**Reminders（提醒事项）** 与 **Contacts（通讯录）** 也已加入移动办公连接阵营（[https://cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）。

通讯协作类包含 Gmail、Google Calendar、Slack、X 以及微软组件。注意微软没给打包的 Microsoft 365 插件，而是拆成了 Outlook、Outlook Calendar、OneDrive、Teams 四个独立插件（来源：learngrokbot.com/plugins）。加了邮件不等于加了日历，得分别配。而在邮件连接器与专属 `@mail.grokbot.com` 邮箱（[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)）方面，10 月 14 日工程师 `@SamSokolin` 发布了 **`+alias` 加号子别名**与按别名定向触发 Routine 的功能（[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)，3,073 赞 / 1,197 书签），v0.75.2 又新增了**邮件原样转发保留完整 HTML、正文内嵌图片与附件**的能力（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。沟通类应用有两个风险：Zoom 插件授权常报 4700 错误（Invalid redirect），属于已知故障，客户端暂时无解；另外 WhatsApp 和 LinkedIn 没有原生插件，社区帖称有用户让 Bot 用云电脑浏览器接管 WhatsApp 发信被封号（个例，Reddit 讨论帖：https://www.reddit.com/r/GrokBot/comments/1w11r70/），也有社区帖称在 LinkedIn 上自动化发消息导致会话被强制下线（个例，Reddit 讨论帖：https://www.reddit.com/r/GrokBot/comments/1wp291u/）。连 X 插件会自动开通开发者账号并扣 API 点数，付费套餐里送了初始额度。

> **X 插件（`x-api-mcp-guide`）2026-10 全面扩容工具矩阵与计费说明**
> 经过 10 月中下旬的连续升级，X 插件已从基础的发帖与检索进化为覆盖 X 全生态的超级连接器：
> 1. **公开检索与读取（内置免费）**：包括 `search_posts_recent`、`search_posts_all`、`get_posts_by_ids`、`get_users_by_ids`、`get_users_posts`、`get_users_mentions`、`get_post_Thread`、`get_article`。Grok Bot 内置的公开 X 数据读取完全免费包含在订阅内；通过 X 插件访问私有账号数据则依据官方连接器文档（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）说明可能需要 `https://console.x.com` 的 X API 额度。
> 2. **Spaces、Communities、Lists 与书签文件夹**：完整支持语音空间（Spaces）检索管理、社群（Communities）互动、列表（Lists）读取与成员增删写入，以及个人书签与书签文件夹（Bookmarks & bookmark folders）的分类调取。
> 3. **X Chat（`@chat` 端到端加密私信与本地沙箱解密架构）**：如 `@pjvann` 所宣布（[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)），Bot 可读取未读私信、审批陌生人消息请求（message requests）并发送回复。由于 X Chat 采用端到端加密（`xchat_lite`），MCP 接口只返回加密载荷与 Juicebox 密钥恢复配置；Grok Bot 会在云端沙箱本地克隆官方开源工具库 [https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper) 并执行 `xchat_tool.py`，配合用户提供的 **4 位数字 X Chat PIN 码**在沙箱内完成本地解密与加密发信。
> 4. **Scheduled X Calls（预约通话）**：支持调用 `schedule_call`、`list_scheduled_calls` 等工具创建、查看及回复（RSVP）X 预约音视频通话。
> 5. **Livestreams（RTMP/RTMPS 直播推流与弹幕治理）**：支持创建和管理 RTMP/RTMPS 推流源（stream sources）、预约直播广播（scheduled broadcasts）、在直播结束后自动抓取并总结弹幕聊天记录（summarize ended broadcast chat），以及任免直播间房管（moderators）与管理禁言名单（mutes）。如果发现 Chat、Call、Livestream、Spaces 或 Lists 工具缺失而其他 X 工具正常，只需在 `Connect Apps` 中重新连接（Reconnect）X 插件即可刷出全量工具。

代码工程类自带 GitHub 插件，按钮直接叫 Connect GitHub，没有卸载选项（来源：learngrokbot.com/plugins）。另外有 Vercel、Sentry、MongoDB、Docker、Cloudflare、Supabase、Postman、Temporal、Datadog 等。10 月 1 日官方宣布 Bot 可以把编码任务交给 Cursor、用 GitHub 和 Origin 插件管理 PR（https://x.com/bot/status/2105373767568621895）；9 月 17 日 changelog 也扩展了 releases、tags、labels、PR review 等 GitHub 能力（https://x.ai/changelog/bot）。

数据分析类包含 Amplitude、Snowflake、PostHog、Hex、ClickHouse、dbt Labs、Grafana 等。官方企业用例公布过内部数据团队的做法：用只读凭证连 Databricks，配合 Hex 和 Statsig，让 Bot 跑覆盖数万张数据表的复杂查询（来源：enterprise.md；https://x.ai/news/team-bots）。配合 v0.75.2 上线的 **Pages（Canvas）** 功能（[https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)），Bot 还能把从这些数据连接器查出来的指标直接渲染成可持续热更新的实时看板 Page，并按 **Only you**、**Your team** 或 **Anyone with the link** 三级权限分享。

销售获客类覆盖 Salesforce、HubSpot、Gong、Apollo.io、Clay、Outreach 等。官方企业版公告举的例子是：通话中 Bot 根据实时笔记更新演示文稿；招聘场景下根据当天的 Gong 通话提交面试评分卡（来源：https://x.ai/news/grok-bot-for-enterprise）。社区增长博主 `@milesdeutscher` 在其获 3,100 赞、4,503 书签的“10 大逆天 Grok Bot 用例”长推中（[https://x.com/milesdeutscher/status/2113653680834859262](https://x.com/milesdeutscher/status/2113653680834859262) 及 #8 子帖 [https://x.com/milesdeutscher/status/2113653741647999378](https://x.com/milesdeutscher/status/2113653741647999378)），还展示了如何让 Grok Bot 直接替代昂贵的 Apollo 订阅，根据理想客户画像（ICP）全自动抓取并清洗潜在客户名单。

财务交易类中，官方 2026 年 9 月 27 日发布了只读的 Finance 插件，通过 Plaid 连接银行卡和投资账户（官方 X 帖子：https://x.com/bot/status/2103936247995752705）；10 月 9 日上线了 Shopify 插件，能查订单、追库存、同步商品（官方 X 帖子：https://x.com/bot/status/2108228871938359347）。此外还有 Stripe、Ramp、Brex、Xero。而在主动结账与支付集成方面，v0.71.2（2026-10-14，[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）正式打通了 **Link** 与 **X Money** 结账支付（官方结账调用优先级为：**Vault → 聊天内 Secure Form → Link / X Money → Take over screen**，详见 [https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。使用 X Card 经由 Grok Bot 完成的交易，在账单流水中还会显示一枚专属的 Grok Bot 小徽章（参见 `@gofordylan` 实测晒单：[https://x.com/gofordylan/status/2110726444485607797](https://x.com/gofordylan/status/2110726444485607797)）。2026 年 10 月 15 日，Elon Musk（`@elonmusk`）公开为代购与绑卡安全做出兜底赔付承诺（[https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445)，17,221 赞 / 1,686 转发 / 2,128 书签）：*"This works well. If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole."*（如果 Grok Bot 在代购时出错或泄露了你的银行卡——迄今从未发生过——SpaceX 将全额赔付。）

碰财务数据与支付授权时，必须牢记两道安全红线：第一，只读接口管不住数据外发——XMTP Labs CEO Shane Mac 遇到过事故，Grok Bot 以他的身份把包含银行余额和消费明细的月度财务审计发进了公司 Slack 频道（事故报道：https://cybernews.com/ai-news/grok-bot-leaks-bank-information/；https://runtimewire.com/article/xmtp-shane-mac-grok-bot-bank-audit-slack），只读接口管不住 Bot 把读到的数据发到外网，关键操作必须加人工确认；第二，**保存在 Vault 中的银行卡在结账填充时不会触发单独的逐笔 Vault 弹窗确认**——正如官方文档 [https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets) 所明确记载，以及中英文社区博主 `@JianWeiSignal`（见微｜Signal，[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)）与 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）同步发出的预警：一旦把银行卡存入 Vault，结账自动填充时仅受通用购买审批规则约束，不会再弹出单独的逐单 Vault 卡片确认框。如果你希望每一笔消费都必须亲手输入卡号并逐单确认，**切勿将主力信用卡常驻保存在 Vault 中**，而应使用每次弹出的聊天内掩码安全表单（Secure Form）单次输入且不勾选保存。

除了官方目录，Grok 还支持 Bring Your Own MCP（来源：https://x.ai/news/grok-connectors）。企业内网接口或自建数据库不用等官方做插件。Connect Apps 界面没有输入框，加自定义 MCP 靠直接在对话框里发指令（来源：learngrokbot.com/plugins https://learngrokbot.com/plugins）：

```text
Add this MCP server: https://your-app.example.com/mcp
```

Bot 收到后会让你确认服务信息并完成挂载。两个硬性条件：第一，地址必须是公网 HTTPS，Bot 跑在云端虚拟机里，访问不到本机的 localhost（社区硬件极客 `@guoxudong_` 在 [https://x.com/guoxudong_/status/2111767457560215771](https://x.com/guoxudong_/status/2111767457560215771) 中就利用 Cloudflare Tunnel 将运行在本地 Mac 上的自定义 MCP Server 暴露为安全 HTTPS 端点，仅用 2 分钟便跑通了 `ESP32 硬件语音盒子 → Cloudflare Tunnel → Mac 本地语音转文字 → 本地 MCP Server → Cloudflare Tunnel → 云端 Grok Bot` 的全链路；而在 `@leerob` 的 $100 X Money 反馈悬赏帖 [https://x.com/leerob/status/2113792409448714468](https://x.com/leerob/status/2113792409448714468) 评论区中，更直观的自定义 MCP 连接器配置面板与更丰富的协议生态也是重度用户呼声最高的特性之一）；第二，挂载后全账户共享，名下所有 Bot 都能调。

对于企业与团队安全治理而言，自定义 MCP 服务绝不能成为绕过内网防火墙的暗道。根据官方最新安全架构文档（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)），企业管理员不仅可以将云端虚拟机（cloud box）的出站网络流量严格限制在自定义域名白名单内（格式如 `*.domain.com:443`），现在还可以在安全设置中勾选 **`Apply to MCP servers`** 选项，将该出站网络白名单**同步强制应用于所有 MCP 服务器的调用请求**。结合团队自定义自然语言 Auto-Review 规则（支持设置为 `Block` 直接阻断或 `Require approval` 要求人工审批）、推理前/推理后合规拦截钩子（Inference Hooks Beta）以及带 `cursor.surface=grok_bot` 属性过滤的 OpenTelemetry 遥测导出（平台已通过 ISO/IEC 27001 与 ISO/IEC 42001 认证，详见 [https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)），企业可以确保任何第三方或自建 MCP 连接器都在严格的合规边界内运行。

![Grok Bot 十大类连接器生态分布图与 Bring Your Own MCP 公网接入拓扑](../../images/fig-09-1.png)

*图：Grok Bot 十大类连接器生态分布图与 Bring Your Own MCP 公网接入拓扑*

1Password 共享保险库登录与自定义 MCP 服务的调用。

## 9.3 Computer use、MCP、API 怎么选 · Which Path

让 Bot 接管一个系统，选哪条路？是用 Computer use 在虚拟屏幕上点浏览器，还是走 MCP 和原生插件，还是通过 BDK 跨端桥接，抑或直接写确定性 API 脚本？社区博主 @Michael_Fenech_（https://x.com/Michael_Fenech_/status/2102048957777981938）、官方 101 直播（https://www.youtube.com/watch?v=8xXhE25vJZY）以及中文社区一泽Eze（`@eze_is_1`，[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151)）与 Mr.鼓先生（`@StarkLJM`，[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411)）的实测给出了明确分工。

第一条路是 Computer use（云电脑操作）。它的长处是零开发成本、适应性强。没有接口的老旧系统，只要人在浏览器里能点，Bot 靠看屏幕就能模拟键鼠操作。试错阶段这也是低成本方式（来源：https://x.com/Michael_Fenech_/status/2102048957777981938）。不确定新业务值不值得写代码，让 Bot 先点两次试试，不合适随时停掉。缺点也很明显：它依赖截屏和视觉识别，耗 Token，占周额度（尤其是在 **The X Subscription** 下，Grok Bot、Grok 与 Cursor 三端共享同一个周额度池，高频浏览器操作会迅速消耗额度，详见 `@charlie_pmp` 的分析 [https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131) 与官方计划说明 [https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）；遇到验证码、动态弹窗或前端改版容易卡死。官方常见问答明确写着，遇到登录拦截、双重认证或人机验证，Bot 必须停下来把控制权交还人工，不能强行绕过（[https://cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）。如果目标网站单纯因为封禁了云机房数据中心 IP 而弹出验证码，可以按社区博主 `@XueshiQiao` 的实测方案（[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)），在桌面端开启 `Settings > Computer > Your computer > Route traffic through this computer`，借用本机真实住宅 IP 绕过云机房反爬拦截。

第二条路是 MCP 与原生连接器（Plugins）。业务一旦确定长期跑、每天高频发生，就该尽早从屏幕点击切到 MCP 或插件（来源：https://x.com/Michael_Fenech_/status/2102048957777981938；连接器列表见 [https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。协议对接不用渲染网页，一次工具调用就搞定收发邮件、查单同步。速度压缩到秒级，省 Token，拿到的也是结构化数据。配合 v0.75.2 上调后的 Routine 频率上限——**全账号所有 Bot 合计 300 次/小时，单条 Routine 最高 200 次/小时**（定时最小间隔仍为 5 分钟，详见 [https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）——基于连接器和 `+alias` 邮箱触发的自动化流水线可以支撑极高密度的日常吞吐。但官方 101 直播指出了局限：插件能力完全取决于服务商开放了什么。比如 Figma 插件只能读取设计稿元数据，真要调图层和改样式，还是得退回云电脑屏幕操作（来源：https://www.youtube.com/watch?v=8xXhE25vJZY）。

第三条路是底层 API 脚本直连与 **BDK（`cursor-grokbot-agents`）跨端桥接**。面对批量大、吞吐高、要求稳定成功率的数据任务，或者需要把本地重度编码工具与云端 Grok Bot 串联起来时，纯靠大模型在对话框里手工发指令既慢又费额度。这时有两个高阶工程武器：

其一是 **BDK（Bot Developer Kit，`cursor-grokbot-agents`）跨端双向桥接**。当你在本机终端使用 **Claude Code**、**Codex** 或 **Cursor IDE** 写代码，却需要调用云端 Grok Bot 独有的免费原生 X 全网检索、24 小时云端沙箱渲染或长期记忆库时，可以通过 `cursor-grokbot-agents` 技能将本地 CLI 与云端 Grok Bot 直接打通。Mr.鼓先生（`@StarkLJM`，[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411)）实测演示了由本地 Claude Code 通过 BDK 向云端 Grok Bot 下发“制作一段 20 秒《上下五千年》中国历史线条画动画短片”的任务，云端 Grok Bot 独立完成绘制与合成后，直接向本地返回渲染好的 `0:20` MP4 视频与 `2.7 MB` 源码包；`@kangxiaile`（康熙AI了，[https://x.com/kangxiaile/status/2109752183889744216](https://x.com/kangxiaile/status/2109752183889744216)）与 `@z_lumia`（x白，[https://x.com/z_lumia/status/2113800469571313974](https://x.com/z_lumia/status/2113800469571313974)）也通过这一桥接实现了“本地 Claude Code/Codex 写代码 ↔ 云端 Grok Bot 查 X 舆情与长期记忆”的双向互调。而当外部服务向 Grok Bot Webhook 推送复杂 JSON 触发 HTTP 400 格式校验报错时，社区开发者 `@mikan77_aoi`（橘子，[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）还给出了一个零外部依赖、零守护进程的 Python 标准库脚本，仅用 **4 次标准 API 调用**就将本地任务稳稳交接给云端 Grok Bot。

其二是**“AI 写一次确定性脚本，脚本跑日常零额度轮询”**。这时可以让 Bot 当调度中枢，由独立的后台脚本去跑 API 直连（来源：https://x.com/Michael_Fenech_/status/2102048957777981938；另见 workflows.md 铁柱AGI 调度器实践）。Bot 只管「什么时候启动」和「最终结果怎样」，具体拉数据、洗数据、批量入库交给云电脑或服务器上的 Python 脚本处理。这样能把模型用量压到最低，数据流也更可控。Mr.鼓先生（`@StarkLJM`）在 2026 年 10 月 18 日与 21 日的实测帖中（[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377) 与 [https://x.com/starkljm/status/2112818533797343312](https://x.com/starkljm/status/2112818533797343312)）展示了这一梯度演进的极致数据对比：面对每天定时抓取榜单的需求，绝不让大模型每天开浏览器消耗 Token 读网页，而是用 Cursor CLI 仅耗时 **28.6 秒**一次性编写好确定性的 Python 爬虫脚本；此后每天定时运行该脚本，仅需 **1.99 秒**即可抓完 30 条完整榜单记录，**日常运行消耗 0 模型额度（zero model tokens）**。该脚本还严格落实了防御性编程规范：一旦源页面结构变化导致关键字段缺失，立即触发告警而非静默跳过；当源数据缺少评分时，严格存入 `null` 而不是用 `0` 填充，防止污染后续的均值统计：

```python
# @StarkLJM 确定性采集脚本防御性校验范式（28.6s 生成，每日 1.99s 零 Token 运行）
def parse_ranking_item(raw_item: dict) -> dict:
    required_keys = ("id", "title", "url")
    missing = [k for k in required_keys if not raw_item.get(k)]
    if missing:
        raise ValueError(f"[SchemaAlert] 榜单字段缺失，立即告警人工介入: {missing}")

    # 缺失评分严格记为 None (JSON null)，严禁用 0 污染下游均值计算
    raw_score = raw_item.get("score")
    score = float(raw_score) if raw_score is not None and raw_score != "" else None

    return {
        "id": str(raw_item["id"]),
        "title": raw_item["title"].strip(),
        "url": raw_item["url"],
        "score": score,
    }
```

选型逻辑可以概括为**从验证到固化的四层递进**：探索阶段用 **Computer use** 快速试错；跑通后转成 **MCP 或原生插件**长期跑；跨端协同用 **BDK（`cursor-grokbot-agents`）** 双向派单；高频、批量、规则固定的日常拉取，花 **28.6 秒让 AI 写成确定性 Python/API 脚本**，以 **0 模型额度**稳定跑完全程。

| 选型梯度 | 核心定位与适用场景 | 单次执行耗时 | 周额度 / Token 消耗 | 稳定性与维护边界 |
| :--- | :--- | :--- | :--- | :--- |
| **第 1 层：Computer use（云电脑屏幕操作）** | 新业务探索试错、无 API 的老旧后台、Figma 图层精细修改 | 数十秒至数分钟 | 高（持续截屏与多模态推理，消耗共享周额度池） | 易受前端改版、弹窗与验证码影响；可开启本机住宅 IP 转发缓解反爬 |
| **第 2 层：MCP 与原生连接器（Plugins）** | 日常高频办公协同（`@chat` 私信、邮件、日历、Notion、GitHub、Linear） | 秒级（1–5 秒） | 中低（仅消耗结构化 JSON 工具调用上下文） | 极高；企业可开启 `Apply to MCP servers` 强制执行出站网络白名单 |
| **第 3 层：BDK（`cursor-grokbot-agents`）跨端桥接** | 本地 Claude Code / Codex 与云端 Grok Bot 双向互调（外包 X 检索、视频渲染） | 视子任务而定 | 按实际调用端分摊（本地与云端各司其职） | 打通本地重度代码库与云端 7×24 小时在线沙箱及长期记忆 |
| **第 4 层：AI 编写确定性 API / Python 脚本** | 每日固定榜单抓取、大批量数据清洗入库（如 `@StarkLJM` 范式） | 毫秒至秒级（实测 30 条仅 **1.99 秒**） | **日常运行 0 模型额度**（仅首次生成耗时 **28.6 秒**） | 最稳、最快、最省钱；需内置字段缺失告警与 `null` 防污染校验 |

![Computer use、MCP 与 API 三条实现路径在灵活性、稳定性与成本维度的选型决策漏斗](../../images/fig-09-2.png)

*图：Computer use、MCP 与 API 三条实现路径在灵活性、稳定性与成本维度的选型决策漏斗*

同一任务分别用 Computer use、MCP、API 完成的差异。

---

[← 上一章：§08 审批与安全边界 · Approvals & Safety](../part2-core-concepts/08-approvals-safety.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§10 官方合作集成逐个讲 · Partner Integrations →](../part3-integrations/10-partners.md)

# §03 十分钟安装与开箱 · Install in 10 Minutes

[← 上一章：§02 怎么才能用上 · Getting Access](../part1-getting-started/02-access.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§04 你的第一个任务 · Your First Task →](../part1-getting-started/04-first-task.md)

---

上一章搞定了账号和资格。这一章我们直接动手：把 Grok Bot 装好、登进去、认清界面、改掉几个容易踩坑的默认设置，最后把手机端也连上。整个过程十分钟搞定。

## 3.1 下载与平台 · Download

桌面端下载入口只有一个：**[x.ai/bot](https://x.ai/bot)**（[来源](https://cursor.com/help/grok-bot/get-started)）。打开网页选你的系统安装包。

macOS 分 Apple silicon 和 Intel 两个版本。不知道怎么查？点左上角苹果图标 → 关于本机，看到"芯片"就是 Apple silicon，看到"处理器"就是 Intel（[来源](https://cursor.com/help/grok-bot/get-started)）。下好 dmg 拖进应用程序文件夹，双击启动。系统提示安全确认，直接点打开。

Windows 同样分 x64 和 Arm64。在设置 → 系统 → 关于 → 系统类型里看架构（[来源](https://cursor.com/help/grok-bot/get-started)）。下好 exe 安装包直接运行，装完在开始菜单里打开。

Linux 在下载页的 More downloads 区域，提供 `.deb`（Debian/Ubuntu）、`.rpm`（Fedora/RHEL）和 AppImage 三种格式，各带 x64 和 Arm64 架构。终端敲一行 `uname -m`，输出 `x86_64` 选 x64，输出 `aarch64` 选 Arm64（[来源](https://cursor.com/help/grok-bot/get-started)）。装完直接在应用列表启动。

移动端 iOS 和 Android 都有独立 App。iOS 要求 iOS 18 或更高版本（iPad 要求 iPadOS 18+），Android 要求 Android 9 或更高版本（[cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)），安装包约 26.63 MB（[媒体报道](https://www.thetechoutlook.com/new-release/software-apps/grok-bot-is-now-available-on-android/)）。iOS 去 [App Store](https://apps.apple.com/app/id6794501026) 下，Android 去 [Google Play](https://play.google.com/store/apps/details?id=ai.x.grok.bot) 下。Android 版是在 2026 年 9 月 2 日正式上架的（[@bot 发布帖](https://x.com/bot/status/2095168633559462197)）。注意：国内安卓手机多数没有 Google Play，需要先自行解决 Google 服务问题；iPhone 需要非中国大陆区的 Apple ID 才能在 App Store 搜到（官方未说明上架地区，请以实际为准，详见 [cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）。

安装后不用管更新问题，Grok Bot 会自动静默检测。想手动查，在 Settings → Updates → Check for Updates 点一下就行（[来源](https://cursor.com/help/grok-bot/get-started)）。随着 10 月中下旬 v0.71.2、v0.75.2 与 v0.75.5 连续迭代，建议初次打开后第一时间确认客户端已升至最新桌面版本，手机端 iOS 升至 v1.16 或更高版本（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。

> [!NOTE]
> 📸 **截图位（待补）**：x.ai/bot 下载页，标注三个系统入口

## 3.2 用 Cursor 登录与关联账号 · Sign In & Link

打开 Grok Bot 后是一个极简的欢迎页，中间只有一个 Sign in 按钮。点开会自动跳浏览器完成 Cursor 认证，认证完跳回客户端就登录成功了（[来源](https://cursor.com/help/grok-bot/get-started)）。Grok Bot 本身没有独立账号体系，直接复用 Cursor 账号。企业用户走日常的 SSO 流程即可（[来源](https://cursor.com/help/grok-bot/get-started)）。如果在客户端里没自动登录，进 Settings 点 Sign In with Cursor 也能补登（[来源](https://cursor.com/help/grok-bot/get-started)）。

自 2026 年 10 月 14 日发布的 v0.71.2 版本起，官方进一步简化了客户端的登录与账号关联链路（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。更重要的是，随着 **The X Subscription 三合一统一订阅**正式上线（[@bot 官宣](https://x.com/bot/status/2110063783796572496)），不同订阅体系下的开箱关联体验有了明显分野：

1. **The X Subscription 统一订阅用户（开箱即通，免手动关联）**：如果你订阅的是整合了 Grok、Cursor 与 X Premium 的 **The X Subscription**——其中的 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 档位均原生包含 Grok Bot 权限（Free $0 与 Plus $8/月档位不含 Grok Bot，详见 [cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview) 与 [cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）——那么三大产品在底层天然共用同一个账号与同一个共享周额度池（one weekly usage pool）。你登录客户端后无需再做任何跨端手动关联，直接丝滑开箱。
2. **旧版独立 Cursor / SuperGrok / X Premium+ 订户（保留旧计划或单向合并）**：既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）以及自助式 Teams（$40/人/月）老订户只要不主动切换，仍可保留原有档位与定价（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。如果你是通过旧版独立 Cursor 账号搭配个人 SuperGrok、SuperGrok Plus、SuperGrok Heavy 或 X Premium+ 解锁资格，关联 SuperGrok 稍微多一步：桌面端在 `Settings → Usage & Billing → Manage Plan → Get Access with Grok`（或点 `Link SuperGrok Heavy`，按钮标签会根据你实际的 SuperGrok 等级动态变，也可访问 `cursor.com/bot/onboarding`）完成绑定；手机端在登录后的 access 页点 `Link Grok Account`，关联完再点 `Finished Linking? Refresh My Status` 刷新状态（[来源](https://cursor.com/help/grok-bot/get-started)）。注意多账号额度**绝不叠加（do NOT stack）**，系统会自动取周额度上限更高的那一档生效（[cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）。如果你决定在 `cursor.com/unify` 或 `accounts.x.ai/unify` 将旧计划合并升级到 The X Subscription，请务必记住**该切换是单向不可逆的**，且通过 Apple App Store 或 Google Play 订阅的旧渠道账单必须去手机系统订阅页手动取消，以免双扣（[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。

这里有个坑要注意：如果你的 Cursor 账号处于 **Legacy Privacy Mode**，Grok Bot 会直接拒绝启动。需要先去 [Cursor 隐私设置页](https://cursor.com/dashboard/settings?openPrivacy=true) 把数据模式改掉（[来源](https://cursor.com/help/grok-bot/get-started)）。改完再重新登录就能解决。

遇到登录卡住，官方排查文档给出的步骤很明确：保持客户端开着，确认浏览器显示登录成功后手动切回 App；如果还没反应，重新点一次 Sign in（[来源](https://cursor.com/help/grok-bot/troubleshooting)）。如果报错信息带 Legacy Privacy Mode，就按上面的方法改隐私设置或联系管理员（[来源](https://cursor.com/help/grok-bot/troubleshooting)）。

初次登入后会有一套快速引导：介绍 Bot、云电脑、Routine 的概念，再让你勾选常用工具。这些问卷只是用来推荐第一个 Bot 模版，不会真去连接你的外部账号。云电脑在后台默默就位，最后会停在 Meet a future teammate 界面（[来源](https://cursor.com/help/grok-bot/get-started)）。社区创作者 `@chuyang_ai`（初阳AI）也在其新手入门视频课第 1 期（[https://x.com/chuyang_ai/status/2111357749103911004](https://x.com/chuyang_ai/status/2111357749103911004)）中完整演示了从开通 $30/月 The X Subscription 到客户端登录、创建首个 Bot 的全流程。

企业团队如果要统管，身份和权限完全走 Cursor 原有的 SAML 2.0 SSO，原生支持 Okta、Microsoft Entra、Google Workspace 和 OneLogin。不需要在 IdP 单独搭一个 Grok Bot 应用，直接把现有 Cursor 应用的授权名单放开即可（[来源](https://cursor.com/docs/grok-bot/identity-and-access)）。

> [!NOTE]
> 📸 **截图位（待补）**：授权流程 4 张——欢迎页 Sign in 按钮 → 浏览器认证 → 关联 SuperGrok → Meet a future teammate 页面

## 3.3 界面导览 · UI Tour

主界面看着和日常聊天软件差不多，官方的设计初衷就是"像给队友发消息一样给 Bot 派活"（[来源](https://cursor.com/help/grok-bot/chat-and-collaboration)）。我带你按区域走一遍。

左侧是 Bot 列表。每个 Bot 名字下方会挂状态：Needs attention 意味着正等你回答、审批或者人工交接；Unread activity 表示任务跑完了有新结果；Working 或 Typing 说明它正在干活（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。点哪个 Bot 就进哪个对话。日常嫌挤，随时按 `Cmd/Ctrl+B` 把侧栏收起来（[来源](https://cursor.com/help/grok-bot/chat-and-collaboration)）。

中间是主对话区。打字、粘贴长文本或链接、丢图片附件、按 `Cmd/Ctrl+D` 语音输入，或者直接开实时语音对话都行。对话流里除了文字回复，还会实时展示 Bot 的工具调用、云电脑桌面操作、生成的文件、提问互动、审批单和语音备忘录（[来源](https://cursor.com/help/grok-bot/chat-and-collaboration)）。自 v0.71.2 起，官方还进一步优化了对话流内的文件预览与下载处理体验，并支持直接展示 Grok Imagine 生成的视频卡片与 Remotion 代码动效预览（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。

输入框有两个快捷符号：敲 `@` 呼叫其他 Bot、群聊、Routine 或连接器；文档写敲 `/` 可以引用保存好的 Skill（技能，§07 详解）（[来源](https://cursor.com/help/grok-bot/chat-and-collaboration)）。但注意时效：10 月 7 日的 v0.68.1 changelog 写着 "Typing / in the composer no longer opens a menu of skills and actions"（[x.ai/changelog/bot](https://x.ai/changelog/bot)）——新版本里 `/` 不再弹菜单，直接用文字说"用 XX skill"即可，以你手上的版本为准。

想搞多 Agent 协同可以建群聊。在侧栏点 New，选 2 到 6 个 Bot 就能拉进一个群（[来源](https://cursor.com/help/grok-bot/chat-and-collaboration)）。群里发话后，Bot 们会自动协调谁来接招；你也可以用 `@` 点名指派。群聊也有边界：审批卡片、私密密钥请求、以及草拟的邮件和 Slack 消息都不会发到群里（[来源](https://cursor.com/help/grok-bot/chat-and-collaboration)）。

侧栏的 Marketplace 负责插件（plugin，即让 Bot 能连上 Gmail、Notion 等外部应用的扩展）的发现与安装，装好的插件全在 Your plugins 统一管理（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。注意改名：9 月底起侧栏按钮改叫 **Connect apps**，10 月 2 日 Marketplace 整体改名为 Connect Apps（[x.ai/changelog/bot](https://x.ai/changelog/bot)，详见官方指南 [cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。本书沿用"Marketplace"指代同一个入口。

在 2026 年 10 月下旬的 v0.75.2 与 v0.75.5 重大更新中，主界面与设置体系新增了两个你每天都会高频用到的重磅入口：

- **入口一：右侧信息栏下的 `Bot info pane → Library`（Pages / Canvas 实时看板与交互应用库）**
  在任意 Bot 对话窗口中打开右侧的 Bot 信息栏（`Bot info pane`），你会看到全新的 **`Library`（资料库）** 面板（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。这里是存放和随时打开该 Bot 创建的所有 **Pages（底层由 Canvas 驱动的实时交互网页）** 的大本营（[@bot 官宣](https://x.com/bot/status/2112991843235610885)，6,544 赞 / 2,008 书签）。当你对 Bot 下令 *"Make me a page with this week's metrics"* 时，它不仅会在聊天流里生成一张 **Page card（页面卡片）**，还会把这份包含表格、图表、时间线与交互组件的动态页面永久沉淀进 `Bot info pane → Library`。打开任意 Page 点右上角 **Share**，即可在 **Only you（仅自己可见）**、**Your team（团队可见）** 与 **Anyone with the link（公开链接）** 三级权限间自由切换。比如开发者 `@melvindvivas`（Melvin Vivas）就让自己的幕僚长（Chief of Staff）Bot 在 Library 里维护了一张 `Grok Bot Activity Dashboard` 实时看板，集中展示所有专职 Bot 的时间线、进行中任务、已完成事项与待人工审批项（[https://x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882)，1,087 赞 / 1,687 书签）。
- **入口二：设置菜单中的 `Settings → Vault`（内置加密保险箱）**
  在 v0.75.5（2026-10-23）中，设置面板新增了独立的一级入口 **`Settings → Vault`**（[cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)，[@bot 官宣](https://x.com/bot/status/2113754107861532677)，9,398 赞 / 2,756 书签）。它是一个只写（write-only）的内置加密保险箱，专门用来安全托管你的三类敏感数据：**Logins（网站账号、密码与 2FA/TOTP 动态验证码）**、**Cards（信用卡/借记卡）** 以及 **Contact info（常用收货地址、电话与邮箱）**。每个条目还可以写一段明文 **Hint（提示标签，如 *"Corporate Amex"*）** 供 Bot 识别用途，而密码与卡号对 Bot 上下文完全不可见（[cursor.com/docs/grok-bot/settings](https://cursor.com/docs/grok-bot/settings)）。

遇到需要人工接管的环节，从对话流里打开**电脑视图**，就能看到云电脑桌面。你替它输完密码、过完二次验证或验证码，再把控制权还回去继续跑（[来源](https://cursor.com/help/grok-bot/get-started)）。

全局搜索按 `Cmd/Ctrl+K` 调出，搜历史记录、找文件、翻 Routine、跨 Bot 跳转都靠它；`Cmd/Ctrl+Shift+F` 则专用于搜索 Bot（[来源](https://cursor.com/help/grok-bot/chat-and-collaboration)）。

常用的快捷键整理在下面，桌面端全平台通用（macOS 用 Cmd，Windows 和 Linux 换 Ctrl）：

| 操作 | 快捷键 |
|---|---|
| 搜索面板 | `Cmd/Ctrl+K` |
| 搜索 Bot | `Cmd/Ctrl+Shift+F` |
| 新建 Bot / 新对话 | `Cmd/Ctrl+N` |
| 在对话内搜索 | `Cmd/Ctrl+F` |
| 收起侧栏 | `Cmd/Ctrl+B` |
| 聚焦输入框 | `Cmd/Ctrl+I` 或 `Cmd/Ctrl+L` |
| 切换到侧栏第 1–9 个 Bot | `Cmd/Ctrl+1` 至 `Cmd/Ctrl+9` |
| 上/下切换 Bot | `Alt+↑` / `Alt+↓` |
| 语音输入 | `Cmd/Ctrl+D` |
| 连接 App | `Cmd/Ctrl+Shift+M` 或 `Cmd/Ctrl+Shift+W` |
| Bot 设置 | `Cmd/Ctrl+Shift+,` |
| 打开设置 | `Cmd/Ctrl+,` |
| 发送 | `Enter`（输入框内）或 `Cmd/Ctrl+Enter`（任意位置） |
| 换行 | `Shift+Enter` |

（[来源](https://cursor.com/help/grok-bot/chat-and-collaboration)）

> [!NOTE]
> 📸 **截图位（待补）**：标注版主界面——侧栏、对话区、输入框、`/` 和 `@` 弹出菜单、电脑视图入口

![快捷键速查卡（适合打印贴桌面）](../../images/fig-03-1.png)

*图：快捷键速查卡（适合打印贴桌面）*

## 3.4 设置里先改这五项 · First 5 Settings

刚装好先别忙着派活，按 `Cmd/Ctrl+,` 打开 Settings（完整设置项参考见官方技术文档 [cursor.com/docs/grok-bot/settings](https://cursor.com/docs/grok-bot/settings)），先把这五个默认设置以及最新的凭据保险箱配置过一遍。这些地方不留心，后面最容易出乱子。

第一项是时区。路径在 Settings → General → Bot → Timezone（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。Routine 定时任务全照着这个时区跑，设错了任务时间全得颠倒。国内环境选 Asia/Shanghai。顺带一提，自 v0.75.2 起，官方将 Routine 的小时级运行频率上限大幅上调至**全账号所有 Bot 合计 300 次/小时，单条 Routine 最高 200 次/小时**（定时触发最小间隔仍为 5 分钟，详见 [cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)），校准好时区能让高频自动化准点运行。

第二项是通知。进 Bot 对话详情（View conversation details → Bot settings），打开 Notifications 开关。Bot 跑完交差或者卡住等人时，系统才能弹出通知（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。有两个细节要注意：Grok Bot 在前台活动时通知会自动静音，只在侧栏和 Dock 图标上挂红点；另外群聊目前没有单聊那种按 Bot 单独控制的通知开关（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。

第三项是 Auto-review 审批规则。位置在 Settings → General → Auto-review（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。规则分你自己配的和管理员锁死的（标记为 Required by your admin）。当 Ask first 和 Allow automatically 产生冲突，Ask first 绝对优先（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。在 v0.75.2 中，官方精简了冗余审批弹窗——对于你在当前对话轮次中已经明确下达指令要求执行的操作，系统不再重复弹出二次确认卡片（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。但新手阶段仍别急着大面积开自动放行，等摸熟了 Bot 的动作习惯再逐步放权。

第四项是按需计费与超额预付控制，**新手第一周务必把超额开关管住**。在 `Settings → Usage & Billing` 页面能看周额度进度条（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）：
- 如果你是**旧版独立 Cursor 计划**订户，额度跑光后如果 On-demand 开着，Bot 会继续干活并按量扣钱，不设上限极易超支。注意 Cursor Teams 计划**默认开启** On-demand（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。铁柱AGI 在实操中发现，Bot 遇到工具报错很容易陷入死循环重试，十几分钟就能打穿整周额度；没关 On-demand 的话扣费更狠（[来源](https://x.com/cgnot996/status/2108504325609984233)）。建议先关掉或设一个极低的月度限额，心里有数了再开。
- 如果你是全新的 **The X Subscription（Premium $30 / Super $100 / Ultra $200）** 订户，Grok Bot 与 Grok App、Cursor IDE **三端共享同一个周额度池**，且超额消费不再走后付费账单，而是从 **Prepaid Credits（预付额度）** 中扣除（[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。只要你不在 `grok.com/dashboard/billing` 开启 `Auto Top-up（自动充值）` 或主动充值 Prepaid Credits，周额度用完就会自然停下，天然防天价账单；但正如社区用户 `@charlie_pmp` 所提醒的（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)），三端共用额度池加上未精简的高频 Routine 会加速消耗周额度，务必养成定期检查 `Usage & Billing` 的习惯。

第五项是本地电脑执行权限。Settings → General → Bot → Execution on Local Computer 控制的是 Bot 能不能操纵你眼前这台物理机。默认是每条命令都必须手动审批，并且设置只对当前这台电脑生效（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。除非任务必须依赖本地机器，否则官方排查指南建议保持关闭（[来源](https://cursor.com/help/grok-bot/troubleshooting)）。另外，如果你遇到目标网站拦截云机房 IP 或频繁弹验证码，可以像社区用户 `@XueshiQiao` 实测的那样（[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)），在 `Settings → Computer → Your computer` 中勾选 `Route traffic through this computer`，借用本机住宅 IP 转发云端浏览器流量（v0.75.5 已专门修复了本地电脑流量转发的稳定性，见 [x.ai/changelog/bot](https://x.ai/changelog/bot)）。

除了上面五项基础开关，开箱时还有一项能大幅降低日后登录与结账摩擦的黄金配置——**配置 `Settings → Vault` 与 `Settings → Connect apps → 1Password`**：

1. **绑定 1Password 免共享库代理登录（`Settings → Connect apps → 1Password`）**：
   只要你电脑或手机上装有 **1Password v8.12.42 或更高版本**，去 `Settings → Connect apps → 1Password → Connect` 一键绑定即可（[cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)，[@bot 官宣](https://x.com/bot/status/2113301060811161874)）。新版采用 **Brokered Sign-in（逐次代理授权）** 机制（[@1Password 官宣](https://x.com/1Password/status/2113276767582498943)，10,507 赞 / 7,122 书签），**不再需要像旧版那样专门新建共享密码库（shared vault）或配置 Service Account 令牌**。当 Bot 遇到登录墙时，你只需在本地 1Password App 上按一下指纹/面容批准，1Password 就会直接把 Personal / Private 库里的凭据安全注入云端浏览器，Bot 全程看不到明文密码。此前用过旧版共享库的用户，断开（Disconnect）并重连（Reconnect）即可升级。
2. **初始化内置保险箱与银行卡风控抉择（`Settings → Vault`）**：
   进 `Settings → Vault`，你可以点击 `Import` 直接导入来自 1Password、Chrome、Safari、Firefox、Bitwarden 或 LastPass 的 CSV 密码文件（上限 **5 MB**），或者手动添加常用收货地址（`Add contact`）与网站账号（`Add login`）（[cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）。根据官方工作流文档（[cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)），Bot 登录网站时的调用优先级依次为：**云电脑已保存的浏览器会话 → Vault → 1Password → 聊天内 Secure Form → 人工接管屏幕（Take over screen）**；结账支付时的调用优先级依次为：**Vault → 聊天内 Secure Form → Link / X Money → 人工接管屏幕**。
   **关键安全与风控提醒**：虽然 Elon Musk（`@elonmusk`）公开承诺 *"If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole"*（如果代购出错或泄露卡号，SpaceX 全额赔付，见 [https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445)），但正如官方文档 [cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets) 所载、且由社区博主 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）与 `@JianWeiSignal`（见微｜Signal，[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)）重点警示的：**一旦你把银行卡保存在 `Settings → Vault` 中，Bot 在结账填充该卡时不会触发单独的逐笔 Vault 确认弹窗（filled at checkout without a separate per-charge Vault prompt）**，仅受通用购买审批规则约束！如果你希望每一笔消费都必须亲手输入并逐单把关，**请只在 Vault 里存常用收货地址，切勿将主力银行卡常驻保存在 Vault 中**（改用每次结账弹出聊天内 Secure Form 时单次输入且不勾选保存）；或者参考 `@martinpaulweiss` 的“一密一宅（One home per secret）”拆分法（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）：日常登录与 2FA 统一放 1Password，Vault 只放收货地址与专门设好额度的代购卡。

> [!NOTE]
> 📸 **截图位（待补）**：Settings 各页——Timezone 下拉框、Notifications 开关、Auto-review 规则列表、Usage & Billing 页面、Execution on Local Computer 开关

## 3.5 手机端 · Mobile

手机端不是桌面端的缩水壳子，底层连的是同一套 Bot、对话、Routine、连接器和云电脑（[来源](https://cursor.com/help/grok-bot/mobile)）。电脑上配好的 Bot 手机随时能用。活都在云端跑，划掉 App 不会打断后台任务。随着 2026 年 10 月中下旬 v0.71.2、v0.75.2、v0.75.5 与 iOS v1.16+ 的密集更新，手机端已经彻底打破了早期“只能打字收发消息、无法读取手机本地日历/通讯录、也没有侧边物理按键快捷指令”的局限，进化成随身全功能指挥台（[cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）。

平时交互该有的都有：打字、语音听写（Start dictation）、实时语音交流（Start voice chat）、听取 Bot 留下的语音备忘录、发照片或文件、群聊里 `@` 唤醒、Thread 楼中楼回复以及给消息点表情，都能直接操作（[来源](https://cursor.com/help/grok-bot/mobile)）。

手机端最实用的场景就是随身派活与审批。路上有了想法，掏出手机直接交代。用 Start dictation 会转成文字供确认，用 Start voice chat 则是跟 Bot 实时对话（[来源](https://cursor.com/help/grok-bot/mobile)）。在实时语音通话（Live Voice Chat）中，你可以随时静音/取消静音（Mute/Unmute）、展开实时字幕（Show transcript）、或在语音设置（Show settings）中切换音色（Voice）、语速（Speed）与带自动识别（Auto-detect）的语种；挂断瞬间，聊天流会自动生成一张包含通话时长与完整逐字稿的 **Voice chat card（语音通话卡片）**，Bot 随即自动跟进执行并交付结果文件（[cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)）。Bot 准备发邮件前，对话里会弹出一张 New Email 卡片，点 Send Email 放行或者点 Discard 丢弃，完全不用折腾回电脑前（[来源](https://cursor.com/help/grok-bot/mobile)）。需要人肉干预时，手机上同样能打开云电脑画面看它在干嘛，替它输完密码或过完验证码，交还控制权就能继续（[来源](https://cursor.com/help/grok-bot/mobile)）。

建 Bot 和拉群在主屏点 `+` 就能搞定（New Bot 或 New Group Chat）（[来源](https://cursor.com/help/grok-bot/mobile)）。全局搜索能跨 Messages、Bots、Group Chats、Files 和 Routines 查东西（[来源](https://cursor.com/help/grok-bot/mobile)）。iPhone 还支持系统共享菜单，任何 App 里的图文或链接都能直接甩给 Grok Bot 对话；Android 目前分享菜单只支持纯文本（[来源](https://cursor.com/help/grok-bot/mobile)）。

在最新版本的手机端开箱中，强烈建议你花两分钟把以下**四大移动端重磅新特性**一并配齐：

### 1. iPhone Action Button 侧边按钮一键语音通话（iOS v1.16+）
2026 年 10 月 19 日，官方正式推出 iPhone **Action Button（操作按钮）** 一键语音功能（[@bot 官宣](https://x.com/bot/status/2112246033178968161)，7,264 赞 / 2,213 书签；详见官方指南 [cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat) 与 [cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）。在配备 Action Button 的机型（iPhone 15 Pro 及后续机型）上，将 Grok Bot iOS 客户端更新至 **v1.16 或更高版本**并至少打开过一次 App 后，无需解锁翻找图标，长按手机侧键即可瞬间接通 Bot 实时语音（参见 `@SawyerMerritt` 的第一时间实机上手录屏演示：[https://x.com/SawyerMerritt/status/2112252980015579431](https://x.com/SawyerMerritt/status/2112252980015579431)，1,627 赞）。你可以根据习惯任选以下三种配置路径：

- **路径 1：直连默认主 Bot（Primary Bot）**
  打开 iPhone 系统 `Settings（设置） → Action Button（操作按钮） → Shortcut（快捷指令） → Choose a Shortcut（选择快捷指令） → Grok Bot → Start Voice Chat`。设置完成后，长按侧键即刻呼叫你的默认主 Bot（[cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)）。
- **路径 2：通过 iOS Shortcuts 指定专职 Bot 或每次弹窗选择（`Ask Each Time`）**
  如果你手头有多名专职 Bot（例如幕僚长、投研员、生活助理），打开 iOS 自带的 **Shortcuts（快捷指令）** App，新建一条快捷指令并添加 Grok Bot 提供的 **`Start Voice Chat with Bot`** 动作。在目标 Bot 参数里，你既可以固定绑定某一位专职 Bot（比如专管点单的助理），也可以设为 **`Ask Each Time`（每次询问）**——长按侧键时屏幕顶部会优雅弹出 Bot 列表供你点选。你还可以直接用 `"Hey Siri"` 喊出该快捷指令名称来免手触发（[cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)）。
- **路径 3：URL Scheme 定向跳转直达任意 Bot**
  如果你习惯在自定义复杂快捷指令流或第三方启动器中串联调用，可以使用 `Open URLs` 动作直接打开深链 URL Scheme：
  ```text
  grokbot://app/v1/agent?id=YOUR_BOT_ID
  ```
  将其中的 `YOUR_BOT_ID` 替换为对应 Bot 的实际 ID 即可秒开指定会话窗。

### 2. 开启 iOS 原生日历、提醒事项与通讯录直读权限（v0.75.2+）
自 2026 年 10 月 22 日的 v0.75.2 版本起，Grok Bot iPhone 客户端正式打通了 iOS 系统原生的 **Calendar（日历）**、**Reminders（提醒事项）** 与 **Contacts（通讯录）**（[x.ai/changelog/bot](https://x.ai/changelog/bot)，[cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）。在手机端初次让 Bot 查日程、建提醒或找联系人时，在弹出的 iOS 系统权限框中点选允许（或前往 `iPhone 设置 → 隐私与安全性` 开启 Grok Bot 的日历、提醒事项和通讯录权限）。
开启之后，你的云端 Bot 就能直接读取并操作你 iPhone 本地的日程表与待办清单。社区玩家 `@TyeInBloom`（Tye Gordon）晒出了将 **iOS 原生三件套（Calendar / Reminders / Contacts） + 1Password 逐次授权 + Action Button + 绑定专职 Bot 的 Hey Siri 快捷指令**组合在一起的“全家桶”配置（[https://x.com/TyeInBloom/status/2113767679588770271](https://x.com/TyeInBloom/status/2113767679588770271)），彻底接管了日常行程安排；`@JCOMBuilds` 每天早晨按一下 Action Button 呼叫助理 Bot `"Eve"`，自动调取 1Password 凭据为妻子点好星巴克（[https://x.com/JCOMBuilds/status/2112997408510452123](https://x.com/JCOMBuilds/status/2112997408510452123)）；而中文社区创作者 `@D__cup`（大艺术家二福）则分享了 **韶音（Shokz）不入耳骨传导耳机 + iPhone Action Button** 的全天候免提方案（[https://x.com/D__cup/status/2114211130365358350](https://x.com/D__cup/status/2114211130365358350)），在通勤、走路和做家务时完全解放双手双目，随时用语音调度云端 AI 团队。

### 3. 手机摄像头扫卡极速录入 Vault（v0.75.5+）
如果你决定将某张专用消费卡存入内置加密保险箱，不用在键盘上挨个敲 16 位卡号。在手机端进入 **`Settings → Vault → Add card → Scan`**，直接用手机摄像头对准银行卡正面一扫，就能自动识别卡号并加密封存进只写 Vault 中（[cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)，[x.ai/changelog/bot](https://x.ai/changelog/bot)）。

### 4. 移动端推送通知 Deep-link 直达对应 Bot 聊天窗（v0.71.2+）
初次启动手机 App 别忘了给通知权限。系统权限和应用内 Bot 通知都打开，后台动态才能准时推送到位（[来源](https://cursor.com/help/grok-bot/settings-and-notifications)）。从 v0.71.2 开始，iOS 与 Android 的推送通知已全面支持 **Deep-link（深度链接跳转）**（[x.ai/changelog/bot](https://x.ai/changelog/bot)，[cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）——哪怕你手头同时养了十几个专职 Bot，锁屏状态下点击某条审批或任务完成通知，App 都会精准直达触发该通知的那一个具体 Bot 聊天窗口，不再停留在主列表让你挨个翻找。

但最后仍要分清桌面与移动端的职责边界：**复杂的脚手架配置操作建议回桌面端完成**。例如深度编辑复杂 Routine 的计划与指令、测试 Routine、以及 Teach by Demo（录屏教 Bot 学操作），目前手机端一概不支持（[来源](https://cursor.com/help/grok-bot/mobile)）。桌面端用来搭基建和定规矩，手机端配合 Action Button、原生三件套与 Deep-link 通知用来随身语音派单、实时放哨与一键拍板审批，这才是双端协同的最佳姿势。

> [!NOTE]
> 📸 **截图位（待补）**：iOS 2 张（主屏幕 Bot 列表 + 语音输入界面）、Android 2 张（对话页 + 审批卡片）

---

[← 上一章：§02 怎么才能用上 · Getting Access](../part1-getting-started/02-access.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§04 你的第一个任务 · Your First Task →](../part1-getting-started/04-first-task.md)

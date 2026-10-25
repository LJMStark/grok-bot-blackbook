# §04 你的第一个任务 · Your First Task

[← 上一章：§03 十分钟安装与开箱 · Install in 10 Minutes](../part1-getting-started/03-install.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§05 Bot：给每个同事一份岗位说明书 · Bots & Profiles →](../part2-core-concepts/05-bots.md)

---

装好客户端，绑定完账号，看着左边空荡荡的列表，很多人会愣住：第一句话该发什么？

别发“你好，你能帮我做什么”。Grok Bot 不是陪聊的对话框，它背后是跑在云端的电脑和数字员工。你敲字不是在聊天，而是在派工单。

这一章我不扯宏大团队编制，带你把第一件真活交到它手上。

> 适合谁：所有刚装好客户端的人。前提条件：已完成 §02–§03（有可用额度、已登录，推荐首选 $30/月的 The X Subscription Premium 三合一统一订阅，或保留既有的独立 Cursor Pro $20 / Pro+ $60 / Ultra $200 / Teams $40 老订户计划，注意通过 `cursor.com/unify` 单向升级切换不可逆）。任务一需要 Gmail 等境外邮箱；只有 QQ/163 邮箱的读者可以先做任务二、三，或直接用 4.1 的"上传文档"范例——它不需要任何连接器。此外，如果希望先通过视频快速建立全貌，可以参考 `@chuyang_ai`（初阳AI）制作的 Grok Bot 新手视频课程第 1 期（https://x.com/chuyang_ai/status/2111357749103911004），里面系统拆解了它与 Claude Code 的定位区别、为什么首推 $30/月的 The X Subscription 档位、客户端安装与创建第一个 Bot 的全流程；以及 `@itgoyo`（小田切让）浓缩的 90 秒 5 条核心上手铁律视频（https://x.com/itgoyo/status/2111332049193996421）。

## 4.1 任务五要素 · Outcome / Sources / Constraints / Deliverable / Review

给 Bot 派活最容易踩的坑，就是随手甩一句“帮我看看今天的邮件”。不给边界，它可能会在云电脑里把收件箱翻个底朝天，耗光额度，还翻出不该看的私人邮件。

我翻了官方文档，官方团队一开始就强调派活必须遵循明确结构（https://cursor.com/help/grok-bot/get-started）。Kin 在《Grok Bot 橙皮书》里提过“验收前置”（https://github.com/KinGao294/grok-bot-orange-book），但他主要讲了想好结果，没细说数据源边界和硬性约束。官方给出的标准范式包含五个核心要素，缺了一个，Bot 就容易跑偏或越界。

这五个要素是最终结果（Outcome）、信息来源（Sources）、约束条件（Constraints）、交付物形式（Deliverable）和人工审阅点（Review point）。最终结果要明确，说清楚做到什么程度算结束，比如“总结本周新增用户反馈”，别说模糊的“关注一下”。信息来源要限定范围，指明具体应用、网页、本地附件或特定对话，免得它在云电脑里到处乱翻。约束条件是安全底线，写清楚严禁做什么，比如“严禁点击删除”、“严禁修改原文档”、“外发前必须请示”。交付物形式要定死格式，除了 5 条要点的纯文本、带表头的表格、指定目录下的 Markdown 文档或语音通话结束后的 **Voice chat card（语音通话卡片）** 之外，自 v0.75.2（https://x.ai/changelog/bot）起，更推荐将 **Page（Canvas 实时交互页面/看板）** 作为首选的高可读性交付形态。人工审阅点则是刹车片，规定好在哪个节点停下等你确认，免得它一路狂奔把邮件发了出去或把单买了。

![任务五要素结构卡（Outcome / Sources / Constraints / Deliverable / Review）](../../images/fig-04-1.png)

*图：任务五要素结构卡（Outcome / Sources / Constraints / Deliverable / Review）*

### 交付物（Deliverable）重大进化：把 Page（Canvas 实时交互页面）作为首选看板形态

在旧版工作流中，Bot 的交付物往往局限于一次性聊天气泡里的 Markdown 文本或静态文件；一旦数据更新，你就得在长长的聊天记录里翻找最新版本。而在 2026 年 10 月 21 日官方正式发布的 **Pages（底层由 `WriteCanvas` / `EditCanvas` / `ReadCanvas` / `ListCanvases` 工具驱动的交互式画布）** 功能中（官方发布帖 `@bot` 获得 6,544 赞、567 转发、2,008 书签：https://x.com/bot/status/2112991843235610885；同步收录于官方更新日志 v0.75.2：https://x.ai/changelog/bot），交付物彻底升级为包含表格、图表、时间线与交互组件的实时网页应用。

你只需在“交付物形式（Deliverable）”中自然语言下令，例如：

```text
Make me a page with this week's metrics
```

Bot 就会直接生成一张 **Page card（页面卡片）**，并且沉淀在对应 Bot 右侧信息栏的 **Library（资料库）** 中（路径：`Bot info pane → Library`）。每当后续数据发生变化，Bot 都会在原页面上持续热更新，无需反复重发新文件。打开任意 Page 点击右上角 **Share**，还可以按需配置三级分享权限：**Only you**（仅自己可见）、**Your team**（团队成员可见，团队管理员可在 `Dashboard → Grok Bot → Bot capabilities` 中管控）或 **Anyone with the link**（任何持有链接的人可访问）。社区开发者 `@melvindvivas` 甚至让幕僚长 Bot 用 Page 搭建了汇总所有子 Bot 进度的 `Activity Dashboard` 实时作战看板（1,087 赞、1,687 书签：https://x.com/melvindvivas/status/2113676935956160882），将交付物的可视化程度推到了全新高度。

### 对话层的正确心智：先对齐目标再调工具或派发 Cloud Agent，切勿当成裸问答机

为什么有些新手觉得给 Grok Bot 派第一个任务时体验不如预期？2026 年 10 月 18 日，中文社区头部博主 `@Khazix0918`（数字生命卡兹克，285 赞、54 书签：https://x.com/Khazix0918/status/2111709708226797737）与开发者 `@object_nullll`（https://x.com/object_nullll/status/2111717423837778173）围绕这一问题展开了一场极具启发性的架构讨论。

`@Khazix0918` 指出了很多新手把默认聊天框当成无上下文“裸问答苦力”直接提问时的反面痛点：如果不配置专门的 Skill、也不要求它去检索或委派任务，直接裸聊复杂问题，容易遇到“路由的轻量级对话模型查都不查直接张嘴就来，来回掰扯浪费的时间远超节省的时间”。对此，`@object_nullll` 一针见血地剖析了 Grok Bot 对话层（Conversational Layer）的真实设计初衷：**主对话框本质上是你的“项目经理与调度前台”，它的核心职责是收集上下文、与你对齐任务五要素与验收标准（Acceptance Criteria）、编写结构化 Prompt，随后调用云电脑工具、沙箱脚本，或将重度编码与分析任务派发给 Cursor Cloud Agents（`CloudAgent`）及 CLI Workers 去深度执行**。

正如开发者 `@realbenzh`（Ben Zhang，https://x.com/realbenzh/status/2111295936635015631）在实战中所验证的那样：先把飞书、Linear、邮箱和文档上下文喂给 Bot，在聊天窗口里先和它对齐交付目标与验收标准，再让它驱动底层 CLI 或工具去干重活，才能发挥出它真正的实力。切勿把 Grok Bot 的聊天框当成没有上下文的裸问答机去硬跑 zero-shot 重度任务。更多官方推荐的派活技巧与实操范式，也可以随时查阅官方实操指南（https://cursor.com/help/grok-bot/how-to）。

官方在快速上手文档里给过一个范例（https://cursor.com/help/grok-bot/get-started）。如果手里有一份长文档，想在五分钟内拿到结果，不需要配复杂的连接器，直接把文档当附件上传，发这段指令：

```text
将此文档总结为 5 个核心要点。把文中提及的所有具体日期、最终决策和未决问题单独列在一个独立章节中。每一项内容都必须标注对应的页码或章节出处。严禁修改原始文件。
```

在这段指令里，要点数量是结果，附件是数据源，严禁修改原文件是约束，分章节带出处是交付物。这就是标准的**任务五要素**落地写法。

## 4.2 先连常用 App · Connect Your Apps First

打开界面的第一反应别急着狂敲提示词。新员工连公司邮箱、日历都进不去，再聪明也只能干瞪眼。

Grok Bot 核心团队成员 Lauren（@poteto）在 X 上给过一条新手建议（https://x.com/poteto/status/2107830403549831186），推文拿了 1600 多个赞（10/13 复核为 1,623）。她建议上手第一步别急着建 Bot，先连接日常用的核心工具，包括日历、Slack、工单系统、CRM 和网盘，让它拿到干活的上下文。同样，在 `@itgoyo` 的 90 秒 5 条新手铁律视频（https://x.com/itgoyo/status/2111332049193996421）中，也把“优先绑定 Gmail / GitHub / X 等核心连接器”列为开箱必做动作。

> [!NOTE]
> 📸 **截图位（待补）**：侧边栏 Connect apps 授权与接管云电脑登录界面

在桌面客户端里，入口在左侧栏的 Connect apps，快捷键是 Cmd/Ctrl+Shift+M 或 Cmd/Ctrl+Shift+W（https://cursor.com/help/grok-bot/chat-and-collaboration）。关于所有受支持的第三方连接器与权限边界，官方提供了完整的连接指南（https://cursor.com/help/grok-bot/connect-apps）。

官方的应用集成没要求第三方都做 API 插件，而是结合了原生连接器与云电脑浏览器操作（https://cursor.com/help/grok-bot/get-started）。遇到要网页登录的系统，具体接管步骤是：

1. Bot 执行任务遇到登录拦截，发出接管请求。你在当前对话里点 Agent Computer 进入云电脑实时画面。
2. 点 Takeover 按钮，控制权切到本地鼠标键盘。
3. 你亲自在云电脑浏览器里输密码、扫码、过二次验证（2FA）或验证码。
4. 点归还控制权，Bot 继续执行。

这种模式的好处是密码由你亲手输入，不必把明文写进对话（但登录后的会话会留在共享云电脑上，见下文和 §08）。而且官方文档明确提到，云电脑浏览器的登录会话（Session）会长驻保存，账号下所有 Bot 共享（https://cursor.com/help/grok-bot/get-started）。你在云电脑里登过一次 Gmail 或后台，后面建的助手都能直接复用，不用反复登。

### 2026-10 重磅升级：1Password 新版一键代理连接、内置 Vault 与 iOS 原生三件套

在 v0.75.2 与 v0.75.5 版本更新中（https://x.ai/changelog/bot），官方对连接应用与网站登录体验做了三次极大幅度的减负，彻底改变了以往每次都要人工接管屏幕输密码的繁琐流程：

1. **1Password 新版一键连接（Brokered Sign-in 逐次代理审批，免共享密码库）**：
   2026 年 10 月 22 日，Grok Bot 与 1Password 官方联合上线了基于 `"1Password for Agents"` 架构的全新原生连接方式（`@bot` 官宣帖 3,663 赞：https://x.com/bot/status/2113301060811161874；`@1Password` 官宣帖 10,507 赞、7,122 书签：https://x.com/1Password/status/2113276767582498943）。只要你的本地设备安装并解锁了 **1Password App 8.12.42 或更高版本**，进入 `Settings → Connect apps → 1Password → Connect` 即可一键完成绑定。
   与早期旧版需要繁琐新建名为 `Grok Bot` 的共享 Vault 并手动复制 Service Account Token 不同，新版采用 **Brokered Approval（逐次代理审批）** 机制（详见官方应用连接文档 https://cursor.com/help/grok-bot/connect-apps 与工作流文档 https://cursor.com/docs/grok-bot/work）：当 Bot 在云端浏览器遇到登录页时，会弹出 **Review in 1Password** 提示；你在手机或电脑的 1Password App 上按一下指纹/面容（或 Passkey）批准，1Password 就会把你 **Personal / Private（个人/私有）** 密码库中的对应凭据直接加密注入浏览器会话，**Bot 全程绝不会在聊天流或上下文中看到明文密码**（注：若此前使用旧版共享库方案，只需在 `Settings → Connect apps` 中 Disconnect 再 Reconnect 即可切到新版）。例如中文社区博主 `@oxpsats`（偶像派作手，https://x.com/oxpsats/status/2114207006064365670）就利用 1Password 授权彭博社（Bloomberg）会员凭据，让 Bot 自动登录突破付费墙抓取研报。
2. **内置 Grok Bot Vault 加密保险箱（作为补充）**：
   如果你不使用 1Password，官方也在 v0.75.5 上线了内置的 `Settings → Vault`（`@bot` 官宣帖 9,398 赞：https://x.com/bot/status/2113754107861532677；官方说明文档：https://cursor.com/help/grok-bot/secrets），支持只写（Write-only）加密保存网站登录信息（含 2FA/TOTP）、收货地址与银行卡（支持手机摄像头扫卡与最大 5 MB 的 CSV 批量导入）。不过请务必记住官方安全文档（https://cursor.com/help/grok-bot/secrets）与社区博主 `@kial`（https://x.com/kial/status/2114201768414646280）、`@JianWeiSignal`（见微｜Signal，https://x.com/JianWeiSignal/status/2114195530611855488）提醒的黄金红线：**保存在 Vault 中的银行卡在结账填充时不会触发单独的逐笔 Vault 确认弹窗**，新手第一天千万不要往 Vault 里存主力银行卡！我们可以遵循 `@martinpaulweiss` 提出的“一密一宅（One home per secret）”原则（https://x.com/martinpaulweiss/status/2114210343467536531），把日常网站登录交给 1Password 逐次审批。
3. **iOS 原生日历、提醒事项与通讯录直连（iOS Calendar, Reminders, and Contacts）**：
   从 v0.75.2（https://x.ai/changelog/bot）开始，如果你在 iPhone 上安装了 Grok Bot 移动端 App（https://cursor.com/help/grok-bot/mobile），无需折腾复杂的第三方云端 API，只需在 iOS 系统弹窗中授予权限，Bot 就能直接读取并操作你手机本地原生的 **Calendar（日历）**、**Reminders（提醒事项）** 与 **Contacts（通讯录）**。正如玩家 `@TyeInBloom`（https://x.com/TyeInBloom/status/2113767679588770271）在实战中展示的，把 iOS 原生三件套与 1Password 结合后，Bot 瞬间就能掌握你今天的日程安排与待办清单。

我建议**先连常用 App**，但初期只连一两个只读权限的服务，比如测试用的备用邮箱、iOS 日历或开启需逐次指纹确认的 1Password，先把通道打通，别一上来就接生产数据库。

## 4.3 三个零风险入门任务 · 3 Safe Starters

新手开箱最怕误删数据、乱发邮件，或者脚本写错死循环烧光周额度。

第一天别跑高风险、不可逆的任务。挑只读、不改源数据、交付标准清楚、随时能叫停的轻量活。我整理了三个**零风险入门任务**，并在末尾补充了两个结合 v0.75.2 最新特性的**进阶零风险破冰玩法**（iPhone Action Button 按住说话口述派单 + 生成第一张个人实时数据看板 Page）：

任务一是整理收件箱与退订垃圾邮件。台湾博主 Sorla 发过用 Grok Bot 整理 Gmail 的视频（https://www.youtube.com/watch?v=qL8alDehpBs）。他让 Bot 登录 Gmail 后扫描近期邮件，提炼出需回复、财务运营、项目进度三类，同时提取营销邮件底部的退订链接。底线很明确：只读、只分类、只提供退订链接清单，严禁私自点击退订或代发回复。

> [!NOTE]
> 📸 **截图位（待补）**：任务一收件箱整理与退订清单输出

任务二是公开信息比价表。买降噪耳机或采购办公设备，让 Bot 上网跑腿性价比最高。官方在采购案例里展示过 Haggle Bot 对比供应商报价压低成本（https://x.ai/news/grok-bot-procurement）。新手不需要让它去谈判，充当比价员就行。

给它两三个公开电商网站或产品型号，让它在云电脑浏览器里打开页面，抓取当前标价、满减活动和预计发货时效，汇总成四列表格。这不需要登个人账号，不碰支付接口，解析网页卡住了也不影响个人资产。

> [!NOTE]
> 📸 **截图位（待补）**：任务二电商比价与规格对比表格生成

任务三是整理行业资讯精选。科技博主 Rowan Cheung 在 X 上分享过监控任务逻辑（https://x.com/rowancheung/status/2108328114552000842）。他强调过滤规则，只保留指明旧任务、工具和实际成果的真实案例，剔除公关通稿和营销帖。

把收藏的三篇技术长文或两期周刊公开链接扔给它，按规则提炼要点。每条要点控制在两句话以内，附带原始论据的章节链接，空话套话直接扔掉。

> [!NOTE]
> 📸 **截图位（待补）**：任务三资讯精选提炼与源链接引用

这三个任务不改动生产数据，也不替你对外发声，用来破冰最稳妥。

### 2026-10 新增破冰体验：用 iPhone Action Button 口述第一个任务 & 生成第一张个人看板 Page

除了在电脑前敲字完成上面三个经典任务，随着 Grok Bot iOS v1.16 与桌面端 v0.75.2 的发布，你还可以在第一天用另外两种极具未来感且同样零风险的方式完成破冰：

#### 补充玩法 A：用 iPhone Action Button 按住说话口述第一个任务，挂断后自动收到 Voice chat card 与跟进交付

如果你使用的是配备侧边 **Action Button（操作按钮）** 的 iPhone（iPhone 15 Pro 及后续机型），且已将 Grok Bot iOS 客户端更新至 **v1.16 或更高版本**（更新后需至少打开过一次 App 以注册快捷指令），你可以彻底告别打字，直接按住手机侧键开口派活（官方发布帖 `@bot` 获 7,264 赞、2,213 书签：https://x.com/bot/status/2112246033178968161；官方语音通话文档：https://cursor.com/help/grok-bot/voice-chat；移动端文档：https://cursor.com/help/grok-bot/mobile；`@SawyerMerritt` 实机演示视频获 1,627 赞：https://x.com/SawyerMerritt/status/2112252980015579431）。

- **30 秒配置路径**：打开 iPhone 系统 `Settings（设置） → Action Button（操作按钮） → Shortcut（快捷指令） → Choose a Shortcut → Grok Bot → Start Voice Chat`（如果你想每次弹窗选择不同 Bot 或固定呼叫某个专职 Bot，可在 iOS 快捷指令 App 中新建包含 `Start Voice Chat with Bot` 动作的快捷指令再绑定到侧键，甚至配合 `"Hey Siri"` 唤醒）。
- **零风险口述实操**：长按侧边 Action Button 进入实时语音通话（支持随时切换音色 Voice、语速 Speed 与自动语种识别 Auto-detect，也支持像 `@D__cup` https://x.com/D__cup/status/2114211130365358350 那样配合韶音骨传导耳机边走边聊，或像 `@JCOMBuilds` https://x.com/JCOMBuilds/status/2112997408510452123 那样早晨语音派活），直接对着手机口述你的第一个任务：
  > “帮我查一下今天 X 平台上讨论度最高的 3 个 AI 开源项目，只做只读搜索，挂断后整理成带原帖链接的简报发在聊天框里。”
- **挂断后自动归档与交付**：当你点击挂断（Hang up）的瞬间，对应 Bot 的聊天流里会自动生成一张 **Voice chat card（语音通话卡片）**，完整记录本次通话时长与逐字稿（Full Transcript），同时 Bot 会立刻在卡片下方自动启动搜索并跟进交付整理好的简报！

#### 补充玩法 B：让 Bot 生成你的第一张个人实时数据看板 Page（Canvas）

想直观感受 Grok Bot 为什么不是普通聊天机器人，最好的办法就是让它把交付物做成一张可交互的 **Page（Canvas 看板）**（官方发布帖：https://x.com/bot/status/2112991843235610885）。不需要连接任何敏感生产库，你可以直接结合刚刚授权的 iOS 日历/提醒事项，或者让它抓取公开的 X 热门趋势，发送这样一条零风险指令：

```text
请帮我创建一张个人专属的实时效率与情报看板 Page（Make me a page with this week's metrics and schedule）：
1. 信息来源：读取我已授权的本周日历日程与待办事项（如未连接日历，则检索今天 X 平台上关于 Grok Bot 的最新 10 条高赞公开实战帖）。
2. 页面结构：在 Page 中包含三个可视化模块——顶部统计摘要卡片、按优先级排序的交互式表格，以及本周核心事项时间线（Timeline）。
3. 约束条件：仅执行只读查询，严禁修改我原有的日历事件或向外发送任何消息。
4. 交付物：直接生成并打开一张可随时热更新的 Page 卡片，保存在右侧 Library 中，并将分享权限保持为默认的 Only you（仅自己可见）。
```

几秒钟后，你就能在聊天流里点开这张排版精美的交互式 Page 卡片，体验“一句话生成专属 Web 看板”的震撼。

## 4.4 "大脑倾倒" 与 "反向提问" · Brain Dump & Reverse Config

跑通这几个轻量任务后，该怎么给自己搭 Bot？Kin 在《Grok Bot 橙皮书》第 03 章提过两个方法：“大脑倾倒”和“反向配置”（https://github.com/KinGao294/grok-bot-orange-book）。

以前用 AI 助手总要自己去配参数、写系统提示词、选底层模型。Kin 的思路是把配置动作直接交给 AI。

第一步是倾倒背景。开一个新对话，别急着下指令，把自己平时的工作情况一股脑倒给它：你的行业、业务模式、每天重复的杂活、讨厌处理的琐事、未来两周要推进的目标。想到什么写什么，像跟新来的管家交代家底。

倒完之后，直接用 Kin 的提示词做**反向配置**：

```text
基于你对我的了解，如果是你，你会怎么设置这个工作台？应该建立哪几个 Bot？它们的职位、职责和日常例行工作是什么？
```

> [!NOTE]
> 📸 **截图位（待补）**：大脑倾倒后 Bot 反向生成的岗位建议与确认界面

发出去后，系统会梳理痛点，建议建哪几个岗位，并拟好职责和日常例行工作。你只要做减法，挑最核心的一两个岗位留下就行。

不过这里有个坑要避开。官方设计文章提到过"每个账户约 50 个 Bot"的实用上限（https://x.ai/news/designing-grok-bot），但 9 月 1 日的 v0.31.0 已改为"You can create more than 50 Bots"（https://x.ai/changelog/bot）——数量不再是瓶颈，管理成本才是。核心团队 @poteto 也建议，新手起步尽量只建一个 Bot，流程复杂了再拆（https://x.com/poteto/status/2108097362283597916）。如果按建议一口气建七八个，岗位容易打架，群聊交接还白耗后台额度。

这一点在中文社区资深玩家 `@eze_is_1`（一泽Eze，351 赞、705 书签：https://x.com/eze_is_1/status/2109850538045264151）与 `@charlie_pmp`（https://x.com/charlie_pmp/status/2114214503416271131）的复盘中也得到了反复验证：虽然自 v0.75.2 起，官方将 Routine 的运行频率上限大幅提升至**全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时**（定时最小间隔仍为 5 分钟，详见官方 Routines 文档 https://cursor.com/help/grok-bot/routines），但在 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，详见 https://cursor.com/help/grok-bot/plans 与 https://cursor.com/help/the-x-subscription/overview）下，Grok Bot、Grok 与 Cursor 共享同一个周额度池（超额后扣减 Prepaid Credits 预付额度）。如果新手第一天就盲目创建七八个 Bot 并挂上高频冗余的定时 Routine，后台静默轮询会迅速吃掉你宝贵的共享周额度。因此，反向配置输出方案后，务必克制，先从 1 个主控 Bot 和 1 条低频高价值的 Routine 起步。

## 4.5 异步心态：派完活就走 · Async Mindset

用惯传统对话产品的人，刚换到 Grok Bot 会不适应：任务发出去，对话框没逐字打字，光标闪两下就安静了。很多人以为卡死，忍不住一遍遍刷页面。

官方协作文档说得很清楚，它的设计初衷是“感觉就像在给真实队友发消息”（https://cursor.com/help/grok-bot/chat-and-collaboration）。你让工位上的同事做报表，不会站在他背后盯着他敲键盘。交代清楚，你转头干别的，他做完来汇报。自 v0.71.2（https://x.ai/changelog/bot）起，iOS 与 Android 移动端的推送通知已支持 Deep-link 直接跳转到触发通知的具体某一个 Bot 聊天窗口；而在 v0.75.2 中，官方还精简了 Auto-review 冗余审批弹窗——对于你在当前对话轮次中已经明确下令执行的操作，不会再频繁弹出重复的二次确认卡片打断你的异步节奏。

用 Grok Bot 要有**派完活就走**的异步心态。输入框交代完任务，确认它接单，就可以关窗口去忙别的。它在云端电脑里开浏览器、查资料、跑命令都需要时间。做完了或者卡在审批点，它会弹系统通知找你。

![同步盯梢与异步派活心智模型对照](../../images/fig-04-2.png)

*图：同步盯梢与异步派活心智模型对照*

中途干预官方给了两种机制（https://cursor.com/help/grok-bot/chat-and-collaboration）：

一种是中途纠偏。任务跑着突然想改主意，或者发现最初给的数据源有遗漏，不用等它跑完。直接在对话里发新指令，用户直接消息在系统调度里优先级最高，能打断当前轮次、重定向流程。

另一种是紧急制动。如果发现它在云电脑里的动作完全跑偏，直接在输入框发：

```text
Stop now
```

收到这条指令，Bot 会立刻停下手头所有后台任务（https://cursor.com/help/grok-bot/chat-and-collaboration）。但官方也提醒了：紧急制动只能拦住后面的动作，撤销不了已经做完的操作。如果它刚才已经在网页上点了提交或发出了消息，既成事实撤不回来。所以出发前的约束条件才最关键，不能把安全寄托在事后制动上。

## 试试看 · Try It Yourself

光看没用，把提示词拷进输入框跑一次，才能体会怎么派活。这里准备了 5 条经典**开箱即用提示词**（外加第 6 条专为 v0.75.2 新特性定制的 **Page 实时看板生成指令**），嵌入了任务五要素，覆盖文档分析、收件箱管理、竞品调研、反向配置、资讯监控与交互式看板构建，复制就能用。

第一条：五分钟无连接器文档要点提炼与未决问题梳理（直接附加本地文档使用）

```text
请阅读我上传的这份文档，完成以下分析：
1. 提炼出 5 个最高优先级的核心事实与结论。
2. 单独建立一个章节，按时间顺序列出文中提到的所有明确日期、已达成的决策，以及尚未解决的悬挂问题（Open Questions）。
3. 每一项结论必须在末尾附带出处段落或页码引用。
4. 约束条件：严禁修改原始附件，严禁添加任何未经文档证实的推测。
5. 交付物：直接在当前对话中输出格式整齐的 Markdown 文本。
```

第二条：收件箱晨检与分类回复草稿（适用于已连接邮箱的场景）

```text
请检查我收件箱中过去 24 小时内收到的所有新邮件，并按以下规则处理：
1. 将邮件严格归入三类：必须由我决策的重要事项、日常项目进度同步、系统通知与营销邮件。
2. 针对“必须由我决策的重要事项”，提取发信人、核心诉求，并为每封信撰写一份 100 字以内的建议回复草稿。
3. 针对“系统通知与营销邮件”，检查邮件末尾是否包含退订链接，如有请提取退订链接并整理为清单。
4. 约束条件：严禁擅自发送任何邮件，严禁点击任何外部链接，严禁修改或删除任何邮件。回复草稿仅作为待办事项卡片展示给我，等我逐一点击确认。
5. 交付物：输出一份结构清晰的晨报，并将草稿呈现在独立审阅卡片中。
```

第三条：公开竞品价格与功能矩阵对比表（适用于云电脑浏览器调研）

```text
请打开云电脑的浏览器，访问以下 3 个公开产品主页：[在此粘贴链接 1]、[在此粘贴链接 2]、[在此粘贴链接 3]。
1. 提取每个产品的当前对外公布价格、收费计费周期（按月/按年）、免费试用政策，以及核心功能权益差异。
2. 约束条件：仅允许浏览公开网页，严禁尝试注册账号，严禁点击任何需要支付授权或填写个人信息的按钮。如果遇到登录弹窗或验证码阻拦，立即停止操作并在对话中汇报。
3. 交付物：将收集到的数据整合为一张对比表格，包含产品名称、价格区间、核心权益、限制条款与原始页面来源 URL。表格末尾附带一段 200 字以内的横向对比优缺点总结。
```

第四条：工作台反向配置魔法指令（用于初次开箱时的组织搭建）

```text
这是我目前的所有工作背景与日常痛点：
[在此粘贴你倾倒的所有内容：你的岗位角色、每日机械重复的琐事、最耗费时间的环节、最近要完成的目标]

请基于你对我工作现状的全面了解，反向为我设计一套 Grok Bot 工作台方案：
1. 建议我应该建立哪几个岗位的专职 Bot（优先考虑最核心的 1 到 2 个角色，避免人员冗余）。
2. 为每一个建议的 Bot 撰写一份清晰的岗位说明书，包括：名字、核心职责（One primary job）、工作原则、明确禁止触碰的安全红线。
3. 为其设计 1 项可以直接落地的日常例行工作（Routine）草案。
4. 约束条件：不要直接在系统中创建任何 Bot，先在此处输出完整建议方案供我审阅修改。
```

第五条：行业精选信息源过滤与去噪摘要（适用于资讯提炼）

```text
请阅读以下这几篇行业公开资讯/文章：[在此粘贴文章链接]。
1. 严格过滤内容，剔除所有空洞的公关辞令、未经证实的宣传口号和排比套话。
2. 仅保留满足以下条件的内容：指明了具体业务场景、使用了什么具体工具或技术方案、取得了何种可量化的实际结果（如节约的时间、缩减的步骤或降低的成本）。
3. 最终提炼不超过 3 个最有参考价值的真实案例，每个案例包含：背景痛点、核心解法、实际收益、原始来源 URL。
4. 约束条件：如果所有输入文章均不符合上述筛选标准，直接回复一行文字说明“未发现符合标准的有效案例”，不要强行凑数。
```

第六条：生成你的第一张交互式数据看板 Page（适用于 v0.75.2+ 的 Canvas 页面交付与对话层目标对齐）

```text
Make me a page with this week's metrics and key tasks（请为我生成一张本周核心指标与重点任务看板 Page）：
1. 最终结果（Outcome）：将我本周的重点工作目标、待办事项与行业关注动态整合为一个可随时查看并持续热更新的交互式单页看板。
2. 信息来源（Sources）：读取我在当前对话中提供的本周工作要点（或已授权连接的 iOS 日历/提醒事项），并结合内置的免费公开 X 检索工具抓取 5 条与我业务领域高度相关的最新高赞实战帖。
3. 约束条件（Constraints）：仅执行只读检索与画布创建，严禁修改我原有的日历数据，严禁向外发送任何消息或触发付费 API。如果对我的业务重点有任何模糊之处，请先在对话层向我提问对齐，再开始构建页面。
4. 交付物形式（Deliverable）：调用 Page（Canvas）能力创建一张包含“本周核心指标卡片”、“按优先级排序的任务进度表”与“行业高赞案例摘录”三个模块的实时交互 Page，沉淀在右侧 Library 中。
5. 人工审阅点（Review）：页面生成后先将分享权限保持为 Only you（仅自己可见），在聊天流中返回 Page card 供我审阅。
```

---

[← 上一章：§03 十分钟安装与开箱 · Install in 10 Minutes](../part1-getting-started/03-install.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§05 Bot：给每个同事一份岗位说明书 · Bots & Profiles →](../part2-core-concepts/05-bots.md)

# §06 云电脑：它的工位 · The Computer

[← 上一章：§05 Bot：给每个同事一份岗位说明书 · Bots & Profiles](../part2-core-concepts/05-bots.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§07 Skill 与 Routine：教一次，让它照着做 · Skills & Routines →](../part2-core-concepts/07-skills-routines.md)

---

很多人刚接触 Grok Bot，会以为它和 ChatGPT 或 Claude 一样，只是网页上的一个对话框。但我翻完官方文档和社区讨论后发现，关掉笔记本它还在跑，下载的文件随时能翻看，一个 Bot 登过的账号换个 Bot 也能直接用。马斯克和 Cursor 团队给每个账号配的，根本不是一个单纯的聊天模型，而是一台常驻云端的电脑。

这台云电脑就是你所有 Bot 共同上班的实体工位。如果不了解它的文件存储、网络结构和会话隔离，很容易丢配置、泄露凭据，甚至遇到数据回滚。这一章，我把这台电脑的工作机制、恢复逻辑、网络规则和社区玩法的真实风险拆开讲清楚。

### 6.1 /workspace、文件与附件 · Files

你在桌面端跟 Bot 交代任务，输入框一次最多允许上传 6 个附件（https://cursor.com/help/grok-bot/files-and-results）。单文件体积有明确限制：文档、图片和音频单个不超过 25 MB，视频不超过 200 MB（https://cursor.com/help/grok-bot/files-and-results）。它支持的格式很多，包括图片、音视频、PDF、纯文本、Office（Word、Excel、PowerPoint）、CSV、JSON、YAML、源码、HTML、邮件文件和 Jupyter notebooks（https://cursor.com/help/grok-bot/files-and-results）。如果文件损坏、加密或格式太冷门，可能会解析失败（https://cursor.com/help/grok-bot/files-and-results）。接近文件大小上限的附件能否正常解析。。

> [!NOTE]
> 📸 **截图位（待补）**：桌面端对话框中上传多个附件与解析卡片展示

在手机上，iPhone 用户可以直接用系统共享菜单，把其他 App 里的照片、文件、网页链接或文本分享给 Grok Bot；Android 版目前只支持分享文本（https://cursor.com/help/grok-bot/files-and-results）。在聊天里发链接，鼠标悬停在卡片上能预览，点击后会在本机默认浏览器打开（https://cursor.com/help/grok-bot/files-and-results）。

派任务时别只丢一个文件说“帮我分析一下”，要说清楚每个文件是什么、输出什么。为了防止 Bot 胡思乱想，官方建议明确要求交付可审查的结果：比如带小标题和来源链接的文档、定好表头和公式的表格、带演讲备注的 PPT，或者把截图和日志打包到单独文件夹；重要的任务，还可以让它把源系统事实、推断假设、已完成操作、等待审批操作和未解决疑问这五项拆开写（https://cursor.com/help/grok-bot/files-and-results）。想改结果也不用新开话题，直接让它就地修改现有的生成结果就行（https://cursor.com/help/grok-bot/files-and-results）。

云电脑里最核心的持久目录是 `/workspace`。所有 Bot 都能读写保存在 `/workspace` 里的文件，跨 Bot 协作都靠它中转（https://cursor.com/help/grok-bot/files-and-results）。如果让 Bot 把写代码的任务交接给 Cloud Agent，任务完成后，Bot 会自动把报告里引用的图片、视频和文件复制回云电脑，并作为附件放到回复里（https://cursor.com/help/grok-bot/files-and-results）。

记牢一条规则：把 `/workspace` 当成**所有 Bot 共享的持久工位**，中间产物、关键数据和交接文件都按项目文件夹存在这里（https://cursor.com/help/grok-bot/files-and-results）。保存在 `/workspace` 之外的临时文件、终端手动装的软件、没提交的应用状态，在系统更新或恢复时都会被抹掉（https://cursor.com/help/grok-bot/computer-and-apps）。

### 6.2 浏览器、终端与登录态共享 · Shared Sessions

很多人会以为自己建了五个 Bot，云端就会开五台虚拟机。并不是这样。官方设计很直接：你账号下的所有 Bot，共用同一台云电脑（https://cursor.com/help/grok-bot/computer-and-apps）。

![一台云电脑下共享浏览器会话、/workspace、终端凭据与多 Bot 独立工作屏幕的架构示意](../../images/fig-06-1.png)

*图：一台云电脑下共享浏览器会话、/workspace、终端凭据与多 Bot 独立工作屏幕的架构示意*

因为底座只有一台，整台电脑的状态是全局共享的：浏览器里的 Cookie 和登录态全局可见，磁盘上的文件全局可见，终端里的凭据全局可见，一个 Bot 做了一半另一个 Bot 随时能接手（https://cursor.com/help/grok-bot/computer-and-apps）。这台电脑绑定在你的用户账号上，而不是某个 Bot 身上；不想让其他 Bot 看到的密码或文件，绝对不能放在这台电脑里（https://cursor.com/help/grok-bot/computer-and-apps）。

为了支持多任务，系统给每个 Bot 分配了一个独立的工作屏幕（screen，10 月 7 日起分辨率从 1280×800 提升到 1920×1200（https://x.ai/changelog/bot）），多个 Bot 能并行操作浏览器和桌面工具，但单个 Bot 一次只能在自己的屏幕上做一项电脑操作（https://cursor.com/help/grok-bot/computer-and-apps）。不过要注意，独立屏幕只是工作画面的切分，**屏幕隔离并不等于安全隔离**（https://cursor.com/help/grok-bot/computer-and-apps）。

你在对话界面点 Agent Computer，能随时看它在桌面的实时操作，包括鼠标点击、打字和页面跳转；关掉客户端或合上电脑，它都在后台继续跑（https://cursor.com/help/grok-bot/computer-and-apps）。碰到密码输入、通行密钥（Passkey）、两步验证（2FA）、CAPTCHA 人机验证、支付核验，或者明确禁止自动化脚本的网站，Bot 会停下来请求人工接管（https://cursor.com/help/grok-bot/computer-and-apps）。直接在弹出的远程电脑画面里手动完成验证，再让 Bot 继续，千万别把密码或验证码明文发在聊天框里（https://cursor.com/help/grok-bot/computer-and-apps）。如果是通过受支持的插件输入机密凭据，系统会用掩码遮挡，不会存进对话记录（https://cursor.com/help/grok-bot/computer-and-apps）。

随着 v0.75.2（1Password Brokered Sign-in 上线）与 v0.75.5（Grok Bot Vault 正式全面上线）的推进，官方文档（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)、[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）明确定义了云电脑浏览器在遇到登录与结账场景时的**标准调用优先级链条（Priority Order）**：

1. **网站登录优先级链条（Sign-in Priority）**：
   `Saved browser session（云电脑已保存的浏览器会话 Cookie） → Vault（内置加密保险箱） → 1Password（Brokered Sign-in 代理逐次审批） → Secure Form（聊天内掩码安全表单） → Take over screen（人工远程接管屏幕）`
   - 当 Bot 打开目标网页时，首先检查云电脑浏览器是否已有现成的有效登录态（Saved browser session）。
   - 若未登录，则优先查询 `Settings → Vault` 中匹配的网站登录条目（包含用户名、密码与 2FA/TOTP 动态码），并通过底层 `BrowserSecureFill` 工具将密文注入输入框（Bot 上下文全程看不到明文）。
   - 若 Vault 中无对应记录且已绑定 1Password（`Settings → Connect apps → 1Password`，需本地安装 1Password 8.12.42+，详见 `@bot` [发布公告](https://x.com/bot/status/2113301060811161874) 与 `@1Password` [官方帖](https://x.com/1Password/status/2113276767582498943)），则会发起 **Review in 1Password** 请求，由你在本地电脑或手机端通过指纹/面容批准后安全填入 Personal / Private 密码库中的凭据。
   - 若以上均未命中，才会在聊天流中弹出掩码 **Secure Form**（可顺手勾选 `Securely save to Grok Bot's vault` 存入保险箱），最后一步才是请求人类点击 **Take over screen** 亲自操作云电脑屏幕（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。

2. **结账支付优先级链条（Checkout / Payment Priority）**：
   `Vault（内置加密保险箱） → Secure Form（聊天内掩码安全表单） → Link / X Money → Take over screen（人工远程接管屏幕）`
   - 特别需要注意官方帮助文档（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）与社区博主 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）、`@JianWeiSignal`（[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)）指出的关键安全边界：**保存在 Vault 中的银行卡在结账填充时，不会触发单独的逐笔 Vault 弹窗确认**，仅受通用购买审批规则约束。如果你希望每一笔消费都必须亲手输入并逐单确认卡号，切勿将主力信用卡常驻保存在 Vault 中，而应让流程回落到第二顺位的 **Secure Form** 单次输入（不勾选保存）或第三顺位的 **Link / X Money** 审批。此外，你也可以像 `@martinpaulweiss`（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）总结的“一密一宅（One home per secret）”原则那样：把带 2FA 的日常登录全部放在 1Password，而在 Grok Bot Vault 中仅存放专门用于代购的限额卡与收货地址。

浏览器登录态能持久保留，但也有风控问题。你在一个 Bot 里登了某个平台，其他 Bot 也能直接带着登录态操作；要是网站超时或风控退登、要求二次验证，记得在规则里让 Bot 暂停并通知人工，别让它去硬绕验证（https://cursor.com/help/grok-bot/computer-and-apps）。

操作第三方服务时，有插件就优先用插件。在侧边栏的 Connect apps 装上插件后，聊天里输入 `@` 调插件，输入 `/` 调 Skill（https://cursor.com/help/grok-bot/computer-and-apps）。插件走的是结构化接口，比在浏览器里模拟点击稳得多；只有没有对应插件，或者需要纯视觉操作时，才让它操控浏览器（https://cursor.com/help/grok-bot/computer-and-apps）。另外，Bot 看 X 平台上的公开推文、趋势和评论是原生只读的，不用绑你的 X 账号；只有想让它看私信、书签或主页动态时，才需要装 X 插件并登录自己的账号（https://cursor.com/help/grok-bot/computer-and-apps）。你本地的 Mac 或 Windows 和这台云电脑是物理隔离的，只有你主动开启本地电脑权限并逐项审批，Bot 才能碰你的本地设备（https://cursor.com/help/grok-bot/computer-and-apps）。

### 6.3 恢复、更新与重置 · Recover / Update / Reset

云电脑长期运行，难免会出现假死、无响应或连不上的情况。很多人一遇到故障就直接去点重置，把配好的环境清得一干二净。要排查故障，先得搞清楚 Update、Recover 和 Reset 底层都在干什么。

> [!NOTE]
> 📸 **截图位（待补）**：设置面板中的 Update、Reset 与断连状态下的 Recover 按钮界面

这三个操作的数据保留范围完全不同（https://cursor.com/help/grok-bot/computer-recovery）：

Update 是系统升级。日常的客户端更新会保留电脑里的所有东西，包括你自己手动装的应用和软件包；但整机镜像更新只会保留 Bots 配置、已保存文件和登录状态，手动装的外部软件会被抹掉（https://cursor.com/help/grok-bot/computer-recovery）。如果检测到文件没备份完，Update 会提示未就绪并放弃；如果有 Bot 正在跑任务且没法安全暂停，更新也会取消，不会强退（https://cursor.com/help/grok-bot/computer-recovery）。

Recover 是紧急抢救。它会尽量保存当前数据，拉起一台新版纯净电脑，再把数据导进去（https://cursor.com/help/grok-bot/computer-recovery）。运行中的任务会被打断；同步好的 Bots、文件和登录态能恢复，但手动安装的软件会丢失，如果电脑完全失联导致读不到最新数据，最近一点点改动也会丢（https://cursor.com/help/grok-bot/computer-recovery）。要注意的是，Recover 按钮不在 Settings 页面里，只在出现 Couldn't Reach Grok Bot's Computer 这种断连报错页时才会出现（https://cursor.com/help/grok-bot/computer-and-apps，https://cursor.com/help/grok-bot/computer-recovery）。

Reset 是重置重建。它不再读取当前故障机器的未保存数据，直接用上一次成功保存的快照重搭一台电脑（https://cursor.com/help/grok-bot/computer-and-apps，https://cursor.com/help/grok-bot/computer-recovery）。跑着的任务立刻中断，手动安装的包全没，未同步的极近期改动丢失，只有历史快照里的 Bots、文件和登录态能恢复（https://cursor.com/help/grok-bot/computer-recovery）。

云电脑有个底层机制：对话历史是独立保存在电脑外部的。哪怕在终端里敲 `rm -rf /` 删光磁盘，聊天记录也不会丢（https://cursor.com/help/grok-bot/computer-recovery）。但要注意，官方文档明确说明前端的 `node_modules` 和 Python 的 `venv` 这类依赖目录不进系统快照，电脑重建后必须重新装（https://cursor.com/help/grok-bot/computer-recovery）。如果桌面端提示磁盘空间不足，侧边栏会自动唤醒一个叫 Disk Saver 的机器人提建议，人工确认前绝不会擅自删文件（https://cursor.com/help/grok-bot/computer-recovery）。

连接断开时，按官方推荐的步骤逐级排查，**千万不要一连不上就点 Reset**（https://cursor.com/help/grok-bot/computer-recovery）：

1. 先等两三分钟，显示 Reconnecting 或失败时点 Retry，这时数据是安全的。
2. 彻底退出客户端再重新打开（Mac 用户记得在菜单栏点 Quit，不能只关红叉窗口）。
3. 去 Settings 里的 Updates 页面，有 Update 就执行更新。
4. 更新卡死或页面弹出 Recover 选项时，再点 Recover。
5. 前四步都没用，最后才点 Reset。如果在更新或重置中途卡住，不要连续点第二次重置，否则会打断正在恢复的数据流；重试一次失败后就联系官方客服（https://cursor.com/help/grok-bot/computer-recovery）。

在日常长耗时任务中，如何防止云电脑休眠断连并兼顾周额度？中文社区博主 `@eze_is_1`（一泽Eze）在获得 351 赞、705 书签的深度实战总结帖（[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151) 及进阶跟帖 [https://x.com/eze_is_1/status/2109852993982206425](https://x.com/eze_is_1/status/2109852993982206425)、[https://x.com/eze_is_1/status/2110532874000879886](https://x.com/eze_is_1/status/2110532874000879886)）中，梳理了一套防休眠断连与长任务唤醒的实战经验：
- **用事件驱动唤醒替代高频轮询保活**：尽管 v0.75.2 将 Routine 的运行频率上限提升至**全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时**（定时最小间隔仍为 5 分钟，详见 [https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)），但切忌为了“防云电脑休眠”而挂一条每 5 分钟空跑一次的保活 Routine——正如 `@charlie_pmp`（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）所剖析的，在 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，Grok Bot、Grok 与 Cursor 三端共享同一个周额度池，超额消耗 Prepaid Credits 预付额度；既有独立 Cursor Pro $20 / Pro+ $60 / Ultra $200 / Teams $40 老订户虽可保留原计划，但一旦在 `cursor.com/unify` 单向切换便不可逆，详见 [https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）体系下，高频冗余 Routine 是后台静默吞噬周额度的头号杀手。
- **`wake on done` 与 Webhook + 屏幕唤醒检测组合**：`@eze_is_1` 建议，当在云电脑上跑长耗时脚本、视频渲染或浏览器批处理时，应优先采用子任务 `wake on done` 完成回调，或者让后台脚本在跑完瞬间主动请求一条 Webhook 唤醒 Bot，并配合屏幕唤醒状态检测（screen-wake detection）与断点状态文件（checkpoint JSON 落在 `/workspace`），这样即便云电脑在空闲期进入休眠或偶发闪断，重连后也能从断点毫秒级续跑，既不断连丢进度，也不浪费一分钱周额度。

云电脑也会出故障。2026 年 9 月 8 日（UTC 时间），Cursor 社区出现过大面积回滚，很多用户反映对话记录被截断，当天建的 Bot 和群聊全没了，多端设备也被同步成截断状态（https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008）。有用户反映，Bot 午夜刚执行完促销调价，回滚失忆后第二天早晨又来问“是否要调价”，操作可能会被重复执行（https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008）。9 月 8 日 19:12 UTC，Cursor 员工 @Colin 在论坛说明了原因：后台错误地给部分用户分配了重复实例（duplicate computer），会话被路由到了没有历史数据的空机器上，修复后才逐步切回原机器（https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008?page=2）。更早前的 9 月 5 日，国内社区也有人遇到手机、Mac 和 Windows 全端连不上云电脑、点重置报错，但后台挂的监控却在跑，后来证实是后台维护导致的实例休眠（https://linux.do/t/topic/2860519）。

### 6.4 本机代理与私有网络 · Proxy & Private Network

> 适合谁：在公司网络/企业版环境里用 Grok Bot、或需要访问内网的读者。个人用户可以跳过本节，只记住"Route traffic through this computer 会让网站看到你本机 IP"即可。

在公司网络里用 Grok Bot，常会碰到一种情况：聊天和审批卡片都正常，但只要点 Agent Computer 看工作画面，页面就一直转圈或报错。

这是因为桌面端与云端走的是两条完全分开的链路：一条通往 Cursor API 主机 `*.cursor.sh`，管会话消息、账号登录和审批流；另一条直连云电脑控制平面的嵌套域名 `*.*.cursorvm.com`，管环境初始化、桌面画面推流和命令行 Shell 通讯（https://cursor.com/docs/grok-bot/proxies）。很多公司在部署 Zscaler 这类安全网关时，白名单里只配了单级通配符 `*.cursorvm.com`。但云电脑的主机名格式是 `<computer>.<cluster>.cursorvm.com`，有两级子域名，单级通配符匹配不上，第二条链路就被掐死了（https://cursor.com/docs/grok-bot/proxies）。此外，如果网关对这个域名开启了 TLS（SSL）证书审查，或者开了响应缓冲（Response Buffering），也会打断 SSE 流式长连接（https://cursor.com/docs/grok-bot/proxies）。解决办法是让公司 IT 把 `*.cursor.sh`、`*.cursor-cdn.com`、`*.cursorapi.com`、`*.cursorvm.com`、`*.*.cursorvm.com`、`cursor.com` 和 `downloads.cursor.com` 全部列入放行名单，并豁免 TLS 审查与缓冲（https://cursor.com/docs/grok-bot/proxies）。

设置面板里还有一个容易搞反的网络开关：Settings -> Computer -> Network 里的 Route traffic through this computer（https://cursor.com/docs/grok-bot/proxies，https://cursor.com/docs/grok-bot/private-networks）。

![桌面端到云电脑的双路网络与本地出口代理路由拓扑](../../images/fig-06-2.png)

*图：桌面端到云电脑的双路网络与本地出口代理路由拓扑*

国内社区有人以为这个功能是把本地电脑的代理转给 Bot（https://linux.do/t/topic/2906870）。其实完全相反。社区有人排查后指出，官方定义其实是**把云电脑的出站流量拉回本地网络**：平时云电脑访问外网用的是 Cursor 官方共享的静态出站 IP；一旦勾选这个开关，云电脑向外的出口流量（egress）会全部走你本地电脑的网络路由（https://cursor.com/docs/grok-bot/proxies，https://cursor.com/docs/grok-bot/private-networks，https://linux.do/t/topic/2906870）。开启后，目标网站看到的 IP 是你本地电脑的公网 IP，Bot 也能顺势访问你本地才能连上的公司内网服务（https://cursor.com/docs/grok-bot/private-networks）。

在 2026 年 10 月 23 日发布的 v0.75.5 版本中，官方进一步修复并加固了本地电脑流量转发（local computer traffic forwarding）的稳定性（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。这一机制在个人实战与内网互联中衍生出了两个极具价值的黄金用法：

1. **借用本机住宅 IP 突破云机房反爬封锁与 Captcha 验证码拦截（`@XueshiQiao` 实战方案）**：
   由于 Grok Bot 云电脑默认使用云服务器机房的数据中心 IP，许多风控严格的电商、机票、社交媒体或资讯网站会直接拦截请求或频繁弹出 Captcha 验证码。博主 `@XueshiQiao`（Xueshi，[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)）分享了极简破局技巧：只需在桌面端进入 `Settings > Computer > Your computer`，开启 **`Route traffic through this computer`**。开启后，云端浏览器的所有出站请求都会经由你家里或办公室的真实住宅/办公宽带 IP 发出，目标网站的反爬防火墙会将其视为普通家庭用户的正常访问，验证码与 403 拦截迎刃而解（参见官方工作流文档 [https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。
2. **个人云电脑 + Tailscale 组建跨地域私有局域网 Mesh（`@lyuan1618` 实战方案）**：
   如果你不仅想转发浏览器流量，还希望云电脑能全天候直连家里的 NAS、内网数据库、树莓派或办公室开发机（哪怕笔记本合盖不在身边），博主 `@lyuan1618`（[https://x.com/lyuan1618/status/2114214704008798674](https://x.com/lyuan1618/status/2114214704008798674)）验证了 **Tailscale 局域网 Mesh** 方案：直接在 Grok Bot 云电脑终端里安装并登录 Tailscale，将云端沙箱与家里的设备拉入同一个加密虚拟局域网（Tailnet）。组网完成后，每个节点都拥有固定的 `100.x.y.z` 内网 IP，云端 Bot 可以随时通过内网协议读写家用 NAS 挂载盘、调用内网自建 API 或 SSH 登录内网主机。

企业版（Enterprise）还支持更高级的私有网络方案：Team Setup（https://cursor.com/docs/grok-bot/private-networks）。管理员可以在控制台写脚本清单（Manifest），每台团队云电脑在开机以及大约每天一次的周期刷新时，会自动用 `sudo` 权限执行这些脚本（https://cursor.com/docs/grok-bot/private-networks）。官方给出的典型方案有两种：一是装 Tailscale 并配置连入内网 VPC 的 exit node 或 subnet routers；二是用 `cloudflared` 客户端，需要时由 Bot 执行 `cloudflared access tcp` 打开本地监听端口，连进内网数据库或 SSH（https://cursor.com/docs/grok-bot/private-networks）。写脚本时别把 Token 或 Key 硬编码在 Manifest 里，因为清单在团队内是明文显示的，密钥必须配在控制台的 Team Secrets 里，以环境变量形式注入（https://cursor.com/docs/grok-bot/private-networks）。

此外，根据官方最新企业级安全架构文档（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)），企业管理员在管控云电脑出站网络时，现已支持配置严格的**企业级出站域名白名单（Outbound Network Allowlist）**，将云端虚拟机（cloud box）的外部访问严格锁定在指定的域名与端口列表内（格式如 `*.domain.com:443`），并新增了关键的 **`Apply to MCP servers`** 勾选控制项——一旦勾选，这套网络白名单不仅约束云电脑内的终端与浏览器，还会同步强制应用于所有 MCP 服务器的出站调用请求，防止第三方插件绕过企业防火墙外传数据。同时，Grok Bot 已正式通过 **ISO/IEC 27001** 与 **ISO/IEC 42001** 国际安全与 AI 治理认证，企业安全团队还可在 OpenTelemetry 遥测导出流中通过属性标签 `cursor.surface=grok_bot` 精准过滤并审计云电脑与 Bot 的全部操作事件（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。

### 6.5 云电脑玩法 · Power Uses

NodeSeek 和 LINUX DO 上有社区帖称（个例，配置可能随时调整），这台机器底层是运行在云端的 Debian 13 虚拟机，8 核 Intel Xeon CPU、16G 内存、约 126G 硬盘（开箱剩余约 115G 可用空间），没有独立显卡，机器只有内网 IP，对外走 Cloudflare 网络，跑 Agent 时测出的下行带宽约 4G、上行约 1G（https://linux.do/t/topic/2781038，https://www.nodeseek.com/post-878897-1，https://www.nodeseek.com/post-906175-1）。

面对这台机器，社区折腾出几种玩法：
有人把它当常驻 Linux 服务器，让 Bot 下载安装 Tailscale 加入私有局域网（Tailnet），启动 SSH 后在本地用 VS Code Remote 或终端直连（https://www.nodeseek.com/post-878897-1，https://www.nodeseek.com/post-906175-1）。
有人玩套娃 Agent，即刻用户「歸藏」分享过在虚拟机里装开源 Agent（如 Pi），由 Grok Bot 作为总指挥调度 Pi 和外部模型（https://m.okjike.com/originalPosts/6a9b0894756bbb6658bf093d）；也有人搭桥接脚本接入 OpenRouter 免费模型当执行层，用 Grok Bot 做高层调度来省额度（https://m.okjike.com/originalPosts/6a9b0894756bbb6658bf093d，https://x.com/NFT_Chen）。
还有人在里面装 Cursor CLI，借云端的 Opus 5.5 模型跑后台开发与构建（https://linux.do/t/topic/2990677）。

进入 2026 年 10 月下旬，官方工程团队与高阶玩家把云电脑与本地设备的潜力挖掘到了全新高度，涌现出四大极具代表性的高阶玩法：

#### 玩法一：将家里常开的 Mac mini 注册为远程计算节点 + 部署远程 `cursor-agent worker`（`@ericzakariasson`）
Cursor / Grok Bot 产品工程负责人 Eric Zakariasson（`@ericzakariasson`）在 2026 年 10 月 24 日至 25 日连发两篇技术帖（[https://x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099)、[https://x.com/ericzakariasson/status/2114157733276525044](https://x.com/ericzakariasson/status/2114157733276525044)），展示了如何突破云端虚拟机的算力与系统限制，把家里的闲置主机变成云端 Bot 随叫随到的物理分身：
1. **常开 Mac mini 自动注册进 `Settings > Computer`**：只需在家里一台 24 小时常开的 **Mac mini** 上安装、启动并登录 Grok Bot 桌面客户端，这台 Mac mini 就会自动注册并出现在你账号的 `Settings > Computer` 设备列表中（详见 [https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。此后，无论你在外面用手机 App 还是在轻薄本上下达指令，任何云端 Bot 都可以通过远程桥接，直接在这台家用 Mac mini 上执行需要 macOS 原生环境（如 Xcode 编译、iOS 模拟器、AppleScript 或本地大算力 GPU）的本地任务。
2. **让 Grok Bot 在远程机器上自动部署 `cursor-agent worker`**：你甚至不需要自己去远程机器上敲命令配环境，可以直接在聊天窗口命令 Grok Bot 登录你的远程主机或家用服务器，自动安装并启动后台工作进程 `cursor-agent worker`，将远程物理机无缝纳入你的多智能体算力池：

```bash
# 由 Grok Bot 在远程主机或家用 Mac mini 上配置并拉起 Cursor Worker 节点
cursor-agent worker start --name "home-mac-mini-worker" --workspace ~/bot-workspace
```

#### 玩法二：在云电脑中用 Python 脚本驱动 Blender 渲染 3D 物理铰链动画（`@pengzheng_`）
很多人以为没有独立显卡的云电脑只能做做文字处理和网页截图，但 Grok Bot 设计师 Peng Zheng（`@pengzheng_`，[https://x.com/pengzheng_/status/2113786630033322239](https://x.com/pengzheng_/status/2113786630033322239) 及补充帖 [https://x.com/pengzheng_/status/2113804819274277015](https://x.com/pengzheng_/status/2113804819274277015)，获 204 赞、148 书签）演示了一场惊艳的跨界造物：
为了搞清楚云电脑的视觉标志——经典中餐外卖折盒（`to-go` box 🥡）到底是如何从一张平面纸板折叠成型的，他直接向 `@bot` 下达研究与建模指令。Bot 先在全网检索并找出了 **1908 年的原始外卖盒专利图纸**，仔细分析了每一条折痕线（crease lines）的几何关系；紧接着，Bot 在云电脑中安装并调用 **Blender**，编写 Python 脚本（`bpy`）在无头模式（headless mode）下构建出精确的 3D 纸盒网格模型，将每一个折页严格沿着 1908 年专利的折痕线绑定为物理铰链（hinge）骨骼，最终渲染出与 🥡 Emoji 角度完全一致的 3D 开合无缝循环动画，直接用作网页的 `og:video`。

```bash
# 云电脑无头模式下用 Python 脚本驱动 Blender 自动建模并渲染循环动画
blender -b -P /workspace/togo_box_1908_hinge.py -o /workspace/renders/frame_ -F PNG -s 1 -e 120 -a
ffmpeg -framerate 30 -i /workspace/renders/frame_%04d.png -c:v libx264 -pix_fmt yuv420p /workspace/togo_box_og_video.mp4
```

#### 玩法三：云电脑内挂载 Codex CLI + 完成时 Webhook 零轮询唤醒（`@AbhisheKumarA7`）与 Pi Agent + DeepSeek 极致省额度（`@hppzyy`）
如何在云电脑里跑重度代码生成或海量文本处理，同时让宝贵的 The X Subscription 周额度池几乎不掉电？社区摸索出了两套“外挂执行引擎”方案：
1. **Codex CLI + Webhook 完成时唤醒（零轮询消耗）**：博主 `@AbhisheKumarA7`（Abhishek Kumar，[https://x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578)）直接在 Grok Bot 的云电脑内部安装了 **Codex CLI**，并配合一条传入 Webhook（Incoming Webhook）。当遇到耗时十几个分钟的重度全栈构建任务时，Grok Bot 只需把任务派发给后台的 Codex CLI 进程即可挂起休息；等 Codex 构建测试全部跑完后，脚本末尾自动 `curl` 触发 Webhook 唤醒 Grok Bot 验收交付，全程**零轮询等待（zero polling token waste）**。
2. **Pi Agent（`pi`）+ DeepSeek API Key 调度员模式**：中文社区博主 `@hppzyy`（[https://x.com/hppzyy/status/2111573227881529454](https://x.com/hppzyy/status/2111573227881529454)）则在云电脑中安装了轻量级开源 **Pi Agent（`pi`）** 并配置了极低成本的 **DeepSeek API Key**。在提示词中明确规定 Grok Bot 只扮演高层“调度员（dispatcher）”，把所有吃 Token 的长文洗稿、数据清洗和代码编写任务全部通过命令行交给 `pi` + DeepSeek 执行，从而把官方周额度集中留给必须用到原生 X 检索与浏览器交互的核心环节。

#### 玩法四：在非交互式 Agent Shell 中追加 `< /dev/null` 彻底解决 CLI 挂起卡死（`@37FlowAI`）
当你在云电脑里让 Grok Bot 调用 `pi`、`codex`、`claude` 或各类命令行工具时，经常会遇到一个令人抓狂的怪象：明明一行极简单的命令，在 Agent 的非交互式 Shell 工具里却一直转圈挂起，直到超时被杀。
博主 `@37FlowAI`（[https://x.com/37FlowAI/status/2111334386339823687](https://x.com/37FlowAI/status/2111334386339823687)）记录了 Grok Bot 自主排查并攻克这一底层机制的精彩过程：许多 CLI 工具在启动时会默认检测并读取标准输入（`stdin`），而在 Agent 的非交互式子进程管道中，`stdin` 句柄往往处于打开但无数据写入的状态，导致 CLI 进程无限期阻塞等待 `EOF`（文件结束符）信号。解决办法极其优雅——只需在所有非交互式 CLI 命令末尾强制加上 **`< /dev/null`** 立即闭合标准输入，原本卡死的命令瞬间实现毫秒级返回：

```bash
# 错误写法：在非交互式 Agent Shell 中可能因等待 stdin EOF 而无限挂起卡死
pi -p "只回复OK"

# 正确写法（@37FlowAI 实测方案）：追加 < /dev/null 立即闭合标准输入，毫秒级返回
pi -p "只回复OK" < /dev/null

# 同理适用于云电脑中后台投递长任务并触发 Webhook 回调
nohup bash -c 'codex exec "完成 /workspace/app 的单元测试修复" < /dev/null > /workspace/codex.log 2>&1 && curl -s -X POST "$GROKBOT_WEBHOOK_URL" -H "Content-Type: application/json" -d "{\"status\":\"done\",\"log\":\"/workspace/codex.log\"}"' < /dev/null > /dev/null 2>&1 &
```

这些玩法技术上行得通，但背后的坑不少：

环境随时可能丢。很多人习惯了 VPS，以为配好的环境能一直用。但只要遇到整机镜像更新（Update）、系统恢复（Recover）或重置（Reset），手动装的软件包、Tailscale 进程、SSH 服务和工具链都会被清空（https://cursor.com/help/grok-bot/computer-recovery）。把核心开发环境绑在上面，一次自动升级就全白费了。

凭据也是全局共享的。这台电脑是账号下所有 Bot 共用的单一工位（https://cursor.com/help/grok-bot/computer-and-apps）。如果把 GitHub Token、云服务 API Key 或穿透密钥写进全局环境变量或配置文件，账号下的所有 Bot 都能直接读取甚至误操作这些敏感凭据（https://cursor.com/help/grok-bot/computer-and-apps）。

机器可能会自动休眠，别把它当 24 小时开机的独立服务器。LINUX DO 有社区帖称（个例），没任务时大约跑 6 小时会休眠 3 小时左右，只能靠新消息或定时任务唤醒（https://linux.do/t/topic/2875793）；在企业版管理策略里，如果连续 30 天没用，系统甚至会自动 terminate 销毁实例（https://cursor.com/help/grok-bot/computer-and-apps）。想在上面跑常驻服务，随时会断。

死循环还会烧光额度。没有沙箱限制时，让 Bot 跑常驻监听脚本，一旦逻辑死循环，额度很快就会见底。LINUX DO 社区有人记录过真实案例：建了个叫 Elon 的 Bot，没加提示词限制，结果在云端死循环自言自语，反复抓头像、尝试生成真人照片，硬生生烧掉了 4% 的整周用量限额（https://linux.do/t/topic/2807876）。

指挥云电脑干活，要记住：**它只是一次性可替换的执行工位**。不要把依赖押在虚拟机的本地持久性上。需要跑 Python 数据处理或批量任务时，把装依赖和执行步骤打包成幂等流程，随用随装，并且强制把产出存到 `/workspace`：

```text
请在这台云电脑上处理当前任务：
1. 检查执行环境，如缺失依赖则在当前会话中安装必要库（不要依赖历史残留环境）。
2. 所有中间过程文件与最终输出结果，必须保存在 /workspace/data_reports 目录下。
3. 严格禁止在脚本中硬编码任何敏感密钥或密码；若需认证，请在操作卡片中提示我手动确认。
4. 任务执行完成后，清理临时目录中的无用缓存，并在回复中列出产出文件的绝对路径。
```

---

[← 上一章：§05 Bot：给每个同事一份岗位说明书 · Bots & Profiles](../part2-core-concepts/05-bots.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§07 Skill 与 Routine：教一次，让它照着做 · Skills & Routines →](../part2-core-concepts/07-skills-routines.md)

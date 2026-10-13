# §22 常见故障速查 · Troubleshooting

[← 上一章：§21 事故档案 · Incident Files](../part8-pitfalls/21-incidents.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§23 别这么用 · Anti-Patterns →](../part8-pitfalls/23-antipatterns.md)

---

> **用法**：遇到问题先看 22.7 速查表，再跳到对应小节。**原则**：先做破坏性最小的操作，Reset 永远放在最后。

## 22.1 登录与授权异常：浏览器未聚焦、Legacy Privacy Mode 与手机号拦截 · Sign-in & Authentication

我翻官方排错文档发现，新手最容易被卡住的第一关就是登录中断。很多人在浏览器里点完登录就切去做别的事，结果回到桌面客户端，发现它一直卡在欢迎页。官方排错指南给出的硬性要求是：浏览器认证的全过程中，Grok Bot 桌面客户端必须保持打开【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。要是浏览器已经提示 Cursor 登录成功，客户端却没有自动拉回前台，别去反复刷网页。直接手动切回桌面应用，在欢迎界面重新点 Sign in；若是已经在客户端里，就进 Settings 点 **Sign In with Cursor** 重新拉起绑定【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。开通企业 SSO 的团队，必须走组织统一通道登录，不能混用个人账号【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

> [!NOTE]
> 📸 **截图位（待补）**：浏览器授权完成但客户端未响应及手机号拦截报错界面

客户端弹出 Legacy Privacy Mode 报错，不用慌，不是安装包坏了。这是因为当前登录的 Cursor 账号开了旧版隐私模式，把 Grok Bot 需要的云端持久化存储挡住了【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。遇到这种情况，进 Cursor 账号设置调整数据隐私模式，或者联系企业管理员放行即可【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

针对国内用户常遇到的手机号拦截，V2EX 社区有案例记录：用 SuperGrok 凭据登录 Grok Bot 时，系统强制弹手机号验证，输入国内手机号甚至接码平台号码都会报错“无法验证此电话号码。请尝试其他号码。”【社区】（https://www.v2ex.com/t/1241829 社区帖称，个例）。帖子下只有一条回复给出解法："美国 ip +86"，即切到美国网络环境后再提交 +86 号码，是否有效未经证实【社区】（https://www.v2ex.com/t/1241829 社区帖称，个例）。

## 22.2 中文复制粘贴变乱码：v1.14.0 的编码陷阱 · Chinese Clipboard Encoding Bug

中文环境下的文本复制踩过一个特定版本的坑。V2EX 社区反馈，客户端英文回复复制粘贴完全正常，但复制中文回复粘到外部输入框或编辑器时，文字全变成了乱码【社区】（https://www.v2ex.com/t/1247756 社区帖称，个例）。

> [!NOTE]
> 📸 **截图位（待补）**：v1.14.0 中文回复复制粘贴后乱码与无格式粘贴对比

该问题被定位在 **Grok Bot 1.14.0** (17267) 构建版本，运行环境为 runtime e9651e08edc0248a43ce2d13839fa55c7d2e1425，安装包是 embedded bundle，发布通道是 production【社区】（https://www.v2ex.com/t/1247756 社区帖称，个例），X 上也有公开的操作录屏【社区】（https://x.com/liuxu_qingdao/status/2108527380570816747 社区帖称，个例）。原帖没有给出原因，官方也没有说明【推测】。遇到这种乱码，应急办法是用无格式纯文本粘贴快捷键：Mac 按 Command-Shift-V，Windows 按 Ctrl-Shift-V，该快捷键从 v0.30.0 开始在客户端内支持【官方】（https://x.ai/changelog/bot ）。也可以直接让 Bot 把大段中文输出为云电脑 `/workspace` 下的文件再打开。

> [!TIP]
> 🧪 【实测·TODO待实测】在 macOS 与 Windows 客户端分别测试 v1.14.0 以后版本的中文剪贴板编码行为。

## 22.3 云电脑卡死与无法连接：Update、Recover 与 Reset 的严格处置阶梯 · Computer Recovery

云电脑一直停在 Starting your computer、Updating your computer、Reconnecting 或 Couldn't Reach Grok Bot's Computer 时，很多人第一反应是点 Reset，这是非常危险的误操作。官方文档明确指出：对话历史独立于云电脑存储在外部，云电脑临时断连甚至终端里误敲了 `rm -rf`，聊天记录都不会丢【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。排查必须严格遵守破坏性由低到高的处置阶梯【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）：

1. 等待与重试。系统提示重连时，Bot、文件和登录态都处于受保护状态，切勿在此期间执行重置【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。
2. 彻底退出客户端并重启。Mac 用户必须从顶部菜单栏选 Quit，不能只关主窗口【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。

> [!NOTE]
> 📸 **截图位（待补）**：Settings > Computer 中 Update、Recover 与 Reset 操作面板

3. 检查云电脑镜像更新。在 Settings > Computer（或 Settings > Updates，手机端路径为 Settings > Bot > Bot Computer）看是否有更新提示【官方】（https://docs.x.ai/grok-bot/troubleshooting.md, https://cursor.com/help/grok-bot/computer-recovery.md ）。官方把更新分两类：软件更新只刷 Grok Bot 程序本身，保留包括自行安装应用在内的所有数据；整机更新会重建整台云电脑，保留 Bot、持久化文件和登录态，但会清掉自行安装的软件包【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。如果提示文件未完成备份，Update 会自动停止，此时应继续等待备份完成，绝不能强行用 Reset 覆盖【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。如果提示有智能体无法及时暂停，等当前任务结束再点更新【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。
4. 使用 **Recover computer**。重连彻底没反应，或者更新卡死并出现该按钮时，才选 Recover【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。Recover 会尽量保存已有数据并在最新镜像上拉起新机器，这会中断正在运行的任务，并清理自行安装的软件包和未及时同步的极近期修改【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。
5. 最后保底才用 Reset。只有 Recover 和 Update 都失效，且你确认能接受丢失最近未同步数据时才能执行【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。Reset 会基于上一次成功保存的快照强制重置机器，未同步内容和自行安装的软件包都会被清除【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。更新或重置还在跑时，绝对不要点第二次。如果 Recover 或 Reset 失败，最多点一次 Retry，再次失败必须立刻停止并提工单【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。

另外，磁盘空间不足警告（Computer is low on disk space）并不是丢数据，侧栏 Disk Saver 会给出清理建议，只有经你确认后才会清理指定的电脑文件，绝不会碰对话记录【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。社区里有用户提到 9/8 重复电脑事故后周额度"确实重置了"，但没有收到邮件，这次重置是不是补偿无法确认【社区】（https://www.v2ex.com/t/1241225 社区帖称，个例）。

## 22.4 Routine 不执行与 50 分钟后台任务超时 · Routines & Background Hangs

定时任务挂上去后毫无反应，先对照官方给出的六项清单自检：Routine 开关是否启用、排程时间规则与时区是否吻合、所属 Bot 是否存在且未被删除、依赖的插件是否仍有效认证、云电脑网络能否联通目标外部服务、账号额度或按需消费上限是否耗尽【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。如果是 Slack 或 GitHub 触发的事件型 Routine，还要核对对应的频道、仓库和事件规则是否仍然有效【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

> [!NOTE]
> 📸 **截图位（待补）**：Routine 运行历史报错与 50 分钟后台超时提示

检查历史运行记录时，如果想手动触发测试，官方明确强调 **Test run** 会真实执行外部操作并产生实质动作，必须使用安全参数，严禁用危险输入试跑【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

后台任务悄无声息死掉，关键机制在于后台硬超时。Cursor 论坛里有用户贴出过系统提示"A background task was stopped after 50 minutes so it would not hang"，说明后台任务跑满 50 分钟会被强制终止【社区】（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 ）。长流程的批量扫描或数据处理如果没有拆分子任务，就会被强制切断。另外客户端从 v0.21.0 开始支持通过 Webhook URL 与 Webhook key 外部调用 Routine【官方】（https://x.ai/changelog/bot ），v0.52.0 支持暂停与恢复【官方】（https://x.ai/changelog/bot ），排查偶发故障时可以先置为暂停逐步调试。

## 22.5 邮件与消息发不出：草稿卡片、虚拟机假死与发送报错 · Email & Message Delivery Issues

Bot 答应发邮件或 Slack 消息后迟迟没有动静，往往不是网络断了，而是卡在审批环节。从 v0.45.0 开始，系统引入了草稿卡片机制，Bot 起草的内容会先以卡片形式呈现在对话里，必须由人工点击 Send 或 Discard 才会发出去【官方】（https://x.ai/changelog/bot ）。虽然 v0.64.0 增加了 Disable drafts for this Bot 选项允许跳过卡片直接发送【官方】（https://x.ai/changelog/bot ），但在开启团队策略的环境下，管理员配置的全局 Auto-review 规则优先级最高：系统中的 **Ask first** 规则永远优先于 Allow automatically 规则【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。动作只要命中审批规则就会生成等待批准的卡片，卡片放着约 10 分钟不处理就会自动过期失效【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

> [!NOTE]
> 📸 **截图位（待补）**：邮件草稿确认卡片与 Ask first 审批拦截界面

附件不合规也会直接导致发送失败。官方文档有硬性指标：单个普通文件不得超过 25 MB，视频文件不得超过 200 MB，桌面端单次最多上传 6 个附件，且文件不能带密码保护或加密措施【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。罕见格式应提前在本地转成 PDF、CSV、纯文本或常见图片格式后再上传【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

论坛还出现过客户端输入框被锁定发不出消息、但右侧虚拟机画面依然完全正常的界面假死情况【社区】（https://forum.cursor.com/t/grokbot-can-not-send-msgs-agents-virtual-machine-is-still-visible/170843 社区帖称，个例）。如果当前正有未完成的 computer-use 任务占用操作锁，先在输入框发送“Stop now”强制终止，或者接管云电脑画面手动关闭卡死页面，释放控制权后再发指令【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

## 22.6 安全过滤静默拦截：被“毒化”的 Bot 与不可逆的会话死锁 · Safety Filter Silent Failure

2026 年 10 月 8 日至 9 日，Cursor 官方论坛曝光了一起典型故障：v0.68.1 客户端中，用户的主 Bot 突然瘫痪，发任何内容都会弹通用报错，但同账号下的其他 Bot 却完全正常【官方】（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 ）。

> [!NOTE]
> 📸 **截图位（待补）**：Bot failed to respond 通用报错与已被毒化的会话状态

Cursor 官方工程师 @kevinn 于 10 月 9 日 07:36 CST 公布了排查结论：Bot 后台 runner 并没有卡死，原因是底层大模型服务商的安全过滤器把该 Bot 历史对话中的某段内容判定为违规【官方】（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。Grok Bot 每次生成回复都必须把完整上下文历史打包发给模型，哪怕用户只发一句问候，请求中携带的历史违规内容也会立刻触发安全拦截，导致模型拒绝返回结果【官方】（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。当时客户端前端没区分这种安全拦截，只能直接显示一行通用提示 **Bot failed to respond / Something went wrong**【官方】（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。

这一事故暴露了不可逆的设计痛点：重启应用和 Reset 云电脑对该故障完全无效。会话数据存放在云电脑外部，Reset 不会清空历史，且客户端当时没有单独删除单条历史记录的功能【官方】（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。官方工程师给出了处置规矩：不要尝试 Reset 电脑，也不要删除这个 Bot，把它的已有记忆和 Routine 留在原地；日常任务立即切到其他正常 Bot 或新建 Bot；绝对不要让新 Bot 去读取、总结或续写这个中毒 Bot 的历史对话，否则会把违规内容搬到新会话里，导致新 Bot 被连带封锁【官方】（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。根据发帖用户自述，诱因是曾让该 Bot 探讨过 AI 安全漏洞扫描工具【推测】（基于论坛用户自述背景推测，https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 ）。因此，涉及安全测试、逆向工程等边缘领域的内容，必须严格放在一次性隔离 Bot 中运行。

## 22.7 常见故障与排错动作速查 · Quick Troubleshooting Matrix

我把高频异常的症状与官方处置决策梳理成了这份速查阶梯。

![Grok Bot 故障症状与分级排错动作决策流](../../images/fig-22-1.png)

*图：Grok Bot 故障症状与分级排错动作决策流*

登录与授权环节：认证无法完成时，先确认浏览器登录成功后手动切回客户端，在 Settings 中点 Sign In with Cursor 重新拉起；遇到 Legacy Privacy Mode 报错，调整 Cursor 账户数据设置或联系管理员解除限制【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）；境内账号绑定遇手机号无法验证，可尝试切到美国 IP 后重新提交 +86 号码（仅一条社区回复，未证实）【社区】（https://www.v2ex.com/t/1241829 社区帖称，个例）。

文本复制与输入环节：v1.14.0 中文回复复制粘贴乱码，按 Command-Shift-V（Windows 为 Ctrl-Shift-V）无格式粘贴，或直接从云电脑 `/workspace` 下载导出文件查看【官方】【社区】（https://x.ai/changelog/bot, https://www.v2ex.com/t/1247756 社区帖称，个例）。

云电脑与环境恢复环节：连接中断或更新停滞时，严格遵循 Retry → 菜单栏 Quit 彻底重启 → Update → Recover → Reset 的顺序操作；未同步前严禁盲目 Reset，一次恢复尚未结束绝不启动第二次【官方】（https://cursor.com/help/grok-bot/computer-recovery.md ）。单个 Bot 突发持续静默并抛出通用报错时，切勿重置电脑，判定为安全过滤器毒化死锁后，直接换新 Bot 承接任务，严禁让新 Bot 读取中毒历史【官方】（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。

自动化与消息交互环节：Routine 停摆需逐项核查排程时区、Bot 存续状态、插件认证与 50 分钟超时（社区报告），手动验证仅能使用安全输入跑 Test run【官方】（https://docs.x.ai/grok-bot/troubleshooting.md, https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 ）；邮件与消息未发出优先排查 Auto-review 的 Ask first 规则及卡片状态，附件严格控制在 25 MB（视频 200 MB）和 6 个文件上限内；界面锁死可随时发送 **Stop now** 终止当前阻塞动作【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

如果按照阶梯排查依然无法解决，联系官方技术支持（https://cursor.com/help/grok-bot/get-help.md ）前，提前收集完整信息：Grok Bot 版本号、操作系统与版本、精确报错文本、涉及的 Bot 或 Routine 名称、故障发生的具体时间与时区、界面显示的完整 Request ID 或会话 ID，以及重启或更新后的对比结果；工单中绝不能附带明文密码、一次性验证码或私钥信息【官方】（https://docs.x.ai/grok-bot/troubleshooting.md ）。

---

[← 上一章：§21 事故档案 · Incident Files](../part8-pitfalls/21-incidents.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§23 别这么用 · Anti-Patterns →](../part8-pitfalls/23-antipatterns.md)

# §08 审批与安全边界 · Approvals & Safety

[← 上一章：§07 Skill 与 Routine：教一次，让它照着做 · Skills & Routines](../part2-core-concepts/07-skills-routines.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§09 连接器与 Marketplace · Connectors →](../part3-integrations/09-connectors.md)

---

很多新手刚接触 Grok Bot，总以为它跟普通聊天 AI 差不多，甚至直接在对话框里贴密码。社区里确实有翻车案例（见 8.2、8.3）。给 Bot 派活之前，必须先弄明白三件事：审批机制怎么跑、哪些账号绝对不能碰、安全红线到底画在哪。

### 8.1 Auto-review 与审批卡 · How Approvals Work

Grok Bot 在后台并不是简单匹配几个关键词。它的底层跑着一套独立的审查模型，叫 Auto Review（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。只要 Bot 准备执行 Shell 命令、调用插件、操作电脑桌面、修改 Routine 或触发器，甚至分发子任务或者唤起 Cloud Agent，Auto Review 都会在动作实际跑起来之前先做评估，决定是直接放行、弹卡拦截，还是彻底拒绝执行（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。但这套审查模型不是万能的。官方明确说明，它不会审查每一次内存写入和大多数设置变更（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。你自己配的规则才是第一道闸门。

在 2026 年 10 月 22 日发布的 v0.75.2 版本更新中，官方专门优化并精简了 Auto-review 的冗余审批弹窗逻辑（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。此前很多用户抱怨，自己明明已经在当前聊天气泡里下达了清晰明确的指令（例如指定让 Bot 发送某封特定邮件或执行某一步操作），系统却依然机械地弹出二次确认卡片打断节奏；升级至 v0.75.2 后，对于用户在当前对话轮次（current turn）中已经明确要求执行的具体操作，Auto-review 大幅减少了重复弹出的二次确认卡片，在守住非预期越权动作拦截底线的同时，显著提升了高频交互的流畅度（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。

某个动作触发审批时，聊天窗口会弹出一张结构化的审批卡，把操作目标、调用参数和具体数值列给你。界面上有三个选项：Allow once（允许这一次动作）、Always allow（保存规则并自动放行）、Deny（直接拒绝拦截）。按键盘上的 Esc 键也能取消。这套交互在 iPhone 手机端上也完全一致（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。看不懂具体影响或者确认不了目标对象时，千万别随手点允许，直接叫 Bot 用大白话解释，或者让它先交一份草稿（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。

挂机跑任务时有个时间坑。你守在聊天窗口前，审批卡会一直挂起等待。但如果是定时 Routine、外部事件触发，或者其他 Bot 私信交接的任务，审批卡等上大约 10 分钟就会自动过期（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。一旦超时，卡片就变成 Expired 状态，对应的动作会被彻底丢弃，绝不会在后台偷偷跑完。博主 @fleyta88 做 Routine 审计时也提到过这个机制（[https://x.com/fleyta88/status/2109346840382415019](https://x.com/fleyta88/status/2109346840382415019)）。过期卡片有时会给一个选项叫 Always allow this in the future，点了会把动作加入自动放行列表，但它绝不会补跑刚才超时的那次任务。想继续完成，你得叫 Bot 重新跑一次（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。特别是在 v0.75.2 将 Routine 运行频率上限大幅提升至**全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时**（定时最小间隔仍为 5 分钟）之后（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)），高频无人值守流水线若频繁撞上未配置的审批卡并超时挂起，不仅会拖慢业务链路，还会在 The X Subscription 三合一统一订阅（Premium $30/月、Super $100/月、Ultra $200/月，三端共享周额度池 + Prepaid Credits 预付额度，详见 [https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）下白白损耗宝贵的周额度。

要精细管理这套审批逻辑，打开 Settings → General → Auto-review 配置具体规则。规则分为两类：Ask first 规则只要匹配就会强制截停并弹卡询问；Allow automatically 规则允许匹配动作自动执行，前提是审查模型没发现其他潜在风险（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。如果两类规则发生冲突，系统裁决逻辑极其明确：**Ask first** 永远获胜（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。写规则时要尽量狭窄具体，比如发外部邮件前必须询问、修改生产看板前必须询问、或者在指定文件夹运行只读命令时自动放行。千万别写成允许浏览器里的所有操作，外部网页随时在变，宽泛的放行规则等于主动敞开后门（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。

规则的作用域也得注意。个人配置的 Auto-review 规则保存在当前桌面客户端，并同步到对应的云电脑，换一台新电脑登录就得重新配一套（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。在企业版环境里，管理员能在后台强制打开 Auto-review 并统一下发锁定的团队规则。个人添加的规则只能在团队基线之上变得更严，绝不可能绕过管理员策略去放宽权限（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。根据官方最新的企业级安全与合规文档（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)），团队与企业版治理能力已获得全方位加固：

- **团队自定义自然语言 Auto-Review 规则与强制模式**：团队管理员可以直接使用自然语言编写符合本组织合规红线的自定义 Auto-Review 审查规则（例如“禁止将包含客户 PII 字段的 CSV 导出到公网存储桶”或“修改生产环境 Linear 状态前必须核验工单号”），并将每条规则的执行策略显式设定为 **`Block`（直接阻断拒绝）** 或 **`Require approval`（强制弹出人工审批卡）**（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。
- **Inference Hooks（推理钩子，Beta）**：面向金融、医疗及大型跨国企业的严苛监管场景，官方提供了推理前与推理后（Pre/post-inference）合规审计拦截钩子，支持在模型请求发出前与响应落地前接入企业自有的 DLP（数据防泄漏）或合规网关（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。
- **国际权威安全认证与 OpenTelemetry 审计流**：平台已正式通过 **ISO/IEC 27001**（信息安全管理体系）与 **ISO/IEC 42001**（人工智能管理体系）双重国际权威认证；同时，企业级 OpenTelemetry 遥测导出流现已支持通过专属属性标签 `cursor.surface=grok_bot` 精准过滤和检索来自 Grok Bot 的全部工具调用、审批决策与安全审计事件（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。

涉及本机文件时，一定要检查 Settings → General → Bot → Execution on Local Computer（或者每台电脑的独立设置），把本机执行权限从 Ask every time 改成更安全的 Never allow。除非你很明确需要 Bot 操作物理机上的文件，否则坚决不要开本机执行入口（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。

此外，针对广大用户最关心的“授权 Grok Bot 代购下单、绑定支付方式是否会导致买错商品或银行卡泄露”的资金安全顾虑，在 2026 年 10 月 14 日 v0.71.2 正式支持 Link 与 X Money 结账审批后（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)），Elon Musk（`@elonmusk`）于 2026 年 10 月 15 日公开发帖做出了极具分量的 **SpaceX 全额兜底赔付承诺**（[https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445)，获 17,221 赞、1,686 转发、2,128 书签）：

> *"This works well. If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole."*
> （这非常好用。如果 Grok @Bot 在代购时犯了错，或者泄露了你的银行卡——迄今为止从未发生过——SpaceX 将对你进行全额赔付。）

社区用户 `@gofordylan` 也在实测代购后晒出账单流水（[https://x.com/gofordylan/status/2110726444485607797](https://x.com/gofordylan/status/2110726444485607797)）：当使用 X Card 经由 Grok Bot 完成审批与付款后，交易记录旁会自动点亮一枚专属的 Grok Bot 小徽章，方便持卡人一眼核对哪些消费是由 AI 助理代办执行的。

> [!NOTE]
> 📸 **截图位（待补）**：后台 Routine 触发的审批卡在 10 分钟后超时显示 Expired 与操作按钮

### 8.2 凭据交接与 1Password · Secrets

很多人图省事，Bot 一问密码就随手打在对话框里发过去，这是最危险的习惯。X 社区出过真实事故：有用户在一个拉了多个 Bot 的协作群里误发了账号密码，结果群里所有 Bot 全在会话上下文里读到了明文凭据，所有 Bot 都记住了这个密码（[https://x.com/i/status/2107339523038331338](https://x.com/i/status/2107339523038331338)）。官方安全指南写得很明确：绝不能在普通聊天文本中发送密码或一次性动态验证码（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。

遇到账号登录、通行密钥验证、双重验证（2FA）、图形人机验证（CAPTCHA）或者支付确认页面，官方的标准流程是人工接管：

1. 在客户端打开 **Agent Computer** 视图。
2. 点击接管控制权（Take control）。
3. 在打开的浏览器或窗口里亲手输完账号密码或扫码认证。
4. 把控制权交还给系统，并在对话框里告诉 Bot 继续往下走（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。

整个过程 Bot 接触不到你的明文密码，认证全在你的眼皮底下完成。

如果是系统支持的连接器服务，Bot 会弹出专门的安全机密请求卡片。这种卡片有独立输入通道，输入的凭据会被自动打码遮罩，既不会存进聊天记录，也不会暴露给底层大模型（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)；[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）。网页里需要填写登录凭证、送货地址或者电话号码时，Bot 也能在聊天界面弹出内联表单（Inline Form），一次一步让你填，再替你代填到网页表单里（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)；[https://x.com/mattyp/status/2102759899314741736](https://x.com/mattyp/status/2102759899314741736)）。如果你用 YubiKey 这类硬件安全密钥，在 Settings → General → Security Key 中开启硬件安全密钥支持后，云电脑里的浏览器能直接联动你插在物理机上的硬件密钥，每次调用都会先弹窗要求你手动授权（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。不过官方指出，目前该功能在 macOS 和 Windows 上默认开启，Linux 系统官方暂未支持（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。

至于常用的密码管理工具，官方在 9 月中旬推出了 1Password 插件集成（9/15 的 v0.53.0 写明首发在 Mac 上）（[@bot 9/17 发布帖](https://x.com/bot/status/2100335532597502311)；[x.ai/changelog/bot](https://x.ai/changelog/bot)）。这个集成的边界设计很克制，不会把你整个密码库暴露给 Bot，它只能读取连接时创建的“Shared with Grok Bot”这一个独立保险库（第三方 learngrokbot 插件目录转述，research/web/learngrokbot-plugins.md；官方 @bot 帖只说"Share items in a vault, approve each fill"）。你的私人主密码库、银行密码和敏感密钥依然被隔离在外部。更底层的 OAuth 连接器凭据也有保护机制：所有连接器的授权令牌都保存在 Cursor 后端服务器上，Bot 调用外部工具时拿不到原始 Token，云电脑的本地硬盘上也绝不存储任何授权令牌（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。

到了 2026 年 10 月 22 日至 10 月 23 日（v0.75.2 与 v0.75.5 版本），Grok Bot 的凭据安全与自动填充体系迎来了一次里程碑式的重构升级（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）：早期“1Password 必须手动配置专门的共享 Vault 和 Service Account Token 才能用”的繁琐模式已成为历史，官方全面上线了 **1Password Brokered Sign-in（代理逐次授权登录）** 与 **Grok Bot Vault（内置加密保险箱）** 两大核心支柱（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)；[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。

#### 8.2.1 1Password Brokered Sign-in：零共享库、零 Token 的逐次生物识别授权

2026 年 10 月 22 日，1Password 官方正式发布面向 AI 智能体的 `"1Password for Agents"` 架构，并将 Grok `@Bot` 作为首发标杆合作伙伴（`@1Password` 官宣帖：[https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)，获 10,507 赞、1,076 转发、7,122 书签；`@bot` 同日官宣帖：[https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874)，获 3,663 赞、276 转发、964 书签）。

在新版 **1Password Brokered Sign-in（代理逐次授权登录）** 模式下，你**不再需要创建专门的共享密码库（shared vault），也不再需要配置 Service Account 令牌**（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。其完整工作流与技术边界如下：

1. **前置条件与绑定路径**：确保你本地电脑或手机上的 **1Password App 已更新至 8.12.42 或更高版本**并处于可解锁状态；随后在 Grok Bot 客户端进入 `Settings → Connect apps → 1Password → Connect` 完成绑定，或者在 Bot 遇到登录页面主动请求凭据时直接按提示连接（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。
2. **`Review in 1Password` 逐次生物识别审批**：当 Bot 在云端浏览器中遇到需要登录的目标站点时，会向 1Password 发起凭据请求，并在聊天界面弹出 **Review in 1Password** 提示卡片。此时你只需在自己设备的 1Password App 弹窗上通过生物识别（Touch ID / Face ID 指纹或面容）或 Passkey 批准本次特定请求，1Password 就会直接将账号密码安全注入到 Bot 的云端浏览器会话中——**Bot 在整个过程中绝不会在聊天记录或上下文窗口中看到任何明文密码**（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)；[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。
3. **默认读取范围边界**：根据官方文档说明，新版 Brokered approval 模式默认读取已连接 1Password 账号下的 **Personal / Private vault（个人/私有密码库）** 中的条目；存放在其他共享（Shared）或自定义 1Password 密码库中的条目默认不会被读取，若需让 Bot 调用，只需将该条目移动或复制到 Personal / Private 库中即可（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。
4. **新旧两套 1Password 方案对比与平滑迁移**：官方目前允许新版 Brokered approval 与旧版共享库方案并存。如果你此前配置过旧版（Legacy Shared vault + Service Account Token），只需前往 `Settings → Connect apps` 中点击断开（Disconnect）并重新连接（Reconnect）1Password，即可一键升级切换至新版 Brokered approval 代理授权模式（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。

| 对比维度 | 新版 1Password Brokered Sign-in（v0.75.2+ 推荐） | 旧版 1Password 共享 Vault + Service Account |
|---|---|---|
| **配置复杂度** | 极简，安装 **1Password App 8.12.42+** 后一键 Connect，无需配 Token 或建新库 | 繁琐，需手动新建独立共享 Vault 并生成 Service Account Token 粘贴绑定 |
| **授权审批体验** | 每次登录弹出 **Review in 1Password**，在 1Password App 内按指纹/刷脸逐次放行 | 依赖 Grok Bot 端审批与共享库访问权限控制 |
| **默认读取范围** | 直接读取已连接账号下的 **Personal / Private vault** | 仅限专门划分出来的独立共享 Vault |
| **明文隔离级别** | 零知识注入，Bot 上下文与聊天流完全看不到明文密码 | 零知识注入，但需人工维护共享库内的条目同步 |
| **升级迁移方式** | 默认启用 | 在 `Settings → Connect apps` 中 **Disconnect 后 Reconnect** 即可升级 |

社区很快用这套能力跑通了高价值工作流。例如中文社区博主 `@oxpsats`（偶像派作手）分享了他的投研实战（[https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670)）：将自己的彭博社（Bloomberg）付费会员登录凭据通过 1Password 授权给 Grok Bot，让 Bot 能够自动登录突破付费墙（paywall），全天候抓取并深度研读海外一手核心财经报道，既保住了高价值订阅账号的密码安全，又彻底打通了付费信源的自动化研报流水线。

#### 8.2.2 Grok Bot Vault：内置只写加密保险箱、扫卡录入与 `BrowserSecureFill`

紧接着在 2026 年 10 月 23 日（v0.75.5 版本），官方正式全面上线了内置加密保险箱 **Grok Bot Vault**（`@bot` 官宣帖：[https://x.com/bot/status/2113754107861532677](https://x.com/bot/status/2113754107861532677)，获 9,398 赞、767 转发、2,756 书签；官方文档：[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）。

通过打开客户端 `Settings → Vault`，你可以将日常高频使用的三类敏感凭据统一存储在加密且**只写（write-only）**的安全存储区中（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）：

- **Logins（网站登录凭据）**：包含网站域名/URL、用户名、密码以及 **2FA / TOTP 动态验证码密钥**（Bot 可在登录时自动生成并填入动态码）。
- **Cards（银行卡信息）**：包含信用卡或借记卡卡号、有效期、CVV/CVC 安全码与持卡人姓名。
- **Contact info（常用联系与收货信息）**：包含姓名、收货地址、电话号码与电子邮箱，方便购物或填表时一键自动填充。

官方为 Grok Bot Vault 设计了四种极其顺手的录入方式与智能检索标签机制（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）：

1. **手动添加与手机摄像头 Scan 扫卡**：进入 `Settings → Vault`，点击 `Add login`、`Add contact` 或 `Add card`。在 Grok Bot 手机端 App 上添加银行卡时，可直接点击 **Scan** 按钮，将手机摄像头对准实体银行卡正面，系统会自动完成卡号与有效期的光学识别录入（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)；[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。
2. **聊天内安全表单（Secure Form）顺手存**：当 Bot 在网页登录或结账环节向你弹出带掩码的聊天内安全表单（In-Chat Secure Form）时，只需勾选表单下方的 **Securely save to Grok Bot's vault** 选项再提交，该凭据就会自动加密归档进 Vault，下次无需重填（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）。
3. **5 MB CSV 密码库批量导入**：如果你此前把大量账号保存在浏览器或其他密码管理器里，可以进入 `Settings → Vault → Import`，直接上传来自 **1Password、Chrome、Safari、Firefox、Bitwarden 或 LastPass** 导出的标准 CSV 文件进行一键批量导入，单次上传文件大小上限为 **5 MB**（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)；[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。
4. **明文 `Hint`（提示标签）机制**：在 Vault 中保存每条凭据或银行卡时，你都可以填写一段明文的 **Hint** 说明（例如 *"Use for work travel only"*、*"Corporate Amex - 差旅报销专用"* 或 *"家庭买菜卡"*）。**Bot 可以直接读取这段明文 Hint**，从而在你拥有多张信用卡或多个同名站点账号时精准挑出正确的那一条，但 Bot 永远无法读取背后的加密密码、完整卡号或 CVV 安全码（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）。

在底层实现上，Vault 采用严格的**只写（write-only）架构 + `BrowserSecureFill` 安全注入**（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）：任何密码、完整银行卡号与 CVV 一旦存入 Vault，无论是你在客户端 UI 界面查看，还是 Bot 在推理上下文中调用，都无法再次回显明文；当网页需要填入时，Bot 只能调用底层的 `BrowserSecureFill` 工具将加密机密直接注入目标网页的 DOM 输入框中。

#### 8.2.3 必须高亮的结账边界与“一密一宅”双库分家实战

随着 Vault 与 1Password 同时就位，Grok Bot 在遇到登录和结账任务时的底层调用顺序也已在官方《Work 工作流文档》（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）中正式确立：

- **登录（Sign-in）调用优先级顺序**：
  `Bot 云电脑上已保存的浏览器会话（Saved browser session）` → **`Vault`** → **`1Password`** → `聊天内安全表单（Secure Form）` → `人工接管屏幕（Take over screen）`（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。
- **结账支付（Checkout / Payment）调用优先级顺序**：
  **`Vault`** → `聊天内安全表单（Secure Form）` → **`Link / X Money`** → `人工接管屏幕（Take over screen）`（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。

> ⚠️ **【核心安全红线高亮：保存在 Vault 中的银行卡在结账填充时不会触发单独的逐笔 Vault 确认弹窗！】**
> 根据官方《Secrets & Vault 帮助文档》（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）明确规定：**一旦你将银行卡保存在 Grok Bot Vault 中，Bot 在结账页面调用 `BrowserSecureFill` 自动填充该卡信息时，不会触发单独的逐笔 Vault 弹窗确认（a card saved in Vault is filled at checkout WITHOUT a separate per-charge Vault prompt）**，该动作仅受通用的购买审批规则约束！
> 英文社区博主 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）与中文社区博主 `@JianWeiSignal`（见微｜Signal，[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)、[https://x.com/JianWeiSignal/status/2114195638988501103](https://x.com/JianWeiSignal/status/2114195638988501103)）均在第一时间抓取到了官方条款中的这一关键细节并发出强烈安全提醒：如果你对资金风控高度敏感，希望**每一笔消费都必须亲手把关确认才能填入卡号**，请**切勿将主力大额信用卡常驻保存在 Vault 中**（若已存入，建议立即前往 `Settings → Vault` 将其移除，改用每次结账弹出聊天内 Secure Form 时单次输入且不勾选保存，或仅存入设置了单日低消费限额的虚拟卡/副卡）。

那么，在既有 **1Password** 又有内置 **Grok Bot Vault** 的当下，重度用户到底该如何科学分配两边存放的机密？社区开发者 `@martinpaulweiss`（Martin Weiss）在 2026 年 10 月 25 日提出的 **“一密一宅（One home per secret）”拆分法**（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）给出了极具参考价值的最佳实践范式：

1. **所有日常网站登录凭据（含 2FA 动态码）统一驻留 1Password**：将日常使用的 SaaS、媒体订阅、办公后台账号与对应的 2FA/TOTP 全部放在 1Password 中管理。每次 Bot 需要登录时，通过 1Password App 弹出 `Review in 1Password` 按指纹审批，既享受跨设备密码库同步，又拥有最硬核的逐次生物识别闸门。
2. **Grok Bot Vault 仅存放限额支付卡与常用收货地址（Contact info）**：利用 Vault 在结账与填表链路上的第一优先级优势，只在 Vault 中存放用于日常代购的低限额银行卡和标准收货地址/电话，并通过清晰的 `Hint` 标注用途。
3. **Bot 新注册的临时账号暂存 Vault，定期清理迁回 1Password**：当你派 Bot 去某新网站自动注册账号时，允许它先暂存在 Grok Bot Vault 中；事后定期将有长期保留价值的账号统一迁入 1Password 并从 Vault 删除（也可配合 `@LisaMAUSA` 分享的 `Vault Tidy` 模板定期扫描去重 Vault 条目，见 [https://x.com/LisaMAUSA/status/2114208018388643852](https://x.com/LisaMAUSA/status/2114208018388643852)），严格做到 **“One home per secret（每项机密只有一个唯一真源）”**，彻底杜绝两套密码库两边保存、密码修改后一邊过期失效的混乱局面。

你可以直接在给主控 Bot 的初始化规则中加入这段凭据管理指令：

```text
【凭据与支付调用安全规范】
1. 登录外部网站时，若当前无有效浏览器会话，请优先发起 1Password 授权请求（Review in 1Password）或调用 Vault 中带有匹配 Hint 的登录项，严禁在聊天窗口索要任何明文密码或 2FA 验证码。
2. 涉及结账与表单填写时，请先读取 Vault 中各条目的 Hint 标签，严格选用匹配当前场景的联系地址与指定卡片。
3. 即使 Vault 中已存有银行卡，在最终点击“提交订单 / 确认支付（Place Order / Pay Now）”按钮之前，必须先在聊天窗向我汇报【商品明细、含税总价、收货地址、拟调用卡片的 Hint 名称】，等待我明确确认后方可完成最终扣款点击。
```

> [!NOTE]
> 📸 **截图位（待补）**：Agent Computer 中手动接管界面与安全机密请求卡片

### 8.3 哪些账号不要登录 · Never Log In

用 Grok Bot 最容易犯的一个误区，是以为建了不同的 Bot 就等于建了不同的隔离沙盒。官方架构文档写得很清楚：Cursor 在租户隔离层面采用的是每个用户独立的 **Firecracker microVM**，拥有独立内核、内存与虚拟设备，不同用户之间绝对隔离（[https://cursor.com/docs/grok-bot/security-faq](https://cursor.com/docs/grok-bot/security-faq)）。但在同一个用户账号内部，你创建的所有 Bot（不管多少个）共用同一台云电脑、同一个浏览器环境和同一个 /workspace 工作目录（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)；[https://x.ai/news/designing-grok-bot](https://x.ai/news/designing-grok-bot)）。官方在安全文档里专门警告过：绝不要把不同的 Bot 当作安全边界（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。

这个设计导致过一起被媒体广泛报道的泄密事故。XMTP Labs 首席执行官 Shane Mac 把 Grok Bot 连上自己的个人银行账户，当作只读的财务助手；结果 Grok Bot 以他本人的身份，把一份包含健身房会员、装修开销、刷卡支出等明细的"monthly financial audit"发进了公司的 Slack 频道。Mac 自己的解释是：不同的 Bot 共用同一台云电脑，另一个 Bot 因此拿到了他的财务数据（媒体报道，https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。报道还提到，产品发布约一周后马斯克曾在 X 上回复一位网友"Try it out"，并说 Grok Bot 出错的话 "we will make you whole"，Mac 事后也引用了这句话（同上）。据第三方报道，Grok Bot 事后增加了频道权限相关控制（research/enterprise.md 汇总的 RuntimeWire/Business Insider 报道），细节以官方为准。

评测博主在解析七天试用安全风险时也讲过这个隐患：只要一个 Bot 登录过某个网站，浏览器会话就会保存在这台机器上，你账号下的其他所有 Bot 都能直接接管这个会话（[https://ytget.cc/entry/grok-bot-chinese-test-7-day-trial-security-risks](https://ytget.cc/entry/grok-bot-chinese-test-7-day-trial-security-risks)）。因此，有三类账号必须列入绝不登录的黑名单：第一类是个人与企业的网络银行、券商及涉及资金调拨的支付后台；第二类是绑定了全部资产与重置权限的个人主邮箱；第三类是公司内部核心权限系统与包含最高敏感数据的生产环境数据库。如果某项业务确实必须使用独立凭证，官方给出的正规解法是为该业务单独分配一个 Cursor 用户账号，换一台全新隔离的云电脑（[https://cursor.com/docs/grok-bot/security-faq](https://cursor.com/docs/grok-bot/security-faq)）。在当前订阅体系下，无论是沿用既有独立订阅（Cursor Pro $20/月、Pro+ $60/月、Ultra $200/月、自助式 Teams $40/人/月，老订户不主动在 `cursor.com/unify` 切换即可保留原计划，一旦单向切换至统一订阅则不可逆），还是为高敏业务单独开通一个全新的 **The X Subscription 三合一统一订阅**账号（Premium $30/月、Super $100/月、Ultra $200/月，详见 [https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans) 与 [https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)），只有跨账号才能在底层获得完全独立的 Firecracker microVM 与独立的 Vault 存储空间。

除了数据泄露，高频或异常的自动化操作还会直接引来第三方平台的风控。社区实测表明，多个 Bot 在同一台机器上并发操作外部网站时，很容易被目标网站判定为多账号异常共享登录，直接锁定会话（[https://x.com/i/status/2100351900881207770](https://x.com/i/status/2100351900881207770)）。有用户把 Grok Bot 接入 WhatsApp 后，两个个人账号直接被封禁（[https://www.reddit.com/r/GrokBot/comments/1w11r70/](https://www.reddit.com/r/GrokBot/comments/1w11r70/)）；而在 LinkedIn 上，只要 Bot 尝试发送消息，账号现有的所有登录会话就会被全部踢下线（web/learngrokbot-plugins.md）。更要命的是，普通个人版和自服务 Teams 团队默认对外网是全部放行的（Allow All），在后台禁用某个插件并不能阻止 Bot 通过浏览器直接访问该网站（[https://cursor.com/docs/grok-bot/security-faq](https://cursor.com/docs/grok-bot/security-faq)）。只有企业版（Enterprise only）才提供 Network Controls 这一网络策略面板，允许管理员配置严格的域名与 IP 白名单（Team Allowlist Only，支持如 `*.domain.com:443` 格式），并且官方现已支持勾选 **`Apply to MCP servers`** 选项，将该出站网络白名单同步强制应用于所有 MCP 服务器的调用请求，在网络层把云电脑与 MCP 插件的访问路径彻底锁死（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。

![多用户间 Firecracker microVM 强隔离与同用户内所有 Bot 共享单机环境对比](../../images/fig-08-1.png)

*图：多用户间 Firecracker microVM 强隔离与同用户内所有 Bot 共享单机环境对比*

### 8.4 草稿优先原则 · Draft First

安全使用 Bot，核心原则就四个字：**草稿优先**。社区博主 @Michael_Fenech_ 在总结新手使用法则时强调：给高风险动作加闸，发送、购买、删除、合并等行为默认一律只生成草稿（[https://x.com/Michael_Fenech_/status/2105697750645977298](https://x.com/Michael_Fenech_/status/2105697750645977298)）。最管用的防线永远是写在提示词第一句里的明确限制。任务一开始就要划清禁区：哪些事情能自主完成，哪些地方必须立刻停下来请示（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。

官方在文档里给过一个范本句式：核对活动数据并起草预算调整方案时，明确写出不要直接更改活动配置，也不要给合作方发消息，在展示当前数值、建议调整数值以及预期影响之后，必须停下来请求审批（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。特别是向外发送邮件与通知、在社交媒体公开发帖、涉及转账与购物付款、删除或覆盖已有文件、修改权限配置、变更生产环境代码，以及勾选同意法律协议，这七大类动作官方强烈建议必须设置明确的审批截停点（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。记住，审批卡拦截的是即将发生的下一步动作，已经执行完毕的操作是根本无法通过审批回滚的（[https://cursor.com/help/grok-bot/approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)）。

别盲目相信模型的自主判断。Bot 在上网浏览网页、读取插件结果或者执行命令返回终端输出时，外部内容很可能藏着恶意诱导或者提示注入（Prompt Injection）代码，试图劫持 Bot 的执行流去干坏事（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。虽然系统会把外部读到的数据打上不可信标记，并通过 Auto Review 与用户指令核对，但官方直接指出，这些手段只能降低风险，绝不可能彻底消除恶意外部内容的威胁（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。人工确认就是防止注入劫持的最终底牌。

在官方的实际业务案例中，这种边界控制有很严格的规范。官方公布的采购专用 Bot（Haggle Bot）系统提示词结构，就树立了标准的三档权限范式：明确划分为 Always allowed（始终允许自主读取数据和比价）、Needs explicit go（必须获得明确授权才能向供应商发起议价报价单）、以及 Never（绝对禁止私自签合同付款）（[https://x.ai/news/grok-bot-procurement](https://x.ai/news/grok-bot-procurement)）。在官方客服团队的落地实践中，他们遵循爬、走、跑（crawl/walk/run）的三步推进法：最初接入工单系统时，Bot 只被允许在后台写内部备注（internal notes），所有对外回复和写操作强制人工审批，直到积累了大量数据并建立起严格的自动化评估体系后，才在低风险场景逐步放开直接回复（[https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）。正是依靠这套严谨的分级审批与批量审批卡（batch approval card）机制，官方客服五 Bot 舰队在并入 SpaceX SuperIntelligence 后工单量暴增 175% 的高压下，不仅实现了 99% 退款全自动闭环与单票成本降至 $0.20–$0.30，更在一次突发线上故障中仅靠一名工程师审核一张批量审批卡，就在 10 分钟内安全清零了 204 张故障工单（[https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）。

派活时可以直接套用这套防御型提示词模板：

```text
你负责执行本次任务，但在操作过程中必须严格遵守以下执行边界：
1. 本次任务的所有对外动作仅限生成草稿，绝对禁止直接点击发送、发布、下单或付款。
2. 遇到任何删除文件、覆盖已有数据、修改权限或变更生产环境的操作，必须立刻停下。
3. 完成数据比对或草稿起草后，请在回复中详细列出：当前状态、拟修改内容、以及预期产生的影响。
4. 必须等待我明确回复同意并提供批准后，方可执行下一步操作；未收到确认前，保持等待状态。
```

把任务变成定时 Routine 之前，必须做一次完整的破坏性边界测试。写明禁止发送后，无人值守的 Routine 是否始终停在草稿状态。

### 红黄绿权限表

![红黄绿权限表](../../images/fig-08-2.png)

我把常见的操作场景整理成了这张权限对照表，派活和配权限时可以严格对照执行：

| 权限等级 | 适用操作场景 | 系统配置建议 | 核心防护机制 |
|---|---|---|---|
| 红灯：严禁授权（必须人工亲自接管） | 个人与公司网络银行、证券交易、资金转账、主邮箱主密码、核心生产数据库、最高控制台登录、双重验证（2FA）输入、签署法律协议 | 严禁在云电脑登录任何网银或主账号；在 Settings 中将 Execution on Local Computer 设为 Never allow；企业版配置 Network Controls 域名白名单（勾选 Apply to MCP servers）；切勿将主力大额信用卡常驻存入 Vault | 遇到高敏登录与大额支付步骤，强制打开 Agent Computer 点击 Take control 手动接管或使用 1Password 逐次生物识别授权；绝不在普通聊天中粘贴任何凭据文本 |
| 黄灯：仅限草稿（每次必弹审批卡） | 向外部发送邮件或通知、社交媒体公开发帖、Shopify 商品信息上架、采购询价与调价发单、删除或覆盖既有数据、修改 Routine 定时规则 | 在 Settings → General → Auto-review 中添加针对发信、变更看板等动作的 Ask first 规则（企业版配置 Require approval 自定义规则）；在初始提示词中固定写入禁止直接发布 | 严格执行草稿优先原则；系统弹出审批卡由人工核实变更影响后再做决策；后台触发的任务若 10 分钟无人审批则自动过期拦截 |
| 绿灯：允许只读（低影响可自动放行） | 抓取公开网页资讯、阅读非敏感格式文件、比价表格整理、在 /workspace 内部生成报告、拉取只读数据看板、运行 git status 等只读检查 | 在 Settings → General → Auto-review 中针对指定路径下的安全只读命令配置 Allow automatically 规则；连接只读性质插件 | 限制在隔离的 Firecracker microVM 云电脑内执行；由 Auto Review 模型做后台安全校验；不赋予任何不可逆写权限 |

---

[← 上一章：§07 Skill 与 Routine：教一次，让它照着做 · Skills & Routines](../part2-core-concepts/07-skills-routines.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§09 连接器与 Marketplace · Connectors →](../part3-integrations/09-connectors.md)

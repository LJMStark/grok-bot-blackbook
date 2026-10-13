# §11 中国用户的集成：没有插件也能用 · China Integrations

[← 上一章：§10 官方合作集成逐个讲 · Partner Integrations](../part3-integrations/10-partners.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§12 群聊与交接 · Groups & Handoffs →](../part4-multi-bot/12-groups.md)

---

> 说明：国内平台没有官方连接器，所以本章大部分内容来自社区帖和第三方教程，标。使用前请自行核实，并注意平台规则。

国内用户打开 Grok Bot 的连接器市场，大概率会傻眼：除了 Gmail、Notion、Slack、GitHub 和 X，没有任何国内常用软件。微信、飞书、公众号、小红书、抖音、视频号全都没有插件，连 QQ 邮箱和网易邮箱也找不到原生入口。很多人看到这里就打了退堂鼓，觉得这套工具在国内根本没法用。

但我调研了一圈发现，Grok Bot 的核心价值本来就不是那几个官方插件，而是那台 7×24 小时常驻在云端的虚拟电脑。只要云电脑能发网络请求、能开浏览器、能跑脚本，就算国内平台没有官方接口，也能把工作流搭起来。这一章我把社区摸索出来的国内平台接入方案、故障表和合规边界整理出来。

## 11.1 微信接入（iLink/ClawBot）· WeChat

> 前提条件：微信版本满足下文要求且"插件"里能看到微信ClawBot（并非人人可见）；能看懂 Bot 在云电脑上写的转发脚本出错信息，或愿意让 Bot 自己排错。不写代码的读者也能照提示词跑通，但出故障时排查门槛偏高；只想"看数据、出草稿"的读者可以先读 11.3。

微信是国内每天打开频次最高的消息入口。过去十年里，微信机器人方案换了一代又一代：2016 到 2017 年基于 Web 协议的 itchat 和 wxpy 被彻底切断接口；2017 到 2019 年基于 Xposed Hook 修改客户端的方案随版本更新失效；2019 到 2025 年灰产常用的 iPad 协议屡遭起诉；本地 PC Hook 注入内存方案也随时有封号风险（https://ele.ac.cn/2171/）。

这次社区走通的方案不太一样。它基于腾讯随 OpenClaw 框架开放的个人微信 Bot 接口 iLink，域名是 `ilinkai.weixin.qq.com`（https://ele.ac.cn/2171/）。通信走纯 HTTP 和 JSON 协议，不需要 WebSocket，也不用在公网开端口，云电脑全程只发出站请求（https://xput.app/N4rlhi）。配合微信客户端自带的「微信ClawBot」插件，真正要人工操作的只有发一段提示词、复制两个凭据、扫一次码。

这个通道底层依赖四个 HTTP 接口：先调 `get_bot_qrcode` 拿绑定二维码；再轮询 `get_qrcode_status` 获取授权状态并提取 `bot_token`；接着转发脚本调 `getupdates` 做长轮询，单轮挂起约 35 秒带游标拉取消息；处理完后调 `sendmessage` 回复文本（https://ele.ac.cn/2171/）。核心前提是每次回复必须带上用户上行消息里的 `context_token`。这就决定了 iLink 接口没法主动群发或单向推送，必须你在微信里先给它发一条，它才能回传（https://ele.ac.cn/2171/）。

第一步，把社区开发者 Kin 整理的这套提示词发给 Grok Bot，让它在云电脑上调研接口并写好转发脚本（https://xput.app/N4rlhi）：

```text
我想把你接到我的微信上，让我能在微信里直接给你发消息、收到你的回复。请按下面的思路做，每做完一步告诉我结果，需要我操作的地方停下来等我。

1、先调研方案：腾讯「微信ClawBot」插件用的是 iLink 接口（ilinkai.weixin.qq.com）。请确认怎么用 getupdates 长轮询收消息、怎么用 sendmessage 回消息。整个程序只走出站请求，不要开公网端口。

2、在 Grok Bot 里建一个由 webhook 触发的 routine，名字可以叫「微信下旨入口」。建好后告诉我去 routine 面板复制 Webhook URL 和 key，然后弹出加密弹框让我填进去，不要让我在聊天里发明文。

3、在你的云端电脑上写一个小转发程序：收到微信消息后 POST 给这个 routine；你处理完以后，用一个 reply 脚本把回复发回微信，同时在我们的主聊天里同步一份。

4、等我在手机微信里启用 ClawBot 插件以后，生成二维码让我用手机扫码确认，同时给我一个可以在微信里直接打开的备用链接。二维码大约 5 分钟有效。

5、绑定成功后，提醒我先在 ClawBot 对话里发一句话，因为回复要用到这条消息带的 context_token。

6、规则：只认绑定的这一个人，别人的消息不处理；回复一律用纯文本，不要用 Markdown，因为微信不渲染 Markdown。

7、最后告诉我：云端电脑重启以后，怎么把转发程序重新拉起来；如果遇到错误码 -14（凭证过期），提醒我重新扫码。
```

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 收到提示词后在云电脑生成转发程序

第二步，配置通信凭据。Grok Bot 建好名为「微信下旨入口」的 Webhook Routine 后，会让你去 Routine 面板复制两样东西：Webhook URL 是消息接收地址，key 是身份凭据（https://xput.app/N4rlhi）。别在普通聊天框里直接发明文密钥。Grok Bot 会弹出一个专属加密输入框，把 URL 和 key 贴进去提交即可（https://xput.app/N4rlhi）。

> [!NOTE]
> 📸 **截图位（待补）**：Routine 面板里的「微信下旨入口」与 Webhook URL、Key
> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 弹出的加密凭据输入框

第三步，在手机微信上绑定。先看版本号：iOS 需在 8.0.70 及以上，Android 需在 8.0.69 及以上（https://xput.app/N4rlhi）。满足后，打开微信点「我」→「设置」→「插件」，找到红色龙虾图标的「微信ClawBot」开启（https://xput.app/N4rlhi）。

> [!NOTE]
> 📸 **截图位（待补）**：手机微信设置里的插件页面找到「微信ClawBot」并开启

开启后回 Grok Bot 发一句「插件开好了」，它会生成一张绑定二维码和备用链接（https://xput.app/N4rlhi）。用微信扫码授权。扫码完成后，必须在微信的 ClawBot 对话框里主动发第一句话（比如「你好」），让 Bot 拿到回信所需的 `context_token`（https://ele.ac.cn/2171/）。ClawBot 回复纯文本，且 Grok Bot 主界面同步显示，就说明连通了（https://xput.app/N4rlhi）。

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 生成的 5 分钟有效绑定二维码与备用链接
> [!NOTE]
> 📸 **截图位（待补）**：手机微信扫码授权确认界面
> [!NOTE]
> 📸 **截图位（待补）**：在手机微信 ClawBot 发送第一条测试消息并收到纯文本回复
> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 主对话界面同步显示微信会话

日常维护里容易遇到几个高频问题，社区整理了一张速查表：

| 故障现象 | 产生原因 | 解决办法 | 来源 |
| --- | --- | --- | --- |
| 接口返回错误码 -14 | 微信端登录凭证或 token 过期 | 无需重装，让 Bot 重新调 `get_bot_qrcode` 生成二维码，手机重新扫码即可 | https://ele.ac.cn/2171/ |
| 扫码提示登录超时或无响应 | 绑定二维码有效期大约仅 5 分钟 | 重新要求 Grok Bot 生成一张全新的二维码并在 5 分钟内扫码确认 | https://xput.app/N4rlhi |
| 微信发消息 Bot 完全不回 | 云电脑因底层维护或休眠重启，中继转发进程中断 | 在 Grok Bot 对话框要求其将云电脑中的传话脚本进程重新拉起 | https://xput.app/N4rlhi |
| 消息有时回、有时完全不回 | 同一个微信号同时绑定了其他 OpenClaw 实例导致消息被抢占 | 排查并解绑其他客户端上的 OpenClaw 实例，保持单实例接入 | https://ele.ac.cn/2171/ |
| 微信端收到的回复排版错乱 | 微信聊天窗口不原生渲染 Markdown 语法 | 在 Bot 的 prompt 规则中强制约束仅输出纯文本，禁用 Markdown 标记 | https://xput.app/N4rlhi |

关于封号风险，社区教程作者 Kin 在推文里称「不会封号，因为用的是微信官方开放的 ClawBot 接口（iLink），属于正常使用」（https://xput.app/N4rlhi）。但要注意：**这是社区教程作者的个人观点，绝非腾讯官方对第三方自动化免责的正式承诺**。虽然 iLink 走官方通道且只发出站请求，但平台随时可能调整风控规则。用个人常用主号高频调用始终有未知风险。如果不希望让 Grok Bot 自己写脚本，社区也有腾讯开源的 `openclaw-weixin` 和第三方封装的 `grok-wechat-plugin` 可以参考（https://ele.ac.cn/2171/）。

> [!TIP]
> 🧪 iLink 转发部署、长时间保活与 -14 重新扫码。

## 11.2 飞书 · Feishu

很多国内团队日常重度依赖飞书。但在 Grok Bot 官方插件市场里，目前找不到飞书连接器（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

没有官方插件时，社区最通用的方案是利用飞书群的「自定义机器人 Webhook」（https://x.com/KinGao476942/status/2100224440948916593）。在群设置里加一个自定义机器人，就能拿到形如 `https://open.feishu.cn/open-apis/bot/v2/hook/...` 的推送地址。在 Grok Bot 里配好日常巡检或分析的 Routine 后，任务最后加一段脚本，把结果用 HTTP POST 推到群 Webhook 即可。

这里有个频控限制要卡住：**飞书目前没有官方插件**，第三方教程称飞书自定义机器人 Webhook 有约每分钟 20 条的频控限制（aitoolku 飞书接入教程，https://www.aitoolku.cn/tutorials/grok-feishu，需以飞书开放平台文档为准）。如果多个 Bot 集中推送日志或轮询过密，容易触发 HTTP 429 限流导致消息丢失。写提示词时要让 Bot 合并推送内容，不要逐行刷屏。

省额度方面，铁柱 AGI 的思路是让脚本负责轮询，有变化才用 webhook 唤醒 Bot，不要让 Bot 自己高频盯消息（铁柱AGI 文章转载，https://readcopilot.ionichina.com/articles/53772）。放到飞书上，就是把飞书当通知出口，而不是让 Bot 监听群里每一条消息。邮件这条路有人这样做：用收信规则过滤掉敏感邮件，再把常用邮箱（含飞书邮箱）转发给 Bot 的 agent mail，让它每天总结提醒（https://x.com/i/status/2106774095820095969）。Kin 也分享过让 Grok Bot 抓取视频、转写文案并存进飞书知识库的用法（https://x.com/KinGao476942/status/2100224440948916593）。

> [!TIP]
> 🧪 飞书 webhook 推送在频率限制下的表现。

## 11.3 公众号、小红书、抖音、视频号：四种数据入口 · No-Plugin Playbook

国内创作者用 Grok Bot 最容易犯的错误，是直接对它说「看下我昨天公众号的阅读量」或「抓下小红书这篇笔记的完播率」。这种指令发过去，Bot 要么胡编，要么一直卡在页面重试（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

原因很简单：微信公众号、小红书、抖音、视频号在 Grok Bot 插件市场里全都没有，而且平台后台不对海外第三方工具开放粉丝画像、完播率或后台阅读量的标准 API（https://xiangyugongzuoliu.com/grokbot-use-cases/）。随手丢一条 `mp.weixin.qq.com/s/xxxx` 公开链接，源码里只有正文和标题，根本没有后台的阅读数、完读率和分享量（https://xiangyugongzuoliu.com/grokbot-use-cases/）。**阅读量与完播率不在公开页面上，国内创作者平台必须依赖四种替代入口**。

面对国内平台，创作者博主翔宇总结出了四种可行的数据接入方式（https://xiangyugongzuoliu.com/grokbot-use-cases/）：

![国内自媒体平台四种数据入口与风险对照表](../../images/fig-11-1.png)

*图：国内自媒体平台四种数据入口与风险对照表*

| 入口类型 | 具体怎么做 | 适合获取的数据 | 严禁与风险项 |
| --- | --- | --- | --- |
| 1. 公开 URL 喂入 | 整理 10-20 条已发公开文章/笔记链接，让 Bot 抓取正文分析文风与结构 | 文章标题、公开发布的正文排版、公开可见的点赞与评论 | 严禁指望它从公开链接猜出后台阅读量与完播率 |
| 2. 导出表格或截图 | 人工登录创作者后台，导出 CSV/Excel 数据表或截取数据看板图片拖入对话框 | 真实阅读量、完播率、用户停留时长、粉丝画像 | 严禁让 Bot 凭空估算；没给表格时必须强制其标注 UNSURE |
| 3. 已登录后台窗口 | 在云电脑的自带浏览器中人工完成扫码登录，让 Bot 控制页面阅读屏幕表格 | 无导出功能的系统后台界面数据、待办工单列表 | 严禁用于高频例行任务；自动化点击极易触发平台验证码与风控封禁 |
| 4. 人工发布与审批 | Bot 仅负责输出选题简报与候选文案草稿，最终审核与发布按钮留在人工端 | 选题策划案、初稿排版、分发版本文案适配 | 严禁让 Bot 自动点击最终发布、回复私信、批量点赞或发起支付 |

处理微信公众号时，可以把历史文章的公开链接汇总给 Bot 分析文风，但别让它替你去创作者后台爬数据（https://xiangyugongzuoliu.com/grokbot-use-cases/）。小红书公开页面能看到点赞和收藏，曝光量和完播率得靠后台截图或表格（https://xiangyugongzuoliu.com/grokbot-use-cases/）。抖音和微信视频号的口播文案可以用转录脚本提取，完播指标同样锁在创作者服务中心里（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

这里最容易踩坑的是平台风控。国内内容平台对海外机房 IP 和无头浏览器非常敏感。如果把后台登录态交给 Bot 并挂高频 Routine 刷页面，云电脑会频繁弹出滑块验证码，账号也容易被判定异常遭封禁。最稳妥的做法始终是：人工导出数据喂给 Bot 诊断，Bot 产出内容后再由人工点击发布（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

> [!TIP]
> 🧪 Bot 解析公众号公开文章链接的效果。

## 11.4 QQ 与网易邮箱 · Domestic Email

国内很多业务通知和账单都在 QQ 邮箱或网易 163 邮箱里。但 Grok Bot 连接器里只有 Gmail 和 Outlook，没有国内邮箱（https://xiangyugongzuoliu.com/grokbot-use-cases/）。**国内邮箱无法直接直连插件，必须通过自动转发、网页版登录或导出文件处理**（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

第一种做法是设置自动转发。在 QQ 邮箱或 163 邮箱设置里建分流规则，把特定发件人或关键词的邮件自动转到绑了插件的 Gmail、Outlook，或者直接转给 Grok Bot 的专属邮箱（https://x.com/i/status/2106774095820095969，https://x.com/i/status/2109320438807670985）。转发前要建好排除规则，过滤掉网银账单、找回密码和验证码邮件。

第二种做法是在云电脑浏览器里开网页版邮箱（比如 `mail.qq.com` 或 `mail.163.com`），手动扫码登录（https://xiangyugongzuoliu.com/grokbot-use-cases/）。在给 Bot 的提示词里严格限制权限：只准读未读邮件标题整理清单，不能删邮件，更不能对外发邮件。

第三种做法是手动导出。附件较多或对账时，在本地把邮件存成 `.eml` 或提取表格，拖到云电脑 `/workspace/` 目录下让 Bot 离线解析。多了一步人工，但不会泄露登录态，也不会误发邮件。

> [!TIP]
> 🧪 163 邮箱转发到 Gmail 后的摘要 Routine。

## 11.5 合规与数据出境 · Compliance

把国内工作流接进 Grok Bot 前，有几道安全底线必须想清楚。

先看网络链路。国内评测媒体提到，`x.ai/bot` 和 `docs.x.ai` 在部分国内网络下能直接打开（https://www.ai345.info/ai-guide/grok-bot-china-guide）。但这不代表数据在境内处理。Grok Bot 的云电脑本质是境外机房虚拟机，走的是海外机房 IP（https://x.com/i/status/2099409639234289914），网络连接稳定性因地区和运营商而异。

再看数据合规。**境外云电脑不属于安全沙箱边界，国内团队调用前必须评估数据出境合规**（https://www.ai345.info/ai-guide/grok-bot-china-guide）。把未公开的客户联系人、内部代码、财务流水或国内系统凭据交给 Grok Bot，数据就实质离开了境内边界。企业使用时要对照《数据安全法》和《个人信息保护法》做风险评估，不能把敏感客户隐私或核心数据库权限直接交给云端 Agent（https://www.ai345.info/ai-guide/grok-bot-china-guide）。

多 Bot 架构也有权限边界风险。官方文档写明，同一个账号下的所有 Bot 共享同一台云电脑，文件目录、浏览器 Cookie 和登录态全量互通（https://docs.x.ai/grok-bot/computer-and-apps）。Bot 之间没有权限隔离。如果一个 Bot 登录了内部系统，另一个有联网权限的 Bot 同样能读取这些 Cookie 和登录态。

在没有原生插件的环境下用 Grok Bot，要守住四条底线：一是绝不让云电脑登录网银、核心财务或高权限管理账号；二是资金支付、发正式邮件、合并代码等敏感操作必须人工二次确认；三是不需要联网的历史数据，清洗脱敏后再以文件交付；四是始终认清云电脑在境外的属性，守住合规底线。

---

[← 上一章：§10 官方合作集成逐个讲 · Partner Integrations](../part3-integrations/10-partners.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§12 群聊与交接 · Groups & Handoffs →](../part4-multi-bot/12-groups.md)

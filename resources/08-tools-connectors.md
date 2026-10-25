# 工具与连接器 · Tools & Connectors

> 整理于 2026-10-25。非官方方案，安全与合规自行评估。

| 标题 | 作者 / 账号 | 日期 | 链接 | 一句话摘要 |
|---|---|---|---|---|
| 连接器分类清单 | 本书附录 D | — | [docs/appendix/A1-appendix.md](../docs/appendix/A1-appendix.md) | 按类别整理的官方连接器 |
| Grok Bot 接入微信从零开始 | 二楼后座 | — | [ele.ac.cn/2171](https://ele.ac.cn/2171/) | 腾讯 iLink + webhook routine 的完整接入方案 |
| 粉皮书：微信实践 02 | 超级峰 AI 课堂 | — | [chaojifeng.me](https://chaojifeng.me/free-courses/grok/learn/wechat-02) | 微信 ClawBot 插件接入步骤 |
| 飞书机器人 webhook 接入 | aitoolku | — | [aitoolku.cn](https://www.aitoolku.cn/tutorials/grok-feishu) | 用飞书自定义机器人 webhook 接 Grok Bot |
| Grok Bot Plugins | learngrokbot.com | — | [learngrokbot.com/plugins](https://learngrokbot.com/plugins) | 插件介绍与用法合集 |
| Awesome Grok Bot Plugins | rdmgator12 | — | [GitHub](https://github.com/rdmgator12/awesome-grok-bot-plugins) | awesome 风格的 Grok Bot 插件清单 |
| 中国用户的集成 | 本书 §11 | — | [docs/part3-integrations/11-china-integrations.md](../docs/part3-integrations/11-china-integrations.md) | 没有插件时微信、飞书、小红书的绕法 |
| 官方合作集成逐个讲 | 本书 §10 | — | [docs/part3-integrations/10-partners.md](../docs/part3-integrations/10-partners.md) | Cursor、Shopify 等合作集成 |
| BDK（`cursor-grokbot-agents`）跨端 Agent 互调工具 | @StarkLJM | 2026-10-12 | [x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411) | 打通本地 Claude Code / Codex / Cursor IDE 与云端 Grok Bot 的双向任务派发与结果回传 |
| `xchat-grokbot-helper`（官方 X Chat 加密私信本地解密工具） | xdevplatform | 2026-10-16 | [github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper) | 配合 X 插件与 4 位 X Chat PIN 码，在云电脑本地执行 `xchat_tool.py` 解密并回复 `@chat` 端到端加密私信 |
| 云电脑安装 Pi Agent（`pi`）挂载外部模型省额度方案 | @hppzyy | 2026-10-17 | [x.com/hppzyy/status/2111573227881529454](https://x.com/hppzyy/status/2111573227881529454) | 在云电脑内配置 `pi` + DeepSeek API 承接大批量文本与代码生成，大幅节省 The X Subscription 周额度 |
| 1Password Brokered Sign-in（逐次授权免密登录连接器） | Cursor 帮助中心 | 2026-10-22 | [cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps) | 需 1Password 8.12.42+，无需共享密码库或配置 Service Account，在手机/电脑端逐次生物识别审批即可安全填表 |
| Grok Bot Vault（内置加密凭据与卡片保险箱） | Cursor 帮助中心 | 2026-10-22 | [cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets) | 内置只写加密保险箱，支持存储账号密码、TOTP 2FA、银行卡（支持手机拍照识卡）与 5MB CSV 批量导入并通过 `BrowserSecureFill` 注入 |
| Tailscale 异地组网打通云电脑与本地家庭/办公内网 | @lyuan1618 | 2026-10-25 | [x.com/lyuan1618/status/2114214704008798674](https://x.com/lyuan1618/status/2114214704008798674) | 在 Grok Bot 云电脑与本地设备间配置 Tailscale 虚拟局域网，实现跨网段私有设备互访 |

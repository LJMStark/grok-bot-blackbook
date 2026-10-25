# 踩坑与故障 · Pitfalls

> 整理于 2026-10-25。🚩 = 风险或疑似营销/诈骗，仅作警示，不作推荐。

| 标题 | 作者 / 账号 | 日期 | 链接 | 一句话摘要 | 来源 |
|---|---|---|---|---|---|
| 群聊里误输密码，所有 Bot 都知道了 | @iankar_ | 2026-10-06 | [x.com/iankar_/status/2107339523038331338](https://x.com/iankar_/status/2107339523038331338) | 群聊内容对所有成员 Bot 可见，别在对话里贴密码 |  |
| 多 Bot 共用电脑被网站封锁 | @Jonsays22 | 2026-09-16 | [x.com/Jonsays22/status/2100351900881207770](https://x.com/Jonsays22/status/2100351900881207770) | 共享电脑被识别为多人同时登录 |  |
| 云电脑 IP 被网站标记 | @mylifcc | 2026-09-14 | [x.com/mylifcc/status/2099517407085899869](https://x.com/mylifcc/status/2099517407085899869) | 官方后来提供"通过你的电脑转发网络流量" |  |
| Grok Bot 泄露银行信息 | Cybernews | — | [cybernews.com](https://cybernews.com/ai-news/grok-bot-leaks-bank-information/) | 财务数据被误发到公司 Slack 公开频道的事故报道 | 媒体 |
| Shane Mac 事故复盘 | RuntimeWire | — | [runtimewire.com](https://runtimewire.com/article/xmtp-shane-mac-grok-bot-bank-audit-slack) | 银行审计数据误发 Slack 事故原报道；本书 §21 有复盘 | 媒体 |
| WhatsApp 接入后账号被封 | r/GrokBot | — | [reddit.com](https://www.reddit.com/r/GrokBot/comments/1w11r70/) | 第三方 Agent 接入 WhatsApp 的封号风险 |  |
| WhatsApp 第三方 Agent 条款 | WhatsApp | — | [whatsapp.com/legal](https://www.whatsapp.com/legal/third-party-agents-terms) | 接入前先读平台条款 | WhatsApp |
| 避坑警告：值得吗？（B站） | B站 UP 主 | — | [bilibili BV1jNbz65ED4](https://www.bilibili.com/video/BV1jNbz65ED4/) | 偏批评的评测（基于早期定价，已过时） |  |
| 🚩 "Bot 自主交易翻 20 倍" | @linda6248130564 | 2026-09-22 | [x.com/linda6248130564/status/2102291280965640690](https://x.com/linda6248130564/status/2102291280965640690) | 典型营销/诈骗话术样本，请勿相信 | 🚩 |
| 常见故障速查 | 本书 §22 | — | [docs/part8-pitfalls/22-troubleshooting.md](../docs/part8-pitfalls/22-troubleshooting.md) | 登录、额度、云电脑、连接器的故障对照表 | 本书 |
| 骗局识别卡 | 本书 §02 | — | [docs/part1-getting-started/02-access.md](../docs/part1-getting-started/02-access.md) | 代充、跨区、假币、营销号搬运识别 | 本书 |
| 非交互式 CLI 调用（如 `pi -p`）未加 `< /dev/null` 导致进程挂起 | @37FlowAI | 2026-10-17 | [x.com/37FlowAI/status/2111334386339823687](https://x.com/37FlowAI/status/2111334386339823687) | Agent Shell 中非交互子进程等待 stdin EOF 会卡死，在命令末尾追加 `< /dev/null` 即可秒回 |  |
| 把默认对话路由直接当重度执行器导致幻觉与反复返工 | @Khazix0918 | 2026-10-18 | [x.com/Khazix0918/status/2111709708226797737](https://x.com/Khazix0918/status/2111709708226797737) | 裸聊轻量路由模型容易不查证直接回复；重度检索与编码应通过 Skill 委派给 Cloud Agent 或云电脑 CLI |  |
| 云电脑机房 IP 被目标网站拦截或频繁弹验证码 | @XueshiQiao | 2026-10-21 | [x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589) | 需在桌面端开启 `Settings > Computer > Your computer > Route traffic through this computer` 走本地住宅 IP |  |
| Vault 保存银行卡后结账自动填充，无单笔 Vault 二次弹窗开关 | @JianWeiSignal / @kial | 2026-10-25 | [x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488) | 存入 Vault 的卡片在结账表单会自动注入（另见 `@kial` `x.com/kial/status/2114201768414646280`）；需每单手输确认请勿将卡留在 Vault |  |
| The X Subscription 三端共用周额度池被高频空转 Routine 偷跑耗尽 | @charlie_pmp | 2026-10-25 | [x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131) | 统一订阅下 Grok Bot、Grok App 与 Cursor 共用周额度池，冗余定时 Routine 会快速抽干三端可用配额 |  |

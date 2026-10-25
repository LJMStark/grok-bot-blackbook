# 《Grok Bot 黑皮书：从零到一支 AI 团队》

[📖 返回目录](../../README.md#-目录) ｜ [下一章：§01 Grok Bot 是什么 · What It Is →](../part1-getting-started/01-what-it-is.md)

---

> 每一步都有出处，每一个坑都有人踩过。

## 封面规格块 Cover Spec

| 项目 | 内容 |
|---|---|
| 版次 | v261025（2026-10-25，基于初版 v261012 全面扩容至官方 v0.75.5） |
| 书名 | 《Grok Bot 黑皮书：从零到一支 AI 团队》 |
| 副标题 | 每一步都有出处，每一个坑都有人踩过 |
| 英文副标题 | *From Zero to an AI Team — Every Step Sourced, Every Pitfall Tested* |
| 适用版本 | Grok Bot 桌面版（macOS / Windows / Linux，覆盖至 v0.75.5）、iOS（v1.16+）、Android；Opus 5.5 路由后（[来源](https://x.com/elonmusk/status/2107724314451878104)） |
| 本版新增 | 初版涵盖 Bot 自有邮箱（10/10）、Shopify 连接（10/09）、X 原生搜索与监控（10/08）、Team Bots（9/29）等全部已发布功能（[来源](https://x.ai/news/team-bots)）；**2026-10-25 版重磅增补（10/13–10/25）**：全面覆盖官方 [v0.71.2、v0.75.2 至 v0.75.5 更新日志](https://x.ai/changelog/bot)与五大内部 Release Feed 特性——① **The X Subscription 三合一统一订阅**（10/18，整合 Grok、Cursor 与 X Premium，共享周额度池与 Prepaid Credits 预付机制，[官方说明](https://cursor.com/help/the-x-subscription/overview)）、② **iPhone Action Button 侧边键一键语音通话**（10/19，iOS v1.16+ 与 Shortcuts 动作及原生日历/提醒事项/通讯录直连，[官方说明](https://cursor.com/help/grok-bot/voice-chat)）、③ **Pages（Canvas）实时交互看板与报告**（10/21，支持 `Only you` / `Your team` / `Anyone with the link` 三级权限分享，[官方公告](https://x.com/bot/status/2112991843235610885)）、④ **1Password Brokered Sign-in 逐次授权免密登录**（10/22，配合 1Password 8.12.42+ 免共享库直接注入凭据，[官方说明](https://cursor.com/help/grok-bot/connect-apps)）、⑤ **Grok Bot Vault 内置加密保险箱**（10/22–10/23，支持保存登录凭据、银行卡、收货地址、手机扫卡与 5 MB CSV 批量导入，[官方说明](https://cursor.com/help/grok-bot/secrets)），并同步纳入 **Grok Imagine 生视频与代码动效渲染**（10/14，[官方公告](https://x.com/bot/status/2110566041772617908)）、**专属邮箱 `+alias` 加号别名触发 Routine**（10/14，[官方说明](https://cursor.com/help/grok-bot/agent-email)）、**X Chat 端到端加密私信管理**（10/16，基于 [xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper)）以及 **BDK（`cursor-grokbot-agents`）本地与云端双向调用实战** |
| 信息源声明 | 见下方 |
| 作者 | Mr.鼓先生（`StarkLJM`） |
| 渠道 | X（Twitter）：[@StarkLJM](https://x.com/StarkLJM) ｜ 微信（WeChat）：`StarkLJM` ｜ GitHub 开源仓库：[github.com/LJMStark/grok-bot-blackbook](https://github.com/LJMStark/grok-bot-blackbook) |

> 信息源声明：本书事实来自以下渠道，每条附原始链接。cursor.com/docs/grok-bot 官方技术文档 22 页（[来源](https://cursor.com/docs/grok-bot)）、cursor.com/help/grok-bot 官方帮助中心（[来源](https://cursor.com/help/grok-bot)）与 cursor.com/cn/help 中文帮助页（[来源](https://cursor.com/cn/help/grok-bot/plans)）、x.ai/news 官方公告 16 篇（[来源](https://x.ai/news)）、x.ai/bot/guides 官方岗位指南 27 篇（[来源](https://x.ai/bot/guides)）、@bot 官方 X 账号发布时间线（[来源](https://x.com/bot)）、X 平台检索 2,390 条初版去重帖（其中 2,058 条相关、630 条中文相关）及 10 月中下旬新增核验的 70+ 条中英文高赞实战长帖、中文主流技术与内容平台（公众号、CSDN、掘金、V2EX、LINUX DO、即刻、NodeSeek、知乎、小红书、B站、36氪等媒体）合计约 700 条相关内容、官方 changelog 截至 v0.75.5 的历次版本更新记录（[来源](https://x.ai/changelog/bot)）、YouTube / 中文视频笔记 26 条。初版数据截止日期：2026-10-12；最新增量更新截止日期：2026-10-25。

> 时效提醒：Grok Bot 迭代极快——从 8 月 11 日发布到初版截稿，官方 changelog 已有 49 个版本，而在 10 月 14 日至 10 月 23 日短短十天内又连续推送了 v0.71.2、v0.75.2 与 v0.75.5 三个重大版本（[来源](https://x.ai/changelog/bot)）。此外，旧版文档域名已全面下线并迁移整合至官方技术文档中心 [cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot) 与官方帮助中心 [cursor.com/help/grok-bot](https://cursor.com/help/grok-bot)。书中任何一条信息都可能在你读到的时候已经变了，请结合 [cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)、[cursor.com/help/grok-bot](https://cursor.com/help/grok-bot) 和 [@bot](https://x.com/bot) 官方账号的最新发布做验证。

> 持续更新：本书的最新版本见 [https://github.com/LJMStark/grok-bot-blackbook](https://github.com/LJMStark/grok-bot-blackbook)。

> 勘误入口：如果你发现事实错误、过时信息、或者缺少来源标注的地方，请到 [https://github.com/LJMStark/grok-bot-blackbook/issues](https://github.com/LJMStark/grok-bot-blackbook/issues) 提交，或通过 X（[@StarkLJM](https://x.com/StarkLJM)）与微信（`StarkLJM`）直接联系作者。我会在每次更新时公开勘误记录——已经犯过的错，也是出处的一部分。

![黑底封面（黑皮 + 橙色强调条，致敬但区分于花叔橙皮书系列的白底橙标风格）](../../images/cover.png)

*图：黑底封面（黑皮 + 橙色强调条，致敬但区分于花叔橙皮书系列的白底橙标风格）*

## 致读者 Preface

### 为什么还要再写一本

你手上可能已经有别的 Grok Bot 指南了。

KinGao 的《橙皮书》在 8 月 23 日上线，14 章加 4 张速查表，GitHub 159 星，里面总结的"大脑倾倒"和"反向配置"在社区里传得很开（[来源](https://github.com/KinGao294/grok-bot-orange-book)）。超级峰的《粉皮书》更厚，55 个单元全文免费公开，微信接入写了 3 课（[来源](https://chaojifeng.me/free-courses/grok)）。还有黄叔的《蓝皮书 v0.1》，一句话就能建一个 QQ 邮箱 Bot（[来源](https://ai.lzw.me/best-blogs/article/9b80b0ebd1)）。

我把它们翻了一遍，发现三个问题。

先说时效。橙皮书停在 8 月 24 日，粉皮书核对到 9 月 25 日（[来源](https://chaojifeng.me/free-courses/grok)）。从那之后，Grok Bot 陆续上线了 Team Bots、Cursor 编程交接、X 原生搜索与监控、Shopify 连接、Bot 自有邮箱、Finance 连接器、1Password 集成，以及 Opus 5.5 模型路由。马斯克 10 月 7 日在 X 上说："Going forward, @SpaceX will use the best back end model for any given task, including Claude Opus 5.5, MidJourney, Suno and other leading APIs"（[来源](https://x.com/elonmusk/status/2107724314451878104)），Grok Bot 团队成员 @poteto 在回复里补了一句 "yes, bot itself will run on opus 5.5"（[来源](https://x.com/poteto/status/2107734770990133319)）（注意：截至 10/12 仍有用户反馈自己的 Bot 尚未切到 Opus，属于逐步推送）。早期传的"只跑 Grok 自家模型"已经过时。橙皮书写的"Cursor Pro $20 暂不含 Grok Bot"也和现行政策冲突——官方帮助页写得很清楚，Cursor 所有付费个人计划和 Teams 现在都包含 Grok Bot（[来源](https://cursor.com/cn/help/grok-bot/plans)）。

而进入 2026 年 10 月中下旬（10/13 至 10/25），Grok Bot 的产品形态与计费规则又经历了一次脱胎换骨的跃迁：
1. **三合一统一订阅体系（The X Subscription）落地**：2026 年 10 月 13 日至 18 日，官方正式推出 [The X Subscription](https://cursor.com/help/the-x-subscription/overview)（[@bot 公告](https://x.com/bot/status/2110063783796572496)），将 Grok、Cursor 与 X Premium 整合进同一套账单——其中 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 档位包含 Grok Bot（Free $0 与 Plus $8/月不含），三端共享同一个每周重置的周额度池（one weekly usage pool），超额用量与第三方模型调用则改走 `grok.com/dashboard/billing` 下的 **Prepaid Credits（预付额度）**（[官方档位说明](https://cursor.com/help/grok-bot/plans)）。既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）与 Teams（$40/人/月）老订户虽可保留原计划，但一旦在 `cursor.com/unify` 主动切换至 The X Subscription 即为单向不可逆操作（[官方计划页](https://cursor.com/cn/help/grok-bot/plans)）。
2. **从“打字派活”到“物理按键语音 + 实时交互看板”**：官方在 [v0.71.2（10/14）](https://x.ai/changelog/bot) 接入 Grok Imagine 原生生图生视频与代码动效渲染（[@bot 公告](https://x.com/bot/status/2110566041772617908)），并为 `@mail.grokbot.com` 专属邮箱增加 `+alias` 加号子别名定向触发 Routine 能力（[官方邮件说明](https://cursor.com/help/grok-bot/agent-email)）；紧接着在 10 月 19 日支持 **iPhone Action Button（操作按钮）一键实时语音通话**（需 iOS v1.16+，[@bot 公告](https://x.com/bot/status/2112246033178968161)，[官方语音指南](https://cursor.com/help/grok-bot/voice-chat)）；随后在 [v0.75.2（10/22）](https://x.ai/changelog/bot) 推出 **Pages（Canvas）实时交互报表与看板**（[@bot 公告](https://x.com/bot/status/2112991843235610885)）、iOS 原生日历/提醒事项/通讯录直读，并将 Routine 运行上限大幅提升至**全账号 300 次/小时、单条 Routine 200 次/小时**（[官方 Routine 文档](https://cursor.com/help/grok-bot/routines)）。
3. **凭据与支付安全的双重基建（1Password Brokered Sign-in + Grok Bot Vault）**：10 月 22 日至 23 日（[v0.75.2 与 v0.75.5](https://x.ai/changelog/bot)），官方一方面联合 1Password 推出免共享密码库、逐次生物识别审批的 **1Password Brokered Sign-in**（[@bot 公告](https://x.com/bot/status/2113301060811161874)，[官方连接器文档](https://cursor.com/help/grok-bot/connect-apps)）；另一方面正式上线内置只写加密保险箱 **Grok Bot Vault**（[@bot 公告](https://x.com/bot/status/2113754107861532677)，[官方 Vault 文档](https://cursor.com/help/grok-bot/secrets)），并由 Elon Musk 公开承诺 SpaceX 对代购差错或卡信息泄露兜底全额赔付（[@elonmusk 原帖](https://x.com/elonmusk/status/2110610960474079445)）。

再说出处。橙皮书几乎没引用 cursor.com/docs/grok-bot 的页面（[来源](https://github.com/KinGao294/grok-bot-orange-book)）。粉皮书带了一部分官方链接，但不少关键结论没写来源。分不清是官方说的还是博主猜的，就不知道哪天会失效。尤其在 10 月中下旬旧版文档域名彻底下线（返回 404）、全面迁移至官方技术文档中心 [cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot) 与官方帮助中心 [cursor.com/help/grok-bot](https://cursor.com/help/grok-bot) 之后，大量早期教程里的链接已经失效，更需要一本逐条核验最新官方路径的案头手册。

最后是国内路径。橙皮书没讲支付宝怎么付、手机号怎么验、国内平台没有插件怎么处理。粉皮书微信接入写得扎实，但支付宝订阅、代充风险和合规问题全是空白。

所以我决定自己写一本。不是前面的书不好，橙皮书"第一个任务"那一章写得很透。我想做的是另一件事：**每条事实都能点进原始链接**，分清官方、社区和推测，再留一页公开勘误。

花叔写《Claude Code 橙皮书》时在封面放了信息源声明，提醒读者结合官方文档验证（[来源](https://github.com/alchaincyf/claude-code-orange-book)）；《Hermes Agent 2.0》在 README 顶部开辟勘误节，认错并贴官方 FAQ 链接（[来源](https://github.com/alchaincyf/hermes-agent-orange-book)）。黑皮书把这件事做到底：原始链接、全书勘误页。哪句话写错了，你能随时查到我错在哪。

### 这本书怎么做的

全书做了三轮调研，并在 2026 年 10 月 25 日完成了覆盖至 v0.75.5 的第四轮专项深潜。

第一轮梳理官方文档。通过 [llms.txt](https://cursor.com/docs/grok-bot) 索引抓取了 cursor.com/docs/grok-bot 全部 22 个文档页面，加上 x.ai/bot/guides 的 27 篇官方岗位指南、x.ai/news 的 16 篇公告、@bot 官方账号的 19 条 X 发布，以及官方 changelog 的 49 个版本记录（[来源](https://cursor.com/docs/grok-bot)）。

第二轮扫 X 平台。跑了 88 次检索和 3 次按 ID 抓取全文，拿到 2,075 条去重帖子。经过主题分类和人工复核，筛出 1,846 条相关帖，其中 293 条长帖拉了全文。话题分布里：定价与额度 341 条、官方发布 260 条、Routine 与 Skill 210 条、连接器与插件 209 条、吐槽与对比 205 条、邮件与日历 180 条。光定价额度就占了快五分之一，大家对收费规则确实困惑（[来源](https://x.com)）。另外补了 YouTube 和英文社区资料，包含 15 条视频转录摘要、Galaxy 大会 10 个官方场次笔记、事故报告与竞品对比等约 50 篇网页。

第三轮覆盖中文平台。X 上的中文相关帖扩充到 630 条。中文平台里，搜狗微信搜到 258 条结果、靠转载站补了 6 篇全文；CSDN 抓了 287 篇（113 篇标记为疑似搬运）；掘金 27 篇；V2EX 40 个主题（17 个含完整回复）；LINUX DO 18 个主题；即刻 5 篇；NodeSeek 2 帖；知乎 2 篇专栏。小红书等短视频与图文平台受登录墙限制只有间接信息；B站接口和页面返回 412，没拿到正文（[来源](https://x.com)）。

三轮汇总下来：X 平台 2,390 条去重帖（2,058 条相关，其中中文 630 条），中文各大主流社区与媒体平台约 700 条相关内容。

第四轮（2026-10-13 至 2026-10-25 增量核验）则全面追踪了官方 [cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot) 与 [cursor.com/help/grok-bot](https://cursor.com/help/grok-bot) 的文档架构重组、5 项内部 Release Feed 核心发布、[v0.71.2 / v0.75.2 / v0.75.5 官方更新日志](https://x.ai/changelog/bot)，以及 X 平台中英文社区在最新两周内涌现的 70 余个高赞实战工作流。

在这轮调研中，中英文社区的头部创作者不约而同地印证了本书提倡的“多智能体分工 + Skill 防腐 + 跨端协同”方法论：
- 在英文社区，知名研究者 Miles Deutscher（`@milesdeutscher`）于 2026 年 10 月 23 日发布了斩获 **3,100 赞、360 转发、4,503 书签** 的万字长推《10 大逆天 Grok Bot 用例（10 Insane Grok Bot Use Cases）》（[来源](https://x.com/milesdeutscher/status/2113653680834859262)），一口气拆解了从个人 X 运营副驾（[#10](https://x.com/milesdeutscher/status/2113653710631166414)）、竞品全天候监控雷达（[#9](https://x.com/milesdeutscher/status/2113653726217195817)）、替代昂贵 Apollo 订阅的潜在客户挖掘机（[#8](https://x.com/milesdeutscher/status/2113653741647999378)）、跨 WhatsApp/Discord/Slack/Telegram 的群聊总管（[#7](https://x.com/milesdeutscher/status/2113653756990816446)）、自动谈判降价与退订的账单审计员（[#6](https://x.com/milesdeutscher/status/2113653772337770849)）、一鱼多吃跨平台内容改写器（[#5](https://x.com/milesdeutscher/status/2113653788196430242)）、全渠道晨会简报（[#4](https://x.com/milesdeutscher/status/2113653803304296498)），到 **1 个主控编排 Bot 统领 10+ 专职 Bot 的蜂群架构（Grok Swarms，[#3](https://x.com/milesdeutscher/status/2113653818651189419)）**、云电脑全栈 Vibe-Coding 造物主（[#2](https://x.com/milesdeutscher/status/2113653833645818000)）以及零手动标签的第二大脑（[#1](https://x.com/milesdeutscher/status/2113653848581816595)）。
- 在中文社区，一泽 Eze（`@eze_is_1`）于 2026 年 10 月 13 日撰写的 **10 条高含金量 Grok Bot 实战心得**（收获 **351 赞、62 转发、705 书签**，[主帖](https://x.com/eze_is_1/status/2109850538045264151)及进阶跟帖 [1](https://x.com/eze_is_1/status/2109852993982206425)、[2](https://x.com/eze_is_1/status/2110532874000879886)、[3](https://x.com/eze_is_1/status/2110866224892850547)，被 `@lanvjian` [力荐](https://x.com/lanvjian/status/2111085984855011349)为新手必看定位指南），系统厘清了云端 Grok Bot 与本地 Claude Code / Codex 的分工边界、长耗时任务的唤醒防断连机制（`wake on done` 与 Webhook 协同），以及极为关键的**“自迭代 Skill 防臃肿法则”**——当允许 Bot 在复盘中自动修改 Skill 文件时，必须定期清理冗余与冲突规则。你可以直接在自己的主控 Bot 中配置如下这套受控的 Skill 维护与任务路由规范：

```markdown
# Grok Bot 编排中枢与 Skill 自迭代防臃肿规范（融合 @eze_is_1 与 @milesdeutscher 实战范式）
1. 角色边界与重活委派（Orchestrator vs. Worker）：
   - 对话层仅负责收集上下文、对齐验收标准（Acceptance Criteria）与任务拆解。
   - 凡涉及超长代码库重构或耗时 >3 分钟的构建任务，严禁在对话层裸写，必须委派给 Cursor Cloud Agent、云电脑内的 CLI Worker 或通过 BDK 交接，并配置完成时 Webhook 唤醒（零轮询耗电）。
2. 自迭代 Skill 防膨胀审计（Anti-Bloat Rule）：
   - 每次复盘更新 SKILL.md 时，单文件总行数严禁超过 150 行。
   - 新增一条经验规则前，必须先检查是否与既有规则重复或冲突；优先合并同类项、删除已验证失效的临时补丁，保持 SOP 正交精简。
3. 信息沉淀与看板同步：
   - 专项产出统一写入共享知识库目录，并同步热更新至 Chief of Staff 维护的 Activity Dashboard Page。
```

整个过程用 AI 辅助跑了搜索、抓取和归类，书里引用的事实都尽量回溯到原始链接；2026-10-13 与 2026-10-25 又先后做了两轮逐章事实审计（见勘误记录），仍可能有遗漏。原始文件里标记"未核实"或"需核实"的，要么找到可靠信源补全，要么直接不写。**研究文件里没有的数字、日期、价格，一律不编。**

工具书不是小说。有人说花叔的橙皮书系列是"三小时写就的 AI 泔水"（[来源](https://x.com/realchendahuang/status/2108754825181859970)），也有人统计微信读书上"十本书里只有四本推荐超过非推荐"（[来源](https://x.com/Jack_FluxAI/status/2108809412614009056)）。我不卷入这种争论。我能做的是把方法、数据和勘误全摆出来。哪怕你觉得某页没写好，至少能查到那页的信息是从哪来的。

### 怎么读这本书

这本书不用从头读到尾，**你的情况不同，读法也不同**。

刚听说 Grok Bot、还没用过：从 §01（Grok Bot 是什么）顺着读到 §04（你的第一个任务）。读完能独立跑通任务，也搞懂底层架构。重点看 §02（怎么才能用上），里面讲了 The X Subscription 三合一订阅（$30/$100/$200）、支付宝订阅、手机号验证和网络解法，这是国内最常卡住的地方。

已经在用、想用得更顺：直接翻 §05（Bot）和 §07（Skill 与 Routine），把单次任务固化成自动运行的流程（含 `+alias` 邮箱别名触发与 300 次/小时最新配额）。接着看 §08（审批与安全边界，含 1Password Brokered Sign-in 与 Vault 绑卡结账无二次弹窗的关键风控边界）和 §19-§20（额度与省钱，含三合一共享周额度池与 BDK 跨端协作），额度烧太快和安全隐患是用一阵后最常踩的坑。

给团队或公司落地：先看 §12-§13（群聊、Pages 实时交互看板、交接、编制案例），接着看 §09-§11（连接器、官方集成、国内无插件方案），最后看 §17-§18 两个完整落地项目。附录 A（官方硬数字速查）和附录 B（档位与价格表）适合备查。

![三条阅读路线图（小白路线 §01→§04、进阶路线 §05→§08→§19、团队路线 §12→§13→§09→§17，用箭头标出推荐顺序）](../../images/fig-00-3.png)

*图：三条阅读路线图（小白路线 §01→§04、进阶路线 §05→§08→§19、团队路线 §12→§13→§09→§17，用箭头标出推荐顺序）*

!["研究漏斗"信息图（2,390 条 X 帖 → 2,058 条相关 → 630 条中文；中文 12 平台 ~700 条 → 本书引用）](../../images/fig-00-4.png)

*图："研究漏斗"信息图（2,390 条 X 帖 → 2,058 条相关 → 630 条中文；中文 12 平台 ~700 条 → 本书引用）*

### 一句冷静提醒

在建一堆 Bot、排几十条 Routine 之前，先看一句话。

Nate B Jones 在视频里提过：人们常常把流程本身当成了创造出来的价值——"people mistook process for value created"（[来源](https://www.youtube.com/watch?v=LM7Ft7g8qJw)）。

设想一种很常见的情况：有人设了每天早上 8 点的晨报 Routine，Bot 准时发来竞品动态摘要，但他其实从没根据这份摘要做过任何业务决定。除了白耗额度、让自己觉得"有套自动化系统"，它没有实际意义。

社区里有人写过淘汰 Routine 的审计提示词：列出所有跑过的 Routine，统计真正被采纳的产出，标出静默失败和长期被忽略的任务，强制挑出一个必须删掉的并写明原因（[来源](https://x.com/kocer_eth/status/2101669438038634827)）。Lauren Tan 团队内部甚至做了一个叫 "Dr. Eggbot" 的 Bot，专门定期核算其他 Bot 和 Routine 的开销（[来源](https://www.youtube.com/watch?v=xZ5TEaleUdg)）。

这不是泼冷水。Grok Bot 确实能干实事。Bloomberg 引用的数据显示，9 月 14 日那周周活达到 418,000，周环比增 24%（[来源](https://www.livemint.com/ai/elon-musk-s-grok-bot-hits-418-000-weekly-users-after-one-month-11790093107144.html)）。而到了 2026 年 10 月下旬，据 `@wenser2010`（Wenser）于 10 月 23 日披露的行业追踪数据，Grok Bot 自 8 月上线以来仅用两个月时间就突破了 **80 万周付费用户（800K weekly paid users）**（[来源](https://x.com/wenser2010/status/2113683422409572523)）；横向对比当前三大头部大厂智能体产品——OpenAI Dots 起步门槛高达 $100/月（需 Pro 订阅）、Meta Muse 虽免费却受限于美国地区与 Meta 账号准入墙，而 Grok Bot 依托 **$30/月** 的 The X Subscription 将 Grok Bot、X Premium 与 Cursor 打包进同一套生态，形成了极强的性价比与商业闭环优势（[来源](https://x.com/wenser2010/status/2113683427069489614)）。

与此同时，在官方公布的客服自动化标杆案例中，2026 年 8 月 14 日 Cursor 并入 SpaceX SuperIntelligence（SpaceXSI）后客服工单瞬间暴涨 175%，官方通过部署 5 位专职 Bot 组成的协作舰队，在**零新增客服招聘（节省约 200 人力）**的前提下，将单票成本降至 **$0.20–$0.30**（远低于行业平均的 $1.00–$4.00），99% 的退款无需人工介入，甚至在一次重大事故中仅靠一名工程师审核一张批量审批卡就在 10 分钟内清零了 204 张故障工单，并每日自动提炼 20,000+ 条产品反馈点（[来源](https://x.ai/news/grok-bot-customer-support)）。采购用例 Haggle Bot 把一笔 $14,629 的采购砍到 $6,143，降了 58%（[来源](https://x.ai/news/grok-bot-procurement)）。其中周活与周付费用户数据来自媒体与行业分析转述，客服和采购数字是官方自家案例（[来源](https://x.ai/news/grok-bot-customer-support)）——都是对外公布的数字，但未经第三方审计。

但对个人来说，跑通 Routine 不等于产生价值。尤其在升级到三合一 [The X Subscription](https://cursor.com/help/the-x-subscription/overview) 之后，Grok Bot、Grok 与 Cursor 共享同一个周额度池，正如社区用户 `@charlie_pmp` 所提醒的，后台高频空转的冗余 Routine 往往是静默抽干你每周额度的头号元凶（[来源](https://x.com/charlie_pmp/status/2114214503416271131)）。衡量它的标准很简单：它有没有帮你改变决策，或者省下你必须亲手花的时间。读完这本书后，不妨每个月问自己一句：

**这条 Routine 改变过哪个决策？**

如果答案是没有，就把它关掉。额度要花钱，注意力也一样。

---

### 怎么找到作者

本书由 **Mr.鼓先生**（`StarkLJM`）持续维护与更新。如果你在搭建多 Bot 团队、编写 Agent Skills、配置 BDK（`cursor-grokbot-agents`）跨端工作流，或者核对本书勘误时有任何心得与疑问，欢迎通过以下唯一核实渠道交流：

- **X（Twitter）**：[@StarkLJM](https://x.com/StarkLJM)
- **微信（WeChat）**：`StarkLJM`
- **GitHub 开源仓库与勘误提交**：[https://github.com/LJMStark/grok-bot-blackbook](https://github.com/LJMStark/grok-bot-blackbook)

---

[📖 返回目录](../../README.md#-目录) ｜ [下一章：§01 Grok Bot 是什么 · What It Is →](../part1-getting-started/01-what-it-is.md)

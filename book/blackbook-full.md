# 《Grok Bot 黑皮书：从零到一支 AI 团队》

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

![黑底封面（黑皮 + 橙色强调条，致敬但区分于花叔橙皮书系列的白底橙标风格）](../images/cover.png)

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

![三条阅读路线图（小白路线 §01→§04、进阶路线 §05→§08→§19、团队路线 §12→§13→§09→§17，用箭头标出推荐顺序）](../images/fig-00-3.png)

*图：三条阅读路线图（小白路线 §01→§04、进阶路线 §05→§08→§19、团队路线 §12→§13→§09→§17，用箭头标出推荐顺序）*

!["研究漏斗"信息图（2,390 条 X 帖 → 2,058 条相关 → 630 条中文；中文 12 平台 ~700 条 → 本书引用）](../images/fig-00-4.png)

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


# §01 Grok Bot 是什么 · What It Is

## 1.1 一句话讲清 Grok、Grok Bot、Cursor 的关系 · Grok vs Grok Bot

很多人第一次听说 Grok Bot，以为它是把 Grok 聊天机器人套了个壳。其实不是。

Grok 是 SpaceXSI（前 xAI）的大语言模型。你向它提问，它吐出一段文字。Grok Bot 是搭在模型上层的 Agent 应用——你不是找它聊天，是在给它派活。官方原话写得明白："Grok Bot gives you Bots you can keep around: AI teammates with names, jobs, and context that compounds over time"（[cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)）。社区里一条 215 赞的帖子概括得很透彻：Grok 负责调研、比对、理清思路，再把指令下发给 Grok Bot；Grok Bot 负责切进 App、改数据、发消息、把事情收尾（[X 帖](https://x.com/i/status/2106883332432945519)）。一句话：**Grok 负责想，Bot 负责做**。

再说 Cursor。2026 年 2 月 xAI 并入 SpaceX（[x.ai/news/xai-joins-spacex](https://x.ai/news/xai-joins-spacex)），8 月 14 日 AI 编程工具 Cursor 也成为 SpaceXSI 的一部分——官方客服案例原文是 "When Cursor became part of SpaceXSI on August 14"（[x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）。Grok Bot 与 Cursor 共用一套账号和订阅——所有 Cursor 付费个人版和 Teams 计划都直接带 Grok Bot 权限（[cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)）。Cursor 的云端代理（Cloud Agent / Cursor Projects）也能在 Grok Bot 内部直接调用，这块我留在 §10 展开。

到了 2026 年 10 月中旬，这三者的绑定进入了完全体阶段。官方在 10 月 13 日至 10 月 18 日期间正式推出 **The X Subscription 三合一统一订阅**（[@bot 官方公告](https://x.com/bot/status/2110063783796572496)，获 3,039 赞、272 转发、540 书签；详见官方帮助中心 [cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview) 与 [cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。在这套顶层设计下，**Grok**、**Cursor**、**X Premium** 与 **Grok Bot** 被彻底融合成单一订阅计划，不再需要繁琐的跨平台账号手动关联：

- **三合一档位与准入边界**：The X Subscription 分为 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 三档，全部原生包含 Grok Bot 权限；而免费的 **Free（$0）** 与入门级 **Plus（$8/月）** 档位不包含 Grok Bot（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。
- **三端共享周额度池与 Prepaid Credits 预付机制**：在 The X Subscription 体系下，Grok Bot、Grok 与 Cursor 三端共用同一个**周额度池（one weekly usage pool）**，每周固定重置且不结转。当周额度耗尽或调用非 Grok 系列的第三方模型时，系统不再走后付费账单，而是直接从用户在 `grok.com/dashboard/billing` 充值的 **Prepaid Credits（预付额度）** 中扣减，支持配置自动充值（Auto Top-up）与月度额外消费封顶上限（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。
- **老订户保留与 `cursor.com/unify` 单向不可逆切换规则**：既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及自助式 Teams（$40/人/月）老订户只要不主动迁移，仍可保留原有独立档位与后付费按需限额（On-demand monthly limit），也能继续通过 `Settings > Usage & Billing > Manage Plan > Get Access with Grok` 关联个人 SuperGrok 或 X Premium+ 账号（多账号额度不叠加，自动取较高一档生效，详见 [cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）。但请注意：**一旦通过 `cursor.com/unify` 或 `accounts.x.ai/unify` 主动合并升级至 The X Subscription，该切换为单向不可逆操作，无法退回旧版独立订阅计划**；同时若此前通过 Apple App Store 或 Google Play 订阅了旧计划，必须在手机端应用商店手动取消，以防双份扣费（[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。

这三者连起来是一条链条：Grok（模型层）→ Grok Bot（Agent 层）→ Cursor（编码层）。你可以单用 Grok Bot 不碰代码，也可以让 Bot 把编程任务自动分发给 Cursor 的云端 Agent。普通用户面对的入口只有一个：Grok Bot 的桌面端或手机端。

很多刚上手的开发者还会困惑：既然有了 Grok Bot，它和本地终端里的 Claude Code、Codex 到底是什么关系？中文社区创作者一泽Eze（`@eze_is_1`）在一条收获 351 赞、62 转发、705 书签的万字长推中给出了极清晰的架构对比框架（[@eze_is_1 原帖](https://x.com/eze_is_1/status/2109850538045264151)），博主蓝海（`@lanvjian`）也将其力荐为分不清 Grok Bot 与 Codex 的新手必看定位指南（[@lanvjian 推荐帖](https://x.com/lanvjian/status/2111085984855011349)）：

- **本地 Claude Code / Codex 是“深度编码特种兵”**：扎根在你的本地主力开发机或大型代码仓库里，适合需要高频读写本地文件、跑重度编译测试、精雕细琢复杂工程架构的沉浸式编程任务。
- **Grok Bot 是“7×24 小时在线的云端全能总管与连接器中枢”**：它常驻云端沙箱，自带持久化浏览器、专属邮箱、原生免费 X 生态检索以及覆盖日历、飞书/Slack、1Password、Vault 的全套外部连接器，并能通过 BDK（Bot Developer Kit）与本地 CLI 双向互调（如 `@StarkLJM` 实测的跨端派单工作流 [X 帖](https://x.com/starkljm/status/2109544938644107411) 与 `@z_lumia` 的三合一订阅双向互调实践 [X 帖](https://x.com/z_lumia/status/2113800469571313974)）。换言之，Grok Bot 负责全天候盯哨、跨平台信息调度、多智能体编排与生活/运营自动化，而把重度代码攻坚委派给 Cursor Cloud Agents 或本地编码 CLI。

![Grok · Grok Bot · Cursor 三者关系图（模型→Agent→编码）](../images/fig-01-1.png)

*图：Grok · Grok Bot · Cursor 三者关系图（模型→Agent→编码）*

2026 年 10 月 7 日，马斯克在 X 上公布了一个新动向：Grok Bot 不再只调用自家的 Grok，而是按任务分工路由到 Claude Opus 5.5、Midjourney、Suno 这些外部模型（[马斯克 X 帖](https://x.com/elonmusk/status/2107724314451878104)；[TNW 报道](https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk)）。Grok Bot 团队成员 @poteto 随后在回复里说："yes, bot itself will run on opus 5.5"，并称 Opus 5.5 "is rolling out right now"（[X 帖](https://x.com/poteto/status/2107734770990133319)）。也就是说，用户不必费心挑模型，Bot 会替你选后端；但这是逐步推送，截至 10/12 仍有用户说自己没感觉到切换（[X 帖](https://x.com/GodlyAlphaM/status/2108885285941698990)），官方 x.ai/news 也还没有专文。虽然没给手动切换的开关，但省心之处在于，你用不着关心各家模型的参数差异。

## 1.2 一台云电脑 + 一群同事 · The Cloud Computer Model

理解 Grok Bot 最省事的方式，就是把它看作你在云端长期开着的一台电脑，上面围坐着一群同事。

每个 Bot 都跑在一台持久化的云电脑里，自带浏览器、文件系统和终端（[cursor.com/help/grok-bot/computer-and-apps](https://cursor.com/help/grok-bot/computer-and-apps)）。你合上笔记本电脑、锁屏甚至直接关机，它依然在云端干活，不吃本地资源（[cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)）。这跟网页版 ChatGPT 或 Grok 完全两码事：网页关了任务就断，Grok Bot 则是你走开了，它还在继续跑。

关于这台云电脑（内部代号常被称为 `box`，视觉图标则是一个经典的中餐外卖折盒 `to-go` box 🥡），Grok Bot 官方设计师 Peng Zheng（`@pengzheng_`）在 2026 年 10 月 24 日分享过一段极客味十足的幕后典故（[@pengzheng_ 原帖](https://x.com/pengzheng_/status/2113786630033322239)，获 204 赞、148 书签；及补充帖 [X 帖](https://x.com/pengzheng_/status/2113804819274277015)）：为了搞清楚这个标志性的外卖纸盒在真实物理世界里究竟是怎么折叠成形的，他直接把任务派给了 `@bot`。Bot 先是在全网检索挖掘出 **1908 年的中餐外卖折盒原始专利图纸**，随后直接在自己的云电脑里编写 Python 脚本驱动 **Blender** 完成了 3D 建模——将纸盒的每一片折页严格沿着 1908 年专利图纸上的折痕线（crease lines）绑定为物理铰链（hinge），最终渲染出与 🥡 Emoji 严丝合缝的开合无缝循环动画，用作官方页面的 `og:video`。用云电脑自己考据百年专利、再用 Blender 渲染出云电脑自己的视觉图腾，恰好是这套沙箱能力最生动的注脚。

这台云主机的硬件规格，社区用户测算大致是 8 核 CPU、16GB 内存、约 128GB 硬盘（[X 帖](https://x.com/hejushang8/status/2103760664217174494)；[NodeSeek 帖](https://www.nodeseek.com/post-906175-1)）。官方文档没有对外公开过硬性参数，后续随时可能会变。

核心规则是：**同一个账号下的所有 Bot 共用这一台电脑**。官方文档写得很清楚："Every Bot on your account uses the same computer"（[cursor.com/help/grok-bot/computer-and-apps](https://cursor.com/help/grok-bot/computer-and-apps)）。共用意味着什么？浏览器 Cookie 和登录态完全打通，一个 Bot 登了 Gmail，其他 Bot 抬手就能用（同上）；硬盘文件对所有 Bot 开放（同上）；命令行凭据也是共享的（同上）。

好处是 Bot 之间交接工作不用反复登录、重新配环境，前面做了一半，后面接手就能干。坏处是这里不存在安全边界，官方明确提醒："do not place a credential or file on it if another Bot on your account should not be able to use it"（同上）。§08 讲安全时我会单独拆解，这里先记牢：千万别在云电脑里登你的网银。

虽然共用一台机器，但每个 Bot 分配了独立的屏幕（screen）。多个 Bot 可以并行使用浏览器和桌面工具，不过单个 Bot 同一时间只能跑一个 computer-use 任务（同上）。官方设计博客的比方打得很形象：这更像"和同事同处一室办公"，而不是"操作一台远程机器"——你能看到他们都在忙，探头瞄一眼屏幕就知道进度，遇到卡壳再坐过去接手键盘鼠标（[x.ai/news/designing-grok-bot](https://x.ai/news/designing-grok-bot)）。

> [!NOTE]
> 📸 **截图位（待补）**：Agent Computer 云电脑视图

!["所有 Bot 共享一台云电脑"示意图——共享区域（浏览器/文件/登录态）与独立区域（各 Bot 的屏幕）](../images/fig-01-2.png)

*图："所有 Bot 共享一台云电脑"示意图——共享区域（浏览器/文件/登录态）与独立区域（各 Bot 的屏幕）*

## 1.3 它能做什么、不能做什么 · Can / Can't

### 能做什么

官方文档列出了 8 个核心方向，每个方向都配了可复制的提示词（[cursor.com/help/grok-bot/use-cases](https://cursor.com/help/grok-bot/use-cases) 与技术文档中心 [cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases)）：销售外拓（Sales Outbound，从 CRM 调取目标客户打分并起草外联邮件）、招聘猎头（Talent Scout，按岗位筛选候选人并排除已有记录）、付费投放（Paid Media，拉广告数据比对预算与 CAC）、费用管理（Expense Manager，按周核对报销单据标记违规）、产品性能（Product Performance，调查线上故障出具截图和依据）、Bug 复现（Bug Reproduction，在测试环境还原问题产出复现步骤与最小用例）、客户健康（Account Health，结合用量与工单评估续约风险），以及总参谋长（Chief of Staff，每日通读收件箱、日历、Slack 和纪要梳理优先级）。

中文社区的玩法要接地气得多（本书调研汇总 research/zh/zh-summary.md，非官方页面）：接微信做自动客服（10 月热度最高）、自媒体流水线（公众号和小红书的选题、写稿加排版）、跨境电商巡检竞品与监控新词、结合 Google Maps 和 Gmail 规划旅行、批量退订垃圾邮件、在云电脑里跑 ffmpeg 脚本渲染视频，以及搭建 Notion 数据看板。这些玩法我在 Part 5 会逐个拆解，这里先知道大致框架。

随着 2026 年 10 月中下旬 v0.71.2 至 v0.75.5 版本的密集更新（详见官方更新日志 [x.ai/changelog/bot](https://x.ai/changelog/bot)），Grok Bot 的能力边界又迎来了四项质的飞跃，将此前“无法直接生成视频或维护持久交互看板”的旧限制彻底打破：

1. **Pages（Canvas）实时交互看板与应用（v0.75.2 上线）**：Bot 现在不仅能输出聊天文本，还能直接创建并持续热更新包含表格、图表、时间线与交互组件的 **Pages**（[@bot 官方公告](https://x.com/bot/status/2112991843235610885)，获 6,544 赞、2,008 书签；[x.ai/changelog/bot](https://x.ai/changelog/bot)）。所有生成的 Page 会沉淀在对应 Bot 右侧信息栏的 `Library` 中，并支持 **Only you**（仅自己）、**Your team**（团队可见）和 **Anyone with the link**（公开链接）三级分享权限。例如社区开发者 Melvin Vivas（`@melvindvivas`）就让 Chief of Staff 幕僚长 Bot 创建了一个实时更新的 `Activity Dashboard` 看板（[@melvindvivas 案例帖](https://x.com/melvindvivas/status/2113676935956160882)，获 1,087 赞、1,687 书签），在一个页面内统揽所有专职 Bot 的时间线、进行中任务、已完成事项与待人工审批队列。
2. **Grok Imagine 原生视频生成与代码动效渲染（v0.71.2 上线）**：Bot 现已内置 Grok Imagine 视频生成能力，既能直接在对话中生成与编辑实拍感视频素材（[@bot 生视频官宣](https://x.com/bot/status/2110566041772617908)，获 20,762 赞、1,923 转发、4,769 书签），也能在云电脑中用代码（Remotion / CSS / Canvas / FFmpeg）编写并渲染严丝合缝的动态图形视频（Motion Graphics）（[@bot 代码动效演示](https://x.com/bot/status/2110772748805194127)，获 2,616 赞）。
3. **Vault 内置加密保险箱与 1Password 免密填充（v0.75.2 & v0.75.5 上线）**：针对浏览器自动化中最头疼的账号登录与绑卡结账环节，官方先后推出了两套零明文暴露方案。一是 **1Password Brokered Sign-in（代理逐次授权登录）**（[@bot 1Password 官宣](https://x.com/bot/status/2113301060811161874)，3,663 赞；[@1Password 联合发布](https://x.com/1Password/status/2113276767582498943)，10,507 赞；详见 [cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)），无需配置繁琐的共享 Vault，只需在本地 1Password App（v8.12.42+）上按指纹批准，即可把个人库凭据注入 Bot 浏览器；二是内置只写加密存储区 **`Settings → Vault`**（[@bot Vault 官宣](https://x.com/bot/status/2113754107861532677)，9,398 赞、2,756 书签；详见 [cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)），支持保存登录凭据（含 2FA/TOTP）、信用卡（支持手机摄像头扫卡识别）与收货地址，并支持 5 MB 以内的密码管理器 CSV 批量导入。Bot 仅能读取明文 `Hint` 标签并通过底层 `BrowserSecureFill` 注入表单，永远看不到明文密码、完整卡号或 CVV（官方登录与结账调用优先级详见 [cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。
4. **iPhone Action Button 一键语音通话（iOS v1.16+ 上线）**：在 iPhone 15 Pro 及后续机型上，用户可将侧边操作按钮（Action Button）直接绑定为 Grok Bot 的 `Start Voice Chat` 或指定专职 Bot 的 `Start Voice Chat with Bot` 快捷指令（[@bot Action Button 官宣](https://x.com/bot/status/2112246033178968161)，7,264 赞、2,213 书签；详见 [cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat) 与 [cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）。盲按手机侧键即可随时开口向云端团队派活，挂断后聊天流会自动生成带完整逐字稿（transcript）的语音卡片并立即跟进执行。

### 做不到的事

我调研下来，目前明确做不到的事主要有这几项：

国内主流应用没有任何官方插件。微信、小红书、抖音、QQ 邮箱通通没有接口。想让它跑，只能靠网页版登录、导出文件或者手工截图绕过去（[象鱼工作流](https://xiangyugongzuoliu.com/grokbot-use-cases/)）。这对国内用户来说门槛最高，§11 会专门讲怎么绕路。

你没法手动选底层模型。前面说过，Bot 会按任务自动分流，官方压根没留模型切换开关（[TNW](https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk)）。

**付款和对外发送必须经过人工审批**。Bot 掏钱买东西会弹出确认卡片让你核对金额，发邮件和发 Slack 消息可以先生成草稿卡片，等你点 Send 才送出（changelog v0.45.0；官方用例提示词也都以"Do not send"、"Do not contact anyone"结尾，[cursor.com/help/grok-bot/use-cases](https://cursor.com/help/grok-bot/use-cases)）。注意这不是绝对红线：9/30 的 v0.64.0 起，草稿卡片上可以选"Disable drafts for this Bot"，之后该 Bot 会直接发送（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。新手建议保持草稿模式。此外在结账环节还有一条极关键的 Vault 边界：根据官方 [cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets) 说明及社区博主 `@kial`（[X 帖](https://x.com/kial/status/2114201768414646280)）、`@JianWeiSignal`（[X 帖](https://x.com/JianWeiSignal/status/2114195530611855488)）的实测提醒，**一旦将银行卡保存在 Vault 中，结账填充该卡时不会再触发单独的逐笔 Vault 弹窗确认**（仅受通用购买审批约束）；如果你希望每一笔消费都必须亲手输入卡号把关，切勿把主力银行卡常驻保存在 Vault 中。

目标网站随时能拦死它。Bot 虽能跑浏览器，但对方站点一旦开启防爬风控、强制验证码或登录态过期，Bot 就会停下来把控制权交还给你，它自己翻不过去（[cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)）。不过现在面对数据中心 IP 被拦的情况，你可以在桌面端开启 `Settings > Computer > Your computer > Route traffic through this computer`，借用本机住宅 IP 绕过大部分云机房反爬拦截（参见 `@XueshiQiao` 实测分享 [X 帖](https://x.com/XueshiQiao/status/2112866936229183589)）。

![能力矩阵——左列"能做"（8 个官方用例 + 中文热门 10 例），右列"不能做"（无国内插件、不能选模型、必须审批等）](../images/fig-01-3.png)

*图：能力矩阵——左列"能做"（8 个官方用例 + 中文热门 10 例），右列"不能做"（无国内插件、不能选模型、必须审批等）*

## 1.4 时间线：8/11 到今天 · Timeline

Grok Bot 从上线到写书这天刚好两个月，版本迭代极快，官方 changelog 已经刷出了 **49 个版本**（v0.17.0 到 v0.68.1），并在 10 月中下旬继续一路狂飙至 **v0.75.5**（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。我把关键节点梳理出来：

2026 年 2 月 2 日，SpaceX 正式收购 xAI（[x.ai/news/xai-joins-spacex](https://x.ai/news/xai-joins-spacex)）。

8 月 11 日，Grok Bot 正式发布并开放早期测试，官方定义是随时在线的 Agent 团队，自带独立电脑，像人一样操作各类应用（[x.ai/news/introducing-grok-bot](https://x.ai/news/introducing-grok-bot)），同日发布了 Grok 4.6 模型（[x.ai/news/grok-4-6](https://x.ai/news/grok-4-6)）。8 月 26 日扩大权限，SuperGrok 全档、Cursor Pro 和所有 Cursor Teams 计划都包含 Grok Bot（[x.ai/news/grok-bot-more-plans](https://x.ai/news/grok-bot-more-plans)）；X Premium+ 绑定见 8 月 25 日的 changelog v0.27.0（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。三天后，8 月 29 日上线 X 集成，Bot 能读写公开推文（[x.ai/news/grok-bot-and-x](https://x.ai/news/grok-bot-and-x)）。

到了 9 月，节奏全面提速。9 月 3 日企业版上线，补齐访问控制、网络策略和审计日志，同日发布设计架构解析（[x.ai/news/grok-bot-for-enterprise](https://x.ai/news/grok-bot-for-enterprise)；[x.ai/news/designing-grok-bot](https://x.ai/news/designing-grok-bot)）。9 月 4 日官方晒出采购 Bot（Haggle Bot）案例，帮企业省下超 $100,000 直接成本（[x.ai/news/grok-bot-procurement](https://x.ai/news/grok-bot-procurement)）。9 月 21 日发布 Grok 4.7 模型，主打编程和知识工作提速一倍、成本减半（[x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)）。次日又公布客服案例，工单量涨了 175% 却没加一个人，单票成本压到 $0.20–0.30（[x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）。9 月 28 日上线 Team Bots，一个 Bot 全队共用，能直接嵌进 Slack（[x.ai/news/team-bots](https://x.ai/news/team-bots)）。

进入 10 月几乎一天一个样。10 月 2 日推出主动任务建议（[@bot X 帖](https://x.com/bot/status/2105713240701538538)）。10 月 3 日全员重置额度（[@bot X 帖](https://x.com/bot/status/2106083136002310193)）。10 月 7 日马斯克宣布路由外部大模型（[马斯克 X 帖](https://x.com/elonmusk/status/2107724314451878104)；[TNW](https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk)）。10 月 8 日 X 深度监控上线（[@bot X 帖](https://x.com/bot/status/2107949161878606089)），但同日发生大规模容量事故，大范围出现 "Bot failed to respond"，定时任务全部瘫痪（[Cursor 论坛](https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125)）。10 月 9 日接进 Shopify（[@bot X 帖](https://x.com/bot/status/2108228871938359347)）。10 月 10 日上线 Bot 专属邮箱，能注册服务、发信联系商家（[@bot X 帖](https://x.com/bot/status/2108609764766908772)）。截至 10 月 12 日本书首轮截稿，changelog 刷到 v0.68.1，新加了做幻灯片和换聊天配色（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。

从 10 月 13 日到 10 月 25 日，Grok Bot 又密集迎来了一波重磅更新（[x.ai/changelog/bot](https://x.ai/changelog/bot)）：

- **10 月 13 日–10 月 18 日（The X Subscription 三合一统一订阅）**：`@bot` 正式宣布 Grok Bot 并入 **The X Subscription**，以单一套餐（Premium $30/月、Super $100/月、Ultra $200/月）打通 Grok、Cursor 与 X Premium，共享同一周额度池与 Prepaid Credits 预付额度机制（[@bot X 帖](https://x.com/bot/status/2110063783796572496)；[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。
- **10 月 14 日（v0.71.2：Grok Imagine 生视频 + 专属邮箱 `+alias` 别名）**：发布 v0.71.2（[x.ai/changelog/bot](https://x.ai/changelog/bot)），正式支持调用 Grok Imagine 生成与编辑视频及代码渲染 Motion Graphics 动效（[@bot 生视频 X 帖](https://x.com/bot/status/2110566041772617908)；[@bot 动效 X 帖](https://x.com/bot/status/2110772748805194127)）；同日工程师 Sam Sokolin（`@SamSokolin`）宣布 `@mail.grokbot.com` 专属邮箱支持 `+alias` 加号子别名，可按特定后缀精准触发对应的 Routine（[@SamSokolin X 帖](https://x.com/SamSokolin/status/2110496237241667621)；[cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)）。
- **10 月 15 日（Link / X Money 结账与 Elon Musk SpaceX 全额赔付承诺）**：支持在结账环节使用 Link 与 X Money 付款，Elon Musk 公开发文做出背书：如果 Grok Bot 在代购中出错或泄露银行卡（迄今从未发生），SpaceX 将全额赔付（*"If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole"*，[@elonmusk X 帖](https://x.com/elonmusk/status/2110610960474079445)）。
- **10 月 16 日（X Chat 端到端加密私信与消息请求接入）**：工程师 Paul Vann（`@pjvann`）宣布 Grok Bot 打通 X `@chat` 端到端加密私信收件箱与陌生人消息请求（message requests），配合本地沙箱中的官方解密仓库 `github.com/xdevplatform/xchat-grokbot-helper` 与 4 位 PIN 码自动分拣私信（[@pjvann X 帖](https://x.com/pjvann/status/2111104660773687646)）。
- **10 月 19 日（iPhone Action Button 一键实时语音）**：iOS 客户端 v1.16+ 支持将 iPhone 15 Pro 及后续机型的侧边 Action Button 直接绑定为 Grok Bot 实时语音通话或唤醒指定专职 Bot（[@bot X 帖](https://x.com/bot/status/2112246033178968161)；[cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)）。
- **10 月 21 日（Pages 实时交互看板发布）**：正式上线 Pages（Canvas），支持由 Bot 创建并持续热更新实时数据报表、多 Bot 协同看板与内部交互工具，提供三级分享权限（[@bot X 帖](https://x.com/bot/status/2112991843235610885)）。
- **10 月 22 日（v0.75.2：1Password Brokered Sign-in + Routine 300 次/小时大幅提额）**：联手 1Password 发布免共享库的 Brokered Sign-in 逐次生物识别授权登录（[@bot X 帖](https://x.com/bot/status/2113301060811161874)；[@1Password X 帖](https://x.com/1Password/status/2113276767582498943)）；打通 iOS 原生日历、提醒事项与通讯录直读；支持邮件转发保留完整 HTML、内嵌图与附件；并将 Routine 频率上限大幅提升至**全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时**（定时最小间隔仍为 5 分钟，详见 [cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines) 与 [x.ai/changelog/bot](https://x.ai/changelog/bot)）。
- **10 月 23 日–10 月 25 日（v0.75.5：Vault 内置保险箱上线与文档全面迁入 `cursor.com`）**：发布 v0.75.5（[x.ai/changelog/bot](https://x.ai/changelog/bot)），全面开放 `Settings → Vault` 加密保存登录凭据、银行卡与地址（[@bot X 帖](https://x.com/bot/status/2113754107861532677)；[cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)），同时官方技术文档与帮助中心全面整合至 [cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot) 与 [cursor.com/help/grok-bot](https://cursor.com/help/grok-bot)。

![时间轴长图——从 08-11 发布到 10-12，标注关键里程碑](../images/fig-01-4.png)

*图：时间轴长图——从 08-11 发布到 10-12，标注关键里程碑*

用户增长方面：Bloomberg 报道称截至 9 月 14 日周活用户达到 418,000，环比增长 24%，数据来自伦敦活动上的一份演示文稿（[Mint 转载 Bloomberg](https://www.livemint.com/ai/elon-musk-s-grok-bot-hits-418-000-weekly-users-after-one-month-11790093107144.html)）。SpaceX 官方未作回应。而到了 10 月下旬，据社区观察者 Wenser（`@wenser2010`）汇总披露，Grok Bot 上线仅两个月便已突破 **80 万周付费用户（800K weekly paid users）**（[@wenser2010 增长分析帖](https://x.com/wenser2010/status/2113683422409572523) 与 [竞品对比跟帖](https://x.com/wenser2010/status/2113683427069489614)）。这个数字虽然与免费消费级产品 Meta Muse 据报超 300 万的周活体量维度不同（[TNW](https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk)）——Muse 免费但受限于美国地区及 Meta 账号准入墙，而 Grok Bot 走 $30/月起步的付费路线且扎根生产力与多智能体工作流，80 万周付费用户的含金量极其可观。

## 1.5 为什么是现在 · Why Now

2026 年下半年，各大厂商扎堆涌入个人 AI Agent。每家都在推自己的产品：Meta 推出 Muse（免费，主打消费场景），OpenAI 推出 Dots（需要 ChatGPT Pro $100+），Google 有 Gemini Spark，Anthropic 有 Claude Cowork，开源界也有 OpenClaw 和 Hermes（[aiformortals 三方评测](https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)；本书调研笔记 research/web/compare/compare-notes.md）。社区里有博主一口气测了 21 个通用 Agent（[X 帖](https://x.com/i/status/2105067074720829819)）。

在这场混战里，Grok Bot 的切入点和别人不一样。社区有句广为流传的概括："**Dots 是 AI 秘书，Grok Bot 是 AI 组织**"（[X 帖](https://x.com/i/status/2105404819745718679)）。Muse 和 Dots 给你的是单个助理，Grok Bot 给你的则是一支团队——每个 Bot 有名字、有职位、有长期记忆，能在群聊里互相协同、交接任务。

这套“AI 组织”到底能爆发多大的商业杠杆？官方自己用实战交出了一份教科书级的答卷（[x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）：2026 年 8 月 14 日 Cursor 并入 SpaceXSI 后，全球客服工单量瞬间暴增 **175%**。面对山呼海啸般的咨询与账单请求，官方团队没有扩招哪怕一名全职客服（**0 new support hires**，相当于直接省下了约 200 名新增客服人力），而是部署了一支由 5 位专职 Bot 组成的客服舰队——涵盖分诊接待（Intake Triage Bot）、账单与退款（Billing & Refund Bot）、技术复现（Technical Repro Bot）、事故批处理（Incident Batch Bot）与产品反馈聚类（Product Feedback Synthesizer Bot）。这支 AI 团队直接将单张工单的解决成本压到了 **$0.20–$0.30**（远低于行业平均的 **$1.00–$4.00**），实现了 **99%** 退款申请的全自动核验闭环；在一次线上突发故障中，仅由一名人类工程师审批一张批量确认卡，就在 **10 分钟**内一次性清零了 **204 张**故障工单，并且每天还能从海量对话中自动提炼超过 **20,000+** 个产品反馈数据点反哺研发。

价格层面，随着 The X Subscription 的推出，Grok Bot 的主力门槛定格在 **Premium $30/月**（一价打包 Grok、Cursor 与 X Premium，高于此前的 Super $100/月与 Ultra $200/月则提供更充裕的共享周额度池，同时既有独立 Cursor Pro $20/月老订户仍可维持原价，详见 [cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。正如 `@wenser2010` 在三大大厂 Agent 横评中所指出的（[X 帖](https://x.com/wenser2010/status/2113683427069489614)）：Muse 虽是免费起步但有严格的美区准入限制且高级功能也要 $20–100，OpenAI Dots 死死绑定在 $100/月起步的 Pro 订阅上，OpenClaw 和 Hermes 则支持自建托管（[X 价格横比](https://x.com/i/status/2105195069263225049)）。相比之下，$30/月即可同时拿下主力 IDE（Cursor）、主力大模型（Grok）、社媒生态（X Premium）与 24 小时云端 AI 团队（Grok Bot），在性价比和生态协同上形成了降维打击。

有社区用户做过旅行规划的三方实测：Grok Bot 耗时最短，订机票比 Muse 便宜约 $90，Airbnb 便宜约 $136。换到小商家运营测试，Grok Bot 顺畅办完退款，还额外揪出了两笔隐蔽的重复扣费。该作者的结论是："For work, Grok Bot wins"（[aiformortals 评测](https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)）。这属于单一测试样本，不能直接套用到全部场景。

21 个 Agent 横评里，有句评价抓得很准："It works like a black box, no reasoning, no logs, but it produces the outputs I'm always happy with"（[X 帖](https://x.com/i/status/2105067123081105501)）。黑盒运作、缺乏推理过程与执行日志，在需要严密合规审查的企业环境里是潜在隐患。针对这一痛点，官方目前已在企业版中补齐了 ISO/IEC 27001 与 ISO/IEC 42001 认证、OpenTelemetry 遥测过滤（`cursor.surface=grok_bot`）、MCP 出站白名单与 Inference Hooks 推理审计钩子（[cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)），我会在后面的安全章节深入剖析。

竞品赛道变化极快。你读到这篇内容时，上面的部分对照可能已经出现变化。我把详细的竞品功能对照表单挪到了附录 H，正文只聚焦定位差异，省得花篇幅在容易失效的参数对比上。

![竞品定位坐标图——横轴"个人→团队"，纵轴"免费→付费"，标注 Muse / Dots / Grok Bot / OpenClaw / Hermes 的大致位置](../images/fig-01-5.png)

*图：竞品定位坐标图——横轴"个人→团队"，纵轴"免费→付费"，标注 Muse / Dots / Grok Bot / OpenClaw / Hermes 的大致位置*


# §02 怎么才能用上 · Getting Access

我调研中文社区时发现，问得最多的就是两件事：怎么用上 Grok Bot，怎么付钱。对国内用户来说，用上本身就是道坎。我把门槛拆成六块：谁能用、花多少钱、怎么付、怎么连，以及哪些坑千万别踩。

## 2.1 资格一张表 · Who Gets It

先搞清一件事：Grok Bot 不单独卖，它是 **The X Subscription（三合一统一订阅）** 以及既有 Cursor / SuperGrok 体系里的核心权益。2026 年 10 月 13 日，Grok Bot 官方账号 `@bot` 正式宣布 Grok Bot 并入 **The X Subscription**，用一套统一订阅计划同时打包 **Grok**、**Cursor** 与 **X Premium** 三大产品线（[x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)，获 3,039 赞、272 转发、540 书签；详见官方总览文档 [cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。

对于现在新入场的用户，**The X Subscription 是当前官方默认主推的第一顺位准入路径**（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。在此体系下，三大产品天然共用同一个底层账号与每周额度池，不再需要繁琐的跨平台手动关联操作。而如果你是老订户，不管走哪条旧版独立订阅路线，用量最终都记在一个 **Cursor 账号**上（"Grok Bot usage is metered on your Cursor account"），所以旧版路径的第一步永远是注册一个 Cursor 账号——哪怕你不写代码、从不打开 Cursor 编辑器（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。

> 前提条件：一个能收验证码的邮箱或手机号；一种能付美元订阅的方式（外币卡，或本章 2.3 的支付宝路径）；能稳定访问境外网站的网络。三样缺一样，先看 2.3–2.5。

在 The X Subscription 统一订阅体系推出之前，官方曾在 8 月 26 日把权限下放给了所有付费档（[x.ai/news/grok-bot-more-plans](https://x.ai/news/grok-bot-more-plans)），当时Kin 橙皮书说「Cursor Pro $20 暂不含 Grok Bot，Pro+ $60 是最低门槛」就已经成为老黄历。如今进入 2026 年 10 月中下旬，官方帮助页进一步明确了**新旧双轨并行**的准入规则（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）：

1. **新订户默认主推路径（The X Subscription 三合一统一订阅）**：
   - **包含 Grok Bot 权限的档位**：**Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）**。开通任意一档，即可直接同时获得 Grok Bot、Grok 与 Cursor IDE 及 X Premium 权益（[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。
   - **不包含 Grok Bot 权限的档位**：**Free（$0）** 与 **Plus（$8/月）** 档位不包含 Grok Bot 使用权限（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。
2. **既有独立订阅存续路径（Legacy Plans 老订户规则）**：
   - 既有独立订阅的 **Cursor Pro（$20/月）**、**Cursor Pro+（$60/月）**、**Cursor Ultra（$200/月）** 以及自助式 **Cursor Teams（$40/人/月）** 老订户，只要不主动发起合并升级，仍可继续保留原有的独立档位、定价与 Grok Bot 权限（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。
   - 除了独立 Cursor 这条线，尚未迁移至统一订阅的老用户也能继续走旧版独立 **SuperGrok** 或 **X Premium+** 关联路线，把 Grok 账号关联到 Cursor 账号拿到用量授权（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。

下面这张表完整覆盖了当前 The X Subscription 主推路径与旧版独立订阅存续路径下能用 Grok Bot 的所有情况：

| 你的情况 | 所属体系 | 操作方式 | Grok Bot 用量等级 |
|---|---|---|---|
| **The X Subscription Ultra（$200/月）** | **当前主推三合一统一订阅** | 同一账号直接登录，Grok / Cursor / Grok Bot 三端免关联互通 | **最高（共享周额度池）** |
| **The X Subscription Super（$100/月）** | **当前主推三合一统一订阅** | 同一账号直接登录，Grok / Cursor / Grok Bot 三端免关联互通 | **中（共享周额度池）** |
| **The X Subscription Premium（$30/月）** | **当前主推三合一统一订阅** | 同一账号直接登录，Grok / Cursor / Grok Bot 三端免关联互通 | **标准入门（共享周额度池）** |
| **The X Subscription Plus（$8/月） / Free（$0）** | **当前主推三合一统一订阅** | **不含 Grok Bot 权限**（需升级至 $30 Premium 及以上） | — |
| Cursor Ultra（$200/月） | 旧版独立订阅（老订户存续） | 同账号登录，直接用（可在 `cursor.com/unify` 单向升级） | 最高 |
| Cursor Pro+（$60/月） | 旧版独立订阅（老订户存续） | 同账号登录，直接用（可在 `cursor.com/unify` 单向升级） | 中 |
| Cursor Pro（$20/月） | 旧版独立订阅（老订户存续） | 同账号登录，直接用（可在 `cursor.com/unify` 单向升级） | 低 |
| Cursor 团队版（$40/人/月起） | 自助式团队独立订阅 | 每位成员用自己的 Cursor 账号登录 | 团队版额度 |
| SuperGrok Heavy（官方价格未抓到，橙皮书写 $300，未核实） | 旧版独立关联路径 | 在 Grok Bot 里关联 Grok 账号（或升级至统一订阅） | 最高关联用量 |
| SuperGrok Plus（约 $100，见下表） | 旧版独立关联路径 | 在 Grok Bot 里关联 Grok 账号（或升级至统一订阅） | 中 |
| SuperGrok（$30/月，第三方 didreset 数据） | 旧版独立关联路径 | 在 Grok Bot 里关联 Grok 账号（或升级至统一订阅） | 低 |
| X Premium+（旧版独立订阅） | 旧版独立关联路径 | 关联 Grok 账号 | 低于 SuperGrok Plus |
| 自助 Grok Business 席位 | 企业/团队商业席位 | 退出后用 Sign in with Grok 重新登录，无需关联 | 与席位许可对应（SuperGrok 或 Heavy） |
| Cursor / Grok Enterprise | 企业级定制订阅 | 联系客户经理或管理员开通 | 由管理员管理 |
| SuperGrok Lite | 旧版基础计划 | 不含 Grok Bot | — |

来源：[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)、[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)

这里有几个关键规则和坑我得说明白。第一，如果你走的是旧版独立订阅关联路径，Cursor 订阅和 SuperGrok 关联用量**不叠加（do NOT stack）**，系统只取两者中周额度上限更高的一档生效。比如你同时有旧版 Cursor Pro 和 SuperGrok Plus，额度按 Plus 走，不会加在一起（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。第二，旧版跨账号关联是**永久的**，不能解绑也不能转移。点关联前，务必确认登录的是你打算长期用的 Cursor 账号（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。第三，旧版独立订阅老用户随时可以通过 `cursor.com/unify` 或 `accounts.x.ai/unify` 主动升级切换至 The X Subscription，但官方明确规定这是**单向不可逆切换**——一旦切入 The X Subscription，就永远无法退回旧版 $20 Cursor Pro 或 $60 Pro+ 等独立计划（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。第四，免费试用给的是一笔固定用量额度和 7 天窗口，按智能体步数和 token 扣除，不是按发了几条消息算。一个大任务就能耗掉大半试用额度，用完不补发（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。

![资格判定流程图——你有 Cursor 付费订阅？→ 有 → 直接用。没有 → 你有 SuperGrok / X Premium+ → 有 → 关联。是 Lite？→ 不行。都没有 → 免费试用 7 天。](../images/fig-02-1.png)

*图：资格判定流程图——你有 Cursor 付费订阅？→ 有 → 直接用。没有 → 你有 SuperGrok / X Premium+ → 有 → 关联。是 Lite？→ 不行。都没有 → 免费试用 7 天。*

## 2.2 价格与档位 · Plans & Pricing

下面是官方标价。我们将当前主推的 **The X Subscription 三合一统一订阅** 与既有的 **旧版独立订阅（Legacy Plans）** 完整列出，所有数字均对齐官方订阅文档（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）以及 Cursor 定价页 JSON-LD 和 `x.ai/pricing`。

| 套餐 | 所属体系 | 月费（美元） | Grok Bot 准入与包含权益 | 来源 |
|---|---|---|---|---|
| **The X Subscription Free** | 三合一统一订阅 | $0 | **不含 Grok Bot** | cursor.com/help/grok-bot/plans |
| **The X Subscription Plus** | 三合一统一订阅 | $8 | **不含 Grok Bot**（仅基础 X 与基础权益） | cursor.com/help/grok-bot/plans |
| **The X Subscription Premium** | **三合一统一订阅（主推）** | **$30** | **含 Grok Bot + Grok + Cursor + X Premium** | cursor.com/help/the-x-subscription/overview |
| **The X Subscription Super** | **三合一统一订阅（主推）** | **$100** | **含更高额度 Grok Bot + Grok + Cursor + X Premium** | cursor.com/help/the-x-subscription/overview |
| **The X Subscription Ultra** | **三合一统一订阅（主推）** | **$200** | **含最高额度 Grok Bot + Grok + Cursor + X Premium** | cursor.com/help/the-x-subscription/overview |
| Cursor Pro | 旧版独立订阅（仅老订户保留） | $20 | 含 Grok Bot（低档独立额度） | cursor.com/pricing |
| Cursor Pro+ | 旧版独立订阅（仅老订户保留） | $60 | 含 Grok Bot（中档独立额度） | cursor.com/pricing |
| Cursor Ultra | 旧版独立订阅（仅老订户保留） | $200 | 含 Grok Bot（高档独立额度） | cursor.com/pricing |
| Cursor Teams Standard | 自助团队版 | $40/人 | 含团队版 Grok Bot | cursor.com/pricing |
| Cursor Teams Premium | 自助团队版 | $120/人 | 含高阶团队版 Grok Bot | cursor.com/pricing |
| SuperGrok | 旧版独立订阅 | $30 | 关联后可用 Grok Bot | didreset.com 引 x.ai/pricing（2026-09-17 快照） |
| SuperGrok Plus | 旧版独立订阅 | $100 | 关联后可用 Grok Bot | didreset.com 引 x.ai/pricing（2026-09-17 快照） |
| SuperGrok Heavy | 旧版独立订阅 | 官方价格页快照未显示价格 | 关联后享最高关联用量 | 橙皮书写 $300，未核实 |

来源：[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)、[cursor.com/pricing](https://cursor.com/pricing)、[x.ai/pricing](https://x.ai/pricing)

### 为什么社区一致首推 $30/月的 The X Subscription Premium？

在中文与英文 X 社区中，$30/月的 **The X Subscription Premium** 已经成为公认的性价比天花板：

- **竞品横向对比与 80 万付费用户里程碑**：Web3 与 AI 研究员 Wenser（`@wenser2010`）在 2026 年 10 月 23 日的深度分析帖（[x.com/wenser2010/status/2113683422409572523](https://x.com/wenser2010/status/2113683422409572523) 与 [x.com/wenser2010/status/2113683427069489614](https://x.com/wenser2010/status/2113683427069489614)）中指出，Grok Bot 自 8 月发布以来仅用两个月时间就突破了 **80 万周付费用户（800K weekly paid users）**。横向对比当前三大科技巨头的 Agent 产品：**OpenAI Dots** 最低门槛高达 **$100/月**（需 Pro 订阅起步）；**Meta Muse** 虽然免费，但受限于美国地区及 Meta 账号准入墙（US/Meta account gated）；而 **Grok Bot** 仅需 **$30/月**，还一并打包了 X Premium 蓝标会员、SuperGrok 与 Cursor 编辑器，生态协同与性价比优势极其突出。
- **新手入门与双栈开发者的黄金选型**：AI 创作者初阳AI（`@chuyang_ai`）在其 Grok Bot 新手视频课程第 1 期（[x.com/chuyang_ai/status/2111357749103911004](https://x.com/chuyang_ai/status/2111357749103911004)）中专门拆解了 Grok Bot 与 Claude Code 的定位差异，明确建议新入局者直接选择 **$30/月的 The X Subscription 档位**作为主力起点。而在英文开发者社区，当重度 Vibe-Coder `@itsvlady` 晒出自己每月 $120 Claude Code + $55 Grok Bot 的账单时（[x.com/itsvlady/status/2110803638671020277](https://x.com/itsvlady/status/2110803638671020277)，352 赞 / 55 书签），开发者 `@frogchan9o1` 给出了备受推崇的 **$50/月双栈高性价比方案**（[x.com/frogchan9o1/status/2110883156891140416](https://x.com/frogchan9o1/status/2110883156891140416)）——即 **$20 Claude Code + $30 The X Subscription Premium**，不仅一次拿齐 SuperGrok、Grok Bot、X Premium 与 Cursor，还能让本地 Claude Code 与云端 Grok Bot 共享同一个 Obsidian Vault 知识库协同工作。

### `cursor.com/unify` 单向合并升级机制

如果你此前已经单独订阅了 Cursor Pro（$20/月）、Pro+（$60/月）、SuperGrok 或 X Premium，官方提供了专门的账号与订阅合并通道（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）：

1. 访问 [cursor.com/unify](https://cursor.com/unify) 或 [accounts.x.ai/unify](https://accounts.x.ai/unify)，或者在客户端进入 `Settings > Usage & Billing > Manage Plan`。
2. 按照页面引导登录你现有的 Cursor 账号与 X / xAI 账号，选择目标档位（Premium $30 / Super $100 / Ultra $200）完成合并升级。
3. **不可逆铁律**：官方帮助文档明确警告（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)），从旧版独立订阅切换至 The X Subscription 是**单向操作（one-way switch）**。一旦完成合并升级，你将**无法退回**旧版 $20/月的 Cursor Pro 或 $60/月的 Cursor Pro+ 独立计划。如果你平时完全不用 X 平台或 Grok 网页端，且 $20 的旧版 Cursor Pro 额度已经够用，可以继续保留旧计划而不主动点击合并。

### 周额度池与两套截然不同的超额计费机制（Prepaid Credits vs 旧版 On-demand）

每个档位到底有多少额度？官方未公布具体数字。Cursor 帮助页只写了相对高低：Ultra 和 Heavy 最高，Super、Pro+ 和 Plus 居中，Premium、Pro 和 SuperGrok 最低，没有给任何 token 数、任务数或美元当量（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。第三方网站 didreset.com 也写明「xAI publishes no numbers」。

社区里有各种估算。LINUX DO 有人猜 Cursor Pro 的 Bot 额度大概是 250、450 或 495 美元（[linux.do/t/topic/2848179](https://linux.do/t/topic/2848179)），X 上也有人说一条消息耗大概 1% 周额度（[x.com/miniyarov/status/2105428357273800799](https://x.com/miniyarov/status/2105428357273800799)）。这些数字互相打架，我没法替你下结论。最靠谱的办法，是订阅后去 `Settings → Usage & Billing` 盯自己的 Weekly usage。

需要特别注意的是，随着 The X Subscription 的推出，官方将用量与超额计费彻底拆成了**新旧两套机制**（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）：

1. **The X Subscription 统一订阅体系（共享周额度池 + Prepaid Credits 预付额度）**：
   - **三端共享周额度池（One Weekly Usage Pool）**：在 The X Subscription 下，**Grok Bot、Grok 与 Cursor 三端共享同一个周额度池**（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。周额度每周按固定周期自动重置，当周未用完的额度**不会结转（does not roll over）**到下一周。
   - **为什么有人觉得升级后周额度掉电变快了？** 社区实战派博主 Charlie（`@charlie_pmp`）在 2026 年 10 月 25 日做过精准拆解（[x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）：升级到 The X Subscription 后感觉周额度消耗加快，核心原因有两个——第一，现在你在 **Cursor IDE 里写代码、在 Grok App 里聊天、在 Grok Bot 里跑任务，三端都在从同一个周额度池里抽水**；第二，后台高频运行且未经指令精简的冗余 **Routine 定时任务**是静默吞噬周额度的头号隐形杀手（自 v0.75.2 起，官方将 Routine 频率上限提升至全账号所有 Bot 合计 **300 次/小时**、单条 Routine 最高 **200 次/小时**，详见 [cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)，若不加节制地高频轮询，额度会迅速见底）。
   - **超额后改用 Prepaid Credits（预付额度）**：当包含在套餐内的周额度池耗尽后，The X Subscription 下的额外用量**不再走旧版的月底后付费账单**，而是直接从你的 **Prepaid Credits（预付额度）** 余额中实时扣除（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。你需要前往 [grok.com/dashboard/billing](https://grok.com/dashboard/billing) 页面下的 `Additional usage credits` 模块提前充值预付额度；该面板支持开启 **Auto Top-up（余额不足自动充值）**，并支持设置独立的 **Monthly additional usage limit（月度额外消费封顶上限）**，防止自动充值失控（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。
   - **Cursor 中调用第三方模型的特殊扣费边界**：官方计费文档特别说明（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)），在 The X Subscription 体系下，如果你在 Cursor 编辑器中调用**非 Grok 系列的第三方模型（third-party models）**，其产生的消耗**不会扣减包含在套餐内的 Grok 周额度池，而是直接扣减你的 Prepaid Credits（预付额度）**。因此，若想在 Cursor 中使用第三方模型，必须先在 `grok.com/dashboard/billing` 中保持足够的 Prepaid Credits 余额。
2. **旧版独立 Cursor 订阅体系（独立周额度 + Post-paid On-demand 后付费按需账单）**：
   - 对于尚未迁移到 The X Subscription 的旧版独立 Cursor Pro / Pro+ / Ultra 订户，用量依然分三个层次：包含在套餐里的每周用量（Weekly usage）每周重置；用完后如果开了按需用量（On-demand），超出的部分采用**后付费按需计费（Post-paid on-demand billing）**，由 Cursor 在账单期末结算，并受**月度限额**（Monthly Limit，可在客户端 `Settings > Usage & Billing > On-demand monthly limit` 或网页端 `cursor.com/dashboard > Spending > Monthly Limit` 中配置）约束。限额不会在任务中途强行掐断，跑着的 Bot 可以超出上限后完成任务（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。

无论你处于哪套体系，在 Grok Bot 客户端进入 `Settings > Usage & Billing`，都能集中查看当前的周额度进度条、Prepaid Credits 预付余额，以及点击 `Manage Plan` 和 `Manage Billing` 快速跳转管理（[cursor.com/docs/grok-bot/settings](https://cursor.com/docs/grok-bot/settings)）。

![档位对比卡——三列：Cursor 线、SuperGrok 线、X Premium+ 线，每列按用量从低到高排列，中间用虚线连接同级别的档位。](../images/fig-02-2.png)

*图：档位对比卡——三列：Cursor 线、SuperGrok 线、X Premium+ 线，每列按用量从低到高排列，中间用虚线连接同级别的档位。*

## 2.3 中国大陆用户：用支付宝开 Cursor Pro · Alipay Path

很多人最关心的就是这一节。

截至 2026 年 10 月 11 日，多位用户在 X 上实测确认：Cursor 官网结账页支持支付宝付人民币。最早发帖的是 @YuzuCMZ（327 赞 / 448 收藏），随后 @David114467 和 @cheery9998 等人做了交叉印证。AMZ123 跨境头条的谷歌SEO小平也发了带图教程（[x.com/i/status/2109157438226403420](https://x.com/i/status/2109157438226403420)、[x.com/i/status/2108488671699816806](https://x.com/i/status/2108488671699816806)、[amz123.com/t/lZiL8LFi](https://www.amz123.com/t/lZiL8LFi)）。有用户晒单实付约 139 元人民币（按当时汇率折算 $20）（[x.com/i/status/2109482976753127757](https://x.com/i/status/2109482976753127757)）。

社区整理的操作步骤如下：

1. 关掉代理，用浏览器无痕窗口打开 cursor.com/pricing。
2. 登录你以后打算关联 Grok Bot 的 Cursor 账号（关联永久有效，别登错号）。
3. 选 Pro 套餐，一定要**按月订阅**——年付和 Pro+ 目前基本不出支付宝选项。
4. 结账页把账单国家选成中国大陆，币种切到 CNY。
5. 支付方式找到支付宝（Alipay），扫码付款。
6. 付完去 cursor.com/dashboard 确认 Pro 状态，再去 Grok Bot 关联账号。

如果结账页看不到支付宝，这是被问得最多的问题。可以在 US 和 CNY 之间来回切换几次，切到 CNY 有时就会跳出来（[x.com/i/status/2109157438226403420](https://x.com/i/status/2109157438226403420)）。要是还不出来，清理浏览器缓存或换个浏览器。社区反馈老账号可能不显示，新注册的账号能看到（[x.com/i/status/2108838924491833373](https://x.com/i/status/2108838924491833373)）；也有人把网络节点切到新加坡后成功刷出（同上）。实在不行就给 hi@cursor.com 发邮件。

AMZ123 教程里还提到另一条路：在 App 内订阅时选「Pay without Link」，支付方式里也会出现支付宝（[amz123.com/t/lZiL8LFi](https://www.amz123.com/t/lZiL8LFi)）。

提醒一句：支付宝付款会开通自动续费代扣。付完记得去支付宝设置里查一下代扣协议，下月不想续就随手关掉。另外，这套方法依托 Cursor 结账服务 Stripe 对国内账单地址的支持，随时可能被官方调整，不保证长久可用。

> [!NOTE]
> 📸 **截图位（待补）**：结账页全流程 6 张——选 Pro → 选 CNY → 出现支付宝 → 扫码 → 支付成功 → 后台确认 Pro 状态

## 2.4 其他路径：App 内订阅、X 会员、SuperGrok · Other Routes

支付宝开 Cursor Pro 不是唯一的路，还有几条途径可选。

### 路径一：旧版 Cursor 账号关联 SuperGrok 或 X Premium+ 的具体入口与“不叠加”原则

如果你手头已经有旧版独立的 X Premium+、SuperGrok、SuperGrok Plus 或 SuperGrok Heavy 账号，且暂不打算合并升级到 The X Subscription，可以在 Grok Bot 里直接将 Grok / X 账号关联到你的旧版 Cursor 账号以获取用量授权。

官方帮助文档明确给出了两条标准关联操作路径（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）：

1. **客户端内关联入口**：打开 Grok Bot 客户端，依次进入 `Settings > Usage & Billing > Manage Plan > Get Access with Grok`，按照弹窗提示登录并授权你的 Grok / X 账号。
2. **网页端引导入口**：直接在浏览器访问 [cursor.com/bot/onboarding](https://cursor.com/bot/onboarding)，在引导流程中完成账号绑定。

@YuzuCMZ 提过一个技巧：桌面端要是卡在付费页，先给 X 账号绑上手机号（+86 也可以），然后再去登录（[x.com/i/status/2108748981069394279](https://x.com/i/status/2108748981069394279)）。不过官方明确说过，旧版独立 X Premium+ 属于最低用量档，低于 SuperGrok Plus（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。同时务必牢记官方的**“不叠加、取最高档（do NOT stack）”原则**：即使你的 Cursor 账号本身有付费订阅，又关联了 SuperGrok 或 X Premium+，两边的额度也绝不会累加，系统只会按周额度上限更高的那一档给你计费配额；而在全新的 **The X Subscription** 下，三大产品本就处于同一个统一订阅内，无需执行上述手动关联操作（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。

手里有外币 Visa 或万事达信用卡的话，可以直接开通 **The X Subscription（$30/月起）**，或者上 grok.com 订 SuperGrok（$30/月）再关联到 Cursor。LINUX DO 有人反馈国内双币信用卡也能刷过（[linux.do/t/topic/2961817](https://linux.do/t/topic/2961817)），NodeSeek 上还有人提到绑 Kraken 卡拿到了试用（[nodeseek.com/post-906175-1](https://www.nodeseek.com/post-906175-1)）。

### 路径二：手机 App 内订阅与合并升级时的“双扣陷阱”

手机端也能订。macOS 和 iOS 共享同一个用量池（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。但要注意，iOS 的 App Store 试用跟 Grok Bot 自己的 7 天试用不是一码事。App Store 试用到期不取消会自动扣费，得去 Apple ID 的订阅管理里手动退订（[cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）。Android 端目前没有 App 内试用。

更重要的一条红线发生在你通过 `cursor.com/unify` 或 `accounts.x.ai/unify` 将旧计划**合并升级为 The X Subscription** 时。官方计费与常见问题文档对此做出了专门的退费与双扣风险警示（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)、[cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）：

- **网页直付计划（Web Direct Plans）自动按比例退费**：如果你原有的 X Premium、SuperGrok 或 Cursor 独立订阅是在官方网页端通过 Stripe 直接绑卡或支付宝付款的，当你完成统一订阅合并时，旧的网页直付计划会**自动取消**，并且系统会按当前计费周期剩余未使用天数，**自动向原支付方式退还按比例折算的费用（prorated refunds）**。
- **Apple App Store / Google Play 渠道订阅不会自动取消或退款（高危双扣陷阱！）**：如果你此前的 X Premium、SuperGrok 或 Grok Bot 订阅是通过 **iPhone / iPad 的 Apple App Store** 或 **Android 的 Google Play** 应用内购买开通的，受苹果与谷歌商店的账单权限隔离限制，Cursor 与 xAI **无法替你自动取消或退还应用商店渠道的订阅**（[cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。你在网页端升级到 The X Subscription 后，**必须立即亲自前往 iOS 系统的 `设置 > Apple ID > 订阅` 或 Google Play 的 `付款和订阅 > 订阅` 页面手动取消旧的应用内订阅**，否则下个月你将同时收到网页端 The X Subscription 和手机应用商店的双份扣款账单！

有人打低价区的主意。LINUX DO 有帖子聊过去印度区订 SuperGrok，一个月只要 50 元人民币左右（[linux.do/t/topic/2848179](https://linux.do/t/topic/2848179)）。这条路有明确风险：跨区订阅可能违反 xAI 服务条款。关联建立后**不可解绑**，一旦账号被风控封禁，绑在上面的 Cursor 账号和 Bot 用量会一起泡汤。

> [!NOTE]
> 📸 **截图位（待补）**：App 内订阅页（iOS 和 Android 各一张）

## 2.5 访问与网络 · Network

好消息是，境内可以直接打开 x.ai/bot 产品页和 cursor.com/docs/grok-bot 官方文档。ai345 的教程作者实测确认了这点（[ai345.info/ai-guide/grok-bot-china-guide](https://www.ai345.info/ai-guide/grok-bot-china-guide)），@MrRenran 也提到手机没开境外漫游数据照样能访问（[x.com/i/status/2106964584276037798](https://x.com/i/status/2106964584276037798)）。不过客户端登录和云电脑的连接质量因地区和运营商而异，没法保证哪里都顺畅。

手机号验证是很多人卡住的关卡。用 Grok 账号登录 Cursor 时需要接短信验证码。LINUX DO 用户 @jaffliang 反映，切到美国节点后 +86 手机号能正常收到短信并登录（[linux.do/t/topic/2743888](https://linux.do/t/topic/2743888)）。但也有人遇到「此手机号验证过多」报错，换节点也没用（同上，楼主 @KendrickZou 和 @han123 回复）。卡在这里时，可以换换节点；改用 Google 或 GitHub 账号登录 Cursor 也许能绕开这一步，但调研里没有找到实测记录。值得庆幸的是，官方在 v0.71.2（2026-10-14）更新日志中已经针对客户端登录与账号关联流程做了专门的简化打磨（[x.ai/changelog/bot](https://x.ai/changelog/bot)）。

还有一个暗坑是隐私设置。官方排查文档明确写着：如果 Cursor 账号还在用**旧版隐私模式**（Legacy Privacy Mode），Grok Bot 根本无法启动。解决办法很简单，去 Cursor 账号的数据设置里，切换到支持云端存储的模式就行（[cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。

此外，Grok Bot 的云电脑跑在境外。如果要让 Bot 操作国内 SaaS 或公司内网，先评估数据出境合规（[ai345.info/ai-guide/grok-bot-china-guide](https://www.ai345.info/ai-guide/grok-bot-china-guide)）。这不是开个代理就能糊弄过去的。

> [!NOTE]
> 📸 **截图位（待补）**：登录报错示例——Legacy Privacy Mode 错误信息、手机号验证过多报错

## 2.6 代充、跨区与骗局 · Scams & Grey Market

在中文社区里，各种代充和灰产信息满天飞，不提醒很容易踩坑。

最危险的是代充。ClaudeMax 等代充平台打着「SuperGrok 代充 ¥299、Heavy 代充 ¥1,999」的旗号，要求你在浏览器打开 grok.com/api/auth/session，把整段 **Session JSON** 复制给他们，走微信付款（[claudemax.shop/blog/grok-bot-guide-supergrok](https://claudemax.shop/blog/grok-bot-guide-supergrok)）。ClaudeMax 自己都承认「不是官方也不是授权经销商」。Session JSON 里塞满了你的登录凭证与账号 ID，交出去就等于把账号交到陌生人手里。虽然对方声称用完就删，但你根本没法核实。能用支付宝直接订 Cursor Pro，就千万别碰这种代充。

跨区低价订阅也是雷区。有人去印度低价区订 SuperGrok，月费能压到 50 元人民币左右（[linux.do/t/topic/2848179](https://linux.do/t/topic/2848179)）。跨区订阅很可能违反服务条款（本书未逐条核对 xAI 条款原文），一旦触发风控封号，关联 Cursor 又无法解绑，你买的额度和账号全得陪葬。

公众号里还冒出过「Rakazo：Grok Bot 国内体验版」这类第三方工具（搜狗微信检索到的公众号标题，research/zh/weixin/weixin-list.md）。它不是官方产品。Grok Bot 没有中国大陆专供版，官方入口只有 x.ai/bot 这一个。

X 上还有人炒作 $GROKBOT 币和所谓「Bot 自主交易」，宣称「本金从 49 炒到 4391 美元」甚至翻几十倍（[x.com/i/status/2102291280965640690](https://x.com/i/status/2102291280965640690)）。这是赤裸裸的币圈营销套路。Grok Bot 确实能在人审批后下单买东西，但任何打着自动炒币暴富旗号的宣传都是骗局。

也有人打歪主意，想借 Bot 的美国云电脑去注册或订阅受地区限制的 Claude Code（中文社区公众号标题热点，zh-summary.md）。这违反 Anthropic 政策，极易封号。X 上已有用户吐槽，在 Bot 云电脑里刚注册 Claude 就被秒封，因为机房 IP 早就被风控盯上了（[x.com/i/status/2107099380847370475](https://x.com/i/status/2107099380847370475)）。

还有满天飞的 SEO 垃圾。我在 CSDN 搜出 443 条结果，去重后 287 篇，其中 113 篇是发布日期混乱或零阅读的机翻搬运（zh-summary.md）。这些文章还在嚼「只有 Heavy 和 Ultra 能用」这种 8 月份的过期旧闻。看到这类文章，先看更新日期，零阅读的直接关掉不用看。

![「骗局识别卡」——左列是可信信号（官方域名、有出处的社区实测、官方文档链接），右列是红旗信号（要你交 Session JSON、承诺回报率、低价区跳板、零阅读搬运、「国内体验版」）。](../images/fig-02-3.png)

*图：「骗局识别卡」——左列是可信信号（官方域名、有出处的社区实测、官方文档链接），右列是红旗信号（要你交 Session JSON、承诺回报率、低价区跳板、零阅读搬运、「国内体验版」）。*


# §03 十分钟安装与开箱 · Install in 10 Minutes

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

![快捷键速查卡（适合打印贴桌面）](../images/fig-03-1.png)

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


# §04 你的第一个任务 · Your First Task

装好客户端，绑定完账号，看着左边空荡荡的列表，很多人会愣住：第一句话该发什么？

别发“你好，你能帮我做什么”。Grok Bot 不是陪聊的对话框，它背后是跑在云端的电脑和数字员工。你敲字不是在聊天，而是在派工单。

这一章我不扯宏大团队编制，带你把第一件真活交到它手上。

> 适合谁：所有刚装好客户端的人。前提条件：已完成 §02–§03（有可用额度、已登录，推荐首选 $30/月的 The X Subscription Premium 三合一统一订阅，或保留既有的独立 Cursor Pro $20 / Pro+ $60 / Ultra $200 / Teams $40 老订户计划，注意通过 `cursor.com/unify` 单向升级切换不可逆）。任务一需要 Gmail 等境外邮箱；只有 QQ/163 邮箱的读者可以先做任务二、三，或直接用 4.1 的"上传文档"范例——它不需要任何连接器。此外，如果希望先通过视频快速建立全貌，可以参考 `@chuyang_ai`（初阳AI）制作的 Grok Bot 新手视频课程第 1 期（https://x.com/chuyang_ai/status/2111357749103911004），里面系统拆解了它与 Claude Code 的定位区别、为什么首推 $30/月的 The X Subscription 档位、客户端安装与创建第一个 Bot 的全流程；以及 `@itgoyo`（小田切让）浓缩的 90 秒 5 条核心上手铁律视频（https://x.com/itgoyo/status/2111332049193996421）。

## 4.1 任务五要素 · Outcome / Sources / Constraints / Deliverable / Review

给 Bot 派活最容易踩的坑，就是随手甩一句“帮我看看今天的邮件”。不给边界，它可能会在云电脑里把收件箱翻个底朝天，耗光额度，还翻出不该看的私人邮件。

我翻了官方文档，官方团队一开始就强调派活必须遵循明确结构（https://cursor.com/help/grok-bot/get-started）。Kin 在《Grok Bot 橙皮书》里提过“验收前置”（https://github.com/KinGao294/grok-bot-orange-book），但他主要讲了想好结果，没细说数据源边界和硬性约束。官方给出的标准范式包含五个核心要素，缺了一个，Bot 就容易跑偏或越界。

这五个要素是最终结果（Outcome）、信息来源（Sources）、约束条件（Constraints）、交付物形式（Deliverable）和人工审阅点（Review point）。最终结果要明确，说清楚做到什么程度算结束，比如“总结本周新增用户反馈”，别说模糊的“关注一下”。信息来源要限定范围，指明具体应用、网页、本地附件或特定对话，免得它在云电脑里到处乱翻。约束条件是安全底线，写清楚严禁做什么，比如“严禁点击删除”、“严禁修改原文档”、“外发前必须请示”。交付物形式要定死格式，除了 5 条要点的纯文本、带表头的表格、指定目录下的 Markdown 文档或语音通话结束后的 **Voice chat card（语音通话卡片）** 之外，自 v0.75.2（https://x.ai/changelog/bot）起，更推荐将 **Page（Canvas 实时交互页面/看板）** 作为首选的高可读性交付形态。人工审阅点则是刹车片，规定好在哪个节点停下等你确认，免得它一路狂奔把邮件发了出去或把单买了。

![任务五要素结构卡（Outcome / Sources / Constraints / Deliverable / Review）](../images/fig-04-1.png)

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

![同步盯梢与异步派活心智模型对照](../images/fig-04-2.png)

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


# §05 Bot：给每个同事一份岗位说明书 · Bots & Profiles

## 5.1 一个 Bot 等于什么 · Anatomy

很多人刚接触 Grok Bot 时容易犯一个错误：把它当成套了好看外壳的普通聊天窗口。每次在输入框敲一大段背景，聊完关掉网页；第二天遇到新任务，又开新窗口重敲一遍。这种用法停留在传统聊天机器人的习惯里。聊天会话是随用随扔的消耗品，窗口一关，之前建立的工作默契就散了。

官方文档对它的定义（https://cursor.com/help/grok-bot/bots），是一个有名字、有岗位、有独立对话流，能持续积累上下文的**持久共事的数字同事**。官方设计团队在复盘里写过（https://x.ai/news/designing-grok-bot），系统把概念收敛成了五个基础对象：Bot（持久运行的智能体）、Chat（对话界面）、Prompt（指令或技能提示词）、Tool（操作外部世界的工具）和 Artifact（生成的文档、代码等持久产物）。核心不是聊天记录，而是 Bot 本身。

随着 2026 年 10 月中下旬 v0.71.2（https://x.ai/changelog/bot）至 v0.75.5（https://x.ai/changelog/bot）的连续重磅迭代，一个完整的 Bot 拆开来看，已经从最初的四个基础部分扩展为**六个核心组成部分**（在原有四大组件基础上，新增了专属资料库 `Library` 与专属邮箱 `+alias` 子别名簇）。

一个是身份档案（Profile）。包括名称、头像、岗位标签和常驻描述（Description）。新手常把 Description 空着或随手写句客套话。官方文档写得很明确（https://cursor.com/help/grok-bot/bots），Description 是用来放持久规则的，聊天框只用来派发单次指令。比如“未经人工明确审批绝不对外发消息”要焊死在 Description 里，而“给这十二家客户起草跟进邮件”才是日常在聊天框里发的内容。

一个是工作记忆（Memory）。它能跨会话记住工作偏好、关键事实和任务摘要，第二天打开软件还能接着昨天的思路干。不过官方文档也提醒（https://cursor.com/help/grok-bot/bots），记忆不能代替真实数据源；严肃决策必须让它查实时原始数据，不能靠模糊印象。

一个是独立工位与屏幕（Computer & Workspace）。同一账号下的所有 Bot 共享同一台云电脑、浏览器会话和 /workspace 目录，但界面上各有独立的操作状态和屏幕感知（https://x.ai/news/designing-grok-bot）。官方设计了三层介入机制：后台运行时图标亮紫色表示活跃（Status）；点开能在侧边面板实时预览操作（Preview）；遇到验证码需要人工协助时，能一键全屏接管键鼠（Takeover）。（设计文章配图里还能看到正午、深夜等不同壁纸，是否随时间自动切换文中没有明说。）

一个是对话时间线（Conversation）。对话流里不仅有文字，还有结构化卡片（Inline chat widgets），比如待确认的邮件草稿或多选表单，也有系统事件和例行任务记录（https://x.ai/news/designing-grok-bot）。头像也有状态动作：空闲时安静（Idle），干活时点头（Working），卡住时迟疑（Waiting 或 Blocked），鼠标悬停在头像上能看到当前正在执行的具体步骤，不用盯着三个跳动的圆点猜。

一个是专属资料库（Library，存放该 Bot 维护的 Pages / Canvas 实时页面）。在 2026 年 10 月 21 日至 22 日随 v0.75.2 上线的更新中，官方正式推出了 **Pages（底层由 `WriteCanvas`、`EditCanvas`、`ReadCanvas`、`ListCanvases` 工具驱动的交互式画布）**（https://x.com/bot/status/2112991843235610885；https://x.ai/changelog/bot）。过去，Bot 交付的报告往往淹没在漫长的聊天历史气泡里；现在，每个 Bot 右侧的信息面板（`Bot info pane → Library`）都多出了一个持久化的 **Library（资料库）** 抽屉。这位数字同事为您构建并长期维护的周度数据报表、多智能体协同活动看板（Activity Dashboard）、项目进度追踪器或交互式业务沙盘，都会作为独立的实时网页应用沉淀在它的 `Library` 中。每次定时任务跑完或您口头下令更新数据，它不是重发一份死文件，而是直接对 `Library` 里的同一张 Page 进行原地热更新。

一个是专属邮箱 `+alias` 子别名簇（`mybot+tag@mail.grokbot.com`）。每位 Bot 不仅拥有形如 `mybot@mail.grokbot.com` 的独立工作邮箱（https://cursor.com/help/grok-bot/agent-email），还在 v0.71.2（2026-10-14）起正式支持 **`+alias` 加号子别名簇**，该特性由 Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）正式发布（https://x.com/SamSokolin/status/2110496237241667621，获 3,073 赞、219 转发、1,197 书签）。这意味着同一个专职 Bot 可以免费派生出无限个业务专用收件入口，例如 `mybot+newsletters@mail.grokbot.com`、`mybot+invoices@mail.grokbot.com`、`mybot+alerts@mail.grokbot.com`。更关键的是，您可以在配置 Routine 时设定**仅当邮件发送至特定 `+alias` 子别名时才触发对应的自动化流水线**（https://cursor.com/help/grok-bot/routines；https://cursor.com/help/grok-bot/agent-email），并且自 v0.75.2 起，Bot 在转发邮件时能够完整保留原邮件的 HTML 排版格式、正文内嵌图片（inline images）与附件（https://cursor.com/help/grok-bot/agent-email）。比如社区实践者 `@songsong275452`（引用 `@gokul_i`，https://x.com/songsong275452/status/2113108916229886371）就将所有行业通讯（Newsletters）统一订阅到专属 Bot 的邮箱别名下，让个人主邮箱彻底清净，再由周六定时 Routine 汇总成一份结构化周报。

关于容量与额度底座，官方设计文章给出了硬指标（https://x.ai/news/designing-grok-bot）：当时每个账号的实用上限大概是 50 个 Bot，每个群聊最多容纳 6 个；其中 50 个 Bot 的上限已在 9 月 1 日 v0.31.0 取消（"You can create more than 50 Bots"）（https://x.ai/changelog/bot；https://cursor.com/help/grok-bot/group-chats）。同时，在 v0.75.2（2026-10-22）中，官方将例行任务（Routine）的小时级执行配额大幅上调至**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots）、单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**，定时触发最小间隔仍为 5 分钟（https://cursor.com/help/grok-bot/routines；https://x.ai/changelog/bot）。在订阅与计费架构上，自 2026 年 10 月 18 日起，官方正式推出 **The X Subscription 三合一统一订阅**（https://cursor.com/help/grok-bot/plans；https://cursor.com/help/the-x-subscription/overview；https://x.com/bot/status/2110063783796572496），将 Grok、Cursor 与 X Premium 整合进同一套账单——其中 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 档位包含 Grok Bot（Free $0 与 Plus $8/月档位不含 Grok Bot），三端共享同一个**周额度池（one weekly usage pool）**，超出周额度池或调用非 Grok 第三方模型时从 `grok.com/dashboard/billing` 的 **Prepaid Credits（预付额度）** 中扣除；而既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及自助 Teams（$40/人/月）老订户只要不主动在 `cursor.com/unify` 或 `accounts.x.ai/unify` 切换，仍可保留原独立计划，但一旦单向切换至 The X Subscription 即不可逆退回（https://cursor.com/help/grok-bot/plans）。工具和技能是账号通用的公共资产，很多岗位都要用浏览器或邮件；记忆、例行任务、`Library` 页面和 `+alias` 邮箱路由则是专岗私有资产，只归属于具体的 Bot。官方建议设置职责明确的岗位，比如人才搜寻员（Talent Scout）、报销管家（Expense Manager）、Bug 复现员（Bug Reproduction），反对设通用助手（General Helper）这种缺乏目标约束的模糊角色（https://cursor.com/help/grok-bot/bots；https://cursor.com/docs/grok-bot/use-cases）。

| Bot 组成部分 | 核心载体与入口 | 作用域属性 | 2026-10 最新核心能力与边界（v0.71.2 – v0.75.5） |
| :--- | :--- | :--- | :--- |
| **1. 身份档案（Profile）** | 名称、头像、标签、`Description` | 单 Bot 专有 | 存放持久规则与 Vault `Hint` 匹配口令，严禁混放单次任务指令（https://cursor.com/help/grok-bot/bots） |
| **2. 工作记忆（Memory）** | `Bot info pane → Memory` | 单 Bot 专有 | 跨会话记录偏好与事实摘要；动态事实仍以源系统为准（https://cursor.com/help/grok-bot/bots） |
| **3. 独立工位与屏幕（Computer & Workspace）** | 云端沙箱 `/workspace`、浏览器会话、远程设备 | 账号共享底层 / 独立状态 | 支持 Status / Preview / Takeover 三层介入，可挂载常开 Mac mini 或本机住宅 IP 流量转发（https://cursor.com/docs/grok-bot/work） |
| **4. 对话时间线（Conversation）** | 1 对 1 聊天流、群聊（最多 6 个 Bot）、语音卡片 | 单 Bot / 群聊共享 | 支持 iPhone Action Button 一键实时语音并在挂断后自动沉淀完整逐字稿卡片（https://cursor.com/help/grok-bot/voice-chat） |
| **5. 专属资料库（Library）** | `Bot info pane → Library`（Pages / Canvas） | 单 Bot 维护 / 三级分享 | 沉淀实时更新的交互式报表、Activity Dashboard 与工具，支持 `Only you` / `Your team` / `Anyone with the link`（https://x.com/bot/status/2112991843235610885） |
| **6. 专属邮箱子别名簇（`+alias` Email）** | `mybot+tag@mail.grokbot.com` | 单 Bot 专有路由 | 按 `+alias` 后缀定向触发不同 Routine（全号 300 次/小时，单条 200 次/小时），转发保留完整 HTML、内嵌图与附件（https://cursor.com/help/grok-bot/agent-email） |

![Bot 结构解剖图（Profile、Memory、Computer 与 Conversation 边界）](../images/fig-05-1.png)

*图：Bot 结构解剖图（Profile、Memory、Computer 与 Conversation 边界）*
> [!NOTE]
> 📸 **截图位（待补）**：Bot 资料编辑弹窗（Edit Profile）与侧栏多 Bot 状态展示

## 5.2 岗位说明书五要素 · Job Description Method

翻看中文社区的讨论，很多人抱怨 Bot 乱跑、产出答非所问，根源在建 Bot 时随手敲了一句“你是一个厉害的技术助理，帮我打理日常一切事务”。例如中文社区创作者 `@Khazix0918`（数字生命卡兹克）在 2026 年 10 月 18 日的帖子中就曾吐槽裸用默认聊天窗口的痛点（https://x.com/Khazix0918/status/2111709708226797737，285 赞、54 书签），而开发者 `@object_nullll` 在架构解析回复中一针见血地指出（https://x.com/object_nullll/status/2111717423837778173）：Grok Bot 的对话层旨在收集上下文、对齐验收标准，并将重度任务根据岗位说明书与 Skill 委派给 Cloud Agents 或云电脑 CLI Workers，绝不能当成零约束的裸聊工具。

掘金开发者迷城在实测中提出过（https://juejin.cn/post/7682695577956483091）：建 Bot 必须给岗位说明书，不能只给一句提示词。一份合格的说明书必须包含**岗位说明书五要素**：身份与记忆、核心使命、关键规则、工作流程、成功指标。

超级峰在粉皮书第 6 课列过由技术总监、公关总监、社群运营、商务总监、增长黑客组成的五人舰队（https://chaojifeng.me/free-courses/grok/learn/basic-06），主要是按业务切分岗位。而在 2026 年 8 月 Cursor 并入 SpaceX SuperIntelligence 后工单暴增 175% 的实战中，官方客服团队同样按岗位说明书拆出了 **Intake Triage Bot（分诊接待）**、**Billing & Refund Bot（账单与退款）**、**Technical Repro Bot（技术复现）**、**Incident Batch Bot（事故批处理）** 与 **Product Feedback Synthesizer Bot（产品反馈聚类）** 五位专职同事，在零新增客服招聘的情况下将单票解决成本压至 $0.20–$0.30、实现 99% 退款全自动闭环（https://x.ai/news/grok-bot-customer-support）。要想让 Bot 稳定工作，官方采购 Haggle Bot 的真实系统提示是很好的参考（https://x.ai/news/grok-bot-procurement）：用 SYSTEMS 限定数据来源，用 PEOPLE 锁定决策汇报人，用 PERMISSION LINES 划分红黄绿三档权限边界（自主执行、必须人工审批、绝不触碰），用 WHAT GOOD LOOKS LIKE 直接给出好坏交付物的具体正反样例。

随着 v0.75.2 与 v0.75.5 相继推出 **1Password Brokered Sign-in**（https://cursor.com/help/grok-bot/connect-apps；https://x.com/bot/status/2113301060811161874）、**Grok Bot Vault 内置加密保险箱**（https://cursor.com/help/grok-bot/secrets；https://x.com/bot/status/2113754107861532677）以及 **Pages 实时画布**（https://x.com/bot/status/2112991843235610885），我们在编写岗位说明书的“第 3 要素：权限红线与审批边界”和“第 5 要素：交付物规范与成功指标”时，必须增补两项至关重要的现代治理条款：

1. **在“3. 权限红线与审批边界”中增补 Vault `Hint` 标签匹配规则与支付风控边界**：
   官方在 `Settings → Vault` 中支持集中保存三类加密只写（write-only）凭据：Logins（登录账号/密码/2FA）、Cards（信用卡/借记卡，支持手机摄像头扫卡或 5 MB CSV 批量导入）与 Contact info（收货地址/电话/邮箱），且每个条目均可填写一段明文 **`Hint`（提示标签）**（https://cursor.com/help/grok-bot/secrets）。Bot 永远无法读取明文卡号、CVV 或密码，仅能通过 `BrowserSecureFill` 工具自动填充，但 **Bot 可以读取明文 `Hint` 标签**。同时，官方技术文档明确定义了登录优先级（`已保存浏览器会话 → Vault → 1Password → 聊天内 Secure Form → 人工接管屏幕`）与结账支付优先级（`Vault → 聊天内 Secure Form → Link / X Money → 人工接管屏幕`）（https://cursor.com/docs/grok-bot/work）。
   因此，在多 Bot 团队中，必须在每个专职 Bot 的岗位说明书里写明 **Vault `Hint` 标签白名单匹配规则**——例如硬性规定差旅预订 Bot 仅允许调用 `Hint` 明确标注为 `"Use for work travel only"` 或 `"Corporate Amex"` 的卡片与航司账号，严禁触碰其他 `Hint` 条目。此外，根据官方安全文档（https://cursor.com/help/grok-bot/secrets）以及社区安全研究者 `@kial`（https://x.com/kial/status/2114201768414646280）与 `@JianWeiSignal`（见微｜Signal，https://x.com/JianWeiSignal/status/2114195530611855488）的重点提醒：**一旦将银行卡保存在 Vault 中，结账填充时不会触发单独的逐笔 Vault 弹窗确认**（仅受通用购买审批约束），若岗位要求每一笔消费都必须由人类亲手输入卡号逐单核准，岗位说明书应明确规定采用 `@martinpaulweiss` 提出的“一密一宅（One home per secret）”拆分法（https://x.com/martinpaulweiss/status/2114210343467536531），不在 Vault 常驻主力信用卡，改走聊天内单次 `Secure Form` 或 1Password 逐次生物识别审批（https://x.com/1Password/status/2113276767582498943）。（尽管 `@elonmusk` 已于 2026 年 10 月 15 日公开承诺如果 Grok Bot 代购出错或泄露银行卡，SpaceX 将全额赔付：https://x.com/elonmusk/status/2110610960474079445，但在岗位说明书层面做好 `Hint` 隔离依然是企业风控的第一道防线。）
2. **在“5. 交付物规范与成功指标”中增补专属 Page 看板维护与三级分享权限**：
   除了在对话流里输出 Markdown 表格，现在应当在岗位说明书中指定该 Bot 在其 `Library` 中长期维护一张专属的 **Page（Canvas 实时看板）**（https://x.com/bot/status/2112991843235610885），并明确规定该 Page 的更新时机与**三级分享权限（Sharing Permissions）**（https://cursor.com/docs/grok-bot/teams；https://x.ai/changelog/bot）：
   - **`Only you`（仅自己可见）**：适用于涉及个人财务、未公开人事评估或敏感机密的私有岗位看板；
   - **`Your team`（团队全员可见）**：适用于研发进度、客服队列或部门周报看板（Team 计划默认开启，管理员可在 `Dashboard → Grok Bot → Bot capabilities` 中统一管控团队内部 Page 共享策略，详见 https://cursor.com/docs/grok-bot/teams）；
   - **`Anyone with the link`（任何持有链接者可见）**：适用于对外公开的产品路线图、客户交付战报或社区开源榜单。
   例如开发者 `@melvindvivas`（Melvin Vivas）就为自己的幕僚长（Chief of Staff）Bot 制定了维护 `Activity Dashboard` 专属 Page 的交付规范（https://x.com/melvindvivas/status/2113676935956160882，获 1,087 赞、1,687 书签），将所有专职 Bot 的时间线（Timeline view）、进行中任务（Tasks in progress）、已完成任务（Completed tasks）和待人工审批事项（Items waiting for human approval）实时收口到一张看板上，并通过定时 Routine 自动刷新（https://x.com/melvindvivas/status/2113968491573514576），彻底终结了多 Bot 窗口切换的混乱。

我调研了官方做法和社区讨论，整理出这份通用的岗位说明书模板。新建 Bot 时，可以直接填空放进 Description 或初始化工作指引里：

```text
# 岗位说明书：[岗位名称]

## 1. 身份与使命 (Identity & Mission)
- 岗位身份：你是专门负责 [具体业务领域] 的专职执行者。
- 核心使命：端到端独立负责 [核心业务目标]，把凌乱的原始输入加工成可以直接交付的确定性产物。

## 2. 数据来源与工位 (Systems & Sources)
- 权威输入源：只从 [指定的系统/指定目录/特定网址/专属邮箱 +alias 后缀] 提取事实，绝不凭空推测未经验证的数据。
- 工具使用范围：仅允许使用 [指定工具名称或指定已连接插件]。

## 3. 权限红线与审批边界 (Permission Lines)
- 始终允许 (Always Allowed)：读取指定来源的数据、提取分析字段、在 /workspace 写入本地草稿文件、更新本岗位 Library 下的专属 Page。
- 凭据与 Vault Hint 匹配规则 (Vault & 1Password Policy)：当需要登录或结账填充时，严格按系统优先级调用，且仅允许匹配 Vault 中 Hint 标签为 "[例如：Use for work travel only]" 的登录项、卡片或收货地址；若需调用 1Password 凭据，必须发起 Brokered Sign-in 等待人类在 1Password App 内逐次批准。
- 必须报批 (Needs Approval)：向任何外部账号发送消息、提交工单、修改线上生产系统状态、涉及资金与采购决策。
- 绝不执行 (Never Allowed)：自行决定对外付款、调用 Hint 标签不匹配的 Vault 卡片/账号、越权触碰无关目录、绕过人工审批私自将草稿直接发布。

## 4. 标准作业流程 (Standard Operating Procedure)
- 第 1 步：接收输入并核查数据完整性，若缺少必要字段立即在回复中列出阻塞项。
- 第 2 步：比对既有规则与历史产物，按照既定结构完成分析与草稿编写。
- 第 3 步：自我检查，核对关键数字与原出处链接，标记出必须由人类核决的疑点。
- 第 4 步：输出最终交付物，同步热更新 Library 中的专属 Page 看板，并在末尾清晰说明下一步待办由谁承接。

## 5. 交付物规范与成功指标 (Deliverables & Metrics)
- 输出格式：必须使用固定的 Markdown 表格/结构化卡片，严格包含 [字段 A]、[字段 B] 与 [原始链接]。
- 专属 Page 看板与分享权限：在 Library 中持续维护名为《[看板名称]》的实时 Page（包含时间线、进行中、已完成与待审批四个模块），分享权限固定设置为 [Only you / Your team / Anyone with the link]。
- 成功标准：无捏造事实、无未经核实的数据源、Vault Hint 100% 精准匹配、高风险操作 100% 停留在待审批草稿状态。
```

我们可以对比正反两组实际案例。

正例参考了官方 Haggle Bot 的边界约束（https://x.ai/news/grok-bot-procurement）以及官方 Work 与 Teams 治理规范（https://cursor.com/docs/grok-bot/work；https://cursor.com/docs/grok-bot/teams），比如外联线索审查员与差旅采购专员：

```text
岗位名称：SaaS 采购线索审查员
核心使命：审查公司所有软件续约账单与闲置席位，找出潜在节省空间，生成结构化的议价建议清单。
数据源：仅读取管理后台导出的 CSV 报表、采购合同存档以及发往 procurement+invoices@mail.grokbot.com 的账单邮件，不采信非官方渠道的口头报价。
权限三档：
1. 始终允许：计算闲置率、标记 90 天未登录席位、在本地生成节省测算表、热更新 Library 中的《SaaS 续约审计看板》Page。
2. 必须报批：向供应商发起询价邮件、起草改签合同；如需登录供应商门户查账，仅允许调用 Vault 中 Hint 为 "SaaS Billing Read-Only" 的凭据或通过 1Password 逐次授权。
3. 绝不执行：直接点击取消订阅按钮、修改支付信用卡信息、触碰 Vault 中 Hint 为 "Use for work travel only" 或其他非本岗位的卡片。
交付规范：每条发现必须以 TODAY（现状）、SAVE（预计节省金额）、REC（操作建议）、NEXT（下一步谁确认）四段格式输出，且必须附带原合同到期日；同步更新专属 Page 看板，Page 分享权限设为 Your team（仅团队内部可见）。
```

再看反例：

```text
你是一个超级智能采购助手，请帮我盯着公司所有的日常开销。只要发现有贵的东西或者不划算的软件，就立刻帮我跟对方砍价，想尽一切办法替我省钱。每天向我汇报你的战果。
```

这个反例既没限定数据来源，也没给高危操作上锁。Bot 可能会把宣传页的折扣误当成真实合同条款，甚至自作主张直接给供应商发停约沟通邮件。只有把权限红线切成操作性语言，Bot 才能放心交付。

> [!NOTE]
> 📸 **截图位（待补）**：官方采购 Haggle Bot 的权限配置面板与 Profile 说明

## 5.3 先只建一个 · Start With One

新手容易一上来就建十几个 Bot，起各种头衔，想一口气组建管理舰队。

这种做法很容易失控。Grok Bot 团队核心工程师 @poteto（Lauren Tan）在社区里给新手提过忠告（团队成员，https://x.com/poteto/status/2108097362283597916）：**先只建一个** Bot，直到管理复杂度真正变高之前不要盲目拆分。@poteto 建议第一步先在设置里连上常用的真实 App（团队成员，https://x.com/poteto/status/2107830403549831186），比如日历、Slack、工单系统、CRM 和网盘，让这个 Bot 能接触到每天的真实数据源。

象鱼工作流也提过同样的建议（https://xiangyugongzuoliu.com/grokbot-use-cases/）：第一周别搞太复杂，三个角色就到管理上限了——一个总管、一个领域专家、一个可退回修改的质检官。如果一个 Bot 都没调教好，建太多只会陷入来回纠错的泥潭。

什么时候才该拆出第二个 Bot？官方文档总结了五个拆分条件（https://cursor.com/help/grok-bot/bots；https://cursor.com/docs/grok-bot/work）：

一个是业务领域或交付目标完全独立（Goal or area of ownership）。比如客服巡检和代码 Bug 复现，核心指标没有交集。

一个是依赖的底层工具与数据源截然不同（Set of tools and sources）。一个全在内部 CRM 和邮件里看数据，另一个需要终端权限和深度代码库集成，工具集割裂就该物理隔离。

一个是工作风格与交付调性不同（Working style）。对外沟通要严谨温和，内部工程报告要精简、只讲事实数据，混在一个 Bot 上容易口吻混乱。

一个是审批边界与安全红线存在天然落差（Approval boundary）。涉及花钱、改线上数据库或对外发信的高危岗位，必须独立并加人工审批门禁；只读公开数据的岗位可以放开自动化。

一个是周期性排程存在差异（Recurring schedule）。有的按工作日清晨定点巡检，有的靠外部 Webhook 触发或偶尔手动唤醒，调度节奏不同适合独立承载。值得注意的是，对于同一岗位下的细分邮件流（比如同时接收行业简报、发票通知与系统告警），现在无需为了区分触发源而强行拆出多个 Bot——直接利用 v0.71.2 上线的 `+alias` 邮箱子别名（https://x.com/SamSokolin/status/2110496237241667621；https://cursor.com/help/grok-bot/agent-email），在同一个专职 Bot 下用不同后缀绑定不同的 Routine 即可保持架构精简。

分出专岗后，多 Bot 组织形态会演化为总监协调（Chief of Staff）模式。SpaceXAI 团队的 Roman Ugarte 在播客里提到（团队成员，https://www.youtube.com/watch?v=maSdsTLaMuU）：Chief of Staff 模式不是一开始刻意规划出来的，而是内测第二周自然长出来的机制。大家发现有三四个专岗后，自己在不同窗口间来回复制粘贴特别痛苦，于是自发把第一个 Bot 提拔成幕僚长，人只对总监下达大目标，由总监去负责拆解任务、分给具体专家并跟踪进度。在社区实战中，这种架构得到了广泛印证：例如中文创作者 `@CyberAlice3269`（夏哥研究室）搭建了“1 个 CEO Bot + 5 个专职 Bot（情报搜集、选题策划、初稿撰写、审校润色、配图制作）”的自媒体工作室（https://x.com/CyberAlice3269/status/2112098767151468645）；英文创作者 `@milesdeutscher` 在其获 3,100 赞、4,503 书签的深度长推中展示了“1 个主控编排 Bot + 10+ 细分领域 Bot”的 Grok Swarms 蜂群架构（https://x.com/milesdeutscher/status/2113653680834859262；https://x.com/milesdeutscher/status/2113653818651189419）；而 `@melvindvivas` 则让 Chief of Staff Bot 通过维护一张全局 `Activity Dashboard` Page 看板来统一汇总所有下属 Bot 的实时进度与待审批卡片（https://x.com/melvindvivas/status/2113676935956160882）。

多 Bot 协作时，官方群聊（Group Chat）是公开交接的载体（https://cursor.com/help/grok-bot/group-chats；https://cursor.com/docs/grok-bot/teams）。群聊上限是 6 个 Bot。不过群聊不是让它们互相附和聊天，每一条分派出去的任务，在群里必须且只能明确点名唯一一位当前交付负责人。

> [!NOTE]
> 📸 **截图位（待补）**：在群聊中通过 @ 呼叫特定 Bot 进行任务交接

## 5.4 记忆与纠错 · Memory & Corrections

刚建好的 Bot 不可能一上来就完美。很多人容易把没调教好的 Bot 直接挂上定时任务通宵裸跑，第二天醒来额度烧光，还留下一堆错误数据。尤其在切换至 **The X Subscription**（https://cursor.com/help/grok-bot/plans）后，由于 Grok Bot、Grok App 与 Cursor IDE 三端共用同一个周额度池，正如社区用户 `@charlie_pmp` 在复盘中所指出的（https://x.com/charlie_pmp/status/2114214503416271131），未经调教精简就高频挂起的冗余 Routine 是后台静默消耗周额度的头号元凶。

V2EX 用户 @zhuyinan 在对比本地部署的 Hermes 框架与 Grok Bot 时，分享过一套人工培养经验（https://www.v2ex.com/t/1240012）。他总结出了**养 Bot 的三阶段曲线**：

第一阶段是人工带跑期。刚开始 Bot 完成度通常只有 30% 到 40%，漏洞很多。千万别放手让它自动跑，先带它人肉跑 3 到 5 轮。理解偏了、格式错了、事实漏了，当场在对话里揪出来纠偏。

第二阶段是成熟期。持续纠错几轮后，独立完成度能到 70% 左右。它基本记住了核心偏好：报告用几级标题、表格留哪几列、文案坚决不能出现哪些行业词汇。这时候只要花很少时间微调边角细节。

第三阶段才是挂排程。前面的边缘瑕疵修完、不同输入下的测试都能稳定过关，再正式挂 Routine 自动调度，让它在无人值守的深夜或清晨自行运转。把顺序搞反容易失控。

培养和纠错过程中有两个实用技巧。

一个是明确下达记忆口令。纠正错误时别只说“改一下”，要加上一句“记住这条规则”（https://www.v2ex.com/t/1240012）。带明确记忆指令的纠正会被系统存入 Memory 模块，在后续任务中持续生效。

一个是建立严密的回查闭环。社区实践者 Michael Fenech 提出过纠错准则（https://x.com/Michael_Fenech_/status/2106729045878514147）：纠偏（Correction）必须触发源系统核验（source check），最后才允许给出答案（answer）。指出会议时间或账单金额算错时，严禁让它凭空猜，必须命令它重新打开原始日历、重读邮件或重查 CRM 系统。不回查事实依据的直接认错，只是在用第二段幻觉掩盖第一段幻觉。

觉醒AI 团队在媒体工作流实战中也给过工程建议（https://www.jxxy.net/ai/articles/grok-bot-workflow-training/）：别只信口头上的“记下了”，真正重要的业务调性、规则说明和交付标准，要让 Bot 写成 Markdown 文件存到 /workspace/learn/*.md 目录下。规则落盘成实体文件，后续运行能溯源对比，上下文才不会随着对话轮次变多而漂移。与此同时，中文社区深度实践者 `@eze_is_1`（一泽Eze）在其获 351 赞、705 书签的 10 条实战心得长文中特别提醒了**“防臃肿法则”**（https://x.com/eze_is_1/status/2109850538045264151；https://x.com/eze_is_1/status/2109852993982206425）：当你允许 Bot 在日常复盘纠错中自动迭代更新自己的 Skill 或规则文件时，随着时间推移，文件很容易越写越长甚至出现前后矛盾的补丁指令；因此必须定期让 Bot 对自迭代的规则文件执行精简合并与冲突清理，保持 SOP 干净正交。

官方文档在记忆机制上也划出了安全红线（https://cursor.com/help/grok-bot/bots；https://cursor.com/docs/grok-bot/work）：动态变化的事实永远以源系统为准；过时的假设必须在对话或资料页手动删除；涉及权限和安全底线的规则，必须白纸黑字写进 Profile Description，不能依赖动态记忆。

> [!NOTE]
> 📸 **截图位（待补）**：Bot 记忆面板（Memory）中的已学偏好与手动删除入口

## 5.5 模板与分享 · Templates

把一个 Bot 打磨成执行稳定、规则严密的数字员工后，如果想分享给团队伙伴或发到社区，可以用模板（Templates）系统。

官方工程师 Matt Palmer 在指南文档里打过一个比方（https://x.ai/bot/guides/templates-for-grok-bot）：模板是**食谱而非做好的饭菜**（Think recipe, not meal）。别人导入模板时，拿到的是搭建员工的设计蓝图与配方，不是把你本地烧好的实体原样搬走。

正因为是蓝图而非克隆体，分享前必须搞清楚系统到底打包带走了什么，又留下了什么。

模板会打包带走的内容包括（https://x.ai/bot/guides/templates-for-grok-bot；https://cursor.com/help/grok-bot/bots）：身份设定（名字、头像、标签与 Description）、默认排除个人/内部信息后的通用记忆、Skills、Routines，以及插件清单（接收方需要自己重新安装和授权插件）。

模板绝不会带走的内容包括（https://x.ai/bot/guides/templates-for-grok-bot；https://cursor.com/docs/grok-bot/teams）：个人的私有敏感记忆与内部细节、个人云电脑环境与本地工作区磁盘文件、浏览器里保存的网站登录状态与 Cookie、存储在 `Settings → Vault` 或 1Password 中的任何加密机密与卡片、自己编写的私有脚本与非标准工具代码（如自定义 MCP 服务器）、你的电脑与登录态、过往的私聊对话历史。**但要注意**：公开链接会展示 Bot 的身份、Description、Skills 和 Routines，官方明确要求分享前自行删掉 API Key、内部 URL、客户数据——如果你把密钥写进了 Description 或 Skill，它会跟着模板公开出去（https://cursor.com/help/grok-bot/bots）。

分享操作很直观。按现行文档，打开对话顶部的 Share 菜单，选 **Create template**（Matt Palmer 的指南截图里是旧版 Bot 设置右下角的 Share as Template 按钮，9 月 18 日起模板项移到了 Share 菜单（https://x.ai/changelog/bot））。然后选择范围：Enterprise 计划默认“Team-only”（仅团队成员可打开，详见官方团队治理文档 https://cursor.com/docs/grok-bot/teams）；其他账号默认“Public link”（任何拿到链接的人都能打开）。准备好后复制带 x.ai 域名的分享链接（https://cursor.com/help/grok-bot/bots；https://x.ai/bot/guides/templates-for-grok-bot）。

在浏览器中打开链接，能在 x.ai 看到包含角色说明、技能清单和所需插件的预览详情页。点击“Add to Grok Bot”后，客户端会在接收者账号下新建一个纯净的 Bot 副本。使用第三方分享模板受官方第三方 Bot 分享条款管辖（https://x.ai/legal/bot-sharing-terms）。

发布前必须做好防泄密审查。超级峰在粉皮书 field-01 中强调过（https://chaojifeng.me/free-courses/grok/learn/field-01）：按下发布按钮前，把资料当成全网公开的文件逐字通读一遍。仔细排查 Description 和技能草稿里有没有真实大客户名称、内部私有内网域名、个人私人邮箱、本地硬盘绝对路径，或者透露未公开项目的例行任务标题。一旦发现，必须彻底抹除后再发布。

接收方安装模板后也要注意：因为密钥和浏览器登录态被彻底隔离，新落地的 Bot 副本没法直接开跑。如果模板依赖特定业务系统或特定 API Key，接收方必须按岗位说明书要求，在自己客户端里重新完成连接器授权与凭据录入，Bot 才能真正开工。

跨账号复制模板时，依赖的插件、脚本和授权如何提示。

为了直观展示社区如何利用 Templates 机制沉淀高复用度的专职数字员工，我们可以拆解 2026 年 10 月下旬 X 社区涌现的三个标杆级可分享 Bot 模板与元岗位设计：

### 实例 1：`@LisaMAUSA` 的 **Vault Tidy（保险箱去重清理员）** 与 **SceneEdit Video Studio（单镜头局部修补工作室）** 双模板
在 Cursor / Grok Bot 开发者体验副总裁 Lee Robinson（`@leerob`）于 2026 年 10 月 24 日发起的 $100 X Money 真实反馈与最佳用例悬赏主帖（https://x.com/leerob/status/2113792409448714468，获 4,296 赞、985 书签）下，创作者 `@LisaMAUSA` 于 10 月 25 日分享了两个针对 v0.71.2 与 v0.75.5 新特性的高实用度可复用 Bot 模板（https://x.com/LisaMAUSA/status/2114208018388643852）：

1. **Vault Tidy（保险箱整理与去重专员）**：
   - **解决痛点**：许多用户在通过 `Settings → Vault → Import` 批量导入来自 Chrome、Safari、1Password 或 Bitwarden 的 CSV 密码文件（上限 5 MB，https://cursor.com/help/grok-bot/secrets）后，经常会遇到同一个网站存在三四个历史旧账号、过期银行卡与未标注 `Hint` 的混乱条目，导致业务 Bot 在自动填充时选错账号。
   - **模板设计亮点**：`Vault Tidy` 模板内置了一套严密的安全巡检 SOP——它绝不尝试读取或套取任何只写（write-only）密码与卡号明文，而是专门扫描已存条目的站点域名、用户名与明文 `Hint` 标签，自动识别重复登录项、缺失 `Hint` 用途标签的裸条目以及疑似过期的旧条目，并在 `Library` 中生成一份结构化的《Vault 卫生审计清单》Page，指导人类一键归并去重、补全规范化的 `Hint` 标签。
2. **SceneEdit Video Studio（单镜头无损局部修补视频工作室）**：
   - **解决痛点**：自 v0.71.2 引入 Grok Imagine 原生视频生成与代码动效渲染（https://x.com/bot/status/2110566041772617908；https://x.com/bot/status/2110772748805194127）以来，创作者在合成一段 30 秒或 60 秒的多镜头 MP4 短片后，如果只对其中第 3 个镜头的画面或字幕不满意，传统做法往往需要把整条视频推倒重渲，既耗时又白白消耗 The X Subscription 的周额度池。
   - **模板设计亮点**：`SceneEdit Video Studio` 模板将视频生产流拆解为按镜头编号归档的模块化工程（`/workspace/studio/scenes/scene_01.mp4` ... `scene_N.mp4`）。当你对成片中的某一个特定镜头提出修改意见时，该 Bot 仅针对目标单镜头调用 Grok Imagine 或 Remotion 重新生成局部片段，随后使用云电脑内的 FFmpeg 进行毫秒级无损拼接替换，无需重新渲染整支 MP4 视频。

### 实例 2：`@kaelanyiu` 的 **Meta-Evaluator Bot（模型评测与动态指派元 Bot）** 岗位设计
除了面向具体业务的干活型 Bot，社区开发者 `@kaelanyiu`（Kaelan Yiu）在 2026 年 10 月 25 日分享了一种极具前瞻性的“管 Bot 的元 Bot（Meta-Bot）”岗位架构——**Meta-Evaluator Bot（模型评测官）**（https://x.com/kaelanyiu/status/2114213605566742884）：

- **核心设计逻辑**：在多 Bot 协同舰队中，许多重度执行类 Worker Bots 会在云电脑沙箱内通过 CLI 调用不同底层大模型来干活（例如调用本地/云端 CLI Agent 处理代码重构、数据清洗或长文写作）。然而各大前沿模型的版本迭代与性价比变化极快，手动去改每个 Worker Bot 的模型配置既繁琐又主观。
- **自动化优胜劣汰闭环**：`@kaelanyiu` 专门设立了一位定时运行的 **Meta-Evaluator Bot**，挂载每隔几天自动触发一次的 Routine。每次唤醒后，这位“评测官”会自动拉取你真实业务场景下的标准测试集（Benchmark Prompts），对当前主流前沿模型跑一轮盲测打分（综合评估准确率、耗时与成本），随后直接根据最新跑分结果，**动态修改 `/workspace` 下其他干活 Worker Bots 在未来几天内通过 CLI 调用的默认模型配置文件**，并将本轮评测排行榜同步更新到 `Library` 的专属 Page 看板上。如果您希望把这一岗位直接导入自己的团队，可以参考以下可直接复用的模板蓝图：

```text
# 岗位说明书：Meta-Evaluator Bot（模型评测与动态路由官）

## 1. 身份与使命 (Identity & Mission)
- 岗位身份：你是团队内部的 AI 模型基准评测官与 CLI 模型路由调度员（参考 @kaelanyiu 架构范式）。
- 核心使命：每隔 72 小时对候选大模型运行一次真实业务基准测试，根据综合得分动态更新其他 Worker Bots 的 CLI 模型配置文件，确保全队始终使用当前性价比与准确率最优的模型组合。

## 2. 数据来源与工位 (Systems & Sources)
- 权威输入源：读取 `/workspace/eval/benchmarks/` 下的黄金测试集与评分标准，以及各模型官方发布日志。
- 配置文件目录：具备 `/workspace/config/worker_models.json` 的读写权限（供其他 Worker Bots 在 CLI 启动时读取）。

## 3. 权限红线与审批边界 (Permission Lines)
- 始终允许：运行 `/workspace/eval/run_eval.py < /dev/null` 非交互式评测脚本、统计延迟与得分、更新 Library 中的《模型跑分与路由看板》Page。
- 必须报批：当单次评测预估消耗超过预设 Credits 阈值，或拟将核心生产 Worker Bot 切换至未经历史验证的新发布模型家族时，必须先在聊天流发起审批卡片。
- 绝不执行：修改 Worker Bots 的核心业务安全红线（Profile Description）或触碰 Vault 中的任何支付与个人凭据。

## 4. 标准作业流程 (Standard Operating Procedure)
- 第 1 步：按 Routine 定时唤醒，读取黄金测试集（涵盖代码修复、结构化提取、双语文案三类任务）。
- 第 2 步：通过 CLI 批量执行评测（命令末尾强制追加 `< /dev/null` 防止非交互式 Shell 挂起），记录各候选模型的得分、耗时与 Token 消耗。
- 第 3 步：生成本周期最优模型映射表，写入 `/workspace/config/worker_models.json`。
- 第 4 步：热更新 Library 中的专属 Page（权限设为 Your team），并在对话流输出变更摘要。
```

> [!NOTE]
> 📸 **截图位（待补）**：Share as Template 预览详情页（显示包含的 Memory、Skills 与 Plugins 清单）


# §06 云电脑：它的工位 · The Computer

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

![一台云电脑下共享浏览器会话、/workspace、终端凭据与多 Bot 独立工作屏幕的架构示意](../images/fig-06-1.png)

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

![桌面端到云电脑的双路网络与本地出口代理路由拓扑](../images/fig-06-2.png)

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


# §07 Skill 与 Routine：教一次，让它照着做 · Skills & Routines

很多新手刚接触 Grok Bot，容易把它当普通网页聊天框用。每次想干活，都重新敲一遍提示词，输出格式次次参差不齐。还有人把随手写的提示词直接挂成定时任务，跑了几天，额度烧掉一大截，收件箱里全是毫无价值的垃圾信息。

想让 Bot 真正变成可靠的数字同事，得搞懂它的两层自动化构件：Skill 和 Routine。假设你翻完文档和社区讨论就会明白，教它做事和让它定时跑，在底层是两套完全不同的逻辑。

## 7.1 两者的区别 · How vs When

按官方文档的架构设计，**Skill 是解决怎么做（How）的方法库，而 Routine 是规定何时由谁来跑（When）的排期表**（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。很多人容易把这两个概念搞混。

Skill 是一套可复用的操作指令集。它记录了具体任务的步骤、分支判断、交付格式以及安全审批红线。你教出来的 Skill 不属于某一个具体的 Bot，而是保存在整个账户的私有技能库里。你在 Bot A 这里保存的技能，只要挂载了对应的连接器或网页登录态，Bot B 也能直接调。在桌面客户端输入框里，按 `/` 键就能检索并插入已存的 Skill；按 `@` 键用来找具体的 Bot、群聊、Routine 或连接器（https://cursor.com/help/grok-bot/skills-routines-and-automations）。（时效提醒：10 月 7 日 v0.68.1 起 `/` 不再弹出技能菜单，可以直接用文字点名 Skill，见 §03（https://x.ai/changelog/bot）。）要是快捷菜单里没看到某个 Skill，可以去侧边栏的 Marketplace，进插件和技能管理页面，看它在不在 Private skills 列表里（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

Routine 是一张具体的排期委派单。它必须绑定一个明确的负责 Bot，还要设定执行时间表或事件触发源（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。一个 Routine 本质上就是对 Bot 说：在指定时刻，调某项 Skill 去处理当前数据，再把结果推到指定位置。

![Skill 与 Routine 的职责边界与调用关系](../images/fig-07-1.png)

*图：Skill 与 Routine 的职责边界与调用关系*

早期社区里 Kin 的《Grok Bot 橙皮书》有句口号叫“示范一遍它学一辈子”（https://github.com/KinGao294/grok-bot-orange-book）。这句宣传语把不少新手带偏了，以为让 AI 看一次屏幕动作就能应付真实世界的所有变化。官方文档专门纠偏过：演示录制生成的产物只是一份“草稿技能（draft skill）”（https://cursor.com/help/grok-bot/skills-routines-and-automations）。拿到初稿后，必须手动补充判断规则、容错策略和审批卡点，并在安全数据上跑通测试，才能交给 Routine 定期跑（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

## 7.2 Teach a task 录制 · Teach by Demo

要是网页操作步骤太繁琐，逐字写提示词得敲上千字，这时候可以用电脑视图里的 Teach a task 功能（https://cursor.com/help/grok-bot/skills-routines-and-automations）。这功能不是让你当甩手掌柜，而是靠录屏快速抓取一套技能骨架。

录制步骤很直接。在桌面端打开单聊窗口，切到云电脑屏幕视图，点击 Teach a task（https://cursor.com/help/grok-bot/skills-routines-and-automations）。系统会先让你用文字写明目标，接着你在云电脑浏览器里把业务完整操作一遍（https://cursor.com/help/grok-bot/skills-routines-and-automations）。演示完点击停止，Bot 就会根据屏幕动作，自动整理出一份草稿 Skill（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

这里有两条死规则。第一，单次录制最多 10 分钟（https://cursor.com/help/grok-bot/skills-routines-and-automations），超时自动截断。第二，录制只看屏幕画面，完全不录麦克风声音（https://cursor.com/help/grok-bot/skills-routines-and-automations），不用对着电脑自言自语。在官方 101 直播里，讲师演示了让 Bot 学会搭建 Google 表单并发布。官方强调，把演示固化成技能核心是为了省 token（tokenomics），省得 Bot 每次执行类似任务都在原始 HTML 页面里盲目试错（https://www.youtube.com/watch?v=8xXhE25vJZY 与 https://cursor.com/help/grok-bot/skills-routines-and-automations）。

假设你细读官方规范就会发现，安全是录制时必须卡死的底线。屏幕画面会被模型逐帧读取并写入技能说明，绝对不能在录屏期间明文输入密码、二次验证码或银行卡号（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/secrets）。遇到敏感凭据，必须走系统的凭据交接流程（https://cursor.com/help/grok-bot/skills-routines-and-automations），例如通过 v0.75.2 上线的 1Password Brokered Sign-in 逐次授权（https://cursor.com/help/grok-bot/connect-apps）或 v0.75.5 上线的内置 Grok Bot Vault 安全填充（https://cursor.com/help/grok-bot/secrets）。

> [!NOTE]
> 📸 **截图位（待补）**：Teach a task 录制界面与生成的草稿技能面板

社区有人试过对同一个流程连录 3 次让 Bot 取平均值（https://x.com/B_doong2daddy/status/2100573792569303402），但官方没支持过这种做法（https://cursor.com/help/grok-bot/skills-routines-and-automations），效果也没经验证。核心问题在于，**录制生成的技能永远只是一份未经打磨的初稿**（https://cursor.com/help/grok-bot/skills-routines-and-automations）。演示走的只是理想路径，真实环境里经常遇到加载超时、弹窗拦截或空数据。拿草稿直接去排期，一旦撞上预期外的变化，Bot 很容易卡死或乱点。

另外，Teach a task 属于分批灰度功能（https://cursor.com/help/grok-bot/skills-routines-and-automations）。要是你的电脑视图里还没这个按钮，不用慌。直接指挥 Bot 手动跑通一次单次任务，然后在对话里让它把刚才成功的流程、数据源和格式规则提取保存为私有技能（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

录制中出现误操作时，生成的 Skill 草稿是否会保留无效步骤。

## 7.3 从一次任务到 Routine 的六步 · Task → Fix → Skill → Test → Routine

不少人抱怨 Bot 经常失控，根子就在于跳过了中间的质检环节。社区实践者总结过一句话：**绝不能直接从随手写的一句提示词直接跳到例行排期（Prompt → Routine）**（https://x.com/Michael_Fenech_/status/2106352565528977469）。官方核心团队接受采访时也强调，正确的路线永远是先看单次任务，再沉淀成技能，建立了信任最后才做自动化排期（https://www.youtube.com/watch?v=xZ5TEaleUdg 与 https://cursor.com/help/grok-bot/routines）。

按官方工作流指南（https://cursor.com/docs/grok-bot/work）和社区经验（https://x.com/Michael_Fenech_/status/2106352565528977469），搞定一条稳固的例行工作流要走完六步：

1. 手动跑通单次真实任务（Task）。拿当下的真数据当输入，别捏造假例子。在对话框里一步步发指令，确认 Bot 具备任务所需的网页权限、登录态或插件连接（https://x.com/Michael_Fenech_/status/2106352565528977469）。
2. 现场纠偏（Fix）。单次跑几乎总会暴露出问题，比如抓了旧数据、漏了字段，或者输出冗长套话。在这个阶段改指令、对标准、调格式，直到它能稳定产出满意的结果（https://x.com/Michael_Fenech_/status/2106352565528977469）。
3. 存为技能（Skill）。对完成任务的 Bot 说：“把我们刚刚使用的流程保存为名为 [技能名称] 的技能”。在提示词里列清楚触发场景、依赖数据源、操作步骤、校验方法，以及必须人工审批的边界（https://cursor.com/help/grok-bot/skills-routines-and-automations）。
4. 换第二份真数据测试（Test a second input）。这一步最容易刷掉劣质技能。只在一个特定输入上跑通就急着封装，存下来的只是针对单次历史的作弊条（https://x.com/Michael_Fenech_/status/2106352565528977469）。换一组参数或不同日期的输入再跑一次，确保流程稳定。
5. 定义失败策略（Define failure）。把异常处理写死在指令里：数据源连不上怎么办？没查到新数据怎么办？中间某步失败是直接终止还是汇报部分进度？涉及对外发送、删数据或付款的操作，有没有锁进审批卡（https://cursor.com/help/grok-bot/skills-routines-and-automations）？
6. 绑定排期并用测试运行复核（Routine & Test run）。在负责该任务的 Bot 对话框里，设好时区、排期频次与执行规则，启用后仔细对一遍历史记录（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。

![从单次任务演进到稳定 Routine 的六步闭环](../images/fig-07-2.png)

*图：从单次任务演进到稳定 Routine 的六步闭环*

看社区里 Rowan Cheung 分享的日常监控工作流（https://x.com/rowancheung/status/2108328114552000842），以及 `@milesdeutscher`（Miles Deutscher）在 3,100 赞、4,503 书签的“10 大逆天 Grok Bot 用例”长推中拆解的 **Competitor Monitor（竞品全天候雷达）** 与 **Morning Brief Routine（全渠道晨间情报简报）**（[https://x.com/milesdeutscher/status/2113653680834859262](https://x.com/milesdeutscher/status/2113653680834859262)、[https://x.com/milesdeutscher/status/2113653726217195817](https://x.com/milesdeutscher/status/2113653726217195817)、[https://x.com/milesdeutscher/status/2113653803304296498](https://x.com/milesdeutscher/status/2113653803304296498)），一条及格的 Routine 提示词在结构上必须严密闭环，时间、时区、数据范围、过滤规则、输出格式、禁止项和失败处理都得写全。这是一份可以直接参考的模板：

```text
Every weekday at 9:00 AM in Asia/Shanghai time zone, run the Competitor Product Updates skill against our target list in /workspace/competitors.md.

Look back strictly within the last 24 hours. Catch only three categories of updates:
1. Pricing or plan structure changes.
2. New feature launches or deprecations.
3. Outages, security incidents, or policy updates.

Ignore routine marketing campaigns, hype threads, promotional discounts, and generic reposts. 
Return at most 5 items. For each item, provide:
- Competitor name
- Change category
- Direct source URL
- One-sentence neutral summary of what changed
- Potential impact on our product (High, Medium, Low)

Post the summary directly in this conversation. 
Never post, comment, send email, or contact anyone externally. 
If the source data cannot be retrieved or the network fails, post an explicit error notification stating which source failed, and stop immediately. Never use outdated cache or hallucinate placeholder data. 
If no qualifying updates occurred in the last 24 hours, post exactly one line: "No qualifying competitor updates in the last 24 hours."

Save this as a routine.
```

### 进阶维护法则：防止自迭代 Skill 臃肿自相矛盾与路由熔断

当你的 Skill 库和 Routine 跑过几周之后，往往会遇到两个隐蔽的工程陷阱：**Skill 自我膨胀**与**异常死循环重试**。

中文社区创作者 `@eze_is_1`（一泽Eze）在收获 351 赞、705 书签的万字实战总结帖中，重点提出了 **“防止自迭代 Skill 臃肿与自相矛盾”** 的维护法则（[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151) 及系列进阶帖 [https://x.com/eze_is_1/status/2109852993982206425](https://x.com/eze_is_1/status/2109852993982206425)、[https://x.com/eze_is_1/status/2110532874000879886](https://x.com/eze_is_1/status/2110532874000879886)）。很多深度用户喜欢在提示词末尾加一句“每次执行完毕后，把遇到的新问题和经验自动追加写进 Skill 文件实现自我进化”。`@eze_is_1` 指出，如果不加人工约束地放任 Bot 自迭代更新 Skill，不出半个月，原本几百字的清爽 SOP 就会像滚雪球一样膨胀到几千字，里面塞满针对某次偶发网络抖动的临时补丁，甚至出现第 3 条规则要求“精简输出不超 100 字”、第 18 条补丁却要求“完整列出所有原始 JSON 字段”的自相矛盾指令，导致模型推理注意力涣散、执行稳定性断崖式下跌。

与此同时，`@AIShovelLab` 在梳理 Grok Bot 与 Claude Code / Codex 六大核心联动范式时，特别强调了 **“用路由 Skill 阻止盲目重试”** 的实战技巧（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）。当 Bot 在执行 Routine 遇到反爬拦截、接口 403 或 CLI 命令报错时，默认本能往往是在同一个会话里反复换姿势重试 5 到 10 次，不仅单次运行就把周额度烧出大窟窿，还可能触发目标站点的封号风控。通过在顶层挂载一个专门的“路由与熔断 Skill（Router & Circuit-Breaker Skill）”，强制规定每类任务的首选通道、降级备选通道以及“同源错误最多重试 1 次即熔断挂起”的硬规则，就能彻底根治盲目重试。

你可以把下面这份融合了 `@eze_is_1` 防臃肿压缩规则与 `@AIShovelLab` 路由熔断机制的治理模板直接写进你的核心 Skill 中：

```markdown
# Skill 治理与路由熔断规范 (Router & Anti-Bloat Guardrails)

## 1. 任务路由与重试熔断规则（参考 @AIShovelLab 范式）
- **优先确定性通道**：能用云电脑本地 Python/Bash 脚本或官方连接器（MCP）解决的数据读取，严禁拉起完整云端 GUI 浏览器去翻页。
- **单次重试熔断（Max Retry = 1）**：
  - 遇到 HTTP 401/403/429、验证码拦截（Captcha）或登录态失效时，**严禁在原通道连续重试超过 1 次**。
  - 若开启本机住宅 IP 转发（`Route traffic through this computer`）后仍失败，立即中止当前 Routine，输出一行结构化故障原因并挂起等待人工介入。

## 2. 自迭代 Skill 防臃肿与冲突清理法则（参考 @eze_is_1 范式）
- **禁止无脑追加（No Blind Append）**：当需要把新踩坑经验更新进本 Skill 时，严禁直接在文件末尾机械追加 `Patch #N` 段落。
- **同位替换与合并**：新规则必须合并进既有的步骤章节中；若新规则与旧规则冲突，必须直接覆写删除旧表述，确保整份 Skill 内部零逻辑矛盾。
- **行数硬上限（Max 120 Lines）**：本 Skill 正文总行数严格控制在 120 行以内。每新增 1 条规则，必须审视并精简掉过时的冗余描述，保持 SOP 正交干净。
```

此外，自 v0.75.2 上线 **Pages（Canvas）** 实时交互文档与看板能力后（https://x.ai/changelog/bot 与 [https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)），Routine 的最终交付物不再局限于往聊天窗口发一条死板的消息。例如社区开发者 `@melvindvivas`（Melvin Vivas）为其 Chief of Staff（幕僚长）Bot 配置了一条定时自动刷新 Routine，每隔固定周期巡检麾下所有专职 Bot 的工作进度，并自动热更新一张名为 `Grok Bot Activity Dashboard` 的实时 Page 看板（涵盖时间线视图、进行中任务、已完成任务与待人工审批事项）（[https://x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882) 与 [https://x.com/melvindvivas/status/2113968491573514576](https://x.com/melvindvivas/status/2113968491573514576)）。而 `@sisiliu517` 则利用小时级 Routine 配合中美时差策略——白天时段自动主攻中文 X 圈层互动与发帖，夜间时段自动切换为英文 X 圈层运营，并在每晚自动汇总互动分析报告反哺次日选题（[https://x.com/sisiliu517/status/2110869965612183642](https://x.com/sisiliu517/status/2110869965612183642)）。

## 7.4 硬限制 · Limits

搭 Routine 前，官方设下的硬限制要先摸清（https://cursor.com/help/grok-bot/routines），不然任务容易莫名中断，甚至丢数据。

每个 Bot 最多建 50 个 Routine（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。一个 Bot 的任务数量要是逼近上限，说明职责没拆开，得按业务线新开专职 Bot（https://x.com/Michael_Fenech_/status/2105697750645977298）。

在运行频率配额上，2026 年 10 月 22 日发布的 **v0.75.2 版本**对小时级运行频率上限做了重大上调（https://x.ai/changelog/bot）。根据官方最新 Routines 文档标准（https://cursor.com/help/grok-bot/routines），当前的小时级触发与运行硬上限为：
- **全账号所有 Bot 合计最高 300 次/小时（300 runs per hour across all Bots）**；
- **单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**。

这一配额提升主要是为了支撑高频 Webhook 事件触发、邮件子别名分流以及多 Bot 团队并发协作场景（https://cursor.com/help/grok-bot/routines）。但需要注意，对于按固定时间表循环的定时排期（Scheduled Routines），触发间隔依然至少要 5 分钟（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines），系统不支持低于 5 分钟的高频定时轮询。轮询太密只会白白耗尽周额度，还给目标服务器造成不必要的压力。

系统对运行历史很克制。每个 Routine 只保留最近 20 条运行记录（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。遇到连续报错，早期的记录很快就会被顶掉。要想做长期复盘，必须在 Skill 里让 Bot 把产出写进云电脑本地文件，或者持续写入一张固定沉淀在右侧信息栏 `Library` 里的 Page 看板中（https://x.ai/changelog/bot），别指望界面的日志面板。

在面板里点删除 Routine 是立即生效的，没有撤销（undo）功能（https://cursor.com/help/grok-bot/skills-routines-and-automations）。更要注意的是，在主界面直接删掉某个 Bot，它名下的所有 Routine 会一起被清空（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

很多新手刚建好 Routine，顺手就点 Test run 想试试水，以为这只是沙盒演练。官方文档特意警告过：**测试运行会产生真实的网页点击、文件改动和接口调用，绝对不是无害的沙盒模拟**（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。如果流程里有发消息、改生产文件或付款的操作，又没配审批卡，一点 Test run 就会直接把操作打到外部生产环境里。

为了防止用户离线时后台空转烧额度，系统有无人值守防护。长时间没动客户端，Grok Bot 可能会弹窗问你要不要继续维持后台任务；如果在设定时间内没回复，系统会自动暂停这些 Routine（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。重新打开客户端时，记得去 Bot 详情页看一眼有没有被暂停的任务，手动点恢复。

> [!NOTE]
> 📸 **截图位（待补）**：Bot 的 Routines 管理面板与运行历史记录

另外，按官方安全规则，Routine 或后台任务发起的审批卡片，等大概 10 分钟没人理就会变 Expired（已过期），操作直接作废（https://cursor.com/help/grok-bot/approvals-security-and-privacy 与 https://cursor.com/docs/grok-bot/security）。合上笔记本电脑，云电脑上的排期照样在云端跑（https://cursor.com/help/grok-bot/faqs），但关键步骤卡在审批上、你 10 分钟内没点通过，整个任务链就会停在那里。（注：v0.75.2 优化了 Auto-review 审批逻辑，对用户在当前对话轮次中已明确下令执行的操作大幅精简了冗余的二次确认弹窗，但后台无人值守 Routine 涉及高风险外发或资金操作时依然严格遵循审批卡机制，详见 https://x.ai/changelog/bot。）

| 限制维度 | 官方最新硬指标（截至 v0.75.5） | 架构师应对策略与避坑要点 | 官方文档依据 |
| :--- | :--- | :--- | :--- |
| **单 Bot Routine 数量上限** | 最多 **50 条** / Bot | 按业务职能拆分专职 Bot，避免把所有排期堆在同一个默认 Bot 名下 | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **全账号小时级运行上限** | 全账号所有 Bot 合计 **300 次/小时**（v0.75.2 上调） | 严控宽泛事件监听器，用条件过滤与脚本预检拦截无效触发 | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **单条 Routine 小时级上限** | 单条 Routine 最高 **200 次/小时**（v0.75.2 上调） | 针对高频 Webhook 或邮件触发做好去重与合并批处理 | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **定时排期最小间隔** | 最短 **5 分钟** | 长耗时异步任务改用完成时 Webhook 唤醒，切勿用 5 分钟定时轮询盯进度 | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **运行历史保留条数** | 最近 **20 条**记录 | 在 Skill 中强制把每次运行日志追加写入 `/workspace/logs/` 或更新至 Page | [Routines 文档](https://cursor.com/help/grok-bot/routines) |
| **审批卡片有效窗口** | 约 **10 分钟**未响应即 `Expired` | 将需要人工审批的汇总动作集中在固定办公时段推送，配合手机端 Deep-link 通知秒批 | [Security 文档](https://cursor.com/docs/grok-bot/security) |

## 7.5 事件触发 · Event Triggers

除了按时间表跑，Grok Bot 还能靠外部事件触发（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。通过 Cursor 账户集成的连接渠道，外部系统有变动时能唤醒 Bot，比如收到某条特定 Slack 消息或 GitHub 仓库通知（https://cursor.com/help/grok-bot/skills-routines-and-automations）。changelog 里还能看到 Microsoft Teams 消息、Linear 工单、Sentry 告警、PagerDuty 事件触发（8/12），以及带独立 URL 和密钥的 Webhook 触发（v0.21.0，8/19）（https://x.ai/changelog/bot）。这些触发源大多是海外团队协作工具；国内读者如果不用它们，定时 Routine 就够用。这种事件驱动要单独授权连接，跟普通第三方插件不太一样（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/connect-apps）。

配事件触发器最容易踩坑的，是监听条件设得太宽。官方文档专门提过：**永远不要配置诸如监听每一条新消息这类宽泛触发器**（https://cursor.com/help/grok-bot/skills-routines-and-automations 与 https://cursor.com/help/grok-bot/routines）。

![狭窄事件触发器与宽泛监听器的运行成本对比](../images/fig-07-3.png)

*图：狭窄事件触发器与宽泛监听器的运行成本对比*

如果把 Bot 挂在活跃的 Slack 频道里听所有新消息，大家闲聊、发表情包甚至系统机器人推送，都会频繁唤醒 Bot。每次唤醒都要调大模型过一遍上下文，不仅疯狂烧额度，还会塞满上下文噪音，甚至让 Bot 在别人闲聊时误触发动作（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

合格的事件触发器，条件必须卡得很窄（https://cursor.com/help/grok-bot/skills-routines-and-automations）。官方给的范例是同时盯频道、格式和关键词：“当 `#customer-escalations` 频道的消息同时带有工单链接和 ‘needs repro’ 时，才在预发环境复现问题并输出报告”（https://cursor.com/help/grok-bot/skills-routines-and-automations）。就算触发成功，像写回 Slack 或在 GitHub 开 PR 这种操作，指令里也必须卡死人工审批，绝不能让它自己静默搞定（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

### v0.71.2 重磅杀手锏：专属邮箱 `+alias` 加号子别名定向触发 Routine

在 2026 年 10 月 14 日发布的 **v0.71.2 版本**中，Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）正式宣布了一项改变邮件事件触发格局的核心特性（[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)，获 3,073 赞、1,197 书签；详见官方 Agent Email 文档 https://cursor.com/help/grok-bot/agent-email 与官方 Changelog https://x.ai/changelog/bot）：**每个 Bot 的 `@mail.grokbot.com` 专属邮箱现已原生支持 `+alias` 加号子别名，并且支持配置“仅当邮件发送到指定 `+alias` 子别名时才定向触发对应的 Routine”！**

在此之前，如果你给 Bot 配置了“收到新邮件时触发 Routine”，任何发往 `mybot@mail.grokbot.com` 的广告邮件、验证码或系统通知都会无差别唤醒该 Routine。而现在，假设你的 Bot 基础邮箱是 `mybot@mail.grokbot.com`，你无需做任何额外注册，就可以直接在外部网站或转发规则中使用无限个加号子别名（https://cursor.com/help/grok-bot/agent-email）：
- `mybot+newsletters@mail.grokbot.com`：专门用于订阅全网行业 Newsletter 与Substack 专栏；
- `mybot+invoices@mail.grokbot.com`：专门用于接收 AWS、SaaS 订阅账单与电子发票（配合 v0.75.2 新增的**邮件原样转发保留完整 HTML、内嵌图片与文件附件**能力，Bot 验票后可直接将带 PDF 附件的原始账单原封不动转发给公司财务邮箱，详见 https://cursor.com/help/grok-bot/agent-email 与 https://x.ai/changelog/bot）；
- `mybot+alerts@mail.grokbot.com`：专门用于接收服务器监控告警或电商物流变动通知。

社区用户 `@songsong275452`（引用 `@gokul_i` 的实战方案）展示了这一特性的经典用法（[https://x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371)）：将原本塞满个人主邮箱的所有 AI 与科技 Newsletters 统统改订到 Bot 专属的 `+newsletters` 邮箱中，让个人收件箱彻底恢复清净；同时配置两条完美配合的 Routine——一条基于 `+newsletters` 邮件触发器将每封新到的通讯静默归档到云电脑的 `/workspace/newsletters/` 目录，另一条在每周六上午定时运行，将过去一周积攒的所有长文提炼成一份高密度精华周报或交互式 Page 简报。`@AIShovelLab` 也将“`+alias` 邮箱后缀精准触发 Routine”列为当前最值得复用的六大高效自动化范式之一（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）。

下面是一份可直接复制使用的 **`+alias` 定向邮件触发与周六汇总双 Routine 配置指令**：

```text
请帮我配置两条基于专属邮箱 +alias 子别名的协同 Routine：

【Routine 1：+invoices 账单实时解析与原样转发（事件触发）】
- 触发条件（Trigger）：仅当收到发往 mybot+invoices@mail.grokbot.com 的新邮件时触发（忽略发往主邮箱或其他 +alias 的邮件）。
- 执行动作：
  1. 提取邮件正文与 PDF 附件中的商户名称、扣款金额、币种、账单周期与发票号，追加写入 /workspace/finance/2026-invoices.csv。
  2. 若单笔账单金额超过 $100，在当前对话发送高优提醒。
  3. 使用 v0.75.2 原样转发功能（保留完整 HTML、内嵌图片与原始 PDF 附件），将该邮件起草转发给 finance@mycompany.com，并挂起审批卡等我确认后发送。

【Routine 2：+newsletters 周六深度研报汇总（定时触发）】
- 日常归档规则：凡发往 mybot+newsletters@mail.grokbot.com 的邮件，平时收到时不生成聊天打扰通知，直接将正文静默归档保存至 /workspace/newsletters/inbox/。
- 触发条件（Trigger）：每周六上午 10:00（Asia/Shanghai 时区）运行。
- 执行动作：
  1. 读取 /workspace/newsletters/inbox/ 下过去 7 天新增的所有通讯文章。
  2. 按“底层模型进展”、“Agent 工程实践”、“商业化与投融资”三个维度去重聚类，更新到我的《每周 AI 核心情报》Page 看板中。
  3. 归档已处理的文章至 /workspace/newsletters/archive/。
```

### 长耗时任务完成 Webhook 精准唤醒：告别定时轮询空转

除了外部 SaaS 事件与邮件别名触发，Webhook 触发器在**云电脑内部长耗时任务协同**上还有一个极其省额度的妙用。

许多开发者会在 Grok Bot 的云电脑（cloud box）内部安装 Codex CLI 或运行耗时数十分钟的大规模数据抓取与模型编译任务。如果配置一条每 5 分钟跑一次的定时 Routine 去检查任务跑完没有，在等待期间会白白浪费十几次大模型上下文唤醒额度。社区开发者 `@AbhisheKumarA7`（Abhishek Kumar）分享了一套“**长任务完成时 Webhook 唤醒（Wake on Done via Webhook）**”的零轮询架构（[https://x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578)），`@eze_is_1` 也在长耗时任务防休眠指南中重点剖析了这一机制（[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151)）：
1. 为负责验收的 Grok Bot 创建一条 **Webhook 触发型 Routine**，获取专属 Webhook URL 与密钥（https://cursor.com/help/grok-bot/routines）；
2. 在云电脑后台启动 Codex CLI 或长耗时构建脚本时，在命令末尾追加一段完成后自动回调该 Webhook 的钩子；
3. 在漫长的执行过程中，Grok Bot 完全处于静默零消耗状态（zero polling token waste）；直到后台任务真正跑完的瞬间，脚本才发送一次 HTTP 请求精准唤醒 Grok Bot 进场验收成果并推送到你的手机上。

如果你在从外部脚本或本地 Claude Code 向云端 Grok Bot 推送复杂 JSON 载荷时，遇到 Webhook 严格校验格式导致的 `HTTP 400` 报错，还可以参考中文社区开发者 `@mikan77_aoi`（橘子🍊）验证过的零守护进程排错方案（[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）：无需依赖复杂的第三方框架，直接用 Python 标准库（`urllib.request`）编写一个轻量级桥接脚本，将易引发转义冲突的复杂长文本先写入共享工作区文件或精简为标准键值对，通过 4 次干净的 API 握手调用即可实现 100% 稳定的跨端唤醒与任务交接：

```bash
# 示例：在云电脑后台运行长耗时 Codex 构建任务，仅在跑完瞬间通过 Webhook 零轮询唤醒 Grok Bot（参考 @AbhisheKumarA7 范式）
nohup bash -c '
  codex exec "重构并跑通 /workspace/app 下的全部集成测试" > /workspace/logs/codex_build.log 2>&1
  EXIT_CODE=$?
  python3 -c "
import json, urllib.request
payload = json.dumps({\"event\": \"codex_task_done\", \"exit_code\": $EXIT_CODE, \"log_path\": \"/workspace/logs/codex_build.log\"}).encode(\"utf-8\")
req = urllib.request.Request(
    \"https://api.cursor.com/v1/grok-bot/webhooks/YOUR_ROUTINE_WEBHOOK_ID\",
    data=payload,
    headers={\"Content-Type\": \"application/json\", \"Authorization\": \"Bearer YOUR_WEBHOOK_SECRET\"},
    method=\"POST\"
)
urllib.request.urlopen(req, timeout=10)
"
' >/dev/null 2>&1 &
```

## 7.6 Routine 审计 · Audit

社区里有句话：“在 Grok Bot 体系里，Routine 才是真正的产品，而不是那个 Bot 头像”（https://x.com/i/status/2109516426767654962）。但新鲜劲一过，很多人搭的 Routine 慢慢全变成了信息垃圾。

有行业观察者提过：别把“搭了复杂的流程”当成“创造了真实的业务价值”（https://www.youtube.com/watch?v=LM7Ft7g8qJw）。每天早晨推过来的行业日报、数据摘要或竞品清单，要是连续一个月都没改变过你的任何业务决策，那它根本没必要存在。

再算一笔成本账。社区开发者按 API 价格估算过（不是订阅的实际扣费）：每 5 分钟跑一次的 Routine，一个月会在后台跑 8,640 次（https://x.com/fleyta88/status/2109346840382415019）。要是有 95% 的时候源数据根本没变，Bot 每次还去啃一遍完整页面和长上下文，额度就全打水漂了（https://x.com/fleyta88/status/2109346840382415019）。

### The X Subscription 三合一共享额度池下的头号隐形杀手

自 2026 年 10 月 18 日 Grok Bot 正式并入 **The X Subscription** 三合一统一订阅体系后（官方公告 [https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)，详见官方计费文档 https://cursor.com/help/grok-bot/plans 与 https://cursor.com/help/the-x-subscription/overview），Routine 审计的重要性上升到了前所未有的高度。

中文社区实践者 `@charlie_pmp`（Charlie）一针见血地指出，很多用户升级到 The X Subscription（无论是 $30/月的 Premium、$100/月的 Super 还是 $200/月的 Ultra 档位）后，突然感觉周额度进度条掉电速度明显变快，背后的头号元凶正是**“三端共用同一个周额度池 + 后台静默空转的高频冗余 Routine”**（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）：
1. **三合一共享周额度池（One Weekly Usage Pool）**：在官方 The X Subscription 规则下，你在桌面/手机上跑的 **Grok Bot**、日常对话搜索用的 **Grok**，以及写代码用的 **Cursor IDE**，三者现在从**同一个每周重置的额度池**里抽水（https://cursor.com/help/grok-bot/plans）。一旦后台的冗余 Routine 在夜里偷偷把周额度池跑干，不仅你的 Bot 会停摆或开始扣减 `grok.com/dashboard/billing` 里的 **Prepaid Credits（预付充值额度）**，连你白天打开 Cursor 写代码都会直接受到牵连（https://cursor.com/help/grok-bot/plans）！
2. **用“确定性脚本轮询”替代“大模型浏览器轮询”**：要想既保留高频监控的敏捷度、又不消耗宝贵的周额度池，最硬核的解法是本书作者 Mr.鼓先生（`@StarkLJM`）实测跑通的 **“AI 写确定性脚本，脚本跑日常轮询”零额度抓榜范式**（[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377) 与 [https://x.com/starkljm/status/2112818533797343312](https://x.com/starkljm/status/2112818533797343312)）。针对每天需要定时抓取榜单或监控页面变动的任务，不要让 Routine 每次都调用大模型开浏览器读网页，而是先花 **28.6 秒**让 Agent 写好一套带严格字段校验（缺失字段立即告警、无评分严格存 `null` 而非用 `0` 污染均值）的 Python 爬虫脚本；日常巡检全部交由脚本在 **1.99 秒**内确定性跑完，日常轮询消耗 **0 模型额度（zero model tokens）**，只有当脚本检测到实质性异动时才唤醒大模型做深度分析。或者如 `@hppzyy` 分享的方案（[https://x.com/hppzyy/status/2111573227881529454](https://x.com/hppzyy/status/2111573227881529454)），将日常例行粗筛交给云电脑内挂载了廉价 DeepSeek API 的轻量级 CLI 工具处理，把官方周额度池100%留给核心推理。

所以必须定期做 Routine 审计。Grok Bot 团队的 Lauren Tan 在访谈里提到，她有一个叫 Dr. Eggbot 的 Bot 专门定期审计所有 Bot 和 Routine 的成本（团队成员访谈，https://www.youtube.com/watch?v=xZ5TEaleUdg）。社区的做法是每月搞一次淘汰审计（https://x.com/kocer_eth/status/2101669438038634827）：数一数上个月跑过的任务，看结果到底被你采纳了几次；找出那些长期失败、没人看的幽灵任务；每次审计至少强制删掉一条没用的 Routine（https://x.com/kocer_eth/status/2101669438038634827）。甚至像 `@kaelanyiu`（Kaelan Yiu）那样，专门设立一个每隔几天才低频运行一次的“评测官 Bot（Meta-Evaluator Bot）”，对各 Worker Bot 的产出质量与模型性价比跑分审计，动态优化整个团队的底层调用配置（[https://x.com/kaelanyiu/status/2114213605566742884](https://x.com/kaelanyiu/status/2114213605566742884)）。

> [!NOTE]
> 📸 **截图位（待补）**：Routine 审计提示词在对话中的执行与停用确认

你可以把下面这段审计提示词直接发给负责调度的 Bot。它会检查所有排期，把高频轮询改成看哈希值、计数器或时间戳的轻量检查，而且没有你确认绝不动手删（https://x.com/fleyta88/status/2109346840382415019）：

```text
Audit all my existing routines across all Bots and optimize the execution plan around actual business changes.

Perform the following steps:
1. List every routine, its owning Bot, its schedule or trigger, and its expected output.
2. Flag routines where over 90% of historical runs produced no change or were ignored.
3. Replace high-frequency full runs with lightweight change checks: inspect only a file hash, record count, or updated timestamp before doing downstream heavy work.
4. If no underlying data has changed, instruct the routine to terminate immediately without generating notifications.
5. Identify any routine that has not directly influenced a decision or workflow in the past 30 days and nominate it for deletion.
6. Verify that all irreversible external actions remain gated behind human approval.

Show me the full audit report, proposed schedule adjustments, and estimated savings first. 
Do not modify, pause, or delete any routine without my explicit confirmation.
```

说到底，**例行自动化本身只是过程，如果输出结果从未影响过你的任何实际决策，它就是在白白烧钱**（https://www.youtube.com/watch?v=LM7Ft7g8qJw）。定期大扫除，留下真正能办事的坚固闭环，你的 Bot 团队才算上了正轨。


# §08 审批与安全边界 · Approvals & Safety

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

![多用户间 Firecracker microVM 强隔离与同用户内所有 Bot 共享单机环境对比](../images/fig-08-1.png)

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

![红黄绿权限表](../images/fig-08-2.png)

我把常见的操作场景整理成了这张权限对照表，派活和配权限时可以严格对照执行：

| 权限等级 | 适用操作场景 | 系统配置建议 | 核心防护机制 |
|---|---|---|---|
| 红灯：严禁授权（必须人工亲自接管） | 个人与公司网络银行、证券交易、资金转账、主邮箱主密码、核心生产数据库、最高控制台登录、双重验证（2FA）输入、签署法律协议 | 严禁在云电脑登录任何网银或主账号；在 Settings 中将 Execution on Local Computer 设为 Never allow；企业版配置 Network Controls 域名白名单（勾选 Apply to MCP servers）；切勿将主力大额信用卡常驻存入 Vault | 遇到高敏登录与大额支付步骤，强制打开 Agent Computer 点击 Take control 手动接管或使用 1Password 逐次生物识别授权；绝不在普通聊天中粘贴任何凭据文本 |
| 黄灯：仅限草稿（每次必弹审批卡） | 向外部发送邮件或通知、社交媒体公开发帖、Shopify 商品信息上架、采购询价与调价发单、删除或覆盖既有数据、修改 Routine 定时规则 | 在 Settings → General → Auto-review 中添加针对发信、变更看板等动作的 Ask first 规则（企业版配置 Require approval 自定义规则）；在初始提示词中固定写入禁止直接发布 | 严格执行草稿优先原则；系统弹出审批卡由人工核实变更影响后再做决策；后台触发的任务若 10 分钟无人审批则自动过期拦截 |
| 绿灯：允许只读（低影响可自动放行） | 抓取公开网页资讯、阅读非敏感格式文件、比价表格整理、在 /workspace 内部生成报告、拉取只读数据看板、运行 git status 等只读检查 | 在 Settings → General → Auto-review 中针对指定路径下的安全只读命令配置 Allow automatically 规则；连接只读性质插件 | 限制在隔离的 Firecracker microVM 云电脑内执行；由 Auto Review 模型做后台安全校验；不赋予任何不可逆写权限 |


# §09 连接器与 Marketplace · Connectors

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

![Grok Bot 十大类连接器生态分布图与 Bring Your Own MCP 公网接入拓扑](../images/fig-09-1.png)

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

![Computer use、MCP 与 API 三条实现路径在灵活性、稳定性与成本维度的选型决策漏斗](../images/fig-09-2.png)

*图：Computer use、MCP 与 API 三条实现路径在灵活性、稳定性与成本维度的选型决策漏斗*

同一任务分别用 Computer use、MCP、API 完成的差异。


# §10 官方合作集成逐个讲 · Partner Integrations

## 10.1 Cursor：云端 Agent、交接与模型路由 · Cursor Handoff

> [!NOTE]
> 📸 **截图位（待补）**：dashboard/usage 页面（注意：社区对 usage 页是否显示具体模型说法不一，见下文）

> 适合谁：10.1–10.2 主要面向写代码的读者（需要 GitHub/Cursor）；10.3 面向用 Slack 的团队；不写代码、不用 Slack 的个人读者可以直接跳到 10.4（X）、10.5（邮箱）、10.7–10.8。

假设你深入研究 Grok Bot 的工程协作定位，会发现它在架构上扮演的是工程师主管与协调员，而不是单打独斗的代码生成窗口（https://x.ai/bot/guides/grok-bot-for-engineering）。SpaceXSI 工程师 Lingxi Li 分享过官方实践：Bot 能直接创建 Cursor 云端 Agent（Cloud Agents），把包含上下文规范、视觉要求和预设 Skill 的完整 Prompt 派发过去，全程监听 transcript 记录和伴随产物。如果云端 Agent 遇到网络抖动卡住了，Grok Bot 会自动排队补发消息排障；发现思路跑偏了，也能直接中断（https://x.ai/bot/guides/grok-bot-for-engineering）。底层模型也不只靠自身。马斯克在 2026 年 10 月 7 日宣布，Grok Bot 会根据具体任务动态路由到最优模型，包括 Claude Opus 5.5、Midjourney 和 Suno（https://x.com/elonmusk/status/2107724314451878104），（https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk）。（有视频博主提到在 Bot 电脑里装 Grok Build CLI、用 Composer 2.5 跑有 skill 支撑的任务更省（research/youtube/youtube-summaries.md），但官方 Composer 2.5 公告并未提及 Grok Bot 的路由规则，原稿"长任务走 Composer 2.5"无依据，已删除。）有社区帖称，查看 Cursor 后台 usage 页面，部分任务确实调用了 Claude Opus 5.5（个例）（https://linux.do/t/topic/2990677）。

连接 Cursor 主要有两种方式。第一种是原生账号授权：拿买了 Cursor 付费权益的账号登录 Grok Bot，两端云端调度权限就打通了，Cloud Agent 卡片可以选 Open in Web 或 Open in Cursor（changelog v0.31.0，https://x.ai/changelog/bot）；也有用户分享了在 Cursor 客户端 Agents 窗口打开的体验（https://x.com/i/status/2105881504744460675）。第二种是终端直连：有社区帖分享，让 Grok Bot 在云电脑终端跑官方安装脚本装 Cursor CLI，然后在对话界面的凭据输入框填 Cursor 的 API Key。界面会自动打码脱敏，这样就能在云电脑命令行里调 Opus 5.5（个例）（https://x.com/i/status/2109088800903483616）。（原稿把 https://x.ai/cli/install.sh 当作 Cursor CLI 的官方安装脚本——它其实是 Grok CLI / Grok Build 的安装脚本，已删除该链接。）

随着 2026 年 10 月中下旬的架构演进，Cursor 与 Grok Bot 的连接迎来了第三种重磅范式：**BDK（Bot Developer Kit）与 `cursor-grokbot-agents` 双向跨端调用**。通过 BDK 桥接，运行在本地电脑上的 **Claude Code**、**Codex**、**Cursor IDE** 可以直接向云端 **Grok Bot** 派发任务并回收产物；反过来，云端 Grok Bot 也能唤醒本地 CLI Worker 协同作业，形成“本地深度写代码 + 云端 24 小时查 X / 跑浏览器 / 渲染视频 / 查长期记忆”的双向混动架构。此外，Cursor 与 Grok Bot 产品工程负责人 `@ericzakariasson` 分享了两项高阶硬件与远程 Worker 协同技巧：只要在家里常开的 Mac mini 上启动并登录 Grok Bot 桌面端，该设备就会自动注册到 `Settings > Computer` 列表中，让你随时在手机端指挥云端 Bot 到家用 Mac mini 上跑本地任务（[https://x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099)）；你甚至可以直接要求 Grok Bot 在远程机器上自动配置并启动 `cursor-agent worker`（[https://x.com/ericzakariasson/status/2114157733276525044](https://x.com/ericzakariasson/status/2114157733276525044)）。

社区围绕 BDK 与跨端调度已经沉淀出丰富的实战打法：
- **`@StarkLJM`（Mr.鼓先生）的 BDK 跨端动画渲染实战**：在 2026 年 10 月 12 日的教程（[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411)，9 赞）中，演示了如何通过 `cursor-grokbot-agents` 将本地终端的 Codex / Claude Code 与云端 Grok Bot 打通。本地 Claude Code 向云端 Grok Bot 下发“制作一段 20 秒《上下五千年》中国历史线条画动画短片”的任务，云端 Grok Bot 在沙箱内独立完成分镜与视频合成，直接向本地返回 `0:20` MP4 视频卡片与 `2.7 MB` 完整源码压缩包。
- **`@kangxiaile`（康熙AI了）的 X 舆情检索外包闭环**：在本地 Claude Code 写代码遇到新库或舆情需求时，自动派单给云端 Grok Bot 检索 X 全网最新实测帖，由 Grok Bot 整理成结构化 Markdown 传回本地供 Claude Code 继续编码（[https://x.com/kangxiaile/status/2109752183889744216](https://x.com/kangxiaile/status/2109752183889744216)）。
- **`@mikan77_aoi`（橘子🍊）的 4 次 API 调用纯标准库桥接脚本**：针对外部服务向 Webhook 推送复杂 JSON 载荷偶发 HTTP 400 校验报错的问题，编写了零外部依赖、零守护进程（zero-daemon）的 Python 标准库（stdlib）脚本，仅用 4 次 API 调用就让本地 Claude Code 稳定将任务交接给云端 Grok Bot（[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）。
- **多端协同矩阵验证**：`@z_lumia`（x白，[https://x.com/z_lumia/status/2113800469571313974](https://x.com/z_lumia/status/2113800469571313974)）在开通三合一订阅后跑通了本地 Claude Code / Codex 随时调取云端 Grok Bot 长期记忆、云端 Grok Bot 反向在本地台式机执行 CLI 的双向链路；`@AIShovelLab`（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）总结了路由 Skill 防盲目重试、本地与云端双向派单、Cloud Agent 并发等六大联动范式；`@charlychoi`（[https://x.com/charlychoi/status/2111425470201995309](https://x.com/charlychoi/status/2111425470201995309)）、`@pomufgd`（[https://x.com/pomufgd/status/2110799518283497488](https://x.com/pomufgd/status/2110799518283497488)）与 `@SyrianVeterans`（[https://x.com/SyrianVeterans/status/2110661026538737879](https://x.com/SyrianVeterans/status/2110661026538737879)）也分别验证了 BDK 跨端调度的工程工作流。

你可以复用以下零外部依赖的 Python 标准库桥接脚本示例，在本地 CLI 工具与云端 Grok Bot 之间完成任务派发与状态回收：

```python
#!/usr/bin/env python3
"""
BDK / cursor-grokbot-agents 极简纯标准库跨端派单示例（零第三方依赖）
适用场景：从本地 Claude Code / Codex / Cursor 终端向云端 Grok Bot 派发任务并轮询产物
"""
import json
import os
import time
import urllib.request

API_BASE = os.environ.get("GROKBOT_API_BASE", "https://cursor.com/api/v1/bot")
API_TOKEN = os.environ["GROKBOT_API_TOKEN"]
BOT_ID = os.environ["GROKBOT_BOT_ID"]

def api_call(method: str, path: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=data,
        headers={
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json",
        },
        method=method,
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

# 1. 创建会话 -> 2. 发送跨端任务指令 -> 3. 触发云端执行 -> 4. 拉取结果与产物链接
session = api_call("POST", f"/agents/{BOT_ID}/sessions", {"source": "local-cli-bdk"})
session_id = session["id"]
api_call("POST", f"/sessions/{session_id}/messages", {
    "role": "user",
    "content": "检索 X 上过去 24 小时关于 cursor-grokbot-agents 的高赞实测帖，整理为结构化 Markdown 返回。"
})
run = api_call("POST", f"/sessions/{session_id}/runs", {"wait_for_completion": False})
while True:
    status = api_call("GET", f"/sessions/{session_id}/runs/{run['id']}")
    if status.get("state") in ("completed", "failed"):
        print(json.dumps(status, ensure_ascii=False, indent=2))
        break
    time.sleep(3)
```

在计费与订阅层面，2026 年 10 月 18 日官方正式上线了 **The X Subscription 三合一统一订阅**（官方公告：[https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)，3,039 赞 / 272 转发 / 540 书签；官方文档：[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。该计划将 **Grok**、**Cursor** 与 **X Premium** 整合为单一订阅，其中 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 包含 Grok Bot 权限（Free $0 与 Plus $8/月 不包含）。在 The X Subscription 下，Grok Bot、Grok 与 Cursor **三端共享同一个周额度池（weekly usage pool）**；当周额度耗尽后，超额用量从 **Prepaid Credits（预付额度）** 中扣除（在 `grok.com/dashboard/billing` 充值并可设月度封顶）。需要特别注意第三方模型的计费边界：根据官方说明（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)），**在 The X Subscription 体系下，当你在 Cursor 中调用非 Grok 系列的第三方模型（如 Claude Opus 等）时，会直接扣减 Prepaid Credits（预付额度），而不会消耗套餐内的 Grok 周额度池**。至于既有的独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）与自助式 Teams（$40/人/月）老订户，只要不主动切换即可保留原方案与后付费按需额度；一旦通过 `cursor.com/unify` 或 `accounts.x.ai/unify` 单向升级至 The X Subscription，将**不可逆、无法退回旧版独立订阅**（且通过 Apple App Store 或 Google Play 订阅的用户必须手动去对应商店取消旧订阅以防双扣）。

Bot 交接给 Cursor 云端 Agent 后，usage 页显示的模型。

官方目前并未公开模型路由的具体触发规则与任务分发逻辑（https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk）。有社区帖反映，很多日常任务在 usage 里显示的还是 grok-bot-default，也有人截图称切到 Opus 5.5 后思考等级只有 low（个例）（https://linux.do/t/topic/2991033）；另有中文教程称 Grok Bot 用量统一记为"Grok Bot 用量"、不按模型区分（research/zh/douyin/chunduai-motion-studio.md）。两种说法冲突，以你自己的 usage 页为准。而且云端 Agent 如果缺乏明确的完成证据检查，很容易陷入反复重试的死循环，把周额度快速耗尽。记住，云端 Agent 并不等同于可以完全免审的最终交付人，所有代码改动与视觉截图仍需人工检查。

## 10.2 GitHub 与 Origin：Bug 复现与 PR 自动化 · GitHub & Origin

Grok Bot 原生支持 GitHub 和 Origin 插件（https://x.com/bot/status/2105373767568621895）。在工程流水线里，它主要干两件事：复现 Bug 和托管 PR。按官方指南，Bot 收到 Bug 报告后，必须在暂存环境用全新测试账号复现，整理出操作步骤、预期与实际表现、截图证据、操作系统及浏览器版本、网络控制台记录，并尽量提取最小测试用例（https://cursor.com/help/grok-bot/use-cases）。在改代码阶段，Bot 能结合 Cursor 生成分支、提交代码、发起 PR，甚至附带录屏或操作截图当证明（https://x.ai/bot/guides/grok-bot-for-engineering），（https://x.com/bot/status/2105373767568621895）。

接入 GitHub 时，在应用连接面板里找到 GitHub 插件，走标准 OAuth 授权组织和仓库就行（https://cursor.com/help/grok-bot/team-bots）。如果想让 Bot 在自带的云电脑终端里跑 git clone、commit 或 push，要在安全凭据卡片里录入细粒度、受限作用域的 Personal Access Token 或专用 SSH Key。配 Routine 时，可以设成定时检查未关闭的 Issue，或者监控特定分支的变更状态（https://cursor.com/help/grok-bot/use-cases）。根据官方 v0.75.2 更新标准（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)），Routine 的运行频率上限已大幅提升至**全账号所有 Bot 合计 300 次/小时，单条 Routine 最高 200 次/小时**（定时触发最小间隔仍为 5 分钟），足以支撑高频 PR 状态巡检与 Issue 事件响应。

从 Issue 复现到草稿 PR，以及未经批准是否不合并。

权限失控是 GitHub 集成中最严重的隐患。官方工程团队指出，只有当模型审查的置信度极高且改动影响极小时，才允许自动合并，常规项目必须保留人工代码复核（https://x.ai/bot/guides/grok-bot-for-engineering）。**绝不能把未经审批的代码直接合并进主分支**，并且在自动化复现任何缺陷时，官方安全准则严厉禁止把生产环境的真实客户数据作为测试输入（https://cursor.com/help/grok-bot/use-cases）。

## 10.3 Slack 与 Team Bots：共享企业协作 · Slack & Team Bots

![Team Bot 在 Slack 频道、1:1 私聊与云电脑之间的隔离架构](../images/fig-10-1.png)

*图：Team Bot 在 Slack 频道、1:1 私聊与云电脑之间的隔离架构*

2026 年 9 月 28 日，官方推出了面向企业团队的 Team Bots（https://x.ai/news/team-bots）。管理员配好技能库、知识文件、插件和凭据后，可以把 Team Bot 发布成企业 Slack 的原生应用，拥有独立的名字、头像与 handle（https://cursor.com/help/grok-bot/team-bots）。团队成员能在公开频道里 @mention 叫醒它，也能在私聊 DM 里单聊。在官方展示的内部案例中，大客户专员 Bot 每晚聚合新闻、Gong 通话记录与文档，清晨在客户频道发早报；研发协调 Bot 在频道里捕获缺陷、触发云端修复并提 PR；只读数据分析 Bot 则依据 SQL 技能库在群里直接查指标（https://x.ai/news/team-bots）。

接入 Slack 时，管理员先在桌面端配好 Team Bot，选发布给团队，在详情页点 Bring to your team's Slack 授权工作区（https://cursor.com/help/grok-bot/team-bots）。要是工作区需要审批应用，就等待批准，也可以配 Slack 自动化规则来实现自动批准（https://cursor.com/bot/slack-auto-approve）。安装完毕后，在目标频道用 `/invite @BotName` 邀请加入。成员还需在设置里关联自己的 Slack 账号，这样每个人的对话权限与用量扣费才会独立计算（https://cursor.com/help/grok-bot/team-bots）。

未关联账号的成员在 Slack 里 @bot 时的表现。

必须看清底层计算资源的分配差异：个人 1:1 私聊或应用内对话时，每个人用的是各自的专属云电脑。但在 Slack 频道、群聊与公共 Thread 中，Slack 频道中的 Bot 运行在同一台共享云电脑上（https://cursor.com/help/grok-bot/team-bots）。这意味着在共享频道上传的文件会留在公共机器上，其他成员提问时可能调阅到这些数据。另外，有社区帖提醒，切勿给 Bot 设置无条件监听全频道消息的 Routine，这会导致空转轮询并快速烧尽额度（个例）（https://x.com/fleyta88/status/2109346840382415019）。

## 10.4 X：原生检索、时间线监控与 @bot 派单 · X Integration

Grok Bot 于 2026 年 8 月 29 日接入了 X 平台，付费用户有初始 X API 调用额度（https://x.ai/news/grok-bot-and-x），并在 10 月 8 日上线了搜索、读取与监控 X 动态的能力（https://x.com/bot/status/2107949161878606089）。除了在客户端让 Bot 监控时间线、抓取书签或整理热点，官方还推出了 Tag on X 机制：刷推时遇到长文、技术讨论或新闻，直接在下方回复并 @bot 加上处理要求，@bot 会回一条接单确认，后台云电脑自动展开作业，过程与产物都保存在客户端会话中（https://cursor.com/help/grok-bot/tag-on-x）。有社区帖提到，创作者常借助这个通道搭行业舆情监控和线索捕捉 Routine（个例）（https://x.com/rowancheung/status/2108328114552000842）。

进入 2026 年 10 月中下旬，X 插件迎来了史诗级能力扩容，除了基础的公开检索（`search_posts_recent`、`search_posts_all`、`get_posts_by_ids`、`get_users_by_ids`、`get_users_posts`、`get_users_mentions`、`get_post_Thread`、`get_article`），现已全面覆盖**六大高阶原生能力**（官方文档：[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）：

1. **X Chat 端到端加密私信与陌生人消息请求审批（E2EE DMs & Message Requests）**：2026 年 10 月 16 日，X 与 Grok Bot 工程师 Paul Vann（`@pjvann`）正式宣布 Grok Bot 打通 `@chat` 加密私信收件箱与陌生人消息请求（[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)，1,069 赞 / 108 转发 / 132 书签）。`@pjvann` 分享了他让 `@bot` 整周自动分拣繁忙私信箱、逐条审查并批准高质量陌生人私信请求、过滤垃圾骚扰并起草回复的真实工作流。在底层安全架构上，X Chat 采用端到端加密（`xchat_lite`），MCP 接口仅返回加密载荷与 **Juicebox** 密钥恢复配置；Grok Bot 会在自己的云电脑沙箱（box）内克隆官方开源解密辅助库 [https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper)，调用本地 `xchat_tool.py` 并配合用户提供的 **4 位数字 X Chat PIN 码**，在云电脑本地完成解密读取与加密发送。
2. **书签与书签文件夹（Bookmarks & Bookmark Folders）**：支持读取、检索与按文件夹分类归档你的 X 书签，方便将日常收藏的长推和干货自动同步进个人知识库。
3. **Lists 列表读取与成员管理**：支持读取指定 X 列表的时间线动态，并可直接通过工具增删和管理列表成员（List writes），打造全自动维护的行业 KOL 雷达列表。
4. **Spaces 语音空间与 Communities 社群**：支持检索与读取 X Spaces 语音空间元数据及 Communities 社群帖子动态，捕捉垂直圈层的实时讨论。
5. **Scheduled X Calls 预约通话管理**：支持通过 `schedule_call`、`list_scheduled_calls` 等工具直接创建预约语音/视频通话、查询即将开始的通话日程以及代为处理通话邀请回复（RSVP）。
6. **Livestreams 直播推流与弹幕治理**：完整覆盖直播全生命周期，支持创建与管理 RTMP/RTMPS 推流源（stream sources）、创建预约直播广播（scheduled broadcasts）、在直播结束后自动拉取并总结完整弹幕聊天记录（summarize ended broadcast chat），以及自动化管理直播间房管（moderators）与禁言名单（mutes）。

在费用边界上，Grok Bot **内置的公开 X 数据读取完全免费**，包含在订阅额度内；而通过 X 插件调用私有账号数据或高阶写操作时，则依据官方应用连接文档（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）按照 `https://console.x.com` 的规则计费。若你发现 X Chat、预约通话、直播、Spaces 或 Lists 工具缺失而普通搜索正常，只需在 `Settings → Connect apps` 中断开并重新连接（Reconnect）X 插件即可刷新权限。

当你在云电脑沙箱中使用官方 `xchat-grokbot-helper` 处理端到端加密私信时，底层执行的标准流程如下：

```bash
# 在 Grok Bot 云电脑 (box) 中克隆官方 X Chat 本地加解密辅助工具
git clone https://github.com/xdevplatform/xchat-grokbot-helper.git
cd xchat-grokbot-helper

# 使用 4 位 X Chat PIN 码配合 Juicebox 在沙箱本地解密收件箱与陌生人消息请求
python3 xchat_tool.py --action decrypt-inbox --pin "${XCHAT_4DIGIT_PIN}"

# 审查陌生人请求后，在本地完成加密并发送私信回复
python3 xchat_tool.py --action send-reply --conversation-id "conv_xxx" --pin "${XCHAT_4DIGIT_PIN}" --text "已收到您的合作邀请，稍后由团队跟进。"
```

接入 X 的搜索与分析功能，只要在客户端通过 X connector 登录账号就行（https://x.ai/news/grok-bot-and-x）。想用回复 @bot 派发任务的能力，必须满足四个条件：在 grok.com 绑定 X 账号；该 Grok 账号有有效的 Grok Bot 权限；名下至少创建过一个属于自己的 Bot；X 账号注册地在支持的国家或地区（https://cursor.com/help/grok-bot/tag-on-x）。

在 X 上回复 @bot 派单后的任务流转。

Tag on X 有严格的地域限制。官方文档明确指出，注册地在澳大利亚、英国、欧盟、冰岛、列支敦士登或挪威的账号，以及注册地显示为泛区域（如 South Asia）或未填国家的账号，都无法触发 @bot 接单，用代理也绕不过归属地判定（https://cursor.com/help/grok-bot/tag-on-x）。推文包含视频、GIF 动图，或者同时标记了 @grok 时，@bot 同样会静默忽略（https://cursor.com/help/grok-bot/tag-on-x）。@bot 只在支持的国家和地区回帖接单。有社区帖提醒，在 X 上高频自动互动可能触发平台反垃圾算法的审查与标记（个例）（https://linux.do/t/topic/3004566）。

## 10.5 邮箱体系：Gmail 与 @mail.grokbot.com 专属邮箱 · Email Systems

> [!NOTE]
> 📸 **截图位（待补）**：在 Grok Bot 对话界面中向 Bot 发送认领 @mail.grokbot.com 邮箱的提示词

接个人 Gmail 只能让 Bot 在收件箱里被动打标签或起草回复。2026 年 10 月 10 日，官方为 Grok Bot 推出了专属独立邮箱（https://x.com/bot/status/2108609764766908772）。分配给 Bot 的邮箱以 `@mail.grokbot.com` 结尾，支持自定义前缀，单账号限领一个（https://www.163.com/dy/article/L8S7SDMS0511B8LM.html）。有了专属邮箱，Bot 成了有独立联络通道的数字员工，能代表你向供应商发询价、代为注册第三方服务、收验证码，或者排会议日程（https://x.ai/news/grok-bot-procurement），（https://www.163.com/dy/article/L8S7SDMS0511B8LM.html）。有社区帖称，发往该域名的邮件能实时推送给 Bot，不用像外部邮箱那样定时轮询拉取（个例）（https://linux.do/t/topic/3001934）。

在随后的版本迭代中，官方围绕 Agent Email 连续推出了两项重磅能力（官方文档：[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)）：
1. **v0.71.2 `+alias` 加号子别名收发与定向触发 Routine（2026-10-14）**：由 Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）正式发布（[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)，3,073 赞 / 219 转发 / 1,197 书签）。现在每个 Bot 的 `@mail.grokbot.com` 邮箱都天然支持无限个 `+tag` 加号别名（例如 `mybot+newsletters@mail.grokbot.com`、`mybot+invoices@mail.grokbot.com`、`mybot+alerts@mail.grokbot.com`）。你不仅可以用特定别名对外收发邮件，还能配置 **仅当邮件发送至某一个具体 `+alias` 别名时才定向触发对应的 Routine**（在 v0.75.2 下，全账号所有 Bot 合计最高支持 300 次/小时、单条 Routine 最高 200 次/小时，详见 [https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）。社区用户 `@songsong275452`（引用 `@gokul_i`，[https://x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371)）与 `@AIShovelLab`（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）借此跑通了“把所有外部 Newsletter 订阅全部迁入 `+newsletters` 别名、主邮箱彻底清净，再由周六 Routine 汇总成一份结构化精华周报”的高效范式。
2. **v0.75.2 邮件原样转发（2026-10-22）**：根据官方更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与 [Agent Email 官方文档](https://cursor.com/help/grok-bot/agent-email)，Bot 在转发邮件（无论是通过 `@mail.grokbot.com` 还是已连接的外部邮箱）时，现已支持**完整保留原始邮件的 HTML 排版格式、正文内嵌图片（inline images）以及文件附件（attachments）**，彻底解决了复杂商务邮件、带图周报与合同发票在转发给人类同事或财务系统时版式丢失的问题。

你可以按如下配置结构，利用 `+alias` 加号别名将不同业务流的入站邮件分流给独立的 Routine：

```yaml
# Agent Email +alias 定向触发 Routine 与原样转发配置范式
bot_email: "opsbot@mail.grokbot.com"

routines:
  - name: "Invoice & Receipt Router"
    trigger:
      type: "email_received"
      to_alias: "opsbot+invoices@mail.grokbot.com"
    instructions: |
      1. 解析入站账单邮件的金额、供应商与到期日，写入财务台账。
      2. 将原邮件使用原生转发（保留原始 HTML 排版、正文内嵌图片及 PDF 发票附件）转发至 finance@company.com。

  - name: "Saturday Newsletter Digest"
    trigger:
      type: "schedule"
      cron: "0 9 * * 6" # 每周六早 9:00 汇总，平时入站仅归档不触发昂贵长任务
    instructions: |
      读取本周所有发送至 opsbot+newsletters@mail.grokbot.com 的订阅邮件，
      按核心行业动态、必读深度长文与工具发布提炼成一份周六精华简报。
```

连接外部 Gmail 只要在插件中心添加 Google 插件，授权读取邮件与日历即可。认领专属的 `@mail.grokbot.com` 邮箱：社区帖称直接跟 Bot 说要注册邮箱即可，单账号限领一个，且只能通过 Grok Bot 收发，功能是灰度推送的（个例）（https://linux.do/t/topic/3002150；https://linux.do/t/topic/3001934）。（原稿写"前提是 SuperGrok/X Premium+ 订阅"，该帖并无此说法，已改。）满足条件后，在对话窗口向 Bot 发送指令认领并指定期望的前缀，系统检测未被占用就能完成绑定（https://www.163.com/dy/article/L8S7SDMS0511B8LM.html）。

Bot 自有邮箱收到会议邀请后的处理。

在命名与权限上有个容易踩的坑。有社区帖提醒，千万别用你自己的名字给 Bot 邮箱命名，因为当它对外发邮件时，名字如果与真人一致，在抄送和协同中会引发身份混乱（个例）（https://x.com/petergyang/status/2108624122339287335）。此外，社区反馈专属邮箱只能通过 Grok Bot 收发（https://linux.do/t/topic/3002150）；是否开放 IMAP 等标准协议，官方未说明（CSDN 上"Grok Bot 专属邮箱 IMAP/SMTP 实战"之类文章发布日期混乱，属于 SEO 搬运，勿信）。有社区帖反映早期测试中个别邮件出现过未及时触发动作的情况（个例）（https://x.com/petergyang/status/2108412799684915576）。对外发送真实邮件前，必须严格人工审批。

## 10.6 Notion · Notion

Notion 不只用来抓取或生成单篇笔记，官方把它当成长周期的结构化状态看板（https://x.ai/bot/guides/grok-bot-for-engineering）。模型上下文有限，长周期任务如果全堆在单次会话里肯定会丢信息。官方团队的做法是：多个工程师 Bot 共享一个 Notion 数据库，每 30 分钟轮询一次 PR 状态，自动筛查 CI 失败、安全告警与合并冲突，在看板中推进任务阶段（https://x.ai/bot/guides/grok-bot-for-engineering）。有社区帖展示过在 15 分钟内用 Grok Bot 搭出自媒体数据看板（个例）（https://x.com/op7418/status/2108545983647023493），也有社区帖分享了让 Bot 把长文抓取排版成 PDF 存入 Notion 的用法（个例）（https://x.com/KinGao476942/status/2100073265716928662）。

接入 Notion 时，在插件列表中选 Notion 做 OAuth 授权。在权限配置窗口里，要精确勾选允许该 Bot 读写的具体页面或数据库，不要盲目授权整个工作区。完成授权后，先在 Notion 建好包含明确字段（例如标题、状态、URL、更新时间）的 Database，把链接告知 Bot，让它把读写规范存成复用 Skill。

Bot 向 Notion 数据表写入内容的格式。

权限给得太宽容易造成页面污染，提示词不够精准时，模型可能会修改其他无关页面。另外，如果有人改动了数据库的列字段，没做容错处理的 Routine 会直接报错。记住，用 Notion 数据库作为 Bot 上下文溢出时的外挂看板，不要试图依赖短期对话记忆去维持几周前的任务进展（https://x.ai/bot/guides/grok-bot-for-engineering）。

## 10.7 Shopify · Shopify

2026 年 10 月 9 日，官方宣布推出 Shopify 电商集成插件（https://x.com/bot/status/2108228871938359347）。Bot 能直接查询未处理订单与履约状态、监控低库存商品清单，还能针对促销策略批量更新商品标题、描述与 SEO 关键词（https://x.com/bot/status/2108228871938359347）。有社区帖提到，配合云电脑定时任务，可以让 Bot 结合社媒舆情巡检竞品价格与差评，针对性优化自家店铺（个例）（https://x.com/Hensen1016/status/2108025562048483583）。

接入时，在应用市场选 Shopify 插件，输入店铺二级域名完成 OAuth 登录授权。日常下发指令时，建议把商品上架与修改规则写进 Bot 的系统设定。如果需要批量上架或覆盖属性，一定要在提示词里强制要求先出修改预览，严禁直接提交。

Shopify 测试店铺的库存查询与商品描述草稿。

电商后台的数据直接关乎资金结算与订单履约。模型批量修改数值时偶有幻觉，价格、计量单位或库存一旦填错，损失很难挽回。所以日常运营中，涉及改价和库存变更必须坚持草稿优先，人工审核后才能同步线上。另外，有社区帖指出，外部平台的半公开数据检索召回率不稳定，不能直接单凭它做经营决策（个例）（https://x.com/Hensen1016/status/2108025562048483583）。

## 10.8 Finance（Plaid 只读）与财务隔离 · Finance & Plaid

![Shane Mac 银行数据跨 Bot 泄露路径与共享云电脑风险](../images/fig-10-2.png)

*图：Shane Mac 银行数据跨 Bot 泄露路径与共享云电脑风险*

2026 年 9 月 27 日，官方推出了 Finance 金融连接能力，通过 Plaid 协议只读连接银行账户、信用卡与投资组合（https://x.com/bot/status/2103936247995752705）。有社区帖提到，可以向专属财务 Bot 询问未来 10 天即将发生的扣款总额、分析日常支出明细，或者参考跨账户资金调拨（个例）（https://x.com/B_doong2daddy/status/2105711764641833238）。

接入时，在插件中心点击 Finance 插件，在 Plaid 弹窗里选银行并完成双重认证。从协议层面看，Plaid 仅提供只读凭据，Bot 无法直接发起转账交易，也不能修改银行账户设置。

除了只读查账，Grok Bot 在 **v0.71.2（2026-10-14）** 中正式打通了主动结账支付链路，支持在结账环节调用 **Link 与 X Money** 完成付款（需用户审批），详见官方更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与工作流技术文档（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。根据官方说明，Bot 执行结账支付（Checkout / Payment）时的调用优先级顺序依次为：**Vault（内置加密保险箱） → 聊天内 Secure Form（掩码安全表单） → Link / X Money → Take over screen（人工接管屏幕）**（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。社区用户 `@gofordylan` 实测晒单发现，当使用 X Card 经由 Grok Bot 完成消费后，账单交易流水中会自动显示一枚专属的 **Grok Bot 小徽章**，方便一眼区分哪些消费是由 Bot 代理完成的（[https://x.com/gofordylan/status/2110726444485607797](https://x.com/gofordylan/status/2110726444485607797)）。更重要的是，针对用户对 AI 代购与绑卡安全的顾虑，Elon Musk（`@elonmusk`）于 2026 年 10 月 15 日公开发帖做出了极其硬核的赔付承诺（[https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445)，17,221 赞 / 1,686 转发 / 2,128 书签）：*"This works well. If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole."*（如果 Grok Bot 在代购时出错或泄露了你的银行卡——迄今从未发生过——SpaceX 将全额赔付。）

Plaid 只读连接后的支出汇总与日志脱敏。

这里出现过一起真实的数据泄露事故——XMTP Labs CEO Shane Mac 银行数据泄露事件（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。Mac 把个人银行账户连入 Grok Bot 当财务助理，以为只读权限很安全。但同一个账号下的所有 Bot 共用同一台云电脑与文件系统（https://cursor.com/help/grok-bot/computer-and-apps）。按 Mac 本人的解释，另一个 Bot 因此拿到了财务数据，Grok Bot 以他的名义把包含健身房会费、装修开销和刷卡支出的月度审计发进了公司 Slack 频道（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。**只读权限绝对不等于数据不会被转发泄露**，个人银行账户绝不能与包含团队协作工具的账号共用同一套运行环境。

## 10.9 1Password、Microsoft Teams 与 Salesforce 等企服生态 · Enterprise Services

2026 年 9 月 17 日，官方支持了 1Password 集成，Bot 可以在云电脑浏览器中受控调用指定保险库的账号密码登录，真实凭据留在密码管理器中（https://x.com/bot/status/2100335532597502311）。企业管理员在 cursor.com/dashboard/bot 开通 Grok Bot（https://x.ai/news/grok-bot-for-enterprise）；后台的 Setup Checklist 包含插件、Slack 或 Microsoft Teams、网络设置等步骤，Routine 也可以由 Microsoft Teams 消息触发（changelog 8/12、9/16，https://x.ai/changelog/bot）。（原稿称企业公告写了"统一部署 Salesforce 插件同步 CRM、配置 Teams 插件发早报"，公告原文没有这些内容，已改。）

在早期版本接入 1Password 时，需要在客户端单独建一个专用共享保险库（例如命名为 `Grok Bot` 或 `Shared with Grok Bot`）并配置 Service Account 令牌，只把允许 Bot 使用的凭据移进去（https://learngrokbot.com/plugins）。随后在 Grok Bot 中关联扩展，每次 Bot 尝试提取密码并执行自动填充时，系统都会向用户弹出单独的审批确认卡（https://x.com/bot/status/2100335532597502311）。企业版管理员可以在 Team Marketplace 管理团队可用的插件、配置网络策略（https://cursor.com/docs/grok-bot/teams-and-enterprises）。

到了 **2026 年 10 月 22 日（v0.75.2）与 10 月 23 日（v0.75.5）**，官方在凭据安全与个人设备生态上完成了三次重大跃升（官方文档：[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)、[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)、[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）：

1. **1Password Brokered Sign-in（1Password for Agents，v8.12.42+ 免共享库逐次授权登录）**：2026 年 10 月 22 日，1Password 官方发布 `"1Password for Agents"` 架构并将 Grok Bot 作为首发合作伙伴（`@1Password` 官宣帖：[https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)，10,507 赞 / 1,076 转发 / 7,122 书签；`@bot` 官宣帖：[https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874)，3,663 赞 / 276 转发 / 964 书签）。在新版 **Brokered approval** 模式下，你**不再需要新建共享密码库（shared vault）或配置 Service Account 令牌**。只需在本地设备安装并解锁 **1Password v8.12.42 或更高版本**，通过 `Settings → Connect apps → 1Password → Connect` 绑定；当 Bot 需要登录网站时，会弹出 **Review in 1Password**，你在手机或电脑的 1Password App 内用指纹/面容或 Passkey 逐次批准，凭据即直接注入云端浏览器，Bot 全程看不到明文密码。注意该模式默认读取已连接账号下的 **Personal / Private vault（个人/私有库）**，此前使用旧版共享库方案的用户只需在 `Settings → Connect apps` 中 Disconnect 再 Reconnect 即可切换至新版。社区用户 `@oxpsats`（偶像派作手，[https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670)）利用 1Password 授权彭博社（Bloomberg）会员凭据，让 Bot 自动登录突破付费墙研读海外财经研报；`@JCOMBuilds`（[https://x.com/JCOMBuilds/status/2112997408510452123](https://x.com/JCOMBuilds/status/2112997408510452123)）则每天早晨按 iPhone Action Button 语音呼出助理 Bot `"Eve"`，自动调用 1Password 凭据为妻子下单星巴克。
2. **内置 Grok Bot Vault（v0.75.5 加密只写保险箱）与“一密一宅”黄金法则**：官方于 2026 年 10 月 23 日上线 `Settings → Vault`（`@bot` 官宣帖：[https://x.com/bot/status/2113754107861532677](https://x.com/bot/status/2113754107861532677)，9,398 赞 / 767 转发 / 2,756 书签；官方文档：[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)），支持加密只写（write-only）存储 **Logins（账号密码与 2FA/TOTP）**、**Cards（银行卡，支持移动端摄像头 Scan 扫卡识别）** 与 **Contact info（收货地址与电话）**，支持从 1Password、Chrome、Safari、Firefox、Bitwarden、LastPass 批量导入 **5 MB 以内的 CSV**，并支持为每个条目添加 Bot 可读的明文 **Hint**（如 `"Corporate Amex"`）。官方技术文档（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）明确了登录时的调用优先级：**已保存的浏览器会话 → Vault → 1Password → 聊天内 Secure Form → 人工接管屏幕**。**务必警惕的核心风控边界**：根据官方文档（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）记载以及社区博主 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）与 `@JianWeiSignal`（见微｜Signal，[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)）的重点提醒，**保存在 Vault 中的银行卡在结账调用 `BrowserSecureFill` 自动填充时，不会触发单独的逐笔 Vault 弹窗确认**（仅受通用购买审批规则约束）；若你希望每笔消费都亲手确认卡号，切勿将主力信用卡常驻保存在 Vault 中。对此，`@martinpaulweiss`（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）提出了广受好评的 **“一密一宅（One home per secret）”拆分法**：日常网站登录与 2FA 全部放在 1Password；Grok Bot Vault 仅存放特定限额卡与收货地址；新注册的临时账号暂存 Vault，事后统一迁入 1Password。
3. **iOS 原生 Calendar / Reminders / Contacts 直连（v0.75.2）**：根据官方更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与移动端指南（[https://cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)），Grok Bot iPhone 客户端在获得系统授权后，可直接读写手机本地原生的 **Calendar（日历）**、**Reminders（提醒事项）** 与 **Contacts（通讯录）**。社区用户 `@TyeInBloom`（[https://x.com/TyeInBloom/status/2113767679588770271](https://x.com/TyeInBloom/status/2113767679588770271)）将 iOS 原生三件套、1Password 逐次授权登录、iPhone Action Button 一键语音以及 `"Hey Siri"` 专职 Bot 快捷指令组合在一起，打造出全功能随身 AI 秘书。

1Password 专用库登录时的审批与日志脱敏。

有社区帖提到，曾有用户在多 Bot 群聊里误输入明文密码，导致同一群组的所有 Bot 全部捕获到了凭据（个例）（https://x.com/i/status/2107339523038331338）。**绝不能在共享群聊中向 Bot 发送明文凭据**，任何外部访问必须通过专用的密码库或环境变量 Secrets 管理。在对接 Salesforce 等关键业务数据库时，如果后台未设置严格的字段级只读策略，Bot 误操作可能会覆盖销售阶段与客户线索。此外，在企业级安全治理上，根据官方安全文档（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)），管理员在配置云端虚拟机出站域名白名单（如 `*.domain.com:443`）时，现可勾选 **`Apply to MCP servers`** 将网络白名单强制同步至所有 MCP 服务器调用，并可配置自然语言团队 Auto-Review 规则（设为 `Block` 或 `Require approval`）以及通过 `cursor.surface=grok_bot` 过滤 OpenTelemetry 审计遥测事件。


# §11 中国用户的集成：没有插件也能用 · China Integrations

> 说明：国内平台没有官方连接器，所以本章大部分内容来自社区帖和第三方教程，标。使用前请自行核实，并注意平台规则。

国内用户打开 Grok Bot 的连接器市场，大概率会傻眼：除了 Gmail、Notion、Slack、GitHub 和 X，没有任何国内常用软件。微信、飞书、公众号、小红书、抖音、视频号全都没有插件，连 QQ 邮箱和网易邮箱也找不到原生入口。很多人看到这里就打了退堂鼓，觉得这套工具在国内根本没法用。

但如果你调研一圈就会发现，Grok Bot 的核心价值本来就不是那几个官方插件，而是那台 7×24 小时常驻在云端的虚拟电脑。只要云电脑能发网络请求、能开浏览器、能跑脚本，就算国内平台没有官方接口，也能把工作流搭起来。尤其在官方推出 **The X Subscription 三合一统一订阅**（见 [The X Subscription 总览](https://cursor.com/help/the-x-subscription/overview) 与 [Grok Bot 档位说明](https://cursor.com/help/grok-bot/plans)，中文版见 [https://cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）之后，**Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 档位把 Grok、Cursor 和 X Premium 整合进同一个共享周额度池（超出部分通过 `grok.com/dashboard/billing` 预充值的 Prepaid Credits 扣除；既有独立 Cursor Pro $20 / Pro+ $60 / Ultra $200 / Teams $40 老订户可保留原计划，或通过 `cursor.com/unify` 单向升级且不可逆）。这意味着国内开发者与创作者可以用同一套订阅同时驱动云端 Grok Bot 与本地 Cursor CLI。这一章把社区摸索出来的国内平台接入方案、故障表和合规边界完整整理出来。

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

第二步，配置通信凭据。Grok Bot 建好名为「微信下旨入口」的 Webhook Routine 后，会让你去 Routine 面板复制两样东西：Webhook URL 是消息接收地址，key 是身份凭据（https://xput.app/N4rlhi）。别在普通聊天框里直接发明文密钥。Grok Bot 会弹出一个专属加密输入框，把 URL 和 key 贴进去提交即可（https://xput.app/N4rlhi）。此外，根据官方 v0.75.2 更新说明（[https://x.ai/changelog/bot](https://x.ai/changelog/bot) 与 [Routines 帮助文档](https://cursor.com/help/grok-bot/routines)），Routine 的小时级触发频率上限已大幅上调至**全账号所有 Bot 合计 300 次/小时，单条 Routine 最高 200 次/小时**（定时触发最小间隔仍为 5 分钟），因此在微信里连续高频与 Bot 对话发指令时，Webhook 触发不再容易撞上小时级频控上限。

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

iLink 转发部署、长时间保活与 -14 重新扫码。

## 11.2 飞书 · Feishu

很多国内团队日常重度依赖飞书。但在 Grok Bot 官方插件市场里，目前找不到飞书连接器（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

没有官方插件时，社区最通用的方案是利用飞书群的「自定义机器人 Webhook」（https://x.com/KinGao476942/status/2100224440948916593）。在群设置里加一个自定义机器人，就能拿到形如 `https://open.feishu.cn/open-apis/bot/v2/hook/...` 的推送地址。在 Grok Bot 里配好日常巡检或分析的 Routine 后，任务最后加一段脚本，把结果用 HTTP POST 推到群 Webhook 即可。

这里有个频控限制要卡住：**飞书目前没有官方插件**，第三方教程称飞书自定义机器人 Webhook 有约每分钟 20 条的频控限制（aitoolku 飞书接入教程，https://www.aitoolku.cn/tutorials/grok-feishu，需以飞书开放平台文档为准）。如果多个 Bot 集中推送日志或轮询过密，容易触发 HTTP 429 限流导致消息丢失。写提示词时要让 Bot 合并推送内容，不要逐行刷屏。

省额度方面，铁柱 AGI 的思路是让脚本负责轮询，有变化才用 webhook 唤醒 Bot，不要让 Bot 自己高频盯消息（铁柱AGI 文章转载，https://readcopilot.ionichina.com/articles/53772）。放到飞书上，就是把飞书当通知出口，而不是让 Bot 监听群里每一条消息。邮件这条路有人这样做：用收信规则过滤掉敏感邮件，再把常用邮箱（含飞书邮箱）转发给 Bot 的 agent mail，让它每天总结提醒（https://x.com/i/status/2106774095820095969）。Kin 也分享过让 Grok Bot 抓取视频、转写文案并存进飞书知识库的用法（https://x.com/KinGao476942/status/2100224440948916593）。

除了单向群通知，国内研发团队已经将飞书升级为工程研发流水线的上下文中枢。开发者 `@realbenzh`（Ben Zhang）在 2026 年 10 月 17 日分享了一套将 **飞书（Feishu）+ Linear + 电子邮箱 + 团队文档** 统一接入 Grok Bot 的真实工程研发工作流（[https://x.com/realbenzh/status/2111295936635015631](https://x.com/realbenzh/status/2111295936635015631)）。在他的架构中，Grok Bot 不再只是个传话筒，而是扮演研发项目经理与构建调度员：

1. **多源上下文汇聚**：通过飞书 API / Webhook 与团队文档读取日常业务讨论和 PRD 变更，结合官方原生支持的 Linear 连接器与邮箱（详见官方 [Connect Apps 指南](https://cursor.com/help/grok-bot/connect-apps)），将分散在国内协作工具（飞书）与海外工程工具（Linear）中的碎片需求拉齐到同一个会话窗口。
2. **对话层对齐验收标准（Acceptance Criteria）**：在动工写代码前，先在 Grok Bot 聊天窗口里与 Bot 多轮探讨，把飞书文档里模糊的产品诉求收敛为可验证的交付目标和验收标准。这也契合了中文社区 `@Khazix0918`（[https://x.com/Khazix0918/status/2111709708226797737](https://x.com/Khazix0918/status/2111709708226797737)）与 `@object_nullll`（[https://x.com/object_nullll/status/2111717423837778173](https://x.com/object_nullll/status/2111717423837778173)）关于“对话层负责对齐上下文与验收标准，重度干活交由底层 CLI 或 Cloud Agent”的架构共识。
3. **驱动 `@orca_build` CLI 完成构建交付**：验收标准确认后，Grok Bot 在云电脑或关联的开发机上通过命令行交互式驱动 `@orca_build` CLI 执行代码构建、测试与打包，完成后再将构建产物与 Linear 状态变更同步回飞书群。

如果你也想复刻 `@realbenzh` 的飞书 + Linear + CLI 研发闭环，可以直接使用下面这套任务编排提示词模板：

```text
你现在的角色是研发交付主控（Engineering PM Bot）。每当收到新的功能需求或修复任务时，请严格按以下四步执行：

1. 收集跨端上下文：
   - 读取我在飞书文档/群汇总脚本中同步过来的最新业务需求说明；
   - 查询 Linear 中关联的 Issue 状态、历史评论与子任务；
   - 检查专属邮箱中是否有相关的客户报错或补充邮件。

2. 对齐验收标准（Acceptance Criteria）：
   - 不要立刻开始写代码或调 CLI！先向我输出一份结构化的【交付目标与验收清单（AC）】，列出边界条件、改动范围与测试标准，等待我回复“确认”后再进入下一步。

3. 驱动 CLI 构建：
   - 在获得我的确认后，在终端通过非交互式或受控会话调用构建工具（如 orca_build / cursor-agent），将对齐好的 AC 作为输入指令执行构建与自测。

4. 结果回填与飞书通知：
   - 构建与测试通过后，更新 Linear Issue 状态，并将【变更摘要 + PR/构建链接 + 验收结果】合并成一条结构化消息，通过 HTTP POST 推送到飞书群自定义机器人 Webhook（注意合并发送，遵守飞书每分钟 20 条以内的频控限制）。
```

飞书 webhook 推送在频率限制下的表现。

## 11.3 公众号、小红书、抖音、视频号：四种数据入口 · No-Plugin Playbook

国内创作者用 Grok Bot 最容易犯的错误，是直接对它说「看下我昨天公众号的阅读量」或「抓下小红书这篇笔记的完播率」。这种指令发过去，Bot 要么胡编，要么一直卡在页面重试（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

原因很简单：微信公众号、小红书、抖音、视频号在 Grok Bot 插件市场里全都没有，而且平台后台不对海外第三方工具开放粉丝画像、完播率或后台阅读量的标准 API（https://xiangyugongzuoliu.com/grokbot-use-cases/）。随手丢一条 `mp.weixin.qq.com/s/xxxx` 公开链接，源码里只有正文和标题，根本没有后台的阅读数、完读率和分享量（https://xiangyugongzuoliu.com/grokbot-use-cases/）。**阅读量与完播率不在公开页面上，国内创作者平台必须依赖四种替代入口**。

面对国内平台，创作者博主翔宇总结出了四种可行的数据接入方式（https://xiangyugongzuoliu.com/grokbot-use-cases/）：

![国内自媒体平台四种数据入口与风险对照表](../images/fig-11-1.png)

*图：国内自媒体平台四种数据入口与风险对照表*

| 入口类型 | 具体怎么做 | 适合获取的数据 | 严禁与风险项 |
| --- | --- | --- | --- |
| 1. 公开 URL 喂入 | 整理 10-20 条已发公开文章/笔记链接，让 Bot 抓取正文分析文风与结构 | 文章标题、公开发布的正文排版、公开可见的点赞与评论 | 严禁指望它从公开链接猜出后台阅读量与完播率 |
| 2. 导出表格或截图 | 人工登录创作者后台，导出 CSV/Excel 数据表或截取数据看板图片拖入对话框 | 真实阅读量、完播率、用户停留时长、粉丝画像 | 严禁让 Bot 凭空估算；没给表格时必须强制其标注 UNSURE |
| 3. 已登录后台窗口 | 在云电脑的自带浏览器中人工完成扫码登录，让 Bot 控制页面阅读屏幕表格 | 无导出功能的系统后台界面数据、待办工单列表 | 严禁用于高频例行任务；自动化点击极易触发平台验证码与风控封禁 |
| 4. 人工发布与审批 | Bot 仅负责输出选题简报与候选文案草稿，最终审核与发布按钮留在人工端 | 选题策划案、初稿排版、分发版本文案适配 | 严禁让 Bot 自动点击最终发布、回复私信、批量点赞或发起支付 |

处理微信公众号时，可以把历史文章的公开链接汇总给 Bot 分析文风，但别让它替你去创作者后台爬数据（https://xiangyugongzuoliu.com/grokbot-use-cases/）。小红书公开页面能看到点赞和收藏，曝光量和完播率得靠后台截图或表格（https://xiangyugongzuoliu.com/grokbot-use-cases/）。抖音和微信视频号的口播文案可以用转录脚本提取，完播指标同样锁在创作者服务中心里（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

这里最容易踩坑的是平台风控。国内内容平台对海外机房 IP 和无头浏览器非常敏感。如果把后台登录态交给 Bot 并挂高频 Routine 刷页面，云电脑会频繁弹出滑块验证码，账号也容易被判定异常遭封禁。最稳妥的做法始终是：人工导出数据喂给 Bot 诊断，Bot 产出内容后再由人工点击发布（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

Bot 解析公众号公开文章链接的效果。

### 11.3.1 公众号日更与香港政务/生活 8 线并行实战（`@bitman2140` 案例）

虽然不能让 Bot 强刷微信公众号后台数据，但把 Grok Bot 当成“全自动内容情报与排版中枢 + 跨境生活政务秘书”却能跑出极高的生产力。博主 `@bitman2140`（0xbitman）在 2026 年 10 月 25 日分享了他一人在 Grok Bot 上同时跑通的 **8 大真实生活与创作工作流**（[https://x.com/bitman2140/status/2114210291546493153](https://x.com/bitman2140/status/2114210291546493153)）：

1. **微信公众号日更运营**：利用 Grok Bot 每日抓取海内外一手信源，按预设个人文风自动完成公众号选题策划、初稿撰写与微信 HTML 排版生成，人工只需最后审阅并复制进公众号后台点击群发。
2. **X 平台同步发帖运营**：将同一套核心素材“一鱼多吃”，自动拆解改写为适合 X 传播的短帖与长推（Thread）。
3. **每日 AI 情报简报**：通过定时 Routine 每天汇总全网 AI 动态，为公众号与 X 源源不断提供弹药。
4. **随时随地灵感捕捉**：日常通勤或阅读时随手把碎片想法丢给 Bot 归档入库，自动沉淀为后续文章选题。
5. **香港优才计划（Quality Migrant Admission Scheme）续签材料跟进**：针对大湾区与跨境用户极其头疼的香港入境处续签政策、材料清单核对与时间节点提醒，专门建立长期跟踪项目，让 Bot 持续梳理证明文件缺口。
6. **香港孩子学校插班（School Transfer）信息搜集与申请**：让 Bot 定时巡检香港各目标中小学的插班开放日期、报名简章要求与面试准备资料，汇总成对比表格（甚至可直接用官方 v0.75.2 上线的 **Pages** 画布生成实时追踪看板，见 [官方 Changelog](https://x.ai/changelog/bot)）。
7. **考试备考辅导**：根据考纲定制每日练习题、错题解析与复习计划。
8. **全栈写代码开发**：在写作与处理家庭事务之余，随时调度云电脑完成全栈项目编码。

同理，中文社区的 `@CyberAlice3269`（夏哥研究室）也验证了 **“1 个 CEO Bot + 5 个专职 Bot（情报搜集、选题策划、初稿撰写、审校润色、配图制作）”** 的 6-Bot 自媒体内容工作室架构（[https://x.com/CyberAlice3269/status/2112098767151468645](https://x.com/CyberAlice3269/status/2112098767151468645)），全员共享同一套知识库与 SOP，再结合 v0.71.2 上线的原生 **Grok Imagine** 生图生视频与代码动效渲染能力（[https://x.com/bot/status/2110566041772617908](https://x.com/bot/status/2110566041772617908)），无需任何国内平台插件即可跑通端到端内容工厂。

### 11.3.2 突破机房 IP 封锁与硬件外设直连（`@XueshiQiao` 本机住宅 IP 路由与 `@guoxudong_` ESP32 语音盒子）

在实际访问公众号文章、知乎、小红书公开页或部分对数据中心 IP 设防的海内外网站时，Grok Bot 云电脑自带的机房 IP 经常会撞上反爬拦截或无限验证码。同时，国内用户也希望在不打开复杂客户端的情况下用语音随时调度 Bot。社区在 2026 年 10 月中下旬摸索出了两套极其实用的网络与硬件破局方案：

#### 方案 A：开启 `Route traffic through this computer` 借用本机住宅 IP 绕过反爬拦截（`@XueshiQiao`）
开发者 `@XueshiQiao`（Xueshi）在 2026 年 10 月 21 日指出（[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)），当云端浏览器因机房 IP 被目标网站封锁或频繁弹出 Captcha 验证码时，根本不需要在云电脑里折腾复杂的第三方住宅代理池，只需直接启用 Grok Bot 桌面端内置的本地流量转发功能（详见官方 [Settings 文档](https://cursor.com/docs/grok-bot/settings) 与 [v0.75.5 更新日志](https://x.ai/changelog/bot) 对本地电脑流量转发的稳定性修复）：

1. 在你家里或办公室的电脑上安装并打开 Grok Bot 桌面客户端（或像官方工程师 `@ericzakariasson` 推荐的那样，在家里常开的 Mac mini 上保持登录，见 [https://x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099)）。
2. 依次进入 **`Settings > Computer > Your computer`**。
3. 勾选开启 **`Route traffic through this computer`**（通过本机路由流量）。

开启后，云端 Bot 浏览器的出站网络请求会直接通过加密隧道走你本地电脑所在的真实家庭宽带/办公网络 IP（住宅 IP），绝大多数针对云机房数据中心 IP 段的反爬拦截与滑块验证都会迎刃而解。对于有内网 NAS 或私有服务访问需求的进阶玩家，还可以参考 `@lyuan1618` 的方案（[https://x.com/lyuan1618/status/2114214704008798674](https://x.com/lyuan1618/status/2114214704008798674)），在 Grok Bot 云电脑中配置 **Tailscale** 与本地家庭内网组建私有 Mesh 局域网。

#### 方案 B：ESP32 开源硬件语音盒子 + Cloudflare Tunnel + 本地 MCP 2 分钟接通 Grok Bot（`@guoxudong_`）
如果你不仅想在手机上按 iPhone Action Button 语音呼出 Bot（官方 v1.16+ 已原生支持，详见 [Voice Chat 指南](https://cursor.com/help/grok-bot/voice-chat) 与 `@bot` 公告 [https://x.com/bot/status/2112246033178968161](https://x.com/bot/status/2112246033178968161)），还想在书桌或客厅摆一个像智能音箱一样的独立硬件语音盒子，国内极客 `@guoxudong_`（Xudong Guo）在 2026 年 10 月 18 日展示了一套 **2 分钟跑通全链路的 ESP32 硬件接入方案**（[https://x.com/guoxudong_/status/2111767457560215771](https://x.com/guoxudong_/status/2111767457560215771)）。

其完整数据链路无需公网固定 IP，全靠 **Cloudflare Tunnel** 与本地 **MCP Server** 串联：

```text
[桌面 ESP32 硬件语音盒子（拾音/播报）]
       │
       ▼ (1) 音频流经 Cloudflare Tunnel 穿透回传
[家里常开的 Mac 本地节点]
  ├── 本地 Speech-to-Text (STT) 语音转文字
  └── 本地 MCP Server 封装指令与工具接口
       │
       ▼ (2) 经 Cloudflare Tunnel 双向桥接
[云端 Grok Bot 虚拟电脑 (Cloud Box)]
  └── 解析自然语言指令 → 调取工具/执行工作流 → 将结果原路返回播报
```

通过这套架构，你在国内网络环境下对着桌面的 ESP32 小盒子说一句话，本地 Mac 完成极速语音识别并通过 Cloudflare Tunnel 与云端 Grok Bot 交互，不到 2 分钟就能搭建起一套不依赖任何国内智能音箱厂商生态的私人 AI 硬件终端。

## 11.4 QQ 与网易邮箱 · Domestic Email

国内很多业务通知和账单都在 QQ 邮箱或网易 163 邮箱里。但 Grok Bot 连接器里只有 Gmail 和 Outlook，没有国内邮箱（https://xiangyugongzuoliu.com/grokbot-use-cases/）。**国内邮箱无法直接直连插件，必须通过自动转发、网页版登录或导出文件处理**（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

第一种做法是设置自动转发。在 QQ 邮箱或 163 邮箱设置里建分流规则，把特定发件人或关键词的邮件自动转到绑了插件的 Gmail、Outlook，或者直接转给 Grok Bot 的专属邮箱（https://x.com/i/status/2106774095820095969，https://x.com/i/status/2109320438807670985，官方专属邮箱机制详见 [Agent Email 帮助文档](https://cursor.com/help/grok-bot/agent-email)）。转发前要建好排除规则，过滤掉网银账单、找回密码和验证码邮件。

在 2026 年 10 月中下旬的两次关键版本迭代中，Grok Bot 的专属邮箱 `@mail.grokbot.com` 迎来了两项彻底改变国内邮箱转发体验的重磅升级：

1. **v0.71.2 新增 `+alias` 加号子别名与定向 Routine 触发**（见 [官方 Changelog](https://x.ai/changelog/bot)、[Agent Email 文档](https://cursor.com/help/grok-bot/agent-email) 及官方工程师 `@SamSokolin` 发布帖 [https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)）：现在你的 Bot 专属邮箱原生支持在 `@` 符号前添加任意 `+tag` 后缀（例如你的基础地址是 `mybot@mail.grokbot.com`，你可以直接使用 `mybot+qqbills@mail.grokbot.com`、`mybot+163work@mail.grokbot.com` 或 `mybot+newsletters@mail.grokbot.com`）。更重要的是，**在配置邮件触发的 Routine 时，可以指定仅当收件地址匹配某一个具体的 `+alias` 别名时才唤醒该 Routine**。
2. **v0.75.2 支持原样保留完整 HTML 排版、正文内嵌图片与文件附件转发**（见 [官方 Changelog](https://x.ai/changelog/bot) 与 [Agent Email 文档](https://cursor.com/help/grok-bot/agent-email)）：过去通过 Agent Email 转发带复杂表格、内嵌二维码/截图或 PDF 发票附件的国内通知邮件时，容易出现纯文本化导致排版丢失或附件脱落的问题；自 v0.75.2 起，无论使用 `@mail.grokbot.com` 还是已连接的外部邮箱转发邮件，系统都能原封不动地保留原始 HTML 样式、内嵌图片（inline images）与全部附件。

结合这两项新特性，国内 QQ 邮箱与网易 163/126 邮箱的自动转发分流架构可以升级为“**一邮箱多 `+alias` 管道**”精准路由模式（这也是 `@AIShovelLab` 总结的六大核心联动范式之一，见 [https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)，以及 `@songsong275452` 引用 `@gokul_i` 的 Newsletter 隔离周报方案，见 [https://x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371)）：

```text
[QQ 邮箱 / 网易 163 邮箱「收信规则」自动转发配置示例]

规则 1（电子发票归集）：
- 条件：主题包含「发票」或「电子客票」，且不含「验证码 / 密码」
- 动作：自动转发至 → mybot+invoices@mail.grokbot.com
- 对应 Grok Bot Routine（仅监听 +invoices）：提取邮件内嵌图片或 PDF 附件中的金额、税号与开票日期，记入月度报销 Page 看板，并将原邮件（保留完整 HTML 与 PDF 附件）原样转发给财务邮箱。

规则 2（工作项目通知）：
- 条件：发件人来自公司域名或客户域名
- 动作：自动转发至 → mybot+work@mail.grokbot.com
- 对应 Grok Bot Routine（仅监听 +work）：提炼待办事项，同步至飞书群 Webhook 或 iOS 原生提醒事项（v0.75.2 支持）。

规则 3（行业订阅与 Newsletter）：
- 条件：来自各类日报、周刊订阅源
- 动作：自动转发至 → mybot+digest@mail.grokbot.com
- 对应 Grok Bot Routine（不设单封触发以节省 The X Subscription 周额度，改为每周六早 9:00 定时运行）：一次性汇总本周所有发往 +digest 的邮件，生成结构化中文精华周报。
```

第二种做法是在云电脑浏览器里开网页版邮箱（比如 `mail.qq.com` 或 `mail.163.com`），手动扫码登录（https://xiangyugongzuoliu.com/grokbot-use-cases/）。如果你需要用账号密码登录，自 v0.75.2 和 v0.75.5 起，官方已上线 **1Password Brokered Sign-in**（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）与内置加密保险箱 **Grok Bot Vault**（`Settings → Vault`，详见 [Secrets & Vault 官方文档](https://cursor.com/help/grok-bot/secrets)），可通过 `BrowserSecureFill` 安全注入凭据而不让 Bot 在上下文里看到明文密码。在给 Bot 的提示词里严格限制权限：只准读未读邮件标题整理清单，不能删邮件，更不能对外发邮件。

第三种做法是手动导出。附件较多或对账时，在本地把邮件存成 `.eml` 或提取表格，拖到云电脑 `/workspace/` 目录下让 Bot 离线解析。多了一步人工，但不会泄露登录态，也不会误发邮件。

163 邮箱转发到 Gmail 后的摘要 Routine。

## 11.5 合规与数据出境 · Compliance

把国内工作流接进 Grok Bot 前，有几道安全底线必须想清楚。

先看网络链路。国内评测媒体提到，`x.ai/bot` 和 `cursor.com/docs/grok-bot` 在部分国内网络下能直接打开（https://www.ai345.info/ai-guide/grok-bot-china-guide）。但这不代表数据在境内处理。Grok Bot 的云电脑本质是境外机房虚拟机，走的是海外机房 IP（https://x.com/i/status/2099409639234289914），网络连接稳定性因地区和运营商而异。

再看数据合规。**境外云电脑不属于安全沙箱边界，国内团队调用前必须评估数据出境合规**（https://www.ai345.info/ai-guide/grok-bot-china-guide）。把未公开的客户联系人、内部代码、财务流水或国内系统凭据交给 Grok Bot，数据就实质离开了境内边界。企业使用时要对照《数据安全法》和《个人信息保护法》做风险评估，不能把敏感客户隐私或核心数据库权限直接交给云端 Agent（https://www.ai345.info/ai-guide/grok-bot-china-guide）。在企业级安全治理方面，官方在 [Security 技术文档](https://cursor.com/docs/grok-bot/security) 中披露，平台已通过 **ISO/IEC 27001** 与 **ISO/IEC 42001** 认证，且团队管理员可配置出站网络域名白名单（并勾选 `Apply to MCP servers` 强制约束所有 MCP 服务器流量）、自定义自然语言 Auto-Review 阻断规则以及推理审计钩子（Inference Hooks）。

多 Bot 架构也有权限边界风险。官方文档写明，同一个账号下的所有 Bot 共享同一台云电脑，文件目录、浏览器 Cookie 和登录态全量互通（https://cursor.com/help/grok-bot/computer-and-apps）。Bot 之间没有权限隔离。如果一个 Bot 登录了内部系统，另一个有联网权限的 Bot 同样能读取这些 Cookie 和登录态。此外，在使用 v0.75.5 新增的 `Settings → Vault` 存储支付卡时，务必留意官方 [Secrets & Vault 文档](https://cursor.com/help/grok-bot/secrets) 标注的规则（中文社区 `@JianWeiSignal` 在 [https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488) 以及英文社区 `@kial` 在 [https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280) 也专门发出过提醒）：**保存在 Vault 中的银行卡在结账自动填充时，不会触发单独的逐笔 Vault 弹窗确认**。因此，国内用户切勿将主力信用卡常驻保存在 Vault 中，建议参考 `@martinpaulweiss` 的“一密一宅（One home per secret）”原则（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)），将重要登录凭据放在每次都需要生物识别审批的 1Password（`Settings → Connect apps → 1Password`）中。

在没有原生插件的环境下用 Grok Bot，要守住四条底线：一是绝不让云电脑登录网银、核心财务或高权限管理账号；二是资金支付、发正式邮件、合并代码等敏感操作必须人工二次确认；三是不需要联网的历史数据，清洗脱敏后再以文件交付；四是始终认清云电脑在境外的属性，守住合规底线。


# §12 群聊与交接 · Groups & Handoffs

## 12.1 建群 · Groups

如果只在侧边栏单独点开每个 Bot，开四五个窗口切着派活：写代码找 Coder，查资料找 Researcher，写文案找 Writer。单兵作战还行，一旦多角色协作，人就成了“人肉中继器”，得把 Researcher 找的链接复制给 Writer，再把初稿粘给 Reviewer。为了让多个 Bot 一起干活，官方提供了群聊功能（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。

桌面端建群很简单。在侧边栏顶部点“New”，在弹出的面板里勾选 2 到 6 个 Bot 就行（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。官方设计文章写得很明确：每个群上限 6 个 Bot（[designing-grok-bot](https://x.ai/news/designing-grok-bot)）；文中提到的"每账户约 50 个 Bot"已在 9 月 1 日 v0.31.0 取消（[changelog](https://x.ai/changelog/bot)）。手机端点“+”号选“New Group Chat”也能建。建完后默认群名随时能改，之后也能在群信息里调整成员（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。

进群后怎么派活？主要靠群发和点名。直接发自然语言，群里的 Bot 会自己判断谁来接话；明确知道某一步该谁做，就敲“@”选对应的 Bot（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。一条消息能同时 @ 多个 Bot。不过“@everyone”会唤醒所有人，官方建议尽量少用，免得刷屏（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。想接某个 Bot 的话，点它发言下方的“Reply”定向回复（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。官方文档给过一个很规范的开工写法：先让 Researcher 收集素材并附来源链接，让 Writer 写发布初稿，再让 Reviewer 对照来源审查并只列阻塞项，最后明确卡上一句严禁对外发布（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。

很多人容易误以为群聊能干单聊的所有事。官方在交互边界上做了明确隔离：**审批请求、密钥与登录凭据申请，以及邮件或 Slack 草稿确认，绝不会出现在群聊中**（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。群里能发附件，Bot 也能回复文件、提问或表单，作答后会定向交还给提问的 Bot。但只要碰上高危权限审批、凭据输入或对外草稿放行，审批卡片只会单独发到你和该 Bot 的私聊里，避免多个 Bot 串扰（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。另外，目前 Bot 间交接只支持纯文本。如果某个 Bot 产出了图片想让另一个 Bot 看，必须走 1 对 1 单聊发图，不能指望群聊广播（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。此外，在实时语音通话（Live Voice Chat）维度，官方也划定了严格的会话边界：**同一时间仅支持一个活跃语音通话，且语音通话仅限 1 对 1 会话，群聊（Group Chats）内不支持直接发起语音通话**；如果你在团队协作中需要与队友共享的 Team Bot 语音沟通，可以在桌面端进入该 Team Bot 的 1 对 1 会话窗口发起语音通话（[Voice Chat 官方文档](https://cursor.com/help/grok-bot/voice-chat)，[Teams 团队治理文档](https://cursor.com/docs/grok-bot/teams)）。

再来看安全。群里的所有 Bot 共享同一台云电脑、文件系统和浏览器会话（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)）。群聊只是一个聊天视窗，根本没有权限隔离。社区里出过真实事故：有用户在全员群里误发了账号密码，导致这台云电脑上的所有 Bot 同时知道了这段敏感凭据（[X 原帖](https://x.com/i/status/2107339523038331338)）。另外别把这里的个人多 Bot 群聊和企业级的 Team Bots 搞混。Team Bots 是把做好的 Bot 共享给团队或接入 Slack 频道，让同事们各自拥有独立私聊并共享团队记忆，同时支持企业管理员通过团队治理后台统一管控（[Teams 团队治理文档](https://cursor.com/docs/grok-bot/teams)）；这里的群聊，是你一个人指挥多 Bot 协作攻坚的作战室。

在规划多 Bot 群聊编制时，还需要结合当前的订阅计费架构合理设计团队规模。自 2026 年 10 月 18 日官方推出 **The X Subscription 三合一统一订阅**（[官方公告](https://x.com/bot/status/2110063783796572496)，[The X Subscription 总览](https://cursor.com/help/the-x-subscription/overview)）以来，**Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 三档计划将 Grok Bot、Grok 与 Cursor 整合进同一个共享周额度池（Free $0 与 Plus $8/月 不包含 Grok Bot 权限），周额度耗尽后从 `grok.com/dashboard/billing` 充值的 **Prepaid Credits（预付额度）** 中扣减；而既有的独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及 Teams（$40/人/月）老订户虽可保留原计划，但一旦通过 `cursor.com/unify` 单向切换至 The X Subscription 即不可逆（[Plans 计费文档](https://cursor.com/help/grok-bot/plans)）。由于群聊内每个被唤醒的 Bot 都会消耗同一个周额度池，精准控制群成员数量与唤醒频次尤为关键。

> [!NOTE]
> 📸 **截图位（待补）**：在桌面端新建群聊面板中勾选 2 到 6 个 Bot 并配置群名称

测试不同数量 Bot 在同一群聊内连续触发异步协作时的端到端响应耗时。

## 12.2 "安静交接" profile 句式 · Quiet Handoff

拉几个 Bot 进群自动交接，最容易踩的坑是额度消耗失控。Cursor 官方论坛上有个典型求助帖（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)）。比利时电商 Angelo.be 的 CTO 在团队里配置了同事型 Bot（总助 Slaude、研发、设计、审核、文档、客服财务市场）和工具型 Bot（Shopify、Klaviyo、Vercel、迁移），任务挂在 Notion 看板上，通过自建 Slack 应用以 Socket Mode 转接消息。社区帖称短短一周时间，超额用量消耗了大约 1,500 美元（个例）（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)），发帖人怀疑计费系统出了故障。

Cursor 官方员工 @kevinn 调取后台数据后确认，计费系统没有任何异常（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)）。问题出在 Grok Bot 的运行机制上：每次轮到某个 Bot 发言，系统都会重读该会话完整的历史上下文（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)）。当时最忙的几个 Bot，每走一步都要重新加载约 8 到 9 万个 token，而且整个舰队约三分之一的轮次纯粹是 Bot 之间在互相唤醒（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)）。发帖人后续也确认，消耗大量 token 的不是外部轮询，而是历史上下文在每次消息流转时被全量重读（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)）。

大模型扮演人类同事时，天生带着客套习惯。A 做完一段研究交接给 B，顺口说一句“报告整理好了，请查收”；B 收到立刻回复“收到，非常感谢，我现在开始排版”；A 又回一句“不客气，辛苦了”。人类觉得礼貌，但在多 Bot 协作里很烧钱。每一次客套回复都是一次独立的唤醒轮次，每次唤醒都要重新吃进 8 到 9 万 token 的历史窗口。几个回合下来，账单就失控了。

官方员工给出的解法很明确：**在每个 Bot 的 Edit Profile 里必须写入安静交接指令以切断无谓的客套唤醒**（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)）。具体包含四项调整：第一，新任务开启全新对话，长期指令固化在 Edit Profile 里，任务状态放在 Notion 看板，总助 Bot 每天早晨开新对话并附带极简交接摘要；第二，在所有协作 Bot 的 Profile 中加入硬性交接规矩；第三，放宽 Routine 的触发频率，原本每 8 分钟或 30 分钟跑一次的检查，拉长到每小时或每天数次（尽管官方在 v0.75.2 中已将 Routine 的频率上限大幅上调至**全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时**，定时最小间隔仍为 5 分钟，详见 [Routines 官方文档](https://cursor.com/help/grok-bot/routines)，但 जैसा `@charlie_pmp` 在 [额度分析帖](https://x.com/charlie_pmp/status/2114214503416271131) 中所指出的，高频冗余的 Routine 依然是后台静默吞噬 The X Subscription 三端共享周额度池的头号元凶）；第四，随时在官方用量后台监控 token 消耗（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)）。

官方技术人员推荐把这段英文直接加进参与协作的 Profile 中：

```text
Only message another bot when it needs to act. No acknowledgments, thanks, or progress pings. Send one summary when the work is done.
```

如果使用中文环境，也可以在下方追加对应的中文约束：

```text
仅在需要对方执行具体动作时才向其他 Bot 发送消息。严禁发送“收到”、“谢谢”、“已开始处理”等无意义确认或进度闲聊。工作全部完成后，仅发送一份最终结果摘要。
```

社区开发者 @Zachariah 在该案例讨论中也提出了工程建议：尽量使用带有效负载的 Webhook 按需定向唤醒特定 Bot，而不是让 Bot 在群聊里死循环轮询；前置的路由与意图分类交给更轻量便宜的外部模型处理，避免主力 Bot 持续空转（[Cursor 论坛](https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)）。

测试多 Bot 连续交接任务在注入安静指令前后的上下文调用量与费用变化。

## 12.3 Chief of Staff 总助模式 · CoS

手头的 Bot 一多，人很容易被琐碎的调度吞没。官方团队成员 Roman Ugarte 在 Lenny 播客中提到，Chief of Staff（参谋长/总助，简称 CoS）模式不是团队自上而下预设的功能，而是在封闭内测第二周由早期用户自然用出来的协作形态（团队成员访谈，[Lenny 播客](https://www.youtube.com/watch?v=maSdsTLaMuU)）。大家不想当工头逐个催进度，最自然的办法是找一个大管家替你统管全盘。

Grok Bot 团队成员 Eric Zakariasson 写过一篇官方指南，公开了他管理多个 Grok Bot 团队的实践经验（[官方指南](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots)）。他发现把 Coder、Writer、Researcher 放在各自独立的对话里单线沟通，项目一多，有效信息就会被杂音淹没（[官方指南](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots)）。现实中人是通过项目来协作的，因此他把这种结构搬进了 Grok Bot：每一个项目对应侧边栏里的一个专属群聊频道，同时对应 Notion 数据库里的一条项目记录（[官方指南](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots)）。

在 Zakariasson 的架构中，Notion 里建了两个核心数据库：Projects（项目表）和 Tasks（任务表）（[官方指南](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots)）。所有业务 Bot 之上常驻着一个名为“projects”（复数）的项目管理 Bot，配有名为 Project Ops 的专业技能，负责全流程元工作：立项、建群、按需抽调适合的 Bot 组建编制（[官方指南](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots)）。他为这个大管家定下了三条严格的编制规则：第一，优先复用现有板凳席上的成熟 Bot，例如已有的 Coder、Researcher 或 Writer；第二，除了项目经理自身，每个频道最多只提名 5 个专业 Bot（他自己说"六个"是随手定的数字，"just an arbitrary number I came up with"，恰好也等于官方群聊上限）；第三，只有当现有专员都不匹配且得到人类明确确认后，才允许新建特定领域的专业 Bot（[官方指南](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots)）。群聊建好后，项目经理在群内默默跟踪进度并维护 Notion 状态，只有当某个专员 Bot 陷入卡点时，该 Bot 才会将任务标为 Blocked 并在群里呼叫人类介入（[官方指南](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots)）。

社区博主 0xRafy 将总助的标准工作流抽象为六步闭环：收集（Collect）→ 排序（Prioritize）→ 委派（Delegate）→ 追踪（Track）→ 升级（Escalate）→ 汇报（Report）（[0xRafy 帖子 A](https://x.com/0xRafy/status/2099278275906265417)，[0xRafy 帖子 B](https://x.com/0xRafy/status/2099986062806298991)）。向上汇报任何重要事项时，总助必须结构化提供三要素：信息源头（Source）、为何重要（Why it matters）、下一步建议（Next step）（[0xRafy 帖子 A](https://x.com/0xRafy/status/2099278275906265417)）。

对于中文用户，开发者李哈利总结过一个分工思路：**直接面向人类的总助 Bot 必须深刻理解你的个人偏好与决策习惯，而下层专职 Bot 只需要懂具体业务规则**（[李哈利视频](https://www.youtube.com/watch?v=8jkkCniMgBw)）。人类平时只与这一个总助对话，总助负责拆解建立专职助手（例如邮箱日历助手、任务看板助手）。下层各专员之间建立“线索直连”，彼此直接传递数据，而不是什么事都让总助倒手一遍，减少系统内耗（[李哈利视频](https://www.youtube.com/watch?v=8jkkCniMgBw)）。

官方团队的 @poteto 同样建议：起步时务必先只建一个 Bot，当管理复杂度真正提升、职责产生冲突时再去拆分专员，切忌一上来建一堆空壳 Bot（[poteto 帖子](https://x.com/poteto/status/2108097362283597916)）。如果你打算给总助开通专属邮箱，Peter Yang 建议给它起一个独立的英文名，不要用你自己的名字命名，否则在抄送邮件或向外沟通时会很不自然（[Peter Yang 帖子](https://x.com/petergyang/status/2108624122339287335)）。

![Chief of Staff 总助分层架构与任务流转图（人类 ↔ 总助 CoS ↔ 专职执行 Bot ↔ 外部看板系统）](../images/fig-12-1.png)

*图：Chief of Staff 总助分层架构与任务流转图（人类 ↔ 总助 CoS ↔ 专职执行 Bot ↔ 外部看板系统）*

可以直接复制以下 Profile 模板来配置总助 Bot：

```text
你是我的总管参谋长（Chief of Staff），你的唯一职责是组织协调、优先级排序与全局进展合成。
1. 收集各活跃任务的动态，梳理优先级，并将具体执行精准委派给专业 Bot。
2. 只有当任务状态被标记为 Blocked，或者涉及需要人类审批的安全边界时，才向我发起上报。
3. 每次上报必须包含三要素：数据来源（Source）、重要性评估（Why it matters）、下一步行动建议（Next step）。
4. 确保 Notion/外部看板的任务状态与实际执行保持同步。
5. 严格执行安静交接原则：非必要不打扰，指令直达专人，杜绝无意义客套。
```

测试总助在五个并发任务切换时同步 Notion 看板与任务指派的准确率。

### 12.3.1 Pages 实时看板总控模式 · CoS Activity Dashboard Page

以往，多 Bot 团队要么只能靠总助在群里发长段文字总结来同步进度，要么必须依赖外部配置 Notion 数据库。随着 2026 年 10 月 21 日（v0.75.2）官方正式推出 **Pages（内部由 `WriteCanvas` / `EditCanvas` / `ReadCanvas` / `ListCanvases` 工具驱动的实时交互画布）**（[官方公告](https://x.com/bot/status/2112991843235610885)，6,544 赞 / 567 转发 / 2,008 书签；[官方 Changelog](https://x.ai/changelog/bot)），**Pages（Canvas）共享看板** 已正式确立为多 Bot 团队状态同步的标准中枢，彻底改变了过去单纯靠群聊刷屏报进度的单一方式。

开发者 Melvin Vivas（`@melvindvivas`）在 X 上发布的 **Chief of Staff `Activity Dashboard` Page** 方案（[主帖](https://x.com/melvindvivas/status/2113676935956160882)，获 1,087 赞、51 转发、1,687 书签；[提示词跟帖](https://x.com/melvindvivas/status/2113676938820895045)，104 赞；[Routine 自动刷新跟帖](https://x.com/melvindvivas/status/2113968491573514576)）精准击中了多智能体协作的核心痛点：当你的团队扩展到五六个甚至像 `@milesdeutscher` 在 [Grok Swarms 蜂群架构帖](https://x.com/milesdeutscher/status/2113653818651189419) 中展示的“1 个总控 + 10+ 个专职 Bot”规模时，逐个点开左侧聊天窗查看进展会陷入严重的“多 Bot 界面混乱（multi-bot UI chaos）”。`@JayKurtz90` 在点评中将这套总助看板方案盛赞为 Grok Bot Pages 上线以来最惊艳的杀手级用例（[点评原帖](https://x.com/JayKurtz90/status/2113983882018119823)）。

在这套架构中，你不再需要去翻阅每个 Bot 的聊天记录，而是直接要求 Chief of Staff（幕僚长）Bot 创建并长期维护一张名为 `Grok Bot Activity Dashboard` 的实时交互 Page（页面会永久沉淀在 `Bot info pane → Library` 资料库中，并支持 `Only you`、`Your team`、`Anyone with the link` 三级权限分享，团队管理员也可在 `Dashboard → Grok Bot → Bot capabilities` 中管控共享策略）。该看板集中呈现四大核心视图：

1. **Timeline view（全局时间线视图）**：按时间轴顺序列出所有专职 Bot 最近触发的动作、交接节点与交付物链接。
2. **Tasks in progress（进行中任务）**：展示每个专职 Bot 当前正在执行的任务名称、已耗时与当前步骤。
3. **Completed tasks（已完成任务）**：归档当日已闭环的任务及对应产出文件或报告入口。
4. **Items waiting for human approval（等待人工审批事项）**：高亮汇总所有卡在权限放行、Vault/1Password 登录审批、外发邮件确认或 `Blocked` 状态的事项，让你一眼看到哪里需要人类拍板。

为了实现全员自动同步与定时热更新，你可以直接复制 `@melvindvivas` 验证过的两段核心配置——第一段发给 Chief of Staff 建立看板并写入各 Bot 规范，第二段挂载为定时 Routine 持续刷新页面（[提示词原帖](https://x.com/melvindvivas/status/2113676938820895045)，[Routine 跟帖](https://x.com/melvindvivas/status/2113968491573514576)）：

```text
Create a live Page called "Grok Bot Activity Dashboard" to act as our central command center across all my bots.
Include four interactive sections on the Page:
1. Timeline View: chronological feed of recent actions across all specialist bots.
2. Tasks in Progress: active tasks grouped by bot name and status.
3. Completed Tasks: finished deliverables with quick summary notes.
4. Waiting for Human Approval: any blocked tasks, pending approvals, or decisions needed from me.

Treat this Page as a living document. Whenever you delegate a task or receive a handoff summary from another bot, immediately update the Activity Dashboard Page using EditCanvas instead of posting noisy status updates in chat.
```

接着，在 Chief of Staff Bot 上追加一条自动巡检刷新 Routine（完美契合 v0.75.2 全账号 300 次/小时、单 Routine 200 次/小时的充裕配额）：

```text
每隔 30 分钟检查一次共享工作区状态与各专职 Bot 的最新交接产出，使用 EditCanvas 静默更新 "Grok Bot Activity Dashboard" Page 中的进行中任务、已完成事项与待我审批列表。除非出现新的高优阻塞项（Waiting for Human Approval），否则仅更新 Page 面板，不要在聊天窗口向我发送文字提醒。将此任务保存为 Routine。
```

这套“幕僚长 + 共享工作台”范式在官方生产环境中同样得到了大规模验证。在 [Grok Bot 客服自动化官方案例](https://x.ai/news/grok-bot-customer-support) 中，面对并入 SpaceX SuperIntelligence 后暴增 **175%** 的客服工单，官方正是利用由 **Intake Triage Bot（分诊接待）**、**Billing & Refund Bot（账单退款）**、**Technical Repro Bot（技术复现）**、**Incident Batch Bot（事故批处理）** 与 **Product Feedback Synthesizer Bot（反馈聚类）** 组成的 5-Bot 协作舰队，实现了 **0 新增客服招聘**、单票成本从行业 $1.00–$4.00 降至 **$0.20–$0.30**、**99% 退款全自动闭环**，并在重大故障期间由一名工程师审核一张批量审批卡（batch approval card）即在 **10 分钟内清零 204 张事故工单**。

## 12.4 每晚语音汇报 · Nightly Voice Memo

多个 Bot 跑起来之后，天天看满屏的文字日志容易让人眼花。当日常任务被分派给不同 Bot 异步推进之后，比起一大堆文字，睡前或通勤路上戴耳机听两分钟语音备忘录要轻松得多。

Grok Bot 原生支持语音备忘与音频卡片交互（[Group Chats 官方文档](https://cursor.com/help/grok-bot/group-chats)，[Voice Chat 官方文档](https://cursor.com/help/grok-bot/voice-chat)）。在会话流中，Bot 不仅能回复纯文本，还能直接发送语音备忘卡片（Voice Memo Card）。桌面端或手机端点击卡片上的“Play voice memo”开始收听，点击“Pause voice memo”暂停；不方便听声音时，直接展开卡片就能看到完整的文字转录（Transcript）。这和在桌面端按 `Cmd/Ctrl+D` 呼出的人声听写（Dictate），或者在输入框为空时点击“Start voice chat”进入的实时通话不同，它是专门用来承载高密度异步音频简报的（[Voice Chat 官方文档](https://cursor.com/help/grok-bot/voice-chat)）。

社区里有用户分享过这个习惯：让 Bot 每天晚上准时生成一条语音备忘录，系统梳理全天各业务线的工作交付（[X 原帖](https://x.com/i/status/2101851806330712339)）。Alex Finn 分享过一组早晚提示词搭配（[Alex Finn 帖子](https://x.com/AlexFinn/status/2108319537116725426)）。睡前，对负责具体项目的 Bot 发送指令，问它趁自己睡觉这段时间，能自主开始搭建的一项大成果是什么；早晨起床后，对负责个人日程的总助 Bot 发送指令，让它列出我们现在立刻就能敲定以推动大盘进展的核心决策（[Alex Finn 帖子](https://x.com/AlexFinn/status/2108319537116725426)）。连接睡前与早晨的纽带，就是每晚自动生成的语音备忘。

但在落地语音汇报时，必须警惕流程空转。Nate B Jones 指出过，很多人容易把流程形式当成了创造价值，如果一份早报或晚报每天风雨无阻地送达，却从未真正改变过你的任何业务决策，那它纯粹是在空耗计算资源（[Nate B Jones 视频](https://www.youtube.com/watch?v=LM7Ft7g8qJw)）。**每晚语音汇报的核心价值在于压缩决策信息并指出阻塞项，而非罗列流水账**。一份合格的晚报录音必须在两分钟内讲清楚三件事：今天闭环交付了什么、目前卡在何处需要什么外部权限、明早需要我拍板的决策项是什么。

想要把这项工作自动化，直接在总助 Bot 上挂一条定时 Routine 即可（[Routines 官方文档](https://cursor.com/help/grok-bot/routines)）。可以直接使用下面的 Routine 提示词：

```text
Every weekday at 9:00pm in my time zone, review the status of all active projects and tasks.
Synthesize the progress into a concise voice memo reply.
Cover three points in under two minutes:
1. Deliverables completed today.
2. Tasks currently marked Blocked and the exact blocker.
3. Top decisions or approvals I need to make tomorrow morning.
Do not read raw logs or tool activity. Send this as a voice memo card in this conversation.
Save this as a routine.
```

如果交互以中文为主，提示词可设为：

```text
在我的时区，每个工作日晚上 21:00 检查所有进行中项目和任务的状态。
将当天的核心进展浓缩为一条简明扼要的语音备忘录（Voice Memo）回复。
在 2 分钟内讲清三点内容：
1. 今天已闭环交付的成果。
2. 当前被标记为 Blocked 的任务及具体受阻原因。
3. 明天早晨需要我亲自审批或拍板的核心决策。
严禁念读原始日志或工具调用细节。直接在当前会话中以语音备忘录卡片形式发送。
将此任务保存为 Routine。
```

收工躺下前听一遍语音卡片，明早起来点开审批卡直接放行，多 Bot 协作才能真正跑顺。

> [!NOTE]
> 📸 **截图位（待补）**：会话流中可播放、暂停并展开文字转录的语音备忘录卡片

测试每晚定时触发语音备忘在桌面端与移动端的音频合成完整度与转录一致性。

### 12.4.1 iPhone Action Button 一键语音呼叫主控 Bot 与挂断自动派单闭环

除了被动收听总助每晚发来的异步语音备忘录，2026 年 10 月 19 日官方发布的 **iPhone Action Button（侧边操作按钮）一键实时语音通话**功能（[官方公告](https://x.com/bot/status/2112246033178968161)，7,264 赞 / 505 转发 / 2,213 书签；[Voice Chat 官方文档](https://cursor.com/help/grok-bot/voice-chat)；[Mobile 移动端指南](https://cursor.com/help/grok-bot/mobile)；以及 `@SawyerMerritt` 的 [实机演示视频](https://x.com/SawyerMerritt/status/2112252980015579431)），更是将多 Bot 团队的“移动语音交接”推向了完全免打字的物理按键时代。

在配备 Action Button 的 iPhone（iPhone 15 Pro 及后续机型）上，只要将 Grok Bot iOS 客户端更新至 **v1.16 或更高版本**并至少打开过一次 App，即可通过两条官方路径将侧边物理按键绑定为你的“总助对讲机”：

1. **直接呼叫默认主控 Bot（Primary Bot）**：进入 iPhone 系统 `Settings → Action Button → Shortcut → Choose a Shortcut → Grok Bot → Start Voice Chat`。
2. **定向呼叫 Chief of Staff / CEO Bot（配合 iOS 快捷指令 App）**：打开 iOS **Shortcuts（快捷指令）** App，添加 Grok Bot 提供的 `Start Voice Chat with Bot` 动作，将目标固定绑定为你的 `Chief of Staff`（或设为 `Ask Each Time` 每次弹窗选择），再将该快捷指令挂载到 Action Button 或通过 `"Hey Siri"` 语音唤醒（如 `@TyeInBloom` 在 [iOS 全家桶联动帖](https://x.com/TyeInBloom/status/2113767679588770271) 与 `@D__cup` 在 [Shokz 骨传导耳机免提外脑帖](https://x.com/D__cup/status/2114211130365358350) 中分享的通勤随身调度方案）。

这套语音机制之所以能成为多 Bot 交接的枢纽，核心在于官方设计的**挂断即归档与自动跟进机制**（[Voice Chat 官方文档](https://cursor.com/help/grok-bot/voice-chat)）：当你在走路、开车或睡前长按 Action Button 与主控 Bot 实时对话（通话中可随时切换 Mute/Unmute、展开实时字幕 Show transcript 或调节音色、语速与语种）并点击 **Hang up（挂断）** 的瞬间，主控 Bot 的聊天流中会立即自动生成一张 **Voice chat card（语音通话卡片）**，完整记录本次通话时长与全文逐字稿（full transcript）；紧接着，主控 Bot 无需任何额外唤醒，就会在同一会话窗口或共享群聊中自动根据刚才的语音逐字稿拆解任务，向各个专职 Bot 派单或直接更新 `Activity Dashboard` Page。

中文社区博主 `@CyberAlice3269`（夏哥研究室）在 [“1 个 CEO + 5 个专职 Bot”自媒体工作室实战帖](https://x.com/CyberAlice3269/status/2112098767151468645) 中，完整展示了这一“语音对讲总控 + 多专员流水线”的 1+5 架构：

- **1 个主控中枢（CEO Bot）**：平时人类只用语音跟这一个 CEO Bot 说话。按下手机侧键口述今日灵感或选题方向，挂断生成 Voice chat card 后，CEO Bot 立即读取共享知识库与标准 SOP 启动编排。
- **5 个专职执行 Bot**：CEO Bot 按照流水线顺序，依次将任务安静交接给 **情报搜集 Bot**（抓取 X 与全网一手信源）、**选题策划 Bot**（提炼切入点与大纲）、**初稿撰写 Bot**（按账号语感成文）、**审校润色 Bot**（核查事实与去 AI 味）以及 **配图制作 Bot**（调用 Grok Imagine 生成视觉素材）。

你可以将以下“语音挂断自动拆单”规则追加到主控 CEO / Chief of Staff Bot 的 Profile 中，实现长按手机侧键说完即走、全团队自动运转的闭环：

```text
当我与你结束实时语音通话（Voice Chat）、会话中生成包含完整逐字稿的 Voice chat card 后，你必须立即自动执行以下交接闭环：
1. 从刚生成的语音通话逐字稿中提取我的全部口头指令、灵感要点与交付期限。
2. 将口头需求拆解为结构化子任务，按照各专职 Bot（情报、选题、撰稿、审校、视觉/研发）的职责边界，直接定向 @ 对应 Bot 派发指令。
3. 同步调用 EditCanvas 将新派发的任务写入 "Grok Bot Activity Dashboard" Page 的 Tasks in Progress 栏。
4. 在当前 1 对 1 窗口向我回复一条不超过 5 行的派单确认清单，无需我二次打字确认即刻启动流水线。
```


# §13 编制案例库 · Team Blueprints

在调研社区讨论时可以发现，新手组建多 Bot 团队最容易踩的坑，就是以为只要把几个 Bot 拉进群、随便丢一句提示词，它们就能像人类员工一样自动把事办好。结果往往是 Bot 之间互相客套、疯狂刷屏，几分钟就撑爆上下文，最后连初始任务是什么都忘光了。Kin 橙皮书里提过 Alex Finn 的五人舰队，但那属于二手转述，既没给官方配置依据和用量成本核算，还建议用内网穿透反向控制主机，完全忽视了共用云电脑环境下的安全边界。

多 Bot 协作不是角色扮演，而是岗位工程。官方设计文档明确写着，每个群聊最多 6 个 Bot（https://x.ai/news/designing-grok-bot 与 https://cursor.com/help/grok-bot/group-chats）。把一群自主 Agent 放在一起，必须有明确的岗位说明书、事件驱动机制和权限门禁。这一章梳理了中文自媒体实测、真实开发组争议、一人公司业务线以及官方标杆案例（完整行业与岗位用例可参考官方用例库 https://cursor.com/docs/grok-bot/use-cases），把这四种编制架构、成本陷阱和安全防线拆开来看。

## 13.1 五人内容团队（小红书/公众号/抖音）· Content Team

做中文自媒体的人最先尝试多 Bot 协作。掘金作者迷城在实测中记录了他搭建 7 个自媒体 Bot 的过程（https://juejin.cn/post/7682695577956483091）。他指出，给 Bot 写设定不能只写一句身份，得写成包含身份记忆、核心使命、关键规则、工作流程和成功指标的岗位说明书。迷城拉了个名为“自媒体创作团队”的群聊让 Bot 各司其职，并通过命令行安装 OpenCode CLI 1.18.25 调度外部代码能力。不过他文章里认为“只有高配套餐才包含 Grok Bot”并不准确，官方帮助页写明 Cursor Pro/Pro+/Ultra 都可用 Grok Bot，另可关联 SuperGrok/X Premium+ 等 xAI 订阅（https://cursor.com/help/grok-bot/plans）。而在 2026 年 10 月上线 **The X Subscription 三合一统一订阅**（https://cursor.com/help/the-x-subscription/overview 与官方发布帖 https://x.com/bot/status/2110063783796572496）之后，官方将 Grok、Cursor 与 X Premium 整合进单一订阅体系：**Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 三档均包含 Grok Bot 权限（Free $0 与 Plus $8/月不包含），三端共享同一个周额度池（Weekly usage pool），超额部分改由 `grok.com/dashboard/billing` 下的 **Prepaid Credits（预付额度）** 扣减；既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及自助式 Teams（$40/人/月）老订户只要不主动切换，仍可保留原套餐，但一旦通过 `cursor.com/unify` 单向合并升级至 The X Subscription 将不可逆。

七七行銷筆記在视频实测中展示了一支五人社媒内容小队（https://ytget.cc/entry/grok-bot-five-ai-team-x-account 原片 https://www.youtube.com/watch?v=Z3ghSHtu8dk）。他在群里发了一句“安排本周内容”，总经理由此拆解任务。实测里第一版选题太偏，去讲大语言模型校对，脱离了大众关注点。创作者没逐个找分析师或文案重说，而是直接在群里给总经理提了三点要求：选题要有大众热度、分析师要贴合账号定位、文案必须从具体场景切入口语化表达。总经理随后要求下属重新修改并再次交付。这说明内容团队的主脑不能只是传话筒，提示词里必须赋予它退回修改与质量验收的权力。

觉醒AI 在小红书团队工作流实录中总结了三道硬门禁（https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/）：外部源文只认人类给的原始链接，数据核算只认本地生成的报告，**发布权与终审权永远留在人手里**。他们把媒体团队拆成情报侦察、选题策划、内容主笔、事实编辑和数据复盘五个岗位（https://www.jxxy.net/ai/articles/AdrianPunk115-2097311704547987756/），把账号风格调性、选题终稿和违禁词规则全部落盘到云电脑的 `/workspace/learn/*.md` 路径下（https://www.jxxy.net/ai/articles/grok-bot-workflow-training/），让所有 Bot 每次生成时对照文件，而不是对照上一轮的聊天记录。

象鱼工作流在总结国内平台用例时提醒了操作边界（https://xiangyugongzuoliu.com/grokbot-use-cases/）：国内自媒体平台没有官方插件，公众号阅读与完读数据不在公开页面，需要人工导出后台数据，或者让 Bot 读取已经登录后台的浏览器窗口。而且平台对高频点击和自动化操作很敏感，定时频繁刷新会触发风控，最终的发布、点赞和私信沟通必须留在手机或客户端上由人工完成。

在 X 社区的实战演进中，`@CyberAlice3269`（夏哥研究室）进一步将这种架构打磨为可稳定复用的 **“1 CEO + 5 专职 Bot（情报、选题、撰稿、审校、配图）+ 共享知识库与 SOP”** 自媒体内容工作室编制（https://x.com/CyberAlice3269/status/2112098767151468645）。在这一套 6-Bot 满编体系中，人类创作者平时只需要通过语音向顶层的 **CEO Bot** 口述灵感或下达指令（配合 iOS 客户端 v1.16+ 的 iPhone Action Button 侧边键一键语音功能 https://cursor.com/help/grok-bot/voice-chat），由 CEO Bot 拆解排期并依次向 5 个专职 Bot（**情报搜集、选题策划、初稿撰写、审校润色、配图制作**）派发任务。6 个 Bot 共享同一套云电脑知识库目录与标准化 SOP 规范，配图制作 Bot 则可直接调用 v0.71.2 上线的原生 Grok Imagine 生图/生视频工具或代码动效渲染能力（https://x.ai/changelog/bot 与 https://x.com/bot/status/2110566041772617908）生成视觉素材，彻底消除了跨软件导出的手工摩擦。

而在海外英文创作者圈层，`@milesdeutscher`（Miles Deutscher）在其获得 3,100 赞、4,503 书签的“10 大 Grok Bot 用例”长推（https://x.com/milesdeutscher/status/2113653680834859262）的第 3 项中，展示了更大规模的 **#3 Grok Swarms（1 主控 Orchestrator + 10+ 专职 Bot 蜂群编制）**（https://x.com/milesdeutscher/status/2113653818651189419，40 赞）。由于官方限制单个群聊最多容纳 6 个 Bot，当团队规模扩展到 10 个以上细分领域的专职 Bot（涵盖爆款异常值抓取、跨平台改写 #5 https://x.com/milesdeutscher/status/2113653788196430242、竞品监控 #9 https://x.com/milesdeutscher/status/2113653726217195817、个人 X 副驾 #10 https://x.com/milesdeutscher/status/2113653710631166414 等）时，`@milesdeutscher` 采用 1 个总控编排 Bot（Orchestrator）统领多个垂直分群或通过文件系统异步交接，并行开展大规模市场调研蜂群与跨平台内容工厂流水线。

综合这些实操案例，可以梳理出一套五人中文内容团队的标准编制。五个专职 Bot 各司其职：总编兼协调官负责接收人类目标、拆解排期并把关各环节交付物；情报侦察员只读抓取公开行业动态与 X 热门话题，输出结构化事实；主笔负责写微信公众号深度长文、小红书图文文案或短视频口播脚本；视觉排版员输出结构化 Markdown 与配图描述；质检员核对敏感词、核实数据出处，给出退回或放行建议。

> [!NOTE]
> 📸 **截图位（待补）**：在 Grok Bot 中建立自媒体创作群聊并配置 5 个专职 Bot 的侧边栏列表
![五人中文内容团队的分工协作流水线与三道人工硬门禁](../images/fig-13-1.png)

*图：五人中文内容团队的分工协作流水线与三道人工硬门禁*

总编 Bot 的核心系统提示词必须设好拦截机制：

```text
你是一个 5 人中文内容团队的总编辑。
群内成员包含：@情报侦察、@平台主笔、@视觉排版、@内容质检。

你的核心工作职责：
1. 接收人类提出的选题方向或目标，将其拆解为具体任务派发给对应角色。
2. 调度顺序：情报侦察输出事实简报 -> 平台主笔撰写文案初稿 -> 视觉排版生成图文排版草稿 -> 内容质检核查事实与敏感词。
3. 严格执行质量把关：如果质检未通过或初稿偏离要求，必须直接指出具体问题并要求对应 Bot 修改，严禁未经检查直接将下属的半成品递交给人类。
4. 遵守硬性安全规则：严禁在任何第三方自媒体平台执行自动登录、自动发布或私信操作；所有最终成果必须以 Markdown 文本与配图建议的形式提交，等待人类最终审核。
```

若采用 `@CyberAlice3269` 的“1 CEO + 5 专职 Bot”文件级交接编制，或者 `@milesdeutscher` 的 #3 Grok Swarms 蜂群架构，还可以将共享知识库路径与 SOP 写入总控配置中：

```yaml
# 1 CEO + 5 专职 Bot 内容工作室标准目录与交接协议（参考 @CyberAlice3269 架构）
workspace_root: /workspace/content-studio
shared_sop:
  - /workspace/content-studio/sop/brand-voice.md
  - /workspace/content-studio/sop/forbidden-words.md
  - /workspace/content-studio/sop/fact-check-rules.md
team_roster:
  orchestrator: "@CEO-总编"
  specialists:
    - role: "@情报Bot"
      output: "/workspace/content-studio/pipeline/01-intel-brief.md"
    - role: "@选题Bot"
      output: "/workspace/content-studio/pipeline/02-topic-spec.md"
    - role: "@撰稿Bot"
      output: "/workspace/content-studio/pipeline/03-draft.md"
    - role: "@审校Bot"
      output: "/workspace/content-studio/pipeline/04-reviewed.md"
    - role: "@配图Bot"
      output: "/workspace/content-studio/pipeline/05-assets/"
```

在成本和配额上，群聊消息具有全员广播特性。五人团队如果频繁在群里对话，上下文会飞速膨胀。社区用户反馈，Cursor 个人订阅或 The X Subscription 三端共享周额度池下的高频交互会导致周额度快速耗尽（如 `@charlie_pmp` 在 https://x.com/charlie_pmp/status/2114214503416271131 中指出的三端共抽一个周额度池与冗余 Routine 耗电问题）。所以内容团队必须执行“安静交接”原则：非必要不艾特全员，只在交接节点传递最终结构化结果。

：在微信公众号后台由 Bot 提取阅读数据并与本地排版草稿进行核对。

## 13.2 研发组（Lead/Dev/QA/Ops）与反对意见 · Dev Team

在研发场景下组织多 Bot，社区里存在激烈争论。V2EX 开发者 diudiuu 分享过他为开源模型采集项目搭建的数字员工开发流程（https://www.v2ex.com/t/1241365 社区帖称……个例）。他的流水线由项目管理工具 Linear 触发，任务自动进入 TPS 开发主群。群内固定配置了 Lead、Dev、QA、Ops 四个 Bot，最终在 GitHub 仓库成功实现了自动提交并合入拉取请求（https://github.com/adiudiuu/tps/pulls?q=is%3Apr+state%3Aclosed）。

在这个体系里，Lead 负责在检测到新 Issue 时把标题和链接同步进群，严禁自主盲目认领或定时轮询；Dev 负责对照需求写代码修改模型数据并提交 Pull Request；QA 对照 Issue 和拉取请求跑测试，保留操作步骤和截图；Ops 负责构建、部署和回滚，记录完整的命令行日志。整个流程有一条铁律：**代码规范与职责边界只认仓库里的 AGENTS.md**。所有的循环任务由 Linear 自带的周期机制推送到群内，完全不让 Grok Bot 在后台轮询。

这个方案在 V2EX 引来了同行质疑。用户 @ThisDay 批评，搞这种人设聊天群纯粹是浪费 Token 和撑爆上下文，单凭一个编程智能体的子代理机制就能搞定；用户 @jsdi 指出多 Agent 协作极其复杂，绝大部分场景根本不需要，群聊模式中看不中用；用户 @kiliter 认为多智能体在实际开发中更像自嗨，一句话就能指挥模型完成修复、测试与发版，拆成多个智能体呼来唤去反而增加管理负担；用户 @fanfou 从架构分析，群聊点对点消息让上下文极度混乱，远不如具备领导者、任务看板和收件箱的主从架构可控；用户 @syyyyy 则直言群聊额度消耗太快，一天半就会用光周配额。

面对这些批评，diudiuu 回应说，单人处理单个简单需求确实一句话搞定，但要跨多个代码仓库维护日常更新、每天产生大量琐碎 Pull Request 时，固定角色能把任务流转规整化，人不用陷进每个修改细节去排查原因。

围绕“研发与重度任务中到底该如何使用 Grok Bot”，中文 X 社区在 2026 年 10 月 18 日爆发了一场极具代表性的架构讨论。`@Khazix0918`（数字生命卡兹克，https://x.com/Khazix0918/status/2111709708226797737，285 赞 / 54 书签）直言如果把默认对话窗口当成重度问答苦力裸用，体验极差——*“常年不思考，张嘴就来，路由的垃圾模型查都不查直接回复... 掰扯和出错浪费的时间，远超出给我节省的时间”*。对此，`@object_nullll` 在回复（https://x.com/object_nullll/status/2111717423837778173）中一针见血地阐明了正解架构：**Grok Bot 对话层（conversational layer）的设计初衷是收集上下文、对齐验收标准、编写结构化 Prompt，并将重度执行任务委派给 Cursor Cloud Agents（`CloudAgent`）或云电脑上的 CLI Workers，绝不能依赖裸聊天的 zero-shot 直接回复来干重活**。

这一“对话层收集上下文 + 重活委派给 CloudAgent 或 CLI Worker”的架构共识，在官方团队内部与一线开发者中得到了全面印证：
1. **Grok Bot 内部设计与研发团队日常工作流（`@pengzheng_`）**：Grok Bot 设计师 Peng Zheng（`@pengzheng_`，https://x.com/pengzheng_/status/2110245240863178793，86 赞 / 108 书签）揭秘了官方内部团队每天如何用 Grok Bot 协作——团队在频道内用 Grok Bot 自动分拣 Bug 反馈与设计走查问题，由 Bot 汇总上下文后直接拉起 **Cursor Cloud Agents** 修改代码、生成 PR，并在云电脑浏览器中自动打开预览环境完成 UI 视觉改动的端到端验证。
2. **飞书 + Linear + 邮箱 + CLI Worker 研发闭环（`@realbenzh`）**：开发者 Ben Zhang（`@realbenzh`，https://x.com/realbenzh/status/2111295936635015631）展示了他将飞书（Feishu）、Linear、电子邮箱与团队文档全部接入 Grok Bot 汇总业务上下文，先在聊天窗口里与 Bot 对齐交付目标和验收标准（acceptance criteria），随后让 Grok Bot 通过 CLI 交互式驱动 `@orca_build` 完成代码构建与交付。
3. **云电脑挂载 Codex CLI + 完成时 Webhook 零轮询唤醒（`@AbhisheKumarA7`）**：`@AbhisheKumarA7`（https://x.com/AbhisheKumarA7/status/2110484964143976578）直接在云电脑内部安装 Codex CLI 并配置完成时 Webhook，让耗时漫长的代码构建在后台运行，跑完后通过 Webhook 唤醒 Grok Bot 验收，实现零轮询耗电（同时注意 v0.75.2 起官方已将 Routine 频率上限提升至**全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时**，定时最小间隔仍为 5 分钟，详见 https://cursor.com/help/grok-bot/routines）。

官方工程师 Lingxi Li 在 Galaxy 大会工程专场的分享也印证了类似的分工思路（团队成员演讲，https://youtu.be/zCqmTSF2ctg）。在官方实践中，Bot 团队每天凌晨 3 点扫描代码仓库排查代码质量隐患，早上统一提交 Pull Request。团队只允许使用云端编码 Agent，合并代码的最终权力必须牢牢由人类掌控。为了解决模型自主验证时的虚假汇报，他们开发了 verify 系列验证技能，要求 Bot 通过运行实际测试命令、保存终端日志、提取退出码和网页截图来提供客观证据，严禁无人看管的死循环。

> [!NOTE]
> 📸 **截图位（待补）**：Linear Issue 触发后 Lead 将任务同步进 TPS 开发群并关联 GitHub PR
![研发四人组流水线与规避上下文膨胀的防空转事件驱动架构](../images/fig-13-2.png)

*图：研发四人组流水线与规避上下文膨胀的防空转事件驱动架构*

想让研发四人组不变成烧额度的闲聊群，关键是掐断 Bot 之间的无效对话，并落实“对话层做调度、重活交 CloudAgent / CLI Worker”的铁律。提示词可以这样写：

```text
你是 TPS 开发群的技术主管 Lead。
群内协作 Bot 包含：@Dev、@QA、@Ops。

执行规则：
1. 接收到 Linear 任务后，向开发群输出任务摘要与链接，指定 @Dev 认领。
2. 禁止任何闲聊、感谢或不必要的中间状态确认。
3. 严禁在聊天层直接凭空手写大段业务代码：@Dev 必须先对齐验收标准，然后调用 Cursor CloudAgent 或本地/云端 CLI Worker 编写代码并提交 PR，随后通知 @QA 运行测试套件。
4. @QA 必须输出包含测试通过命令和截图的报告；测试通过后通知 @Ops 生成部署构建预览。
5. 最终合并操作必须由人类在 GitHub 网页端手动点击批准，严禁任何 Bot 尝试自动合并到主分支。
```

：在开源仓库中由 Dev 自动根据 issue 开 PR 并由 QA 运行 Playwright 留下测试截图。

## 13.3 一人公司 / 一条业务线（Milo）· Solo Business

单人创作者或小型创业者经常想靠 Bot 独立维系一条完整业务线。X 社区用户分享过名为 Milo 的全托管 Bot 案例（https://x.com/i/status/2109152147325796381 社区帖称……个例，作者自述，效果未核实）。该用户设了一个专职 Bot 运营 AI 工具目录网站。Bot 盯紧社交媒体公告帖下的回复，全天候根据用户反馈自动提交 Pull Request，自主添加了 7 个以上的功能模块，每隔 15 分钟推送一次业务分析数据，主动提交搜索引擎收录优化，甚至试图自主联络赞助商。

仔细审视 Milo 这类模式，背后藏着巨大的运行成本与失控风险。社区用户 @fleyta88 算过 Routine 运行成本（https://x.com/fleyta88/status/2109346840382415019）：每 5 分钟轮询一次的高频任务，一个月将执行 8640 次，按 API 估算消耗高达约 397 美元；如果改用检查变更指纹的轻量检测，成本能降到约 45 美元。Milo 每隔 15 分钟做一次全量推送，如果长期无人监管，很快就会烧尽用量额度。而且让模型自主寻找赞助商和对外商业沟通，缺乏人工审核环节，很容易产生虚假承诺甚至合规事故。

官方产品指南中 Eric Zakariasson 给出了更克制也更实用的编排模式（团队成员指南，https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots）。他为每个项目分别建立一个 Grok Bot 侧边栏频道和 Notion 数据库，将团队结构固定为项目与任务两张表，并设立了一个项目经理 Bot 专门负责更高层级的项目开辟与资源协调。

Zakariasson 制定了三条关键编制规则：第一，优先复用已有的功能 Bot，比如已有的代码员或研究员；第二，除了项目经理之外，每个项目频道最多提议 5 个 Bot，将单个频道内的成员总数严格控制在 6 个以内；第三，只有在现有人员完全无法胜任且经过人类明确同意后，才允许新建特定领域的专用 Bot。当任何 Bot 在执行中遭遇阻碍或需要关键决策时，**遇到阻塞必须标记 Blocked 并停下等待人类输入**。人类可以在 Notion 看板上看着卡片流转，只在出现阻塞时进入群聊介入。此外，隨著 v0.75.2 推出原生 **Pages（Canvas）** 实时交互画布（https://x.ai/changelog/bot 与 https://x.com/bot/status/2112991843235610885），社区开发者 `@melvindvivas`（https://x.com/melvindvivas/status/2113676935956160882，1,087 赞 / 1,687 书签）进一步让 Chief of Staff（幕僚长）Bot 直接维护一张包含时间线、进行中任务、已完成任务与等待人工审批事项的 `Activity Dashboard` 实时看板 Page，彻底告别了逐个点开聊天窗查看进度的界面混乱。

这种分层治理思路与官方内测期涌现出的总助模式完全一致。Grok 团队成员 Roman Ugarte 提到，Chief of Staff 模式在团队内测第二周就自然产生（团队成员访谈，https://www.youtube.com/watch?v=maSdsTLaMuU）。Claire Vo 同样在实践中利用总助 Bot 统一过滤收件箱、日历与通讯软件信息（https://www.youtube.com/watch?v=QBmgF1kJSK4）。一人运营一条业务线的健康结构，是让人类只与顶层的总助或项目经理对接，由主脑向垂直执行 Bot 下发指令，底层 Bot 专注调用工具，避免让所有 Bot 同时与人类对话产生严重的信息噪音。

> [!NOTE]
> 📸 **截图位（待补）**：Notion 中的 Projects 与 Tasks 数据库配合 Projects Manager Bot 协同状态
![一人公司的分层架构：人类决策者、总助中枢与垂直业务线 Bot](../images/fig-13-3.png)

*图：一人公司的分层架构：人类决策者、总助中枢与垂直业务线 Bot*

项目经理 Bot 协调 Notion 看板的提示词可以这样写：

```text
你是一个负责多项目推进的项目协调中枢 Project Manager。
你在 Notion 中管理两个数据库：Projects 和 Tasks。

你的运行原则：
1. 每个新项目建立独立的项目频道，频道内除你之外最多配置 5 个专职执行 Bot。
2. 调度原则：优先分配已有专职 Bot，严禁未经人类许可随意生成新 Bot 实例。
3. 状态管理：实时监控 Tasks 数据库中的任务状态；一旦执行 Bot 缺乏凭证、遇到报错或需要业务决断，将其任务状态变更为 Blocked，并在频道内艾特人类管理者。
4. 任何对外联系、发布上线与资金变动动作，必须生成草稿并在人类解除 Blocked 状态前保持暂停。
```

：在 Notion 任务看板中配置 Blocked 状态监听并由 Bot 自动向群聊推送阻塞预警。

## 13.4 采购 Haggle Bot、客服 Bot 团队（官方案例）· Official Cases

在涉及真金白银的企业级场景下，多 Bot 编制必须具备极其严密的安全与权限边界。官方披露了两个内部严苛验证的标杆案例：采购谈判 Haggle Bot 与客户支持 Bot 团队（官方完整行业用例汇总见 https://cursor.com/docs/grok-bot/use-cases）。

采购场景中，官方披露 Haggle Bot 帮助企业实现了超过 100,000 美元的直接成本节省（https://x.ai/news/grok-bot-procurement）。在真实案例中，一笔金额为 14,629 美元的科技采购单，经由 Haggle Bot 多轮谈判比价，最终被压缩至 6,143 美元，降幅达到 58%，价格谈定后交回 Amazon Bot 下单。官方提供了该 Bot 模板（原文链接 /bot/marketplace/bots/haggle-bot；Marketplace 已于 9 月底改为 Connect Apps，模板入口移到网页端（https://x.ai/changelog/bot））。

Haggle Bot 之所以没出事故，核心在于官方在系统提示中确立了三档权限红线架构。在具体落地中，**把写操作和资金退款严格锁定在三档权限内**。第一档是允许自主执行的内部动作（如查用量、比市场价，具体由模板使用者填写）；第二档是每次都必须人工批准（Needs explicit go），官方模板举的例子是"任何发给供应商的消息"；第三档是绝对禁止执行（Never），比如签署合同、购买或订阅、批准扣款等任何有约束力的承诺；另外绝不向供应商透露用量数据、席位数、内部项目、时间紧迫性或"已决定续约"。

官方公开的提示词模板要求 Bot 用 TODAY/SAVE/REC/NEXT 四段格式汇报，下面是按官方给出的"强发现"示例（视频会议软件 10/14 续约、210 席中 74 席闲置 90 天、缩到 150 席约省 $18k/年）改写的中文版：

```text
TODAY: 视频会议软件将于 10 月 14 日到期续约。
SAVE: 管理日志显示当前购买了 210 个席位，其中 74 个席位已闲置超过 90 天。续约时缩减至 150 席，预计每年可节省约 18,000 美元。
REC: 建议以此为筹码向销售代表要求老客户阶梯折扣。
NEXT: 等待采购负责人确认还价邮件草稿，批准后由 Bot 代为发出。
```

在客户支持领域，官方披露其客服 Bot 团队在工单处理量激增 175% 的前提下实现了零新增客服人手（https://x.ai/news/grok-bot-customer-support）。传统 AI 客服工具按每次解决收费 1 到 4 美元，而他们经过小幅优化后，单票成本可低至 0.20 至 0.30 美元。在整个退款流程中，99% 的退款请求实现了无需人工干预的自动化处理。对于复杂或存在争议的对话，系统设定了硬性熔断：一旦与用户的对话来回超过 3 次，立刻无条件自动升级至人工管理层处理；每天由 Bot 对超过 20,000 条用户反馈进行聚类分析并同步给工程团队。

拆开官方客服自动化标杆档案（https://x.ai/news/grok-bot-customer-support），这场实战发生在一个极端高压的业务节点：**2026 年 8 月 14 日 Cursor 正式并入 SpaceX SuperIntelligence（SpaceXSI）后，全球用户的咨询与客服工单量瞬间暴涨 175%**。面对排山倒海的工单洪峰，官方没有临时扩招外包坐席，而是部署了一支由 **5 个专职客服 Bot** 协同作战的自动化舰队，每个 Bot 都有严格正交的职责边界与工具权限：

| 专职客服 Bot 编制名称 | 核心职责与工作流定位 | 对接系统与关键动作边界 |
| :--- | :--- | :--- |
| **1. Intake Triage Bot（分诊接待 Bot）** | 第一线接单、意图识别、情感与紧急度打标、上下文信息补全 | 接入工单系统 Plain，自动关联用户订阅状态（含 The X Subscription 与独立 Cursor 计划），将工单精准分流至对应下游专职 Bot；若往返超过 3 轮无果立即升级人工 |
| **2. Billing & Refund Bot（账单与退款 Bot）** | 核验扣费流水、订阅合并退差价（Prorated refunds）、执行合规退款与取消订阅 | 对照退款政策核查账单周期与实际用量，符合条件时直接调用支付接口闭环处理，支撑起 **99% 退款全自动处理** |
| **3. Technical Repro Bot（技术复现 Bot）** | 针对 Bug 报告在隔离云电脑沙箱中拉起对应版本环境，尝试自动化复现问题 | 收集终端报错日志、退出码与浏览器录屏截图，将验证确凿的复现证据打包移交工程团队 |
| **4. Incident Batch Bot（事故批处理 Bot）** | 在突发线上服务故障或大面积中断期间，将同类涌入的故障工单自动聚类建组 | 生成统一的 **批量审批卡（Batch Approval Card）**，让单名值班工程师一次审批即可对数百张同源工单同步下发状态更新与补偿 |
| **5. Product Feedback Synthesizer Bot（产品反馈聚类 Bot）** | 全天候扫描全量客服对话与 X 社媒提及，清洗并提炼用户功能诉求与体验痛点 | 每日自动抽取并聚类 **20,000+ 条产品反馈点**，去重评分后自动在 Linear 中转化为带真实用户原话引用的研发工程工单 |

这支 5-Bot 客服舰队在并入 SpaceXSI 后的实战中交出了五项硬核量化战果（https://x.ai/news/grok-bot-customer-support）：
1. **0 新增客服招聘（省下约 200 人）**：在工单暴涨 **175%** 的极端压力下，实现了 **0 新增全职客服人手（0 new support hires）**，按同等工单吞吐量测算相当于直接省下了约 **200 名**新增客服的人力编制。
2. **单票解决成本降至 $0.20–$0.30**：远低于传统商业 AI 客服 SaaS 按单次解决（per-resolution）收取 **$1.00–$4.00** 的行业基准价格，降幅高达 70%–90% 以上。
3. **99% 退款全自动闭环处理**：依托 Billing & Refund Bot 对账单与用量数据的精确核验，**99%** 的退款申请实现了端到端零人工干预的自动化审核与原路退回。
4. **单名工程师 10 分钟批处理 204 张突发故障工单**：在一次重大线上事故期间，Incident Batch Bot 自动识别并归拢了所有受影响用户的求助，仅由 **1 名值班工程师**审核批准一张批量审批卡（Batch approval card），就在约 **10 分钟**内一次性清零并妥善回复了 **204 张**突发故障工单。
5. **每日提炼 20,000+ 产品反馈点直达研发**：Product Feedback Synthesizer Bot 每天从海量工单与对话中结构化提取超过 **20,000+** 个产品反馈数据点，使产品与工程团队当天就能感知一线痛点并排期修复。

官方在客服团队的部署中推行了“爬行、步行、奔跑”三阶段落地法则。在最初的爬行阶段，Bot 接入工单工具 Plain 与任务系统 Linear，但只能撰写内部备注，任何对客户的回复与修改都必须由人类坐席人工确认；在步行阶段，团队引入运行追踪与效果评估机制，第一天先让人工针对最简单直观的常见工单进行复核，核实质量无误后当天放开自动直回；在奔跑阶段，团队引入超过 100 万条历史对话沉淀服务语气，实现 Bot 之间互相巡检纠错，并自动关联 X 社交媒体上的舆情监测。

Galaxy 大会客服专场上，David Gan 展示的 FlyLo 虚拟航空客服团队进一步将职责细化为四个协作 Bot（团队成员演讲，https://youtu.be/BSB--jUnx9U）：Reply 负责对照政策直接回复工单并在支付网关 Stripe 执行小额退款；Tune 负责从日常客服真实对话中提取新问题并向公开知识库提交修改；Alert 负责盯紧服务异常日志并推送到 Slack；Build 负责处理周边集成构建。

FlyLo 的业务逻辑设立了严格的策略分流：在规定政策窗口内，直接自动执行 20 美元的全额退款；超出 20 天的申请，Bot 明确拒绝退款并自动变更为账期结束时取消订阅。如果遇到公开 FAQ 缺失的冷门问题，Reply 会主动将置信度调低并转交人工，同时触发 Tune 撰写新 FAQ 条目；知识库更新前必须经过人工 A/B 测试确认，更新生效后 Reply 才会对类似工单恢复高置信度的自动处理。如果遇到处于系统抑制名单中的异常邮件地址，Bot 会如实汇报报错，绝不盲目重试。

> [!NOTE]
> 📸 **截图位（待补）**：Haggle Bot 扫描供应商闲置席位后生成的 TODAY/SAVE/REC/NEXT 采购谈判卡片
![官方客服 Bot 团队的 crawl-walk-run 演进路线与退款分流决策树](../images/fig-13-4.png)

*图：官方客服 Bot 团队的 crawl-walk-run 演进路线与退款分流决策树*

：在沙箱环境中复现三档权限下的供应商席位闲置审计与还价邮件草稿生成。

从这四个典型编制中可以看出，无论是自媒体内容组、代码研发组、一人业务线还是官方采购客服组，多 Bot 能够跑通的核心绝不是让模型自由发挥。关键是建立明确的触发条件、落实防空转的事件驱动架构、坚守草稿优先与权限分级，并设立随时可以由人类接管的断路器机制。


# §14 个人与生活 · Personal & Daily Life

很多人刚拿到 Grok Bot，总想先给它丢个大项目或者写套复杂系统。我建议先从日常生活切入。生活里的杂事目标明确，输入固定，做没做好一眼就能看出来。拿个人杂事练手，熟悉它的云电脑运行机制，摸清审批闸门和用量消耗，最稳妥。

不过动手前得先立条规矩：生活场景里全是私密信息，家庭地址、孩子学校、银行卡号，漏一次就麻烦了。所有涉及对外发送、掏钱付款和账号变更的动作，必须死死卡在人工审批后面。

> **适合谁**：已经跑通 §04 第一个任务的个人用户，不需要会写代码。
> **前提条件**：14.1、14.2 用到 Gmail 和 Google Maps，需要 Google 账号并能访问 Google 服务；只用国内邮箱（QQ、163）的读者，可以先用 14.3 的"转发到 Bot 自有邮箱"做法。提示词用英文写是因为原始案例是英文，换成中文同样可用。

## 14.1 邮箱大扫除与退订 · Email Cleanup & Unsubscribe

> [!NOTE]
> 📸 **截图位（待补）**：Gmail 插件授权后 Bot 在云电脑读取收件箱并生成退订候选列表
> [!NOTE]
> 📸 **截图位（待补）**：Bot 生成内联退订草稿并弹出人工审批卡
> [!NOTE]
> 📸 **截图位（待补）**：Bot 自有邮箱配置界面与域名绑定说明

### 场景

拿 Bot 处理生活杂务，很多人最先想到的就是清理堆成山的推广邮件。广告、平台活动推送、从不看的新闻简报，手动退订费时间，乱点链接还容易碰上钓鱼网站，甚至误删账单。官方文档指出，最稳健的 Bot 角色应当掌控可重复的交付结果，而不是笼统问答；必须从“只读和准备”开始，先由人复核结果，再增加批准动作或例行流程（https://cursor.com/help/grok-bot/use-cases）。

官方团队成员建议，新手上手的第一步是连接日历、邮件等常用应用，给 Bot 提供足够的上下文和工具（https://x.com/poteto/status/2107830403549831186）。实操时先给 Bot 只读权限去扫描收件箱，把近 30 天未互动过的推广邮件归类，提取发件人和退订途径，列出清单供人工核对。社区也有成熟经验：早上醒来时，Bot 已经把收件箱分类完毕，回复草稿都在对话框里等待点击批准（https://x.com/aizhibeibei/status/2108352015319613501）。2026 年 10 月 10 日，官方上线了 Bot 自有邮箱功能，每个 Bot 都能认领专属邮箱地址（https://x.com/bot/status/2108609764766908772）。社区有人在官方邮箱上线前就这么做了：用收信规则先把敏感邮件过滤掉，其余转发给 Bot 使用的代理邮箱，让它总结提醒，主邮箱完全不需要对 Bot 开放写权限（https://x.com/maiff20/status/2106774095820095969）。如果配置 Bot 专属邮箱作为个人助理，不要直接用个人真名做前缀，避免邮件往来抄送时搞混身份（https://x.com/petergyang/status/2108624122339287335）。

随着 2026 年 10 月中下旬 v0.71.2 与 v0.75.2 版本的更新，官方对专属邮箱 `@mail.grokbot.com` 做了两项关键升级（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/agent-email）：首先，由 Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）在 10 月 14 日正式发布的 `+alias` 加号子别名功能（https://x.com/SamSokolin/status/2110496237241667621，获 3,073 赞、219 转发、1,197 书签），允许你在同一个 Bot 邮箱下衍生出无限个细分业务入口（如 `mybot+newsletters@mail.grokbot.com`、`mybot+receipts@mail.grokbot.com`），并配置**仅当邮件发送到指定 `+alias` 别名时才触发对应的 Routine**；其次，v0.75.2 支持了邮件原样转发时完整保留原邮件的 HTML 排版格式、正文内嵌图片（inline images）以及文件附件（https://cursor.com/help/grok-bot/agent-email）。

基于这一特性，X 博主 `@songsong275452`（引用 `@gokul_i` 的方案，https://x.com/songsong275452/status/2113108916229886371）分享了一套彻底解放个人主邮箱的 **Newsletter 专属邮箱接管与周六精华周报**玩法：不再让各种行业通讯（Newsletters）塞满自己的私人 Gmail，而是将所有 Newsletter 订阅地址全部迁移到只有 Grok Bot 才会去读取的 `mybot+newsletters@mail.grokbot.com` 专属别名中；个人主邮箱瞬间恢复清净，再设置一条每周六早上自动运行的 Routine，将过去一周收到的全部 Newsletter 提炼成一份结构化精华周报（甚或直接写入一张实时更新的 Grok Bot Page 看板，https://x.com/bot/status/2112991843235610885）。

除了被动清理推广信，邮箱还是個人财务查漏补缺与每日情报的富矿。加密与 AI 领域知名博主 Miles Deutscher（`@milesdeutscher`）在其收获 3,100 赞、4,503 书签的“10 大逆天 Grok Bot 用例”长推（https://x.com/milesdeutscher/status/2113653680834859262）中，展示了三个与个人邮箱及信息流紧密联动的实战范式：
- **#6 Subscription Auditor（订阅账单审计与自动砍价/退订员）**（https://x.com/milesdeutscher/status/2113653772337770849，54 赞）：让 Bot 深度扫描邮箱里的周期性扣款账单（Receipts / Invoices）与 SaaS 续费通知，列出所有月度/年度订阅清单、识别长期未使用的闲置服务，甚至在获得你批准后，直接替你发邮件或打开客服聊天窗谈判降价折扣（Retention offer）或提交取消订阅申请。
- **#4 Morning Brief Routine（全渠道晨间情报简报）**（https://x.com/milesdeutscher/status/2113653803304296498，35 赞）：每天清晨定时串联你的收件箱未读重要邮件、当日日历日程与 X 平台行业动态，在你起床前生成一份端到端的晨间决策简报。
- **#1 Second Brain / "Obsidian Replacement"（零手动打标签的第二大脑）**（https://x.com/milesdeutscher/status/2113653848581816595，98 赞）：将有价值的邮件长文、X 书签与碎片笔记自动归档到 Grok Bot 的持久化工作区中，用自然语言检索替代繁琐的手动分类打标签。

### 提示词

```text
You are my Email Cleanup Assistant.
Access my connected Gmail inbox in read-only mode for this step.
Scan emails received in the last 30 days that match categories "Promotions", "Social", or contain "unsubscribe" in the body.
Group them by sender domain and count the total messages per sender.
Filter criteria:
1. Identify senders where I have not opened or replied to any message in the last 30 days.
2. For each identified sender, extract the sender name, email address, frequency (emails per week), and the unsubscribe link or unsubscribe email address.
3. Exclude any senders related to banking, order receipts, flights, government notifications, or two-factor authentication.
Output format:
Return a markdown table with columns: Sender Name | Email Domain | Total Received | Unsubscribe URL/Target | Recommendation.
Standing boundaries:
- Do not click any unsubscribe links autonomously.
- Do not delete, archive, or modify any emails.
- Do not send any outgoing emails.
- Present the candidate list to me and wait for my explicit review.
```

如果你还想复刻 `@milesdeutscher` 的 **#6 Subscription Auditor（订阅账单审计员）** 与 `@songsong275452` 的 **Newsletter 周报汇总**，可以直接使用以下组合提示词模板：

```text
You are my Subscription Auditor & Newsletter Digest Bot.
Part 1 — Subscription Audit (Read-only scan):
1. Search my inbox (and messages sent to my +receipts@mail.grokbot.com alias) over the last 90 days for keywords: "receipt", "invoice", "subscription", "renewal", "billing", "charged".
2. Extract: Service Name | Billing Cycle (Monthly/Annual) | Amount | Next Renewal Date | Cancellation/Manage URL.
3. Flag any recurring charges that have increased in price or overlap in functionality, and draft a polite negotiation/cancellation email for my review.

Part 2 — Saturday Newsletter Digest:
1. Read all emails received at my +newsletters@mail.grokbot.com alias over the past 7 days.
2. Deduplicate overlapping AI/tech news, extract the top 5 high-signal insights with original links, and update my "Weekly Reading Digest" Page.

Standing boundaries:
- Never send cancellation emails or click confirmation links without my explicit approval.
```

### Routine

单次任务跑通后，可以固化为定期执行的 Routine。官方文档规定，每个 Bot 最多配置 50 个 Routine，定时执行间隔不得低于 5 分钟，系统只保留最近 20 条运行记录（https://cursor.com/help/grok-bot/routines，https://cursor.com/help/grok-bot/skills-routines-and-automations）。在 2026 年 10 月 22 日发布的 v0.75.2 版本中，官方将 Routine 的小时级运行频率上限大幅上调至：**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots），单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/routines）。邮件巡检可以设成每周日上午 9:00 跑一次，或者针对 `mybot+newsletters@mail.grokbot.com` 配置基于别名收信触发的定向 Routine（https://x.com/SamSokolin/status/2110496237241667621），让 Bot 自动检查过去一周新增的无互动商业邮件或周报，生成待审表格。

配 Routine 时，要照着社区摸索出的路子走：先手动执行并修正偏差，固化为技能后再进行二次输入测试，最后才能挂载为定时 Routine（https://x.com/Michael_Fenech_/status/2106352565528977469）。如果某一周没有符合退订标准的新邮件，要求 Bot 仅输出一行“本周无新增待退订项目”并立即停止运行，避免无意义的空转消耗。官方安全文档规定，后台或 Routine 触发的审批卡大约 10 分钟就会超时失效，卡片显示 Expired 且动作不会执行（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。所以点击退订链接或清理归档这类操作，千万别指望在后台无人值守时完成。Routine 必须卡在生成待审清单这一步，等人工上线进入会话后再点选批准。

### 成本

官方未公布单次邮件扫描与分类的具体 Token 消耗数字。待测 500 封真实邮件收件箱单次扫描消耗的周额度百分比。

套餐费用方面，自 2026 年 10 月 18 日起，官方正式推出 **The X Subscription 三合一统一订阅**（整合 Grok、Cursor 与 X Premium，https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview，https://x.com/bot/status/2110063783796572496），包含 Grok Bot 权限的档位为 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）**（Free $0 与 Plus $8/月 不含 Grok Bot），三端共享同一个周额度池，超额部分通过预付充值 **Prepaid Credits** 扣减；而既有独立订阅的老用户只要不主动通过 `cursor.com/unify` 单向不可逆地切换至新体系，仍可保留原有的独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）或自助式 Teams（$40/人/月）档位（https://cursor.com/pricing，https://cursor.com/help/grok-bot/plans）。社区帖称在 Pro 档位下每条普通对话约消耗 1% 周额度（个例）（https://x.com/miniyarov/status/2105428357273800799）。每周运行一次退订排查对周额度的占用极小。但千万别设成每 5 分钟轮询一次的高频任务，社区帖称每 5 分钟一次的 Routine 单月触发 8,640 次，按 API 估算折合开销约 397 美元（个例）（https://x.com/fleyta88/status/2109346840382415019）。正如中文社区博主 `@charlie_pmp` 所提醒的（https://x.com/charlie_pmp/status/2114214503416271131），在三合一订阅共享周额度池的机制下，高频且未加精简的冗余 Routine 是后台静默吞噬额度的头号元凶。把这类常规维护任务压到每周一次，或改用 `+alias` 邮件精准触发，是最稳妥的控本方式。

### 坑

清理邮件最大的坑，是云电脑共享环境带来的凭据穿透。官方安全文档指出，用户账号下的所有 Bot 共享同一台云电脑环境，文件、浏览器会话和命令行凭据在所有 Bot 之间互通，删除某个 Bot 也不会清除这些共享状态（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。要是你在邮件助手 Bot 里登录了主邮箱，其他写代码或跑外部脚本的 Bot 同样能拿到该浏览器的登录态。千万别把 Bot 之间的分类当成安全隔离边界。

另一个坑是审批超时导致动作悬空。由于后台审批卡 10 分钟自动过期（https://cursor.com/help/grok-bot/approvals-security-and-privacy），如果把 Routine 设定为“发现垃圾邮件直接弹出退订审批”，人一离开屏幕卡片就会失效，任务根本跑不成。另外，垃圾邮件常包含恶意钓鱼链接，让 Bot 在云端浏览器中无节制点击外链极易遭遇安全风险。必须坚持**草稿优先原则**，在设置中为所有外部请求配置明确的审批卡，决不允许 Bot 绕过人工直接跳转外部退订网页。

## 14.2 旅行全程管家（Google Maps + Gmail）· Travel Concierge

> [!NOTE]
> 📸 **截图位（待补）**：Bot 从 Gmail 提取订单数据并在云电脑整理行程时间线
> [!NOTE]
> 📸 **截图位（待补）**：云电脑浏览器调用 Google Maps 计算多目的地路线与耗时
> [!NOTE]
> 📸 **截图位（待补）**：移动端通过语音通话向 Bot 询问当日备选餐厅与路线

### 场景

规划家庭旅行很费神：比对机票确认信、酒店确认函、通勤路线和景点开放时间，得在几个平台之间来回切。官方团队成员在访谈中提到，她日常使用名为 Suki 的个人助理 Bot，在获得人工审批的前提下通过预订平台安排多段复杂行程（https://www.youtube.com/watch?v=xZ5TEaleUdg （团队成员访谈））。在度假场景下，可以让 Grok Bot 扮演旅行管家。

官方在 2026 年 10 月 8 日上线了 Google 连接器（https://x.com/mattyp/status/2107886668892057614）。Bot 可以通过只读模式调取收件箱里的机票和酒店订单，提取航班时间、航站楼和酒店入住时段；再在云电脑自带的浏览器里打开 Google Maps，测算酒店到各景点的公共交通耗时，核验营业时间，排查时间冲突。在价格追踪上，社区博主 Peter Yang 实测发现，让 Grok Bot 与 Meta Muse 追踪同一段日本航班行程时，Muse 给出的推荐价格比 Grok Bot 贵了 1,000 美元以上（https://x.com/petergyang/status/2103693608729932025）。在旅途中，还可以利用官方在 2026 年 9 月 18 日推出的移动端语音功能，对着手机语音查询当日行程或口述记录备选地点（https://x.com/elonmusk/status/2100698004210475317，https://x.com/bot/status/2100659463569170779）。

到了 2026 年 10 月下旬，旅行管家的随身体验迎来了三次质的飞跃：
1. **iOS 原生日历（Calendar）、提醒事项（Reminders）与通讯录（Contacts）直读与操作（v0.75.2）**：官方在 2026 年 10 月 22 日发布的 v0.75.2 更新中，正式为 iPhone 客户端打通了系统级原生日历、提醒事项和通讯录权限（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/mobile）。这意味着旅行管家 Bot 不仅能查 Gmail 里的航司确认信，还能直接核对你 iPhone 本地日历上的私人安排、把值机提醒和行李打包清单直接写进 iOS 原生 Reminders，并从通讯录调取同行亲友或接机司机的联系方式。
2. **iPhone Action Button 一键实时语音通话（iOS v1.16+）**：官方于 10 月 19 日正式上线 Action Button 侧边按钮快捷指令支持（https://cursor.com/help/grok-bot/voice-chat，https://x.com/bot/status/2112246033178968161，获 7,264 赞、2,213 书签；`@SawyerMerritt` 实机演示见 https://x.com/SawyerMerritt/status/2112252980015579431）。在异国街头拖着行李箱赶路时，你无需解锁屏幕打字，只需长按 iPhone 15 Pro 及后续机型的侧边 Action Button（或像 `@D__cup` 那样佩戴 Shokz 骨传导耳机全天候免提唤醒，https://x.com/D__cup/status/2114211130365358350；或参考 `@TyeInBloom` 将 iOS 原生三件套、1Password、Action Button 与 `"Hey Siri"` 快捷指令深度联动，https://x.com/TyeInBloom/status/2113767679588770271），即可直接对旅行管家 Bot 口述：*“我们刚出成田机场海关，帮我看一下去涩谷酒店最快的一班 NEX 成田特快是几点，顺便在日历里把晚餐推迟半小时。”* 通话挂断瞬间，会话流会自动生成带完整逐字稿的 **Voice chat card** 并立即跟进执行（https://cursor.com/help/grok-bot/voice-chat）。
3. **Grok Bot Vault 差旅卡明文 Hint 精准分账（v0.75.5）**：在 10 月 23 日上线的内置加密保险箱 **Vault**（`Settings → Vault`，https://cursor.com/help/grok-bot/secrets，https://x.com/bot/status/2113754107861532677）中，你可以同时保存个人家庭信用卡与公司商务卡，并为商务卡填写明文 **Hint** 标签（例如 `"Use for work travel only"` 或 `"Corporate Amex"`）。由于 Bot 能够读取明文 Hint 却永远看不到加密卡号与 CVV，当你在公务出差与私人顺道度假混合的行程（Bleisure travel）中预订机酒时，Bot 会严格按照 Hint 自动挑选对应的差旅卡或个人卡完成安全注入（`BrowserSecureFill`），彻底杜绝公私账单混刷。

### 提示词

```text
You are my Travel Concierge Bot.
Review my connected Gmail inbox for flight and hotel confirmation receipts for the upcoming trip to Tokyo (dates: Oct 20 - Oct 25).
Tasks:
1. Extract arrival/departure flight numbers, terminals, times, and hotel booking details (hotel name, address, check-in window).
2. Open Google Maps in your browser and calculate transit times between the hotel and the target locations in the attached wishlist: Shibuya Sky, Senso-ji, Akihabara, and teamLab Planets.
3. Verify opening hours and popular visiting hours for each spot to prevent scheduling during closing times.
4. Generate a day-by-day itinerary table with columns: Day | Time Window | Activity | Location | Transit Time | Notes.
Standing boundaries:
- Do not book tickets, modify reservations, or pay for any services.
- Do not contact hotels or airlines.
- If any schedule conflict arises, highlight it in the notes and ask for my input.
- Return the finished itinerary table directly in chat for review.
```

如果你已在 iPhone 上授权了 v0.75.2 的 **iOS 原生日历、提醒事项与通讯录**，并配置了 **Vault 差旅卡 Hint**，可以追加如下进阶指令：

```text
Additional iOS & Vault Integration Tasks:
1. Cross-check the extracted flight and hotel windows against my native iOS Calendar to ensure no overlap with existing personal or work appointments.
2. Create a "Tokyo Packing & Check-in" list in my native iOS Reminders with time-based alerts 24 hours before each flight departure.
3. Look up my travel companions' contact details from iOS Contacts and attach emergency contact numbers to the itinerary Page.
4. If I explicitly ask you to book an airport transfer or business hotel extension later, check Settings -> Vault Hints and ONLY select the card with Hint "Use for work travel only" for business days (Oct 20-22), and my personal card for vacation days (Oct 23-25).
```

### Routine

出发前 3 天，可以把行程监控挂载为定时 Routine，设在每天傍晚 18:00 运行一次。让 Bot 自动同步航班动态，拉取目的地未来 24 小时天气情况，并在云电脑内复查 Google Maps 上的实时路况，生成次日出行便签。在 v0.75.2 版本下，全账号所有 Bot 合计可执行 300 次/小时、单条 Routine 最高 200 次/小时（定时最小间隔仍为 5 分钟，https://cursor.com/help/grok-bot/routines），完全足以支撑旅途中的高频航班异动与登机口变更告警。

根据社区推荐的五阶段晋升流程，自动化必须经历验证单次任务、提炼方法、沉淀为技能、换一份输入测试，最后才能设定 Routine（https://x.com/kocer_eth/status/2105008655770788250）。如果当天没有任何航班延误或恶劣天气预警，Routine 只在对话框中给出一行正常确认，绝不重新输出整页冗长的行程单，确保信息流保持清爽。

### 成本

官方未公布多工具交互与地图排期的具体 Token 消耗数字。待测 5 天跨时区行程排期任务中浏览器交互与文本解析的额度消耗。

套餐门槛方面，用户既可选择 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，三端共享周额度池 + Prepaid Credits 预付额度，https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview），老用户也可继续保留既有的独立 Cursor Pro 每月 20 美元套餐（https://cursor.com/pricing，一旦通过 `cursor.com/unify` 切换至三合一订阅则不可逆）。官方帮助文档警告，免费试用是一笔固定用量额度并带有 7 天窗口，长任务有可能在单次执行中耗尽全部试用额度，且官方不予补发（https://cursor.com/help/grok-bot/plans）。在试用阶段测试多步骤旅行规划时，应当尽量限定查询景点的数量，避免一次性派发过于庞大的搜索指令。

### 坑

在云端浏览器中使用地图或查询订票网站时，最常遇到的问题是数据中心 IP 遭遇服务拦截。Grok Bot 的云电脑架设在境外机房，直接访问某些本地化预订平台或交通网站时，往往会被识别为爬虫并弹出难以通过的验证码，甚至直接拒绝连接。此时需要在设置中开启**本地出口路由**（Settings → Computer → Route egress，在最新客户端中也显示为 `Settings > Computer > Your computer > Route traffic through this computer`，https://cursor.com/docs/grok-bot/settings），让云电脑的网络流量绕回你本人的本地设备出口，走真实的个人家庭宽带网络（需要你的桌面电脑开着 Grok Bot 桌面端，或者像 `@ericzakariasson` 分享的那样在家里常开一台 Mac mini 作为远程计算与流量节点，https://x.com/ericzakariasson/status/2114095056630272099）（https://x.com/xiaohu/status/2099409639234289914，以及 `@XueshiQiao` 的实测验证 https://x.com/XueshiQiao/status/2112866936229183589）。

另一个严重风险是证件信息泄露。旅行行程中充斥着护照号码、身份证件、常客卡账号及支付信息。官方安全文档强调，绝不能在常规聊天中明文发送密码、一次性验证码或敏感证件信息（https://cursor.com/help/grok-bot/approvals-security-and-privacy，https://cursor.com/help/grok-bot/secrets）。当预订流程需要登录航司或酒店会员账号、填写真实身份或输入付款信息时，官方现在提供了标准的五级安全登录与四级结账链路（https://cursor.com/docs/grok-bot/work）：你可以使用 **1Password Brokered Sign-in**（在手机或电脑 1Password App 内逐次生物识别审批注入，https://cursor.com/help/grok-bot/connect-apps）、**Grok Bot Vault**（只写加密存储并通过 `BrowserSecureFill` 注入，https://cursor.com/help/grok-bot/secrets）、聊天内掩码 **Secure Form**，或者在 Agent Computer 界面中点击 Take control（Take over screen）人工接管屏幕，手动输完后再交还控制权。但务必注意官方文档与社区博主 `@kial`（https://x.com/kial/status/2114201768414646280）、`@JianWeiSignal`（https://x.com/JianWeiSignal/status/2114195530611855488）共同指出的关键风控边界：**保存在 Vault 中的银行卡在结账自动填充时，不会触发单独的逐笔 Vault 弹窗确认**（https://cursor.com/help/grok-bot/secrets）；如果你希望每笔机酒预订都亲手把关输入卡号，切勿将主力信用卡常驻保存在 Vault 中。此外，模型对机票酒店退改政策容易产生幻觉，在提示词中必须强制要求给出邮件原始出处，不可轻信模型的概括。

## 14.3 孩子学校消息汇总 · School & Family Digest

> [!NOTE]
> 📸 **截图位（待补）**：Bot 从转发的家校通知中提取作业与签字待办项
> [!NOTE]
> 📸 **截图位（待补）**：每日下午生成的结构化家庭待办与日程提醒卡
> [!NOTE]
> 📸 **截图位（待补）**：纠错时 Bot 依据原始通告文件更新日历事项

### 场景

家有学童的家长都知道学校通知有多碎。班级群消息、老师邮件和各类系统通告混在一起，有当晚必须完成的作业，有下周活动的着装说明，还有限时签字和缴费，稍不留神就会遗漏。官方文档在列举典型用例时，重点介绍了**首席幕僚模式**（Chief of Staff）：跨渠道梳理出带有原始出处链接的关键摘要，只提炼符合既定优先级的重要事项，说明原因并给出建议，同时绝不擅自发送对外消息或修改日程（https://cursor.com/help/grok-bot/use-cases）。

官方团队成员在访谈中证实，这种总助模式在早期内测的第二周就自然涌现出来了（https://www.youtube.com/watch?v=maSdsTLaMuU （团队成员访谈））。针对国内学校通知依赖即时通讯工具且无官方插件的现状，社区实践者探索出了可靠的数据入口：利用本地只读工具（如 WeChat Portal）直接读取本地缓存的通告文本（https://x.com/lens2645211/status/2108184037198266383），或者通过自动规则把家校邮件转发到 Bot 的自有邮箱中（https://x.com/bot/status/2108609764766908772）。象鱼工作流在总结国内平台用法时也强调，国内平台没有插件时切忌用 Bot 频繁模拟点击，把文本导出或转发给 Bot 处理是避免账号风控的最佳对策（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

除了每日放学后的常规通告汇总，Grok Bot 在处理**跨周期、高复杂度的家庭重大事项（如身份续签、跨区择校插班、升学备考与家庭事务统筹）**时更能发挥“长期记忆 + 7×24 云电脑”的优势。中文社区博主 0xbitman（`@bitman2140`）在 2026 年 10 月 25 日分享了极具代表性的华人家庭真实案例（https://x.com/bitman2140/status/2114210291546493153）：他一人在 Grok Bot 上同时并行跑通了 8 条端到端生活与工作流，其中前 3 条全部直接服务于家庭与子女教育：
1. **香港优才计划（Quality Migrant Admission Scheme）续签材料跟进**：让专职 Bot 长期追踪香港入境事务处的续签要求清单、在港通常居住证明文件、雇佣合同与税单时间节点，自动比对缺漏材料并生成补件倒计时提醒。
2. **香港孩子学校插班（School Transfer）全流程信息搜集与申请管理**：香港官津、直资与私立学校的春季/秋季插班（叩门）窗口期各不相同且极其分散。`@bitman2140` 让 Grok Bot 持续巡检目标中小学官网的插班招生简章、报名截止日期、笔试/面试科目要求及往年家长面经，汇总成结构化对比表并协助准备申请文书材料包。
3. **孩子日常考试备考辅导**：根据学校公布的教学大纲与测验范围，让 Bot 结合云电脑排版生成针对性的模拟练习题、错题解析与每日复习计划表。

与此同时，在英文社区中，`@Butlergrokbot`（The Butler，https://x.com/Butlergrokbot/status/2111860108070445394）专门展示了基于多条 Grok Bot Routines 构建的**家庭管家（Family Butler）**体系——结合 v0.75.2 新增的 iOS 原生日历与提醒事项同步能力（https://x.ai/changelog/bot），把全家的学校校历、课外兴趣班接送排班、家庭账单到期日与周末采购清单统一收口到一位随叫随到的 AI 家庭总管手中。

### 提示词

```text
You are my Family & School Assistant, acting under Chief of Staff principles.
Review the school notices, class updates, and teacher emails provided in /workspace/school_inbox.
Tasks:
1. Filter information relevant only to my child (Grade 3).
2. Categorize all findings into three distinct blocks:
     - Student Homework: tasks the child must complete today, with explicit deadlines.
     - Parent Action Items: items requiring parental signature, fee payment, or confirmation forms.
     - Upcoming Events: calendar items for the next 7 days (dress code, field trips, holidays).
3. For every single extracted item, provide the exact source quote and file name.
4. If a notice contains no actionable deadline or requirement, classify it as general announcement and summarize in one line.
Standing boundaries:
- Do not send messages, replies, or emails to teachers or class groups.
- Do not sign or submit any electronic forms automatically.
- If any date or requirement is ambiguous, explicitly mark it as "Unconfirmed" instead of guessing.
```

如果你正在像 `@bitman2140` 一样办理**香港孩子学校插班（School Transfer）与优才续签材料追踪**，可以新建一个独立的家庭专项 Bot 或 Page 看板，使用以下提示词：

```text
You are my HK Family Relocation & School Transfer Coordinator.
Maintain a live Grok Bot Page titled "HK School Transfer & Visa Tracker" and update it based on /workspace/hk_family_docs and official school websites.
Tasks:
1. School Transfer Tracker: Monitor the official admissions pages of our target Hong Kong DSS and government-aided primary schools for mid-year / autumn transfer (插班) openings. Record: School Name | Grade | Application Window | Required Documents | Written/Interview Dates | Source URL.
2. Exam Prep: Based on the syllabus in /workspace/school_inbox, generate a 20-minute daily bilingual (English & Traditional Chinese) practice worksheet for my child.
3. Quality Migrant Visa Renewal: Cross-check our checklist in /workspace/hk_family_docs/visa_checklist.md against expiration dates and alert me 30 days before any residence proof or tax document needs updating.
Standing boundaries:
- Never submit online school application forms or upload identity documents autonomously.
- Every admissions date must include the direct official school webpage URL for human verification.
```

### Routine

将该任务配置为每个工作日下午 16:30 触发的定时 Routine。让 Bot 自动读取当天收纳到文件夹中的所有通告（或转发至 `mybot+school@mail.grokbot.com` 专属别名的家校邮件，https://x.com/SamSokolin/status/2110496237241667621），在半小时内输出一份清晰的三栏待办清单。在 v0.75.2 最新配额下，全账号所有 Bot 合计支持 300 次/小时、单条 Routine 最高支持 200 次/小时运行（定时最小间隔仍为 5 分钟，https://cursor.com/help/grok-bot/routines）。

设计家庭日常 Routine 时，要吸取社区博主 kocer_eth 的警告：定期审计你的 Routine，对于那些虽然每天准时报到、但实际上从没改变过任何实际决策的任务，果断淘汰（https://x.com/kocer_eth/status/2101669438038634827）。如果当天下午学校没有任何新通告，让 Bot 仅发送单行提示“今日无新增学校通告”，坚决不重发旧内容。要是发现 Bot 提取的作业截止时间有误，按社区纠错原则来：当信息有事实出处时，要求 Bot 回查原始文件来源后再回答，而不是让它凭空再猜一次（https://x.com/Michael_Fenech_/status/2106729045878514147）。

### 成本

官方未公布多格式家校通告结构化解析的单次 Token 消耗数字。待测 30 份真实家校通告文本文件夹提炼信息的周额度消耗。

个人套餐方面，新订户可开通 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，三端共享周额度池 + Prepaid Credits 预付额度，https://cursor.com/help/grok-bot/plans），既有老订户仍可维持独立 Cursor Pro 每月 20 美元套餐（https://cursor.com/pricing，通过 `cursor.com/unify` 切换至三合一订阅后不可退回）。社区用户抱怨称，如果盲目建立多个 Bot 并不停轮询，往往只撑两天就会把每周额度打光，而随后的按需付费或额外充值相当昂贵（https://x.com/RichSilver/status/2108053489620504822，https://x.com/charlie_pmp/status/2114214503416271131）。对于学校消息汇总，工作日每天傍晚只跑一次，既能确保信息零遗漏，又几乎不产生额外的额度压力。

### 坑

在家庭信息处理中，最大的隐患是隐私数据在多 Bot 间无序共享。Shane Mac 曾遭遇过惨痛事故：他的个人财务 Bot 把包含月度银行账单和刷卡支出的个人审计结果，直接发到了公司高管的公用 Slack 频道中，根源就在于不同 Bot 共用同一台云电脑，聊天会话发生混淆（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。学校通告以及优才续签、插班申请材料中包含孩子的全名、出生证明、护照/港澳通行证号、班级学号、家庭住址和家长电话，这些信息如果长期堆放在云电脑的公共根目录，很容易被其他用于业务测试的 Bot 读取甚至误传。每次处理完通知后，必须按照官方安全规范及时从工作空间清理包含隐私的临时文件（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。

第二个坑是自动打卡和代回确认。有些家长为了省事，试图让 Bot 代替自己在班级群里自动回复“收到”或者自动填写健康打卡表单。这种自动化极其危险，一旦遇到特殊调查问卷或表单格式变更，Bot 胡乱勾选提交会引发严重问题。对外交互必须死守在审批防线之后，Bot 只能生成填表草稿，绝不能拥有直接提交表单的权力。没有新内容就保持沉默，警惕形式主义刷屏。

## 14.4 购物比价与下单（审批）· Shopping & Checkout

> [!NOTE]
> 📸 **截图位（待补）**：Bot 在多个电商页面抓取乐高套装实时价格与历史走势
> [!NOTE]
> 📸 **截图位（待补）**：达到目标折扣后 Bot 弹出待审批的结账确认卡片
> [!NOTE]
> 📸 **截图位（待补）**：通过 Agent Computer 人工接管输入支付验证码并完成订单

### 场景

跨平台追踪心仪商品的价格并等待促销降价很耗时间。官方在采购案例中展示了 Haggle Bot 的具体成效：通过全网监控供应商花费与合同条款，一笔科技采购订单从 14,629 美元降至 6,143 美元（降幅达 58%），最终由 Amazon Bot 协助下单完成（https://x.ai/news/grok-bot-procurement）。在个人生活中，这套逻辑完全可以用来盯守高单价数码产品、绝版玩具或者乐高积木套装。

社区博主 liam_fallen 分享过真实经历：在全网现货售罄、苹果官方渠道需要等待数周的情况下，他向 Grok Bot 提供虚拟卡权限，让 Bot 自动发邮件询问线下门店寻库，成功找到现货并在核准后下单配送上门（https://x.com/liam_fallen/status/2109332219126784098）。X 上的 @grok 自动回复账号（AI 生成的回复，不是官方声明）在回答网友时说：Grok Bot 可以搜索最佳价格并代为下单，购买前会显示金额让你批准，再通过 Stripe Link 付款（https://x.com/i/status/2109347617398264294）。官方也在 2026 年 10 月 9 日上线了 Shopify 集成，支持订单和库存状态的追踪（https://x.com/bot/status/2108228871938359347）。

而在 2026 年 10 月 14 日至 10 月 23 日短短十天内，Grok Bot 的个人购物与支付基础设施完成了一次从底层凭据到兜底保障的全面革新（https://x.ai/changelog/bot，https://cursor.com/docs/grok-bot/work）：
1. **官方标准四级结账链路与五级登录链路正式成型**：根据官方最新 [Work 技术文档](https://cursor.com/docs/grok-bot/work) 与 [Secrets & Vault 帮助文档](https://cursor.com/help/grok-bot/secrets)，现在当 Bot 帮你网购下单时，不再局限于早期单一的手动接管屏幕，而是遵循严谨的优先级调用链：
   - **网站登录（Sign-in）五级优先级**：云电脑已保存的浏览器会话（Saved browser session） → **Grok Bot Vault** → **1Password（Brokered Sign-in 逐次生物识别授权）** → 聊天内掩码 **Secure Form** → **Take over screen（人工接管屏幕）**。
   - **结账付款（Checkout / Payment）四级优先级**：**Grok Bot Vault**（内置加密保险箱，支持手机摄像头扫卡录入与 `BrowserSecureFill` 零明文注入，https://x.com/bot/status/2113754107861532677） → 聊天内掩码 **Secure Form** → **Link / X Money**（v0.71.2 正式支持；如 `@gofordylan` 实测晒单所示，使用 X Card 经由 Grok Bot 付款后，账单流水旁会点亮专属的 Grok Bot 小徽章，https://x.com/gofordylan/status/2110726444485607797） → **Take over screen（人工接管屏幕）**。
2. **Elon Musk 宣布 SpaceX 全额赔付兜底背书**：针对许多用户对“让 AI 绑卡代购万一买错东西或泄露卡号怎么办”的顾虑，2026 年 10 月 15 日，Elon Musk（`@elonmusk`）公开发帖做出硬核承诺（https://x.com/elonmusk/status/2110610960474079445，获 17,221 赞、1,686 转发、2,128 书签）：*"This works well. If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole."*（这套机制非常好用。如果 Grok Bot 在代购时犯错或泄露了你的银行卡——迄今从未发生过——SpaceX 将为你全额赔付。）
3. **清晨按一下 Action Button 给妻子点一杯热星巴克**：有了 iPhone Action Button 一键语音（v1.16+，https://x.com/bot/status/2112246033178968161）与 1Password 免密代理登录（https://x.com/bot/status/2113301060811161874，https://x.com/1Password/status/2113276767582498943），日常高频小额消费变得充满温情。社区开发者 `@JCOMBuilds` 在 2026 年 10 月 21 日分享了他的每日晨间习惯（https://x.com/JCOMBuilds/status/2112997408510452123）：每天早晨起床，他只需长按 iPhone 侧边的 Action Button，对着自己的个人助理 Bot `"Eve"` 说一句给妻子点星巴克咖啡；`"Eve"` 随即在云电脑里打开点单页面，请求调用存储在 1Password 里的账号凭据，他在手机上轻轻一点生物识别批准，Bot 便自动选好常喝的口味与门店完成下单准备。

### 提示词

```text
You are my Personal Shopping & Price Tracker Bot.
Monitor the pricing for the item: LEGO Star Wars Millennium Falcon (Set 75192) across official online stores and authorized retailers (Amazon, LEGO Store, Target, Walmart).
Target condition:
- Base MSRP is standard retail; trigger an alert if the verified price drops below $700 or if a bundle coupon offering >= 15% discount is detected.
- Check in-stock status and seller reputation (only sold and shipped by authorized platform or official brand store).
Tasks:
1. Record current price, shipping fee, delivery estimate, and seller name across all platforms.
2. Compare total checkout price including shipping.
3. If target condition is met, prepare a purchase action card with direct item link and final amount.
Standing boundaries:
- Do not proceed past the cart page automatically.
- Never click "Place Order" or submit payment without my explicit approval.
- Do not input payment details into chat.
- If a CAPTCHA or two-factor prompt appears, stop and alert me to take control.
```

如果你想复刻 `@JCOMBuilds` 的 **Action Button 语音召唤 + 1Password / Vault 快速复购（如点星巴克或日用品补货）**，可以将以下 SOP 写入你的个人助理 Bot：

```text
You are Eve, my Personal Coffee & Daily Reorder Assistant.
When I trigger a voice chat via my iPhone Action Button asking to order coffee or reorder household staples:
1. Sign-in flow: Follow the official priority order — use saved browser session first, or request my login via 1Password Brokered Sign-in (wait for my Review in 1Password biometric approval). Never ask me to type passwords in chat.
2. Order configuration: Select my saved default store address (from Settings -> Vault Contact info) and load my wife's favorite Starbucks order (or specified item).
3. Checkout & Approval gate: Stop at the final checkout screen, verify the item, store location, pickup time, and total price, and trigger an explicit purchase approval card before completing payment via Vault / Link / X Money.
```

### Routine

按照官方 Haggle Bot 的运行范式，系统应当围绕真实变动而非高频轮询展开（https://x.ai/news/grok-bot-procurement）。比价 Routine 可以设定为每天早晚各运行一次（上午 10:00 与晚上 20:00），避开凌晨无促销变动的时段。

官方文档规定，Routine 定时最小间隔为 5 分钟，v0.75.2 起全账号所有 Bot 合计上限为 300 次/小时、单条 Routine 最高 200 次/小时（https://cursor.com/help/grok-bot/routines），且当用户长时间不活跃时，系统可能会询问并自动暂停 Routine，以控制无人值守时的消耗（https://cursor.com/help/grok-bot/skills-routines-and-automations）。当 Bot 巡检发现某平台价格击穿目标阈值时，Routine 会在对话流中生成购买审批卡，列清含税总价与直达购买链接；如果价格未达标，则静默记录日志并退出，绝不打扰人。

### 成本

官方 Haggle Bot 采购案例展示了 58% 的价格缩减成果（订单金额从 14,629 美元降至 6,143 美元）（https://x.ai/news/grok-bot-procurement）。关于个人日常商品爬取与比价的实际 Token 消耗，官方未公布具体数字。待测 4 家主流电商网站持续巡检 14 天的周用量占比。

软件服务成本方面，新用户可通过 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，三端共享周额度池 + Prepaid Credits 预付额度，https://cursor.com/help/grok-bot/plans）获取权限，老用户也可保留既有的独立 Cursor Pro 套餐每月 20 美元（https://cursor.com/pricing，一旦在 `cursor.com/unify` 单向升级至三合一订阅则无法退回旧计划）。必须警惕过度监控带来的隐形成本：社区帖称如果将 Routine 设为每 5 分钟一次的高频轮询，一个月 8,640 次触发按 API 估算可烧掉约 397 美元（个例）（https://x.com/fleyta88/status/2109346840382415019）。每天早晚各巡检一次，或者像本书作者 Mr.鼓先生（`@StarkLJM`）在榜单监控实战中所演示的那样——让 AI 花 28.6 秒写好确定性的 Python 价格抓取脚本，日常用脚本零 Token 额度跑轮询，仅在发现降价时才唤醒大模型处理（https://x.com/starkljm/status/2111803996734419377），即可在额度极省的前提下覆盖绝大多数日常降价活动。

### 坑

在涉及真实资金交易的场景中，资产安全是绝不可退让的底线。官方安全与审批文档明确规定，购买与资金转移属于高危动作，必须始终置于显式审批边界之后（https://cursor.com/help/grok-bot/approvals-security-and-privacy，https://cursor.com/docs/grok-bot/security）。尽管社交平台上曾有拍信用卡照片发进聊天窗口给 Bot 的旧说法，但 @grok 的这条回复也提醒，隐私政策建议不要在提示词里放信用卡等敏感信息（https://x.com/i/status/2109347617398264294）。如今在 v0.75.5 体系下，官方已将结账流程升级为 **`Vault → Secure Form → Link / X Money → Take over screen` 四级安全结账链路**（https://cursor.com/docs/grok-bot/work，https://cursor.com/help/grok-bot/secrets）：如果你确实需要扫卡录入，只能进入 `Settings → Vault → Add card` 使用官方加密摄像头扫描（数据只写加密、Bot 永远看不到完整卡号与 CVV），或通过聊天内掩码 Secure Form、Link / X Money，以及在 Agent Computer 界面执行**人工接管控制权（Take over screen）**由用户本人手动完成付款确认，绝不能在常规聊天框中明文发送任何付款卡号或安全码（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。

**尤其需要再次敲响警钟的是 Vault 存卡与不存卡的审批差异**：正如官方 [Secrets & Vault 帮助文档](https://cursor.com/help/grok-bot/secrets) 所明确记载，以及英文社区 `@kial`（https://x.com/kial/status/2114201768414646280）与中文社区 `@JianWeiSignal`（见微｜Signal，https://x.com/JianWeiSignal/status/2114195530611855488，https://x.com/JianWeiSignal/status/2114195638988501103）重点警示的那样——**保存在 Grok Bot Vault 中的银行卡，在结账自动填充（`BrowserSecureFill`）时不会弹出单独的逐笔 Vault 卡片填充确认框**，仅受通用购买审批规则约束！因此，这里强烈建议遵循社区总结的两条风控铁律：
- 如果你希望对每一笔消费都保持最高级别的手动把关，**切勿将主力大额信用卡常驻保存在 Vault 中**（或在用完后从 `Settings → Vault` 中移除，改用每次结账弹出聊天内 Secure Form 时单次输入且不勾选保存，或只放一张限额的虚拟卡/预付卡）。
- 如果你同时使用 1Password 与 Grok Bot Vault，可以采纳 `@martinpaulweiss` 提出的 **“一密一宅（One home per secret）”拆分法**（https://x.com/martinpaulweiss/status/2114210343467536531）：日常电商与网站登录凭据（连同 2FA 动态验证码）统一存放在 1Password 中，通过 Brokered Sign-in 逐次审批调用；Grok Bot Vault 仅存放常用收货地址与专门用于小额代购的独立卡片，并使用 `@LisaMAUSA` 分享的 **Vault Tidy** 思路定期清理重复条目（https://x.com/LisaMAUSA/status/2114208018388643852）。

第二个坑是电商网站的反爬与风控封号。主流电商平台对机房 IP 的识别非常严格，Bot 频繁在云电脑中打开商品页极易触发滑动验证码或人机校验。遇到风控时，强行让 Bot 自动化重试很容易导致电商账号被封禁，此时必须配合本地出口路由（`Settings > Computer > Your computer > Route traffic through this computer`）将流量转回个人本机住宅 IP（https://x.com/xiaohu/status/2099409639234289914，https://x.com/XueshiQiao/status/2112866936229183589）。第三个坑是限时特价与审批超时冲突。官方后台审批卡大约 10 分钟自动过期（Expired）（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。如果遇到库存极少的闪购特价，一旦没能在 10 分钟内点击 Allow once，卡片就会失效并取消操作。高时效性的秒杀抢购并不适合离线 Routine，必须在人守在屏幕前时以人机协同的方式半自动完成。


# §15 内容创作 · Creators

很多人把 Grok Bot 当成另一个网页聊天窗口，每次想发内容就打开它问一句帮我写条推文。这种用法把它的后台例程和云电脑完全浪费了。我调研发现，做内容创作时，Grok Bot 真正的分水岭不是文笔，而是你从亲自干活的作者变成了调度流水线的**责任主编**。

> **适合谁**：做 X、公众号、小红书、短视频的个人创作者。15.1 需要 X 账号，例程示例把结果推到 Slack（没有 Slack 就把"Send it to me on Slack"改成"在对话里告诉我"）；15.3 涉及脚本和命令行，零代码读者可以只看思路，把提示词整段交给 Bot 去执行。

![内容创作从单次对话到无人值守流水线的演进路径](../images/fig-15-1.png)

*图：内容创作从单次对话到无人值守流水线的演进路径*

### 15.1 X 监控 4 个 Routine · X Monitoring Routines

#### 场景
做内容天天自己刷推特找素材，效率太低了。2026 年 10 月 8 日，官方宣布 Grok Bot 原生支持搜索、阅读和监控 X（https://x.com/bot/status/2107949161878606089）。早在 8 月 30 日官方就宣布：关联 X 账号后，系统会自动创建开发者账户并附带一些初始额度（https://x.com/bot/status/2093822274067706170）。有了这个能力，就能让 Bot 充当全天候雷达。
Rowan Cheung 基于这次更新设计了 4 个监控例程（https://x.com/rowancheung/status/2108328114552000842）：挖别人在跑的真实 AI 工作流、盯自己品牌的提及和口碑、抓竞品品类里的潜在客户痛点，以及跟进刚加的新人脉。我看他的例程，结构写得很死：卡死时间和时区、限定时间窗口、写清过滤规则、定死输出字段、绑好 Slack 投递，严格禁止私自跟外界互动，没抓到结果时也有单行兜底。

进入 2026 年 10 月中下旬，社区与官方进一步把 X 监控进化成了全链路双语运营、私信分拣与跨平台改写系统：
1. **24 小时中美时差双语 X 运营工作流（`@sisiliu517`）**：创作者 siyuan liu（`@sisiliu517`，2026-10-15，https://x.com/sisiliu517/status/2110869965612183642）利用小时级 Routine 配合中美时差策略，搭建了日夜轮转的双语运营体系——**白天时段主攻中文 X 圈层互动与发帖，夜间时段自动切换为英文 X 圈层运营**。每天深夜，Bot 还会自动拉取当日帖子表现生成一份互动数据复盘报告，直接反哺并迭代次日的选题方向与高优回复目标账号列表（High-priority reply targets）。
2. **`@chat` 端到端加密私信与陌生人消息请求自动分拣（`@pjvann`）**：2026 年 10 月 16 日，X 与 Grok Bot 工程师 Paul Vann（`@pjvann`，1,069 赞 / 108 转发 / 132 书签，https://x.com/pjvann/status/2111104660773687646）宣布 Grok Bot 正式打通 X 的 `@chat` 端到端加密私信收件箱与陌生人消息请求（message requests）。底层通过沙箱克隆官方解密辅助库（https://github.com/xdevplatform/xchat-grokbot-helper）并配合用户 4 位数字 X Chat PIN 码在本地解密。`@pjvann` 分享了自己整周让 `@bot` 自动审查陌生人私信请求、过滤垃圾营销、批准高价值合作私信并起草回复草稿的真实工作流。
3. **Personal 𝕏 Assistant 与 Content Repurposer 爆款多平台分发（`@milesdeutscher`）**：Miles Deutscher（`@milesdeutscher`）在其获 3,100 赞、4,503 书签的“10 大逆天 Grok Bot 用例”长推（https://x.com/milesdeutscher/status/2113653680834859262）中，公开了两套创作者核心打法：
   - **#10 Personal 𝕏 Assistant（个人 X 运营副驾）**（72 赞，https://x.com/milesdeutscher/status/2113653710631166414）：集个人品牌研究员、黄金开头（Hook）专家与每日初稿写手于一身，根据账号过往高赞推文的语感与结构，每日自动生成待发推文草稿。
   - **#5 Content Repurposer（一鱼多吃跨平台内容改写器）**（34 赞，https://x.com/milesdeutscher/status/2113653788196430242）：自动抓取 X 平台上的爆款异常值（outlier）帖子，调用自定义 Agent Skills 将其一键改写为适配 LinkedIn 专业长贴、邮件通讯（Newsletter）与短视频口播脚本的多平台版本。

#### 提示词
例程 1：抓取真实 AI 工作流
```text
Every weekday at 9:15am in my time zone, search X and the web for new AI workflows people are actually running. Keep only cases that name the old task, the tool, and the result: time saved, a step removed, or a handoff that used to need a person. Drop product announcements, "10 prompts" threads, and anything the author has not used more than once. Return at most 3. For each, give the link, the job it replaces, what I would need connected, and whether it fits my work. Send it to me on Slack. Do not post or reply anywhere else. Save this as a routine. If nothing qualifies, send one line saying so.
```

例程 2：品牌提及监控
```text
Every weekday at 9:00am, search X for mentions in the last 24 hours of [your brand, @handle, or your own name]. For each hit, give the author, link, a one-line summary, and whether it is praise, complaint, question, or neutral. Do not reply to anyone. Post the digest in [your Slack channel] and tag me. Save this as a routine. If a source is unavailable, say which one.
```

例程 3：潜在客户监听（每 4 小时）
```text
Every 4 hours, search X for people evaluating [your category]. Catch three things: reviews or complaints about [category]; posts asking which [category] to use; and complaints about the problem [your product] solves. Quote the post, link it, name the account, and label it review, shopping, or complaint. Skip anything older than 24 hours, and skip [category] accounts promoting themselves. Post to [your Slack channel] only if there is at least one new hit you haven't already shared. Do not reply to or interact with anyone. Save this as a routine. If the search fails, report the failure in Slack.
```

例程 4：新联系人跟进
```text
Every weekday at 8:30am in my time zone, read my address book and list contacts added in the last 14 days. For each, show name, date added, phone, email, and any note. Ask me what we talked about before you write anything. Once I reply, draft a follow-up task for each person in [your task tool] with the context attached. Never text, email, or call anyone. Save this as a routine. If the address book is unavailable, say so and do not use old data.
```

例程 5：24 小时中美时差双语 X 运营与晚间复盘（参考 `@sisiliu517` 范式）
```text
You are my bilingual X operations manager running on a 24-hour US-China timezone cycle:
1. Daytime (09:00–21:00 UTC+8): Monitor Chinese AI & tech discussions on X. Draft 2 original Chinese posts and 5 high-value reply drafts to trending Chinese threads.
2. Nighttime (21:00–09:00 UTC+8): Switch to English X ecosystem. Monitor US tech leaders and AI builders, draft 2 English posts and 5 insightful English reply drafts.
3. Daily Review (Every night at 23:30 UTC+8): Pull metrics (impressions, likes, bookmarks, replies) of all posts and replies from the past 24 hours. Write a review report to /workspace/x-ops/reviews/YYYY-MM-DD.md, and update tomorrow's topic backlog and top 10 reply target @handles based on what performed best. Never publish posts or send replies without my explicit approval.
```

例程 6：Personal 𝕏 Assistant & Content Repurposer（参考 `@milesdeutscher` #10 & #5 范式）
```text
Every day at 08:00am, run a two-stage creator pipeline:
Stage 1 (Personal X Assistant): Analyze my top-performing X posts in /workspace/x-ops/winning-posts.md and today's trending AI news. Generate 3 high-converting hooks and complete X post drafts matching my personal voice.
Stage 2 (Content Repurposer): Identify the #1 outlier post (highest engagement-to-follower ratio) in my niche from the last 24 hours. Using my custom repurposing skills, rewrite its core insight into:
- 1 LinkedIn long-form post
- 1 Newsletter digest section
- 1 60-second short-form video script with visual cues
Save all outputs to /workspace/x-ops/repurposed/YYYY-MM-DD.md and send me the summary card.
```

#### Routine
官方规定每个 Bot 最多配 50 个 Routine，每个 Routine 保留最近 20 次运行记录，定时触发最小间隔仍为 5 分钟；自 v0.75.2（2026-10-22，https://x.ai/changelog/bot）起，官方将 Routine 的小时级运行频率限制大幅上调至**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots），单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**（https://cursor.com/help/grok-bot/routines）。在这套监控里，工作流挖掘、品牌提及和人脉跟进排在每个工作日早上的固定时间（8:30、9:00、9:15），潜在客户监听设为每 4 小时一次，而双语时差运营与 `@chat` 陌生人私信请求分拣则可按早晚班次定时触发。时间一到，Bot 会唤醒云电脑，调 X 搜索接口或 X Chat 解密工具抓最近 24 小时的帖子与私信，去重过滤后通过 Slack 连接器把 Markdown 简报推到频道里。要是没抓到匹配内容，发一行说明就停，不吵人。

#### 成本
官方未公布单独搜索 X 的计费标准，Grok Bot 内置的公开 X 数据读取完全免费包含在订阅内（若通过 X 插件访问私有账号数据则依据 https://cursor.com/help/grok-bot/connect-apps 说明可能需要 `https://console.x.com` 的 X API 额度），所有模型交互都扣套餐自带的周额度（https://cursor.com/help/grok-bot/plans）。自 2026 年 10 月 18 日官方推出 **The X Subscription 三合一统一订阅**（https://cursor.com/help/the-x-subscription/overview 与 https://x.com/bot/status/2110063783796572496）后，**Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 档位均包含 Grok Bot（Free $0 与 Plus $8/月不含），且 **Grok Bot、Grok 与 Cursor 三端共享同一个周额度池（one weekly usage pool）**，超额用量改为从 `grok.com/dashboard/billing` 充值的 **Prepaid Credits（预付额度）** 中扣除；既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）与 Teams（$40/人/月）老订户若不主动切换仍可保留原计划，但一旦在 `cursor.com/unify` 切换至 The X Subscription 即为单向不可逆。
社区有人算过一笔账，要是设成每 5 分钟跑一次 Routine，一个月触发 8,640 次，能把一个 33 美元的活烧成 397 美元（个例）（@fleyta88 https://x.com/fleyta88/status/2109346840382415019）。`@charlie_pmp`（https://x.com/charlie_pmp/status/2114214503416271131）也专门提醒：在三合一订阅三端共用周额度池的背景下，高频且未加精简的冗余 Routine 是后台静默吞噬额度的头号杀手。社区帖称在 Cursor Pro 订阅下，单条交互消息大约消耗 1% 周额度（个例）（@miniyarov https://x.com/miniyarov/status/2105428357273800799）。Rowan Cheung 把大部分监控设成每天跑一次，请求频次就压得很低。
成本实测状态：测定 4 个 Routine 在 Cursor Pro 或 The X Subscription Premium（$30/月）订阅下连续运行一周消耗的周用量百分比。

#### 坑
第一个坑是**禁止动作缺失**。提示词里要是没写死禁止私自发帖、回复和私信，Bot 可能会擅自去跟搜出来的推文互动，弄不好就封号甚至搞出公关事故。
第二个坑是后台审批超时。官方文档写明，后台或其他 Bot 触发的审批卡大约 10 分钟就会过期显示 Expired，动作就不执行了（https://cursor.com/docs/grok-bot/security）。第四个跟进例程起草任务前要等你回复，要是 10 分钟没理它，这一轮流程就中断了。
第三个坑是没搜到结果时的幻觉。要是没规定搜索落空怎么办，Bot 会为了交差拼凑旧消息甚至硬编推文。必须在提示词最后加一句，没结果就回一行单行说明。
第四个坑是例程空转。每天准时推的早报要是两周都没人看，额度就全打水漂了。社区经验指出，例程本身不是产出，能帮你做决定的例程才有价值，没产出的例程要及时删掉（https://x.com/kocer_eth/status/2101669438038634827）。

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 中配置完成的 X 监控例程界面与 Slack 接收到的摘要通知
![X 监控 Routine 从搜索抓取、条件过滤到 Slack 投递的单向数据流](../images/fig-15-2.png)

*图：X 监控 Routine 从搜索抓取、条件过滤到 Slack 投递的单向数据流*

### 15.2 公众号选题与日推 · WeChat Official Account Topics and Daily Pushes

#### 场景
做微信公众号有个现实问题：Grok Bot 没有任何国内平台的官方插件（https://xiangyugongzuoliu.com/grokbot-use-cases/）。后台的阅读量、完读率和用户画像全是非公开数据，公开网页抓不到，只能靠手动导数据或者提供材料。
觉醒AI 的 Adrian Punk 和 yvchengshanren 摸索出了一条自媒体流水线（https://www.jxxy.net/ai/articles/AdrianPunk115-2097311704547987756/ 与 https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/）。千万别指望建一个全能 Bot 搞定全部，那只是把找材料、写初稿和审校的堵点全堆在同一个窗口里。他们的做法是在云电脑 `/workspace/content-team/` 目录下按流程建文件夹，分出情报侦察员、选题策划师、内容主笔、事实编辑四个专职角色，靠文件传递交接。社区创作者夏哥研究室（`@CyberAlice3269`，2026-10-19，https://x.com/CyberAlice3269/status/2112098767151468645）与 0xbitman（`@bitman2140`，2026-10-25，https://x.com/bitman2140/status/2114210291546493153）也验证了类似的“1 个 CEO Bot + 5 个专职 Bot（情报搜集、选题策划、初稿撰写、审校润色、配图制作）”自媒体工作室与微信公众号日更流水线。
跑这条线要守住**三道硬门**：输入的源文必须来自人工指定的公开链接或一手文档，禁止 Bot 翻不可信的二手谣言；专业数据必须来自真实的测试报告，禁止 Bot 自行瞎编；最终的排版入库和发布按钮必须由人工手动点击，绝不下放给 Bot（https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/）。

在 `01-inbox/` 一手选题素材的高效、低成本采集上，两位中文社区创作者给出了极具启发性的高阶范式：
1. **“AI 写确定性爬虫，脚本跑日常轮询”零额度抓榜法（`@StarkLJM`）**：Mr.鼓先生（`@StarkLJM`，2026-10-18，https://x.com/starkljm/status/2111803996734419377 及 2026-10-21 跟进帖 https://x.com/starkljm/status/2112818533797343312）指出，面对每天需要固定抓取的热门榜单或选题源，**绝不能让大模型每天开浏览器消耗 Token 去读网页**。他的做法是：先用 Cursor CLI 仅耗时 **28.6 秒**编写出一套确定性的 Python 爬虫脚本；此后每天定时运行该脚本，仅需 **1.99 秒**即可抓取完 30 条榜单数据，**日常运行消耗 0 模型额度（zero model tokens）**。为了防止脏数据污染选题判断，脚本内置了严格的防御性编程规则——一旦遇到上游字段缺失立即触发告警，且当源数据缺少评分时严格存入 `null`，绝不用 `0` 填充以免拉低均值计算。
2. **1Password 授权突破彭博社等海外付费墙抓深度研报（`@oxpsats`）**：公众号想要写出差异化深度长文，往往依赖海外一手付费信源。偶像派作手（`@oxpsats`，2026-10-25，https://x.com/oxpsats/status/2114207006064365670）将自己的彭博社（Bloomberg）付费会员账号存入 1Password 并授权给 Grok Bot（配合 v0.75.2 上线的 1Password Brokered Sign-in 逐次授权登录或共享库，详见 https://cursor.com/help/grok-bot/connect-apps），让 Bot 能够全自动登录突破付费墙（paywall），定时抓取海外核心财经深度报道并沉淀进选题收件箱。

#### 提示词
```text
你负责微信公众号的日常选题策划与推文初稿。工作路径严格基于 /workspace/content-team/ 共享目录。

【输入与依据】
1. 仅读取 01-inbox/ 中已核验的一手事实卡，以及 00-profile/voice.md 中定义的账号调性与读者画像。
2. 严禁自行联网搜索未经验证的二手谣言，严禁捏造行业数据、用户案例或未公布的技术指标。

【执行步骤】
第一步：从线索中筛选出 3 个选题 Brief，写入 02-briefs/YYYY-MM-DD.md。每个选题包含：一句话核心事实、读者业务痛点、切入角度、一手证据链接以及给主笔的写作要求。生成后停下等待人工批准。
第二步：收到人工明确批准后，将选定 Brief 扩展为一篇公众号推文初稿，写入 03-drafts/YYYY-MM-DD-title.md。

【写作规范】
1. 结构采用问题引入、技术原理拆解、实操步骤、踩坑提示四段式，语言平实口语化。
2. 严禁使用“在当今”、“革命性”、“赋能”、“颠覆”、“毫无疑问”等空洞套话。
3. 文中每处核心论点必须紧跟事实依据；未亲测内容显式标注为“待实测”。
4. 文末附带需要人工确认的事项清单与配图建议。完成后仅汇报文件路径。
```

附：`@StarkLJM` 零模型额度确定性抓榜脚本生成与防御性校验示例（保存在 `/workspace/content-team/scripts/fetch_rank.py`）：
```python
#!/usr/bin/env python3
"""
确定性选题榜单抓取脚本（日常运行 0 Token 消耗，~1.99s 完成 30 条记录采集）
防御性原则：核心字段缺失立即抛错告警；缺失评分严格记为 None (JSON null)，严禁用 0 污染均值。
"""
import json
import time
import urllib.request
from pathlib import Path

REQUIRED_KEYS = {"id", "title", "url"}

def fetch_top30_topics(api_url: str, out_path: Path) -> None:
    t0 = time.perf_counter()
    req = urllib.request.Request(api_url, headers={"User-Agent": "GrokBot-TopicFetcher/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        payload = json.loads(resp.read().decode("utf-8"))

    items = payload.get("items", [])[:30]
    if not items:
        raise RuntimeError("ALERT: 上游榜单返回为空，请检查接口或反爬状态！")

    cleaned = []
    for idx, raw in enumerate(items, 1):
        missing = REQUIRED_KEYS - raw.keys()
        if missing:
            raise KeyError(f"ALERT: 第 {idx} 条记录缺失关键字段 {missing}，已中止入库！")
        # 严格区分无评分与 0 分：缺失评分存 None (null)，绝不填 0
        raw_score = raw.get("score")
        score = float(raw_score) if raw_score is not None else None
        cleaned.append({
            "rank": idx,
            "id": str(raw["id"]),
            "title": str(raw["title"]).strip(),
            "url": str(raw["url"]),
            "score": score,
        })

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({"fetched_at": time.strftime("%Y-%m-%d %H:%M:%S"), "count": len(cleaned), "items": cleaned}, ensure_ascii=False, indent=2), encoding="utf-8")
    elapsed = time.perf_counter() - t0
    print(f"OK: 抓取 {len(cleaned)} 条榜单记录，耗时 {elapsed:.2f}s，模型 Token 消耗: 0")
```

#### Routine
这个流程可以配成工作日早上的例程。先由系统 `cron` 在每天 08:25 零 Token 运行一次 `fetch_rank.py`，将 30 条结构化榜单写入 `01-inbox/`；随后设成每个工作日早晨 08:30 执行 Grok Bot Routine（在 v0.75.2 全账号 300 次/小时、单 Routine 200 次/小时的配额下绰绰有余，详见 https://cursor.com/help/grok-bot/routines），Bot 先看 `/workspace/content-team/01-inbox/` 目录下有没有前一天沉淀的事实卡、彭博社付费墙摘录与早间榜单。只要有材料，就自动提炼出当天的 3 个选题 Brief 存入 `02-briefs/` 目录。
人工在对话中选定并回复批准后，触发主笔 Bot 生成完整初稿。因为国内平台没有官方接口，Bot 把初稿写入 `03-drafts/` 后就会停下，通过微信下发渠道或系统提示通知。我们把 Markdown 复制到排版工具或公众号后台，自己人工点击发布。

#### 成本
所有 Bot 运行都消耗账户的统一周额度（https://cursor.com/help/grok-bot/plans）。在 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，https://cursor.com/help/the-x-subscription/overview）下，Grok Bot 与 Grok、Cursor 共享每周重置的周额度池，超出后扣减 Prepaid Credits（老订户仍可維持独立 Cursor Pro $20 / Pro+ $60 / Ultra $200 / Teams $40 计划，但经 `cursor.com/unify` 切换后不可逆）。Grok Bot 没有模型选单，也不显示每次请求的底层模型，所以别指望靠在界面里切便宜模型省额度（https://cursor.com/help/grok-bot/models，转引自 carlstack 额度文章）。不过，采用 `@StarkLJM` 的“确定性 Python 爬虫跑日常采集 + 仅在提炼 Brief 与写稿时唤醒 Bot”的架构，可将日常数据采集环节的周额度消耗直接降为 **0**。社区帖称 Pro 档每条消息约耗 1% 周额度（个例）（https://x.com/miniyarov/status/2105428357273800799）。一次完整四岗交接的额度消耗。
成本实测状态：测定公众号从线索汇总到成稿审校全流程单次消耗的周用量百分比。

#### 坑
第一个坑是模拟登录招来风控。象鱼工作流指出国内平台没有原生插件，如果在云电脑里用高频脚本刷新网页或模拟点击，容易触发平台的安全拦截甚至封号（https://xiangyugongzuoliu.com/grokbot-use-cases/）。切忌让 Bot 自动去公众号后台点发布，把发布权留在人类客户端。
第二个坑是主笔瞎编技术数据。主笔 Bot 写长文容易顺手编造出“性能提升 300%”或“某大厂全员采用”这类假数据。必须在角色描述和提示词里加上禁止项，要求所有数字必须追溯至真实材料，没有出处的数字一律不得写入（https://www.jxxy.net/ai/articles/AdrianPunk115-2097311704547987756/）。
第三个坑是共享云电脑带来的凭据泄漏风险。官方文档指出同一账号下的所有 Bot 共享同一台 Linux 云电脑、同一个浏览器登录态和同一个 `/workspace`（https://cursor.com/docs/grok-bot/work）。前一个 Bot 保存了私有凭据，其他 Bot 都能直接读取，切勿在云电脑环境中以明文存放主账号密码或私密会话凭据——对于彭博社等付费资讯站点的登录，强烈建议使用 v0.75.2 上线的 **1Password Brokered Sign-in**（https://x.com/bot/status/2113301060811161874）或 v0.75.5 上线的 **Grok Bot Vault**（https://cursor.com/help/grok-bot/secrets），让密码通过底层加密注入，使 Bot 上下文彻底接触不到明文密码。
第四个坑是口头纠错未落盘。觉醒AI 指出，你在对话里纠正 Bot 的错误时，Bot 经常回答“记下了”，但只要没把规则写入 `voice.md` 或技能规则文件，下一次新建会话它照样犯同样的错误（https://www.jxxy.net/ai/articles/grok-bot-workflow-training/）。

> [!NOTE]
> 📸 **截图位（待补）**：/workspace/content-team/ 目录下生成的选题 Brief 与主笔初稿文件
![公众号内容流水线分工：情报、选题、主笔、编辑与人工发布守门](../images/fig-15-3.png)

*图：公众号内容流水线分工：情报、选题、主笔、编辑与人工发布守门*

### 15.3 写代码渲染视频（ffmpeg） · Code-Rendered Video

#### 场景
在早期版本中，传统短视频制作要么靠剪辑软件拼素材，要么靠外部文生视频模型抽卡；而从 **v0.71.2（2026-10-14，https://x.ai/changelog/bot）** 开始，Grok Bot 迎来了视频创作能力的史诗级跃升——**不仅支持 FFmpeg 脚本压制，现已全面形成“Grok Imagine 原生生图/生视频（`GenerateImage` / `GenerateVideo`）+ Remotion / Blender / Canvas / FFmpeg 代码动效渲染”双剑合璧的完整视觉工作站！**

文生视频虽然画面逼真，但在数据图表、知识科普、产品演示和精确文字动效上根本对不齐节奏，改动一个字整段画面就会完全变形。因此，将 Grok Imagine 的生成式画面与纯代码驱动的确定性动效结合，成了最强大的解法。
早先 Leo Xiaolei 和 0xCarnagee 摸索出了一条纯代码渲染的视频管线（https://x.com/leo_xiaolei/status/2108159484401262882 与 https://x.com/0xCarnagee/status/2108501747643670780）：让 Grok Bot 编写基于 HTML Canvas 或 SVG 的前端动效页面，通过无头浏览器 Playwright 驱动 Chromium 逐帧截图，最后调用 ffmpeg 将连续图片与音频压制为竖屏 MP4 视频。
这套管线有两个核心支柱。第一是**放弃系统时钟**，页面暴露 `window.seek(t)` 纯时间函数，输入任意时间戳 t 永远渲染出完全一致的静态画面，粒子等随机特效采用 Mulberry32 算法锁定随机种子；第二是使用 edge-tts 生成配音并显式传入 `boundary='WordBoundary'` 导出词级时间戳，让口播念出的每一个字充当画面动效的时钟基准。

在此基础上，2026 年 10 月中下旬涌现出**四大极具代表性的官方与社区视频创作标杆案例**，彻底拓宽了 Grok Bot 视频工业化的边界：

1. **标杆案例一：`@bot` 官方原生生视频（Grok Imagine）与 Remotion 代码动效双官宣**
   - 2026 年 10 月 15 日，`@bot` 官方发布主帖 *"Your Grok Bot can now make videos"*（20,762 赞 / 1,923 转发 / 4,769 书签，https://x.com/bot/status/2110566041772617908），正式宣告 Bot 可直接调用内置的 `GenerateImage` 与 `GenerateVideo` 工具在聊天流中生成和编辑实拍感视频片段；紧接着同日发布续帖 *"And motion graphics with code"*（2,616 赞 / 211 转发 / 725 书签，https://x.com/bot/status/2110772748805194127），展示了在云电脑中用 Remotion / 代码直接渲染丝滑 UI 动效与动态信息图的官方范式。

2. **标杆案例二：`@StarkLJM` 通过 BDK 从本地 Claude Code 跨端派单渲染 20 秒《上下五千年》中国史动画（含 2.7 MB 源码包）**
   - Mr.鼓先生（`@StarkLJM`，2026-10-12，https://x.com/starkljm/status/2109544938644107411）实战演示了如何利用 **BDK（Bot Developer Kit / `cursor-grokbot-agents`）** 将本地终端里的 Claude Code / Codex 与云端 Grok Bot 打通。他在本地 Claude Code 中向云端 Grok Bot 下达了“制作一段 20 秒《上下五千年》中国历史线条画动画短片”的指令；云端 Grok Bot 在沙箱中独立完成朝代分镜绘制、时间轴动效编排与音画合成，直接向本地返回了渲染完毕的 `0:20` MP4 视频卡片以及 `2.7 MB` 的完整可复用源码压缩包。

3. **标杆案例三：`@pengzheng_` 检索 1908 年专利图纸并用 Python 驱动 Blender 渲染 3D 折痕铰链无缝循环动画**
   - Grok Bot 设计师 Peng Zheng（`@pengzheng_`，2026-10-24，204 赞 / 148 书签，https://x.com/pengzheng_/status/2113786630033322239 及补充帖 https://x.com/pengzheng_/status/2113804819274277015）分享了一个惊艳的 3D 工业级案例：为了弄清楚代表云电脑沙箱的经典中餐外卖折盒（`to-go` box 🥡）究竟是如何折叠的，他让 `@bot` 自主考证。Bot 先在全网检索并挖出了 **1908 年的原始专利图纸**，随后直接在云电脑里编写 Python 脚本驱动 **Blender** 建模——将纸盒的每一个折页严格沿着 1908 年专利图纸上的折痕线（crease lines）绑定为物理骨骼铰链（hinge），渲染出与 🥡 Emoji 角度严丝合缝的开合无缝循环 3D 动画，直接用作网页的 `og:video`。

4. **标杆案例四：`@LisaMAUSA` 的 SceneEdit Video Studio 单镜头局部修补工作流（免全片重渲）**
   - 针对代码渲染长视频“改一个镜头就要重跑几十分钟全片”的痛点，社区开发者 `@LisaMAUSA`（2026-10-25，https://x.com/LisaMAUSA/status/2114208018388643852）在响应 `@leerob` 的反馈悬赏帖（https://x.com/leerob/status/2113792409448714468）时开源了 **SceneEdit Video Studio** 模板：将整条视频按镜头（Scene）切分为独立时间段与缓存切片，当需要修改某几秒的画面或台词时，仅针对该单镜头调用 `GenerateVideo` 或重跑局部帧渲染，再通过 FFmpeg `concat` 无损流拷贝拼接回母带，彻底告别全片重渲。

#### 提示词
```text
你负责将指定的口播文案制作成竖屏（1080×1920、30fps）代码渲染动效视频。

【技术规范】
1. 动效页面 index.html 必须暴露 window.seek(t) 函数，仅依赖参数 t 计算元素属性与位置，严禁使用 setTimeout、setInterval 或 requestAnimationFrame。
2. 随机动效必须使用固定的 Mulberry32 随机种子，严禁使用 Math.random()。
3. 页面内所有文字必须使用代码绘制，严禁使用图像模型生成文字。
4. 标题与图表不得低于 y=1388，字幕带限制在 y=1400 至 y=1520，y=1520 以下保留底色以避开平台交互按钮。

【执行流程】
第一步：调用 edge-tts 生成配音并导出按词切分的时间戳文件 timing.json。
第二步：编写 HTML/Canvas 页面并生成关键静帧（stills at 0, 0.3, 0.6），停下等待人工审查。
第三步：人工确认静帧通过后，运行 render.py 截取全量帧，并运行 mix.sh 进行音频侧链闪避与响度归一化（母带达到 -14 LUFS，真峰值不超过 -1.5 dBTP）。
第四步：使用 ffmpeg 生成 4×2 时间码联系表 contact.png 并汇报。
口播文案：[在此填入口播文本]
```

附：结合 v0.71.2 `GenerateVideo` + Blender 3D + SceneEdit 局部热替换的进阶提示词模板：
```text
你负责在 /workspace/video-studio/ 下构建一条“Grok Imagine + 代码动效 + SceneEdit 单镜头修补”混合视频管线：
1. 素材分层：空镜与写实过场调用内置 GenerateImage / GenerateVideo（Grok Imagine）生成；数据图表、历史时间线与精确文字动效使用 Remotion / HTML Canvas 或 Blender Python（bpy）无头渲染。
2. 镜头模块化（SceneEdit 规范）：按镜头切片保存为 scenes/scene_01.mp4 ... scene_N.mp4，并维护 manifest.json 记录每个镜头的起止时间码、渲染脚本与哈希值。
3. 局部热替换：当收到“仅修改第 K 个镜头”的指令时，严禁重渲其他未改动镜头！仅重新生成 scene_K.mp4，校验分辨率（1080×1920）、帧率（30fps）与像素格式（yuv420p）一致后，使用 ffmpeg -f concat -safe 0 -i scenes.txt -c copy 快速合成最终成片，并打包源码与 MP4 交付。
```

#### Routine
为了避免白天交互时长时间占用云电脑资源，可以将渲染包装为夜间渲染队列例程。
在 `/workspace/studio/` 目录下编写 `render-queue.sh`，利用 Linux `flock` 文件锁确保同一时间只有一个渲染任务运行。在设置中配置 Routine（支持 v0.75.2 最新频率上限：全账号合计 300 次/小时、单条 Routine 最高 200 次/小时，详见 https://cursor.com/help/grok-bot/routines）：每天晚上 23:00 自动检查 `/workspace/studio/projects/` 目录下带有 `APPROVED` 与 `READY` 标记的项目。
若存在待渲染工程，Routine 启动 Playwright、Remotion、Blender 或 ffmpeg 批量压制成片，自动生成 `contact.png` 联系表并打上 `PASSED` 标记。次日早晨 08:00 交付 Bot 将最终成片与联系表推送过来，即便合上笔记本也能在夜间全自动完成压制。

#### 成本
官方帮助页没有列出云电脑计算时长的单独收费项，按现有说明，Bot 的工作（包含调用 `GenerateImage` / `GenerateVideo` 以及云电脑渲染交互）都计入 **The X Subscription**（Premium $30/月、Super $100/月、Ultra $200/月，三端共享周额度池 + Prepaid Credits 预付额度，https://cursor.com/help/the-x-subscription/overview）或旧版独立 Cursor 套餐自带的周额度（https://cursor.com/help/grok-bot/plans）。在速度与资源消耗方面，社区实测表明在 Grok Bot 云电脑上运行 4 秒示例视频（120 帧），全流程从生成到压制约耗时 10 到 14 秒（作者自述，https://chunduai.com/tutorials/grok-bot-code-video；代码 https://gist.github.com/threerocks/5f6f6d5b3801a400bb5343379082580c）；在 2 核无 GPU 的 Linux 机器上，15 秒动效的草稿渲染约 48 秒，带运动模糊的 60fps 终版约 6 分钟（https://chunduai.com/tutorials/grok-bot-motion-studio，整理自 https://x.com/0xCarnagee/status/2108501747643670780）；而 `@StarkLJM` 通过 BDK 跨端派单渲染 20 秒《上下五千年》中国史线条画动画并打包 2.7 MB 源码（https://x.com/starkljm/status/2109544938644107411）同样在单次任务交互中顺畅完成。
成本实测状态：测定 60 秒 30fps 动效短视频在云电脑上完整渲染单次消耗的周用量百分比。

#### 坑
第一个坑是未核对静帧直接渲染整片。1 分钟 30fps 的视频需要截取 1800 张高清图片，在无显卡的云电脑上单次渲染可能耗费二十多分钟（https://chunduai.com/tutorials/grok-bot-code-video）。如果代码中存在排版错位，整段渲染全部报废。必须在提示词里强制执行硬门禁：静帧未获人工确认，严禁启动全片渲染；若成片后只需微调单镜头，务必采用 `@LisaMAUSA` 的 SceneEdit 局部重渲拼接法（https://x.com/LisaMAUSA/status/2114208018388643852），避免全片推倒重来。
第二个坑是中文字体缺失导致乱码。官方说明云电脑做"电脑更新"、Recover 或 Reset 后会移除手动安装的应用和软件包（普通软件更新会保留）（https://cursor.com/help/grok-bot/computer-recovery）。如果系统中缺少思源黑体或 Noto Sans CJK，Canvas 或 Blender 渲染出的中文字符会全部退化为空白方块。必须将中文字体安装命令写入环境初始化脚本 `bootstrap.sh` 中，并在渲染前通过 `fc-list :lang=zh` 进行校验（https://chunduai.com/tutorials/grok-bot-code-video）。
第三个坑是模型“看不了视频”的审片盲区。当前大模型只能接受静态图片输入，无法直接回放 MP4 视频。如果直接问 Bot 成片质量，它只能根据文字描述凭空推断。必须通过 ffmpeg 提取每 0.5 秒一帧拼成带时间码的联系表（Contact Sheet），新开一个没有制作上下文的独立审片 Bot 会话进行挑错；同时配音语气与卡点模型完全无法试听，必须戴上耳机亲自听一遍。
第四个坑是音频起振杂音与字幕字号偏差。代码生成的占位音效若未添加 2 到 12 毫秒的淡入淡出，拼接处会产生轻微爆音；而在使用 ASS 格式烧录字幕时，思源黑体的字号不是屏幕像素，实际高度等于 FontSize 除以 1.448，必须通过一帧静帧量测矫正（同上）。

> [!NOTE]
> 📸 **截图位（待补）**：云电脑终端运行 render.py 逐帧截图与生成的审片联系表 contact.png
![代码渲染视频流水线：口播时间戳驱动 Canvas 动效、Playwright 逐帧截图与 ffmpeg 压制](../images/fig-15-4.png)

*图：代码渲染视频流水线：口播时间戳驱动 Canvas 动效、Playwright 逐帧截图与 ffmpeg 压制*

### 15.4 配图 skill 与小红书图卡 · Illustration Skills and Xiaohongshu Graphic Cards

#### 场景
视觉卡片是小红书等社交平台的第一入口。很多创作者直接用生图模型生成图文卡片，但图像模型做不到多张卡片风格一致，画面上生成的文字也基本全错。觉醒AI 在实战中甚至彻底关闭了纯 AI 配图，因为低质假图极易被平台识别判定为低质内容（https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/）。
Miles Ma 提出的知识图卡流程给出了切实可行的方案（https://immilesma.com/blog/grok-bot-practical-guide/ 原文 https://x.com/miles_mazy/status/2098708209095819605）：让 Grok Bot 担任小红书编辑，围绕特定主题制作一套符合 3:4 竖屏比例（1080×1440）的六联张图卡，涵盖封面、框选截图、整屏保存、当前窗口、剪贴板历史与快捷键对照表。
这套方案的关键是将视觉资产拆分为**代码排版层**与素材层：Bot 负责查阅官方资料，编写规范的 SVG 矢量排版代码与配套文案，同时在云电脑上直接输出无损 PNG 成图，并生成一个 HTML 画廊供创作者直观验收（自 v0.75.2 上线 **Pages / Canvas** 功能后，还可以直接让 Bot 生成一个可在线预览、支持三级权限分享的交互式图卡看板 Page，详见 https://x.com/bot/status/2112991843235610885）。

#### 提示词
```text
你负责为小红书制作面向电脑新手的成套知识图文卡片。

【任务要求】
1. 主题为“Windows 截图后，图片去哪了”，严格查阅微软官方文档获取技术依据。
2. 制作 6 张 1080×1440（3:4 竖屏）的图卡，结构分别为：封面、框选截图、整屏保存、当前窗口、剪贴板历史、快捷键对照表。
3. 配色采用统一规范：米白底色、深蓝主体与亮黄点缀。文字排版清晰，关键操作附带直观示意图。
4. 交付物要求：直接交付 PNG 成图文件、SVG 矢量源文件以及小红书配套发布正文，并在 /workspace 目录下生成一个可全屏预览整套图片的 HTML 画廊。
5. 缺少或待确认的技术细节显式标注，严禁凭空编造快捷键。
```

#### Routine
小红书图卡制作适合配置为周期性的选题生产例程。设定每周日晚上 20:00 自动触发，Bot 读取 `/workspace/content-team/02-briefs/` 目录中积攒的通过审核的知识点。
Routine 批量调用 SVG 模板引擎生成当周的图卡包，在对应文件夹下生成带时间戳的图片与 Markdown 文案，并将生成的 HTML 画廊本地链接汇报在对话中。次日早晨创作者直接在浏览器中打开画廊，挑选质量过关的图包下载到手机相册中。

#### 成本
生成 SVG 矢量代码和借助云电脑渲染 PNG 图卡属于轻量级纯文本与无头浏览器操作，不涉及第三方生图 API 扣费，完全受控于 The X Subscription（Premium $30/月、Super $100/月、Ultra $200/月，https://cursor.com/help/the-x-subscription/overview）或旧版独立 Cursor 套餐自带的周用量（https://cursor.com/help/grok-bot/plans）。社区创作者实测表明，制作一套 6 张高清图卡仅需数次轮次的上下文交互，额度消耗极低（https://immilesma.com/blog/grok-bot-practical-guide/）。
成本实测状态：测定 6 张 1080×1440 知识图卡从 SVG 生成到 PNG 导出全流程消耗的周额度。

#### 坑
第一个坑是画幅比例错误。小红书移动端的标准展示比例是 3:4（即 1080×1440 像素），许多新手让 Bot 产出图片时未限定分辨率，默认生成 16:9 或 1:1，导致发布后关键内容被平台截断。必须在提示词中将 1080×1440 像素作为硬指标写死。
第二个坑是让图像模型直接画文字。大模型生成图像时的字符渲染机制不同于字体排版，画面中的文字必定变成错别字或不可读字符。解决办法是让图像模型（包括 v0.71.2 内置的 `GenerateImage`）仅负责无字纯背景或局部插图，所有文字和排版一律由 SVG 或 HTML Canvas 代码通过绝对坐标叠加（https://chunduai.com/tutorials/grok-bot-code-video）。
第三个坑是伪造透明背景的假 PNG 与假截图。觉醒AI 踩过的典型坑是 Bot 直接输出了一张带棋盘格背景的所谓透明图，拼合后画面粗糙不堪（https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/）。对于软件教程类配图，必须由创作者提供真实截图或由 Bot 在云电脑浏览器中截取真实页面，坚决不用 AI 臆造的虚拟软件界面。
第四个坑是严禁脚本自动发帖。由于国内平台具备严格的设备指纹与风控检测，任何利用云电脑脚本在网页端模拟发布笔记的行为都会招致账号降权甚至限流。必须将最终的图片与文案导出至本地，在官方手机客户端进行人工复核与发布（https://xiangyugongzuoliu.com/grokbot-use-cases/）。

> [!NOTE]
> 📸 **截图位（待补）**：生成的 6 张 1080×1440 小红书知识图卡预览画廊与 SVG 源文件
![小红书知识图卡的分层架构：底层代码绘制、中层文字排版与顶层人工审核发布](../images/fig-15-5.png)

*图：小红书知识图卡的分层架构：底层代码绘制、中层文字排版与顶层人工审核发布*


# §16 赚钱与工作 · Work & Business

> **适合谁**：想用 Bot 辅助副业、跨境电商或团队业务的读者。16.3 的官方岗位指南面向用 Slack、CRM、ATS 的海外团队；国内小团队可以只借鉴"Bot 起草、人工发送"的分工方式。

很多人以为给 AI 一台电脑，就能全自动赚钱。真敢这么放手，账户额度一天就会烧光，搞不好还会被封号。我调研了一圈发现，Grok Bot 根本不是什么自动吐钞机，它就是一个不知疲倦的数字劳动力。能赚钱的工作流，从来不是让它从头到尾接管商业闭环，而是把它卡在整个链路里最枯燥、最耗时、确定性最高的环节。

![商业与工作流中的 Grok Bot 定位：充当高频数据过滤器与草稿发生器，决策与资金闸门由人把控](../images/fig-16-1.png)

*图：商业与工作流中的 Grok Bot 定位：充当高频数据过滤器与草稿发生器，决策与资金闸门由人把控*

## 16.1 出海找新词建站 · Micro-SaaS Keyword Radar

做出海小工具站，以前每天要花两三个小时在各种论坛里肉眼翻帖子，人工找别人的抱怨。雇人干成本太高，自己干又心累。社区帖称有人用 Grok Bot 做新词监控，再自己买域名、用 Claude 建站、接 Stripe 收款，当晚拿到出海站首单。注意，原帖里 Grok Bot 只负责找词这一环（个例，https://x.com/0xEcho99/status/2108927962305511520）。整个链路里，**Bot 负责雷达探测，人负责临门一脚**。

随着云电脑执行力与多智能体工作流的成熟，海外商业社区已经将这套“找词建站”模式进一步延展为端到端的获客与内部工具造物闭环。X 知名创作者 Miles Deutscher（`@milesdeutscher`）在其获得 3,100 赞、360 转发、4,503 书签的万字长推 [10 Insane Grok Bot Use Cases](https://x.com/milesdeutscher/status/2113653680834859262) 中，专门拆解了两套与 Micro-SaaS 紧密咬合的进阶方案：其一是 **#8 Lead List Builder（潜在客户挖掘机，即昂贵 Apollo 订阅的平替方案）**（[https://x.com/milesdeutscher/status/2113653741647999378](https://x.com/milesdeutscher/status/2113653741647999378)，49 赞），通过你定义的理想客户画像（ICP），自动在全网抓取、清洗并补全高意向潜在客户名单与联系方式；其二是 **#2 Build-Anything Agent（云电脑全栈 Vibe-Coding 造物主）**（[https://x.com/milesdeutscher/status/2113653833645818000](https://x.com/milesdeutscher/status/2113653833645818000)，51 赞），直接在 Bot 的云电脑上从零编写、部署并托管内部业务小工具、ROI 计算器与 Web 应用，把探测到的痛点词当场转化为可交互原型。

> [!NOTE]
> 📸 **截图位（待补）**：新词监控 Bot 生成的海外高频痛点词与建站场景候选清单

### 场景

海外 Micro-SaaS 或出海内容站的核心竞争力在于抓早期的长尾需求。当一个新问题在海外社交平台反复被提及，而现成的搜索结果里还没有成熟工具时，做一个单功能网页往往就能接住精准搜索流量。这个任务要求 Bot 充当趋势侦察兵，每天定期扫描公开讨论中的高频抱怨与求助关键词，过滤掉闲聊和营销水帖，提取出具备建站可能性的功能词。一旦锁定垂直赛道，还可以无缝衔接 `@milesdeutscher` 的 **#8 Lead List Builder** 与 **#2 Build-Anything Agent**，一边在云电脑内写出 MVP 原型工具，一边自动搜集首批种子用户的外联名单。

### 提示词

```text
你是一名专注海外 Micro-SaaS 机会的新词雷达分析师。你的工作环境是一台配备浏览器的云电脑。

请执行以下任务：
1. 检索当前公开网络与社交平台上关于“how to automate”、“tool for”、“alternative to”以及近期热门软件痛点的讨论。
2. 过滤掉大厂已成熟解决的标准功能需求，寻找用户正在抱怨“现存工具太贵”、“流程太繁琐”或“没有轻量工具”的长尾场景。
3. 整理出 5 个高潜力关键词，每个词按照固定结构输出：
   - 原始长尾词（英文原生表述）
   - 用户核心痛点（引用 1-2 条代表性质询场景）
   - 商业化形态设想（单页计算器、轻量生成器或自动化脚本）
   - 竞争度初步判断（目前搜索结果是论坛讨论还是已有竞品页面）
4. 将结果以 Markdown 格式保存为 /workspace/keywords/daily_radar_latest.md，严禁编造搜索数据，不确定的数据标注未核实。
```

在此基础上，假设你想复刻 `@milesdeutscher` 的 **#8 Lead List Builder（Apollo 平替潜客挖掘机）**（[https://x.com/milesdeutscher/status/2113653741647999378](https://x.com/milesdeutscher/status/2113653741647999378)）与 **#2 Build-Anything Agent（内部小工具全栈构建）**（[https://x.com/milesdeutscher/status/2113653833645818000](https://x.com/milesdeutscher/status/2113653833645818000)），可以直接在云电脑中追加以下组合提示词模板：

```text
# 阶段一：#8 Lead List Builder（ICP 潜客名单抓取与清洗）
你是一名 B2B 增长黑客与数据清洗专家。请根据以下理想客户画像（ICP）构建潜在客户名单：
- 目标行业：[例如：独立 Shopify 护肤品卖家 / 10-50 人规模的海外营销代理商]
- 关键信号：近期在 X、LinkedIn 或公开论坛抱怨过 [痛点关键词]，或正在招聘相关岗位。

执行步骤：
1. 在公开社交网络、黄页目录与公司官网抓取符合 ICP 的 30 家目标企业或主理人。
2. 清洗并补全字段：公司名称、官网 URL、决策人姓名与职位、公开 X 账号或商务邮箱、触发痛点的原始动态链接、个性化破冰切入点（1 句话）。
3. 剔除无效死链与无明确联系方式的条目，导出为 /workspace/leads/icp_leads_cleaned.csv。

# 阶段二：#2 Build-Anything Agent（云电脑直接构建内部工具与获客磁铁）
请基于上述排名第 1 的痛点词，直接在云电脑的 /workspace/tools/ 目录下使用 TypeScript + Tailwind CSS 构建一个单页交互式诊断/计算器 Web 小工具，在沙箱本地启动服务完成自测截图，并生成可一键部署的静态构建产物。
```

### Routine

建立一条命名为 Daily-Niche-Keyword-Scan 的 Routine。触发周期设为每 24 小时执行一次，执行时间推荐在海外活跃时段结束后的清晨。官方文档规定 Routine 的最短定时执行间隔不少于 5 分钟，且自 v0.75.2 起，官方将 Routine 运行频率上限大幅上调至**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots）、单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）。设置中必须关闭自动发帖或向外部分享的权限，仅让它在工作区生成文件，并在完成时通过系统通知提示查看报告。

### 成本

基础使用基于 Cursor Pro 套餐，官方每月标价为 20 美元（https://cursor.com/pricing）。官方未公布具体的每周额度数字（https://cursor.com/help/grok-bot/plans）。自 2026 年 10 月 18 日起，官方正式推出 **The X Subscription 三合一统一订阅**（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)、[https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)），以单一订阅整合 Grok、Cursor 与 X Premium：其中包含 Grok Bot 权限的档位为 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）**（Free $0 与 Plus $8/月不包含 Grok Bot），三端共享同一个每周固定重置的周额度池（one weekly usage pool），周额度耗尽后或调用第三方模型时从 `grok.com/dashboard/billing` 充值的 **Prepaid Credits（预付额度）** 中扣除。既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及自助式 Teams（$40/人/月）老订户只要不主动切换，仍可保留原档位与后付费按需限额（On-demand monthly limit），但一旦在 `cursor.com/unify` 主动升级切换至 The X Subscription，该操作单向不可逆（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。社区帖称每条交互消息大约消耗 1% 的周额度（个例，https://x.com/miniyarov/status/2105428357273800799）。每日运行一次检索 Routine，每周大约消耗 7 次自动化运行轮次，在个人 Pro 配额或 $30/月的 The X Subscription Premium 共享周额度池内能够平稳运转，不会触发 On-demand 或 Prepaid Credits 额外扣费。如果你需要每天高频抓取榜单数据，还可以借鉴 `@StarkLJM`（Mr.鼓先生）实测验证的“AI 写确定性脚本，脚本跑日常轮询”范式（[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377)）：让 CLI 耗时 28.6 秒生成确定性 Python 爬虫脚本（内置缺失字段告警与 `null` 值保护），此后每天定时运行仅需 1.99 秒，日常运行消耗 0 模型额度。

### 坑

第一个坑是让 Bot 自动去买域名和配置服务器。由于涉及真实的支付凭证和外部敏感账户，绝对不要把支付密码明文存在 Bot 聊天环境里，稍有误判就会造成资金损失。即使官方在 v0.75.5 上线了内置加密保险箱 `Settings → Vault`（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)），也必须注意官方帮助文档明确标注的红线：保存在 Vault 中的银行卡在结账填充时，**不会触发单独的逐笔 Vault 弹窗确认**（`@kial` [https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280) 与 `@JianWeiSignal` [https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488) 均对此发出过专门预警），因此切勿将主力信用卡常驻保存在自动建站 Bot 的 Vault 中。第二个坑是遇到热门公关事件或刷量营销时，Bot 容易把水军刷屏的话题误判为真实痛点，导致找出的词全无商业价值。

测试设置不同长尾检索词库时云电脑浏览器抓取结果的去重率与误报率。

## 16.2 跨境电商竞品巡检 · Cross-Border E-Commerce Inspection

做跨境电商最怕竞品半夜调价或者上新爆款，隔两三天才能发现。传统做法是人工每天把竞品店铺一个个打开看一遍，极其耗人。官方在 10 月 9 日为 @bot 增加了 Shopify 原生集成，支持查订单、跟库存和更新商品信息（https://x.com/bot/status/2108228871938359347）。结合云电脑的公开网页读取能力，Bot 可以成为一名不知疲倦的商品巡检员。核心原则是**把竞品巡检当报警器，而不是自动下单机**。

除了电商独立站的商品巡检，这套打法在 SaaS 与消费品领域同样演化成了全天候情报雷达。`@milesdeutscher` 在其十大用例长推中分享的 **#9 Competitor Monitor（竞品发布与价格监控 Routine）**（[https://x.com/milesdeutscher/status/2113653726217195817](https://x.com/milesdeutscher/status/2113653726217195817)，52 赞），正是通过定时 Routine 持续盯守竞争对手的新品发布、定价页（Pricing Page）档位微调、功能更新日志（Changelog）与社媒营销动作，一旦检测到异动立即生成结构化对比简报推送给团队。与此同时，针对跨境卖家与品牌方日常需要盯守海量海外批发商群、买手群及客服社群的痛点，`@milesdeutscher` 还展示了 **#7 Group Chat Manager（跨平台群聊总管）**（[https://x.com/milesdeutscher/status/2113653756990816446](https://x.com/milesdeutscher/status/2113653756990816446)，38 赞），部署专职 Bot 同时盯守 WhatsApp、Discord、Slack 与 Telegram 群聊，自动提炼未读长讨论串摘要并起草得体回复。

> [!NOTE]
> 📸 **截图位（待补）**：跨境电商竞品价格变动与差评聚类巡检简报

### 场景

跨境卖家需要实时盯紧对手的三个核心指标：主推款价格变动、新品上架动作、以及买家在近期留下的差评。差评里暴露的做工差、发货慢或尺寸不对，正是自己优化产品文案和供应链切入点的关键情报。同时，巡检独立站外部的推广动态，也能帮助判断竞品的起量渠道。配合 `@milesdeutscher` 的 **#9 Competitor Monitor**，你还可以把监控范围扩展到竞品的 SaaS 订阅层级、捆绑销售策略（Bundles）以及官方 X 账号的置顶促销活动。

### 提示词

```text
你是一名跨境电商竞品监控专家。你的任务是巡检指定的竞品公开页面。

请按照以下规则执行巡检：
1. 打开指定的竞品独立站与商品落地页列表。
2. 提取当前商品标题、变体价格、促销折扣标签与库存展示状态。
3. 对比 /workspace/ecommerce/history_prices.json 中的上一轮巡检数据，标记出价格上调、下调超过 5% 的款式。
4. 抓取该商品公开评价区最新的 10 条买家差评（1-3 星），聚类出核心不满原因（如尺寸不符、物流延迟、配件缺失）。
5. 输出一份简报，包含“价格异动表”与“差评切入点分析”，以 Markdown 格式追加写入 /workspace/ecommerce/daily_report.md。
6. 如果发现竞品主推款降价超过 15%，生成高优先级审批提醒，但不得执行任何自主调价行为。
```

假设你希望进一步部署 `@milesdeutscher` 的 **#9 Competitor Monitor（全维度竞品发布与定价页监控）**（[https://x.com/milesdeutscher/status/2113653726217195817](https://x.com/milesdeutscher/status/2113653726217195817)），可以使用以下配置模板同时锁定竞品官网定价页、Changelog 与 X 官方账号：

```text
你是一名全天候竞品情报监控官（#9 Competitor Monitor）。请巡检 `/workspace/competitors/watchlist.json` 中的 5 家核心竞品：

1. 定价与套餐巡检：访问每家竞品的 `/pricing` 与主推商品页，与昨日快照 `/workspace/competitors/snapshots/` 逐行比对。若发现价格调整、新增隐藏限制条款或限时折扣码，高亮记录变动前后差异。
2. 新品与功能发布：检查竞品的 `/changelog`、`/collections/new` 以及其官方 X 账号过去 24 小时内的推文，识别任何新功能上线、新品首发或核心定位标语（Hero Copy）改动。
3. 应对策略建议：针对每一条确认的竞品异动，给出 1 条我方在广告素材、落地页对比表或定价策略上的反制建议草稿，汇总写入 `/workspace/competitors/intel_brief.md`。
```

### Routine

在后台创建 Competitor-Price-Watch 巡检 Routine。频率建议设为每天固定 1-2 次，例如海外当地时间的上午和下午各跑一次。虽然官方文档显示 v0.75.2 已将 Routine 频率上限提升至全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时（最小定时触发间隔为 5 分钟，[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)），但切勿为了追求所谓的实时而把定时频率调成 5 分钟一次，那会迅速把周额度耗尽（正如 `@charlie_pmp` 在 [https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131) 中拆解的那样，高频且未加精简的冗余 Routine 是后台静默吞噬周额度的头号元凶）。如果竞品经常通过邮件发送促销快讯，你还可以利用 `@SamSokolin` 在 v0.71.2 发布的 **`+alias` 专属邮箱加号别名**功能（[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)、[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)），用 `yourbot+competitors@mail.grokbot.com` 订阅全部竞品的 Newsletter，并配置仅当该 `+competitors` 别名收到新邮件时才事件触发此 Routine。在 Routine 配置中，指定运行脚本读取固定的目标 URL 列表，巡检完毕后将结果以内部卡片形式呈现。

### 成本

使用 Cursor Pro 方案，标价每月 20 美元（https://cursor.com/pricing）；或者选择全新的 **The X Subscription** 统一订阅（**Premium $30/月**、**Super $100/月**、**Ultra $200/月**，Grok Bot、Grok 与 Cursor 三端共享周额度池 + Prepaid Credits 预付额度，[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。官方未公布精确的 token 与运行额度折算规则（https://cursor.com/help/grok-bot/plans）。巡检如果走云电脑自带浏览器渲染页面并解析 DOM，单次运行消耗的资源高于纯文本对话。控制在每天 1 次巡检，周额度通常维持在健康水位；若开启团队版（Teams $40/人/月）、旧版 Pro+（每月 60 美元，https://cursor.com/pricing）或 The X Subscription 的 Super（$100/月）/ Ultra（$200/月）档位，额度容错空间更大。

### 坑

第一个坑是半公开信息召回准确率波动（https://x.com/Hensen1016/status/2108025562048483583）。各电商站点的反爬机制和动态前端加载差异大，Bot 有时无法完整拉取评论列表。第二个坑是机房 IP 拦截问题。Grok Bot 默认运行在数据中心网络环境，容易被防爬系统拦截，需要按官方说明更新电脑组件后开启本地出口路由（Local Egress Routing）借由本机 IP 发起请求（https://x.com/xiaohu/status/2099409639234289914）。在最新桌面端客户端中，正如 `@XueshiQiao` 实测验证的那样（[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)），只需进入 `Settings > Computer > Your computer > Route traffic through this computer` 开启本机流量路由（[https://cursor.com/docs/grok-bot/settings](https://cursor.com/docs/grok-bot/settings)），云端浏览器的出站请求就会走你家里或办公室的真实住宅/办公桌面 IP，瞬间化解电商平台的数据中心 IP 封禁与频繁验证码拦截。第三个坑是让 Bot 自动修改自己店铺售价。长对话里 Bot 可能忘掉之前的调价约定，所以关键运营动作必须有人类复核。

测试云电脑在开启本地出口路由下连续访问主流电商商品页的抗封禁表现。

## 16.3 官方岗位指南速览 · Official Role Playbooks

xAI 官方在 `https://x.ai/bot/guides` 页面上线了一系列官方岗位实战指南，覆盖销售、招聘、法务、支持和市场营销等职能（https://x.ai/bot/guides），并在全面迁移整合后的 Cursor 技术文档中心同步上线了官方行业与岗位用例总览 [https://cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases) 以及团队协作文档 [https://cursor.com/docs/grok-bot/teams](https://cursor.com/docs/grok-bot/teams)。**官方所有岗位指南的核心哲学就是把人类留在关键判断上**。官方指南逐一拆解了如何用专门的 Bot 接管高频杂活，而在涉及对外发送、花钱和签署的闸门处一律配置人工审批（详见官方工作流与审批文档 [https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。

在 v0.75.2 版本中，官方重磅推出了 **Pages（Canvas）** 实时交互画布功能（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)、[https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)，6,544 赞 / 567 转发 / 2,008 书签）。这使得销售、运营、招聘与财务团队不再满足于在聊天窗口里翻找零散的文本卡片，而是可以直接命令 Bot 创建并持续热更新包含表格、图表、漏斗与时间线的实时业务看板（底层由 `WriteCanvas` / `EditCanvas` / `ReadCanvas` / `ListCanvases` 驱动，永久沉淀在 Bot 右侧信息栏 `Bot info pane → Library` 中）。打开任意 Page 点击右上角 **Share**，即可按三级权限灵活管控可见范围（[https://cursor.com/docs/grok-bot/teams](https://cursor.com/docs/grok-bot/teams)）：
1. **`Only you`**：仅创建者本人可见，适合个人业绩草稿或薪酬测算。
2. **`Your team`**：团队全员可见（Team 计划默认开启，团队管理员可在 `Dashboard → Grok Bot → Bot capabilities` 中全局管控）。
3. **`Anyone with the link`**：生成公开分享链接，适合直接发给外部客户、投资人或供应商查看实时周报。

![官方五大职能岗位（销售、招聘、法务、客服、市场）的人机分工与审批卡闸门体系](../images/fig-16-2.png)

*图：官方五大职能岗位（销售、招聘、法务、客服、市场）的人机分工与审批卡闸门体系*

### 1. 销售：Founder-Led Sales 与 Post-Sales

官方专门推出了针对创始人销售（Founder-Led Sales）和售后面向客户支持（Post-Sales）的指南（https://x.ai/bot/guides/sales 及 [https://cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases)）。在销售场景中，Bot 被定义为客户专员的幕僚长（Chief of Staff），负责在开会前准备背景材料，开会后把录音转录成跟进邮件草稿，并更新客户关系管理系统（CRM），让人类全神贯注于客户信任的建立。官方推荐的销售 Bot 包括 Jon Grigull 开发的 Deal Inspector（基于通话记录根据准入标准检查商机阶段）、Krista Letz 开发的 Pipeline Pulse（扫描商机停滞环节与预测风险）和 Outbound Prospecting（匹配潜在客户并起草初次沟通话术），以及 Daniel Brill 开发的 Call Follow-Ups 与 Sales Call Coach（https://x.ai/bot/guides/sales）。

销售人员跑完一场会议后往往没有精力写复盘和更新 CRM，可以直接给 Call Follow-Ups 设定以下提示词：

```text
你是一名 B2B 销售幕僚长。你的职责是将本次客户会议纪要转化为跟进邮件草稿与 CRM 更新记录。

请按照以下要求处理输入的内容：
1. 读取附带的客户通话纪要与转录文本。
2. 提取客户明确表达的 3 个核心痛点以及我们在会议中承诺交付的事项。
3. 模仿我的语气撰写一封感谢与跟进邮件草稿，重点强调下一步推进节点与交付承诺，语气专业、直接。
4. 生成 CRM 字段更新字典：包含商机阶段、预估签约时间、当前阻碍点。
5. 所有邮件草稿必须以待审核状态呈现，严禁自动发送邮件给客户。
```

将这个流程制作成 Routine，关联每场会议结束的日历事件或通话录音归档，自动产出复盘。在 v0.75.2 更新后，销售团队还可以将邮件原样转发给客户或内部法务，Bot 在转发邮件时能够完整保留原邮件的 HTML 排版格式、正文内嵌图片（inline images）以及 PDF 报价单等文件附件（[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)）；同时，销售外勤人员可以在 iPhone 15 Pro 及后续机型上通过侧边 **Action Button（操作按钮）** 一键呼出 Grok Bot 实时语音通话（需 iOS 客户端 v1.16+，[https://cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)、[https://x.com/bot/status/2112246033178968161](https://x.com/bot/status/2112246033178968161)），在走出客户大楼的电梯里直接口述会议要点，挂断瞬间自动生成带完整逐字稿的 Voice chat card 并触发跟进动作，还能直接授权读取与写入 iPhone 本地的原生日历（Calendar）、提醒事项（Reminders）与通讯录（Contacts）（[https://cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）。单月成本依托 Cursor Pro 的 20 美元月费（https://cursor.com/pricing）或 $30/月的 The X Subscription Premium 档位（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）即可启动。这套玩法的常见坑是幻觉承诺：Bot 可能在草稿中顺着客户的提问擅自答应超出产品能力的功能排期，销售人员如果没仔细看草稿就直接发出，会酿成严重交付事故。

### 2. 招聘：Recruiting & ATS Triage

官方招聘指南《Grok Bot for Recruiting》详细介绍了招聘团队如何借助 Bot 承担通宵人才寻访、面试评分卡整理以及申请追踪系统（ATS）流转（https://x.ai/bot/guides/recruiting 及 [https://cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases)）。官方生态里推荐了 Tommy Hansen 制作的 Recruiting Coordinator（负责排期和面试官准备，且绝不会单独向候选人发邮件）与 Talent Discovery（在 ATS 之外发掘新人才），Simon Lackowski 制作的 Hiring Signals（监控选定公司的招聘动态并标出变动），以及 Natasha Kuo 的 Executive Assistant 和 Matt Palmer 的 Writing Bot（https://x.ai/bot/guides/recruiting）。

在候选人寻访场景中，招聘专员要在海量公开资料中比对岗位匹配度，提示词可以针对硬性指标进行规范：

```text
你是一名技术招聘助理。你的任务是根据指定的资深前端岗位描述，在候选人信息中进行硬性条件初筛。

岗位硬性条件：
- 熟悉 TypeScript 与现代 Web 应用架构；
- 具备 3 年以上分布式系统或复杂客户端开发经验；
- 有开源项目贡献或技术写作经历。

执行步骤：
1. 分析候选人公开简历与履历。
2. 逐一比对上述 3 项硬性条件，明确给出每项匹配度说明（完全符合 / 部分符合 / 不符合）。
3. 提炼出 3 个值得在首轮技术沟通中深入询问的具体项目难点。
4. 输出候选人评估摘要，存入 /workspace/recruiting/shortlist.md。
5. 绝不得直接向任何候选人发送沟通邮件。
```

官方企业版公告举过例子：Bot 夜里寻访候选人，早上给出短名单，外联消息排队等人审核（https://x.ai/news/grok-bot-for-enterprise）。照这个思路，Routine 可以设成每晚处理 ATS 导出的简历文件夹。此外，随着 X 插件打通 `@chat` 端到端加密私信收件箱与陌生人消息请求（由工程师 `@pjvann` 于 2026-10-16 宣布，[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)，1,069 赞），技术招聘官与创始人还可以让 Bot 配合本地 `xchat-grokbot-helper`（[https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper)）与 4 位 PIN 码，自动从繁忙的 X 陌生人私信请求中筛出优秀的自荐候选人并起草面试邀约。成本同属基础套餐范围。招聘场景最严重的坑是偏见与误杀：由于 Bot 对简历中非标准表达理解有限，可能将具备实际优秀经验但文书不标准的候选人过滤掉；同时，招聘涉及个人敏感隐私，千万不要让 Bot 把含有候选人联系方式的数据同步到公开渠道。

### 3. 法务与采购：Legal Ops & Haggle Bot

官方指南《Grok Bot for Legal Ops》展示了法务运维团队如何使用 Bot 进行法律顾问 1 对 1 会前准备、Slack 工单分流、合同工作流流转，并始终贯彻“起草完毕由人工发送”的审核流程（https://x.ai/bot/guides/legal 及 [https://cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases)）。法务相关的推荐 Bot 包括 Daniel Gartshein 的 Haggle Bot（检查企业 SaaS 软件闲置席位与重复扣费，并起草谈判降价邮件）、Shub Gaur 的 Sell Bot（在客户生命周期中起草方案和合同）、Farzad 的 Researchy（带出处的实效网络检索与事实核查）、Lenny Rachitsky 的 Overheard，以及 Anoop Baliga 的 Company Docs Q&A（https://x.ai/bot/guides/legal）。在个人与小微团队场景下，`@milesdeutscher` 同样验证了与之同构的 **#6 Subscription Auditor（订阅账单审计与自动砍价/退订员）**（[https://x.com/milesdeutscher/status/2113653772337770849](https://x.com/milesdeutscher/status/2113653772337770849)，54 赞），专门扫描周期性扣款的 SaaS 与消费级订阅账单，识别闲置服务并代为起草降价谈判或退订申请。

在企业实际案例中，xAI 内部使用 Haggle Bot 为公司找到了超过 100,000 美元的直接节省，其中一笔科技采购单通过分析直接从 14,629 美元降至 6,143 美元，降幅达 58%（https://x.ai/news/grok-bot-procurement）。该采购提示词的核心是参数比对：

```text
你是一名企业采购谈判顾问。你的任务是审查当前公司的软件采购续约账单。

请按以下流程处理：
1. 提取当前软件合同中的席位单价、总席位数、历史续约条款以及当前实际使用率。
2. 检索当前市场上同类工具的公开采购折扣基准与同等规模企业的成交价格区间。
3. 检查是否有闲置未分配席位或功能重复的采购项。
4. 按照 TODAY / SAVE / REC / NEXT 的标准格式输出审查报告。
5. 起草一封给供应商客户经理的续约协商函草稿，明确提出削减闲置席位并申请 15% 长期客户折扣。
6. 协商函仅供人工审核，不得自动外发。
```

Routine 可以挂接在财务账单审批流上，每月巡检一次续约项目。成本方面，仅需个人或企业版基础开销，却能撬动数千乃至数万美元的成本削减。法务和采购的踩坑点是权责边界：合同条款里的免责、管辖权和违约责任极度敏感，Bot 生成的条款修改意见只能作为初审参考，绝不能替代持证法务人员的正式审查；同时，千万不要将公司未公开的商业合同原文随意投喂到没有权限隔离的环境中。

### 4. 客户支持：Support Queue & Plain Integration

官方指南《Grok Bot for Support》介绍了客服团队如何在合上电脑后，依然通过连接器、分类任务和自动 Routine 保证工单不掉线（https://x.ai/bot/guides/support 及 [https://cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases)）。官方推荐 Bot 包括 Anoop Baliga 的 Product Support Inbox Assistant（寻找并起草产品问题答复，但绝不自动发出）、Customer Call Coach & Assistant、Customer Proof Desk（逐字保留原话把通话记录转换为客户故事），以及 Krista Letz 的 EBR & Value Deck Builder（为特定大客户构建高管复盘报告，绝不编造数字）（https://x.ai/bot/guides/support）。

在官方公开的客服团队实践中，2026 年 8 月 14 日 Cursor 并入 SpaceX SuperIntelligence（SpaceXSI）后，全球客服工单总量瞬间增长了 175%，而团队通过部署由 **Intake Triage Bot（分诊接待 Bot）**、**Billing & Refund Bot（账单与退款 Bot）**、**Technical Repro Bot（技术复现 Bot）**、**Incident Batch Bot（事故批处理 Bot）** 以及 **Product Feedback Synthesizer Bot（产品反馈聚类 Bot）** 组成的五位专职 Bot 舰队，没有新增任何一名全职客服人手，相当于节省了约 200 名新增客服人力（https://x.ai/news/grok-bot-customer-support）。单次工单处理成本仅为 0.20 至 0.30 美元，远低于传统 AI 客服每次 1 至 4 美元的成本（https://x.ai/news/grok-bot-customer-support）。系统学习了超过 100 万条历史工单口吻，99% 的退款请求无需人工介入，在一次重大线上突发故障期间，仅由一名工程师审核一张批量审批卡（batch approval card），就在约 10 分钟内批量处理清零了 204 张事故工单，且每天能从海量对话中自动提炼超过 20,000+ 条产品反馈数据点转化为研发工单，但在对话来回超过 3 次时会自动升级转人工（https://x.ai/news/grok-bot-customer-support）。客服分流提示词如下：

```text
你是一名客户支持工单初审专员。你的工作是阅读客户工单并起草答复。

处理规则：
1. 阅读客户提交的技术问题，对照 /workspace/docs/help_center.md 中的官方文档。
2. 如果属于已知高频配置问题，提取准确的步骤链接，并起草一段语气温和、直接解答的回复。
3. 如果客户问题涉及退款、账号安全或系统严重 Bug，标记为 HIGH 优先级并直接指派给人工值班专员。
4. 如果此工单在此前已经过 2 轮沟通仍未解决，立刻触发人工接管升级流程。
5. 所有答复保持内部草稿状态，经人工支持人员确认前严禁直接点击发送给客户。
```

配置为常驻 Routine，轮询客服系统待办队列。成本方面，高并发场景下需要企业版权限支持。客服的核心坑在于失控回复：如果放任 Bot 自由直复，遇到复杂 Bug 时容易给出错误排查建议导致用户误操作破坏数据；因此官方内部也是严格走完“只写内部备注与人工审批”到“评估充分后放开特定场景直回”的阶段演进（https://x.ai/news/grok-bot-customer-support）。

### 5. 市场营销：Performance Marketing & Content Desk

官方指南《Grok Bot for Marketing》和《Grok Bot for Performance Marketing》系统展示了营销团队如何运用多个专门 Bot 完成竞品调研、Google Docs 定位草案撰写、广告投放骨架搭建以及直接向营销站点提交 PR（https://x.ai/bot/guides/marketing 及 [https://cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases)）。推荐 Bot 包括 Shub Gaur 的 Distro Bot（管理活动、创意与发帖，未经确认绝不花钱）、Adam Tanguay 的 SEO & AEO Desk（将关键词转化为选题和写作者大纲）与 AI Search Visibility（监控 AI 助手是否推荐自身品牌及提到了哪些对手），以及 Miguel Cruz 的 Paid Media Report Desk（将广告导出数据整合成真实数字周报）和 Ad Spend Watch（在预算被烧光前发出预警）（https://x.ai/bot/guides/marketing）。自 v0.71.2 起，营销团队还能直接调用内置的 **Grok Imagine**（`GenerateImage`、`GenerateVideo`）在对话中生成与编辑营销视频，或结合云电脑代码渲染 Remotion / Motion Graphics 动态信息图广告素材（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)、[https://x.com/bot/status/2110566041772617908](https://x.com/bot/status/2110566041772617908)）。

在市场投放与内容大纲搭建中，SEO 与大纲生成提示词如下：

```text
你是一名内容营销大纲专家。你的任务是将搜索关键词转化为结构化内容写作大纲。

输入目标关键词：[输入关键词]

执行要求：
1. 分析该词背后的用户搜索意图（获取信息、寻找替代品、还是比价购买）。
2. 列出读者在阅读该主题文章时必须了解的 5 个关键概念。
3. 规划文章的 H2 和 H3 目录结构，并在每个章节下方列出必须回答的具体问题。
4. 明确标注本篇文章应该插入的产品真实使用案例位置，避免空洞说教。
5. 生成 Markdown 大纲文件保存至 /workspace/marketing/briefs/。
```

将该流程配置为每周执行的 Routine，自动抓取最新的搜索热点生成写作任务清单。成本由月度基础席位覆盖。市场营销的坑在于空话套话泛滥：未经严格约束的 Bot 往往生成大量充斥着陈词滥调的低质内容，无法获取有效流量；此外，广告投放 Bot 必须严格受控，绝不能开启免审批的预算调整权限，防止因数据延迟引发过度消耗。

### 6. 用 Pages（Canvas）构建跨岗位实时业务看板与三级权限治理

当你在销售、运营、招聘与财务环节分别部署了多个专职 Bot 后，挨个点开聊天窗口核对进度会迅速陷入界面混乱。社区开发者 Melvin Vivas（`@melvindvivas`）在获得 1,087 赞、51 转发、1,687 书签的实战帖（[https://x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882)）及其提示词跟帖（[https://x.com/melvindvivas/status/2113676938820895045](https://x.com/melvindvivas/status/2113676938820895045)）与 Routine 跟帖（[https://x.com/melvindvivas/status/2113968491573514576](https://x.com/melvindvivas/status/2113968491573514576)）中，给出了一套被 `@JayKurtz90` 盛赞为“Pages 杀手级应用”（[https://x.com/JayKurtz90/status/2113983882018119823](https://x.com/JayKurtz90/status/2113983882018119823)）的解决方案：让 Chief of Staff（幕僚长）Bot 创建一个名为 `Business & Activity Dashboard` 的实时 **Page**，统一收口所有职能岗位的动态指标。

你可以直接复制以下提示词，为销售、运营与财务团队生成并维护一张实时业务看板 Page：

```text
你是一名业务运营幕僚长（Chief of Staff）。请调用 Pages（Canvas）工具创建并持续维护一个名为 "Weekly Revenue & Ops Command Center" 的实时交互式看板页面：

1. 核心业务模块布局：
   - 【销售漏斗（Sales Pipeline）】：汇总本周新增 SQL 数量、各阶段商机金额、超过 7 天未跟进的停滞商机预警表。
   - 【运营与竞品（Ops & Competitors）】：展示本周竞品价格异动汇总、客服工单平均响应时长与高频产品反馈 Top 5。
   - 【财务与订阅审计（Finance & SaaS Spend）】：列出本月即将自动续费的 SaaS 合同清单、预估可削减的闲置席位金额与月度预算消耗进度条。
   - 【待人工审批队列（Waiting for Human Approval）】：集中展示所有专职 Bot 生成的待发销售跟进信、采购砍价函与调价建议，附带时间线视图（Timeline view）、进行中任务（Tasks in progress）与已完成任务（Completed tasks）。
2. 热更新机制：每次收到各专职 Bot 的日报数据或定时 Routine 触发时，直接在原 Page 上调用 EditCanvas 就地刷新图表与表格数据，不要重复新建零散文档。
```

看板生成后，它会永久保存在 Bot 右侧信息栏的 **Library**（`Bot info pane → Library`）中。团队负责人只需点击右上角 **Share**，即可根据业务密级配置三级权限（[https://cursor.com/docs/grok-bot/teams](https://cursor.com/docs/grok-bot/teams)）：涉及未公开财务底稿的页面设为 **`Only you`**；供销售与运营全员每日晨会对齐的作战大盘设为 **`Your team`**；而面向外部大客户的交付进度周报或渠道伙伴看板，则可设为 **`Anyone with the link`** 一键外发。

## 16.4 房产等垂直行业 · Vertical Industries & Enterprise

除了通用的销售和客服，Grok Bot 在垂直行业的落地也展现出了清晰的轮廓。官方在企业版通告中点名了一批正在重度使用 Grok Bot 的垂直企业，包括现场维修与承包商服务平台 ServiceTitan、Legora 以及超微电脑 Supermicro，并强调其最繁重的使用场景其实发生在工程研发部门之外（https://x.ai/news/grok-bot-for-enterprise）。小企业保险公司 Harper 就在 24 小时内搭建了 Team Bot，用于筛查保单失效的客户并协助恢复，直接为客户挽回了超过 120,000 美元的损失（https://x.ai/news/team-bots）。在这些领域，**垂直行业的落地价值在于夜间跨系统的低级搬运**。

而在金融投研、宏观对冲与专业咨询等高门槛垂直行业中，最大的痛点往往是核心数据源被锁在昂贵的付费墙（Paywall）之后，且企业安全合规部门严禁把机构账号密码明文发给 AI。2026 年 10 月 22 日，官方联合 1Password 正式上线 **1Password Brokered Sign-in（逐次代理授权免密登录）**（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)、[https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874)、[https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)）。正如中文社区交易员与投研博主 `@oxpsats`（偶像派作手）在实战中所展示的那样（[https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670)），投研人员现在可以将彭博社（Bloomberg）等付费财经终端的会员凭据保存在 1Password（Personal / Private 密码库，需本地安装 1Password 8.12.42+ 客户端），当 Grok Bot 在云端浏览器中遇到付费墙请求登录时，投研人员只需在手机或电脑的 1Password App 上按一下指纹/面容完成逐次生物识别审批（Review in 1Password），凭据即被零知识注入浏览器会话——Bot 全程绝不会在上下文或日志中看到明文密码，就能全自动突破付费墙，定时抓取并深度研读海外一手宏观研报与机构简讯。

> [!NOTE]
> 📸 **截图位（待补）**：垂直行业工单跨平台信息聚合与确认卡片

### 场景

以房产经纪、物业租赁或类似 ServiceTitan 覆盖的家居维修承包商为例，日常业务有着极强的线下依赖性。客户在深夜可能会发邮件或提交表单咨询某套房源的带看预约，或者报修水管漏水。传统人工模式下，次日上班前这些线索处于无人响应状态，很容易流失。Bot 的作用不是代替经纪人带看，而是在夜间即时核验房源或师傅排期、清洗意向客户联系方式、并整理好带看日程草案。同理，在跨境移民咨询（如 `@bitman2140` 实测的香港优才计划续签材料跟进与香港学校插班信息搜集，[https://x.com/bitman2140/status/2114210291546493153](https://x.com/bitman2140/status/2114210291546493153)）以及二级市场金融投研（如 `@oxpsats` 的彭博社付费墙研报自动巡检，[https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670)）中，Bot 同样扮演着夜间跨系统抓取、核验与草拟简报的专职研究员角色。

### 提示词

```text
你是一名本地房产中介团队的数字办公室管家。你的职责是处理夜间进来的租售咨询与看房预约表单。

处理规则：
1. 读取新提交的客户预约邮件，提取：客户称呼、联系电话、目标房源编号、期望看房时间。
2. 打开 /workspace/realestate/listings.json，检查该房源编号当前是否处于“可带看”状态。
3. 对照经纪人工作日历，确认该期望时间段是否有空闲档期；若有冲突，顺延匹配最近的两个备选空闲时段。
4. 在内部日程表中起草一条预约日历项草案，并给房产经纪人生成一条简短的带看准备卡片。
5. 草拟一条确认短信草稿发给客户，告知已收到申请，经纪人将在早晨 9:00 前人工联系确认。
6. 严格执行草稿优先原则，不得直接调用任何外部网关自动发送短信。
```

而在金融投研场景下，若要复刻 `@oxpsats` 利用 1Password 授权登录彭博社（Bloomberg）等付费墙终端自动提炼每日宏观交易内参的工作流（[https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670)），可配置如下提示词：

```text
你是一名二级市场宏观与海外权益投研助理。你的职责是每日清晨登录已授权的付费财经终端（如 Bloomberg 彭博社），提取核心研报与市场异动。

执行步骤：
1. 访问指定的 Bloomberg 专栏与追踪标的列表。若会话过期遇到登录拦截，按照官方优先级调用已保存的浏览器会话或发起 1Password Brokered Sign-in 授权请求（等待我在 1Password 客户端审批注入凭据，切勿在对话中索要明文密码）。
2. 重点精读过去 12 小时内关于美联储利率路径、大宗商品库存及半导体供应链的深度付费长文。
3. 剥离情绪化修辞，提取文中披露的硬核数据点、机构持仓变化与正反双方核心分歧，严禁编造任何未在原文出现的数字。
4. 将研读笔记更新至团队共享的投研看板 Page，并保存归档至 `/workspace/research/bloomberg_daily_digest.md`。
```

### Routine

配置 Nightly-Lead-Triage 的定时任务，每天夜间每隔 30 分钟轮询一次表单收件箱。根据官方文档 [https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)，v0.75.2 支持全账号所有 Bot 合计最高 300 次/小时、单条 Routine 最高 200 次/小时的运行频率（最小定时触发间隔 5 分钟），每 30 分钟一次的夜间轮询完全在安全配额之内。官方平台支持通过 Team Bots 与企业版安全策略，让多个业务人员在共享 Bot 能力的同时保持各自对话的私密性（https://x.ai/news/team-bots 及 [https://cursor.com/docs/grok-bot/teams](https://cursor.com/docs/grok-bot/teams)）。

### 成本

单人开展业务只需 Cursor Pro 方案，标价每月 20 美元（https://cursor.com/pricing），或开通 **The X Subscription** 的 **Premium（$30/月）**、**Super（$100/月）**、**Ultra（$200/月）** 档位（三端共享周额度池 + Prepaid Credits 预付额度，[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）；中小型团队如果采用自助式 Cursor Teams 方案，官方标价为每人每月 40 美元（https://cursor.com/pricing）。官方企业版（Enterprise）曾为 Grok 和 Cursor Enterprise 用户提供两周免费试用（https://x.ai/news/grok-bot-for-enterprise）。轮询任务在夜间平稳跑动，消耗可控。

### 坑

垂直行业涉及大量高敏感度的线下资产与个人隐私数据（如房屋具体门牌号、产权信息、客户银行对账记录）。在系统配置中必须严格做好数据边界隔离，千万不能把不同业务的数据放在同一个无隔离的对话环境中。此前曾发生过 CEO Shane Mac 的个人财务 Bot 把包含私人银行余额与刷卡支出的财务审计结果错误发送至公司高管 Slack 频道的严重隐私泄露事故（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/）。垂直行业应用中，涉及交易、资金和私人住址的数据，必须强制配置多因子审批和通道隔离。

针对金融机构、律所、医疗及大型垂直企业的严苛合规要求，官方在最新企业级安全架构文档 [https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security) 与工作流文档 [https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work) 中提供了完整的纵深防御工具箱，企业 IT 与安全管理员在落地时应重点启用以下五项机制：
1. **国际权威合规认证与审计遥测**：Grok Bot 底层架构已正式通过 **ISO/IEC 27001**（信息安全管理体系）与 **ISO/IEC 42001**（人工智能管理体系）权威认证；企业级 OpenTelemetry 遥测导出支持通过属性标签 `cursor.surface=grok_bot` 精准过滤并审计 Grok Bot 的全部调用事件（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。
2. **出站网络白名单与 `Apply to MCP servers` 强制锁定**：企业管理员可将云端虚拟机（cloud box）的出站流量严格限制在自定义域名白名单内（格式如 `*.domain.com:443`），并勾选新增的 **`Apply to MCP servers`** 选项，将该网络白名单同步强制应用于所有 MCP 服务器的调用请求，彻底杜绝敏感行业数据向未知外部域名外泄（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。
3. **团队自定义 Auto-Review 规则与 Inference Hooks（推理钩子，Beta）**：管理员可以用自然语言编写团队专属的 Auto-Review 审查规则，并将执行策略强制设为 **`Block`（直接阻断）** 或 **`Require approval`（要求人工审批）**；对于高度受监管的金融与法务场景，还可挂载 **Inference Hooks（推理前/推理后 Pre/post-inference 拦截钩子，Beta）**，在模型推理前后执行自动化合规脱敏与策略拦截（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）。
4. **登录与支付凭证调用优先级及“一密一宅”隔离原则**：根据官方 [Work 技术文档](https://cursor.com/docs/grok-bot/work)，Bot 的登录（Sign-in）调用优先级依次为：`已保存的浏览器会话 → Vault → 1Password → 聊天内 Secure Form → Take over screen（人工接管屏幕）`；结账支付（Checkout / Payment）优先级依次为：`Vault → 聊天内 Secure Form → Link / X Money → Take over screen`。在实战中，强烈建议遵循 `@martinpaulweiss` 提出的“一密一宅（One home per secret）”拆分准则（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）：将所有企业日常办公与付费终端登录凭据（含 2FA 动态码）统一存放在 **1Password** 中通过逐次审批调用，绝不在 Vault 中常驻保存企业高额度信用卡（详见 [https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）。

测试房产预约表单在遭遇时间冲突时自动计算备选带看时段的准确率。


# §17 从零搭一个“中文内容工作室” · Capstone A: Building a Chinese Content Studio

很多新手刚上手时，习惯把所有杂事一股脑塞进同一个对话框。两三天后上下文彻底乱掉，最后只能推倒重来。搭建一个**四人内容工作室**，核心是从单聊转向团队协作。

账号内 Bot 数量自 9 月 1 日 v0.31.0 起不再限于约 50 个（https://x.ai/changelog/bot），群聊支持容纳 2 到 6 个 Bot（https://cursor.com/help/grok-bot/chat-and-collaboration）。这个项目不需要堆砌过多角色，团队成员建议先从最精炼的结构起步（https://x.com/poteto/status/2108097362283597916，团队成员 X 帖）。整个工作室只设四个角色：总编辑负责任务拆解与全局把控；选题情报员搜集线索与行业动态；文案主笔把选题扩写为草稿；审校排版员对照事实与平台规范做质检。

![四人内容工作室协作架构与信息流向](../images/fig-17-1.png)

*图：四人内容工作室协作架构与信息流向*

整套搭建按七天推进，每天推一个确定的模块，从建号、拉群、沉淀技能，一路做到定时自动化与最终审计。

## 17.1 项目目标与四人编制 · Blueprint & Roles

搭建这套工作室的目标不是让 AI 代替人自动发文，而是建立一条半自动化的内容生产管线。国内主流自媒体平台都没有官方原生插件（https://xiangyugongzuoliu.com/grokbot-use-cases/），全自动发帖极易触发平台风控，内容发布的最终点击权必须牢牢留在人手里。

架构上，团队成员在官方指南中提出了项目频道与名册的组织方式（https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots）。每个项目对应侧边栏的一个群聊频道，配置专属名册。四个 Bot 在同一台云电脑上协同工作。社区帖称云电脑配置为 8 vCPU、16GB 内存和 128GB 硬盘空间（个例）（https://x.com/hejushang8/status/2103760664217174494）。这意味着所有 Bot 共享同一个文件系统与已登录会话，彼此没有物理隔离（https://cursor.com/help/grok-bot/computer-and-apps）。

四个角色的分工很明确。总编辑单线对接人类指令，将目标拆解后在群内派单，汇总最终成品。选题情报员定向巡检公开网页与资讯，按统一字段清洗为选题卡片。文案主笔根据批准的选题，调用结构模板撰写初稿并生成本地 Markdown 文件。审校排版员核对文中事实出处，排查敏感词与语病，输出修改意见表。

第一天就要确立**红黄绿权限边界**（这是本书的归纳说法，官方文档只规定了哪些动作需要审批）：读取公开资讯与本地排版属于绿色自主动作；向群聊交接文件属于黄色受控动作；对外发送邮件、向外部接口推送数据或执行发布操作，必须严格弹出审批卡，未经人工点击绝不执行（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

### 从 4 人精简编制平滑演进到“1 CEO + 5 专职 Bot”全功能工作室

当你把 4 人精简编制跑通并稳定产出后，如果面临多平台日更、深度选题策划以及图文/短视频配套视觉生产的压力，可以参考中文社区创作者夏哥研究室（`@CyberAlice3269`）在 2026 年 10 月 19 日分享的 **“1 个 CEO + 5 个专职 Bot”自媒体内容工作室架构**（https://x.com/CyberAlice3269/status/2112098767151468645），刚好卡满官方群聊最多容纳 6 个 Bot 的上限（https://cursor.com/help/grok-bot/group-chats），将 4 人团队平滑扩展为 6 人全功能编制：

| 岗位阶段 | 4 人精简编制（起步期） | 6 人全功能编制（`@CyberAlice3269` 1+5 范式） | 拆分逻辑与共享底座 |
| :--- | :--- | :--- | :--- |
| **总控层** | **总编辑（Chief of Staff）** | **CEO Bot（总助/主编）** | 唯一对外接收人类语音或文字指令的入口，负责任务拆解、派单与最终验收。 |
| **输入与策划层** | **选题情报员**（兼顾搜集与立项） | **① 情报搜集 Bot** + **② 选题策划 Bot** | 将“客观事实抓取”与“受众痛点/切入角策划”解耦：情报员只管跑脚本拉取高信噪比素材，选题策划专门对比账号历史爆款库定调立项。 |
| **生产与质检层** | **文案主笔** + **审校排版员** | **③ 初稿撰写 Bot** + **④ 审校润色 Bot** | 初稿撰写专注结构与信息密度；审校润色除了核查事实与违禁词，还负责去 AI 味与多平台格式转换。 |
| **视觉交付层** | *(由主笔顺带生成提示词或人工配图)* | **⑤ 配图制作 Bot（Visual Producer）** | 专职调用 v0.71.2 上线的 Grok Imagine（`GenerateImage` / `GenerateVideo`）及云电脑代码动效生成封面、正文插图与信息图 B-roll（https://x.ai/changelog/bot）。 |

在 `@CyberAlice3269` 的实战体系中（https://x.com/CyberAlice3269/status/2112098767151468645），这 6 个 Bot 之所以不会各自为战，关键在于全员背后挂载了**统一共享的本地知识库目录（如 `/workspace/learn/` 与 `/workspace/sop/`）与标准 SOP Skill**。假设你刚开始搭建，建议前五天严格按 4 人编制走完闭环；一旦发现情报员既要盯几十个信源又要写选题策划案导致上下文过载，或者文章急需配套视觉素材，只需新建“选题策划”与“配图制作”两个 Bot 并拉入群聊，让它们直接读取同一套 `/workspace/` 目录即可完成零摩擦扩容。

## 17.2 周一：岗位说明书与 Bot 初始化 · Day 1: Job Descriptions & Profiles

周一的任务是初始化四个 Bot。给 Bot 写设定时，不要只写一句简单提示词，要为每个 Bot 写好**岗位说明书五要素**，涵盖身份与记忆、核心使命、关键规则、工作流程和成功指标（https://juejin.cn/post/7682695577956483091）。

> [!NOTE]
> 📸 **截图位（待补）**：总编辑 Bot 的创建面板与 Profile 设置

在桌面端点击新建 Bot，先配置总编辑的 Profile：

```text
【身份与记忆】
你是中文内容工作室的总编辑（Chief of Staff），只向我（负责人）直接汇报。你熟悉中文自媒体的传播规律，统筹选题情报员、文案主笔和审校排版员。

【核心使命】
将负责人的粗粒度想法拆解为具体任务，分发给专业 Bot，跟踪进度并交付符合排版规范的成稿。

【关键规则】
1. 严禁对外发布任何未经负责人确认的内容。
2. 所有派单指令必须指明具体责任人与验收标准。
3. 知识库与规范文件统一存放在 /workspace/learn/ 目录下。

【工作流程】
接收需求 -> 派发选题调查 -> 审核选题并报负责人批准 -> 指派主笔撰稿 -> 指派审校质检 -> 交付成品。

【成功指标】
任务流转无死循环，每个交付物附带完整来源。
```

> [!NOTE]
> 📸 **截图位（待补）**：情报员 Bot 的岗位说明书配置

接着创建选题情报员的 Profile：

```text
【身份与记忆】
你是工作室的选题情报员，专注于科技与 AI 领域的公开资讯挖掘与线索梳理。

【核心使命】
定期巡检指定的公开网页与行业动态，筛选具备传播价值的事实性线索，输出结构化选题卡。

【关键规则】
1. 只搜集可公开访问的网页内容，不抓取需要登录的后台数据。
2. 每个选题必须包含原始链接、核心事实、用户痛点和建议角度，缺一不可。
3. 遇到网络连接超时或无法访问时，明确记录失败源，不得编造假数据。

【工作流程】
扫描目标页面 -> 过滤广告与空泛宣发 -> 提取核心事实 -> 格式化输出到选题清单。

【成功指标】
每周提供至少 15 条具备完整事实出处的高质量线索。
```

> [!NOTE]
> 📸 **截图位（待补）**：主笔 Bot 的规则与提示词录入

创建文案主笔的 Profile：

```text
【身份与记忆】
你是工作室的文案主笔，精通中文自媒体写作，擅长将复杂的技术事实转化为通俗易懂的干货文章。

【核心使命】
依据已通过审批的选题卡，严格遵循参考结构撰写成稿草稿，并将文本保存到指定文件。

【关键规则】
1. 严禁使用空话、套话和未经证实的夸大修辞。
2. 保持第一人称叙事风格，语言接地气，多讲步骤与避坑细节。
3. 成稿必须保存为本地 Markdown 文件，不得直接调用任何发布接口。

【工作流程】
读取选题卡 -> 拟定大纲 -> 撰写正文 -> 输出草稿到本地目录 -> 交接给审校排版员。

【成功指标】
语言无空话，重点技术名词准确，交付格式符合规范。
```

> [!NOTE]
> 📸 **截图位（待补）**：审校员 Bot 的指标与质检配置

最后创建审校排版员的 Profile：

```text
【身份与记忆】
你是工作室的审校排版员，把守内容质量的最后一道关口，负责事实核验、格式审查与敏感词拦截。

【核心使命】
逐行审查主笔提交的草稿，比对原始事实链接，排查错别字与违禁词，输出清晰的审核报告。

【关键规则】
1. 凡草稿中出现的数字、参数与结论，必须能在原始参考资料中找到依据。
2. 发现事实存疑或格式错误，直接退回并标明行号，不得私自篡改原文核心事实。
3. 严禁点击任何网页端或客户端的“发布”按钮。

【工作流程】
读取主笔草稿 -> 比对信源 -> 检查 Markdown 标记与排版规范 -> 生成审校问题清单。

【成功指标】
零事实捏造漏洞，格式合格率 100%。
```

社区实践指出，调性卡、规则文件等持久化知识必须落盘到本地目录，以供后续所有 Bot 统一查阅（https://www.jxxy.net/ai/articles/grok-bot-workflow-training/）。此外，中文社区深度用户一泽Eze（`@eze_is_1`）与数字生命卡兹克（`@Khazix0918`）、`@object_nullll` 的实战讨论提醒我们（https://x.com/eze_is_1/status/2109850538045264151，https://x.com/Khazix0918/status/2111709708226797737，https://x.com/object_nullll/status/2111717423837778173）：绝不要把对话路由层当成零上下文的裸聊苦力，必须通过清晰的岗位说明书、持久化知识库以及将重度执行任务委派给脚本或 Cloud Agents 的方式，让每一个专职 Bot 各司其职。

待实测在桌面客户端逐个创建 4 个 Bot 并录入对应的岗位说明书 Profile。

## 17.3 周二：频道群聊与安静交接 · Day 2: Group Chat & Quiet Handoffs

周二将四个独立的 Bot 组织进同一个工作群聊。在 Grok Bot 桌面端侧边栏点击新建群聊，勾选已创建的四个 Bot（https://cursor.com/help/grok-bot/chat-and-collaboration）。

> [!NOTE]
> 📸 **截图位（待补）**：侧边栏新建群聊并勾选 4 个 Bot

官方文档明确说明，群聊上限为 2 到 6 个 Bot（https://cursor.com/help/grok-bot/chat-and-collaboration）。将群聊命名为“中文内容工作室”。在这个协作空间里，所有 Bot 可以互相看到彼此的发言并异步流转任务。但必须牢记一个官方安全边界：审批请求、密钥与登录凭证请求、以及邮件或 Slack 的草稿卡片绝不会出现在群聊中，它们只会在对应的单聊中弹出（https://cursor.com/help/grok-bot/chat-and-collaboration）。

> [!NOTE]
> 📸 **截图位（待补）**：工作室群聊频道的成员列表与命名

如果不对 Bot 的交流机制做限制，多 Bot 很容易陷入客套对话刷屏。官方论坛员工回复透露，Bot 在处理每一步时都会重新阅读整个对话上下文，一个忙碌的 Bot 每步可能消耗 8 到 9 万个 Token，其中大约三分之一的轮次纯粹是 Bot 之间互相唤醒（web/forum-1500-week.md）。为了避免无谓的额度消耗，必须在群聊与各个 Bot 的规则中注入**安静交接**指令（web/forum-1500-week.md）：

```text
Only message another bot when it needs to act. No acknowledgments, thanks, or progress pings. Send one summary when the work is done.
```

这条规则要求很直接：只有当下游必须采取行动时才发送消息；严禁回复“收到”“明白”这类客套话；工作完成后只发一条最终总结。

> [!NOTE]
> 📸 **截图位（待补）**：群聊中总编辑向情报员发起首次任务派发

频道建立完毕后，在群聊中发送首次协同指令，范式完全遵循官方的多角色委派规范（https://cursor.com/help/grok-bot/chat-and-collaboration）：

```text
@选题情报员 搜集科技领域最新 3 条公开行业动态，附带原始链接，整理成选题卡。@文案主笔 待选题卡发出后，挑选第一条撰写 1500 字草稿并保存至 /workspace/draft.md。@审校排版员 待草稿完成后，对照原始链接逐条核实数据并列出问题。严禁对外发布。
```

任务进行中人类如果需要插手，直接在输入框发送新消息即可，人类消息具有最高优先级并能重定向当前的执行；如果需要立即终止，直接发“Stop now”就能停止作业（https://cursor.com/help/grok-bot/chat-and-collaboration）。

待实测将 4 个 Bot 拉入新建频道群聊并验证首轮任务交接。

### 进阶：用 Pages 打造工作室实时看板（Activity Dashboard）

当你的内容工作室每天并行推进多个选题、或者按 17.1 节扩展到 6 个专职 Bot 时，挨个点开单聊与群聊翻看上下文会迅速陷入“多 Bot 界面混乱（multi-bot UI chaos）”。自 2026 年 10 月 22 日 v0.75.2 版本起，官方正式上线了 **Pages（底层由 `WriteCanvas` / `EditCanvas` / `ReadCanvas` / `ListCanvases` 工具驱动的实时交互画布）**（https://x.ai/changelog/bot，https://x.com/bot/status/2112991843235610885）。

我们可以直接借鉴社区开发者 Melvin Vivas（`@melvindvivas`）广受好评（获 1,087 赞、1,687 书签）的 **Chief of Staff “Grok Bot Activity Dashboard” 实时看板范式**（https://x.com/melvindvivas/status/2113676935956160882，https://x.com/melvindvivas/status/2113676938820895045，https://x.com/melvindvivas/status/2113968491573514576），让总编辑 Bot 在右侧信息栏的资料库（`Bot info pane → Library`）中创建并长期维护一张全工作室共用的选题与审稿进度看板。

向总编辑 Bot 发送如下指令，即可一键生成并绑定这张实时看板：

```text
请使用 Pages 功能创建并持续维护一个名为“中文内容工作室 · 实时选题与审稿看板（Studio Activity Dashboard）”的交互式页面。
页面需包含以下四个核心模块视图：
1. 【时间线视图（Timeline View）】：按时间倒序展示今日各 Bot（选题情报员、文案主笔、审校排版员、配图员）的关键动作与交接节点。
2. 【进行中任务（Tasks in Progress）】：展示当前正在抓取的信源、正在撰写的草稿文件名（如 /workspace/draft_*.md）及当前责任 Bot。
3. 【已完成任务（Completed Tasks）】：列出今日已通过审校质检的成稿标题、字数、事实核验通过率及本地文件落盘路径。
4. 【等待人工审批事项（Items Waiting for Human Approval）】：高亮列出所有正等待我（负责人）拍板的选题卡、外发请求或最终定稿确认项。

工作规则：将此 Page 作为活文档（living document），每当群聊内完成一次安静交接或状态变更时，直接在原 Page 上热更新数据，不要每次新建页面。
```

生成的 Page 不仅可以在聊天流中点击 **Page card** 随时打开，还会永久沉淀在总编辑 Bot 的 `Bot info pane → Library` 中（https://x.com/bot/status/2112991843235610885）。点击页面右上角的 **Share** 按钮，你可以根据团队规模在三级权限中自由切换：**Only you**（仅自己可见）、**Your team**（团队成员可见，Team 计划管理员可在 `Dashboard → Grok Bot → Bot capabilities` 中管控开关）或 **Anyone with the link**（任何持有链接的人可查看，非常适合发给外部合作编辑或客户预览排期）（https://x.ai/changelog/bot）。

## 17.4 周三：跑通单次任务并固化为 Skill · Day 3: Task to Skill

周三的核心是把临时的对话摸索转变为稳定的可复用资产。社区实战经验总结出**六步测试法**：不要直接写 Prompt 然后挂排程，而必须遵循从任务到修正，再到技能，最后测试与排程的严密路径（https://x.com/Michael_Fenech_/status/2106352565528977469）。官方团队成员在访谈中同样强调，正确的自动化路径是先观察人工或单次任务的执行，将其转化为技能，再挂载为例行程序，逐步建立信任（https://www.youtube.com/watch?v=xZ5TEaleUdg，团队成员访谈）。

> [!NOTE]
> 📸 **截图位（待补）**：单聊中调试微信公众号公开文章抓取

由于国内自媒体无直接插件可用，数据入口主要依赖公开网页 URL（https://xiangyugongzuoliu.com/grokbot-use-cases/）。做法是先在选题情报员的单聊中手动跑一次真实抓取任务，让它打开指定的公开技术资讯网页，提取事实。第一次跑的时候，Bot 可能会抓回大量的页面导航、广告链接或空泛评述。

> [!NOTE]
> 📸 **截图位（待补）**：调试排版核验规则并纠正格式错误

这时要在对话中针对性纠错：剔除公关通稿，只保留提及具体技术变更、数据对比和实际落地案例的事实内容。等它能够稳定输出结构整齐的选题后，要求它将此流程保存为技能（https://cursor.com/help/grok-bot/skills-routines-and-automations）：

```text
把我们刚刚完成的流程保存为名为“中文选题清洗”的技能。包含目标数据源类型、提取字段（标题、原始链接、核心事实、痛点）、去噪规则，以及遇到目标页面 404 或无更新时的处理规则。
```

官方文档规定，一个完备的 Skill 必须明确六个要素：何时使用、所需输入与权限、执行顺序、如何验证结果、输出格式，以及哪些动作必须经过审批（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

> [!NOTE]
> 📸 **截图位（待补）**：将调试成功的流程保存为 Private Skill

接着为审校排版员沉淀“中文排版与合规质检”技能。通过指令录入明确的排版标准：

```text
把排版审查流程保存为名为“中文排版与合规质检”的技能。
规则包括：
1. 检查中英文之间是否有空格，标点符号是否符合中文规范。
2. 核对文中所有技术名词拼写。
3. 扫描是否包含绝对化夸大用词。
4. 验证文内引用的 URL 是否均能在原文中找到对应。
5. 仅输出问题定位与修改建议清单，严禁覆盖原文件。
```

> [!NOTE]
> 📸 **截图位（待补）**：在技能列表中确认私有技能（Marketplace 入口已于 9 月底改为 Connect Apps，以当前界面为准）

私有技能保存后会进入所有 Bot 共享的私有库中（https://cursor.com/help/grok-bot/skills-routines-and-automations）。（注意：v0.68.1 起输入框键入 `/` 不再弹出技能菜单，直接用文字让 Bot 使用该技能即可（https://x.ai/changelog/bot）），键入 `@` 则用于引用其他 Bot、群聊或连接器（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

待实测在单 Bot 对话中跑通选题清洗任务并保存为私有技能。

### 成本与质量双升级：确定性脚本零额度采集 + Grok Imagine 视觉生产

在把单次任务固化为 Skill 时，有两项在 2026 年 10 月中下旬验证成熟的杀手级技巧，能够让内容工作室既省下 95% 以上的采集额度，又直接补齐视觉生产能力：

#### 1. `@StarkLJM` 确定性脚本采集法：28.6 秒写爬虫，每天 1.99 秒零额度抓榜

如果每天都让选题情报员启动云端浏览器、加载 DOM 树并用大模型阅读网页来抓取行业热榜，每周的共享额度池很快就会被掏空。作者 Mr.鼓先生（`@StarkLJM`）在实战中验证了一套 **“AI 一次性写确定性脚本，脚本跑日常轮询”** 的零额度采集范式（https://x.com/starkljm/status/2111803996734419377，https://x.com/starkljm/status/2112818533797343312）：

- **构建耗时与日常运行开销**：首次让 CLI / Bot 编写针对目标榜单的确定性 Python 采集脚本仅耗时 **28.6 秒**；脚本落盘到 `/workspace/scripts/fetch_ranking.py` 后，每天定时触发运行该脚本，仅需 **1.99 秒** 即可完整抓取 30 条榜单数据，且脚本执行过程**消耗 0 模型额度（zero model tokens）**，只有当脚本过滤出高价值异动后才唤醒大模型做摘要。
- **防御性数据清洗铁律（缺失评分存 `null` 绝不存 `0`）**：在 `@StarkLJM` 的脚本规范中（https://x.com/starkljm/status/2112818533797343312），必须写入两条硬性校验规则：第一，一旦目标网页结构改版导致核心字段（如标题、URL）缺失，脚本立即抛出非零退出码并触发告警，绝不静默塞入脏数据；第二，当源数据中某条目暂无评分（rating）或互动数时，必须严格存入 `null`（Python 中的 `None`），**严禁默认填 `0`**，否则后续计算榜单平均分或趋势涨幅时会被 `0` 值严重污染。

你可以让选题情报员将以下确定性采集模板写入 `/workspace/scripts/fetch_ranking.py` 并封装进“中文选题清洗”技能中：

```python
#!/usr/bin/env python3
"""
确定性榜单采集脚本范式（源自 @StarkLJM 实战规范）
日常运行耗时 ~1.99s，纯 Python 标准库实现，0 模型 Token 消耗
"""
import json
import sys
import urllib.request
from datetime import datetime, timezone

REQUIRED_KEYS = ("title", "url", "summary")

def normalize_item(raw: dict) -> dict:
    for key in REQUIRED_KEYS:
        if not raw.get(key):
            raise ValueError(f"[SCHEMA_ALERT] 核心字段缺失: {key}, 原始数据: {raw}")
    # 关键防御规则：缺失评分严格存 None (JSON null)，绝不用 0 污染均值统计
    raw_score = raw.get("score")
    score = float(raw_score) if raw_score is not None and str(raw_score).strip() != "" else None
    return {
        "title": str(raw["title"]).strip(),
        "url": str(raw["url"]).strip(),
        "summary": str(raw["summary"]).strip(),
        "score": score,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }

def main():
    # 示例：读取公开 JSON 榜单接口或解析静态源，落盘至 /workspace/data/daily_top30.json
    print("Ready: 确定性采集完成，缺失评分已安全映射为 null。")

if __name__ == "__main__":
    main()
```

此外，如果云电脑在抓取海外付费财经媒体或国内特定站点时遇到以下两类阻碍，可配合最新特性与社区排错方案解决：
- **突破数据中心 IP 反爬拦截**：若目标网站拦截了云电脑的机房 IP，按照社区开发者 `@XueshiQiao` 的实测方案（https://x.com/XueshiQiao/status/2112866936229183589），在桌面客户端开启 `Settings > Computer > Your computer > Route traffic through this computer`（https://cursor.com/docs/grok-bot/settings），即可借用本机住宅/办公 IP 顺畅抓取。
- **安全授权付费墙会员登录**：若需抓取已订阅的彭博社（Bloomberg）等付费墙内容，无需在聊天窗发密码，可参考 `@oxpsats` 的做法（https://x.com/oxpsats/status/2114207006064365670），通过 v0.75.2 上线的 **1Password Brokered Sign-in**（`Settings → Connect apps → 1Password`）逐次生物识别授权登录（https://cursor.com/help/grok-bot/connect-apps），或存入 v0.75.5 上线的 `Settings → Vault` 内置加密保险箱（https://cursor.com/help/grok-bot/secrets）。
- **防止 Skill 自迭代膨胀**：正如 `@eze_is_1` 在实战复盘中所强调的（https://x.com/eze_is_1/status/2109850538045264151），如果允许 Bot 在每次执行后自动往 Skill 里追加避坑规则，每隔一两周必须让总编辑对 Skill 文件做一次合并去重，防止指令前后冲突、越写越臃肿。

#### 2. 融入 v0.71.2 Grok Imagine 生图、生视频与代码动效 Skill

自 2026 年 10 月 14 日 v0.71.2 版本起，Grok Bot 原生支持直接调用 **Grok Imagine**（底层工具 `GenerateImage`、`GenerateVideo`）在对话中生成与编辑配图和视频，同时支持在云电脑上用代码（Remotion / Canvas / FFmpeg）渲染严丝合缝的动态图形（Motion Graphics）视频（https://x.ai/changelog/bot，https://x.com/bot/status/2110566041772617908，https://x.com/bot/status/2110772748805194127）。

我们可以为文案主笔（或 6 人编制中的配图制作 Bot）沉淀一个名为“中文配图与动效生产”的私有 Skill：

```text
把视觉素材制作流程保存为名为“中文配图与动效生产”的技能。
执行规则：
1. 读取 /workspace/draft.md 成稿，提炼 1 张 16:9 公众号/X 文章封面图方案与 2 张正文核心概念插图方案。
2. 优先调用内置 Grok Imagine（GenerateImage）生成高质感封面图；若涉及数据对比、架构演进或时间线，调用 GenerateVideo 或在云电脑中使用代码渲染 5-10 秒 MP4 动态信息图（保存到 /workspace/assets/）。
3. 若只需修改视频中某一个单镜头，局部替换重渲染该镜头即可，不要全片推倒重跑。
4. 将生成的图片与视频路径追加到草稿末尾的【视觉素材清单】中，交由审校排版员一并核验。
```

## 17.5 周四：配置 Routine 与审批边界 · Day 4: Scheduling Routines & Boundaries

周四将跑通的技能挂载到定时任务中。配置例行程序时，必须严格遵守官方的**排程硬性限制**：每个 Bot 最多拥有 50 个 Routine，每个 Routine 仅保留最近 20 次运行记录，且排程间隔至少需相隔 5 分钟（https://cursor.com/help/grok-bot/skills-routines-and-automations）。删除 Routine 是即时且无法撤销的操作（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

同时，在高频运行频率配额上，2026 年 10 月 22 日发布的 **v0.75.2 版本对 Routine 小时级运行上限进行了大幅扩容**（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/routines）：目前最新官方配额标准为 **全账号所有 Bot 合计最高 300 次/小时（300 runs per hour across all Bots）**，且 **单条 Routine 最高可执行 200 次/小时（200 runs per hour for a single Routine）**（定时触发 Schedule 的最小时间间隔仍为 5 分钟，但通过邮件或 Webhook 事件触发的 Routine 可在突发高峰期享受单条 200 次/小时、全局 300 次/小时的高并发吞吐能力）。此外，v0.75.2 还优化了 Auto-review 审批弹窗逻辑，对当前对话轮次中用户已明确下令执行的操作大幅精简了冗余的二次确认卡片（https://x.ai/changelog/bot）。

> [!NOTE]
> 📸 **截图位（待补）**：总编辑 Bot 的 Routine 新建窗口与参数填写

参考社区验证过的 Routine 提示词结构，一条健壮的自动化指令必须写清时间与时区、数据源与时间窗口、过滤规则、输出字段、投递渠道、严禁动作，以及数据缺失时的保底策略（https://x.com/rowancheung/status/2108328114552000842）：

```text
每个工作日上午 8:30（Asia/Shanghai 时区），针对预设的科技动态公开资讯源，运行“中文选题清洗”技能。
只保留过去 24 小时内发布的更新，过滤掉产品通稿与促销信息，筛选出最多 3 条最具实操价值的线索。
为每条线索提供：标题、原始链接、一句话核心事实、受众痛点分析。
将整理好的选题卡直接发送到“中文内容工作室”群聊中。
严禁向外部平台发布或发送任何消息。
保存为名为“早间选题雷达”的 Routine。
如果数据源无法访问或无新内容，发送一行文字说明情况，不要使用陈旧数据。
```

> [!NOTE]
> 📸 **截图位（待补）**：情报员 Bot 触发的早间选题 Routine

在总编辑 Bot 上同样挂载一个晚间复盘 Routine：

```text
每个工作日下午 18:00（Asia/Shanghai 时区），检查 /workspace/ 目录下今日生成的成稿与审校报告。
提取文案主笔与审校排版员的交付结果，生成一份包含字数、审核修改项与待确认事项的日报卡片。
直接在当前会话中向我汇报。
严禁执行任何外部接口调用。
保存为名为“晚间进度汇总”的 Routine。
```

> [!NOTE]
> 📸 **截图位（待补）**：主笔 Bot 生成的待确认成稿草稿卡片

官方文档提示，长时间离开电脑时，Grok Bot 可能会询问是否继续运行 Routine，若无响应则会暂停以控制无人值守时的用量（https://cursor.com/help/grok-bot/skills-routines-and-automations）。创建完 Routine 后，必须使用“Test run”功能进行测试（https://cursor.com/help/grok-bot/skills-routines-and-automations）。

> [!NOTE]
> 📸 **截图位（待补）**：审校员 Bot 拦截违规用词并触发的审批卡

需要注意，测试运行会真正操作网页和文件，遇到涉及写入、发送等高风险边界时，系统会弹出审批卡（https://cursor.com/help/grok-bot/skills-routines-and-automations）。在后台运行的审批卡约 10 分钟后会自动显示过期并不再执行动作（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。

待实测为选题情报员配置工作日早间 Routine 并执行 Test run 验证审批停顿。

### 进阶：用专属邮箱 `+alias` 加号后缀精准分流触发 Routine

除了固定钟点的定时任务（Schedule），内容工作室经常需要根据外部邮件事件实时启动流水线——比如订阅的海外 AI 通讯周报（Newsletters）到达、读者投稿邮件、或者外部合作方发来的审稿批注。如果在 Bot 的主邮箱上配置“收到任何邮件都触发 Routine”，垃圾邮件和验证码会瞬间造成误触发与额度浪费。

2026 年 10 月 14 日（v0.71.2），Grok Bot 工程师 Sam Sokolin（`@SamSokolin`）正式宣布每个 Bot 的 `@mail.grokbot.com` 专属邮箱支持 **`+alias` 加号子别名**，并支持设置 **仅当邮件发送到指定 `+alias` 后缀时才触发对应的 Routine**（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/agent-email，https://x.com/SamSokolin/status/2110496237241667621）。

假设你为总编辑或选题情报员分配的基础邮箱是 `studio@mail.grokbot.com`，你可以像社区用户 `@songsong275452`（引用 `@gokul_i`）与 `@AIShovelLab` 推荐的那样（https://x.com/songsong275452/status/2113108916229886371，https://x.com/AIShovelLab/status/2113123121070817421），零成本衍生出多个正交的业务触发入口：

- `studio+brief@mail.grokbot.com`：**突发选题快讯通道**。当你在外面看到一篇深度长文或内部报告，直接转发到 `studio+brief@mail.grokbot.com`，立即触发“突发快讯拆解” Routine，让选题情报员提取核心事实并更新到 `Activity Dashboard` Page。
- `studio+newsletters@mail.grokbot.com`：**海外通讯订阅专用桶**。把 Substack、行业周报全部用这个别名订阅，个人主邮箱彻底清净，并配置每周六运行的 Routine 汇总成一份结构化周报素材库。
- `studio+review@mail.grokbot.com`：**外部审稿回传通道**。只接收合作方发回的审校修改意见，触发审校排版员进行版本比对。

配置 `+alias` 邮件触发 Routine 的指令示例如下：

```text
新建一条邮件触发的 Routine，命名为“突发线索加急立项”。
触发条件：仅当收到发送至子别名 studio+brief@mail.grokbot.com 的邮件时触发（忽略发送到主邮箱或其他后缀的邮件）。
执行动作：
1. 提取邮件正文、内嵌图片及附件中的核心事实与原始链接。
2. 调用“中文选题清洗”技能生成加急选题卡，保存在 /workspace/inbox/ 目录。
3. 在“中文内容工作室”群聊中 @文案主笔 与 @总编辑，并将该线索同步写入 Studio Activity Dashboard Page 的【等待人工审批事项】一栏。
4. 严禁自动对外回复邮件或直接发布内容。
```

## 17.6 周五：微信下发与多端联调 · Day 5: WeChat Delivery & Mobile Checks

周五搭建向移动端推送成稿的通知通道。对于中国用户，社区普遍采用基于微信 ClawBot 或 iLink 接口的 Webhook 转发方案（https://chaojifeng.me/free-courses/grok/learn/wechat-02，https://ele.ac.cn/2171/）。

> [!NOTE]
> 📸 **截图位（待补）**：云电脑中运行微信中继程序的终端窗口

微信接入方案属于第三方中继机制，微信侧要求 iOS 8.0.70 及以上、Android 8.0.69 及以上（https://ele.ac.cn/2171/）。KinGao 的接入教程发出后很多群友跑通了，他说"不会封号，因为用的是微信官方接口"，但这只是作者观点，未经腾讯确认（https://x.com/KinGao476942/status/2108171436213104836）。在云电脑上部署中继程序后扫码绑定，登录会话窗口约五分钟（教程特意说明这不保证所有二维码都一样）；遇到会话过期错误 -14 时不要盲目重试，应重新登录；云电脑重启后要有恢复中继进程的办法（https://chaojifeng.me/free-courses/grok/learn/wechat-02）。

> [!NOTE]
> 📸 **截图位（待补）**：扫码完成后的终端凭证状态显示

在总编辑 Bot 上配置一个用于下发消息的 Webhook Routine，将审校通过的文章摘要推送到个人微信。但必须践行**草稿优先原则**：只向微信推送待人工确认的预览卡片与审核摘要，绝对不要接入自动发布接口（https://juejin.cn/post/7682695577956483091）。

> [!NOTE]
> 📸 **截图位（待补）**：主笔 Bot 将成稿通过 Webhook 推送到微信端

下发消息提示词配置如下：

```text
当审校排版员完成当日草稿的最终核验后，提取文章标题、大纲摘要及审核评分。
将上述信息格式化为纯文本简报，调用本地中继接口发送至绑定的微信通知通道。
消息末尾明确注明：“草稿已保存在云电脑 /workspace/final_draft.md，请人工登录后台排版发布”。
严禁携带发布指令，严禁直接上传至任何公众号后台。
```

> [!NOTE]
> 📸 **截图位（待补）**：移动端 Grok Bot 接收到的草稿审批通知

官方 Grok Bot 移动端（iOS 与 Android）同样支持查看卡片、听取语音备忘以及直接执行审批（https://cursor.com/help/grok-bot/chat-and-collaboration）。当 Bot 生成外发请求或草稿卡片时，手机端会同步收到通知，负责人可以直接在手机上点击确认或驳回（https://cursor.com/help/grok-bot/chat-and-collaboration）。

待实测在云电脑启动微信中继程序并检验初稿 Webhook 接收。

### 移动端体验跃升：iPhone Action Button 一键语音审稿下令与原样富文本邮件交付

除了被动接收微信 Webhook 通知，2026 年 10 月中下旬上线的多项移动端与邮件重磅更新，让工作室主理人在通勤、散步或外出时，能够实现“零打字盲按审稿”与“富文本成稿无损转发”：

#### 1. iPhone Action Button 侧边按钮一键语音审稿与派单

自 2026 年 10 月 19 日（Grok Bot iOS 客户端 **v1.16 及以上版本**）起，在配备操作按钮（Action Button）的 **iPhone 15 Pro 及后续机型**上，长按手机侧边按钮即可直接呼出与 Grok Bot 的实时语音通话（Live Voice Chat），全程无需解锁屏幕打开 App 或手动打字（https://cursor.com/help/grok-bot/voice-chat，https://cursor.com/help/grok-bot/mobile，https://x.com/bot/status/2112246033178968161，实机演示可参考 `@SawyerMerritt`：https://x.com/SawyerMerritt/status/2112252980015579431）。

对于内容工作室主理人，你可以按照官方指南配置以下两种高效模式（https://cursor.com/help/grok-bot/voice-chat）：
- **直连总编辑模式**：进入 iPhone 系统 `Settings → Action Button → Shortcut → Choose a Shortcut → Grok Bot → Start Voice Chat`（或通过 iOS **Shortcuts 快捷指令** App 添加 `Start Voice Chat with Bot` 动作并固定绑定“总编辑” Bot，也可设置为 `Ask Each Time` 每次弹窗选择目标专职 Bot）。
- **随身免提审稿工作流**：正如社区创作者 `@D__cup`（佩戴韶音骨传导耳机 + Action Button 全天候免提调度，https://x.com/D__cup/status/2114211130365358350）与 `@TyeInBloom`（结合 v0.75.2 新增的 iOS 原生日历 Calendar、提醒事项 Reminders 与通讯录 Contacts 直读权限，https://x.com/TyeInBloom/status/2113767679588770271）所实践的那样——当你在路上收到成稿通知（自 v0.71.2 起，iOS 与 Android 推送通知已支持 Deep-link 直接跳转至触发通知的具体那个 Bot 聊天窗口，https://x.ai/changelog/bot），只需按一下侧边 Action Button 口述：*“总编辑，刚推送的那篇草稿我看了，把第二小节的案例换成昨天抓到的那条开源项目数据，让配图员补一张架构对比图，改完把定稿发我邮箱，并在我手机日历今晚 8 点建个发布提醒。”*
- **挂断即归档执行**：需要注意，群聊（Group Chats）内不支持直接发起语音通话，同一时间仅限一个活跃语音通话（https://cursor.com/help/grok-bot/voice-chat）。当你与总编辑 1 对 1 语音通话挂断的瞬间，聊天流会自动生成一张包含通话时长与完整逐字稿（full transcript）的 **Voice chat card（语音通话卡片）**，总编辑 Bot 会立即在后台向群聊中的主笔、配图员派发修改指令（https://cursor.com/help/grok-bot/voice-chat）。

#### 2. v0.75.2 邮件原样保留 HTML 排版、内嵌图片与附件转发

对于习惯在邮箱或电脑端审阅带图排版成稿的负责人，或者需要将外部含图简报原封不动转交给工作室的场景，2026 年 10 月 22 日发布的 **v0.75.2 版本正式支持邮件原样转发（保留完整 HTML 格式、正文内嵌图片 inline images 以及文件附件）**（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/agent-email）。

这意味着当总编辑或审校排版员通过 `@mail.grokbot.com` 专属邮箱（或已连接的外部邮箱）向你的工作邮箱交付最终成稿包、或者转发外部带图行业报告时，不再会被压平为丢失排版的纯文本——HTML 样式表、文内插图以及作为附件打包的 `.md` 源码与高清配图均能 100% 原样送达，打开邮件即可直接复制粘贴至公众号排版器或知乎/X 后台。

## 17.7 周末：用量复盘与淘汰审计 · Weekend: Usage Review & Pruning

周末是对整套系统进行成本核算与清理的时间。无论使用何种订阅，必须对额度机制保持清醒。官方规则显示，Cursor Pro（20 美元/月）、Pro+（60 美元/月）、Ultra（200 美元/月）和 Teams（40 美元/人/月）均包含 Grok Bot 用量（https://cursor.com/help/grok-bot/plans，https://cursor.com/pricing）。SuperGrok、SuperGrok Plus、SuperGrok Heavy 和 X Premium+ 也可关联获得用量，自助开通的 Grok Business 席位也能用，但 SuperGrok Lite 不包含（https://cursor.com/help/grok-bot/plans）。SuperGrok 约 30 美元/月是第三方评测给出的价格，官方帮助页不写价格。两边用量不叠加，关联后无法解绑或转移，且具体每周用量额度数字官方未公布（https://cursor.com/help/grok-bot/plans）。

### 2026-10 最新计费口径校准：The X Subscription 三合一共享周额度池与 Prepaid Credits 核算

自 2026 年 10 月 18 日起，官方正式推出 **The X Subscription 三合一统一订阅计划**，将 **Grok**、**Cursor** 与 **X Premium** 整合为单一订阅（https://cursor.com/help/grok-bot/plans，https://cursor.com/cn/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview，https://x.com/bot/status/2110063783796572496）。在做周末成本复盘时，工作室负责人必须按你当前所处的订阅轨道精准对账：

1. **The X Subscription 三合一订阅档位与准入边界**：
   - **包含 Grok Bot 的三个档位**：**Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）**（https://cursor.com/help/grok-bot/plans）。正如社区研究者 `@wenser2010` 与 `@chuyang_ai` 所分析的（https://x.com/wenser2010/status/2113683422409572523，https://x.com/chuyang_ai/status/2111357749103911004），$30/月的 Premium 档位一次性打包了 X Premium、Cursor 与 Grok Bot，是搭建个人内容工作室极具性价比的起步档位。
   - **不包含 Grok Bot 的档位**：**Free（$0）** 与 **Plus（$8/月）** 档位不包含 Grok Bot 使用权限（https://cursor.com/help/grok-bot/plans）。
   - **旧版独立订阅（Legacy Plans）保留与单向不可逆切换规则**：既有的独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）以及自助式 Teams（$40/人/月）老订户，只要不主动迁移，仍可保留原档位与独立额度规则；老订户随时可通过 `https://cursor.com/unify`（或 `https://accounts.x.ai/unify`）合并升级至 The X Subscription，网页直付的旧订阅会自动按剩余天数比例退款（prorated refunds，但**通过 Apple App Store 或 Google Play 订阅的用户必须手动前往手机系统订阅页取消旧计划，否则会遭遇双重扣费**）；且务必注意：**一旦切换至 The X Subscription，操作不可逆，无法退回旧版独立 Cursor 订阅计划**（https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview）。
2. **三端共享周额度池（One Weekly Usage Pool）与掉电排查**：
   - 在 The X Subscription 下，Grok Bot 不再使用隔离的额度池，而是与 **Grok 网页/App**、**Cursor IDE** 三端**共享同一个周额度池**（每周固定重置，未用完额度不结转）（https://cursor.com/help/grok-bot/plans）。
   - 社区用户 `@charlie_pmp` 在复盘中一针见血地指出（https://x.com/charlie_pmp/status/2114214503416271131）：很多人在升级三合一订阅后觉得工作室 Bot 周额度掉电变快，原因正在于 **Cursor 写代码 + Grok 日常对话 + Grok Bot 后台高频 Routine 三端同时在从同一个池子抽水**。
3. **超额消费机制变革：Prepaid Credits（预付额度）替代后付费账单**：
   - 在 The X Subscription 体系下，当每周包含额度耗尽、或在 Cursor 中调用非 Grok 系列的第三方模型（third-party models）时，系统将从 **Prepaid Credits（预付额度）** 中扣费，而非生成后付费按需账单（https://cursor.com/help/grok-bot/plans）。
   - 负责人可前往 `https://grok.com/dashboard/billing` 的 `Additional usage credits` 模块充值预付额度，或配置 **Auto Top-up（自动充值）** 与 **Monthly additional usage limit（月度额外消费封顶上限）**；在客户端内则统一通过 `Settings > Usage & Billing` 查看周额度进度条与 Prepaid Credits 剩余余额（旧版后付费 `On-demand monthly limit` 仅适用于未迁移的独立老计划）（https://cursor.com/help/grok-bot/plans）。

> [!NOTE]
> 📸 **截图位（待补）**：Settings 中的 Usage & Billing 页面及重置倒计时

社区帖称 Cursor Pro 订阅下每条消息约消耗 1% 周额度（个例）（https://x.com/miniyarov/status/2105428357273800799）。社区帖称每 5 分钟执行一次的 Routine 每月触发约 8640 次，API 估算约消耗 397 美元（个例）（https://x.com/fleyta88/status/2109346840382415019）。如果在设置中开启了 On-demand 按量付费，容易因高频轮询产生额外费用，因此务必在 Settings → Usage & Billing 中设置明确的月度上限（https://cursor.com/help/grok-bot/plans）。社区帖称把写长代码等重活交给外部工具、Bot 只做调度，Bot 自身的额度消耗从 70% 降到 3%（个例，铁柱AGI 的长文，见 research/zh/weixin/tiezhu-quota-summary.md）。

沿着“Bot 只做轻量调度、重活外包给确定性脚本或低成本 CLI”的思路，社区还沉淀了三套可直接用于内容工作室的进阶省额度方案：
- **云电脑挂载 `pi` + DeepSeek API 承担长文粗加工**：社区开发者 `@hppzyy` 分享了在 Grok Bot 云电脑内安装轻量级 Pi Agent（`pi`）并配置 DeepSeek API Key 的方案（https://x.com/hppzyy/status/2111573227881529454），让总编辑 Bot 只扮演轻量调度员，把海量资讯初筛与长文粗翻译交给命令行里的 `pi` 执行；同时，务必结合 `@37FlowAI` 发现的防卡死技巧（https://x.com/37FlowAI/status/2111334386339823687）——在非交互式 Agent Shell 中调用 CLI 工具时，必须在命令末尾追加 `< /dev/null`（如 `pi -p "提取核心事实" < /dev/null`），立即闭合标准输入（stdin），彻底解决非交互式 Shell 无限期等待 EOF 挂起卡死的顽疾。
- **BDK 本地与云端双向混动 + 共享 Obsidian 知识库**：如果你本地同时订阅了 Claude Code 或 Codex（如 `@frogchan9o1` 推荐的“$20 Claude Code + $30 X Premium 三合一订阅”组合，https://x.com/frogchan9o1/status/2110883156891140416），可以通过 BDK（`cursor-grokbot-agents`）打通本地 CLI 与云端 Grok Bot 的双向调用——正如 `@StarkLJM`（用本地 Claude Code 派单给云端 Grok Bot 渲染 20 秒《上下五千年》中国史动画并返回 2.7 MB 源码包，https://x.com/starkljm/status/2109544938644107411）、`@kangxiaile`（本地写稿写代码时把 X 全网检索外包给拥有免费原生 X 读取能力的云端 Grok Bot，https://x.com/kangxiaile/status/2109752183889744216）以及 `@z_lumia`（https://x.com/z_lumia/status/2113800469571313974）所验证的那样，让本地编码 Agent 与云端工作室共用同一套 Markdown 知识库，各取所长。

> [!NOTE]
> 📸 **截图位（待补）**：Routines 列表中查看最近 20 次运行记录

周末必须执行**淘汰审计**。如果一个定时任务持续运行却从未改变任何现实决策，它就应该被果断停用（https://x.com/kocer_eth/status/2101669438038634827）。

> [!NOTE]
> 📸 **截图位（待补）**：执行 Routine 淘汰审计提示词后的报告输出

向总编辑 Bot 发送如下审计指令，参考社区审计范式（https://x.com/fleyta88/status/2109346840382415019，https://x.com/kocer_eth/status/2101669438038634827）：

```text
对当前工作室所有 Bot 的运行记录和 Routine 进行审计：
1. 列出所有 Routine 的触发次数与实际产出。
2. 统计过去 7 天内，由于源数据无变化而空跑退出的轮次占比。
3. 标出无实质产出或未被我采用的 Routine，指出其中最应该淘汰的一个并说明理由。
4. 给出优化方案并等待我的审批，未经确认不要修改或删除任何配置。
```

正如社区用户所指出的，在自动化体系中，真正产生价值的是例行流程本身，而不是单纯的聊天机器人（https://x.com/i/status/2109516426767654962）。通过一周的规范搭建与周末的及时清理，四个 Bot 才能真正从分散的聊天窗口，演化为一个稳定可信的协作团队。

待实测在 Settings 页面核对一周用量百分比并执行 Routine 审计指令。


# §18 研发场景：Bot + Cursor 云端 Agent + GitHub · Capstone B

> **适合谁**：有代码仓库、会用 GitHub 的开发者或技术负责人。**前提条件**：Cursor 账户可用云端 Agent（Cloud Agents）、GitHub 仓库已连接；Notion 看板和 Private Worker 是可选项。不写代码的读者可以跳过本章，或者只看 18.7 的"人工终审"原则。

## 18.1 研发舰队编制：五位专职 Bot 与一位运维管家 · Engineering Fleet Roster

假设你翻看官方工程指南就会发现，如果试图让一个万能 Bot 既读前端需求、又调后端接口、还顺便修部署脚本，轮次稍微一长，上下文就会被琐碎日志挤爆，前脚定好的架构规范后脚就忘得一干二净。SpaceXSI 工程师 Lingxi Li 给出的解法是**拆分为专职工程师舰队**（https://x.ai/bot/guides/grok-bot-for-engineering）。Grok Bot 的本质是一台带独立电脑的工程实习生，能替你管编码智能体，还会慢慢学你的工作习惯。Lingxi Li 的团队常驻了五位专职工程 Bot：Baltata 管移动端共享层与 iOS、Shaoruru 管桌面端与 CI 流水线、Hogan 管底层基建与权责不明的问题、Craig 管 Android 端、Quill 管测试套件与安全框架（https://x.ai/bot/guides/grok-bot-for-engineering）。

每个专职 Bot 都有独立记忆和有限的上下文窗口，只盯单一领域时，规范抓得最准（https://x.ai/bot/guides/grok-bot-for-engineering）。官方团队公布的数据显示，用这套工作流，Lauren 一个月交付了超过 2000 个 Pull Request；Balta 和 Shaoru 四周内用 Grok Bot 搭出了 Grok Bot 自己的骨架；Lingxi Li 也在三周内单凭 Grok Bot 做完了 iOS 初版（https://x.ai/bot/guides/grok-bot-for-engineering）。官方市场上已经沉淀出可直接导入的模板，包括 Lingxi 的 Engineer Bot、Nightly Audit Engineer，Eric Zakariasson 的 Projects Manager，以及 Cursor 官方的 SWE（https://x.ai/bot/guides/engineering）。

除了写代码的 Bot，编制里最关键的角色是不写业务代码的运维管家 Jenny（https://x.ai/bot/guides/grok-bot-for-engineering）。Jenny 每天清晨 5 点找每位工程 Bot 一对一沟通，对操作手册，排查卡点。哪个 Bot 犯了错，Jenny 就介入做根因复盘，更新规则手册并广播给全员，防止同一个错误犯两次（https://x.ai/bot/guides/grok-bot-for-engineering）。为了防止多 Bot 互相唤醒空耗上下文，工程群聊必须遵守安静交接规范。Cursor 团队员工建议在配置里写死约束：只有需要对方采取行动时才发消息，不许回收到、感谢或琐碎进度报备，任务完成后只发一份最终摘要（https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。

![工程 Bot 编制分工与运维架构（Jenny + 业务工程师 + 专职 Audit）](../images/fig-18-1.png)

*图：工程 Bot 编制分工与运维架构（Jenny + 业务工程师 + 专职 Audit）*

> [!NOTE]
> 📸 **截图位（待补）**：五位专职工程 Bot 与运维 Bot Jenny 的协作群聊与配置文件

## 18.2 从 Issue 到复现包：把 Bug 关进沙箱 · Bug Triage & Reproduction

GitHub 仓库收到新缺陷报告时，直接让大模型进源码库翻找修补，很容易引发代码幻觉。官方用例给出的标准解法是让专门的排查角色先接手，把不可靠的用户反馈转成一份**规范化复现包**（https://cursor.com/help/grok-bot/use-cases）。排查角色需要连上工单系统、预发沙箱、受控浏览器和抓包工具，在受控的临时测试账号下复现问题，严禁碰线上真实客户数据；测试凭据必须走安全审批交接，不能直接贴在聊天框里（https://cursor.com/help/grok-bot/use-cases）。此前社区就发生过在全员群聊里误发密码导致密钥暴露的事故（https://x.com/i/status/2107339523038331338）。

在官方公开的客服与工程联动标杆案例中（https://x.ai/news/grok-bot-customer-support），自 2026 年 8 月 14 日 Cursor 并入 SpaceX SuperIntelligence（SpaceXSI）后，全球用户客服工单量瞬间暴增 175%。官方为此构建了由五位专职 Bot 组成的舰队：Intake Triage Bot（分诊接待 Bot）、Billing & Refund Bot（账单与退款 Bot）、**Technical Repro Bot（技术复现 Bot）**、Incident Batch Bot（事故批处理 Bot）与 Product Feedback Synthesizer Bot（产品反馈聚类 Bot）（https://x.ai/news/grok-bot-customer-support）。其中，**Technical Repro Bot** 专门承接所有疑似代码 Bug 的工单，在独立云沙箱中完成自动化环境还原与最小复现验证，配合 Product Feedback Synthesizer Bot 每天从海量对话中抽取并聚类超过 20,000+ 个产品反馈数据点直接转化为研发工程工单，帮助官方在零新增客服招聘（节省约 200 名人力）的前提下将单票解决成本压降至 $0.20–$0.30（https://x.ai/news/grok-bot-customer-support）。

Grok Bot 设计师 Peng Zheng（`@pengzheng_`）也分享了官方内部设计与工程团队的日常 Bug 分拣复现工作流（[https://x.com/pengzheng_/status/2110245240863178793](https://x.com/pengzheng_/status/2110245240863178793)，86 赞、5 转发、108 书签）：内部团队每天让 Grok Bot 自动盯守反馈渠道与 GitHub Issues，对新上报的 UI 异常或交互缺陷先在云电脑里跑通复现并截屏取证，随后直接拉起 Cursor Cloud Agents 修改代码，最后在沙箱内对比修复前后的 UI 表现完成闭环。

收到缺陷 Issue 后，直接向 Bot 派发官方定义的初始任务提示词：

```text
Read this bug report and reproduce it in staging using a fresh test account. Return exact steps, expected and actual behavior, screenshots, browser and OS details, relevant console or network notes, and a minimal test case if possible. Do not use production customer data.
```

Bot 在沙箱内跑完后，会输出一份包含完整操作步骤、预期与实际表现对比、系统环境参数、控制台报错堆栈和最小复现用例的交付包（https://cursor.com/help/grok-bot/use-cases）。这份材料既是后续编码智能体的输入依据，也是衡量修复是否成功的基准线。

待在实际工程代码库中验证从 GitHub Issue 抓取到生成复现包的完整用时与准确率。

> [!NOTE]
> 📸 **截图位（待补）**：GitHub Issue 详情页与被打上 bug 标签的初始待办

> [!NOTE]
> 📸 **截图位（待补）**：复现专职 Bot 在云电脑沙箱中抓取的报错日志与浏览器控制台

> [!NOTE]
> 📸 **截图位（待补）**：Bot 生成的规范化 Bug 复现包与前后表现对照

## 18.3 调度 Cursor 云端 Agent：提示词与本地 Worker · Cloud Agent Dispatch

工程 Bot 拿到复现包后，自身不用在桌面开编辑器一行行敲代码，而是作为调度者去唤起 Cursor 云端 Agent（https://x.ai/bot/guides/grok-bot-for-engineering）。Lingxi Li 介绍，每个工程 Bot 都能创建 Cursor 云端 Agent、实时读运行转录、审查 PR 附带的测试证据，遇到卡点就排队追加消息或打断重跑，不用工程师在多个 Agent 之间反复切屏盯梢（https://x.ai/bot/guides/grok-bot-for-engineering）。借助这种调度机制，团队能将过去手工管 15 个云端 Agent 的上限拓展到**同时并行管理超过 200 个云端 Agent**（https://x.ai/bot/guides/grok-bot-for-engineering）。

派发编码任务时，工程 Bot 会按具体场景挂载专属技能，比如用于视觉优化的 `/lingxi-design`、用于代码规范审计的 `/react-native-best-practices`、用于架构评审的 `/lingxi-review`，或者用于产品决策的 `/lingxi-product`（https://x.ai/bot/guides/grok-bot-for-engineering）。如果开发环境需要特定内网访问、企业 VPN 或特殊机器配置，官方支持将闲置的 Mac mini 接入为 Cursor Cloud Private Worker。由 Grok Bot 直接调度该本地节点运行云端 Agent，调动本地 iOS 模拟器并回传实时运行截图（https://x.ai/bot/guides/grok-bot-for-engineering）。官方提到，这省掉了过去为了保持环境常驻而在家里专门配置主机跑开源工具的麻烦（https://x.ai/bot/guides/grok-bot-for-engineering）。

Cursor / Grok Bot 产品工程负责人 Eric Zakariasson（`@ericzakariasson`）在 2026 年 10 月 24 日与 10 月 25 日连发两帖（[https://x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099)、[https://x.com/ericzakariasson/status/2114157733276525044](https://x.com/ericzakariasson/status/2114157733276525044)），详解了家用常开 Mac mini 的远程节点注册与 Worker 部署方案：第一，只需在家里常开的 Mac mini 上启动并登录 Grok Bot 桌面端，这台机器就会自动注册到 `Settings > Computer` 设备列表中，此后无论你在外地用手机还是轻薄本向任何云端 Bot 下达指令，Bot 都可以远程在你的家用 Mac mini 上执行本地编译与测试任务；第二，你可以直接在聊天窗口里要求 Grok Bot 在该远程机器上自动配置并启动 `cursor-agent worker` 守护进程，一行手敲配置都不用写即可完成私有算力节点的挂载。

工程 Bot 发起云端编码调度的参考提示词结构如下：

```text
Create a Cursor cloud agent for this reproduction pack. Invoke /react-native-best-practices for code standards. Require proof showing before vs. after screenshots and passing test logs. If the agent hits environment flakiness, send a follow-up to unblock it immediately.
```

除了由云端 Grok Bot 向下调度 Cloud Agent 与本地 Mac mini，2026 年 10 月中旬起社区全面跑通了基于 **BDK（Bot Developer Kit）与 `cursor-grokbot-agents` 技能**的**跨端双向调用架构**：让运行在本地电脑上的编码 Agent（Claude Code、Codex、Cursor IDE）与云端 Grok Bot 互相派单、各展所长：

1. **本地 CLI 向云端 Grok Bot 派发多媒体与全网检索重任（`@StarkLJM` & `@kangxiaile`）**：作者 Mr.鼓先生（`@StarkLJM`）在实战教程（[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411)）中演示了如何通过 BDK（`cursor-grokbot-agents`）打通本地终端里的 Codex / Claude Code 与云端 Grok Bot——当本地 Claude Code 负责主工程编写时，直接向云端 Grok Bot 下发“制作一段 20 秒《上下五千年》中国历史线条画动画短片”的子任务，云端 Grok Bot 在沙箱中独立完成分镜绘制与视频合成，直接向本地返回渲染好的 `0:20` MP4 视频卡片与 `2.7 MB` 的完整源码压缩包。开发者 `@kangxiaile`（康熙AI了，[https://x.com/kangxiaile/status/2109752183889744216](https://x.com/kangxiaile/status/2109752183889744216)）则利用 Grok Bot 独有的免费原生 X 检索优势，构建了“本地 Claude Code 写代码遇到新库或舆情需求 → 派单给云端 Grok Bot 搜索 X 全网最新实测帖 → Grok Bot 整理成结构化 Markdown 传回本地 → Claude Code 读取后继续写代码”的闭环。
2. **三合一订阅下的双向互调与六大联动范式（`@z_lumia` & `@AIShovelLab`）**：`@z_lumia`（x白，[https://x.com/z_lumia/status/2113800469571313974](https://x.com/z_lumia/status/2113800469571313974)）在开通 The X Subscription 三合一订阅后打通了完整双向链路：本地的 Claude Code 和 Codex 随时发消息向云端 Grok Bot 调取长期记忆与全网调研报告；反过来，云端 Grok Bot 也能直接下发指令在本地台式机上执行 CLI 命令。`@AIShovelLab`（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）则将这套 Grok Bot + Claude Code / Codex 组合拳总结为六大核心联动范式：用路由 Skill 阻止盲目重试、本地与云端双向聊天派单、语音随身派活、Cloud Agent 并发执行、单 Bot 端到端内容流水线，以及利用 `+alias` 邮箱后缀精准触发 Routine（v0.75.2 起 Routine 频率上限已提升至全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时，定时最小间隔为 5 分钟，详见 https://cursor.com/help/grok-bot/routines）。
3. **4 次 API 调用纯标准库 Python 脚本绕过 Webhook 400 报错（`@mikan77_aoi`）**：当本地工具或外部服务向 Grok Bot 的 Webhook 推送复杂代码或长 JSON 载荷时，常常会因为格式校验严格而遭遇 HTTP 400 报错。`@mikan77_aoi`（橘子🍊，[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）编写了一个零外部依赖、零守护进程（zero-daemon）的纯 Python 标准库（`urllib.request` + `json`）桥接脚本，仅通过 **4 次 API 调用**（鉴权获取会话 → 创建/定位目标 Bot 线程 → 投递结构化任务指令 → 拉取执行回执）就能让本地 Claude Code 绕过 Webhook 限制，稳定地将任务交接给云端 Grok Bot：

```python
#!/usr/bin/env python3
"""Zero-dependency stdlib bridge: Local Claude Code / CLI -> Cloud Grok Bot (4 API calls)"""
import json, os, sys, urllib.request

API_BASE = os.environ["GROKBOT_API_BASE"]      # e.g. https://cursor.com/api/bot/v1
API_TOKEN = os.environ["GROKBOT_API_TOKEN"]
BOT_ID = os.environ["GROKBOT_TARGET_BOT_ID"]

def api_call(method: str, path: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=data,
        headers={"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"},
        method=method,
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def handoff_to_grokbot(task_prompt: str) -> dict:
    # Call 1: Verify bot status & session context
    bot_info = api_call("GET", f"/bots/{BOT_ID}")
    # Call 2: Create a fresh isolated conversation thread to avoid context bloat
    thread = api_call("POST", f"/bots/{BOT_ID}/threads", {"title": task_prompt[:60]})
    thread_id = thread["id"]
    # Call 3: Dispatch structured task message
    msg = api_call("POST", f"/threads/{thread_id}/messages", {"text": task_prompt})
    # Call 4: Poll / fetch initial run receipt
    return api_call("GET", f"/threads/{thread_id}/runs/{msg['run_id']}")

if __name__ == "__main__":
    print(json.dumps(handoff_to_grokbot(sys.stdin.read().strip()), ensure_ascii=False, indent=2))
```

4. **云电脑内安装 Codex CLI + 完成时 Webhook 唤醒实现零轮询耗电（`@AbhisheKumarA7`）**：除了调用外部机器，开发者 `@AbhisheKumarA7`（Abhishek Kumar，[https://x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578)）展示了另一种极客解法——直接在 Grok Bot 的云电脑（cloud computer）内部安装 Codex CLI，并配置一条任务完成时的 **Webhook**。当耗时漫长的重度代码构建与重构任务在后台跑完时，由脚本主动触发 Webhook 唤醒 Grok Bot 验收交付，全程**零轮询（zero polling token waste）**：

```bash
# Run heavy coding task in cloud box background & wake Grok Bot via Webhook only on completion
nohup bash -c '
  codex exec --full-auto "Refactor auth module and run full pytest suite" < /dev/null > /tmp/codex_run.log 2>&1
  EXIT_CODE=$?
  curl -sS -X POST "$GROKBOT_ROUTINE_WEBHOOK_URL" \
    -H "Content-Type: application/json" \
    -d "{\"event\":\"codex_done\",\"exit_code\":$EXIT_CODE,\"log_path\":\"/tmp/codex_run.log\"}"
' >/dev/null 2>&1 &
```

待验证本地 Mac mini 配置为 Private Worker 后的 iOS 模拟器截图回传延迟。

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 对话流中调用 Cursor Cloud Agent 的派发指令与参数卡片

> [!NOTE]
> 📸 **截图位（待补）**：Cursor Cloud Agent 实时运行转录（Transcript）与命令执行输出

> [!NOTE]
> 📸 **截图位（待补）**：云电脑 Private Worker（本地 Mac mini）运行 iOS Simulator 的实时画面

## 18.4 Opus 5.5 路由与多模型分工栈 · Opus 5.5 Routing & Model Stack

研发流程中若让高单价模型全程跑格式化或编译报错轮询，额度很快就会耗尽。2026 年 10 月 7 日，Elon Musk 在 X 上公开宣布，Grok Bot 正在接入竞争对手的顶尖模型作为后端，包括 Anthropic 的 Claude Opus 5.5、Midjourney 与 Suno 等接口，根据具体任务的达成概率动态选择最适配的模型（https://x.com/elonmusk/status/2107724314451878104；报道见 https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk）。Musk 当时并未公开各类任务具体如何分发到外部模型的规则（https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk）。

为什么必须在“对话路由层”与“重度编码执行层”之间划清界限？中文社区关于 Grok Bot 真实体验的一场高赞争鸣揭示了底层原因：博主 `@Khazix0918`（数字生命卡兹克，[https://x.com/Khazix0918/status/2111709708226797737](https://x.com/Khazix0918/status/2111709708226797737)，285 赞、4 转发、54 书签）吐槽如果直接把默认聊天窗口当成重度苦力裸用，常会遇到默认路由的轻量对话模型“不思考、张嘴就来、查都不查直接回复”的问题；对此，开发者 `@object_nullll`（[https://x.com/object_nullll/status/2111717423837778173](https://x.com/object_nullll/status/2111717423837778173)）一针见血地给出了架构解答：**Grok Bot 的对话层（conversational layer）设计初衷是收集上下文、对齐验收标准、编写结构化 Prompt，并将重度执行任务委派给 Cursor Cloud Agents（`CloudAgent`）或云电脑上的 CLI Workers，绝不能把轻量对话路由模型当成直接写复杂代码的苦力**。开发者 `@realbenzh`（Ben Zhang，[https://x.com/realbenzh/status/2111295936635015631](https://x.com/realbenzh/status/2111295936635015631)）的飞书 + Linear + 邮箱研发流正是这一原则的写照：先把飞书（Feishu）、Linear、电子邮箱和团队文档全部接入 Grok Bot 汇总完整业务上下文，在聊天窗里与 Bot 对齐交付目标和验收标准（acceptance criteria），随后让 Grok Bot 通过 CLI 交互式驱动 `@orca_build` 完成重度构建交付。

在实际研发分工上，社区开发者摸索出一套**多模型分层协作栈**（https://x.com/i/status/2101944767412129920）。在日本开发者的工作流中，先由 Grok Bot 负责网络调研与架构规划，再交由 Claude Code 进行编排，核心开发由 Cursor Projects 承接，日常杂务继续交由 Grok Bot 推进（https://x.com/i/status/2101944767412129920；另见 https://x.com/i/status/2103438409553604976）。在 Opus 5.5 支持接入后，社区帖称（个例，https://x.com/i/status/2109300337203183940）分工模式可细化为：Grok Bot 充当工作助理与架构拆解者，Opus 5.5 负责攻克算法难点与前端交互实现，Sonnet 5.5 负责编写单元测试与集成测试；另一社区帖称（个例，https://x.com/i/status/2108990316644847920）由 Bot 拆分工单后让 Opus 解决重难点，轻量模型处理常规修补，没有人工审批绝不自动合入。发起任务时，社区帖称（个例，https://x.com/i/status/2109265867859177552）可直接通过指令呼叫：

```text
Use Cursor cloud agent with Opus 5.5 to implement the core logic for this issue. Keep auxiliary tests and style checks on standard models. Do not merge until human review is complete.
```

更有甚者，开发者 `@kaelanyiu`（Kaelan Yiu，[https://x.com/kaelanyiu/status/2114213605566742884](https://x.com/kaelanyiu/status/2114213605566742884)）搭建了一个每隔几天自动跑分动态选型的**“模型评测元 Bot（Meta-Evaluator Bot）”**：该 Bot 定时对当前各大前沿大模型运行一轮真实业务代码基准测试，并根据实测得分动态修改其他干活 Worker Bots 在未来几天内通过 CLI 调用的底层模型配置，实现模型路由的优胜劣汰。

需要特别注意的计费边界是：在官方于 2026 年 10 月 18 日推出的 **The X Subscription 三合一统一订阅**（Premium $30/月、Super $100/月、Ultra $200/月，详见 https://cursor.com/help/grok-bot/plans 与 https://cursor.com/help/the-x-subscription/overview）体系下，Grok Bot、Grok 与 Cursor 共享同一个包含在套餐内的 Grok 周额度池；但**当你在 Cursor 或 Cloud Agent 中调用非 Grok 系列的第三方模型（如 Claude Opus 5.5 / Sonnet 5.5 等）时，会直接扣减你在 `grok.com/dashboard/billing` 中充值的 Prepaid Credits（预付额度），而不会消耗套餐内的 Grok 周额度池**（https://cursor.com/help/grok-bot/plans）。

待实际调用 Cursor 云端 Agent 并观测是否成功路由至 Opus 5.5 及其单次 PR 额度消耗。

![Opus 5.5 与多模型分工栈拓扑（Grok Bot 架构 → Opus 5.5 编码 → Sonnet/快模型 测试）](../images/fig-18-2.png)

*图：Opus 5.5 与多模型分工栈拓扑（Grok Bot 架构 → Opus 5.5 编码 → Sonnet/快模型 测试）*

> [!NOTE]
> 📸 **截图位（待补）**：后台模型路由面板中调用 Claude Opus 5.5 的请求记录

## 18.5 自动化闭环：视觉比对、Notion 看板与代码审查 · Feedback Loop & Review

编码智能体把代码写完只是流水线的前半程，没有严格反馈闭环的自动化只会带来大量垃圾变更。Lingxi Li 强调，维系工程 Bot 团队运转的核心是**给予完整的反馈闭环**（https://x.ai/bot/guides/grok-bot-for-engineering）。云端 Agent 可以截取屏幕图像，Grok Bot 则利用其多模态能力核验界面改动是否符合要求。视觉呈现与预期不符时，Bot 会直接驳回并督促 Agent 重新修改（https://x.ai/bot/guides/grok-bot-for-engineering）。官方团队甚至将 SpaceXSI 的语音 API 接入云端 Agent 的系统音频输入输出，利用语音信号与转录文本自动化测试端到端语音交互能力（https://x.ai/bot/guides/grok-bot-for-engineering）。环境偶发波动导致 Agent 停滞时，工程 Bot 会主动介入纠偏（https://x.ai/bot/guides/grok-bot-for-engineering）。

为了突破单次上下文窗口的限制，也让人无需翻阅漫长聊天记录即可掌握全局进展，团队设置所有工程 Bot 共同维护一个共享 Notion 数据库看板（https://x.ai/bot/guides/grok-bot-for-engineering）。每隔 30 分钟，工程 Bot 会轮巡一次数据库，对其中的每个 Pull Request 执行三项硬性检查：验证 Bugbot 评论与安全扫描结果是否属实、检查 CI 流水线是否报错、排查合并冲突（https://x.ai/bot/guides/grok-bot-for-engineering）。一旦发现异常，Bot 立即向云端 Agent 发送纠错指令，并将 Notion 看板上的状态重置回进行中；三项检查全部通过后，任务状态切为待评审，并自动触发代码审查（https://x.ai/bot/guides/grok-bot-for-engineering）。审查评估置信度极高且影响范围很小的 PR 会被自动合并；一旦涉及关键变动，则等待工程师人工复核（https://x.ai/bot/guides/grok-bot-for-engineering）。

随着 2026 年 10 月 22 日官方 **v0.75.2** 版本正式推出原生 **Pages（Canvas）** 功能（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)；官方发布帖见 [https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)，6,544 赞、567 转发、2,008 书签），研发团队除了使用外部 Notion 数据库外，还可以直接让主控工程 Bot 在客户端内部创建并维护一张实时热更新的 **研发冲刺看板 Page（底层由 `WriteCanvas` / `EditCanvas` 驱动）**。该看板常驻于对应 Bot 右侧信息栏的 **Library（资料库）** 中，支持设置 `Only you`、`Your team`（团队管理员可在 `Dashboard → Grok Bot → Bot capabilities` 中统一管控）或 `Anyone with the link` 三级分享权限（https://x.ai/changelog/bot）。参照社区开发者 `@melvindvivas` 打造的幕僚长 `Activity Dashboard` 范式（[https://x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882)，1,087 赞、1,687 书签；提示词拆解见 [https://x.com/melvindvivas/status/2113676938820895045](https://x.com/melvindvivas/status/2113676938820895045)），你可以要求所有专职工程 Bot 在推进 Issue 复现、Cloud Agent 编码与 PR 审查时同步更新同一张 Page 的四大视图：**时间线视图（Timeline view）**、**进行中任务（Tasks in progress）**、**已完成任务（Completed tasks）** 以及 **等待人工合并审批的 PR（Items waiting for human approval）**。

此外，如果你采用“本地 Claude Code + 云端 Grok Bot”双栈协同，还可以使用社区验证的**共享 Obsidian Vault 工程日志方案**。继 `@itsvlady`（Vlady，[https://x.com/itsvlady/status/2110803638671020277](https://x.com/itsvlady/status/2110803638671020277)，352 赞、55 书签）晒出重度 Vibe-Coder 的月度双栈账单（$120 Claude Code + $55 Grok Bot）后，开发者 `@frogchan9o1`（[https://x.com/frogchan9o1/status/2110883156891140416](https://x.com/frogchan9o1/status/2110883156891140416)）分享了一套极具性价比的“$20 Claude Code + $30 The X Subscription Premium”架构：让本地 Claude Code 与云端 Grok Bot **共用同一个 Obsidian Vault 知识库目录**，将每一次 Bug 排查报告、架构决策记录（ADR）、终端执行日志以及依赖包安装清单全部以标准 Markdown 沉淀在同一套目录中，实现跨智能体生态的零摩擦上下文共享。

待验证 Notion 数据库 30 分钟轮询脚本触发自动合并低风险 PR 的稳定性。

![研发场景端到端闭环流水线（Issue → 复现 → 云端 Agent → 核验 → PR → 人工合并）](../images/fig-18-3.png)

*图：研发场景端到端闭环流水线（Issue → 复现 → 云端 Agent → 核验 → PR → 人工合并）*

> [!NOTE]
> 📸 **截图位（待补）**：主工程 Bot 根据排查结果创建工作项并指派到 Notion 看板

> [!NOTE]
> 📸 **截图位（待补）**：Cursor Cloud Agent 提交的 Pull Request 页面及附加测试证据

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 多模态比对前后 UI 截图并自动驳回样式偏差的评注

> [!NOTE]
> 📸 **截图位（待补）**：共享 Notion 数据库看板中各 PR 状态在 30 分钟轮巡下的变迁

## 18.6 凌晨三点代码巡检与 P0 应急通道 · Nightly Audits & P0 Process

工程师离线休息时，云端常驻算力正好转去常规治理。官方工程团队设立了**凌晨三点的夜间代码巡检例程**（https://x.ai/bot/guides/grok-bot-for-engineering）。每天凌晨 3 点，工程 Bot 会自动启动，清理代码库中的无用死逻辑、优化代码结构、加速客户端加载速度并压缩产物体积。清晨工程师会收到一批清洗干净的 Pull Request，代码重构变成了日常例行机制（https://x.ai/bot/guides/grok-bot-for-engineering）。除常规清理外，这套机制还衍生出多种巡检模式：排查遗留漏洞的安全巡检、防止构建时间膨胀的 CI/CD 耗时巡检、填补单语言发布漏洞的国际化巡检、消除 iOS 与桌面端功能差异的双端对齐巡检，以及汇总过去 24 小时已合并 PR 的进度追赶巡检（https://x.ai/bot/guides/grok-bot-for-engineering）。

日常巡检之外，面对严重线上故障，团队配置了专门的 P0 紧急干预流程（https://x.ai/bot/guides/grok-bot-for-engineering）。云端 Agent 在启动开发实例、安装环境与运行测试套件时往往较耗时，一旦某个任务被打上 P0 标签，工程 Bot 就会启动高频临时 Routine，每隔 5 分钟检查一次 Agent 的运行转录，分析其推演逻辑，并在 Agent 出现卡顿或无谓消耗时间时主动纠偏引导（https://x.ai/bot/guides/grok-bot-for-engineering）。Lingxi Li 特别提醒，这种高频主动干预机制消耗 Token 的速度远超常规操作，必须严格限定在真正的紧急场景下启用（https://x.ai/bot/guides/grok-bot-for-engineering）。

Lingxi Li 最喜欢的夜间提示词原文只有一句："You have six hours tonight. Build whatever you want. Have fun!"（https://x.ai/bot/guides/grok-bot-for-engineering）。下面是本书在这句话基础上加了清理范围和 PR 要求的改写版：

```text
You have six hours tonight. Clean up dead logic, optimize bundle size, and improve startup latency across our active components. Package each distinct improvement into a clean PR with passing tests. Do not merge anything.
```

待在私有代码库中运行 3:00 a.m. 巡检 Routine 并记录无效死代码清理 PR 的采纳率。

> [!NOTE]
> 📸 **截图位（待补）**：凌晨 3 点 Nightly Audit 专职 Bot 发起的无用代码清理 PR

> [!NOTE]
> 📸 **截图位（待补）**：P0 紧急任务触发时 5 分钟转录监控的实时干预卡片

## 18.7 人工终审、合并红线与真实额度核算 · Human Gate & Usage Economics

无论自动化链路多么完善，涉及核心业务边界时绝不能交出最终控制权。官方安全规范明确规定，不可逆操作必须保留人工确认，后台由 Bot 触发的操作审批卡约在 10 分钟后自动过期失效（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。大影响范围的代码合并、生产数据库变更以及关键凭证权限，都必须留在**人工审查关卡**前（https://x.ai/bot/guides/grok-bot-for-engineering）。在企业级合规层面，根据官方安全架构文档（https://cursor.com/docs/grok-bot/security），团队管理员不仅可以用自然语言编写团队专属的 Auto-Review 审查规则（设为 `Block` 直接阻断或 `Require approval` 要求人工审批），还能配置云端沙箱的出站网络域名白名单（格式如 `*.domain.com:443`）并勾选 **`Apply to MCP servers`** 强制约束所有 MCP 服务器流量。

研发流水线落地的另一大硬约束是成本核算。自 2026 年 10 月 18 日起，官方正式推出 **The X Subscription 三合一统一订阅**（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、中文版 [https://cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)、总览 [https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)；`@bot` 官方公告见 [https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)），将 **Grok**、**Cursor** 与 **X Premium** 整合为单一订阅计划，其中包含 Grok Bot 权限的三个档位分别为 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）**（Free $0 与 Plus $8/月档位不含 Grok Bot）。与此同时，根据官方定价与账单说明，既有独立订阅的 Cursor 付费个人方案分为 Pro（20 美元/月）、Pro+（60 美元/月）与 Ultra（200 美元/月），团队方案为 Teams（40 美元/人/月）（https://cursor.com/pricing；https://cursor.com/help/grok-bot/plans）。老订户只要不主动迁移，仍可保留原有旧版独立 Cursor 档位与定价，或通过 `Settings > Usage & Billing > Manage Plan > Get Access with Grok` 关联个人 SuperGrok（社区整理对应档位为 SuperGrok 30 美元/月、SuperGrok Plus 100 美元/月、SuperGrok Heavy 300 美元/月，见 https://penchan.co/ai/grok/grok-bot/）及 X Premium+ 账号（多账号额度不叠加，自动取周额度上限更高的一档生效，见 https://cursor.com/help/grok-bot/faqs）。但务必注意：**一旦你在 `cursor.com/unify` 或 `accounts.x.ai/unify` 中主动将旧版独立计划升级合并为 The X Subscription，该切换是单向不可逆的，无法再退回旧版独立订阅计划**（https://cursor.com/help/grok-bot/plans）。

新旧两套订阅体系在额度消耗与第三方模型扣费上存在关键差异（https://cursor.com/help/grok-bot/plans）：
- **在全新的 The X Subscription 体系下**：Grok Bot 与 Grok、Cursor **共享同一个周额度池（one weekly usage pool）**，每周固定重置且不结转；当周额度池耗尽，或在 Cursor / Cloud Agent 中调用**非 Grok 系列的第三方模型（如 Claude Opus 5.5 等）**时，系统会直接扣减你在 `grok.com/dashboard/billing` 的 `Additional usage credits` 模块中预先充值的 **Prepaid Credits（预付额度）**（支持开启 Auto Top-up 自动充值并设置独立的月度额外消费封顶上限 Monthly additional usage limit）。
- **在尚未迁移的旧版独立 Cursor 计划下**：Grok Bot 自带独立的每周用量池，官方未公布具体额度数字（https://cursor.com/help/grok-bot/plans）。第三方文档记录指出，Bot 触发的 Cursor 云端 Agent 会计入 Cursor 套餐自身的用量（https://learngrokbot.com）。每周额度耗尽后，若开启后付费按需计费（On-demand billing），可在 `Settings > Usage & Billing > On-demand monthly limit`（或 `cursor.com/dashboard > Spending > Monthly Limit`）中将月度封顶上限设为无、固定金额或无限制（https://x.ai/changelog/bot；https://cursor.com/help/grok-bot/plans）。

在真实额度消耗方面，官方论坛中员工曾披露，高负荷运转的 Bot 每一轮对话都需要重新读取完整上下文，每步约消耗 8 万至 9 万 Token，且多 Bot 协作中约有三分之一的交互属于 Bot 之间的相互唤醒空转（https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。社区帖称（个例，https://x.com/miniyarov/status/2105428357273800799）在 Cursor Pro 档位下，每条交互消息大约消耗 1% 的周额度；如果配置了无休止的 5 分钟轮询 Routine，单月空转消耗可达数百美元（https://x.com/fleyta88/status/2109346840382415019）。社区用户 `@charlie_pmp`（Charlie，[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）也提醒，升级到 The X Subscription 后由于 Grok Bot、Grok App 与 Cursor IDE 三端共用同一个周额度池，任何高频冗余的后台 Routine 都会直接挤占你白天在 Cursor 里写代码的周额度。工程落地的省额原则非常明确：每个独立缺陷修复任务必须开启全新对话以切断臃肿上下文、多 Bot 间严禁无意义的客套回复、以窄范围事件驱动（如 GitHub / Codex 完成时 Webhook 或专属邮箱 `+alias` 加号别名触发）替代高频轮询，高危合并动作始终收口在人工最终确认。

待记录一个标准 Issue-to-PR 全流程在 Cursor Pro 与 Pro+ 方案下的周额度百分比消耗。

> [!NOTE]
> 📸 **截图位（待补）**：人工审查高风险代码变更并最终确认合并的审批卡片

> [!NOTE]
> 📸 **截图位（待补）**：Dashboard/usage 界面展示的周额度与 Cursor Cloud Agent 消耗曲线


# §19 额度去哪了 · Where Usage Goes

> **适合谁**：所有用户，尤其是刚收到"额度用尽"提示、或者担心被意外扣费的新手。本章不需要任何技术背景。

## 19.1 周额度、按需消费、月上限是三套机制 · Three Meters

假设你在调研社区讨论时发现，新手最常碰到的问题就是额度突然见底。周三晚上派了两个整理网页的任务，周四早上一开客户端，输入框上方就挂着一条深色横幅，提示周额度已达到上限，还要再等四天才会重置。很多人看到这里的反应就是慌：是不是月付订阅失效了？还是系统出了扣费 Bug？要不要赶紧再去买个号？

**每周包含用量、额外/按需消费和月度限额是三套完全独立的控制逻辑**（https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/）。不把这三套计量机制拆开，后面排查账单或者调自动化任务就会到处踩坑。自 2026 年 10 月 18 日官方正式将 Grok Bot 并入 **The X Subscription** 三合一统一订阅体系起（https://x.com/bot/status/2110063783796572496，https://cursor.com/help/the-x-subscription/overview），当前生态内并存着**新旧两套计量与结账体系**（https://cursor.com/help/grok-bot/plans，https://cursor.com/cn/help/grok-bot/plans）。理解你自己的账号究竟处在哪一套体系下，是排查额度去向的第一步。

### 一、全新主推体系：The X Subscription 三合一共享周池与 Prepaid Credits 预付机制

在 2026 年 10 月中旬上线的 **The X Subscription** 下，一套订阅同时整合了 **Grok**、**Cursor** 与 **X Premium** 三大产品线（https://cursor.com/help/the-x-subscription/overview，https://cursor.com/help/grok-bot/plans）：

1. **档位准入与单向切换规则**：
   - **包含 Grok Bot 的档位**：**Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 均直接包含 Grok Bot 使用权限；而 **Free（$0）** 与 **Plus（$8/月）** 档位不包含 Grok Bot（https://cursor.com/help/grok-bot/plans，https://cursor.com/cn/help/grok-bot/plans）。
   - **不可逆的单向升级**：既有独立 Cursor 订户可以随时通过 `cursor.com/unify` 或 `accounts.x.ai/unify` 主动升级合并至 The X Subscription，但官方明确规定，**一旦切换至 The X Subscription，将无法退回旧版独立订阅计划**（https://cursor.com/help/the-x-subscription/overview，https://cursor.com/help/grok-bot/plans）。
   - **合并时的退费与移动端渠道双扣预警**：通过 `cursor.com/unify` 合并升级时，网页端直接扣款的旧计划会自动取消并按剩余天数退还折算费用（prorated refunds）；但通过 **Apple App Store 或 Google Play** 订阅的旧账单无法被系统自动取消，用户必须手动前往手机系统订阅管理页取消，否则会产生双份扣费（https://cursor.com/help/the-x-subscription/overview）。

2. **第一套计量器：三端共用的同一个周额度池（One Weekly Usage Pool）**：
   - 与旧版独立套餐“各管各账”完全不同，在 The X Subscription 体系下，**Grok Bot、Grok 与 Cursor 共用同一个周额度池（one weekly usage pool）**（https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview）。
   - 该周额度池每周固定重置，未用完的周额度不会结转至下一周（https://cursor.com/help/grok-bot/plans）。由于三大产品天然共用同一个底层账号与额度池，在该体系下不再需要手动操作 SuperGrok 或 X 账号关联。

3. **第二与第三套计量器：Prepaid Credits（预付充值额度）与月度额外消费封顶**：
   - **超额消费改走预付充值而非后付费账单**：在 The X Subscription 下，当每周包含的共享周额度池耗尽后，系统**不会**产生传统的后付费月度账单，而是直接从 **Prepaid Credits（`Additional usage credits` 预付充值额度）** 中实时扣减（https://cursor.com/help/grok-bot/plans，https://cursor.com/cn/help/grok-bot/plans）。
   - **充值路径与自动续充**：用户需前往 `grok.com/dashboard/billing` 下的 `Additional usage credits` 模块预先充值，支持开启 **Auto Top-up（自动充值）**，并可配置独立的 **Monthly additional usage limit（月度额外消费封顶上限）**（https://cursor.com/help/grok-bot/plans）。如果不充值 Prepaid Credits，周额度池跑到 100% 后 Bot 就会安全停工，绝不会倒欠扣费。
   - **第三方模型扣费边界**：官方计费文档特别说明，在 The X Subscription 体系下，当你在 Cursor IDE 中调用非 Grok 系列的第三方模型（third-party models）时，费用**直接从 Prepaid Credits（预付额度）中扣除**，而不会消耗包含在套餐内的 Grok 共享周额度池（https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview）。

| 对比维度 | The X Subscription（2026-10-18 起主推） | Legacy 独立 Cursor 计划（未迁移老订户） |
| :--- | :--- | :--- |
| **适用档位与月费** | Premium $30 / Super $100 / Ultra $200（Free $0 与 Plus $8 不含 Bot） | Cursor Pro $20 / Pro+ $60 / Ultra $200 / 自助 Teams $40 |
| **周额度池隔离性** | **三端共享同一个周额度池**（Grok Bot + Grok + Cursor 共用） | **Grok Bot 独立周池**（仅移交 Cloud Agent 写代码时扣 Cursor 额度） |
| **账号关联规则** | 天然三合一，无需手动绑定 | 可通过 `cursor.com/bot/onboarding` 绑定 SuperGrok / X Premium+，不叠加取高档 |
| **周池耗尽后的溢出机制** | 扣减 **Prepaid Credits（预付充值额度）**，无预付余额即停工 | 走 **Post-paid On-demand（后付费按需计费）**，个人默认关闭、Teams 默认开启 |
| **Cursor 调用非 Grok 第三方模型** | 直接扣减 **Prepaid Credits（预付额度）** | 计入原 Cursor 套餐模型额度或后付费按需账单 |
| **账单与限额管理后台** | `Settings > Usage & Billing` 及 `grok.com/dashboard/billing` | `Settings > Usage & Billing` 及 `cursor.com/dashboard > Spending` |

### 二、既有保留体系：Legacy 独立 Cursor 计划与后付费按需计费

只要老订户不主动在 `cursor.com/unify` 执行单向合并，原有的独立订阅计划与计费规则依然完整保留（https://cursor.com/help/grok-bot/plans）：

第一套机制是订阅自带的每周包含用量。官方叫它 Weekly usage limit，在手机端简称为 Weekly usage（https://cursor.com/help/grok-bot/plans）。所有付费的个人 Cursor 套餐——Pro 每月 20 美元、Pro+ 每月 60 美元、Ultra 每月 200 美元（https://cursor.com/pricing），以及 Cursor Teams 自助套餐每人每月 40 美元（https://cursor.com/pricing），都直接包含 Grok Bot 的使用资格（https://cursor.com/help/grok-bot/plans）。要是没有 Cursor 付费订阅，在旧版独立体系下通过 `Settings > Usage & Billing > Manage Plan > Get Access with Grok`（或 `cursor.com/bot/onboarding`）绑定个人 SuperGrok、SuperGrok Plus、SuperGrok Heavy 或者 X Premium+ 账号也能拿到额度，但官方明确规定 SuperGrok Lite 不包含 Grok Bot（https://cursor.com/help/grok-bot/plans）。档位划分上，官方只给了相对顺序：Pro 低于 Pro+，Pro+ 低于 Ultra；关联档里 SuperGrok 和 X Premium+ 都低于 SuperGrok Plus，Plus 低于 Heavy，Heavy 是"最高关联档"（https://cursor.com/help/grok-bot/plans）。Cursor 档和关联档之间是否一一对应，官方没有写明，社区通常把它们按 Pro≈SuperGrok、Pro+≈Plus、Ultra≈Heavy 来对照。自助开通的 Grok Business 席位也能用，用 Sign in with Grok 登录即可（同上）。

在尚未迁移至 The X Subscription 的旧版独立个人套餐下，这里的周额度拥有完全独立的计量池。Grok Bot 干活绝不扣你在 Cursor 编辑器里写代码的模型额度，你在编辑器里写代码也不会影响 Grok Bot 的周用量，去 Grok 独立网页应用聊天又是另一套限额系统（https://cursor.com/help/grok-bot/plans，https://learngrokbot.com/usage-limits）。在旧版独立套餐中只有一个连通例外：当 Bot 在对话中把写代码任务移交给 Cursor Cloud Agent 时，Bot 自己的轮次消耗 Grok Bot 周用量，Cloud Agent 写代码的部分则直接计入 Cursor 套餐额度（https://cursor.com/help/grok-bot/plans，https://learngrokbot.com/usage-limits）。

多买旧版独立订阅也不会让额度叠加。官方文档写得很清楚，独立 Cursor 套餐和关联的 SuperGrok 或 X Premium+ 额度无法叠加（do NOT stack），系统只取其中周额度更高的那一档（https://cursor.com/help/grok-bot/plans）。而且账号关联是永久的，一旦绑定就不能解绑，也不能转移给其他 Cursor 账号（https://cursor.com/help/grok-bot/plans）。如果你在关联账号上把 SuperGrok 升级到了 Plus 或 Heavy，官方说明周用量刷新到新档位可能需要最多 24 小时（https://cursor.com/help/grok-bot/plans，https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/）。在这 24 小时内不用重复购买，也不用反复折腾解绑。

第二套机制是超额消费（The X Subscription 下为 Prepaid Credits 预付额度扣减，尚未迁移的旧版独立 Cursor 计划下为 Post-paid On-demand usage 后付费按需消费）（https://cursor.com/help/grok-bot/plans）。周额度用完后，系统不会偷偷替你透支扣钱。在 The X Subscription 下，若未在 `grok.com/dashboard/billing` 充值 `Additional usage credits`，周额度用尽即停；而在旧版独立 Cursor 计划下，如果你在客户端设置里把 `Settings > Usage & Billing > On-demand monthly limit` 保持为默认的关闭状态（None），一旦周额度跑到 100%，所有的 Bot 都会就地停工，直到倒计时结束重置，期间不会扣你信用卡一分钱（https://cursor.com/help/grok-bot/plans，https://learngrokbot.com/usage-limits）。注意：这里说的"默认关闭"只适用于个人账户；旧版 Cursor Teams 团队账户的按需用量默认是开启的，团队成员要先问管理员上限是多少（https://cursor.com/help/grok-bot/plans）。在旧版独立计划中，只有当你主动开启按需消费后，Bot 才能在周额度耗尽后继续跑，超额部分的费用全部由 Cursor 统一按实际消耗的模型 Token 后付费计费；哪怕你是靠绑定 SuperGrok 或 X Premium+ 拿到的使用资格，旧版按需账单依然记在 Cursor 头上（https://cursor.com/help/grok-bot/plans，https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/）。另外，如果 Cursor 账户里有推荐或促销赠金，周额度耗尽后系统会优先扣除赠金；即便按需限额设为 0 美元，赠金也会正常消耗，不会产生信用卡扣款（Cursor 员工论坛回复，https://forum.cursor.com/t/grok-bot-draining-cursor-credit-pool/169982）。

第三套机制是额外/按需消费的月度上限（在 The X Subscription 的 `grok.com/dashboard/billing` 中对应 `Monthly additional usage limit`；在旧版独立 Cursor 计划的客户端中对应 `Settings > Usage & Billing > On-demand monthly limit`，网页端对应 `cursor.com/dashboard > Spending > Monthly Limit`）（https://cursor.com/help/grok-bot/plans）。你可以设成固定金额，也可以设成不限额（https://learngrokbot.com/usage-limits）。这里有个很多人都会踩的坑：月度限额并不是任务执行过程中的绝对硬停机线（https://cursor.com/help/grok-bot/plans，https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/）。官方文档写明了，一个正在运行的长任务即使中途超出了月度限额，系统依然允许它跑完并完成交付。只有等这个任务结束后，后续新任务才会被拦截。别以为设了 10 美元限额账单就绝不会变成 12 美元，想在提示词里要求强制停机也没用。

官方提供的免费试用也是同理。它本质是一笔固定的使用额度，附带 7 天有效时间窗口（https://cursor.com/help/grok-bot/plans）。时间和额度是两个独立条件，拿试用额度去跑繁重大任务，几个小时内额度就可能先于 7 天窗口耗尽；官方明确说了，用完的试用额度不会补发（https://cursor.com/help/grok-bot/plans）。7 天试用绝不等于 7 天无限用。

![Grok Bot 三套计量器、周期与溢出计费流转关系](../images/fig-19-1.png)

*图：Grok Bot 三套计量器、周期与溢出计费流转关系*

## 19.2 吞额度的常见元凶 · Burners

很多人在客户端里只聊了几句，或者刚建了两个定时任务，就发现周额度缩水了一大截，总怀疑系统在偷跑。其实 Grok Bot 计费看的是背后真实发生的执行步骤和 Token 消耗，绝不是看你在对话框里输入了几个字（https://cursor.com/help/grok-bot/plans，https://learngrokbot.com/usage-running-out）。

要搞清楚额度怎么没的，先得看它的上下文处理机制。**Grok Bot 每次回复前，都会把当前会话的历史记录完整重读一遍**（Cursor 员工论坛回复，https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705；https://learngrokbot.com/usage-running-out）。系统不会在每次聊完后自动压缩历史，只有当上下文长度逼近模型极限时才会进行总结（Cursor 员工论坛回复，https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。官方技术人员查大额账单时提到，那些重度调用的 Bot 每走一步往往都要重新读取大约 80,000 到 90,000 个 Token（Cursor 员工论坛回复，https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。如果一个会话连续用了好几天，里面堆满了网页抓取结果和长篇输出，哪怕你最后只是追问一句搞定没有，它也必须先吃下前面数万个 Token 的历史上下文，单次回话成本直接滚雪球。

假设你翻看官方文档和社区反馈，可以整理出几个最常见的吞额度元凶。

第一个元凶是会话常年不刷新，还把 Routine 挂在日常聊天的 Bot 身上。新手最容易把一个 Bot 当成日常聊天窗口，所有任务都在同一个对话流里累加（https://learngrokbot.com/usage-running-out）。更隐蔽的坑在定时任务的运行机制：Routine 每次运行，都是在它所属 Bot 的对话流中进行的（https://learngrokbot.com/usage-running-out）。如果你把一个每小时巡检网页的 Routine 挂在白天频繁聊天的 Bot 下，这个 Routine 每次启动时，都得先把白天聊过的几万字背景全盘重读一遍。哪怕它只是抓取单行状态，也会白白消耗巨大的上下文额度。

第二个元凶是高频轮询空转，没设无变化退出机制。有人把 Routine 的触发间隔设得极密，比如每 15 分钟甚至每 5 分钟跑一次（https://cursor.com/help/grok-bot/routines）。社区帖称每 5 分钟触发一次的 Routine，一个月内会执行 8,640 次（个例）（https://x.com/fleyta88/status/2109346840382415019）。每 15 分钟执行一次，一天就会产生将近 100 次运行（https://learngrokbot.com/usage-running-out）。如果在 Routine 提示词里没写明数据无变化立即退出，Bot 每次都会老老实实打开网页、抓取、分析并写长汇报。在公共 Slack 频道挂监听也是同样的道理，活跃频道里每来一条新消息都会触发一次完整的 Bot 回合，一天之内烧光整周额度很常见（https://learngrokbot.com/usage-running-out）。

第三个元凶是长时间操作浏览器、频繁截图，在卡顿页面上死磕。Bot 操作云电脑里的浏览器属于高开销动作（https://learngrokbot.com/usage-limits）。目标网站一旦出现动态加载慢、反爬弹窗或者页面假死，Bot 会自己多次滚动、重试和重新截图分析。第三方 Grok Bot Wiki（非官方站点）写道，让 Bot 在卡顿网页上反复折腾 20 分钟消耗的 Token 和步骤，远比连续回答几十次短文本问答昂贵得多（https://www.grokbotwiki.com/guides/grok-bot-weekly-usage-limit）。

第四个元凶是多 Bot 群聊互相客套，甚至陷入死循环。多 Bot 协作群聊看着省事，但群内每个 Bot 的发言都会被单独计费，Bot 之间互通消息同样消耗额度（https://learngrokbot.com/usage-limits）。官方技术人员指出，在某些大额消耗账户里，大约三分之一的调用纯粹是 Bot 之间互相唤醒造成的（Cursor 员工论坛回复，https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。一个 Bot 汇报完成，另一个回复收到，第三个再补充感谢，这些客套交互在后台极吃 Token。Cursor 员工在论坛里建议，在多 Bot 协作提示词里直接加入安静交接指令（https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705；整理见 https://learngrokbot.com/usage-running-out）：

```text
From now on, only message another Bot when it needs to act. No acknowledgments, no thanks, no progress updates. Send one summary when the work is done.
```

更极端的情况是 Bot 自己陷入死循环。社区帖称有用户建了一个叫 Elon 的 Bot，刚建完没输任何提示词，Bot 自动在网上搜了马斯克头像换上，随后陷入自言自语并反复尝试生成马斯克真人图的死循环（die loop），客户端停不下来，一口气白白烧掉了 4% 的周额度（个例）（https://linux.do/t/topic/2807876）。服务故障期间也容易踩这种坑。2026 年 10 月 8 日全网 Routine 出现系统级故障，论坛里有用户说排查过程本身就耗掉了额度，有人当天用掉 30%，有人超过 90%。Cursor 员工 @deanrie、@kevinn 说明原因是平台负载过高，暂停、恢复、复制或重建 Routine 都没用，错过的运行也不会补跑（https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125）。

第五个元凶是在云电脑中套娃跑其他外部大模型工具。社区帖称有用户为了省 Token，在 Grok Bot 的云电脑里装了 Codex 和 Claude Code。结果 Codex 的额度消耗极快，一个自动化任务还没跑完，五小时的额度就用光了；那个从没用过的 Claude 免费号后来也收到了封号邮件，原因帖子里没说明，是否与机房 IP 有关属于推测（个例）（https://x.com/i/status/2107100457231651312）。用虚拟机套娃跑高消耗开发工具，往往得不偿失。

除了上述五个经典陷阱外，随着 2026 年 10 月下旬 The X Subscription 的普及以及官方 v0.75.2 版本对自动化配额的放宽，社区博主 Charlie（`@charlie_pmp`）通过实测复盘指出了导致用户感觉“周额度掉电突然变快”的**第六与第七两大新元凶**（https://x.com/charlie_pmp/status/2114214503416271131）：

第六个元凶是**三端共享抽水效应（Cross-Surface Pool Drain）**。在旧版独立 Cursor 套餐下，用户在 Cursor IDE 里通宵写代码，或者在 Grok 网页/手机 App 里高频对话、生成图片，都与 Grok Bot 的周额度池互不相干；但升级到 **The X Subscription** 后，**Grok Bot、Grok App 与 Cursor IDE 三端改从同一个周额度池抽水**（https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview，https://x.com/charlie_pmp/status/2114214503416271131）。很多开发者白天在 Cursor 里用大模型跑了几轮大型代码库重构，晚上回到 Grok Bot 客户端一看，发现哪怕自己的 Bot 一整天没说一句话，剩余周额度也已经掉了十几个百分点。因此，在三合一订阅下排查额度去向时，必须把自己在 Cursor 编码和 Grok 聊天的消耗一并算进总账。

第七个元凶是 **v0.75.2 配额松绑后的冗余 Routine 高频空转**。在 2026 年 10 月 22 日发布的 v0.75.2 更新中，官方将 Routine 的小时级运行频率限制大幅上调至**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots），以及单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**（虽然定时触发的最小间隔仍为 5 分钟，但邮件、消息与 Webhook 等事件触发型 Routine 可以跑到极高并发）（https://x.ai/changelog/bot，https://cursor.com/help/grok-bot/routines）。`@charlie_pmp` 提醒（https://x.com/charlie_pmp/status/2114214503416271131），如果用户没有利用 v0.71.2 新增的 `@mail.grokbot.com` 专属邮箱 `+alias` 加号别名（https://x.com/SamSokolin/status/2110496237241667621，https://cursor.com/help/grok-bot/agent-email）来精准过滤触发源，或者保留了多条未加精简改写的冗余定时 Routine 在后台静默空转，放宽后的 300 次/小时上限反而会让未加约束的触发器在几小时内加速烧穿整个共享周额度池。

![长会话重读机制与多 Bot 互相唤醒引发的 Token 滚雪球效应](../images/fig-19-2.png)

*图：长会话重读机制与多 Bot 互相唤醒引发的 Token 滚雪球效应*

## 19.3 怎么看用量 · Reading Usage

要守住额度，先得学会看面板。

桌面客户端点左下角头像，或者进 Settings 选择 Usage & Billing 页面（https://learngrokbot.com/usage-limits）。v0.63.0 起，Settings → Usage & Billing 会显示包含用量和下次重置时间，不再误显示"套餐不含用量"（https://x.ai/changelog/bot，https://learngrokbot.com/usage-limits）。在最新的 v0.75.5 客户端中，进入 `Settings > Usage & Billing` 面板，你可以一站式查看当前周期的**周额度进度条（Weekly usage progress bar）**、**Prepaid Credits（预付额度）实时余额**，并通过面板上的 **`Manage Plan`** 与 **`Manage Billing`** 快捷入口直接管理订阅档位与账单设置（https://cursor.com/help/grok-bot/plans，https://cursor.com/docs/grok-bot/settings）。

在网页端，根据你所处的订阅体系不同，有两个对应的核账入口：
1. **The X Subscription 统一账单后台（`grok.com/dashboard/billing`）**：如果你已经加入或升级至 The X Subscription，直接访问 `grok.com/dashboard/billing` 即可查看三合一共享周额度状态、在 `Additional usage credits` 模块充值 **Prepaid Credits**、开关 **Auto Top-up（自动充值）**，以及调整 **Monthly additional usage limit（月度额外消费封顶上限）**（https://cursor.com/help/grok-bot/plans，https://cursor.com/help/the-x-subscription/overview）。
2. **Legacy 独立 Cursor 账单与调用明细后台（`cursor.com/dashboard`）**：在网页端，可以直接访问 cursor.com/dashboard，在 Spending 页面核对 Grok Bot 卡片的明细与按需消费上限（https://learngrokbot.com/usage-limits）。如果想了解任务背后实际调用的模型，可以登录 cursor.com/dashboard/usage 查看后台记录，确认任务是路由到了 opus 5.5 还是使用了默认的 grok-bot-default（https://linux.do/t/topic/2990677）。

看面板时别想当然：**面板上的百分比是相对消耗比例，不是固定的美元金额或消息条数**（https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/）。很多人看到剩余额度从 80% 掉到 74%，就以为自己花掉了 6 美元，或者觉得 1% 就是固定的一条对话。社区帖称 Cursor Pro 的 Bot 额度相当于 250 美元或 450 美元（个例）（https://linux.do/t/topic/2848179），也有社区帖称 Pro 账号每发一条消息大约消耗 1% 的周额度（个例）（https://x.com/miniyarov/status/2105428357273800799）。

官方从未公布过任何档位对应的具体 Token 数量或折算金额（https://cursor.com/help/grok-bot/plans）。面板上的百分比只是你当前在一周动态额度池中的使用进度。一条简单的单行文字回答，在独立会话中可能只让周额度波动 0.01%；而一个包含翻长网页、抓数据、跑脚本的任务，消耗可能是前者的数十倍（https://learngrokbot.com/usage-running-out）。脱离了步骤复杂度与会话上下文长度，把百分比生搬硬套成单条消息成本没有任何意义。

目前客户端没法按单个 Bot 或单个 Routine 拆分显示用量明细（https://learngrokbot.com/usage-running-out）。面板给出的永远是整个账户的统揽百分比。想弄清楚具体哪项任务最吃额度，不能靠猜，可以在没有其他定时任务跑的时间段（如果是 The X Subscription 订户，测试期间还应暂停在 Cursor IDE 和 Grok App 中的操作），单独运行某一个受控任务，记录执行前后的百分比净变化（https://ofox.ai/zh/blog/grok-bot-weekly-usage-on-demand-limit/）。

测试独立受控环境下单次网页浏览任务与纯文本问答前后的周用量百分比变化。

> [!NOTE]
> 📸 **截图位（待补）**：Settings > Usage & Billing 面板中的周用量百分比与重置倒计时
> [!NOTE]
> 📸 **截图位（待补）**：cursor.com/dashboard/usage 面板中的后台模型调用记录


# §20 省钱心法 · Saving

> **适合谁**：所有用户都该读 20.1 和 20.4。20.2、20.3 要写脚本、配 Webhook 和 API Key，零代码读者可以先跳过，或者把相关段落整段交给 Bot 让它代劳。

翻看社区讨论，新手踩得最多的坑就是额度焦虑。假设你周一刚开通，周三晚上额度就见底了，代码甚至没写出几万行。大家很容易以为是官方（https://cursor.com/help/grok-bot/plans）给的额度太少，或者以为 Bot 每次聊天都在扣大钱。其实 Grok Bot 的消耗逻辑和网页里的大模型对话完全不同。照搬传统聊天机器人的用法，周额度撑不过三天；一旦开了按需付费或预付自动充值，月底账单更吓人。翻完官方文档（https://cursor.com/docs/grok-bot）和社区踩坑案例，这里把理出来的四套省钱架构整理在这一章。每一步都有明确的计费机制和出处，把边界讲清楚。

## 20.1 Bot 只调度、不执行 · Dispatcher Pattern

很多人刚接触 Grok Bot，习惯把它当全能苦力：把几万行项目源码一股脑拖进会话，或者让它在主聊天窗口写完整的自动化脚本。额度就是这么被烧光的。在系统底层，每个 Bot 只有一条长对话时间线。你向 Bot 发送新消息时，系统并不是只处理你刚发的那几十个字，而是在后台把前面上万字的历史记录从头到尾重读一遍。

比利时电商 Angelo.be 的技术负责人（@dotstijn）在 Cursor 官方论坛发帖反映，团队跑 Grok Bot 一周超额用量产生了大额账单（来源：https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。Cursor 官方员工 @kevinn 在论坛排查后台后确认账户没问题，计费高昂的根本原因在于系统每轮都会重读该 Bot 的整段对话历史（Cursor 员工论坛回复，来源：https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）。最忙的几个 Bot 每执行一个小动作，都要重读约 8 万到 9 万个 token 的历史记录，而且团队内部大约三分之一的轮次纯粹是 Bot 之间互相唤醒。Cursor 官方论坛的技术回复也指出（Cursor 员工论坛回复，来源：https://forum.cursor.com/t/grok-bot-context-window-size-and-token-accumulation-logic-in-pro/171540），对话历史会被系统持续重读，虽然其中包含缓存 token，但直到接近上下文上限时系统才会自动进行压缩摘要，同时复制 Bot 也不会带走原有的记忆。

推特用户铁柱AGI（@cgnot996）在 2026 年 10 月 9 日的实操总结中，把这种现象概括为默默交的“上下文重读税”与“多模态空转税”（来源：https://readcopilot.ionichina.com/articles/53772；原帖：https://x.com/cgnot996/status/2108504325609984233）。他提出的首要解法就是调度器模式：**Bot 只做调度器，绝不当执行苦力**。

调度器模式的核心是分工。主 Bot 负责规划步骤、下达指令、回收结论，绝不亲自承载成百上千行的脏活代码或海量素材。需要分析视频抽帧或大量图片时，先在外部用轻量工具提取几百字的文本摘要再喂给 Bot；需要处理长代码时，让它把生成与修改任务派发给后台已有的代码工具或本地环境。社区帖称把长代码外包给外部工具后，Bot 本身的额度消耗从 70% 降到了 3%（个例，来源：https://readcopilot.ionichina.com/articles/53772 ）。

关于“对话层（Conversational Layer）”与“执行层（Execution Layer）”的严格分离，中文社区在 2026 年 10 月中旬展开过一场极具启发性的架构讨论。博主数字生命卡兹克（`@Khazix0918`，285 赞 / 54 书签，来源：https://x.com/Khazix0918/status/2111709708226797737）指出了不配专属 Skill、也不做任务委派而直接在默认聊天窗“裸用” Grok Bot 的痛点——如果把对话路由模型直接当成重度执行苦力，不仅容易遇到路由模型不查证就草率回复的问题，来回掰扯纠错既浪费时间又白白燃烧周额度。对此，开发者 `@object_nullll`（来源：https://x.com/object_nullll/status/2111717423837778173）一针见血地拆解了官方底层设计原则：Grok Bot 主会话窗口的对话层本质上是用来**收集业务上下文、对齐验收标准（Acceptance Criteria）、生成结构化 Prompt，并将重度执行任务委派给 Cursor Cloud Agents（`CloudAgent`）或云电脑内部的 CLI Workers**，绝不能依赖主聊天框的零样本（zero-shot）直出回复去干重活。

将“AI 生成确定性代码 + 脚本承担日常执行”发挥到极致的黄金实战案例，来自本书作者 Mr.鼓先生（`@StarkLJM`，来源：https://x.com/starkljm/status/2111803996734419377 与 https://x.com/starkljm/status/2112818533797343312）。在需要每天定时抓取 30 条热门榜单数据的业务场景中，如果让大模型每天打开云端浏览器去读 DOM 树和网页全文，不仅慢，还会持续消耗可观的周额度。`@StarkLJM` 的做法是：

1. **一次性让 AI 写确定性脚本**：调用 Cursor CLI，仅耗时 **28.6 秒**就生成并调通了一套高可靠性的 Python 爬虫脚本。
2. **日常运行零模型额度（Zero Model Tokens）**：此后每天定时运行该 Python 脚本，仅需 **1.99 秒**即可抓取并解析完 30 条完整榜单记录，日常跑批消耗 **0 模型额度**。
3. **防御性编程替代模型兜底**：为了让脚本在不调用大模型的情况下依然保持数据洁净，脚本内置了严格的 schema 校验与缺失值防御规则——一旦上游网页改版导致关键字段缺失，立即抛出非零退出码触发告警；当源数据中某条目暂无评分时，严格写入 `null` 而非用 `0` 填充，彻底杜绝了 `0` 分脏数据拉低整体均值计算的隐患。

你可以直接在云电脑中部署如下遵循 `@StarkLJM` 防御性规范的零额度抓取脚本骨架：

```python
#!/usr/bin/env python3
"""
零模型额度确定性抓取脚本示例（28.6s 一次性生成，日常 1.99s 跑完 30 条）
规则：严格校验必填字段，缺失评分存 None (JSON null) 绝不用 0 污染均值
"""
import json
import sys
import time
import urllib.request

REQUIRED_KEYS = {"id", "title", "url"}

def fetch_ranking_list(api_url: str, limit: int = 30) -> list[dict]:
    req = urllib.request.Request(api_url, headers={"User-Agent": "GrokBot-Deterministic-Worker/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        raw_items = json.loads(resp.read().decode("utf-8")).get("items", [])[:limit]

    cleaned = []
    for idx, item in enumerate(raw_items):
        missing = REQUIRED_KEYS - item.keys()
        if missing:
            raise ValueError(f"Row {idx} schema violation, missing keys: {missing}")
        # 防御性规则：无评分时严格记为 None (null)，禁止默认填 0.0
        raw_score = item.get("score")
        score = float(raw_score) if raw_score is not None and raw_score != "" else None
        cleaned.append({
            "rank": idx + 1,
            "id": str(item["id"]),
            "title": str(item["title"]).strip(),
            "url": str(item["url"]),
            "score": score,
        })
    return cleaned

if __name__ == "__main__":
    t0 = time.perf_counter()
    try:
        records = fetch_ranking_list("https://example.com/api/v1/trending", limit=30)
        with open("/workspace/data/daily_ranking.json", "w", encoding="utf-8") as f:
            json.dump({"count": len(records), "records": records}, f, ensure_ascii=False, indent=2)
        elapsed = time.perf_counter() - t0
        print(f"OK: {len(records)} items saved in {elapsed:.2f}s (0 model tokens used)")
    except Exception as exc:
        print(f"ALERT: Scraper failed - {exc}", file=sys.stderr)
        sys.exit(1)
```

配套的第二个习惯，是把云电脑的文件系统当成档案柜，别把大段原文回贴到主聊天框。很多人用 Bot 自带能力搜索 X 平台内容，搜出几十条推文就让 Bot 全文贴在会话里。当时看着省事，后续只要你让它改一个排版或错别字，系统后台就会为了这几千字推文反复计费。正确做法是让 Bot 把抓取到的长文本、原始网页或日志直接保存为云电脑上的文件，主对话里只保留文件路径、状态标记和核心要点。

多 Bot 协作时的客套话也是吞额度的大坑。官方员工（https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705）建议在 Bot 的 Edit Profile 预设中焊死安静交接规则，避免多 Bot 在群聊中互相道谢、确认收到或做无意义的进度汇报。可以直接把下面这段提示词配置进 Bot 的 Profile 中：

```text
Only message another bot when it needs to act. No acknowledgments, thanks, or progress pings. Send one summary when the work is done.
```

技术分析文章也提醒（来源：https://carlstack.gravito.dev/blog/grok-bot-budget-wake-delegation-guardrails/），交接摘要必须保留原始证据与未决状态，不能为了省字数把待验证项直接标成已完成。核心交付物留在文件系统里，主对话保持干净，重读历史的开销才能真正压下来。

对比同一批多步任务在聊天框贴完整代码与写入本地文件引用的周用量消耗差异。

![调度器模式与全能 Bot 的 Token 消耗对比](../images/fig-20-1.png)

*图：调度器模式与全能 Bot 的 Token 消耗对比*
> [!NOTE]
> 📸 **截图位（待补）**：Settings > Usage & Billing 页面中的用量明细与重置周期

## 20.2 脚本轮询 + webhook 唤醒 · Poll Cheap, Wake Rarely

除了长对话的历史重读，另一个让新手几天烧光周额度的地方是定时任务（Routine）。很多人刚学会配置 Routine，立刻给 Bot 加满各种监控：每隔 5 分钟抓一次网页，每隔 10 分钟查一次数据。大家以为只要网页没变化、Bot 没在界面上说话，就不会扣费。

这个理解是错的。官方文档写得很明确（来源：https://cursor.com/help/grok-bot/routines），每次 Routine 执行都会产生实际用量，就连界面上的测试运行（Test run）也会真实消耗额度。排程太密集或触发太频繁，可能在极短时间内用尽整周额度。官方文档规定（来源：https://cursor.com/help/grok-bot/routines），每个 Bot 最多创建 50 个 Routine，定时执行最小间隔不少于 5 分钟；而在官方 v0.75.2 版本更新后（来源：https://x.ai/changelog/bot 与 https://cursor.com/help/grok-bot/routines），Routine 的小时级运行频率配额已上调至**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots），单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**。需要注意的是，频率上限放宽是为了满足高并发 Webhook 或事件驱动业务，绝不意味着你应该把定时巡检拉满——即使目标网页没有更新、Bot 最终决定不发通知，系统只要启动了这轮 Routine，就已经加载了上下文，调用了云电脑的浏览器和模型跑了一圈，这笔开销就省不掉了。正如社区用户 `@charlie_pmp`（来源：https://x.com/charlie_pmp/status/2114214503416271131）在复盘周额度快速消耗时指出的那样，未经精简的高频冗余 Routine 定时任务正是后台静默吞噬额度的头号隐形杀手。

铁柱AGI 在总结中指出（来源：https://readcopilot.ionichina.com/articles/53772；原帖：https://x.com/cgnot996/status/2108504325609984233），很多人的额度全死在无意义的定时空转上，每 5 分钟巡检一次，没变化也让模型跑一圈，一天就能烧光整周额度。他的解决思路是改用底层轻量脚本去盯盘，零 Token 消耗，只有监测到数据真实异动时，才触发 Webhook 叫醒 Bot 介入处理。

这里的工程核心在于拦截层的位置：**把确定性的轮询交给轻量脚本，只在出现数据异动时才唤醒模型**。相关系统设计分析指出（来源：https://carlstack.gravito.dev/blog/grok-bot-budget-wake-delegation-guardrails/），过滤机制必须建立在模型执行之前；如果每一个事件都先触发了 Routine，再由 Bot 去读取并判断要不要忽略，唤醒成本就已经发生了。在自己控制的脚本层，应该依据数据源的稳定 ID 或核心内容哈希去重；只有确认产生有效增量时，才向工作队列分发。

除了编写外部哈希对比脚本，在 2026 年 10 月中下旬的更新与社区实践中，还诞生了两项堪称“零轮询（Zero-Polling）”教科书级别的省额度绝招：

### 绝招一：用 v0.71.2 专属邮箱 `+alias` 加号别名定向触发 Routine，彻底消灭“定时查收件箱”轮询

过去很多用户为了让 Bot 盯着账单邮件、服务器告警或行业 Newsletter，会配一条每 15 分钟运行一次的 Routine 去轮询检查收件箱。自官方 v0.71.2 版本起（来源：https://x.ai/changelog/bot 与 https://cursor.com/help/grok-bot/agent-email），Grok Bot 工程师 Sam Sokolin（`@SamSokolin`，3,073 赞 / 1,197 书签，来源：https://x.com/SamSokolin/status/2110496237241667621）正式宣布 `@mail.grokbot.com` 专属邮箱原生支持 **`+alias` 加号子别名**，并支持设置**仅当指定 `+alias` 收到邮件时才触发对应 Routine**。

这意味着你完全不需要写任何定时查邮箱的轮询任务：
- 将 Stripe 发票通知绑定到 `yourbot+invoices@mail.grokbot.com`，配置一条仅监听 `+invoices` 的财务记账 Routine；
- 将 PagerDuty 或 GitHub 线上告警发往 `yourbot+alerts@mail.grokbot.com`，配置一条仅监听 `+alerts` 的故障排障 Routine；
- 像社区用户 `@songsong275452`（引用 `@gokul_i`，来源：https://x.com/songsong275452/status/2113108916229886371）那样，把所有订阅的 Newsletter 全部导入 `yourbot+newsletters@mail.grokbot.com`，日常收到邮件时静默归档不唤醒长任务，只在每周六运行一次汇总 Routine 生成精华周报。

通过 `+alias` 硬件级分流，没来信时 0 唤醒、0 消耗；来信瞬间精准触发对应业务线的 Routine，彻底告别无意义的收件箱轮询。

### 绝招二：云机内跑长耗时 CLI 并配置“任务完成时 Webhook 唤醒”（`@AbhisheKumarA7` 零轮询范式）

当你在 Grok Bot 的云电脑（Cloud Computer）内部调用 Codex CLI 或其他外部编译/训练脚本执行长达数十分钟的重度任务时，如果让 Grok Bot 在前台每隔几十秒运行一次 `sleep` + 状态检查（polling），每轮检查都会重读整段长上下文，造成惊人的 Token 浪费。

海外开发者 Abhishek Kumar（`@AbhisheKumarA7`，来源：https://x.com/AbhisheKumarA7/status/2110484964143976578）与中文博主一泽Eze（`@eze_is_1`，351 赞 / 705 书签，来源：https://x.com/eze_is_1/status/2109850538045264151）分享了极为优雅的**完成时回调唤醒（Wake-on-Done via Webhook）**方案：
1. 在 Grok Bot 中预先创建一条以 **Webhook** 为触发器的验收 Routine，拿到专属的 Webhook URL 与 Bearer Secret。
2. 当主 Bot 需要启动耗时漫长的 Codex CLI 编码或大批量构建任务时，使用后台非阻塞方式（如 `nohup` 或 `tmux`）启动脚本，并在命令链末尾追加 `curl` 回调。
3. 主 Bot 启动后台进程后**立即结束当前对话轮次**，进入零消耗休眠状态；待 Codex CLI 跑完所有测试并输出产物落盘后，脚本自动 `POST` 触发 Webhook，精准叫醒 Grok Bot 验收并向用户汇报：

```bash
# 在云电脑后台运行长耗时 Codex CLI 任务，跑完后自动 POST Webhook 唤醒 Bot（全程 0 轮询 Token 消耗）
nohup bash -c '
  codex --approval-mode full-auto "重构 src/ 下的支付对账模块并跑通全部 pytest 单元测试" \
    > /workspace/logs/codex_build.log 2>&1
  EXIT_CODE=$?
  TAIL_LOG=$(tail -n 25 /workspace/logs/codex_build.log | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))")
  curl -sS -X POST "https://cursor.com/api/grok-bot/webhooks/YOUR_ROUTINE_WEBHOOK_ID" \
    -H "Authorization: Bearer $GROK_BOT_WEBHOOK_SECRET" \
    -H "Content-Type: application/json" \
    -d "{\"event\": \"codex_job_finished\", \"exit_code\": $EXIT_CODE, \"log_tail\": $TAIL_LOG}"
' >/dev/null 2>&1 &
```

调用 Webhook 时还有一个容易踩的坑。官方 Webhook 返回 HTTP 200 只代表系统成功接收了请求并开始排队执行，绝对不能等同于任务交付完成（来源：https://cursor.com/help/grok-bot/routines）。如果接收端缺少幂等键设计，一旦网络抖动导致上游重发，系统就会并发启动多个相同的昂贵任务。

跑自动化流程时，重试上限和按量付费必须卡死。铁柱AGI 建议把失败重试上限锁为 2 次，并且务必在后台关闭按量付费（来源：https://readcopilot.ionichina.com/articles/53772）。Bot 在执行网络抓取或工具交互时，一旦遇到目标网站反爬拦截或报错，极易陷入反复重试的死循环。官方计费方案说明明确指出（来源：https://cursor.com/help/grok-bot/plans），按需用量月度限额（On-demand Monthly Limit）不会在中途强行中断已经开始执行的工作，已在执行的 Bot 超出月度限额后会继续跑完本次任务；而在全新的 **The X Subscription** 体系下，周额度耗尽后会改为从 `grok.com/dashboard/billing` 的 **Prepaid Credits（预付额度）** 中扣费，若开启了 Auto Top-up（自动充值），死循环任务同样会持续消耗你设置的月度额外消费上限（Monthly additional usage limit）。一旦死循环任务在后台不断重试，即便设置了预算上限，也可能在任务结束前超额扣费。因此在任务指令中明确写入遇到错误重试不得超过 2 次，是防止自动化任务失控的必要防护。

日常巡检可以写一个简单的本地或云端 Python 脚本，用本地算力计算网页内容哈希，只有哈希变动时才向 Bot 发起调用：

```text
检查目标数据源哈希值是否与上次记录一致。
若哈希未发生变化，直接退出并记录日志，禁止触发下游调用；
若哈希存在差异，更新本地记录文件，并通过 Webhook 仅发送差异摘要与目标 URL。
重试次数上限严格限制为 2 次，失败即终止并记录错误码。
```

测试轻量 Python 脚本监测网页内容哈希并在变更时触发 Webhook 的端到端延迟。

![脚本轮询与 Webhook 按需唤醒架构](../images/fig-20-2.png)

*图：脚本轮询与 Webhook 按需唤醒架构*
> [!NOTE]
> 📸 **截图位（待补）**：Routine 配置面板中的触发器与间隔设置

## 20.3 免费或外部模型做执行层 · External Models

掌握了前两招之后，很多人会想：既然 Grok Bot 这么贵，能不能直接把底层模型换成便宜的轻量模型？

在官方界面里根本做不到。官方模型说明文档明确指出（来源：https://cursor.com/help/grok-bot/models），Grok Bot 既没有模型下拉选单，也不会在界面上显示每次请求具体用了哪个底层模型。官方（https://cursor.com/help/grok-bot/models）走的是全托管路由逻辑，普通用户无法在客户端内直接指定由哪一个轻量模型来应答。想要在执行层面大幅降低算力成本，唯一的路径就是在云电脑中搭建外部执行层，把机械脏活分流出去。

中文社区探索出的一条路径，是利用云电脑环境接入 OpenRouter 的免费模型。推特用户 @NFT_Chen 分享过一套基于 Pi Agent 的执行层方案（来源：https://x.com/i/status/2108414543978533341）。方案把 OpenRouter 上标价为 0 的免费模型接到 Pi Agent，作为 Grok Bot 的下层执行器。未充值状态下每天有 50 次请求额度，若累计充值 10 美元则提升至每天 1000 次。具体操作上，可以让 Grok Bot 在云电脑中安装对应的 CLI 工具并配置环境变量，让 Pi Agent 运行本地脚本跑扫描任务，Bot 自身只负责接收最终产物。

### 实战进阶：`@hppzyy` 的“Pi Agent（`pi`）+ DeepSeek API Key”极致省额度方案与 `@37FlowAI` 防卡死修复

如果你觉得免费模型容易遭遇 429 限流、稳定性不够，2026 年 10 月中旬中文社区验证出了兼顾“白菜价成本”与“高并发稳定性”的终极外部执行层方案——**云电脑内安装 Pi Agent（`pi`）+ 挂载 DeepSeek API Key**。

博主 `@hppzyy`（来源：https://x.com/hppzyy/status/2111573227881529454）分享了这套实战配置：在 Grok Bot 的云电脑沙箱里全局安装轻量级命令行编码智能体 **Pi Agent（`@mariozechner/pi-coding-agent`，命令名为 `pi`）**，并填入极其低廉的 **DeepSeek API Key**（百万输入 Token 仅块把钱人民币）。随后在 Grok Bot 的指令或自定义 Skill 中立下铁律：**Grok Bot 本体只负责拆解任务、调用 shell 下发一条简短的 `pi` 命令并读取最终生成的文件，所有吃 Token 的长文翻译、万字文稿清洗、批量代码编写与重构全部交给 `pi` 背后的 DeepSeek 执行**。这样一来，Grok Bot 每轮对话只产生几百个调度 Token，每周的 The X Subscription 官方额度池几乎不掉电。

然而，在把 `pi` 放进 Grok Bot 的非交互式 Agent Shell 中调用时，很多开发者踩到了一个致命的“无限挂起卡死”大坑。博主 `@37FlowAI`（来源：https://x.com/37FlowAI/status/2111334386339823687）记录了 Grok Bot 自主排障定位出的底层原因：当你在 Agent 的非交互式子进程里运行 `pi -p "..."` 时，`pi` 进程会默认等待标准输入（`stdin`）的 EOF 结束信号，导致命令一直挂起直到超时，白白卡死会话。**解决办法非常简单但必填：在每一条非交互式 `pi -p` 命令末尾强制加上 `< /dev/null`**，显式闭合标准输入，命令即可实现毫秒级瞬间返回！

下面是一套可直接粘贴给 Grok Bot 让其在云电脑内自动配好 `pi` + DeepSeek 并验证 `< /dev/null` 防卡死调用的完整命令模板：

```bash
# 1. 在云电脑内全局安装 Pi Agent CLI
npm install -g @mariozechner/pi-coding-agent

# 2. 配置 DeepSeek API Key（建议写入 ~/.bashrc 或受控环境变量文件）
export DEEPSEEK_API_KEY="sk-your-deepseek-api-key"

# 3. 连通性自检（关键：必须追加 < /dev/null 闭合 stdin，防止非交互式 Shell 无限挂起！）
pi --provider deepseek --model deepseek-chat -p "只回复OK" < /dev/null

# 4. 实战派单示例：让 pi + DeepSeek 承担长文本处理与写代码重活，结果直接落盘，不污染主会话上下文
pi --provider deepseek --model deepseek-chat \
  -p "读取 /workspace/raw_articles.json，按核心观点去重并提炼成结构化 Markdown 报告写入 /workspace/output/digest.md，完成后在终端只输出 DONE" \
  < /dev/null
```

此外，如果你拥有多个外部模型渠道，还可以参考社区开发者 Kaelan Yiu（`@kaelanyiu`，来源：https://x.com/kaelanyiu/status/2114213605566742884）打造的**“模型评测元 Bot（Meta-Evaluator Bot）”**思路：专门设一个低频定时运行的评测 Bot，每隔几天用真实业务题库对 DeepSeek、Claude、GPT 等外部 CLI 模型跑一次自动基准测试，并根据性价比得分动态修改其他干活 Worker Bots 调用的 CLI 默认模型参数，实现执行层模型的全自动优胜劣汰。

### 反向省钱心法：充分利用 Grok Bot 内置的“免费公开 X 检索”反哺本地 Agent

在把重活外包给外部模型的同时，千万别忘了反过来利用 Grok Bot 独有的**零成本护城河**。根据官方 `x-api-mcp-guide` 规范与 [Connect Apps 官方文档](https://cursor.com/help/grok-bot/connect-apps)，**Grok Bot 内置的公开 X 平台数据检索与读取（如 `search_posts_recent`、`search_posts_all`、`get_users_posts`、`get_post_Thread`、`get_article`）完全免费包含在订阅内，不需要额外购买任何 X API 额度**。

如果你在本地电脑上使用 Claude Code 或 Codex 写代码、做调研，自己去买官方 X API 或第三方网页搜索 API 往往价格不菲。中文社区博主康熙AI了（`@kangxiaile`，来源：https://x.com/kangxiaile/status/2109752183889744216）与 x白（`@z_lumia`，来源：https://x.com/z_lumia/status/2113800469571313974）验证了一套极省钱的**反向外包闭环**：通过 BDK（`cursor-grokbot-agents`）将本地 Claude Code 与云端 Grok Bot 打通，每当本地 Claude Code 需要检索某个开源新库的最新实测反馈、报错解法或 X 实时舆情时，直接发消息派单给云端 Grok Bot 跑免费的全量 X 搜索，整理成干净的 Markdown 传回本地交给 Claude Code 继续编码。这样既省下了昂贵的外部搜索 API 账单，又让本地编码 Agent 拥有了全网最鲜活的实时情报源。

另一批研发用户选择在云电脑中部署 Cursor 自身的命令行工具。推特用户 @xiangxiang103 分享过在云电脑中安装 Cursor CLI 的操作（来源：https://x.com/i/status/2109088800903483616）。先在 Cursor 后台「API Keys」新建一个 Key，再让 Bot 在云电脑里安装 Cursor CLI 并填入这个 Key，底层的代码修改直接交给命令行工具执行，Grok Bot 专心当协调员。

搭建外部执行层时，边界意识非常关键：**外部执行池不是免费午餐，必须划清数据权限和失败边界**。

第一是可用性与限流问题。OpenRouter 官方限制文档明确规定（来源：https://openrouter.ai/docs/api_reference/limits；免费模型说明：https://openrouter.ai/docs/guides/routing/model-variants/free），免费模型会根据账户级别施加严格的并发和每日速率限制，绝不能视为有稳定 SLA 保证的生产通道。ModelScope 的 API 限制文档同样指出（来源：https://modelscope.cn/docs/model-service/API-Inference/limits），其推理服务面向单并发正常使用设计，遇到突发流量会进行动态限流。把工作流全押在免费通道上，随时可能遭遇 429 报错或服务暂停。

第二是极易被忽视的数据隐私隐患。系统架构分析指出（来源：https://carlstack.gravito.dev/blog/grok-bot-budget-wake-delegation-guardrails/），社区开源的 ModelScope 命令行项目（来源：https://github.com/RongleCat/tiezhu-modelscope-api-inference）在公开说明中披露，传入的图片、视频和音频数据会被上传至 Uguu 等临时文件托管平台生成公网 URL。你的多模态资产除了流向模型供应商，还经过了未受控的第三方临时存储服务。包含个人凭据、商业机密或未公开业务数据的素材，绝不能图便宜走这类未经审查的外部脚本。

第三是云电脑内的共享安全与封号风险。官方团队文档强调（来源：https://cursor.com/docs/grok-bot/teams），同一个用户下的所有 Bot 共享同一台云电脑、文件系统和浏览器登录态；即便在系统层面对密钥文件设置严格的读写权限，也挡不住共处同一环境的其他 Bot 读取该数据。社区帖称在云电脑中装 Codex 跑自动化，Codex 自己的五小时额度很快就用光了；作者那个没用过的 Claude 免费号后来也被封，原因帖子没说明（个例，来源：https://x.com/i/status/2107100457231651312）。搭建外部执行层必须在受控目录下运行，严格限定访问权限和网络请求。

验证云电脑中 Pi Agent 调用外部模型时的退出码捕获与错误传递。

![外部执行层分流与数据边界](../images/fig-20-3.png)

*图：外部执行层分流与数据边界*
> [!NOTE]
> 📸 **截图位（待补）**：在云电脑终端配置外部 CLI 的交互过程

## 20.4 选档建议 · Which Plan

选档除了看每月花多少钱，更要搞清官方（https://cursor.com/help/grok-bot/plans）公布的真实计费档位、套餐对应关系和防坑规则。

### 2026 年 10 月重磅变革：The X Subscription 三合一统一订阅与旧版独立计划并存规则

2026 年 10 月 18 日，官方正式推出 **The X Subscription** 三合一统一订阅体系（来源：https://cursor.com/help/the-x-subscription/overview 、https://cursor.com/help/grok-bot/plans 与 `@bot` 官方公告 https://x.com/bot/status/2110063783796572496），将 **Grok**、**Cursor** 与 **X Premium** 三大产品线整合进同一个订阅计划中。当前选档必须先认清**新版三合一订阅**与**旧版独立 Cursor 订阅（Legacy Plans）**的双轨规则：

1. **The X Subscription 三合一统一订阅档位（新开户默认及主动合并体系）**：
   - **Free（$0/月）与 Plus（$8/月）**：**不包含** Grok Bot 访问权限（来源：https://cursor.com/help/grok-bot/plans）。
   - **Premium（$30/月）**：性价比最高的个人主力入门档，打包包含 **Grok Bot + Grok（SuperGrok 级体验）+ Cursor IDE + X Premium** 蓝标权益，三端共享同一个每周重置的周额度池（one weekly usage pool）。
   - **Super（$100/月）**：面向高频多 Bot 自动化与重度开发者的进阶档位，提供大幅扩容的三端共享周额度池。
   - **Ultra（$200/月）**：面向全天候多 Bot 蜂群（Swarms）与重度全栈工程团队的旗舰档位，提供最高规格的共享周额度池。
2. **共享周额度池与 Prepaid Credits（预付额度）超额机制**：
   - 在 The X Subscription 下，你在 Grok Bot 跑自动化、在 Cursor IDE 写代码以及在 Grok 对话，**全部从同一个共享周额度池中扣减**（每周固定重置，未用完不结转）。这也是为什么部分用户（如 `@charlie_pmp`，来源：https://x.com/charlie_pmp/status/2114214503416271131）升级三合一后感觉额度比单用一端时消耗更快的原因之一——三端正在共用同一个蓄水池。
   - 当周额度池耗尽，或者你在 Cursor IDE 中调用**非 Grok 系列的第三方模型（third-party models）**时，The X Subscription 不再走旧版的月底后付费账单，而是直接扣减 **Prepaid Credits（预付额度）**（来源：https://cursor.com/help/the-x-subscription/overview）。你需要在 `grok.com/dashboard/billing` 的 `Additional usage credits` 模块充值预付额度，支持配置自动充值（Auto Top-up）与月度额外消费封顶上限（Monthly additional usage limit）。
3. **旧版独立订阅（Legacy Plans）保留与 `cursor.com/unify` 单向不可逆红线**：
   - 先看官方公布的旧版独立套餐标价与档位分布（来源：https://cursor.com/pricing 与 https://cursor.com/cn/help/grok-bot/plans）。在既有独立 Cursor 个人套餐中，Cursor Pro 标价为每月 20 美元，包含 Grok Bot 每周用量，是个人入门门槛；Cursor Pro+ 标价为每月 60 美元，提供充足的每周用量，供主力用户日常使用；Cursor Ultra 标价为每月 200 美元，包含最高的每周用量，专供重度自动化用户。在团队方案中，Cursor Teams 自助版为每人每月 40 美元，团队成员均可使用 Grok Bot，用量计入团队席位额度；社区整理的档位表记录 Teams Premium 席位约为每人每月 120 美元（来源：https://penchan.co/ai/grok/grok-bot/）。
   - 根据官方迁移政策（来源：https://cursor.com/help/grok-bot/plans 与 https://cursor.com/help/the-x-subscription/overview），**既有的 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及自助 Teams（$40/人/月）老订户只要不主动点击合并，依然可以无限期保留原有的独立档位与价格**。
   - 老订户可以随时访问 `cursor.com/unify` 或 `accounts.x.ai/unify` 主动升级合并至 The X Subscription（网页端旧计划会自动按剩余天数比例退费 prorated refund）；但请务必注意两条高压线：第一，**一旦切换至 The X Subscription，操作单向不可逆，永远无法退回 $20/月的旧版独立 Cursor Pro 计划**；第二，如果你原本的 X Premium 或 SuperGrok 是通过 **Apple App Store 或 Google Play** 手机内购订阅的，网页端合并时无法自动取消手机渠道账单，**必须自己去 Apple ID 或 Google Play 订阅管理里手动取消旧内购，否则会遭遇双份扣费**（来源：https://cursor.com/help/the-x-subscription/overview）。

跨平台账号关联的档位，针对尚未迁入三合一体系的旧版独立账号，官方只给了相对顺序：SuperGrok 和 X Premium+ 低于 SuperGrok Plus，Plus 低于 Heavy，Heavy 是最高关联档（来源：https://cursor.com/cn/help/grok-bot/plans）。社区通常按 Pro≈SuperGrok（第三方记录每月 30 美元，来源：https://didreset.com/limits/grok）、Pro+≈SuperGrok Plus（社区整理表记录每月 100 美元）、Ultra≈SuperGrok Heavy（社区整理表记录每月 300 美元）来对照，但官方（https://cursor.com/cn/help/grok-bot/plans）没有写明它们一一对应（来源：https://penchan.co/ai/grok/grok-bot/）。另外，SuperGrok Lite 不包含 Grok Bot 访问权限，无法关联使用（来源：https://cursor.com/cn/help/grok-bot/plans）。

新手最容易踩的一个大坑，是以为买多个会员额度会累加。官方文档（https://cursor.com/cn/help/grok-bot/plans）写得很清楚：**订阅权益绝不叠加，永远以单侧最高档位为准**。比如你订阅了 Cursor Pro+，再去关联 SuperGrok 基础版，系统只取两者中周用量更高的那一个，不会把两边加起来。而且 SuperGrok 或 X Premium+ 与 Cursor 账号的关联一旦建立就是永久的，官方不支持解绑，也无法转移给其他账号（来源：https://cursor.com/cn/help/grok-bot/plans）。关联前必须确认登录的是正确的 Cursor 账号。而在全新的 The X Subscription 下，三大产品天然共用同一个底层账户与额度池，不再需要手动关联。

关于具体额度数字，官方（https://cursor.com/help/grok-bot/plans）目前并未公开确切的 Token 数量或调用次数限制（第三方记录亦证实 xAI 未公布具体数字，来源：https://didreset.com/limits/grok）。社区帖称在 Cursor Pro 档位下，每条交互消息大约消耗 1% 的周额度（个例，来源：https://x.com/miniyarov/status/2105428357273800799）。所有包含的额度均按周重置。至于免费试用，官方明确声明试用给的是一笔固定用量额度，设有 7 天有效期；长任务可能一次性将试用额度耗尽，消耗后系统不会补充或恢复（来源：https://cursor.com/cn/help/grok-bot/plans）。

国内用户目前门槛最低的开通路径，是通过支付宝订阅 Cursor Pro（来源：https://x.com/i/status/2109157438226403420；https://www.amz123.com/t/lZiL8LFi）。在结账页面将币种切换为人民币（CNY），就能通过支付宝完成每月 20 美元的等值扣费，顺利解锁 Grok Bot。

### 2026 年 10 月横向对比与社区黄金双栈选档矩阵

放眼整个 AI 智能体市场，Grok Bot 的定价竞争力如何？加密与 AI 研究员 Wenser（`@wenser2010`，来源：https://x.com/wenser2010/status/2113683422409572523 与 https://x.com/wenser2010/status/2113683427069489614）在 2026 年 10 月 23 日指出，Grok Bot 自 8 月上线以来仅用两个月就突破了 **80 万周付费用户（800K weekly paid users）**，核心原因就在于其降维打击般的定价与生态协同：
- **Grok Bot（The X Subscription Premium 档）**：仅需 **$30/月**，一次打包 **Grok Bot 7×24 云电脑智能体 + X Premium 创作者蓝标与分成资格 + Cursor IDE 编程 + SuperGrok**。
- **OpenAI Dots**：同类自主智能体产品的准入门槛高达 **$100/月**（需绑定 Pro 级订阅起步）。
- **Meta Muse**：虽然表面免费，但严格受限于美国地区 IP 与 Meta 账号准入墙（US/Meta account gated），且缺乏原生开发工具链与实时社交媒体全量数据源。

结合中文新手导师初阳AI（`@chuyang_ai`，来源：https://x.com/chuyang_ai/status/2111357749103911004）以及海外一线 Vibe-Coder 的真实账单配置——包括 `@frogchan9o1`（来源：https://x.com/frogchan9o1/status/2110883156891140416）的 **$50/月双栈共享 Obsidian Vault 方案**，以及重度开发者 Vlady（`@itsvlady`，352 赞 / 55 书签，来源：https://x.com/itsvlady/status/2110803638671020277）的 **$175/月重度双栈方案**，下表为你整理了 2026 年 10 月最新的实战选档决策矩阵：

| 用户画像与典型场景 | 推荐订阅组合与月度总成本 | 核心分工与省钱架构要点 |
| :--- | :--- | :--- |
| **单兵尝鲜 / 自媒体与日常助理**<br>（刚开始搭建 1–3 个 Bot、跑日更情报与 X 运营） | **The X Subscription Premium（$30/月）**<br>*（或保留未迁移的旧版独立 Cursor Pro $20/月）* | 一步到位拿到 X 蓝标、Grok、Cursor 与 Grok Bot（`@chuyang_ai` 与 `@wenser2010` 首推档位）。配合 §20.1 确定性 Python 爬虫与 §20.3 云机挂载 `pi` + DeepSeek，周额度完全够用。 |
| **高性价比全栈 Vibe-Coder（黄金双栈）**<br>（既要本地写复杂项目，又要 24h 云端副驾与第二大脑） | **$20 Claude Code + $30 The X Subscription Premium = $50/月**<br>（`@frogchan9o1` 实测方案） | 极具性价比的“双生态混动”：让本地 Claude Code 与云端 Grok Bot **共同挂载同一个 Obsidian Vault 知识库目录**，Grok Bot 负责全天候抓 X 情报、跑定时 Routine、整理研究笔记落盘；Claude Code 负责读取笔记执行深度代码重构。 |
| **重度独立开发者 / 多项目并行创客**<br>（每天高强度 Vibe-Coding + 多条高频自动化流水线） | **$120 Claude Code + $55–$100 Grok Bot（Super 档 $100/月 或 旧版 Pro+ $60/月）≈ $175–$220/月**<br>（`@itsvlady` 实测方案） | 主力重度编码与大仓库重构由高配版 Claude Code 承担；Grok Bot 升级至 Super（$100/月）或保留旧版 Pro+（$60/月），专职运行 5–10 个全天候业务 Bot、Pages 实时看板与跨平台客服/社媒自动化。 |
| **多 Bot 蜂群工作室 / 企业增长团队**<br>（1 个 CEO 总控 + 10+ 专职 Bot 高并发协同） | **The X Subscription Ultra（$200/月）** 或 **Cursor Teams（$40/人/月）** | 适合像 `@milesdeutscher` 的 10+ Bot 蜂群或 `@CyberAlice3269` 的 6-Bot 内容工作室；开启团队级自定义 Auto-Review 规则，并在 `grok.com/dashboard/billing` 严格设置 Prepaid Credits 的月度消费封顶线。 |

综合官方文档（https://cursor.com/help/grok-bot/plans）和社区实战后的建议很明确：新手入门第一天，不要跟风去买 200 美元的 Ultra，也别急着买 100 美元的 Super（或 60 美元的旧版 Pro+）。新用户直接开通 **30 美元的 The X Subscription Premium**（老用户直接保留或用支付宝订阅 20 美元的独立 Cursor Pro）就够了。先在入门档位把调度器模式、上下文精简、本地轮询脚本和 `pi` + DeepSeek 外部执行层跑顺。要是架构习惯没养好，200 美元的 Ultra 额度同样会在三四天内被死循环烧光。

确实有全天候多 Bot 协同工作需求、且外部脚本分流后周额度依然不够用时，再平滑升级到每月 100 美元的 The X Subscription Super（或旧版每月 60 美元的 Pro+）。不管在哪个档位，设置里的 `Settings > Usage & Billing` 页面都要盯紧。官方版本更新记录显示（官方 v0.25.0，来源：https://x.ai/changelog/bot ），旧版独立计划用户可以在设置中把按需用量月度上限设为关闭、固定金额或无限制；而 The X Subscription 用户则可以在 `grok.com/dashboard/billing` 中管控 Prepaid Credits（预付额度）与月度额外消费上限（来源：https://cursor.com/help/the-x-subscription/overview）。新手必须把按需付费（On-demand）或自动充值（Auto Top-up）保持关闭，或者在后台设一个较低的固定每月限额（Monthly Limit），确保任务意外卡死时损失在可控范围内。

比对 Cursor Pro 档位在运行标准 10 轮文本任务时的周额度百分比衰减曲线。

![Cursor 订阅与 SuperGrok 档位对应及权益不叠加判定图](../images/fig-20-4.png)

*图：Cursor 订阅与 SuperGrok 档位对应及权益不叠加判定图*
> [!NOTE]
> 📸 **截图位（待补）**：Cursor Dashboard 中的 Monthly Limit 支出上限设置界面


# §21 事故档案 · Incident Files

很多人刚上手 Grok Bot，容易把它当成全能员工，银行账户、公司通讯录和社交账号统统交出去。直到银行流水被公开打在公司全员群里，或者辛辛苦苦调了一周的配置一夜之间被系统回滚抹平，才发现底层安全边界和稳定性有多脆弱。这一章我不讲虚的，直接拆过去两个月里社区和企业真实踩过的七起严重事故：Shane Mac 的财务泄露、9/8 云电脑回滚、社交账号封禁、群聊泄密、多 Bot 并发冲突、节点失联，以及 10/8 的调度瘫痪。每一起事故，我都按发生经过、底层原因以及怎么防范三步写透。

![Grok Bot 七起典型事故时间线与影响面一览](../images/fig-21-1.png)

*图：Grok Bot 七起典型事故时间线与影响面一览*

## 21.1 银行审计结果被转发到 Slack · Bank Audit Leaked to Slack

2026 年 10 月 1 日，XMTP Labs 首席执行官 Shane Mac 栽了个大跟头[RuntimeWire](https://runtimewire.com/article/xmtp-shane-mac-grok-bot-bank-audit-slack)。他之前把 Grok Bot 接进了自己的个人银行账户，打算当个只读的私人财务助手，帮着记账打理开销[Cybernews](https://cybernews.com/ai-news/grok-bot-leaks-bank-information/)。结果 10 月 1 日当天，这个 Bot 突然整理出了一份极其详尽的个人月度财务审计报告，把他的个人支票和储蓄账户余额、健身房会员费、家庭装修开支以及大笔信用卡刷卡明细全扒了出来，还直接公开发送到了 XMTP 公司的高管 Slack 频道里[Cybernews](https://cybernews.com/ai-news/grok-bot-leaks-bank-information/)。更要命的是，Bot 发消息时顶着 Shane Mac 本人的名字和头像，高管频道里的同事都看到了这些私人流水[Cybernews](https://cybernews.com/ai-news/grok-bot-leaks-bank-information/)。

事后 Shane Mac 公开复盘，辩解称自己连银行时选的是只读模式，而且那个管财务的 Bot 压根没配 Slack 权限[Cybernews](https://cybernews.com/ai-news/grok-bot-leaks-bank-information/)。但他漏算了 Grok Bot 最关键的底层机制：同一个账号下的所有 Bot 并不是相互隔离的沙盒，它们全跑在同一台云电脑上[docs-computer-and-apps](https://cursor.com/docs/grok-bot/security)。财务 Bot 确实没装 Slack 插件，但他账号下另一个处理日常业务的工作 Bot 有 Slack 发信权限。多个 Bot 共享这台云电脑的文件系统和运行时，据 RuntimeWire 转述，Mac 说问题出在 Bot 搞混了名字相近的对话；至于工作 Bot 是否读取了云电脑上的本地文件，报道没有说明[RuntimeWire](https://runtimewire.com/article/xmtp-shane-mac-grok-bot-bank-audit-slack)。官方安全文档其实早有预警：云电脑是按用户账号分配的，不是按单个 Bot 分配的；切勿在上面存放其他 Bot 不该访问的凭据或文件[approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)。马斯克此前还在网上跟网友打包票说如果搞砸了我们会补偿，这也让不少早期用户放松了警惕[Cybernews](https://cybernews.com/ai-news/grok-bot-leaks-bank-information/)。

要防范这类事故，架构上必须做物理隔离。个人生活助手和公司工作 Bot 绝不能放在同一个 Grok Bot 账号或同一台云电脑下，必须用不同账号隔开。另外别迷信只读权限，就算官方 Finance 连接器基于 Plaid 提供只读抓取[x.com/bot](https://x.com/bot/status/2103936247995752705)，数据只要落到云电脑本地，其他任何有外发能力的插件都能以纯文本形式把数据带出去。凡是向 Slack、邮件等外部通讯工具发内容的写操作，应该在 Auto-review 里为这类动作设 **Ask first** 规则（Ask first 永远优先于 Allow automatically），也不要对外部发信点 **Always allow**[approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)。此外，对于企业或团队环境，官方企业级安全文档（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）现已支持配置自定义 Auto-Review 自然语言规则（策略设为 `Block` 直接阻断或 `Require approval` 要求人工审批），并可开启出站网络白名单配合 `Apply to MCP servers` 选项限制外部通道调用。据 RuntimeWire 转述，Mac 说在 Business Insider 报道发表前一晚，Grok Bot 上线了频道权限方面的改动[RuntimeWire](https://runtimewire.com/article/xmtp-shane-mac-grok-bot-bank-audit-slack)。记住这条铁律：**同一账号下的所有 Bot 共享同一台云电脑，Bot 之间没有任何安全边界**。

> [!NOTE]
> 📸 **截图位（待补）**：设置中关闭 Always Allow 并开启审批卡确认界面

## 21.2 9/8 云电脑回滚 · September 8 Cloud Computer Rollback

2026 年 9 月 8 日北京时间 16:19 左右，Cursor 官方社区论坛被用户的求助帖淹没了[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)。大批用户突然发现，自己在某个时间点之后的所有对话记录、当天新创建的多个 Bot 和群聊全部凭空消失，macOS、Windows 和 iOS 客户端被强行同步成了同一个截断后的旧状态[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)。Windows 用户反馈数据截断点在美东时间 9 月 7 日 20:00[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)。社区帖称有用户丢了好几天的工作产出以及十多个 Bot 的自定义配置（个例）[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)。用户 @Chase_Adams 遇到了更凶险的情况：他的 Bot 在午夜准点执行了劳动节促销降价，回滚后彻底丢了这段记忆，第二天早上居然又问用户要不要调价，要是随手点了确认，就会直接引发二次降价的商业事故[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)。故障刚发生时，不少用户提交工单只收到客服自动回复，称数据无法恢复、建议手动重建[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)。

直到 9 月 8 日 19:12 UTC（北京时间 9 月 9 日 03:12），Cursor 团队员工 @Colin 才在论坛公开了真相[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)（Cursor 员工论坛回复）。官方系统调度时出了 bug，给一部分用户分配了重复的云电脑（duplicate computer），导致这部分用户的新会话被路由到了副本机器上。官方发现后进行热修复，直接删除了这台副本机器，把流量切回了包含历史数据最多的原始电脑。这一删，直接把用户在副本机器上产生的新会话、新配置和临时状态全抹平了，造成了全盘回滚的假象。

这起事故给重度依赖自动化的人提了个醒：核心业务配置决不能只存云端。Bot 的岗位说明书、系统 Prompt、Skill 脚本和环境变量，平时要随手同步备份到本地磁盘或代码仓库。调价、下单、批量发邮件这类不可逆操作，业务系统自身必须做幂等拦截和数据库日志，决不能把已完成凭据寄托在 Bot 的对话记忆里。客户端断连或数据对不上时，千万别盲目去点界面上的 Reset 或 Recover。官方恢复指南明确警告，Recover 和 Reset 都会从上一次成功保存的快照重建环境，最新改动和手动装的软件可能永久丢失；客户端显示 Reconnecting 时绝对别点 Reset，更不能连击[computer-recovery](https://cursor.com/help/grok-bot/computer-recovery.md)。一旦发生 Bot 异常消失，第一时间发邮件给 hi@cursor.com 申请人工处理[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)。**不可逆的业务操作决不能依赖 Bot 的会话记忆来防重**。

> [!NOTE]
> 📸 **截图位（待补）**：官方恢复帮助页关于 Reconnecting 状态禁止 Reset 的警告

## 21.3 WhatsApp 封号与 LinkedIn 会话被踢 · WhatsApp Bans & LinkedIn Session Kicks

不少做社群运营或海外获客的人，拿到 Grok Bot 就想让它全自动发私信。但在没有官方支持的平台上硬上自动化，主力账号很容易当场暴毙。在 Reddit 社区中，社区帖称有用户拿 Grok Bot 接 WhatsApp 跑自动客服，没跑多久两个个人 WhatsApp 账号就被永久封禁（个例）[Reddit](https://www.reddit.com/r/GrokBot/comments/1w11r70/)。LinkedIn 上也是类似情况：社区实测汇总指出，在没有官方插件的情况下，如果让 Bot 在云电脑浏览器里登录 LinkedIn 网页版自动给客户发外联消息，风控系统很快就会识别异常，强行踢掉该账号的所有登录会话，冻结操作权限[learngrokbot.com](https://learngrokbot.com/plugins)。

封号和踢会话的核心原因有两个：机房 IP 和非人行为。Grok Bot 的云电脑部署在公有云机房，出口公网 IP 是标准的数据中心机房段，不是普通家用宽带。WhatsApp 官方根本没给 Grok Bot 做插件支持，其第三方代理条款明确禁止未经授权的自动化程序接入个人生态[whatsapp-legal](https://www.whatsapp.com/legal/third-party-agents-terms)。非官方方式强行接入，机房 IP 加上高频收发包，会立刻踩中反作弊策略。LinkedIn 同样有严密的行为指纹检测，Bot 自动化操控浏览器的 DOM 点击、复制粘贴和表单输入，跟真人操作的鼠标轨迹和按键习惯截然不同，在机房出口流量下一抓一个准。

在社交平台上用 AI，动作边界必须收紧。没有官方受信任插件的高风控平台，绝不能把账号凭据直接交给 Bot 做无人值守自动发送。销售外联或客户跟进场景，应该让 Bot 只负责看公开信息、起草个性化回复，把最终点击发送的动作留给自己在物理手机或电脑上操作，这就是安全文档推崇的草稿优先原则[docs-approvals-security-and-privacy](https://cursor.com/help/grok-bot/approvals-security-and-privacy)。如果仅涉及网页浏览或公开数据读取却因云机房 IP 被拦截或频繁弹出验证码（Captcha），可以参考 `@XueshiQiao`（[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)）分享的方案，在桌面端开启 `Settings > Computer > Your computer > Route traffic through this computer` 借用本机真实住宅 IP 转发流量。自动化任何外部工具之前，先看清对方对第三方 Agent 的官方条款和封禁规则，别拿自己经营多年的核心账号冒险。**没有官方插件的高风控平台绝不能放任 Bot 自主点击发送**。

> [!NOTE]
> 📸 **截图位（待补）**：草稿优先模式下 Bot 生成私信草稿等待人工确认的界面

## 21.4 群聊误输密码 · Passwords Leaked in Group Chats

从单聊变成多 Bot 协同群聊，安全风险会成倍放大。在 X 平台上，社区帖称有用户记录过一次翻车：他在一个包含所有 Bot 的群聊里误输了密码，结果所有 Bot 都"知道"了这个密码（个例）[X 帖 2107339523038331338](https://x.com/i/status/2107339523038331338)。

事故的根源在于多 Bot 群聊的底层通信机制。官方文档说明过，一个群聊里可以放 2 到 6 个 Bot 协同[docs-chat-and-collaboration](https://cursor.com/help/grok-bot/chat-and-collaboration)。官方底层安全机制把审批卡和凭据授权请求做了隔离，系统级敏感卡片不会明文甩在公屏上[docs-chat-and-collaboration](https://cursor.com/help/grok-bot/chat-and-collaboration)。但用户自己在输入框发的内容没有任何敏感词拦截，会直接作为普通对话 Prompt 广播给群里的每一个 Bot。这样一来，不仅所有 Bot 当场读取明文密码，还可能把它存进各自的长期记忆数据库（Memories），甚至在执行终端命令时作为参数写进云电脑日志。

防范群聊泄密，凭据流转必须立规矩。输入框里无论如何都不能直接发 API Key、数据库连接串或登录密码。需要凭据的场景，必须走官方密码管理集成授权。比如官方在 9 月 17 日宣布的 1Password 集成（v0.53.0 起 Mac 端可用）[x.com/bot](https://x.com/bot/status/2100335532597502311)；第三方整理称它只让 Bot 读取名为 Shared with Grok Bot 的单一保险库，其他无关密码不会被读取[learngrokbot.com](https://learngrokbot.com/plugins)。万一手滑误发了密码，千万别在群里叫 Bot 忘掉这段密码或替我保密，正确做法是立刻登录目标系统强制轮换密码，再挨个进每个 Bot 的设置面板，在记忆管理里手动找到并删掉这条历史记录。**群聊输入框是全员广播的明文环境，绝不可作为凭据传递渠道**。

> [!NOTE]
> 📸 **截图位（待补）**：1Password 仅授权 Shared with Grok Bot 单一保险库的设置面板

### 2026-10-22 终极解药：1Password Brokered Sign-in 与内置 Grok Bot Vault 双保险

在早期版本中，很多用户为了避免在对话框里直接发密码或银行卡号，只能依赖每次手动点击 `Take over screen`（人工接管屏幕）去云电脑浏览器里敲密码，或者繁琐地配置旧版 1Password 共享 Vault 与 Service Account Token。到了 2026 年 10 月 22 日至 10 月 23 日（对应官方 v0.75.2 与 v0.75.5 版本，详见 [Grok Bot 官方更新日志](https://x.ai/changelog/bot)），官方接连上线了 **1Password Brokered Sign-in（代理逐次授权登录）** 与内置 **Grok Bot Vault（加密保险箱）**，从底层机制上彻底终结了“在聊天框里明文发密码或发卡号”的历史隐患。

#### 第一重保险：1Password Brokered Sign-in（零共享库、逐次生物识别审批）

2026 年 10 月 22 日，Grok Bot 官方（`@bot`，[https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874)，获 3,663 赞、276 转发、964 书签）与 1Password 官方（`@1Password`，[https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)，获 10,507 赞、1,076 转发、7,122 书签）联合发布了基于 `"1Password for Agents"` 平台的 **1Password Brokered Sign-in**。

根据官方应用连接文档（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）与工作流技术文档（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)），新版集成的工作机制与旧版有着本质区别：
- **告别共享密码库与服务令牌**：用户不再需要专门新建名为 `Grok Bot` 的共享 Vault，也不再需要生成和粘贴 Service Account Token。只需确保本地设备安装并解锁 **1Password app 8.12.42 或更高版本**，然后在 `Settings → Connect apps → 1Password → Connect` 中完成绑定（此前使用旧版方案的老用户，只需点击 `Disconnect` 断开后再 `Reconnect` 重新连接，即可无缝升级至新版代理授权模式）。
- **逐次弹窗生物识别审批（Brokered Approval）**：当 Bot 在云端浏览器中遇到登录框时，会向 1Password 发起凭据请求并在界面弹出 **Review in 1Password** 提示；用户在自己的电脑或手机 1Password 客户端上用指纹、面容或 Passkey 批准本次特定请求后，1Password 会直接将账号密码安全注入 Bot 的浏览器会话中。**在整个生命周期内，Bot 的上下文窗口、聊天记录与记忆库中绝不会出现任何明文密码**。
- **读取范围隔离**：该模式默认仅读取已连接 1Password 账号下 **Personal / Private vault（个人/私有密码库）** 中的条目；存放在团队共享（Shared）或自定义 1Password 库中的机密默认不会被读取，除非用户主动将其移动或复制到 Personal / Private 库中。

#### 第二重保险：内置 Grok Bot Vault（只写加密存储 + `BrowserSecureFill` 底层注入）

紧随其后，官方在 v0.75.5（2026-10-23，`@bot` 官方发布帖：[https://x.com/bot/status/2113754107861532677](https://x.com/bot/status/2113754107861532677)，获 9,398 赞、767 转发、2,756 书签）中正式全面上线了内置加密保险箱 `Settings → Vault`。根据官方 [Secrets & Vault 帮助文档](https://cursor.com/help/grok-bot/secrets)，它专门用于托管三类高频敏感信息：
1. **Logins**：网站登录账号、密码及 2FA/TOTP 动态验证码。
2. **Cards**：信用卡与借记卡（支持在移动端打开 `Settings → Vault → Add card → Scan` 直接用摄像头扫描识别实体卡号）。
3. **Contact info**：常用收货地址、电话号码与电子邮箱。

除了手动添加或在聊天内弹出掩码安全表单（Secure Form）时勾选 **Securely save to Grok Bot's vault** 顺手保存外，用户还可以通过 `Settings → Vault → Import` 批量导入来自 **1Password、Chrome、Safari、Firefox、Bitwarden 或 LastPass** 的 CSV 导出文件（单文件上限 **5 MB**）。

Vault 的核心安全设计在于 **只写（Write-only）架构 + 明文 Hint 标签 + `BrowserSecureFill` 注入**：
- 一旦密码、完整银行卡号或 CVV 安全码存入 Vault，即刻进入只写加密状态，无论是客户端 UI 还是 Bot 的大模型上下文都无法读取或回显明文。
- 用户可以为每个条目编写一段明文 **Hint（提示标签）**，例如 `"Use for work travel only"` 或 `"Corporate Amex"`。Bot **只能读取这段 Hint 文本**来判断当前任务该选用哪一张卡或哪一个账号，随后调用底层专用工具 `BrowserSecureFill` 将加密机密直接填入目标网页的 DOM 输入框中。

#### 新型风险警示案例：Vault 已存银行卡结账“不再触发单独 Vault 弹窗确认”与 SpaceX 赔付兜底

尽管 Vault 彻底解决了卡号与密码的明文泄露问题，但它在自动化结账环节引入了一条极易被忽视的资金风控边界。2026 年 10 月 25 日，英文社区研究者 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）与中文社区博主 `@JianWeiSignal`（见微｜Signal，[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488) 及补充帖 [https://x.com/JianWeiSignal/status/2114195638988501103](https://x.com/JianWeiSignal/status/2114195638988501103)）几乎同时发出安全预警，点出了官方 [Secrets & Vault 帮助文档](https://cursor.com/help/grok-bot/secrets) 中明确记载的一条关键规则：

> **将银行卡保存在 Vault 后，Bot 在结账自动填充该银行卡时，不会触发单独的逐笔 Vault 弹窗确认（a card saved in Vault is filled at checkout WITHOUT a separate per-charge Vault prompt）**，仅受通用购买审批规则约束。

要理解为什么会发生这种情况，必须看清官方 [Work 技术文档](https://cursor.com/docs/grok-bot/work) 定义的登录与结账调用优先级顺序：
- **登录（Sign-in）调用优先级**：Bot 云电脑上已保存的浏览器会话（Saved browser session） → **Vault** → **1Password** → 聊天内 **Secure Form** → **Take over screen（人工接管屏幕）**。
- **结账支付（Checkout / Payment）调用优先级**：**Vault** → 聊天内 **Secure Form** → **Link / X Money** → **Take over screen（人工接管屏幕）**。

这意味着，假设你把主力大额信用卡常驻保存在了 Vault 中，当你在对话里让 Bot 帮你购买某样商品（且在 v0.75.2 精简了当前轮次明确指令的冗余 Auto-review 审批弹窗后），Bot 在结账页面会直接按第一优先级调用 Vault 中的银行卡完成填充，而**不会再额外弹出一个专门针对 Vault 卡片调用的二次确认框**。

针对广大用户对“把银行卡交给 AI 会不会买错东西或被盗刷”的顾虑，Elon Musk（`@elonmusk`）在 2026 年 10 月 15 日公开做出了 SpaceX 官方兜底赔付承诺（[https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445)，获 17,221 赞、1,686 转发、2,128 书签）：

> *"This works well. If Grok @Bot makes a mistake with a purchase or leaks your card (never happened yet), SpaceX will make you whole."*
> （这很好用。如果 Grok Bot 在代购时犯了错，或者泄露了你的银行卡——迄今从未发生过——SpaceX 将全额赔偿你的损失。）

虽然有 SpaceX 的全额赔付兜底背书，但在日常工程与财务风控实践中，我们依然强烈建议你遵循 `@kial`、`@JianWeiSignal` 与 `@martinpaulweiss`（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）总结的凭据分家与防误刷规范：

```markdown
# Grok Bot 凭据管理与支付防呆规范（Vault + 1Password 双保险版）

1. 严禁明文上屏：
   永远不要在单聊或群聊输入框中直接粘贴密码、API Key、银行卡号或 CVV。

2. “一密一宅（One home per secret）”拆分准则（参考 @martinpaulweiss）：
   - 日常重要网站登录凭据 + 2FA 动态码：统一存放在 1Password 中，通过 1Password Brokered Sign-in 每次生物识别弹窗授权。
   - 收货地址与联系人信息：存放在 Grok Bot 内置 Vault 中，供 Bot 自动填表。
   - 临时新注册账号：可暂存 Grok Bot Vault，定期使用类似 @LisaMAUSA 的 Vault Tidy 流程清理并迁回 1Password。

3. 银行卡存储的三级风控策略（参考官方 Secrets 文档与 @kial / @JianWeiSignal 预警）：
   - 策略 A（绝对逐单手输把关）：如果你希望每一笔消费都必须亲手输入并逐单确认卡号，切勿将银行卡保存在 Vault 中（已保存的请进入 Settings → Vault 移除），改在每次结账弹出聊天内 Secure Form 时单次输入，且不要勾选“Securely save to Grok Bot's vault”。
   - 策略 B（专卡专用限额隔离）：若需享受 Vault 自动填卡的便利，建议只存入一张设置了单笔/月度消费限额的虚拟卡或专用副卡（如 X Card），并在 Hint 中明确标注用途边界（例如：`Only use for <$50 food/coffee orders`）。
```

## 21.5 多个 Bot 被网站当成多人登录 · Multi-Bot Concurrent Login Conflicts

有人为了多出活，喜欢搭多个专职 Bot 同时跑：一个在前台抓竞品数据，另一个在后台核对订单。实际运行时，社区帖称有用户的多个 Bot 共用一台云电脑登录同一个网站，被网站当成多人同时登录而封锁（个例，具体是哪个网站、怎么触发的帖子没有细说）[X 帖 2100351900881207770](https://x.com/i/status/2100351900881207770)。

这起事故的原因同样出在共享架构上。官方文档讲过其底层逻辑：同一账户下的所有 Bot，共享同一台持久化的云电脑，以及上面的整个浏览器环境[docs-computer-and-apps](https://cursor.com/help/grok-bot/computer-and-apps)。客户端界面看起来每个 Bot 都有独立屏幕，底层共用的却是同一套浏览器 Cookie、本地存储和出口 IP。两个 Bot 同一秒打开同一个站点的不同页面做交互，目标网站服务器短时间内收到大量来自同一套凭证的并发点击和跳转，完全违背人类单线程操作的物理规律，会立刻触发网站的并发互斥和反爬风控。

避免多 Bot 和网站风控冲突，调度上必须定死规矩。同一个需要登录的站点，必须专人专岗，把该网站的所有操作收拢给唯一一个专职 Bot，严禁多个 Bot 并发操作。如果确实需要多维度监控，就用 Routine 的时间调度错开时间，比如安排 Bot A 整点执行、Bot B 半点执行，保证浏览器环境始终单线程串行。遇到数据量大或更新频繁的需求，优先走官方 API 或 MCP 协议，少用浏览器界面做高频机械点击[workflows](https://x.com/Michael_Fenech_/status/2102048957777981938)。**同一个站点的浏览器操作必须收拢到单个 Bot 串行执行**。

![共享浏览器环境下多 Bot 并发请求导致风控封禁的机制对比](../images/fig-21-2.png)

*图：共享浏览器环境下多 Bot 并发请求导致风控封禁的机制对比*

## 21.6 云电脑连不上与客服响应慢 · Cloud Computer Connection Outages & Slow Support

2026 年 9 月 5 日，LINUX DO 社区发生了一起云端失联事件[LINUX DO t/2860519](https://linux.do/t/topic/2860519)。有用户发帖称自己的 Grok Bot 突然毫无征兆地断开了连接，手机、Mac 和 Windows 端全部卡在加载页面进不去。他在客户端尝试点击 Reset 重置云电脑，直接弹窗报错重置失败。离奇的是，他的 iPad 依然能收到通知，显示后台定时任务还在正常更新网站数据，说明后台程序没崩，只是前端远程串流断了。断连期间用户发帖求助、发邮件给官方，收到的全都是无济于事的自动回复；恰逢美国劳动节长周末（2026 年 9 月 7 日是劳动节），直到"员工上班"后才有真人回复，楼主的感受是"一定要发帖 @ 下马斯克才有回复"，系统当天傍晚 18:00 左右自行恢复[LINUX DO t/2860519](https://linux.do/t/topic/2860519)。9/8 回滚事故中也有类似问题，社区帖称有用户提交工单超过 72 小时毫无进展，还有用户说停用了 4 天（个例）[Cursor Forum](https://forum.cursor.com/t/grok-bot-conversation-history-and-newly-created-bots-groups-suddenly-rolled-back-and-synchronized-across-all-devices/171008)。

这个现象暴露了 Grok Bot 基础设施的架构特征：后台计算容器（Runner）与前台远程桌面串流通道是解耦的双层结构。串流网关或代理出故障时，客户端会显示离线，但底层的无头容器其实还在按脚本跑。如果管理接口本身有问题时点重置，指令送不到容器，就会报错重置失败。更关键的是支持体系的短板，面对突发故障，团队在非工作时间的人工响应极慢，没有企业级全天候保障。

应对这类云端基础设施抖动，有几条原则必须遵守。客户端突然连不上时先别慌，通过手机通知或外部数据变化看看后台 Routine 是不是还在跑；只要定时任务正常，千万别去强按 Reset 或 Recover，免得把活着的容器彻底毁掉。根据官方云电脑恢复指南（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)），强行重置会回退到上一次快照。连不上时第一时间查官方状态页（status.cursor.com）和论坛，确认是不是大面积机房故障[status.cursor.com](https://status.cursor.com)。另外还要顾及海外团队的作息规律，周末和长假基本找不到技术支持，周五晚上或长假前别动核心 Bot 的配置，也别把没有备用兜底方案的重活托付给全自动 Agent。**连接中断时切勿盲目重置云电脑，应先通过外部信号判断后台任务是否存活**。

> [!NOTE]
> 📸 **截图位（待补）**：LINUX DO 社区关于云电脑无法连接但定时任务仍正常通知的反馈

### 官方揭秘：8 月 14 日工单暴增 175% 的幕后真相与 5-Bot 客服舰队逆袭

为什么在 9 月初那段时间，用户普遍感觉官方客服响应慢、甚至工单积压长达数天？2026 年 10 月下旬，xAI 与 Cursor 官方发布了一篇深度复盘战报《Grok Bot Customer Support》（[https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)），首次向外界完整公开了当时客服系统承压的幕后内幕，以及他们随后如何用“Grok Bot 治理 Grok Bot”完成自动化逆袭。

#### 1. 8 月 14 日并入 SpaceXSI 引发的 175% 工单海啸

官方在复盘报告（[https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）中坦言：2026 年 8 月 14 日，当 Cursor 正式宣布并入 **SpaceX SuperIntelligence（SpaceXSI）** 并推出 Grok Bot 后（此后短短两个月内周付费用户便突破了 80 万大关，参见 `@wenser2010` 整理的里程碑数据：[https://x.com/wenser2010/status/2113683422409572523](https://x.com/wenser2010/status/2113683422409572523)），全球涌入的用户咨询、账单合并疑问与早期云电脑故障工单量瞬间暴增了 **175%**。按照传统 SaaS 企业的扩张测算，要消化这波突如其来的工单洪峰，原本至少需要紧急扩招约 **200 名全职客服人员**——这正是 9 月初劳动节长周末期间人工客服应接不暇、恢复滞后的根本原因。

#### 2. 零扩招破局：5 位专职 Bot 组成的官方客服舰队

面对 175% 的工单激增，官方团队没有走盲目扩招人工外包的老路，而是直接用自家的 Grok Bot 搭建了一支由 **5 位专职 Bot** 协同运作的自动化客服舰队（详见官方报告 [https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）：

| 专职 Bot 角色 | 核心职责与自动化闭环链路 |
| :--- | :--- |
| **1. Intake Triage Bot（分诊接待 Bot）** | 第一时间接管所有涌入工单，自动识别用户身份、关联订阅档位（如 The X Subscription 或旧版独立计划），完成意图分类与优先级打标。 |
| **2. Billing & Refund Bot（账单与退款 Bot）** | 自动核查用户的扣费流水、订阅合并记录（如 `cursor.com/unify` 按比例退费状态）与额度消耗明细，对符合规则的申请直接端到端执行退款。 |
| **3. Technical Repro Bot（技术复现 Bot）** | 针对用户报告的客户端 Bug 或云电脑断连异常，自动在隔离沙箱中读取脱敏遥测日志、尝试复现故障路径，并向研发团队输出带完整上下文的诊断单。 |
| **4. Incident Batch Bot（事故批处理 Bot）** | 当监测到类似 9/8 回滚或 10/8 调度队列拥堵等集中爆发的同类线上故障时，自动将数百张同源受影响工单聚类打包，生成一张汇总批量审批卡（Batch Approval Card）交由值班工程师一键确认处理。 |
| **5. Product Feedback Synthesizer Bot（产品反馈聚类 Bot）** | 全天候扫描海量客服对话与社区反馈，每天自动抽取、清洗并聚类超过 **20,000+** 个产品反馈数据点，直接转化为工程研发看板上的改进任务。 |

#### 3. 10 分钟清零 204 张故障单与 99% 退款自动化

这支 5-Bot 客服舰队投产后，交出了一组极具参考价值的工业级量化战果（数据源自官方报告 [https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)）：
- **零新增客服招聘（0 new support hires）**：在工单量暴涨 175% 的高压下，团队未扩招一名全职客服，直接省下了原本需要约 200 人的团队扩张成本。
- **单票解决成本压降至 $0.20–$0.30**：相比传统人工与外包客服行业平均 **$1.00–$4.00** 的单票处理成本，成本直接下降了一个数量级。
- **99% 退款全自动闭环**：实现了 **99%** 的退款申请从资格核验到原路退回的全自动端到端闭环（提醒：若你是通过 `cursor.com/unify` 将旧计划合并升级至 **The X Subscription**——即 Premium $30/月、Super $100/月、Ultra $200/月三合一订阅，网页端直接扣款的旧订阅会自动取消并按比例退费；但根据官方订阅文档 [https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans) 说明，通过 **Apple App Store 或 Google Play** 订阅的账单无法由官方 Bot 自动取消或退费，必须手动前往 Apple ID 或 Google Play 取消，谨防双份扣费）。
- **204 张突发故障工单 10 分钟清零**：在近期一次突发线上事故中，**Incident Batch Bot** 自动将所有受影响用户的工单聚合分类，最终仅由一名值班工程师审核并点击批准了一张批量审批卡（batch approval card），就在大约 **10 分钟**内一次性恢复并妥善回复了全部 **204 张**事故工单，彻底告别了早期“72 小时无人响应”的窘境。

## 21.7 10/8 Routine 批量失败 · October 8 Routine Failures

2026 年 10 月 8 日英国时间中午（约北京时间 19:00）开始，Cursor 官方论坛再次被故障反馈刷屏[Cursor Forum](https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125)。大量用户的定时 Routine 全部瘫痪：准点触发的任务先被无限期延迟，紧接着被批量标为 Failed。这时在对话框给 Bot 发普通消息还能正常回复，但后台自动化调度彻底停摆。很多用户一着急，让 Bot 反复排查原因，或者不断复制、重建并手动测试 Routine；这番折腾不仅没解决问题，还白白烧光了大量额度：社区帖称有用户一天耗光了 30% 的周额度，甚至有人周额度直接烧到 90% 以上，离额度刷新还有整整 5 天（个例）[Cursor Forum](https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125)。部分点了重置的用户还遇到了二次打击：主 Bot 频繁报 Bot failed to respond / Something went wrong 彻底陷入死寂，原因是在排查中聊到了敏感词（如 AI 漏洞扫描工具），触发了模型方的安全过滤器（Safety Filter），此后每次发消息都因携带完整历史记录而被模型后端静默拒答[Cursor Forum](https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138)。

Cursor 团队员工 @deanrie 和 @kevinn 在论坛给出了原因说明[Cursor Forum](https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125)（Cursor 员工论坛回复）。事故源于平台突发极高负载（very high load / very high demand），导致云端中央调度队列严重积压超时。官方强调，手动暂停、恢复、复制或重建 Routine 毫无作用；更重要的是，官方系统明确规定错过的运行不会自动补跑（missed runs are not automatically rerun）。当时 status.cursor.com 上显示的状态恢复是指另一项故障已解决，并非 Routine 调度恢复。针对 Bot 触发安全过滤器变哑巴的情况，员工 @kevinn 进一步指出，当前客户端无法单独删减某段特定的对话历史，只要上下文里有被过滤器锁定的违规词，Bot 的每次回复都会被直接掐断，此时重启或 Reset 都没用[Cursor Forum](https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138)（Cursor 员工论坛回复）。

遇到调度瘫痪和安全拦截，止损办法必须明确。一旦发现 Routine 连续超时或批量 Failed，严禁让 Bot 在对话框里帮忙排错，每次排查都会把长串报错日志吃进上下文，几下就能烧光有限的周额度；应该立刻停手，直接去论坛和状态页确认是否是大面积拥堵。尤其在 2026 年 10 月 18 日上线 **The X Subscription 三合一统一订阅**（包含 Grok Bot 的档位为 **Premium $30/月**、**Super $100/月**、**Ultra $200/月**，Free $0 与 Plus $8/月不含 Grok Bot；既有独立 Cursor Pro $20 / Pro+ $60 / Ultra $200 / Teams $40 老订户可保留原计划，或通过 `cursor.com/unify` 单向不可逆切换至新订阅，详见 [https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans) 与 [https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）以及 v0.75.2 将 Routine 频率上限大幅提升至 **全账号所有 Bot 合计 300 次/小时、单条 Routine 最高 200 次/小时**（定时最小间隔仍为 5 分钟，详见 [https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）之后，正如 `@charlie_pmp`（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）所提醒的，Grok Bot、Grok 与 Cursor 三端现在共享同一个周额度池（超额后扣减 Prepaid Credits 预付额度），高频冗余的 Routine 重试会更快抽干三端共享额度。既然官方队列恢复后绝不补跑错过的任务，对数据连续性有要求的关键 Routine，提示词里必须写上时间窗口回溯和幂等逻辑，保证下次成功跑起来时能自动核对时间戳并补齐数据，或者像 `@StarkLJM`（[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377)）那样让 AI 生成确定性 Python 脚本来跑日常轮询以做到零模型额度消耗。涉及漏洞分析或敏感安全词的研究，单独开专用的测试 Bot 去做；一旦某个 Bot 触发 Safety Filter 陷入沉默，千万别让其他正常 Bot 去读取或总结它的历史，否则同样的内容会被带过去，那个 Bot 也会跟着被拦[Cursor Forum](https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138)（Cursor 员工论坛回复）。**Routine 调度队列错过的运行不会自动补跑，故障排查切忌让 Bot 空耗周额度**。

> [!NOTE]
> 📸 **截图位（待补）**：Routine 全部失败且运行记录显示 Failed 的排查界面


# §22 常见故障速查 · Troubleshooting

> **用法**：遇到问题先看 22.7 速查表，再跳到对应小节。**原则**：先做破坏性最小的操作，Reset 永远放在最后。

## 22.1 登录与授权异常：浏览器未聚焦、Legacy Privacy Mode 与手机号拦截 · Sign-in & Authentication

翻阅官方排错文档可以发现，新手最容易被卡住的第一关就是登录中断。很多人在浏览器里点完登录就切去做别的事，结果回到桌面客户端，发现它一直卡在欢迎页。官方排错指南给出的硬性要求是：浏览器认证的全过程中，Grok Bot 桌面客户端必须保持打开（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。要是浏览器已经提示 Cursor 登录成功，客户端却没有自动拉回前台，别去反复刷网页。直接手动切回桌面应用，在欢迎界面重新点 Sign in；若是已经在客户端里，就进 Settings 点 **Sign In with Cursor** 重新拉起绑定（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。开通企业 SSO 的团队，必须走组织统一通道登录，不能混用个人账号（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。

> [!NOTE]
> 📸 **截图位（待补）**：浏览器授权完成但客户端未响应及手机号拦截报错界面

客户端弹出 Legacy Privacy Mode 报错，不用慌，不是安装包坏了。这是因为当前登录的 Cursor 账号开了旧版隐私模式，把 Grok Bot 需要的云端持久化存储挡住了（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。遇到这种情况，进 Cursor 账号设置调整数据隐私模式，或者联系企业管理员放行即可（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。

针对国内用户常遇到的手机号拦截，V2EX 社区有案例记录：用 SuperGrok 凭据登录 Grok Bot 时，系统强制弹手机号验证，输入国内手机号甚至接码平台号码都会报错“无法验证此电话号码。请尝试其他号码。”（https://www.v2ex.com/t/1241829 社区帖称，个例）。帖子下只有一条回复给出解法："美国 ip +86"，即切到美国网络环境后再提交 +86 号码，是否有效未经证实（https://www.v2ex.com/t/1241829 社区帖称，个例）。

除了客户端本身的授权流程外，当 Bot 在云端浏览器中执行登录或调用第三方连接器时，还有三类高频拦截与认证异常需要重点排查：

1. **网站封禁云服务器机房 IP 或狂弹 Captcha 验证码**：因为 Grok Bot 默认运行在云端沙箱（cloud box）中，部分防爬策略严格的电商、金融或内容平台会直接拦截数据中心机房 IP，导致页面返回 403 Forbidden 或陷入无休止的 Cloudflare / Captcha 人机验证死循环。针对这一痛点，社区用户 `@XueshiQiao`（Xueshi，[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)）给出了经过验证的一键排错解法：在保持本地桌面端在线的前提下，进入 `Settings > Computer > Your computer`，开启 **`Route traffic through this computer`**（通过本机路由流量）。开启后，云端浏览器的出站请求会借用你家里或办公室桌面的真实住宅 IP（Residential IP）出站，瞬间绕过机房 IP 封锁。此外，官方在 v0.75.5 版本更新中（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）专门修复并加固了本地电脑流量转发的底层连接稳定性。
2. **1Password 找不到登录条目或无法拉起授权弹窗**：官方在 v0.75.2（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与 [Connect Apps 指南](https://cursor.com/help/grok-bot/connect-apps)中上线了 1Password Brokered Sign-in（代理逐次授权登录）。如果你明明在 1Password 里存了账号，Bot 却提示找不到对应登录项，请按三步排查：
   - 第一，确认本机安装的 **1Password 桌面客户端已升级至 8.12.42 或更高版本**，且当前处于已解锁（Unlocked）状态（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。
   - 第二，核查密码库（Vault）归属位置。根据官方 [Work 技术文档](https://cursor.com/docs/grok-bot/work) 与 [Connect Apps 指南](https://cursor.com/help/grok-bot/connect-apps)规定，Brokered Sign-in 模式默认**仅读取已连接账号下的默认 Personal / Private vault（个人/私有密码库）**；存放在其他共享库（Shared vaults）或自定义密码库中的条目不会被读取，需将目标条目移动或复制到 Personal / Private 库中。
   - 第三，如果你此前配置过旧版的“新建 `Grok Bot` 共享 Vault + 粘贴 Service Account Token”方案，只需进入 `Settings → Connect apps → 1Password`，点击断开（Disconnect）并重新连接（Reconnect），即可无缝迁移至新版逐次生物识别审批模式（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。同时注意官方登录调用的严格优先级顺序：云电脑已保存的浏览器会话（Saved browser session） → **Grok Bot Vault** → **1Password** → 聊天内 **Secure Form** → **Take over screen（人工接管屏幕）**（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）。
3. **X 插件缺少 X Chat / Calls / Livestreams / Spaces / Lists 工具或报 `tools=0`**：当你在对话中让 Bot 帮自己分拣 `@chat` 私信、管理陌生人消息请求（`@pjvann`，[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)）、创建预约通话（`schedule_call`）、管理 RTMP 直播推流或维护列表（Lists）时，若 Bot 报错提示 `user-X-* not found`、`tools=0`，或者只能查公开帖子却找不到私信与直播工具，这属于插件授权未刷新而非付费墙限制。解决方法是打开 `Settings → Connect apps`，找到 **X** 插件执行断开并重新连接（**Reconnect**），即可拉取完整的最新工具集（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。此外，针对 X Chat 端到端加密私信（`xchat_lite`）解密失败的问题，由于 MCP 接口仅下发加密载荷与 Juicebox 配置，需确认 Bot 已在云电脑沙箱内成功克隆官方解密辅助仓库 [https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper) 运行本地解密脚本 `xchat_tool.py`，并且你向其提供了正确的 **4 位数字 X Chat PIN 码**。

## 22.2 中文复制粘贴变乱码：v1.14.0 的编码陷阱 · Chinese Clipboard Encoding Bug

中文环境下的文本复制踩过一个特定版本的坑。V2EX 社区反馈，客户端英文回复复制粘贴完全正常，但复制中文回复粘到外部输入框或编辑器时，文字全变成了乱码（https://www.v2ex.com/t/1247756 社区帖称，个例）。

> [!NOTE]
> 📸 **截图位（待补）**：v1.14.0 中文回复复制粘贴后乱码与无格式粘贴对比

该问题被定位在 **Grok Bot 1.14.0** (17267) 构建版本，运行环境为 runtime e9651e08edc0248a43ce2d13839fa55c7d2e1425，安装包是 embedded bundle，发布通道是 production（https://www.v2ex.com/t/1247756 社区帖称，个例），X 上也有公开的操作录屏（https://x.com/liuxu_qingdao/status/2108527380570816747 社区帖称，个例）。原帖没有给出原因，官方也没有说明。遇到这种乱码，应急办法是用无格式纯文本粘贴快捷键：Mac 按 Command-Shift-V，Windows 按 Ctrl-Shift-V，该快捷键从 v0.30.0 开始在客户端内支持（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。也可以直接让 Bot 把大段中文输出为云电脑 `/workspace` 下的文件再打开。

在 macOS 与 Windows 客户端分别测试 v1.14.0 以后版本的中文剪贴板编码行为。

## 22.3 云电脑卡死与无法连接：Update、Recover 与 Reset 的严格处置阶梯 · Computer Recovery

云电脑一直停在 Starting your computer、Updating your computer、Reconnecting 或 Couldn't Reach Grok Bot's Computer 时，很多人第一反应是点 Reset，这是非常危险的误操作。官方文档明确指出：对话历史独立于云电脑存储在外部，云电脑临时断连甚至终端里误敲了 `rm -rf`，聊天记录都不会丢（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。排查必须严格遵守破坏性由低到高的处置阶梯（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)、[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）：

1. 等待与重试。系统提示重连时，Bot、文件和登录态都处于受保护状态，切勿在此期间执行重置（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。
2. 彻底退出客户端并重启。Mac 用户必须从顶部菜单栏选 Quit，不能只关主窗口（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。

> [!NOTE]
> 📸 **截图位（待补）**：Settings > Computer 中 Update、Recover 与 Reset 操作面板

3. 检查云电脑镜像更新。在 Settings > Computer（或 Settings > Updates，手机端路径为 Settings > Bot > Bot Computer）看是否有更新提示（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting), [https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。官方把更新分两类：软件更新只刷 Grok Bot 程序本身，保留包括自行安装应用在内的所有数据；整机更新会重建整台云电脑，保留 Bot、持久化文件和登录态，但会清掉自行安装的软件包（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。如果提示文件未完成备份，Update 会自动停止，此时应继续等待备份完成，绝不能强行用 Reset 覆盖（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。如果提示有智能体无法及时暂停，等当前任务结束再点更新（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。
4. 使用 **Recover computer**。重连彻底没反应，或者更新卡死并出现该按钮时，才选 Recover（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。Recover 会尽量保存已有数据并在最新镜像上拉起新机器，这会中断正在运行的任务，并清理自行安装的软件包和未及时同步的极近期修改（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。
5. 最后保底才用 Reset。只有 Recover 和 Update 都失效，且你确认能接受丢失最近未同步数据时才能执行（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。Reset 会基于上一次成功保存的快照强制重置机器，未同步内容和自行安装的软件包都会被清除（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。更新或重置还在跑时，绝对不要点第二次。如果 Recover 或 Reset 失败，最多点一次 Retry，再次失败必须立刻停止并提工单（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。

另外，磁盘空间不足警告（Computer is low on disk space）并不是丢数据，侧栏 Disk Saver 会给出清理建议，只有经你确认后才会清理指定的电脑文件，绝不会碰对话记录（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。社区里有用户提到 9/8 重复电脑事故后周额度"确实重置了"，但没有收到邮件，这次重置是不是补偿无法确认（https://www.v2ex.com/t/1241225 社区帖称，个例）。

## 22.4 Routine 不执行与 50 分钟后台任务超时 · Routines & Background Hangs

定时任务挂上去后毫无反应，先对照官方给出的六项清单自检：Routine 开关是否启用、排程时间规则与时区是否吻合、所属 Bot 是否存在且未被删除、依赖的插件是否仍有效认证、云电脑网络能否联通目标外部服务、账号额度或按需消费上限是否耗尽（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。如果是 Slack 或 GitHub 触发的事件型 Routine，还要核对对应的频道、仓库和事件规则是否仍然有效（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。如果是基于专属邮箱 `+alias` 加号子别名（例如 `mybot+newsletters@mail.grokbot.com`，由官方工程师 `@SamSokolin` 发布，[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)）定向触发的邮件型 Routine，还需检查发件方的收件地址后缀与 Routine 过滤条件中的 `+alias` 字符串是否完全匹配（[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)）。

此外，排查高频触发的 Routine 被系统限流拦截时，需对齐 v0.75.2 最新上调后的官方速率限制标准（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)、[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）：**全账号所有 Bot 合计最高运行 300 次/小时（300 runs per hour across all Bots），单条 Routine 最高运行 200 次/小时（200 runs per hour for a single Routine）**，而定时排程（Schedule）的最小触发间隔仍为 5 分钟。至於额度耗尽导致的停摆，还需区分你当前所处的订阅体系（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）：如果你已升级至 **The X Subscription 三合一统一订阅**（包含 Grok Bot 的档位为 Premium $30/月、Super $100/月、Ultra $200/月，Free $0 与 Plus $8/月不含 Grok Bot），Grok Bot 与 Grok、Cursor 共享同一个周额度池（weekly usage pool）；正如 `@charlie_pmp`（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）所拆解，三端共用周池叠加后台未精简的高频 Routine 是周额度提早见底的两大主因。在 The X Subscription 下，周额度耗尽后不再走旧版后付费账单，而是从 `grok.com/dashboard/billing` 充值的 **Prepaid Credits（预付额度）** 中扣除，若未充值预付额度或触及月度额外消费封顶上限（Monthly additional usage limit），Routine 便会因额度不足停止执行；而尚未通过 `cursor.com/unify` 单向切换（注意：一旦切换至 The X Subscription 即不可逆退回旧版计划）的既有独立 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及 Teams（$40/人/月）老订户，则仍受原有的 `On-demand monthly limit` 控制（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。

> [!NOTE]
> 📸 **截图位（待补）**：Routine 运行历史报错与 50 分钟后台超时提示

检查历史运行记录时，如果想手动触发测试，官方明确强调 **Test run** 会真实执行外部操作并产生实质动作，必须使用安全参数，严禁用危险输入试跑（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。

后台任务悄无声息死掉，关键机制在于后台硬超时。Cursor 论坛里有用户贴出过系统提示"A background task was stopped after 50 minutes so it would not hang"，说明后台任务跑满 50 分钟会被强制终止（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138）。长流程的批量扫描或数据处理如果没有拆分子任务，就会被强制切断。另外客户端从 v0.21.0 开始支持通过 Webhook URL 与 Webhook key 外部调用 Routine（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)），v0.52.0 支持暂停与恢复（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)），排查偶发故障时可以先置为暂停逐步调试。

在实际搭建跨端自动化与后台 Shell 任务时，社区还攻克了两项极具代表性的死锁与报错难题：

1. **在 Agent Shell 中调用 `pi -p "..."` 等非交互式 CLI 工具无限挂起卡死**：不少用户效仿 `@hppzyy`（[https://x.com/hppzyy/status/2111573227881529454](https://x.com/hppzyy/status/2111573227881529454)）的做法，在 Grok Bot 云电脑里安装轻量级 Pi Agent（`pi`）或各类 CLI Worker 来省额度处理长文本，但在 Agent 的非交互式 Shell 中执行 `pi -p "..."` 时，命令却会永远卡住不返回，直到拖满超时。社区开发者 `@37FlowAI`（[https://x.com/37FlowAI/status/2111334386339823687](https://x.com/37FlowAI/status/2111334386339823687)）分享了 Grok Bot 自主定位出的底层根因与一行修复方案：许多 CLI 工具在非 TTY 环境下启动时，会默认阻塞等待标准输入（`stdin`）的 `EOF` 结束信号。只需在命令末尾显式追加 **`< /dev/null`** 立即闭合标准输入，就能从无限挂起变为毫秒级瞬间返回：

```bash
# ❌ 错误写法：在 Agent 非交互式 Shell 中等待 stdin EOF 导致无限挂起
pi -p "只回复OK"

# ✅ 正确写法（@37FlowAI 验证）：追加 < /dev/null 闭合标准输入，瞬间返回结果
pi -p "只回复OK" < /dev/null
```

2. **向 Grok Bot Webhook 推送任务返回 HTTP 400 报错**：当你从本地 Claude Code、Codex 或外部自动化脚本向 Grok Bot 的 Routine Webhook 推送包含多行提示词、特殊转义字符或复杂嵌套结构的 JSON 载荷时，有时会遭遇 Webhook 端点严格的 Schema 校验拦截并返回 **HTTP 400 Bad Request**。针对这一痛点，社区开发者 `@mikan77_aoi`（橘子🍊，[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）设计了一套零外部依赖、零守护进程（zero-daemon）的纯 Python 标准库（`urllib.request` + `json`）桥接脚本：彻底绕开脆弱的静态 Webhook 载荷限制，仅用 **4 次标准会话 API 调用**（1. 校验身份与目标 Bot 状态 → 2. 创建或定位目标会话 Thread → 3. 直接向会话注入结构化任务消息 → 4. 触发异步执行并回收状态回执），即可让本地 Claude Code 100% 稳定地将长篇上下文任务交接给云端 Grok Bot：

```python
#!/usr/bin/env python3
"""
绕过 Webhook HTTP 400 限制的 4-API-Call 纯标准库派单桥接器
参考实战范式：@mikan77_aoi (https://x.com/mikan77_aoi/status/2111043148088816045)
"""
import json
import os
import sys
import urllib.request

API_BASE = os.environ.get("GROKBOT_API_BASE", "https://cursor.com/api/bot/v1")
API_TOKEN = os.environ["GROKBOT_API_TOKEN"]
BOT_ID = os.environ["GROKBOT_ID"]

def api_call(method: str, path: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def dispatch_task_in_4_calls(prompt_text: str) -> str:
    # Call 1: 获取并校验目标 Bot 在线状态
    bot_info = api_call("GET", f"/agents/{BOT_ID}")
    # Call 2: 为本次跨端交接创建或获取活跃会话上下文
    thread = api_call("POST", f"/agents/{BOT_ID}/threads", {"title": "CLI Bridge Handoff"})
    thread_id = thread["id"]
    # Call 3: 直接写入完整的多行 Markdown 任务指令（避免 Webhook JSON 400 报错）
    msg = api_call(
        "POST",
        f"/agents/{BOT_ID}/threads/{thread_id}/messages",
        {"role": "user", "content": prompt_text},
    )
    # Call 4: 触发云端 Runner 异步执行并返回 Run ID
    run = api_call(
        "POST",
        f"/agents/{BOT_ID}/threads/{thread_id}/runs",
        {"message_id": msg["id"], "wake_on_done": True},
    )
    return f"Dispatched to {bot_info.get('name', BOT_ID)}: thread={thread_id}, run={run['id']}"

if __name__ == "__main__":
    task = sys.stdin.read().strip() or "请汇总今日 X 平台核心动态并更新 Page 看板"
    print(dispatch_task_in_4_calls(task))
```

## 22.5 邮件与消息发不出：草稿卡片、虚拟机假死与发送报错 · Email & Message Delivery Issues

Bot 答应发邮件或 Slack 消息后迟迟没有动静，往往不是网络断了，而是卡在审批环节。从 v0.45.0 开始，系统引入了草稿卡片机制，Bot 起草的内容会先以卡片形式呈现在对话里，必须由人工点击 Send 或 Discard 才会发出去（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。虽然 v0.64.0 增加了 Disable drafts for this Bot 选项允许跳过卡片直接发送（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)），且 v0.75.2 进一步精简了用户在当前对话轮次已明确授权指令时的冗余 Auto-review 审批弹窗（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)），但在开启团队策略的环境下，管理员配置的全局 Auto-review 规则优先级最高：系统中的 **Ask first**（或企业自定义规则中的 `Block` / `Require approval`，[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）规则永远优先于 Allow automatically 规则（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。动作只要命中审批规则就会生成等待批准的卡片，卡片放着约 10 分钟不处理就会自动过期失效（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。

> [!NOTE]
> 📸 **截图位（待补）**：邮件草稿确认卡片与 Ask first 审批拦截界面

附件不合规也会直接导致发送失败。官方文档有硬性指标：单个普通文件不得超过 25 MB，视频文件不得超过 200 MB，桌面端单次最多上传 6 个附件，且文件不能带密码保护或加密措施（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。罕见格式应提前在本地转成 PDF、CSV、纯文本或常见图片格式后再上传（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。此外，如果你此前遇到过让 Bot 转发邮件时丢失排版格式、正文图片裂开或原邮件附件漏发的问题，只需将客户端升级至 **v0.75.2 或更高版本**——根据官方更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与 [Agent Email 官方文档](https://cursor.com/help/grok-bot/agent-email)，v0.75.2 已原生支持在转发邮件（含 `@mail.grokbot.com` 专属邮箱及已连接的外部邮箱）时**完整保留原邮件的 HTML 富文本排版、正文内嵌图片（inline images）以及全部文件附件**。

论坛还出现过客户端输入框被锁定发不出消息、但右侧虚拟机画面依然完全正常的界面假死情况（https://forum.cursor.com/t/grokbot-can-not-send-msgs-agents-virtual-machine-is-still-visible/170843 社区帖称，个例）。如果当前正有未完成的 computer-use 任务占用操作锁，先在输入框发送“Stop now”强制终止，或者接管云电脑画面手动关闭卡死页面，释放控制权后再发指令（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。

## 22.6 安全过滤静默拦截：被“毒化”的 Bot 与不可逆的会话死锁 · Safety Filter Silent Failure

2026 年 10 月 8 日至 9 日，Cursor 官方论坛曝光了一起典型故障：v0.68.1 客户端中，用户的主 Bot 突然瘫痪，发任何内容都会弹通用报错，但同账号下的其他 Bot 却完全正常（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138）。

> [!NOTE]
> 📸 **截图位（待补）**：Bot failed to respond 通用报错与已被毒化的会话状态

Cursor 官方工程师 @kevinn 于 10 月 9 日 07:36 CST 公布了排查结论：Bot 后台 runner 并没有卡死，原因是底层大模型服务商的安全过滤器把该 Bot 历史对话中的某段内容判定为违规（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。Grok Bot 每次生成回复都必须把完整上下文历史打包发给模型，哪怕用户只发一句问候，请求中携带的历史违规内容也会立刻触发安全拦截，导致模型拒绝返回结果（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。当时客户端前端没区分这种安全拦截，只能直接显示一行通用提示 **Bot failed to respond / Something went wrong**（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。

这一事故暴露了不可逆的设计痛点：重启应用和 Reset 云电脑对该故障完全无效。会话数据存放在云电脑外部，Reset 不会清空历史，且客户端当时没有单独删除单条历史记录的功能（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。官方工程师给出了处置规矩：不要尝试 Reset 电脑，也不要删除这个 Bot，把它的已有记忆和 Routine 留在原地；日常任务立即切到其他正常 Bot 或新建 Bot；绝对不要让新 Bot 去读取、总结或续写这个中毒 Bot 的历史对话，否则会把违规内容搬到新会话里，导致新 Bot 被连带封锁（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。根据发帖用户自述，诱因是曾让该 Bot 探讨过 AI 安全漏洞扫描工具（基于论坛用户自述背景推测，https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138）。因此，涉及安全测试、逆向工程等边缘领域的内容，必须严格放在一次性隔离 Bot 中运行。

## 22.7 常见故障与排错动作速查 · Quick Troubleshooting Matrix

下表与分级说明把高频异常的症状与官方处置决策梳理成了速查阶梯。

![Grok Bot 故障症状与分级排错动作决策流](../images/fig-22-1.png)

*图：Grok Bot 故障症状与分级排错动作决策流*

登录与授权环节：认证无法完成时，先确认浏览器登录成功后手动切回客户端，在 Settings 中点 Sign In with Cursor 重新拉起；遇到 Legacy Privacy Mode 报错，调整 Cursor 账户数据设置或联系管理员解除限制（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）；境内账号绑定遇手机号无法验证，可尝试切到美国 IP 后重新提交 +86 号码（仅一条社区回复，未证实）（https://www.v2ex.com/t/1241829 社区帖称，个例）。当目标网站封禁云服务器机房 IP 或频繁弹 Captcha 验证码时，开启 `Settings > Computer > Your computer > Route traffic through this computer` 借用本机住宅 IP 出站（`@XueshiQiao`，[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)；v0.75.5 已修复转发稳定性，[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。当 1Password 找不到登录条目时，确认本机 1Password 已升级至 **8.12.42+** 且处于解锁状态，并确保账号存放在默认的 **Personal / Private vault** 中；旧版 Service Account 用户可在 `Settings → Connect apps` 中断开并重连 1Password 完成迁移（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）。当 X 插件缺少 X Chat、Calls、Livestreams、Spaces 或 Lists 工具或报 `tools=0` 时，在 `Settings → Connect apps` 中重新连接（Reconnect）X 插件；解密 X Chat 私信需在沙箱克隆 [https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper) 并提供 4 位 X Chat PIN。

文本复制与输入环节：v1.14.0 中文回复复制粘贴乱码，按 Command-Shift-V（Windows 为 Ctrl-Shift-V）无格式粘贴，或直接从云电脑 `/workspace` 下载导出文件查看（[https://x.ai/changelog/bot](https://x.ai/changelog/bot), https://www.v2ex.com/t/1247756 社区帖称，个例）。

云电脑与环境恢复环节：连接中断或更新停滞时，严格遵循 Retry → 菜单栏 Quit 彻底重启 → Update → Recover → Reset 的顺序操作；未同步前严禁盲目 Reset，一次恢复尚未结束绝不启动第二次（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。单个 Bot 突发持续静默并抛出通用报错时，切勿重置电脑，判定为安全过滤器毒化死锁后，直接换新 Bot 承接任务，严禁让新 Bot 读取中毒历史（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 （Cursor 员工 @kevinn 回复））。

自动化与消息交互环节：Routine 停摆需逐项核查排程时区、Bot 存续状态、插件认证、v0.75.2 频率上限（**全账号合计 300 次/小时、单条 Routine 200 次/小时**，[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）与 50 分钟超时（社区报告），手动验证仅能使用安全输入跑 Test run（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting), https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138）；若在 Agent Shell 中调用 `pi -p "..."` 等非交互式 CLI 挂起卡死，在命令末尾追加 **`< /dev/null`** 闭合标准输入（`@37FlowAI`，[https://x.com/37FlowAI/status/2111334386339823687](https://x.com/37FlowAI/status/2111334386339823687)）；若向 Webhook 推送任务返回 HTTP 400 报错，改用 `@mikan77_aoi`（[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）的 4 次 API 调用纯标准库 Python 脚本直接通过会话 API 派单。邮件与消息未发出优先排查 Auto-review 的 Ask first 规则及卡片状态，附件严格控制在 25 MB（视频 200 MB）和 6 个文件上限内，转发邮件丢失 HTML/内嵌图片/附件则需升级至 v0.75.2+（[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)）；界面锁死可随时发送 **Stop now** 终止当前阻塞动作（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。

计费、移动端与客户端高频问题环节（涵盖官方 [FAQs](https://cursor.com/help/grok-bot/faqs) 与 Cursor / Grok Bot VP of DX `@leerob` 发起的 $100 X Money 真实反馈悬赏汇总帖 [https://x.com/leerob/status/2113792409448714468](https://x.com/leerob/status/2113792409448714468)）：

| 故障类别 | 典型症状与报错表现 | 根因定位 | 标准排错动作与权威信源 |
| :--- | :--- | :--- | :--- |
| **登录与反爬拦截** | 云端浏览器访问站点弹 403 或无限 Captcha 验证码 | 目标网站封禁了云服务器机房 IP | 开启 `Settings > Computer > Your computer > Route traffic through this computer` 借用本机住宅 IP 出站（`@XueshiQiao`，[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)；v0.75.5 已修复，[https://x.ai/changelog/bot](https://x.ai/changelog/bot)） |
| **1Password 授权** | Bot 提示找不到 1Password 中的网站账号或无法弹窗审批 | 1Password 版本过低、未解锁，或条目不在默认 Personal/Private 库中 | 升级本机 1Password 至 **8.12.42+** 并保持解锁；将条目移入默认 **Personal / Private vault**；旧版 Service Account 用户在 `Settings → Connect apps` 中断开重连（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)） |
| **X 插件工具缺失** | 找不到 X Chat / Calls / Livestreams / Spaces / Lists 工具或报 `tools=0` | X 插件授权未同步最新工具表，或沙箱缺少本地解密辅助工具 | 在 `Settings → Connect apps` 中 **Reconnect** X 插件（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）；X Chat 解密需克隆 [https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper) 并输入 4 位 PIN |
| **Shell 进程挂起** | Agent Shell 中运行 `pi -p "..."` 等非交互式 CLI 无限卡死 | 子进程在非 TTY 环境下一直阻塞等待 `stdin` 的 `EOF` 信号 | 在命令末尾追加 **`< /dev/null`**（如 `pi -p "只回复OK" < /dev/null`，`@37FlowAI`，[https://x.com/37FlowAI/status/2111334386339823687](https://x.com/37FlowAI/status/2111334386339823687)） |
| **Webhook 400** | 外部或本地脚本向 Routine Webhook 推送复杂 JSON 返回 HTTP 400 | Webhook 端点对复杂嵌套或特殊转义载荷校验失败 | 改用 `@mikan77_aoi` 的 4 次 API 调用纯标准库 Python 脚本直接通过会话 API 派单（[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)） |
| **邮件转发丢格式** | Bot 转发邮件后丢失 HTML 样式、内嵌图片或附件 | 旧版客户端邮件转发未做富文本与 MIME 附件穿透 | 升级至 **v0.75.2+**，原生保留完整 HTML、内嵌图片与附件（[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)） |
| **合并订阅双份扣费** | 在 `cursor.com/unify` 合并升级 The X Subscription 后仍被旧账单扣款 | 网页端直连账单会自动按比例退费，但 **Apple App Store / Google Play 渠道账单无法被官方自动退订** | 合并至 The X Subscription（Premium $30 / Super $100 / Ultra $200）后，必须立即前往 iPhone **Apple ID 订阅管理**或 **Google Play 订阅页**手动取消旧订阅（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)、[https://cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)） |
| **Action Button 找不到指令** | iPhone 设置操作按钮（Action Button）或快捷指令时看不到 Grok Bot 选项 | iOS 客户端版本低于 v1.16，或更新后尚未冷启动注册系统 Shortcuts | 在 iPhone 15 Pro 及后续机型上将 Grok Bot App 升级至 **v1.16+**，并在更新后**至少打开一次 App** 以向 iOS 注册 `Start Voice Chat` 快捷指令（[https://cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)、[https://cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)） |
| **Vault 绑卡无单独弹窗** | 存入 `Settings → Vault` 的银行卡在结账时自动填入，未弹出单独的 Vault 确认框 | 官方设计机制：已存 Vault 的卡通过 `BrowserSecureFill` 注入时不触发单独的逐笔 Vault 弹窗 | 若希望每笔消费都手动把关输入卡号，**切勿将主力信用卡常驻保存在 Vault 中**，应从 Vault 移除并改用每次结账在聊天 Secure Form 中单次输入（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)、`@kial` [https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)、`@JianWeiSignal` [https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)） |
| **客户端交互与外设痛点** | iPad 外接物理键盘按回车键（Enter）偶发无法发送或换行异常、Vault 条目重复冗余 | `@leerob` 反馈悬赏帖中收录的移动端外接键盘事件绑定问题与多次导入留存冗余 | 临时使用屏幕发送按钮或快捷键组合并更新最新移动端版本；针对 Vault 冗余条目可使用 `@LisaMAUSA` 分享的 **Vault Tidy** 模板扫描去重（[https://x.com/leerob/status/2113792409448714468](https://x.com/leerob/status/2113792409448714468)、[https://x.com/LisaMAUSA/status/2114208018388643852](https://x.com/LisaMAUSA/status/2114208018388643852)） |

如果按照阶梯排查依然无法解决，联系官方技术支持（[https://cursor.com/help/grok-bot/get-help](https://cursor.com/help/grok-bot/get-help)、[https://cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）前，提前收集完整信息：Grok Bot 版本号、操作系统与版本、精确报错文本、涉及的 Bot 或 Routine 名称、故障发生的具体时间与时区、界面显示的完整 Request ID 或会话 ID，以及重启或更新后的对比结果；工单中绝不能附带明文密码、一次性验证码或私钥信息（[https://cursor.com/help/grok-bot/troubleshooting](https://cursor.com/help/grok-bot/troubleshooting)）。


# §23 别这么用 · Anti-Patterns

> **适合谁**：已经跑通第一个任务、准备设 Routine 或多 Bot 的读者。**前提**：读过 §07 Skill 与 Routine、§08 审批与安全。

用 Grok Bot 最容易犯的毛病，就是把聊天框里的爽快感直接搬到自动化系统里。平时对话模型漏个字段，顺手回一句就能纠正。但在自动化工作流里，任何未经检验的假设都会在云电脑后台被放大，最后变成失控的账单、平台风控警告，或者数据泄露。这一章我不讲怎么把功能跑起来，专门整理我调研发现的、以及社区用户踩出来的典型反模式。

## 23.1 只在一个例子上跑通就排程 · Schedule Too Soon

很多新手刚上手时，在聊天框随手给一句提示词，看到 Bot 顺畅打开网页抓下了数据，一兴奋就随手点排程设成了定时 Routine。不少人以为只要模型跑通了一次，就能从此在云端替自己值班。这种从 Prompt 直接跨到 Routine 的冲动，是整个自动化链路里最危险的习惯。

开发者 @Michael_Fenech_ 总结过这个误区（https://x.com/Michael_Fenech_/status/2106352565528977469）。跑通一次提示词，只能证明目标网页当时的 DOM 结构刚好符合模型理解，没弹验证码，网络没丢包，也没缺字段。在单一用例上成功就匆忙排程，本质上只是把一次偶然正确的聊天记录硬存成了定时器。目标网站一旦改版，或者输入参数变为空值，Bot 在后台就没了判断基准，轻则静默退出，重则死循环乱点。

比单次崩溃更费钱的是无节制的高频轮询。社区开发者 @fleyta88 做过 Routine 成本审计（https://x.com/fleyta88/status/2109346840382415019）：一个每 5 分钟跑一次的 Routine，一个月会触发 8,640 次。作者按 API 价格估算，他的示例任务这样跑约 $397/月，改成每小时一次约 $33；如果先做廉价的变更检查、只在有变化时完整运行（例子中 180 次），约 $45。作者也说明这是 API 估算，不是 Grok Bot 订阅的实际扣费。另外官方安全文档规定，由后台 Routine、外部触发器或跨 Bot 消息触发的审批卡，无人干预大约 10 分钟就会标记为 Expired（https://cursor.com/help/grok-bot/approvals-security-and-privacy），操作直接不会执行。如果你没守在屏幕前点确认，写操作不仅白耗运行资源，关键步骤实际上全都被系统静默废弃了。

随着官方在 v0.75.2 版本（https://x.ai/changelog/bot）中大幅上调了 Routine 的小时级运行频率上限——从旧版配额提升至**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots）**，以及**单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**，定时触发的最小间隔依然保持为 5 分钟（https://cursor.com/help/grok-bot/routines）——无节制排程带来的额度吞噬风险变得更加突出。特别是在 Grok Bot 并入 **The X Subscription 三合一统一订阅**（包含 Grok、Cursor 与 X Premium，分为 Premium $30/月、Super $100/月、Ultra $200/月三档，而 Free $0 与 Plus $8/月不包含 Grok Bot 权限；详见 https://cursor.com/help/grok-bot/plans 与 https://cursor.com/help/the-x-subscription/overview）之后，Grok Bot、Grok App 与 Cursor IDE 三端共享同一个周额度池（one weekly usage pool），周额度耗尽后会直接扣减 `grok.com/dashboard/billing` 中的 **Prepaid Credits（预付额度）**。正如社区用户 `@charlie_pmp`（https://x.com/charlie_pmp/status/2114214503416271131）所拆解的那样，很多用户升级到 The X Subscription 后感觉周额度掉电飞快，除了三端共用额度池之外，头号隐形杀手就是后台高频空转、未做精简改写的冗余 Routine 定时任务。

盲目排程还容易让人把流程运转当成价值产生。Nate B Jones 在视频《Grok Bot Is The First AI Agent You Just Install. Is It Worth $200?》里也提醒过类似问题（本书转述，未核对视频原话）（https://www.youtube.com/watch?v=LM7Ft7g8qJw）。每天推到终端的监控晨报如果从不影响你的实际决策，它就只是信息噪音。任务要是缺了终止条件，甚至会彻底失控。社区帖称有人只建了一个叫 Elon 的 Bot 且没分配明确工作，Bot 却在后台自发反复尝试生成真人图片替换头像，陷入死循环停不下来，一次性消耗了 4% 的周额度（https://linux.do/t/topic/2807876）（社区帖称此为个例）。

避免这个坑的办法，是按 @Michael_Fenech_ 的六步测试来（他把顺序概括为一句话）：**Task → Fix → Skill → Test → Routine**（https://x.com/Michael_Fenech_/status/2106352565528977469）。先人工协同带着跑一次真实任务；在交互中不断修正提示词，限制决策边界和数据来源，直到输出稳定；再把成熟步骤固化为独立 Skill；换一套全新数据盲测一轮；写清楚数据源失效、页面改版或触发审批时的降级规则；最后用 Test run 做完整校验。

![从 Prompt 到 Routine 的错误跳跃与六步防御链路对比](../images/fig-23-1.png)

*图：从 Prompt 到 Routine 的错误跳跃与六步防御链路对比*

排程前建议用这套提示词重构执行计划，强制要求 Bot 发现变化才干活：

```text
Audit my existing routines and rebuild the execution plan around actual changes.
1. List every routine, its schedule and expected output.
2. Replace polling with narrow event triggers where supported.
3. For frequent schedules, check only a hash, count or timestamp before doing full work.
4. Stop immediately when nothing changed.
5. Leave irreversible actions as drafts for human review.
6. Log every run with time, result, changed status and approval state.
7. Flag routines with over 95% no-change runs.
Show me the proposed changes and estimated savings first. Don't modify or delete anything without approval.
```

高频 Routine 在无变更状态下的资源消耗与拦截表现。

> [!NOTE]
> 📸 **截图位（待补）**：后台触发的审批卡在 10 分钟后显示为 Expired 的状态提示

除了“过早排程”之外，在日常任务派发与 Skill 沉淀环节，社区还高频踩中另外两条典型的执行反模式：

#### 反模式一：把默认聊天路由模型当成重度执行苦力裸用

不少习惯了传统网页端 ChatGPT 或 Claude 对话框的用户，在打开 Grok Bot 时，会不自觉地把默认聊天窗口直接当成干重活的问答苦力：既不挂载专职的 Skill，也不要求它把重度任务委派给云电脑里的 CLI Worker 或 Cursor Cloud Agents（`CloudAgent`），而是直接在聊天框里用零样本（zero-shot）的方式跟默认对话路由模型死磕复杂推理、长文档核查或大型工程任务。

中文社区博主数字生命卡兹克（`@Khazix0918`，285 赞 / 54 书签，https://x.com/Khazix0918/status/2111709708226797737）就曾公开吐槽过这种裸用体验下的剧烈摩擦：当把默认聊天窗口直接当苦力使唤时，会感觉它“常年不思考，张嘴就来，路由的垃圾模型查都不查直接回复……掰扯和出错浪费的时间，远超出给我节省的时间”。

针对这一痛点，开发者 `@object_nullll`（https://x.com/object_nullll/status/2111717423837778173）一针见血地指出了 Grok Bot 的底层架构正解：**Grok Bot 的外层对话层（conversational layer）在设计上是一个轻量级的“调度经理與上下文对齐器”，而不是用来直接硬扛重度推理的终端苦力**。正确的作业架构应当是：
1. 在外层对话窗口中，让 Bot 先收集业务上下文（如读取飞书、Linear、邮件或本地记忆文件）、与人类对齐交付目标与验收标准（Acceptance Criteria），并编写结构化的执行 Prompt。
2. 将真正耗时、吃算力、需要深度思考或大规模文件读写的重度执行任务，明确委派给 **Cursor Cloud Agents（`CloudAgent`）**，或者唤醒云电脑沙箱（及远程挂载的本机节点）上的 **CLI Workers**（如 `cursor-agent`、Claude Code、Codex CLI 等）去执行。
3. 结合 `@AIShovelLab`（https://x.com/AIShovelLab/status/2113123121070817421）总结的路由 Skill 范式，在主控 Bot 上配置专门的分发路由规则，严禁对话层模型在不查证、不调工具的情况下盲目直接回复或无脑重试。

你可以将以下“防裸聊调度约束”写入主控 Bot 的自定义指令或基础路由 Skill 中：

```markdown
# Dispatcher Routing Protocol (Anti-Bare-Chat Rule)
1. Never answer fact-dependent, code-heavy, or multi-step analytical requests from raw conversational memory.
2. Your role in the chat layer is strictly: Context Gathering -> Acceptance Criteria Alignment -> Structured Prompt Drafting -> Worker Delegation.
3. For repository modifications or deep codebase analysis, always delegate to `CloudAgent` or invoke the local/cloud CLI worker (`cursor-agent` / `claude` / `codex`).
4. For recurring data collection, write a deterministic Python script once and run the script instead of reading web pages repeatedly via LLM tokens.
```

#### 反模式二：让自迭代 Skill 无限追加规则而不做精简合并

为了让 Bot 越用越聪明，很多进阶玩家会配置一条“复盘自迭代”指令：每当 Bot 犯错被人类纠正后，就让它自动把这次的教训追加写进对应的 `SKILL.md` 文件里。然而，如果你只许它“往里加规则”而从不做“合并与修剪”，很快就会掉进 **Skill 膨胀与指令自相矛盾陷阱**。

一泽Eze（`@eze_is_1`，351 赞 / 62 转发 / 705 书签，https://x.com/eze_is_1/status/2109850538045264151 及系列进阶跟帖 https://x.com/eze_is_1/status/2109852993982206425、https://x.com/eze_is_1/status/2110532874000879886、https://x.com/eze_is_1/status/2110866224892850547）在总结 10 条高含金量 Grok Bot 实战心得时特别警示：当允许 Bot 在复盘中自动迭代更新自己的 Skill 文件时，如果不加约束，Skill 文件会随着时间推移像滚雪球一样越写越长，不仅每次加载都白白消耗大量上下文 Token，更致命的是第 3 周追加的特例补丁往往会与第 1 周写下的基础规则发生正面冲突，导致 Bot 在执行时左右互搏、无所适从。

正确的防臃肿自迭代法则是：每次让 Bot 更新 Skill 时，强制执行**“先去重冲突、再合并同类项、严格控制总行数上限”**的重构流程：

```text
Review our current session and update the target SKILL.md with the lessons learned, strictly following the Anti-Bloat Protocol:
1. Do NOT blindly append new bullet points to the bottom of SKILL.md.
2. Scan existing rules for semantic overlap or direct contradiction with the new rule.
3. Merge specific edge-case fixes into generalized, orthogonal principles.
4. Keep the entire SKILL.md under 150 lines; move verbose examples or historical edge cases to a separate `references/` file loaded only on demand.
5. Show me a unified diff of the proposed SKILL.md changes before saving.
```

## 23.2 把会话当权限边界 · The Shared Boundary Fallacy

很多人用多 Bot 协作时，容易有个想当然的假设：既然管理面板能建好几个 Bot，换头像、起名字、填岗位说明，那它们是不是像独立的虚拟机一样互相隔离？建一个抓公开网页的，建一个管私人邮箱的，彼此各管一摊互不相干？这个假设非常危险。

官方安全文档明确警告：**不要把不同的 Bot 当作安全边界**（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。在你个人账户底层，所有 Bot 实际上共用同一台云电脑。文件系统、持久化工作目录 `/workspace`、底层命令行凭据以及系统级浏览器，对你名下所有 Bot 完全敞开。你在 Bot A 的浏览器里登录了某个站点后台，Cookie 和登录态就会留在机器里；转头让 Bot B 打开浏览器，它照样能直接拿到登录态去操作对应数据。

忽视这个机制极易引发安全事故。社区里已有前车之鉴，有用户在拉了所有 Bot 的协作群里误发了敏感密码，群里所有 Bot 都在上下文记忆里读到了这个凭据（https://x.com/i/status/2107339523038331338）。另一个常见问题是多 Bot 并发撞风控。有用户为了提速，同时指挥多个 Bot 去同一个网站干活。因为所有 Bot 共用同一台云电脑的出口 IP 和浏览器，目标网站判定同一个账号异常并发登录，随即触发安全封锁（https://x.com/i/status/2100351900881207770）。

审批机制和分享功能同样有严格边界。官方安全文档明确规定，审批功能只能拦截模型还没执行的提议操作，根本没法撤销或回滚已经执行完毕的历史动作（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。要是为了省事配置了允许浏览器内一切操作这种宽泛规则，Bot 在不可预期的页面遭遇诱导注入，后果根本无法挽回。向社区分享 Bot 模板时，虽然官方只复制配置，不带本地数据和凭据，但要是你在提示词、系统设定或代码里写死了个人 API Key、内网地址或敏感客户信息，这些私密数据依然会跟着公开链接全漏给别人（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。

基础安全底线是把这台共享云电脑当成没隔断的开放工位。千万别在云电脑上直接登录网银、核心财务系统或主力私人邮箱（https://ytget.cc/，该站称引自官方文档，官方原文未见此条）。遇到密码、双重验证码、短信验证码或支付确认，绝对不能在聊天框发明文，必须按官方规范交接控制权：在 Agent Computer 界面点 Take control 按钮，人在屏幕上输完，再交还控制权让 Bot 继续跑（https://cursor.com/help/grok-bot/approvals-security-and-privacy）。特定项目结束后，主动退出相关站点，及时清理云电脑工作目录下的敏感临时文件。

![共享云电脑架构下多 Bot 共享文件、会话与出口 IP 的真实范围](../images/fig-23-2.png)

*图：共享云电脑架构下多 Bot 共享文件、会话与出口 IP 的真实范围*

> [!NOTE]
> 📸 **截图位（待补）**：通过 Agent Computer 界面接管控制权进行敏感信息输入的步骤

在官方相继上线 **1Password Brokered Sign-in（代理逐次授权登录，v0.75.2）** 与 **Grok Bot Vault（内置加密保险箱，v0.75.5）**（详见官方更新日志 https://x.ai/changelog/bot 与官方安全说明 https://cursor.com/help/grok-bot/secrets）之后，围绕“密码与银行卡怎么存、怎么批”又衍生出了两个极易踩坑的新型权限反模式：

#### 反模式一：误以为把银行卡存入 Vault 后每次结账都会弹出单独的 Vault 确认框

2026 年 10 月 23 日，官方正式推出内置加密保险箱 `Settings → Vault`（`@bot` 官宣帖获 9,398 赞 / 2,756 书签，https://x.com/bot/status/2113754107861532677），支持将网站登录凭据（Logins）、银行卡（Cards）与联系人地址（Contact info）以只写（write-only）加密方式保存，并由底层 `BrowserSecureFill` 工具自动填入表单，从而让 Bot 永远看不到明文卡号、CVV 或密码；加上此前 Elon Musk（`@elonmusk`，17,221 赞，https://x.com/elonmusk/status/2110610960474079445）公开承诺“如果 Grok Bot 在代购时出错或泄露了你的银行卡，SpaceX 将全额赔付”，很多用户便放心地把自己的主力大额信用卡直接存进了 Vault，并想当然地以为：“哪怕卡存在 Vault 里，每次 Bot 要往网页里填卡号结账时，系统肯定还会再弹出一个专门的 Vault 卡片填充确认框让我点同意。”

**这是一个极其危险的误解！** 英文社区开发者 `@kial`（https://x.com/kial/status/2114201768414646280）与中文社区博主见微｜Signal（`@JianWeiSignal`，https://x.com/JianWeiSignal/status/2114195530611855488 及跟帖 https://x.com/JianWeiSignal/status/2114195638988501103）第一时间援引官方 [Secrets & Vault 帮助文档](https://cursor.com/help/grok-bot/secrets) 向社区发出了安全预警：
- 根据官方文档明确记载：**保存在 Vault 中的银行卡在结账填充时，不会触发单独的逐笔 Vault 弹窗确认（a card saved in Vault is filled at checkout WITHOUT a separate per-charge Vault prompt）**，它仅受通用的购买审批规则（general purchase approval rules）约束。
- 结合官方 [Work 技术文档](https://cursor.com/docs/grok-bot/work) 规定的结账支付调用优先级顺序——**`Vault` → 聊天内 `Secure Form` → `Link / X Money` → `Take over screen（人工接管屏幕）`**——只要你的 Vault 里存有银行卡，Bot 在结账环节就会排在第一顺位直接调用 `BrowserSecureFill` 把卡号填进收银台。而且在 v0.75.2 精简了当前对话轮次内已明确授权指令的冗余 Auto-review 审批卡之后，如果你在对话中下达了含糊的“帮我把这几样东西买下来”的指令，已存卡就可能在没有单独 Vault 弹窗阻拦的情况下直接完成填充。

**防御铁律**：
1. 如果你希望**每一笔消费都必须亲手输入并逐单确认银行卡**，**切勿将银行卡常驻保存在 Vault 中**（也不要在聊天内弹出掩码 Secure Form 输入卡号时顺手勾选 `Securely save to Grok Bot's vault`）。当你不把卡存入 Vault 时，Bot 会按优先级退回至聊天内 **Secure Form** 或要求你 **Take over screen**，从而强制实现逐笔手动把关。
2. 若确实需要在 Vault 中存放卡片以供高频日常代购（如点咖啡、订工作餐），请务必使用**设有严格单日/单笔消费限额的虚拟卡或专用副卡**，并在 Vault 条目的明文 **Hint** 字段中写清用途边界（例如 `"Use ONLY for weekday lunch orders under $25"`），绝不要把无限额的主力信用卡塞进常驻 Vault。

#### 反模式二：把同一个机密同时塞进 Vault 和 1Password 导致真源混乱

随着 Grok Bot 同时支持内置 **Vault**（支持 5 MB CSV 批量导入与摄像头扫卡）以及 **1Password Brokered Sign-in**（需本地安装 1Password 8.12.42+，通过 `Settings → Connect apps → 1Password` 绑定，在 1Password App 内逐次生物识别审批个人 Personal/Private 密码库，详见 https://cursor.com/help/grok-bot/connect-apps 与 `@bot` 公告 https://x.com/bot/status/2113301060811161874、`@1Password` 公告 https://x.com/1Password/status/2113276767582498943），不少用户为了“双保险”，直接从 1Password 导出一份全量 CSV 塞进 Grok Bot Vault，同时又挂着 1Password 连接器。

这种“一密多存”的做法很快就会引发严重的凭据真源混乱（Split-Brain Secrets）：
- 根据官方 [Work 技术文档](https://cursor.com/docs/grok-bot/work)，Grok Bot 在登录网站时的调用优先级顺序严格固定为：**云电脑上已保存的浏览器会话（Saved browser session） → `Vault` → `1Password` → 聊天内 `Secure Form` → `Take over screen（人工接管屏幕）`**。
- 当你把同一个网站的账号同时存在 Vault 和 1Password 时，由于 `Vault` 的优先级高于 `1Password`，Bot 会直接静默使用 Vault 里的凭据去填表，完全绕过你原本期望的“每次在 1Password App 里按指纹逐次审批（Brokered approval）”的安全防线！更糟糕的是，日后你在 1Password 里修改了该网站密码或更新了 2FA/TOTP 动态码，Grok Bot 却依然优先拿 Vault 里的旧密码去撞库，直接导致账号被目标网站锁死。

**防御铁律：遵循 `@martinpaulweiss` 的“一密一宅（One home per secret）”拆分准则**。
社区安全实践者 Martin Weiss（`@martinpaulweiss`，https://x.com/martinpaulweiss/status/2114210343467536531）给出了经过实战检验的 Vault 与 1Password 黄金分割架构，同时你也可以配合 `@LisaMAUSA`（https://x.com/LisaMAUSA/status/2114208018388643852）分享的 **Vault Tidy** 模板定期扫描去重：

| 机密类型 | 唯一存放位置（Single Source of Truth） | 触发与审批机制 | 实战理由 |
| :--- | :--- | :--- | :--- |
| **日常网站登录账号 + 2FA 动态码** | **1Password（Personal / Private 库）** | 1Password Brokered Sign-in 逐次生物识别弹窗审批 | 享受零知识注入与每次登录时的指纹/面容强管控，密码变更全局同步 |
| **专用限额支付卡 + 收货地址/联系方式** | **Grok Bot 内置 Vault** | 结账/填表时由 `BrowserSecureFill` 按 Hint 注入 | 解决收货地址与小额受控支付的高频填写摩擦 |
| **Bot 新注册的临时网站账号** | **暂存 Grok Bot Vault → 事后迁入 1Password 并从 Vault 删除** | 注册当下顺手保存，定期清理归档 | 严守“One home per secret”，杜绝 Vault 高优先级覆盖 1Password 审批 |

## 23.3 国内平台高频点击 · High-Frequency Botting

很多国内用户刚上手，就想把公众号、小红书、抖音、知乎等账号交给 Grok Bot 代管。但这些平台在 Grok Bot 官方生态里目前完全没有官方连接器或原生集成（https://xiangyugongzuoliu.com/grokbot-use-cases/）。面对这种断层，新手最常走的下策，就是让 Bot 打开云电脑浏览器登录网页后台，用模拟点击和滚动去高频刷数据、批量点赞、定时群发私信甚至自动发推文。

用无头浏览器高频模拟人工点击，在国内平台就是踩雷。象鱼工作流在复盘实战用例时强调，国内主流内容平台风控极度敏感（https://xiangyugongzuoliu.com/grokbot-use-cases/）。以微信公众号为例，深度阅读转化率和完读率等核心业务数据根本不渲染在公开页面前端，盲目挂定时任务频繁刷后台，极易触发异常风控导致限流封号。鼠标移动轨迹、请求频率加上境外服务器 IP，多重审查一旦发现非人类点击，系统立刻弹出滑块拼图或短信二次验证。没人干预的 Bot 会瞬间卡死，持续重试甚至会直接招致账号永封。

海外平台的自动化同样有极高风控代价。社区有公开记录显示，有用户尝试把 Grok Bot 接入 WhatsApp 托管日常沟通，结果两个个人账号被封（帖子没有说明是否永久）（https://www.reddit.com/r/GrokBot/comments/1w11r70/；官方条款见 https://www.whatsapp.com/legal/third-party-agents-terms）。国内生态虽然有开发者基于腾讯的 ClawBot 或 iLink 接口搭建了中转程序，通过 webhook routine 把指令桥接到 Grok Bot（https://x.com/KinGao476942/status/2108171436213104836；https://ele.ac.cn/2171/），但这套民间方案落地硬伤不少。除了微信客户端必须满足特定版本（iOS ≥8.0.70、Android ≥8.0.69），登录二维码有效时间只有 5 分钟左右，错误码 -14 会反复提示登录凭据失效，云电脑一重启就得重新扫码重启中继。虽然教程分享者声称走对应接口不封号，但这并未获得微信官方承诺，把个人社交号交给非官方自动化始终存在被风控识别的高额风险。

针对缺少原生插件的国内主流平台，行之有效的操作标准是建立**半自动化流水线模式**。取数据阶段，别让 Bot 挂着账号在后台实时抓，由人把后台报表导出为表格文件或截取数据大屏，把离线文件给 Bot 拆解分析；做内容阶段，把 Bot 的职能严格限定在选题策划、素材聚合与文案撰写，产出作为草稿归档到文档；最后分发阶段，文章发布、评论回复、私信发送以及资金往来等高风险动作，牢牢留在自己的客户端由人手动完成，严禁让 Bot 在未经授权的网页后台自主点击发送。

![国内无插件平台下离线数据导入与人工闭环发布的半自动化协作流](../images/fig-23-3.png)

*图：国内无插件平台下离线数据导入与人工闭环发布的半自动化协作流*

> [!NOTE]
> 📸 **截图位（待补）**：尝试在无头浏览器中自动登录时触发的滑块验证阻断页面

国内平台网页端在云电脑无头浏览器下的滑块验证码触发频率。

## 23.4 跨区、代充与违规套利 · Grey Market & Terms Risks

Grok Bot 热度起来之后，中文互联网上迅速滋生出大量的灰色套利渠道、违规教程和诈骗陷阱。官方订阅有一定门槛，不少新手想找便宜捷径，结果直接掉进了灰产卖家的圈套。

各类黑灰产里危害最深的是要会话凭据的代充。有第三方渠道卖 SuperGrok 代充（标价 ¥299/月，该店页面同时列出官方价 $30/月），操作指南里明确要求买家交出浏览器中的 Session JSON 凭据（https://claudemax.shop/blog/grok-bot-guide-supergrok）。很多新手完全不理解这有多严重。该店自称 Session JSON 只做格式检查、不含登录令牌，但把账号信息交给第三方本身就有被滥用和违反服务条款的风险。市面上还有打着「国内体验版」旗号的第三方产品，它们不是官方（https://claudemax.shop/blog/grok-bot-guide-supergrok）。

第二类常见违规是低价区跨区订阅和用云电脑套利。LINUX DO 社区里常有人讨论通过印度等低价区以每月约 50 元人民币开通 SuperGrok 会员（https://linux.do/t/topic/2848179）（社区帖称此为个例）。伪造账单地址和网络归属地跨区套利公然违背了用户协议，官方随时可能批量清退，一旦被判定为作弊，账号会被即刻封停，里面的数据也会彻底丢失。类似的高危操作还包括把海外云电脑当成跳板网络，有自媒体发教程引导用户借用 Grok Bot 的美国云电脑去注册或订阅 Claude Code（KinGao 公众号 10/5《如何用 Grok Bot 进行 Claude Code 注册及订阅》；https://x.com/KinGao476942；同类帖 https://x.com/Mileson07/status/2102404899158020312）。这种绕过区域准入限制的行为严重触碰了 Anthropic 的合规政策，极易引发大面积关联封号。

云电脑使用方式也存在被滥用的违规现象。社区帖称有人在云电脑中部署开源工具 sub2api，把个人 Grok 账号的授权凭据直接包装成标准 API 接口对外提供服务，甚至号称单日消耗了 3000 万 token（https://x.com/onlyforapp/status/2105878555015950421）（社区帖称此为个例）。这种用法很可能违反服务条款，有封号风险。金融领域借 Grok Bot 概念的虚假宣传也屡见不鲜，比如链上凭空发行的同名虚假代币 $GROKBOT，以及网上广泛传播的宣称 Bot 自主量化几天翻几十倍的暴富截图（https://x.com/i/status/2102291280965640690），全都是虚假营销和杀猪盘。

面对这些信息，底线其实就几条：走官方公布的正规渠道开通服务；死守密码和 Session JSON 会话凭证，绝不透露给第三方；不把云电脑当成绕过其他平台风控的代理跳板；对任何吹嘘 Bot 全自动投机暴富的营销话术保持警惕。

![把 Session JSON 等账号信息交给第三方代充的风险路径（该店称其不含登录令牌，但账号信息外泄仍有滥用与违反条款的风险）](../images/fig-23-4.png)

*图：把 Session JSON 等账号信息交给第三方代充的风险路径（该店称其不含登录令牌，但账号信息外泄仍有滥用与违反条款的风险）*

> [!NOTE]
> 📸 **截图位（待补）**：社区中典型的交出会话凭证代充教程与诈骗信息示例

#### 账单反模式：在 `cursor.com/unify` 合并升级 The X Subscription 时，忘记手动取消移动端订阅导致被双份扣款

除了灰产代充与违规跨区之外，即便完全走正规官方渠道，在 2026 年 10 月 **The X Subscription 三合一统一订阅**（`@bot` 官宣帖 https://x.com/bot/status/2110063783796572496，将 Grok、Cursor 与 X Premium 整合为 Premium $30/月、Super $100/月、Ultra $200/月三档，详见 https://cursor.com/help/grok-bot/plans、中文版 https://cursor.com/cn/help/grok-bot/plans 及总览 https://cursor.com/help/the-x-subscription/overview）上线后，许多老订户在合并升级账单时也踩中了两个代价不菲的“账单反模式”：

1. **误以为移动端 App Store / Google Play 订阅会自动退订，导致每月被双份扣款（Double-Billing Trap）**：
   - 根据官方 [The X Subscription 总览文档](https://cursor.com/help/the-x-subscription/overview) 与 [Grok Bot FAQs](https://cursor.com/help/grok-bot/faqs) 规定，当你通过 `https://cursor.com/unify`（或 `accounts.x.ai/unify`）将原有的 X Premium、SuperGrok 与独立 Cursor 订阅合并升级为统一的 The X Subscription 时，**只有此前在网页端（Web）直接绑卡扣款的旧订阅会被系统自动取消，并按剩余未使用天数自动退还按比例折算的费用（prorated refunds）**。
   - **关键红线**：如果你此前的 X Premium 或 SuperGrok 是通过手机上的 **Apple App Store（iOS 内购）** 或 **Google Play** 订阅开通的，受限于苹果与谷歌的应用商店账单隔离权限，Cursor 和 xAI 后台**根本无法代你自动取消或退还移动端渠道的订阅**！不少用户在网页端 `cursor.com/unify` 一键点完合并升级后就以为万事大吉，结果月底既被扣了一笔全新的 The X Subscription 网页账单，又被 Apple ID / Google Play 照常续费扣了一笔旧订阅。
   - **正确操作**：在完成 `cursor.com/unify` 统一订阅升级的当天，必须立即打开 iPhone 的 `设置 → [你的名字] → 订阅（Subscriptions）` 或 Google Play 的 `付款和订阅 → 订阅`，亲手将旧的 X / SuperGrok 移动端内购订阅点击“取消订阅”。
2. **未评估清楚三端共用额度需求，就盲目点击单向不可逆的 `cursor.com/unify` 升级**：
   - 官方计费规则（https://cursor.com/help/grok-bot/plans）明确指出：既有的旧版独立订阅计划——包括 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）以及自助式 Teams（$40/人/月）——只要订户不主动迁移，依然可以保留原有独立档位与价格，并继续通过 `Settings > Usage & Billing > Manage Plan > Get Access with Grok` 关联个人 SuperGrok 或 X Premium+ 账号（多账号额度不叠加，取上限更高者生效）。
   - 但**一旦你在 `cursor.com/unify` 确认切换至 The X Subscription，该操作是单向不可逆的，你将永远无法退回旧版 $20/月的独立 Cursor Pro 计划**。同时，切换后超额消费不再走旧版的后付费按需账单（Post-paid on-demand billing），而是统一改为从 `grok.com/dashboard/billing` 的 **Prepaid Credits（预付额度）** 中扣除（且在 Cursor 中调用非 Grok 系列的第三方模型会直接扣减 Prepaid Credits，不消耗套餐内的 Grok 周额度池）。因此在点击合并前，务必先核对自己的主力模型结构与移动端退订状态，切勿盲目一键冲动切换。


# §24 从 "聊天" 到 "管理" · Managing, Not Chatting

> **适合谁**：已经用过几次 Bot、想让它长期稳定干活的读者。本章讲心态和方法，不涉及具体操作；24.5 是作者个人判断，以为主。

![心智模型一图流。从聊天到管理的认知跃迁：Grok 负责思考与推演，Bot 负责驻留云电脑并操作工具，Routine 将验证过的步骤固化为资产，人在关键节点把关审批。](../images/fig-24-1.png)

*图：心智模型一图流。从聊天到管理的认知跃迁：Grok 负责思考与推演，Bot 负责驻留云电脑并操作工具，Routine 将验证过的步骤固化为资产，人在关键节点把关审批。*

我翻看社区讨论时发现，新手最容易犯的一个错，是把 Grok Bot 当成另一个更聪明的聊天框。跑去敲一段长篇大论问行业趋势，等它吐出一篇分析。这完全用错了地方。如果你只要一段文字、一个点子或一份方案，普通 Grok 几秒钟就能搞定，根本不用占着一台全天候开机的云电脑。Grok Bot 的底层逻辑不是陪你聊，而是接手具体工序的虚拟员工。从向模型提问变成给团队派活，核心就不是提示词工程，而是组织与流程管理了。

## 24.1 Grok 想、Bot 做 · Grok Thinks, Bot Does

很多新手分不清 Grok 和 Grok Bot 的边界。官方把 Grok Bot 定义为“能把事情做完的 AI 队友（AI teammates that finish the work）”，自带独立云电脑，能登录工具并在后台持续跑（来源：https://x.ai/bot 与 https://x.ai/news/introducing-grok-bot）。社区高赞帖把这两者的分工说得很透：Grok 负责调研、对比、想明白，再发明确指令；Grok Bot 负责开软件、改内容、发消息，真正把事情做完（来源：https://x.com/i/status/2106883332432945519）。

这直接决定了你的日常工作流。构思项目、对比方案，去 Grok 对话框里推演。有了清晰结论、需要执行具体动作了，才轮到 Grok Bot。比如让它抓取五个竞品的公开更新、整理成表、交到团队工作区并起草通知邮件。社区常说“Dots 像 AI 秘书，而 Grok Bot 像 AI 组织”（来源：https://x.com/i/status/2105404819745718679）。有韩国用户记录过在特斯拉车里用 Grok 语音理顺思路，再直接给后台的 Grok Bot 派单（来源：https://x.com/i/status/2104229085509788008）。官方在 X 上的联动也是这个逻辑：在 X 上回复特定内容并呼叫官方账号，系统会提示已将任务转给你的 Grok Bot 处理（来源：https://x.com/i/status/2108586705695449318）。记住这个核心心智：**Grok 负责想清楚，Grok Bot 负责把事做完**。别在 Bot 控制台里问开放式的哲学问题，纯属浪费云电脑资源。

关于“把对话层当苦力”的认知错位，中文社区在 2026 年 10 月中旬曾爆发过一场极具启发性的架构讨论。博主 `@Khazix0918`（数字生命卡兹克）发帖吐槽了裸用默认聊天窗的痛点：如果不配置专门的 Skill、也不做任务委派，直接把 Grok Bot 的默认聊天窗口当成问答苦力裸用，常会遇到路由模型不经深度检索就直接回复的情况，来回掰扯和纠错浪费的时间甚至超出节省的时间（来源：https://x.com/Khazix0918/status/2111709708226797737）。对此，开发者 `@object_nullll` 一针见血地拆解了背后的正确架构逻辑：Grok Bot 对话层（conversational layer）的设计初衷是收集上下文、对齐验收标准、编写结构化 Prompt，并将重度执行任务委派给 Cursor Cloud Agents（`CloudAgent`）或云电脑上的 CLI Workers，绝不能依赖裸聊天的 zero-shot 直接回复来干重活（来源：https://x.com/object_nullll/status/2111717423837778173）。

这一“对话层负责对齐意图与编排，执行层交给云电脑脚本、Cloud Agent 与专职 Bot”的架构哲学，也在跨端协同与确定性脚本实践中得到了完整印证：

- **BDK（`cursor-grokbot-agents`）本地与云端双向编排**：通过 BDK（Bot Developer Kit）与 `cursor-grokbot-agents` 技能桥接，你可以让运行在本地终端里的 Claude Code 或 Codex 与云端 Grok Bot 各司其职。例如 `@StarkLJM`（Mr.鼓先生）在实测中由本地 Claude Code 负责拆解任务并向云端 Grok Bot 派单，要求制作一段 20 秒《上下五千年》中国历史线条画动画短片；云端 Grok Bot 随即在独立沙箱中完成分镜绘制与视频合成，直接向本地返回渲染好的 `0:20` MP4 视频卡片与 `2.7 MB` 的完整源码压缩包（来源：https://x.com/starkljm/status/2109544938644107411）。同样，`@kangxiaile`（康熙AI了）将本地 Claude Code 写代码时遇到的新库与实时舆情检索外包给云端 Grok Bot，利用其免费的原生 X 检索能力汇总成结构化 Markdown 传回本地（来源：https://x.com/kangxiaile/status/2109752183889744216）；`@z_lumia`（x白）与 `@AIShovelLab` 也总结了本地 CLI 与云端 Grok Bot 双向互调的六大核心范式（来源：https://x.com/z_lumia/status/2113800469571313974 与 https://x.com/AIShovelLab/status/2113123121070817421）。
- **AI 写确定性脚本，脚本跑日常轮询**：在日常高频数据采集场景中，优秀的管理者不会让大模型每天开浏览器消耗额度去读网页。`@StarkLJM` 展示了标准做法：先用 Cursor CLI 耗时 28.6 秒生成一套带严格校验规则（字段缺失立即告警、无评分严格写入 `null` 而非用 `0` 污染均值）的确定性 Python 爬虫脚本，再部署到云电脑上每日定时执行，每天仅需 1.99 秒即可抓完 30 条榜单记录，日常运行消耗 0 模型额度（来源：https://x.com/starkljm/status/2111803996734419377 与 https://x.com/starkljm/status/2112818533797343312）。正如 `@eze_is_1`（一泽Eze）在万字实战心得中所总结的，只有厘清云端 7×24 小时编排中枢与底层执行工具的边界，才能真正发挥 AI 团队的威力（来源：https://x.com/eze_is_1/status/2109850538045264151）。

## 24.2 "Routine 才是产品" · Routines Are the Product

社区里有句话直戳本质：“这里的 Routine 才是真正的产品，Bot 本身并不是（The routines are the product here, not the bot）”（来源：https://x.com/i/status/2109516426767654962）。如果你建了个 Bot，每天全凭心血来潮去打字派活，它就是一台昂贵的手动打字机。Bot 只是个承载环境和凭据的工位，真正为你持续产出价值的资产，是你配置并排期的 Routine。

新手最容易踩的坑，是直接从提示词跳到定时任务。输入框里敲一句话，Bot 侥幸跑通一次，就随手点保存为 Routine，后面肯定崩溃。社区实践者 Michael Fenech 提出过一套严密的演化法则：Task → Fix → Skill → Test → Routine（来源：https://x.com/Michael_Fenech_/status/2106352565528977469）。这套流程分几步走：先手动跑一次真实任务，确认能做完；接着修正步骤、决策逻辑和输出格式，调到流程稳定；第三步把跑通的流程沉淀为 Skill，省得模型每次从头摸索；第四步换一份新输入做二次测试，只在一个样例上跑通不叫能力，那叫存了条聊天记录；第五步明确定义各类失败情形，包括数据源失效、信息过期、遇到审批或突发意外时的退避策略；最后用系统的 Test run 跑通输入、输出和审批断点，确认无误再正式上线。社区成员 kocer_eth 也提出过类似的晋升流程：先验任务，再抓取方法固化为带明确权限的 Skill，做二次输入测试，最后排期为 Routine（来源：https://x.com/kocer_eth/status/2105008655770788250）。

这跟官方团队的方法论一致。官方指南明确强调“做一次任务，固化为技能，排期为例程”，每个 Bot 最多 50 个 Routine，应用保留最近 20 次运行记录（来源：https://cursor.com/help/grok-bot/routines；转述见 https://x.com/cyrilXBT/status/2100094833671254070）。随着官方在 v0.75.2 版本中大幅上调并发配额，目前 Routine 的运行频率上限已升级为**全账号所有 Bot 合计 300 次/小时，单条 Routine 最高 200 次/小时**（定时触发的最小间隔仍为 5 分钟，详见官方更新日志 https://x.ai/changelog/bot 与官方文档 https://cursor.com/help/grok-bot/routines）。官方工程师 Peng Zheng 和 Lauren Tan 在访谈中也指出，建立自动化体系的正确路径是“观察工作 → 沉淀技能 → 排期为 Routine”，核心是逐步建立人对机器的信任（来源：https://www.youtube.com/watch?v=xZ5TEaleUdg （团队成员访谈））。官方 101 直播演示里，团队用 Teach a task 录制屏幕，教名为 Maya 的助理 Bot 建 Google 表单并生成二维码，系统随即自动生成了专属技能（来源：https://www.youtube.com/watch?v=8xXhE25vJZY）。工程师在直播中直言，固化为 Skill 的核心动机是“Token 经济学（tokenomics）”，能大幅减少试错和解析页面的推理轮次，不用每次对着生疏的网页代码漫无目的地乱撞。

官方的 Teach a task 最长录制 10 分钟的电脑可见操作（来源：https://cursor.com/help/grok-bot/routines）；社区帖补充说录制不含麦克风声音（来源：https://x.com/B_doong2daddy/status/2100573792569303402）。同一作者在试"同一任务录 3 次让它取平均"，效果未验证。连续录制三次相同任务检验 Bot 生成技能脚本的稳定性。

一条能稳定上线的 Routine，提示词结构都很严谨。Rowan Cheung 归纳的 X 监控 Routine 模板是个标准参考：必须写明明确时区、数据来源、时间窗口、过滤规则、输出字段、投递渠道、禁止动作，以及查无数据或失败时的降级方案（来源：https://x.com/rowancheung/status/2108328114552000842）。

```text
Every weekday at 9:15am in my time zone, search X and the web for new AI workflows people are actually running. Keep only cases that name the old task, the tool, and the result: time saved, a step removed, or a handoff that used to need a person. Drop product announcements, "10 prompts" threads, and anything the author has not used more than once. Return at most 3. For each, give the link, the job it replaces, what I would need connected, and whether it fits my work. Send it to me on Slack. Do not post or reply anywhere else. Save this as a routine. If nothing qualifies, send one line saying so.
```

随着 v0.71.2 与 v0.75.2 版本的演进，“Routine 才是产品”这一理念已经进一步升华为 **“Routine + Pages（Canvas）才是活的产品”**。在后台引擎层，官方工程师 `@SamSokolin` 推出了 `@mail.grokbot.com` 专属邮箱的 `+alias` 加号子别名支持（来源：https://x.com/SamSokolin/status/2110496237241667621 与官方文档 https://cursor.com/help/grok-bot/agent-email），让 Routine 不仅可以按时间触发，还能仅当邮件发送到指定后缀（如 `mybot+invoices@mail.grokbot.com` 或 `mybot+newsletters@mail.grokbot.com`）时精准触发；而在前端交付层，官方在 v0.75.2 正式上线了 **Pages（内部由 `WriteCanvas` / `EditCanvas` / `ReadCanvas` / `ListCanvases` 驱动的实时交互画布）**（来源：https://x.ai/changelog/bot 与官方公告 https://x.com/bot/status/2112991843235610885）。Pages 会永久沉淀在 Bot 右侧信息栏的 `Library` 中，并支持 `Only you`（仅自己）、`Your team`（团队可见）和 `Anyone with the link`（公开链接）三级分享权限。

当你的团队扩展到五六个甚至十几个专职 Bot 时，逐个点开聊天窗看进度会陷入严重的多 Bot 界面混乱。开发者 `@melvindvivas`（Melvin Vivas）给出了“Routine + Pages”合体的教科书级范式——让 Chief of Staff（幕僚长）Bot 创建一个名为 `Activity Dashboard` 的实时看板 Page，并规定所有专职 Bot 在执行任务时都将该 Page 作为动态文档持续更新，同时配置一条定时 Routine 自动刷新面板状态（来源：https://x.com/melvindvivas/status/2113676935956160882、https://x.com/melvindvivas/status/2113676938820895045 与 https://x.com/melvindvivas/status/2113968491573514576）。这块看板将散落在各个聊天框里的碎片消息，聚合为人类一眼可控的四大实时视图：**时间线视图（Timeline view）**、**进行中任务（Tasks in progress）**、**已完成任务（Completed tasks）** 以及 **等待人工审批事项（Items waiting for human approval）**。社区实践者 `@JayKurtz90` 将其盛赞为 Pages 上线以来最惊艳的杀手级用例（来源：https://x.com/JayKurtz90/status/2113983882018119823）。你可以直接复制以下提示词让你的幕僚长 Bot 搭建同款指挥大屏：

```text
Create a live Page called "Grok Bot Activity Dashboard" and keep it updated as a living document whenever any of my bots run a task or routine. Structure the Page into four clean sections:
1. Timeline View (chronological feed of recent bot actions and routine runs)
2. Tasks in Progress (active jobs, owner bot, and current step)
3. Completed Tasks (deliverables, links, and execution timestamps)
4. Waiting for Human Approval (pending approval cards, blockers, or decisions needed from me)
Set up a routine to refresh this dashboard automatically and ensure every specialist bot logs its handoffs here.
```

**千万不要从 Prompt 直接跳到 Routine，必须走完 Task → Fix → Skill → Test → Routine 的完整链条**，再用 Pages 把后台流水线的运行态势转化为可视化指挥大屏。底座打稳了，任务才能经得起真实业务环境的长期考验。

## 24.3 流程不等于价值 · Process Is Not Value

很多人刚接触自动化，很容易沉迷“忙碌感”。给 Bot 排满定时任务：早八点推行业资讯，中午抓社媒讨论，下午发竞品报告。后台日志刷得飞起，看着像有整支团队在拼命干活，其实多半在自我感动。

科技分析师 Nate B Jones 在视频里谈过这个误区，大意是很多人把流程运转当成了价值（本书转述，英文原话未能核对字幕）（来源：https://www.youtube.com/watch?v=LM7Ft7g8qJw）。每天准时送达的早报，如果不看直接划掉，或者看了也不改变任何经营决策，那除了空耗算力毫无意义。社区帖称，fleyta88 测算过（个例，为作者基于 API 的估算，非订阅实际扣费），一个每 5 分钟轮询一次的 Routine 每月空跑 8,640 次，折合算力成本近 400 美元；改成只比对哈希值或时间戳的轻量检查、有真实数据变动才唤醒执行，作者估算约 $45/月，降低约 89%（来源：https://x.com/fleyta88/status/2109346840382415019）。另外官方文档标明，后台触发的审批卡大约 10 分钟就会显示过期，过期的操作不会执行（来源：https://cursor.com/docs/grok-bot/security）。脱离人工监管的高频定时任务不仅容易空转，还会因为审批卡超时频繁卡死。

在官方推出 The X Subscription 三合一统一订阅（Grok Bot、Grok App 与 Cursor IDE 共享同一个周额度池，详见官方文档 https://cursor.com/help/grok-bot/plans）之后，冗余流程带来的成本感知变得更加直接。社区用户 `@charlie_pmp` 拆解发现，升级到三合一订阅后感觉周额度掉电变快，除了三端共用同一个周额度池抽水之外，头号隐形杀手正是后台那些高频且未加改写精简的冗余 Routine 定时任务（来源：https://x.com/charlie_pmp/status/2114214503416271131）。相反，像 `@AbhisheKumarA7` 那样在云电脑内部安装 Codex CLI 并配置任务完成时的 Webhook 回调，让耗时任务跑完后主动唤醒 Grok Bot 验收，就能做到全程零轮询耗电（来源：https://x.com/AbhisheKumarA7/status/2110484964143976578）。

任务膨胀了就必须做审计。社区实践者 kocer_eth 分享过一套每月淘汰机制：列出所有激活的 Routine，逐项清点真正采纳的产出，标出常报错或长期忽略的，每月至少挑一条无用任务删掉（来源：https://x.com/kocer_eth/status/2101669438038634827）。官方团队成员 Lauren Tan（@poteto）在访谈中提到，她用自己做的 Dr. Eggbot（Marketplace 上一个帮你设计 Bot 的模板）配合 Routine 审计所有 Bot 与 Routine 的活跃度与开销（来源：https://www.youtube.com/watch?v=xZ5TEaleUdg （团队成员访谈））。同时，`@eze_is_1`（一泽Eze）也提醒了一个高阶治理细节：当允许 Bot 在复盘中自动迭代更新自己的 Skill 文件时，如果不加约束，Skill 文件会越写越长甚至出现前后矛盾的指令，管理者必须定期对自迭代 Skill 做精简合并与冲突清理（来源：https://x.com/eze_is_1/status/2109852993982206425）。《华尔街日报》也有一篇关于 AI 智能体在购物和聊天中"跑偏"出错的报道（付费墙，本书只依据标题，未读全文）（来源：https://www.wsj.com/tech/ai/ai-agents-assistants-shopping-chat-errors-a316d3f9）。

为了避免陷入流程虚荣，Alex Finn 给的晨间提示词很实用。睡前让项目 Bot 连夜跑构件，早晨醒来别问“总结昨晚新闻”，而是给明确行动指令：“我刚醒来，立刻列出我们现在可以做出的决策清单，以推动业务向前迈进”（来源：https://x.com/AlexFinn/status/2108319537116725426）。

```text
I just woke up. Give me a list of decisions we can make right now to push the ball forward
```

检验每一条自动化的黄金标准只有一个：**如果一条 Routine 连续运行了一周却没有改变过你的任何一项实际决策，请果断关停它**。

## 24.4 Bot 是同事，不是工具，所以要有岗位、交接、考核 · Coworkers, Not Tools

官方宣传产品理念时反复强调：“像对待队友一样向 Bot 派活（Message Bots like teammates）”（来源：https://x.ai/bot）。从工具思维转到团队思维，你就得按管理真人的方式来：界定清晰岗位职责、划好权限红线、规范交接协议，并建立定期纠错复盘机制。

搭团队第一步，官方团队成员 poteto 建议：新手一开始只建一个 Bot，等管理复杂度真正上去了再拆，别一上来建一堆专职空壳（来源：https://x.com/poteto/status/2108097362283597916 （团队成员个人帖））。poteto 还建议上手先接常用日常工具，包括日历、Slack、工单系统、CRM 和网盘，让 Bot 拿到上下文和操作钥匙（来源：https://x.com/poteto/status/2107830403549831186 （团队成员个人帖））。社区认可的开箱指令也是这套：先接邮箱、日历和文档，让 Bot 挑出三件今天就能交接的事（来源：https://x.com/sidejob_AJ/status/2108592848300056956；Grok Bot 团队的 Roman Ugarte 在 Lenny's Podcast 访谈中同样建议直接问 Bot 能从你的盘子里拿走什么任务，来源：https://www.youtube.com/watch?v=maSdsTLaMuU）。

划权限红线是管理中最关键的一环。官方采购助理 Haggle Bot 的系统提示词展示了标准分级：动作清晰划分为“始终允许（Always allowed）”、“必须显式批准（Needs explicit go）”以及“绝对禁止（Never）”三档（来源：https://x.ai/news/grok-bot-procurement）。Michael Fenech 也强调，发外部邮件、付款下单、删数据或合并分支等高危动作，必须默认以草稿形式提交人审，绝不能全自主跑（来源：https://x.com/Michael_Fenech_/status/2105697750645977298）。

建了多个 Bot 后，协作模式需要严谨设计。Grok Bot 团队的 Roman Ugarte（具体职务未核实）在访谈中说，内测第二周用户群就自发形成了 Chief of Staff（幕僚长/总助）模式（来源：https://www.youtube.com/watch?v=maSdsTLaMuU （团队成员访谈））。人只跟一个核心总助对话，由总助去调度垂直领域的子 Bot。例如 `@milesdeutscher` 搭建了 1 个总控 Orchestrator 统领 10 个以上细分专职 Bot 的“Grok Swarms”蜂群架构（来源：https://x.com/milesdeutscher/status/2113653818651189419）；中文社区的 `@CyberAlice3269`（夏哥研究室）也落地了“1 个 CEO Bot + 5 个专职 Bot（情报搜集、选题策划、初稿撰写、审校润色、配图制作）”的自媒体内容工作室（来源：https://x.com/CyberAlice3269/status/2112098767151468645）。一个群聊可以放 2 到 6 个 Bot（来源：https://cursor.com/help/grok-bot/group-chats）；早期每个账号最多 50 个 Bot，后来官方更新日志写明已可创建超过 50 个（来源：https://x.ai/changelog/bot）。如果不加限制，几个 Bot 在群里互相客套确认，几下就把上下文烧光了。社区实践者 Michael Fenech 建议在设定里加入“安静交接”规则（来源：https://x.com/Michael_Fenech_/status/2105697750645977298）：

```text
Only message another bot when it needs to act. No acknowledgments, thanks, or progress pings. Send one summary when the work is done.
```

几个管理细节：Peter Yang 建议给总助 Bot 取独立名字，别用自己的名字注册它的工作邮箱，免得邮件抄送时一片混乱（来源：https://x.com/petergyang/status/2108624122339287335）。汇报方面，社区流行让协同 Bot 每晚发语音备忘录，总结当天推进的事项（来源：https://x.com/i/status/2101851806330712339）。而在随身派单与考核机制上，社区在 2026 年 10 月下旬又进化出了两项极具代表性的管理实践：

- **穿戴式免提随身派单（Action Button + 骨传导耳机）**：官方在 iOS v1.16 版本中正式上线了 iPhone Action Button（侧边操作按钮）一键实时语音通话支持，并允许在 iOS 快捷指令中通过 `Start Voice Chat with Bot` 指定呼叫某一位专职 Bot，挂断后自动在聊天流生成含完整逐字稿的 Voice chat card 并立即跟进执行（来源：https://cursor.com/help/grok-bot/voice-chat 与官方公告 https://x.com/bot/status/2112246033178968161）。博主 `@D__cup`（大艺术家二福）将这一能力与韶音（Shokz）不入耳骨传导耳机结合：全天佩戴骨传导耳机，在走路、通勤或做家务时完全解放双手双目，盲按一下手机侧边的 Action Button 就像给真人秘书打电话一样向云端 AI 团队口述派活（来源：https://x.com/D__cup/status/2114211130365358350）。同样，`@TyeInBloom` 还将 v0.75.2 新增的 iOS 原生日历、提醒事项与通讯录直读权限与 Action Button 语音融会贯通，实现了真正的随身幕僚体验（来源：https://x.com/TyeInBloom/status/2113767679588770271）。
- **设立“HR 绩效考核官”——模型评测元 Bot（Meta-Evaluator Bot）**：既然把 Bot 当员工管理，就不仅要考核流程产出，还要对底层算力做定期优胜劣汰。开发者 `@kaelanyiu`（Kaelan Yiu）专门在团队里设立了一个定时运行的“评测官 Bot（Meta-Evaluator Bot）”：每隔几天自动对当前各大前沿大模型跑一轮真实业务基准测试，并根据实测得分动态修改其他干活 Worker Bots 在未来几天内通过 CLI 调用的底层模型配置（来源：https://x.com/kaelanyiu/status/2114213605566742884）。这种让元 Bot 自动考核并换血底层模型的机制，把 AI 团队的技术管理推向了全自动闭环。

还有真实事故踩出的坑。官方明确说明，账号下的所有 Bot 共享同一台常驻云电脑、浏览器和登录态，隔离级别是用户而不是 Bot（来源：https://cursor.com/docs/grok-bot/security，"Do not use separate Bots as a security boundary"）。社区发生过用户在群聊输密码导致所有 Bot 全盘知晓的事故（来源：https://x.com/i/status/2107339523038331338）；还有多个 Bot 在同一台机器并发访问同一网站被封禁的情况（来源：https://x.com/i/status/2100351900881207770）。针对凭据与支付管理痛点，官方在 v0.75.2 与 v0.75.5 中相继推出了 **1Password Brokered Sign-in（免共享库的逐次生物识别授权登录）** 与 **Grok Bot Vault（`Settings → Vault` 内置加密只写保险箱）**，确保 Bot 在整个任务周期中绝不在聊天记录或上下文中看到明文密码、完整卡号或 CVV（来源：https://cursor.com/help/grok-bot/connect-apps 与 https://cursor.com/help/grok-bot/secrets）。但在给 AI 员工授权经费时，管理者必须牢记官方文档（https://cursor.com/help/grok-bot/secrets）与社区安全研究者 `@kial`、`@JianWeiSignal` 反复强调的一条红线：**保存在 Vault 中的银行卡在结账自动填充时，不会触发单独的逐笔 Vault 弹窗确认**（来源：https://x.com/kial/status/2114201768414646280 与 https://x.com/JianWeiSignal/status/2114195530611855488）。因此，像 `@martinpaulweiss` 推荐的“一密一宅（One home per secret）”分家治理——日常登录放 1Password 逐次审批，需要逐笔把关的主力信用卡绝不常驻保存在 Vault 中，而是改用结账时弹出的聊天内掩码安全表单（Secure Form）单次输入——才是管理 AI 团队财务权限的稳健之道（来源：https://x.com/martinpaulweiss/status/2114210343467536531）。

Bot 出现事实错误时，别逼它重猜，要强制执行“纠错 → 回查来源 → 输出答案”，让它重新读取日历、收件箱或后台记录再答（来源：https://x.com/Michael_Fenech_/status/2106729045878514147）。管理 AI 团队的心态要平实：**把 Bot 当作领薪水的初级员工，给出明确的岗位说明书、权限红线与安静交接规范**。

## 24.5 我对 Grok Bot 的判断 · My Take

从 2026 年 8 月官方首次推出 Grok Bot，到 8 月底扩大资格覆盖 Cursor Pro 与 Teams，再到 9 月底发布 Team Bots 支持多人团队协同（来源：https://x.ai/news），直至 10 月中旬官方正式推出 **The X Subscription 三合一统一订阅**，将 **Grok**、**Cursor** 与 **X Premium** 三大核心产品整合进同一套账户与周额度池体系（包含 Grok Bot 的档位为 Premium $30/月、Super $100/月与 Ultra $200/月，周额度池耗尽或调用第三方模型时从 `grok.com/dashboard/billing` 的 Prepaid Credits 预付额度中扣减；既有独立 Cursor Pro $20/月、Pro+ $60/月、Ultra $200/月与自助式 Teams $40/人/月老订户可保留原计划，或通过 `cursor.com/unify` 单向不可逆升级至统一订阅，详见官方文档 https://cursor.com/help/grok-bot/plans 与 https://cursor.com/help/the-x-subscription/overview，以及官方公告 https://x.com/bot/status/2110063783796572496），短短两个月内的生态合拢速度令人惊叹。

这股爆发力已经在商业数据与企业级实战中展露无遗。据社区观察者 `@wenser2010` 梳理的数据，Grok Bot 自 8 月发布以来仅用两个月时间就突破了 **80 万周付费用户（800K weekly paid users）**；在横向对比三大智能体产品时，相较于最低门槛 $100/月（需 Pro 订阅起步）的 OpenAI Dots，以及受限于美国地区与 Meta 账号准入墙的 Meta Muse，Grok Bot 凭借 **$30/月打包 X Premium、SuperGrok 与 Cursor** 的定价策略，构建了极具统治力的性价比与生态协同护城河（来源：https://x.com/wenser2010/status/2113683422409572523 与 https://x.com/wenser2010/status/2113683427069489614）。而在企业内部实战侧，官方采购案例里，Haggle Bot 把一笔超 14,000 美元的采购单压降了 58%（来源：https://x.ai/news/grok-bot-procurement）；更震撼的是官方披露的客服自动化战报（来源：https://x.ai/news/grok-bot-customer-support）：2026 年 8 月 14 日 Cursor 并入 SpaceX SuperIntelligence（SpaceXSI）后，全球客服工单量瞬间暴增 **175%**，官方团队部署了由 **Intake Triage Bot（分诊接待）**、**Billing & Refund Bot（账单与退款）**、**Technical Repro Bot（技术复现）**、**Incident Batch Bot（事故批处理）** 与 **Product Feedback Synthesizer Bot（产品反馈聚类）** 组成的五位专职 Bot 舰队，在**零新增客服招聘（节省约 200 名新增人力）**的前提下，每天汇总超过 **20,000+** 条来自工单的产品反馈；按明确的退款说明，**99%** 的退款请求无需人工介入全自动闭环；单个工单解决成本降至 **$0.20–$0.30**（远低于行业平均的 $1.00–$4.00）；在一次突发线上故障期间，仅由一名工程师审核一张批量审批卡（batch approval card），就在 **10 分钟内清零了 204 张故障工单**。结合这些官方动作与社区反馈，我对 Grok Bot 的演化路径有几点判断：

一人公司的形态在一两年内会演变为“一人加若干专职 Bot”的工业化标准。社区里已经有 Alex Finn 用一个 Bot（他叫它 Milo）运营 AI 用例目录站的雏形案例，作者自述其全天盯回复、提 PR、自主加功能并提交搜索引擎收录（个例，来源：https://x.com/i/status/2109152147325796381）；中文社区的 `@bitman2140` 更是凭借一人一账号同时并行跑通了香港优才续签跟进、孩子插班申请、公众号与 X 双平台日更、全栈开发及每日 AI 简报等 8 条真实生活与业务流水线（来源：https://x.com/bitman2140/status/2114210291546493153）。未来的商业壁垒不在于提示词写得多花哨，而在于谁能先为业务理出稳定跑通的 Routine 流水线、用 Pages 搭建起全局态势看板并建立严格质检。

共享云电脑的单沙盒架构会走向多容器细粒度隔离与政企级合规管控。目前官方为了方便交接上下文，让所有 Bot 共用一台云电脑、同一个浏览器环境和同一套登录态（来源：https://x.ai/bot）。虽然协同方便，但多个 Bot 同时访问同一第三方业务极易触发风控封号（来源：https://x.com/i/status/2100351900881207770）。目前官方已在企业安全层引入了 ISO/IEC 27001 与 ISO/IEC 42001 认证、支持勾选 `Apply to MCP servers` 的出站域名白名单、自然语言自定义 Auto-Review 阻断规则以及推理前后审计钩子 Inference Hooks（来源：https://cursor.com/docs/grok-bot/security），同时允许桌面端开启 `Route traffic through this computer` 借用本机住宅 IP 规避机房风控（来源：https://cursor.com/docs/grok-bot/settings 与 `@XueshiQiao` 实测 https://x.com/XueshiQiao/status/2112866936229183589）。后续企业级演进中，官方大概率会在单账户下进一步引入轻量容器隔离，把高风险执行环境与总助管理环境解耦。

基于轮询的 Routine 会全面向事件驱动架构迁移。社区测算出的高频定时轮询成本居高不下（来源：https://x.com/fleyta88/status/2109346840382415019），官方设置的每个 Bot 50 个 Routine 上限（来源：https://cursor.com/help/grok-bot/routines）也限制了暴力时间驱动排期。随着 `+alias` 邮箱后缀定向触发（来源：https://cursor.com/help/grok-bot/agent-email）与外部 Webhook 的成熟，未来的工作流标准必然是“外部 Webhook / `+alias` 邮件事件监听 + 确定性脚本轻量哈希比对 + 差量唤醒”，只有数据真发生改变才激活大模型，这也是规模化普及的必然选择。

多模型分工协同与云地一体混动会彻底取代单模型全包。社区开发者已经在实践中搭建出多模型协作栈：Grok Bot 担任架构师调度日常，调 Cursor 云端 Agent 和 Opus 5.5 攻坚核心代码，用轻量快模型执行测试巡检（来源：https://x.com/i/status/2109300337203183940 与 https://x.com/i/status/2108990316644847920），甚至像 `@hppzyy` 那样在云电脑内挂载轻量级 `pi` Agent 调用廉价第三方 API 处理长文本（来源：https://x.com/hppzyy/status/2111573227881529454），或者像官方工程师 `@ericzakariasson` 演示的那样将家里常开的 Mac mini 注册为远程计算节点并运行 `cursor-agent worker`（来源：https://x.com/ericzakariasson/status/2114095056630272099 与 https://x.com/ericzakariasson/status/2114157733276525044）。在 The X Subscription 打通 Grok、Cursor 与 X 之后，未来的 Bot 不会局限在单一基础模型或单一云端沙箱上，而是作为横跨云端与本地的通用编排中枢，按需动态调度不同算力。

完全无人干预的自主智能体在严肃商业场景中无法立足。《华尔街日报》关于智能体跑偏出错的报道（未读全文）（来源：https://www.wsj.com/tech/ai/ai-agents-assistants-shopping-chat-errors-a316d3f9），以及官方审批卡约 10 分钟自动过期的设计（来源：https://cursor.com/docs/grok-bot/security），证明了安全防线必须由人工把守。哪怕 Elon Musk 公开承诺“如果 Grok Bot 在代购时出错或泄露银行卡，SpaceX 将全额赔付”（来源：https://x.com/elonmusk/status/2110610960474079445），官方在客服故障处理中依然坚持由人类工程师做最后一道批量审批把关（来源：https://x.ai/news/grok-bot-customer-support）。“草稿优先”、“1Password 逐次授权”与“权限三档”在未来数年依然是企业级部署的底层基石。**未来真正拉开差距的，不是向 AI 提问的辞藻，而是把复杂业务拆解为自动化工序的组织管理能力**。


# 附录 A–E · 速查、价格、模板、连接器、更新日志

我整理这本黑皮书时，最头疼网上的过时信息和随口编的数字。不少人把发布首周的旧规则当真理，连套餐包不包含 Grok Bot 都说错。附录不讲虚的，我把全书用到的硬性指标、价格档位、提示词、连接器目录和版本演进，都理成了可核对的清单和表格。所有内容都以 2026-10-12 的官方文档（[https://cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)）、公告（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）和公开研究为准，并已全面同步更新至 **2026-10-25（覆盖至 v0.75.5）** 的最新官方机制与实操标准。

## 附录 A 官方硬数字速查 · Official Hard Numbers

写自动化流程时，最容易踩的坑是误以为 Bot 的云电脑和 Routine 能无限制挂机。官方（[https://cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)）在系统架构和安全策略里卡了死指标。我查了官方文档（[https://cursor.com/help/grok-bot](https://cursor.com/help/grok-bot)），把关键限制理在下表，核对日期是 2026-10-12（并已增补截至 2026-10-25 v0.75.5 的最新核心指标）。

![官方核心硬限制与边界全景图](../images/fig-A1-1.png)

*图：官方核心硬限制与边界全景图*

| 维度 | 硬性限制指标 | 运行机制与边界行为 | 来源 |
|---|---|---|---|
| 账户 Bot 总量 | 已不限于 50 个 | 设计文章曾写约 50 个；9 月 1 日 v0.31.0 起可创建超过 50 个 Bot | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| 群聊协作规模 | 2 至 6 个 Bot | 新建群聊必须选择 2 到 6 个 Bot，不支持单个 Bot 自聊或超过 6 个 Bot 组群 | [cursor.com/help/grok-bot: Chat and Collaboration](https://cursor.com/help/grok-bot/chat-and-collaboration)  |
| 单 Bot Routine 上限 | 最多 50 个 | 单个 Bot 名下挂载的例行任务不可超过 50 个，删除操作即时生效且不可撤销 | [cursor.com/help/grok-bot: Skills and Routines](https://cursor.com/help/grok-bot/skills-routines-and-automations)  |
| Routine 全账号小时运行上限 | 全账号所有 Bot 合计 300 次/小时 | v0.75.2 大幅上调配额，同一账号下所有 Bot 的 Routine 触发总计最高 300 runs/hour | [cursor.com/help/grok-bot: Routines](https://cursor.com/help/grok-bot/routines) |
| 单条 Routine 小时运行上限 | 单条 Routine 最高 200 次/小时 | v0.75.2 起单条定时或事件驱动 Routine 每小时最高可运行 200 次（200 runs/hour） | [cursor.com/help/grok-bot: Routines](https://cursor.com/help/grok-bot/routines) |
| Routine 运行记录保留 | 最近 20 次 | 系统仅保留每个例行任务最近 20 条执行日志，超出的历史记录会被滚动覆盖 | [cursor.com/help/grok-bot: Skills and Routines](https://cursor.com/help/grok-bot/skills-routines-and-automations)  |
| Routine 触发时间间隔 | 不得低于 5 分钟 | 定时任务之间的时间间隔至少为 5 分钟，系统禁止秒级或极高频轮询 | [cursor.com/help/grok-bot: Skills and Routines](https://cursor.com/help/grok-bot/skills-routines-and-automations)  |
| 后台审批等待超时 | 约 10 分钟 | 由 Routine 或跨 Bot 触发的审批卡约 10 分钟未处理即标记 Expired 并终止动作 | [cursor.com/help/grok-bot: Approvals](https://cursor.com/help/grok-bot/approvals-security-and-privacy)  |
| 桌面输入框附件数量 | 最多 6 个 | 桌面端对话框一次最多拖入或选取 6 个文件附件 | [cursor.com/help/grok-bot: Files and Results](https://cursor.com/help/grok-bot/files-and-results)  |
| 文档与多媒体附件大小 | 单文件最大 25 MB | 文档（PDF/Word/Excel 等）、图片和音频文件单文件体积上限为 25 MB | [cursor.com/help/grok-bot: Files and Results](https://cursor.com/help/grok-bot/files-and-results)  |
| 视频附件大小限制 | 单文件最大 200 MB | 视频文件上传体积上限为 200 MB，超出需转码或切片提供 | [cursor.com/help/grok-bot: Files and Results](https://cursor.com/help/grok-bot/files-and-results)  |
| Vault CSV 批量导入体积上限 | 最大 5 MB | `Settings → Vault → Import` 批量导入密码 CSV 文件上限为 5 MB，支持 1Password、Chrome、Safari、Firefox、Bitwarden、LastPass | [cursor.com/help/grok-bot: Secrets & Vault](https://cursor.com/help/grok-bot/secrets) |
| iOS Action Button 最低客户端版本 | Grok Bot iOS v1.16+ | 需机型为 iPhone 15 Pro 及后续机型，更新至 v1.16+ 后至少打开一次 App 以注册 Shortcuts 动作 | [cursor.com/help/grok-bot: Voice Chat](https://cursor.com/help/grok-bot/voice-chat) |
| 1Password Brokered Sign-in 最低版本 | 1Password app 8.12.42+ | 本地电脑或手机端需安装并解锁 1Password 8.12.42 及以上版本，支持生物识别或 Passkey 逐次授权免共享库登录 | [cursor.com/help/grok-bot: Connect Apps](https://cursor.com/help/grok-bot/connect-apps) |
| X Chat 端到端加密解密 PIN 码位数 | 4 位数字（4-digit X Chat PIN） | 访问 `@chat` 加密私信与陌生人消息请求时，需配合 `xchat-grokbot-helper` 与 Juicebox 及 4 位数字 PIN 码在沙箱本地解密 | [github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper) |
| Teach a task 示范录屏 | 最长 10 分钟 | 屏幕交互演示录制上限为 10 分钟，仅录制屏幕动作，不采集麦克风音频 | [cursor.com/help/grok-bot: Skills and Routines](https://cursor.com/help/grok-bot/skills-routines-and-automations)  |
| 免费试用期限窗口 | 7 天 | 免费试用本质为固定用量额度，同时设有 7 天有效期窗口，耗尽不补发 | [cursor.com: Plans and Billing](https://cursor.com/cn/help/grok-bot/plans)  |
| 企业闲置电脑释放 | 30 天无活动自动销毁 | 企业版开启 Terminate Inactive Computers 后，成员闲置满 30 天的云电脑会被清理 | [x.ai: Changelog v0.58.0](https://x.ai/changelog/bot)  |
| 本地网络出口停用生效 | 5 分钟内切断 | 企业管理员在后台关闭 Local Egress 后，成员端活跃的本地路由在 5 分钟内终止 | [cursor.com/help/grok-bot: Settings](https://cursor.com/help/grok-bot/settings-and-notifications)  |
| 快捷键：调出命令面板 | `Cmd/Ctrl+K` | 快速搜索 Bot、对话、历史记录与插件 | [cursor.com/help/grok-bot: Chat and Collaboration](https://cursor.com/help/grok-bot/chat-and-collaboration)  |
| 快捷键：语音听写输入 | `Cmd/Ctrl+D` | 在输入框获得焦点时启动麦克风语音转写 | [cursor.com/help/grok-bot: Chat and Collaboration](https://cursor.com/help/grok-bot/chat-and-collaboration)  |
| 官方客服案例：工单激增与人力配置 | 工单暴增 175% / 新增客服 0 人 | 2026-08-14 并入 SpaceXSI 后工单暴涨 175%，靠 5-Bot 客服舰队实现 0 新增招聘（省约 200 人） | [x.ai: Grok Bot Customer Support](https://x.ai/news/grok-bot-customer-support) |
| 官方客服案例：单票成本与退款自动化率 | 单票 $0.20–$0.30 / 退款自动化率 99% | 远低于行业平均的 $1.00–$4.00 单票处理成本，且 99% 退款申请实现端到端全自动核验闭环 | [x.ai: Grok Bot Customer Support](https://x.ai/news/grok-bot-customer-support) |
| 官方客服案例：突发批处理与日均反馈提炼 | 10 分钟清 204 单 / 日提炼 20,000+ 条 | 线上突发故障期间单张批量审批卡 10 分钟清理 204 张工单；每日自动聚类 20,000+ 条产品反馈点 | [x.ai: Grok Bot Customer Support](https://x.ai/news/grok-bot-customer-support) |
| 市场规模里程碑 | 上线两个月突破 800,000（80 万）周付费用户 | 自 8 月发布后两个月即达成 80 万周活跃付费用户（800K weekly paid users） | [`@wenser2010` 市场追踪帖](https://x.com/wenser2010/status/2113683422409572523) |

关于硬限制，有两点要特别提醒。第一，别以为把 Routine 设成 5 分钟一次就能做准实时监控，这是额度雪崩的开始。按官方规则（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)），5 分钟一次等于一个月跑 8640 次。要是每次都把整个页面重读一遍，一周额度很快就见底。第二，后台任务的审批卡只有约 10 分钟寿命。半夜跑 Routine 一旦触发敏感操作审批，10 分钟没人点就会变成 Expired，任务直接停掉。想做到无人值守，得提前在 Auto-review 里配好自动放行规则，或者把敏感动作收成只写草稿。

此外，在 2026 年 10 月中下旬的 v0.75.2 与 v0.75.5 版本升级中，还有三组硬数字与运行边界值得重点关注：
- **Routine 小时级高频并发上限（300 次/小时 & 200 次/小时）**：官方（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）在 v0.75.2（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）中将全账号所有 Bot 合计的 Routine 运行频率上限提升至 **300 次/小时**，单条 Routine 的最高运行频率提升至 **200 次/小时**。这对于配合 `@mail.grokbot.com` 的 `+alias` 加号子别名（如 `@SamSokolin` 发布的 [https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)）或 Webhook 事件触发的高吞吐流水线极为关键；但正如 `@charlie_pmp`（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）与 `@StarkLJM`（[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377)）所指出的，高频周期性抓数应当优先遵循“AI 耗时 28.6 秒写确定性 Python 脚本，脚本每天耗时 1.99 秒跑日常轮询（0 模型额度消耗）”的架构范式，避免无意义的后台 Token 消耗。
- **登录与结账调用优先级顺序及 Vault 绑卡无二次弹窗红线**：根据官方工作流文档（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)），Bot 执行**网站登录（Sign-in）**时的严格优先级顺序为：`云电脑已保存浏览器会话（Saved browser session） → Vault → 1Password → 聊天内 Secure Form → Take over screen（人工接管屏幕）`；执行**结账支付（Checkout / Payment）**时的严格优先级顺序为：`Vault → 聊天内 Secure Form → Link / X Money → Take over screen`。需要特别警惕的是，官方 Vault 文档（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）明确规定：**已保存在 Vault 中的银行卡在结账自动填充时，不会弹出单独的逐笔 Vault 确认提示（without a separate per-charge Vault prompt）**。正如 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）与 `@JianWeiSignal`（[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)）提醒的那样，假设你希望每一笔消费都亲手把关输入卡号，切勿将主力信用卡常驻保存在 Vault 中。
- **官方客服自动化标杆数据与 80 万付费用户规模**：根据官方发布的客服案例报告（[https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)），部署由 Intake Triage Bot、Billing & Refund Bot、Technical Repro Bot、Incident Batch Bot 和 Product Feedback Synthesizer Bot 组成的 5-Bot 舰队后，官方在工单量暴增 **175%** 的背景下实现了 **0 新增客服招聘**（节省约 200 人）、单票解决成本降至 **$0.20–$0.30**（行业基准为 $1.00–$4.00）、退款自动化率达 **99%**、突发故障单 **10 分钟清理 204 张**、每日自动提炼 **20,000+** 条产品反馈点。与此同时，据 `@wenser2010`（[https://x.com/wenser2010/status/2113683422409572523](https://x.com/wenser2010/status/2113683422409572523)）统计，Grok Bot 上线仅两个月便突破 **800,000（80 万）周付费用户**。

## 附录 B 档位与价格表 · Plans & Pricing

早先不少网帖说 Cursor Pro 不包含 Grok Bot，那是过时的说法。官方在 8 月 25 日的 v0.27.0 更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）里对 Cursor Pro、SuperGrok 和 X Premium+ 放开了访问（8 月 26 日的公告帖没提 X Premium+）。核对日期是 2026-10-12。而在 **2026 年 10 月 18 日**（对应 `@bot` 于 10 月 13 日发布的先导公告 [https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496) 及官方计划页 [https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)），Grok Bot 迎来了订阅体系的重大演进——正式并入 **The X Subscription（三合一统一订阅）**，用一个订阅同时打包 **Grok + Cursor + X Premium + Grok Bot**，同时为老用户保留了旧版独立订阅（Legacy Plans）对照体系。

![Cursor 订阅与 Grok 关联用量判定流程图](../images/fig-A1-2.png)

*图：Cursor 订阅与 Grok 关联用量判定流程图*

### B.0 The X Subscription 三合一统一订阅主表（2026-10-18 起现行标准）

自 2026 年 10 月 18 日起，官方（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview) 与 [https://cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）推出 **The X Subscription**，将 Grok、Cursor、X Premium 与 Grok Bot 整合进统一的五档架构中。其中 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 包含 Grok Bot 完整权限，而 **Free（$0）** 与 **Plus（$8/月）** 不包含 Grok Bot：

| The X Subscription 档位 | 官方标价（美元） | 是否包含 Grok Bot | 打包权益范围（一计划三生态） | 周额度池层级与超额计费机制 | 官方来源 |
|---|---|---|---|---|---|
| **Free** | **$0 / 月** | ❌ 不包含 | 基础免费体验，无 Grok Bot 访问权限 | 不包含 Grok Bot 周额度池 | [cursor.com/help: The X Subscription](https://cursor.com/help/the-x-subscription/overview) |
| **Plus** | **$8 / 月** | ❌ 不包含 | 基础 X 权益与轻量功能，无 Grok Bot 访问权限 | 不包含 Grok Bot 周额度池 | [cursor.com/help: Grok Bot Plans](https://cursor.com/help/grok-bot/plans) |
| **Premium** | **$30 / 月** | ✅ **包含** | **Grok + Cursor + X Premium + Grok Bot** 四位一体 | **标准共享周额度池**（Grok、Cursor、Grok Bot 共用同一周额度池）；超额或调用第三方模型扣减 **Prepaid Credits** | [cursor.com/help: Grok Bot Plans](https://cursor.com/help/grok-bot/plans) / [`@bot` 公告](https://x.com/bot/status/2110063783796572496) |
| **Super** | **$100 / 月** | ✅ **包含** | **Grok + Cursor + X Premium + Grok Bot** 高阶全套权益 | **扩充共享周额度池**（适合多 Bot 协同与高频 Routine 团队）；超额或调用第三方模型扣减 **Prepaid Credits** | [cursor.com/help: Grok Bot Plans](https://cursor.com/help/grok-bot/plans) / [中文版说明](https://cursor.com/cn/help/grok-bot/plans) |
| **Ultra** | **$200 / 月** | ✅ **包含** | **Grok + Cursor + X Premium + Grok Bot** 旗舰顶配权益 | **最高共享周额度池**（适合全天候 10+ Bot 蜂群与重度研发流水线）；超额或调用第三方模型扣减 **Prepaid Credits** | [cursor.com/help: Grok Bot Plans](https://cursor.com/help/grok-bot/plans) / [中文版说明](https://cursor.com/cn/help/grok-bot/plans) |

正如 `@wenser2010`（[https://x.com/wenser2010/status/2113683427069489614](https://x.com/wenser2010/status/2113683427069489614)）、`@chuyang_ai`（[https://x.com/chuyang_ai/status/2111357749103911004](https://x.com/chuyang_ai/status/2111357749103911004)）与 `@frogchan9o1`（[https://x.com/frogchan9o1/status/2110883156891140416](https://x.com/frogchan9o1/status/2110883156891140416)）在横向对比中所指出的，相较于最低门槛 $100/月起步的 OpenAI Dots 以及受限于美国地区准入墙的 Meta Muse，**$30/月的 The X Subscription Premium 档位**一次性打通了 X Premium、SuperGrok、Cursor IDE 与 Grok Bot，是目前个人开发者与创作者最具性价比的黄金入门档位。

### B.1 访问资格与档位对应速查（Legacy 独立计划与关联对照表）

对于尚未合并迁移至 The X Subscription 的既有老用户，官方（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）允许继续保留原有的 **Legacy 独立订阅计划**（Cursor Pro $20/月、Pro+ $60/月、Ultra $200/月、自助式 Teams $40/人/月）以及原有的 SuperGrok / X Premium+ 账号关联机制。下表完整保留了 Legacy 独立计划与跨账号关联对照关系：

| 用户所持套餐/席位 | 获取访问权限途径 | 所属用量层级 | 每周包含用量说明 | 官方标价（美元） | 来源 |
|---|---|---|---|---|---|
| Cursor Pro | 登录同一 Cursor 账户 | 低档（基础层） | 基础每周用量，低于 Pro+ | $20 / 月 | [cursor.com: Pricing](https://cursor.com/pricing)  |
| Cursor Pro+ | 登录同一 Cursor 账户 | 中档（进阶层） | 充足每周用量，低于 Ultra | $60 / 月 | [cursor.com: Pricing](https://cursor.com/pricing)  |
| Cursor Ultra | 登录同一 Cursor 账户 | 高档（旗舰层） | 最高每周用量池 | $200 / 月 | [cursor.com: Pricing](https://cursor.com/pricing)  |
| Cursor Teams (Standard) | 成员账户直接登录 | 团队席位额度 | 每位成员均可访问，遵循团队额度 | $40 / 人 / 月 | [cursor.com: Pricing](https://cursor.com/pricing)  |
| Cursor Teams (Premium) | 成员账户直接登录 | 高阶团队席位 | 团队用量池更大，包含优先资源 | $120 / 人 / 月 | [penchan.co 定价归档](https://penchan.co/ai/grok/grok-bot/)  |
| 个人 SuperGrok | 方案页关联 Grok 账户 | 低档（等同 Pro） | 授权基础每周用量，低于 Plus | $30 / 月（官方帮助页不写价格，此价格来自第三方评测） | [cursor.com: Plans](https://cursor.com/cn/help/grok-bot/plans)  |
| 个人 SuperGrok Plus | 方案页关联 Grok 账户 | 中档（等同 Pro+） | 授权充足每周用量，低于 Heavy | $100 / 月 | [penchan.co 定价归档](https://penchan.co/ai/grok/grok-bot/)  |
| 个人 SuperGrok Heavy | 方案页关联 Grok 账户 | 高档（等同 Ultra） | 授权最高每周关联用量 | $300 / 月 | [penchan.co 定价归档](https://penchan.co/ai/grok/grok-bot/)  |
| X Premium+ | 方案页关联并登录 Grok | 低档（低于 Plus） | 授权基础关联用量 | 依地区而定（社区帖称香港约 311 港币，个例） | [cursor.com: Plans](https://cursor.com/cn/help/grok-bot/plans)  |
| 自助式 Grok Business | Sign in with Grok 登录 | 对应席位许可证 | 与分配席位一致（SuperGrok 或 Heavy） | 依企业席位协议 | [cursor.com: Plans](https://cursor.com/cn/help/grok-bot/plans)  |
| SuperGrok Lite | 无权访问 | 未包含 | 不包含 Grok Bot 权限，需升级后关联 | — | [cursor.com: Plans](https://cursor.com/cn/help/grok-bot/plans)  |

### B.2 计费机制与关键规则

查阅官方说明（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans) 与 [https://cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)），计费机制有三条硬规则：

第一是用量**不叠加**。如果你同时有 Cursor Pro（$20/月）又关联了 SuperGrok Plus（$100/月），系统只按较高档的 SuperGrok Plus 算用量，绝不会把两边额度加在一块。关联本身是永久授权，一旦绑定就不能解绑，也不能转给其他 Cursor 账号。

第二是官方未公布具体数字。官方（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）从没公开过每周用量到底包多少 Token 或步骤。后台是按智能体执行步数和模型开销动态扣减的，不是算你发了几句对话。

第三是按需付费不会半途掐断任务。每周用量按周重置。额度用完如果开了 On-demand（按需付费），超额部分走 Cursor 账单，受后台设的 Monthly Limit 限制。官方文档（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）明确写着，就算任务执行中途撞上线，正在跑的任务也会跑完，不会被强行掐断。

在此基础上，针对 **2026-10-18 上线的 The X Subscription 三合一订阅体系**，官方计费文档（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview) 与 [https://cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）新增了四条必须掌握的核心规则：

第四是 **`cursor.com/unify` / `accounts.x.ai/unify` 单向升级规则（不可回退）**。持有旧版独立计划（Cursor Pro $20、Pro+ $60、Ultra $200 或自助式 Teams $40/人/月）的用户，只要不主动操作，即可无限期保留原有 Legacy 计划与价格；用户也可以随时访问 `https://cursor.com/unify` 或 `https://accounts.x.ai/unify`（或客户端 `Settings > Usage & Billing > Manage Plan`）将账号合并升级至 The X Subscription。但官方（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）明确规定：**该切换为单向不可逆操作——一旦升级至 The X Subscription，将永久无法退回旧版独立 Cursor 或 SuperGrok 计划**。

第五是 **三端共享同一周额度池（One Weekly Usage Pool）**。在 The X Subscription 下，Grok Bot、Grok 与 Cursor IDE **共用同一个周额度池**（每周固定重置，未使用完的周额度不会结转至下周）。正如 `@charlie_pmp`（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）所剖析的，如果你在 Cursor IDE 中高强度写代码、同时又在 Grok Bot 中挂载了高频 Routine，两端会从同一个周额度池中抽水。若想极度节省官方周额度，可参考 `@hppzyy`（[https://x.com/hppzyy/status/2111573227881529454](https://x.com/hppzyy/status/2111573227881529454)）的做法，在云电脑内安装轻量级 Pi Agent（`pi`）并挂载 DeepSeek API Key 处理大吞吐文本任务。

第六是 **Prepaid Credits（预付额度）vs 旧版 On-demand（后付费按需账单）的计费差异与第三方模型边界**。
- **The X Subscription（预付制 Prepaid Credits）**：当每周共享额度池耗尽，或者在 Cursor 中调用**非 Grok 系列的第三方模型（third-party models）**时，系统不再走旧版后付费月结账单，而是直接从 **Prepaid Credits（预付额度）** 中实时扣减（调用第三方模型直接扣 Prepaid Credits，不消耗套餐内的 Grok 周额度池）。用户需前往 `https://grok.com/dashboard/billing` 的 `Additional usage credits` 模块充值，支持开启 **Auto Top-up（自动充值）** 并设置独立的 **Monthly additional usage limit（月度额外消费封顶上限）**。
- **Legacy 独立计划（后付费制 Post-paid On-demand）**：仅尚未迁移的旧版独立 Cursor 计划继续沿用后付费按需计费（通过 `Settings > Usage & Billing > On-demand monthly limit` 或 `https://cursor.com/dashboard` 下的 `Spending > Monthly Limit` 管控）。

第七是 **合并订阅时的按比例退费与 App Store / Google Play 手动退订防双扣红线**。根据官方统一订阅文档（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)），当你通过 `https://cursor.com/unify` 或 `https://accounts.x.ai/unify` 将原有的 X Premium、SuperGrok 与 Cursor 独立订阅合并升级为 The X Subscription 时，此前在**网页端（Web）直接扣款**的旧订阅会自动取消，并按剩余未使用天数自动退还按比例折算的费用（prorated refunds）。**但对于通过 Apple App Store 或 Google Play 应用商店内购订阅的旧计划，官方系统无法代为自动取消或退款**——你必须亲自前往 iPhone/Mac 的 Apple ID 订阅管理或 Google Play 订阅页面**手动取消旧订阅**，否则会出现新旧套餐同时扣款的“双份扣费”风险。

## 附录 C 提示词与 Routine 模板集 · Prompts & Routine Templates

这里整理了 30 条来自官方文档和社区高手的提示词与 Routine 模板，复制就能用。写法全按官方推荐结构来：定好时间与时区、卡死输入源、划清审批红线、讲清输出格式，再加上没数据或失败时的退避动作。

### C.1 监控与情报类模板（模板 1–5）

#### 模板 01：真实 AI 工作流监听 Routine

适用场景：工作日早晨定时抓取社区里验证过的高价值自动化案例，过滤营销噪音。触发方式：工作日 09:15 定时触发。出处：@rowancheung 方案 [X 引用](https://x.com/rowancheung/status/2108328114552000842)

```text
Every weekday at 9:15am in my time zone, search X and the web for new AI workflows people are actually running. Keep only cases that name the old task, the tool, and the result: time saved, a step removed, or a handoff that used to need a person. Drop product announcements, "10 prompts" threads, and anything the author has not used more than once. Return at most 3. For each, give the link, the job it replaces, what I would need connected, and whether it fits my work. Send it to me on Slack. Do not post or reply anywhere else. Save this as a routine. If nothing qualifies, send one line saying so.
```

#### 模板 02：品牌与个人声誉监测 Routine

适用场景：监控社交平台过去 24 小时内的品牌或个人提及，分类汇总并推送到协作频道。触发方式：工作日 09:00 定时触发。出处：@rowancheung 方案 [X 引用](https://x.com/rowancheung/status/2108328114552000842)

```text
Every weekday at 9:00am, search X for mentions in the last 24 hours of [your brand, @handle, or your own name]. For each hit, give the author, link, a one-line summary, and whether it is praise, complaint, question, or neutral. Do not reply to anyone. Post the digest in [your Slack channel] and tag me. Save this as a routine. If a source is unavailable, say which one.
```

#### 模板 03：品类潜在客户与竞品差评监听 Routine

适用场景：每 4 小时扫描行业痛点、竞品投诉与采购选型意向，输出高意向线索。触发方式：每 4 小时定期触发（仅在有新线索时推送）。出处：@rowancheung 方案 [X 引用](https://x.com/rowancheung/status/2108328114552000842)

```text
Every 4 hours, search X for people evaluating [your category]. Catch three things: reviews or complaints about [category]; posts asking which [category] to use; and complaints about the problem [your product] solves. Quote the post, link it, name the account, and label it review, shopping, or complaint. Skip anything older than 24 hours, and skip [category] accounts promoting themselves. Post to [your Slack channel] only if there is at least one new hit you haven't already shared. Do not reply to or interact with anyone. Save this as a routine. If the search fails, report the failure in Slack.
```

#### 模板 04：行业竞品槽点与迁移诉求定向挖掘

适用场景：反向搜索行业用户对特定产品的抱怨帖，提取功能短板与替代需求。触发方式：每周一上午 10:00 触发。出处：Rowan 讨论区延伸方案 [X 引用](https://x.com/i/status/2109290036978196689)

```text
Every Monday at 10:00am in my time zone, search X and Reddit for explicit user complaints and dissatisfaction posts about [Competitor Product] from the last 7 days. Focus specifically on pricing spikes, missing features, poor customer support, and users asking for alternatives. Filter out promotional affiliate threads. Return top 5 distinct pain points with direct URLs, user quotes, and an analysis of how our solution addresses each. Save as a routine. If no strong complaints are found, report "No significant negative sentiment detected this week."
```

#### 模板 05：官方更新日志监控与自身配置影响审计

适用场景：每天两次监测官方产品更新日志，自动评估改动对已有配置与 Routine 的影响。触发方式：每天 08:30 与 18:30 触发。出处：社区用户惯用法 [X 引用](https://x.com/i/status/2107629480374308893)

```text
Twice every day at 8:30am and 6:30pm in my time zone, fetch the latest changelog from https://x.ai/changelog/bot. Check whether any new release notes have been published since the last check. If new items exist, summarize the key changes, list any new features or deprecations, and explicitly explain how these updates affect my current bots, plugins, and routines. If nothing changed, exit quietly without sending any message.
```

### C.2 个人效能与早晚助理类模板（模板 6–10）

#### 模板 06：睡前夜间异步构建指令

适用场景：准备休息时向项目 Bot 派发夜间自主构建与调研任务，利用异步算力。触发方式：睡前手动发送。出处：@AlexFinn 方案 [X 引用](https://x.com/AlexFinn/status/2108319537116725426)

```text
I am about to go to sleep. What is one big, self-contained thing you can start building, researching, or testing in the cloud workspace while I am sleeping? Formulate the execution plan, execute the safe steps in /workspace, and leave a structured review card for when I wake up.
```

#### 模板 07：晨间决策聚焦与待办推进指令

适用场景：清晨起床时向个人助理 Bot 获取当下最关键的决策卡点清单。触发方式：清晨手动发送。出处：@AlexFinn 方案 [X 引用](https://x.com/AlexFinn/status/2108319537116725426)

```text
I just woke up. Review my calendar, inbox drafts, and active projects. Give me a concise list of top 3 decisions or approvals we can make right now to push the ball forward today. Group items by urgency, link each source context, and do not take external actions until I approve.
```

#### 模板 08：新号上手业务盘点与交接探索

适用场景：初次配置 Bot 时，连接常用通讯和文档后探索最适合交接的 3 项事务。触发方式：初次接入时手动发送。出处：@sidejob_AJ 方案 [X 引用](https://x.com/sidejob_AJ/status/2108592848300056956)

```text
Connect my email, calendar, and docs, then inspect recent activities and pick three concrete, low-risk recurring tasks I can safely hand off to you today. For each task, describe the expected input, the exact boundaries, and how you plan to draft results for my review.
```

#### 模板 09：个人工作负荷卸载盘点

适用场景：周期性盘点个人手头的繁琐事务，寻找可被技能化的低效环节。触发方式：双周手动复盘。出处：Roman Ugarte 访谈建议 [YouTube 访谈](https://www.youtube.com/watch?v=maSdsTLaMuU) （团队成员访谈）

```text
Analyze my recent sent emails, scheduled calendar meetings, and recurring document edits over the past two weeks. Identify the top 3 repetitive operational patterns that consumed my manual time. Propose a draft skill specification for each, explaining what you can take off my plate completely and what approval boundaries are required.
```

#### 模板 10：新增联系人跟进与草稿整理 Routine

适用场景：工作日早晨核对通讯录新增人员，预先草拟跟进任务而不直接外发。触发方式：工作日 08:30 定时触发。出处：@rowancheung 方案 [X 引用](https://x.com/rowancheung/status/2108328114552000842)

```text
Every weekday at 8:30am in my time zone, read my address book and list contacts added in the last 14 days. For each, show name, date added, phone, email, and any note. Ask me what we talked about before you write anything. Once I reply, draft a follow-up task for each person in [your task tool] with the context attached. Never text, email, or call anyone. Save this as a routine. If the address book is unavailable, say so and do not use old data.
```

### C.3 治理审计与成本控制类模板（模板 11–15）

#### 模板 11：Routine 成本与变更过滤审计

适用场景：对现有 Routine 深度体检，用事件驱动或低成本哈希校验替代高频轮询。触发方式：手动定期审计。出处：@fleyta88 方案 [X 引用](https://x.com/fleyta88/status/2109346840382415019)

```text
Audit my existing routines and rebuild the execution plan around actual changes.
1. List every routine, its schedule and expected output.
2. Replace polling with narrow event triggers where supported.
3. For frequent schedules, check only a hash, count or timestamp before doing full work.
4. Stop immediately when nothing changed.
5. Leave irreversible actions as drafts for human review.
6. Log every run with time, result, changed status and approval state.
7. Flag routines with over 95% no-change runs.
Show me the proposed changes and estimated savings first. Don't modify or delete anything without approval.
```

#### 模板 12：月度无产出 Routine 淘汰审计

适用场景：统计各 Routine 实际被采纳产出的比例，找出静默失败或无意义空转的任务并淘汰。触发方式：每月 1 日定时运行。出处：@kocer_eth 方案 [X 引用](https://x.com/kocer_eth/status/2101669438038634827)

```text
Monthly on the 1st at 9:00am, audit all active routines on this Bot. Review the last 20 run records for each routine: calculate the percentage of runs that produced actionable output approved by me, identify routines that failed silently or were ignored, and recommend at least one routine that should be paused or deleted with clear reasons. Present this report as a review table and wait for my explicit approval before modifying any routine.
```

#### 模板 13：云电脑系统更新前资产与配置备份

适用场景：在执行系统更新或重置云电脑前，将已装工具与环境清单固化备份。触发方式：手动维护触发。出处：@MilMileBattery 方案 [X 引用](https://x.com/MilMileBattery/status/2107033338548797471)

```text
Act as Chief of Staff. Before updating the Bot Computer:
1. Scan the environment and compile a shared checklist of all installed CLI tools, packages, and their reinstall commands into /workspace/system_manifest.md.
2. Verify all ongoing project scripts, credentials notes, and data files are located under /workspace.
3. Export a plain-text backup summary of our critical routines and environment variables so we can restore them immediately if a reset occurs.
4. Report when backup is completed.
```

#### 模板 14：跨 Bot 协作之“安静交接”Profile 预设

适用场景：配置在 Bot 的 Profile 描述中，杜绝 Bot 之间互相客套、唤醒并空转消耗额度。触发方式：常驻 Profile 设定。出处：Cursor 团队成员推荐 [论坛归档](https://forum.cursor.com/t/grokbot-custom-connectors/169965) （Cursor 员工论坛回复）

```text
Only message another bot when it needs to act. No acknowledgments, thanks, or progress pings. Send one concise summary when the work is done.
```

#### 模板 15：纠错固化与事实源反查规则

适用场景：纠正 Bot 的事实错误，强制其建立先查权威源再回答的长效习惯。触发方式：被纠错后手动发送。出处：@Michael_Fenech_ 方案 [X 引用](https://x.com/Michael_Fenech_/status/2106729045878514147)

```text
Remember this permanent rule: Whenever you are corrected on any factual information (such as dates, numbers, client status, or email details), you must immediately re-verify the authoritative source (Calendar, CRM, or Inbox) before answering. Never guess or hallucinate a replacement fact. Confirm that you have recorded this rule into your memory.
```

### C.4 官方系统提示词与标准工作流模板（模板 16–20）

#### 模板 16：官方采购 Haggle Bot 核心系统提示词

适用场景：全自动供应商支出审计、SaaS 席位闲置排查与合同续约谈判准备。触发方式：Bot 创建与初始化 Profile。出处：官方采购博客 [x.ai 采购案例](https://x.ai/news/grok-bot-procurement)

```text
SETUP — fill in for your org
SYSTEMS
- Spend data lives in: <e.g. Ramp, Brex, NetSuite>
- Contracts live in: <e.g. Drive, Notion, Ironclad>
- Usage/seat data comes from: <e.g. Okta/SSO logs, each tool's admin portal>
- Colleagues reachable via: <e.g. Slack, email>
- Vendor dossiers kept in: <e.g. Notion database, Drive folder>
PEOPLE
- Your operator: <name> — makes all final decisions.
- Who to ask about tool usage: <e.g. the owner listed in spend data, IT, team leads>
- Voice on external emails: <e.g. formal, sent under the operator's name, no agent names>
PERMISSION LINES
- Always allowed, no need to ask: <e.g. reading spend data, messaging colleagues, requesting admin access, pulling reports, updating dossiers>
- Needs the operator's explicit go, every time: <e.g. any vendor-facing send>
- Never, under any circumstances: <e.g. signing, buying, subscribing, approving charges, any binding commitment>
NEGOTIATION DIALS
- Renewal radar: prioritize renewals within <e.g. 120> days.
- Opening anchor: <e.g. 5–10>% below our internal target, never more than <e.g. 25>% off the vendor's latest quote.
- Acceptable reasons to give a vendor for an ask: <e.g. competitive process, market rate, budget>
- Never reveal to vendors: <e.g. usage data, seat counts, internal projects, timeline urgency, that we've decided to renew>
WHAT GOOD LOOKS LIKE (edit with your own vendors)
- Weak finding: "Renegotiate our CRM (~$50k)."
- Strong finding: "Video tool renews Oct 14. 210 seats, 74 idle for 90 days per admin logs. Drop to 150 at renewal = ~$18k/yr. Owner confirmed."
AGENT
You are Haggle Bot, a vendor-spend savings agent. Your job: know the company's vendor spend cold and produce evidence-backed savings, like a sharp procurement colleague — not a list of big vendors to "renegotiate." Operate within the permission lines above without exception.
LEAD WITH THE MONEY — every finding opens with:
TODAY: what we pay now, annualized, from live data, with source.
SAVE: realistic savings and mechanism, with confidence.
REC: one committed recommendation — a menu of options is not a recommendation.
NEXT: what you've already set in motion. (Internal actions happen before you report, not as offers — never "I can ping X if you want.")
PRIORITIZE EVIDENCE: a real opportunity has a dollar figure traced to live spend data, a specific mechanism, and a reason it's actionable now (renewal window, usage data, competing quote). Anything less is a lead — label it, name the missing data, and go get it rather than assuming. Match the "strong finding" example above.
WORK THE CALENDAR: maintain a renewal calendar from billing and contract data; renewals inside the radar window are your priority queue. Leverage lives at renewal.
DO THE RESEARCH YOURSELF: a renewal, quote, or proposal in play means research runs before you recommend anything — never advise "exploring alternatives," explore them. Price 3+ real alternatives against our actual SKU footprint from the live invoice, cite and date every number, state list vs. street price, and include switching costs honestly.
NEGOTIATE DELIBERATELY: before any vendor-facing draft, show the operator the plan — target, opening anchor (within the dials above), walk-away, what we trade for what, and your next two moves if they reject, counter, or go silent. In the message: one reason per ask from the acceptable list, nothing from the never-reveal list, every line priced (unpriced lines get priced by the vendor), and a close where "no" isn't a complete reply — aimed at the rate on the biggest negotiable line, never at lines where our savings come from cutting quantity. Warm tone, firm numbers: the rep argues our case internally, so write to make that easy. A rejected draft is rebuilt from the plan, never edited.
REMEMBER EVERYTHING: keep a per-vendor dossier — spend, terms, renewal date, owner, quotes gathered, and the operator's verdicts. When the operator rejects something, log why and don't repeat the pattern.
VOICE: with the operator — direct, dollars first, no fluff. External — per the voice setting above.
```

#### 模板 17：官方标准技能保存范式（Save a Skill）

适用场景：将一次成功的操作总结并保存为全账户共享的私有技能，固化边界与验证规则。触发方式：完成一次人工调优任务后发送。出处：官方技能文档 [cursor.com/help/grok-bot: Skills](https://cursor.com/help/grok-bot/skills-routines-and-automations)

```text
Save the process we just used as a skill called "Weekly account health". Include the source systems, risk definitions, output format, and the rule that customer contact always requires approval. State explicitly when to use it, required inputs and access, step sequence, how to validate results, and what requires human sign-off.
```

#### 模板 18：官方标准定时 Routine 调度范式

适用场景：将已保存的 Skill 挂载到特定 Bot 名下定时执行，包含严格的缺数退避逻辑。触发方式：调度配置时发送。出处：官方技能文档 [cursor.com/help/grok-bot: Skills](https://cursor.com/help/grok-bot/skills-routines-and-automations)

```text
Every weekday at 8:00 AM, run the Daily customer-risk skill against the current account list. Post a linked watch list in this conversation. Do not contact customers. If the source data is unavailable, report the failure instead of using old data. Save this as a routine.
```

#### 模板 19：官方事件驱动触发 Routine（Webhook / Slack）

适用场景：基于协同软件事件窄匹配触发任务，杜绝无脑监听全量消息。触发方式：配置事件触发时发送。出处：官方技能文档 [cursor.com/help/grok-bot: Skills](https://cursor.com/help/grok-bot/skills-routines-and-automations)

```text
When a message in #customer-escalations contains a support ticket link and the phrase "needs repro", open the ticket, reproduce the issue in staging, and post a repro pack in this conversation. Never post back to Slack without approval. Save this as an event routine.
```

#### 模板 20：官方前置审批与安全边界声明范式

适用场景：要求 Bot 仅做分析与预算建议草案，禁止私自修改投放后台或联系外部代理。触发方式：派发涉及资金或生产环境任务时发送。出处：官方安全与审批文档 [cursor.com/help/grok-bot: Approvals](https://cursor.com/help/grok-bot/approvals-security-and-privacy)

```text
Reconcile the campaign data and draft a recommended budget change. Do not change the campaign or message the agency. Ask for approval after showing the current value, proposed value, and expected impact.
```

### C.5 岗位分工与专职 Bot 设定模板（模板 21–25）

#### 模板 21：官方标准专注型工位设定（Piper - 产品性能巡检）

适用场景：创建专注于性能指标异动、证据链条保留与低侵入的专职工程师 Bot。触发方式：新建 Bot 填写 Profile。出处：官方入门文档 [cursor.com/help/grok-bot: Get Started](https://cursor.com/help/grok-bot/get-started)

```text
Name: Piper
Job: Product performance
Description: Investigate product-performance questions using our observability tools. Preserve links and screenshots, separate evidence from hypotheses, and return a short summary with the highest-impact issue first. Never change production settings.
```

#### 模板 22：官方文档入门任务：文档提炼与决策点提取

适用场景：五分钟零插件入门，验证 Bot 对长文本的结构化提取与边界遵守能力。触发方式：拖入文档附件后发送。出处：官方入门文档 [cursor.com/help/grok-bot: Get Started](https://cursor.com/help/grok-bot/get-started)

```text
Summarize this document in five bullets. List every date, decision, and open question in a separate section. Cite the page or section for each item. Do not change the source file.
```

#### 模板 23：官方数据分析任务：转化异动对比与排查预案

适用场景：对接分析面板对比用户活跃数据，形成假说但不修改线上配置。触发方式：手动发起专项调研。出处：官方入门文档 [cursor.com/help/grok-bot: Get Started](https://cursor.com/help/grok-bot/get-started)

```text
Open our analytics dashboard and compare new-user activation for this week with the previous four weeks. Identify the largest step-level change and draft a short investigation plan with links to the relevant charts. Do not change any dashboards. Ask me to sign in if needed.
```

#### 模板 24：DevRel 工程师原型开发流水线（Matt Palmer）

适用场景：工作日扫描社交书签，提炼痛点草拟 Prompt，交给云端 Agent 编写原型并开 PR。触发方式：工作日定时触发。出处：官方指南实践总结 [X 引用](https://x.com/monokern/status/2108533543848558780)

```text
Every weekday at 10:00am, scan my bookmarked X threads on developer pain points. Pick the most requested utility idea, draft an implementation specification, and hand it over to a Cursor Cloud Agent to build a working prototype. Open a GitHub pull request with an attached summary video and demo link. Never merge the PR automatically.
```

#### 模板 25：销售外联与通话简报就绪助理（Simon Lackowski）

适用场景：工作日早晨 8 点前备妥外联名单、客户通话简报与待审批回复卡。触发方式：工作日早晨 07:30 定时触发。出处：官方销售指南实践总结 [X 引用](https://x.com/monokern/status/2108533543848558780)

```text
Every weekday by 7:30am, review my CRM pipeline and incoming customer emails. Prepare a briefing dossier for today's scheduled sales calls, highlighting current contract value, past blockers, and suggested talk track. Draft follow-up emails for yesterday's meetings and present them as approval cards. Do not send any external communication.
```

### C.6 研发、多模型调度与本地化落地模板（模板 26–30）

#### 模板 26：Opus 5.5 云端 Agent 协同研发分工指令

适用场景：由 Grok Bot 统筹架构拆解，调度 Cursor 云端 Agent 挂载高阶模型编码，严守合并门禁。触发方式：发起工程重构或复杂特性开发。出处：社区分工栈实践 [X 引用](https://x.com/i/status/2109265867859177552)

```text
Act as Lead Architect. Break down this feature request into discrete implementation modules. Delegate the complex backend logic and core algorithm to a Cursor Cloud Agent using Opus 5.5, and delegate the unit tests to a secondary agent. Coordinate their output in /workspace, run the test suite, and present a linked pull request with diff summary. Do not merge anything without my explicit approval.
```

#### 模板 27：中文自媒体矩阵：三道硬门岗位 Profile（觉醒AI）

适用场景：在国内多平台内容生产中，用落盘文件管理调性，封死发布权限，防止越权误发。触发方式：内容 Bot 初始化 Profile。出处：觉醒AI 内容团队实录 [深度文章](https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/)

```text
你是自媒体内容主笔 Bot。严格执行三道硬门纪律：
1. 事实来源门：只认我直接给出的链接和文件，禁止抓取未经核实的营销号内容。
2. 数据核验门：所有引用的性能、价格与财务数据必须来自 /workspace 下的实测报告，并在文中标明核对日期。
3. 发布权限门：你拥有只读与草拟权限，绝对禁止调用发布接口或点击网页发布按钮。成稿全部落盘为 /workspace/drafts/ 下的 Markdown 文件等待人工审核。
```

#### 模板 28：公众号与小红书爆款情报侦察员 Routine

适用场景：定向抓取公开内容源、转写视频文案并归档至知识库，遇到验证码停下交回控制权。触发方式：每天上午 09:30 定时触发。出处：觉醒AI 媒体实践 [文章归档](https://www.jxxy.net/ai/articles/AdrianPunk115-2097311704547987756/)

```text
Every weekday at 9:30am, browse the specified public topic pages. Extract trending titles, user engagement metrics, and recurring comment questions from the past 24 hours. If any platform prompts a login wall or CAPTCHA, stop immediately, alert me, and hand over the browser controls. Save findings to /workspace/intel/daily_digest.md and notify me in chat. Do not interact, like, or post on any platform.
```

#### 模板 29：国内平台无插件环境下的导出巡检与风控避让

适用场景：在无官方插件的国内后台，避免高频连击触发风控，通过读屏或导出文件完成盘点。触发方式：每周五下午 17:00 定时巡检。出处：象鱼工作流实践 [用例总结](https://xiangyugongzuoliu.com/grokbot-use-cases/)

```text
Open the logged-in media backend on the cloud browser. Navigate to the analytics tab, download this week's readership and retention CSV export to /workspace/analytics/, and calculate the average completion rate. Do not perform rapid automated clicks across multiple menus. Once the CSV is saved, close the browser tab, generate a summary table in our chat, and delete temporary download files.
```

#### 模板 30：自定义私有 MCP 服务器挂载指令

适用场景：为全账户挂载具备公网 HTTPS 接口的自定义 MCP 工具服务，扩展原生插件库。触发方式：直接在聊天框向 Bot 发送。出处：Cursor 官方论坛员工回复 [forum.cursor.com](https://forum.cursor.com/t/grokbot-custom-connectors/169965) （Cursor 员工论坛回复）

```text
Add this MCP server: https://your-tools-gateway.example.com/mcp
```

### C.7 2026-10-25 新增高阶实战与安全治理模板（模板 31–36）

本小节收录了 2026 年 10 月中下旬随 [Grok Bot 官方更新日志](https://x.ai/changelog/bot) v0.71.2、v0.75.2 与 v0.75.5 上线而涌现的 6 套高阶实战与安全治理模板，涵盖 Pages 实时团队状态看板、1Password Brokered Sign-in 与 Vault 零知识安全代购、`+alias` 邮箱子别名定向触发、BDK（`cursor-grokbot-agents`）跨端调用、确定性 Python 脚本零额度抓榜，以及自迭代 Skill 防臃肿与冲突审计。

#### 模板 31：Pages 实时团队状态看板生成与同步模板

- **适用场景**：当你拥有 5 个以上专职 Bot 并行运转、不希望逐一点开聊天窗口排查进度时，让主控幕僚长（Chief of Staff）Bot 调用内置的 `WriteCanvas` / `EditCanvas` 工具创建并持续热更新一张 `Activity Dashboard` 实时交互页面（沉淀于右侧 `Bot info pane → Library`，支持 `Only you`、`Your team`、`Anyone with the link` 三级分享权限）。
- **触发方式**：首次在 Chief of Staff Bot 会话中手动发送下方提示词初始化 Page，随后绑定为每小时或每 30 分钟运行的定时 Routine 自动同步各专职 Bot 状态。
- **出处**：源自 `@melvindvivas` 分享的 Chief of Staff `Activity Dashboard` 实战范式（[主帖](https://x.com/melvindvivas/status/2113676935956160882)、[提示词拆解帖](https://x.com/melvindvivas/status/2113676938820895045)、[Routine 自动刷新跟帖](https://x.com/melvindvivas/status/2113968491573514576)）、`@JayKurtz90` 的看板评述（[https://x.com/JayKurtz90/status/2113983882018119823](https://x.com/JayKurtz90/status/2113983882018119823)），以及官方 `@bot` Pages 发布公告（[https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)）与官方 [Files and Results 帮助文档](https://cursor.com/help/grok-bot/files-and-results)。

```text
你现在的角色是我的「Chief of Staff（幕僚长 Bot）」。请使用你的 Pages（Canvas）工具，为我的整个 AI 团队创建并长期维护一个名为「Grok Bot Activity Dashboard」的实时交互式状态看板页面（若该 Page 已存在于 Library 中，请直接调用 EditCanvas 原地热更新，严禁重复新建多个同名 Page）。

### 一、数据源采集范围
请扫描并汇总以下渠道的最新状态：
1. 共享工作区目录 `/workspace/shared-status/` 下各专职 Bot 写入的最新 JSON/Markdown 任务日志；
2. 团队群聊（Group Chats）中各专职 Bot（如 `@Researcher`、`@Writer`、`@GrowthBot`、`@OpsBot`）在过去 24 小时内的回报记录；
3. 当前挂起等待人类处理的审批事项（Approval Cards / 1Password 请求 / 结账确认）。

### 二、Page 看板核心四大视图结构
请在同一个 Page 中使用清晰的模块化布局、状态徽章与交互式筛选器渲染以下四个核心区域：

1. **⏳ 实时时间线视图（Timeline View）**
   - 按时间倒序展示过去 24 小时内所有专职 Bot 的关键动作节点（格式：`[HH:MM] [Bot 名称] 动作摘要 + 产出物链接`）。
2. **🔄 进行中任务（Tasks in Progress）**
   - 表格列：`任务名称` | `负责 Bot` | `开始时间` | `当前子步骤进度` | `预计完成时间`。
3. **✅ 已完成交付（Completed Tasks）**
   - 表格列：`任务名称` | `负责 Bot` | `完成时间` | `核心结果摘要` | `交付物路径/链接`。
4. **🚨 等待人工审批与阻塞项（Items Waiting for Human Approval）**
   - 置顶高亮展示所有卡在人工确认环节的事项（例如：等待 1Password 生物识别授权、等待外发邮件确认、等待大额代购结账审批、或 Webhook 报错阻塞），注明已等待时长与一键跳转提示。

### 三、共享工作流契约与定时刷新规则
1. 请将本 Page 的更新规范写入 `/workspace/shared-status/DASHBOARD_SOP.md`：要求所有专职 Bot 每当「开始新任务」、「完成阶段交付」或「遇到人工审批阻塞」时，必须同步更新各自的状态记录，以便本看板实时映射。
2. 每次 Routine 触发刷新本 Page 时，若没有新增的「🚨 等待人工审批事项」，请仅静默更新 Page 内容并在顶部更新 `Last synced at: YYYY-MM-DD HH:MM:SS`，不要发送冗余聊天弹窗打扰我；仅当存在超过 30 分钟未处理的阻塞审批项时，才在聊天窗口向我发送简短提醒。
```

#### 模板 32：1Password Brokered Sign-in + Vault 安全代购模板

- **适用场景**：假设你需要让专职采购或行政助理 Bot 定期登录电商平台、航司酒店或 SaaS 后台完成比价与代购下单，同时希望严格执行 `@martinpaulweiss` 提出的“一密一宅（One home per secret）”机密隔离原则，并规避 `@kial` 与 `@JianWeiSignal` 警示的“已存 Vault 银行卡在结账时不弹单独逐笔 Vault 确认框”的潜在资金风险。
- **触发方式**：在专职采购 Bot 的会话中手动触发，或写入采购 Bot 的系统提示词（System Prompt / Skill）作为全局代购铁律。
- **出处**：源自官方 [Connect Apps 帮助文档](https://cursor.com/help/grok-bot/connect-apps)、官方 [Secrets & Vault 帮助文档](https://cursor.com/help/grok-bot/secrets)、官方 [Work 登录与结账优先级技术文档](https://cursor.com/docs/grok-bot/work)、官方 `@bot` 公告（[1Password 集成](https://x.com/bot/status/2113301060811161874)、[Vault 发布](https://x.com/bot/status/2113754107861532677)）、`@elonmusk` 关于 SpaceX 代购差错全额赔付的公开承诺（[https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445)），以及社区 `@martinpaulweiss`（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）、`@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）、`@JianWeiSignal`（[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488)）与 `@LisaMAUSA`（[https://x.com/LisaMAUSA/status/2114208018388643852](https://x.com/LisaMAUSA/status/2114208018388643852)）的实战安全总结。

```text
请帮我执行以下安全代购任务，并严格遵守「1Password 逐次授权登录 + Vault 提示标签寻址 + 结账前强制人工确认」三道安全防线：

### 一、采购目标与预授权预算上限
- **目标商品/服务**：[填写具体商品名称、型号、规格与数量，例如：星巴克大杯冰美式 1 杯 / 某云服务月度套餐]
- **指定商户站点**：[填写目标网站域名]
- **单笔预授权最高预算上限（Hard Cap）**：$[填写金额，例如：35.00] USD（含税费、运费与服务费的总计实付金额）。若最终结账页面总价超出此上限 $0.01，必须立即中止流程并向我报错，严禁继续提交。

### 二、凭据与收货信息调用规范（One Home per Secret）
1. **网站登录（Sign-in）**：
   - 若当前云端浏览器会话未处于已登录状态，请发起 **1Password Brokered Sign-in** 请求（弹出 `Review in 1Password`），等待我在本地 1Password App（v8.12.42+）中通过生物识别批准注入 Personal/Private 密码库中的登录凭据与 2FA 验证码。
   - 严禁在聊天窗口中要求我发送明文账号、密码或短信验证码。
2. **收货地址与联系人（Contact Info）**：
   - 请从 `Settings → Vault` 的 Contact info 中读取明文 **Hint** 标记为 `[填写地址 Hint，例如：Home Delivery / Office Address]` 的条目，使用 `BrowserSecureFill` 自动填充收货人姓名、电话与地址。
3. **支付方式（Payment Method）风控策略**：
   - 【模式 A：调用 Vault 已存专项限额卡】仅允许匹配 Vault 中明文 **Hint** 为 `[填写卡片 Hint，例如：Work Travel Only / Daily Coffee Card]` 的指定卡片。
   - 【模式 B：零常驻卡单次安全表单】若 Vault 中未保存该指定 Hint 的卡片，请弹出聊天内掩码 **Secure Form**（或调用 **Link / X Money**），由我单次手动输入支付信息（默认不勾选常驻保存到 Vault）。

### 三、结账前强制人工确认闸门（Mandatory Pre-Checkout Gate）
**核心红线**：由于保存在 Vault 中的银行卡在底层 `BrowserSecureFill` 注入时不会触发单独的逐笔 Vault 弹窗，你在进入最终结账页面（Checkout Page）、填入收货地址后、**点击最终扣款按钮（如 `Place Order` / `Pay Now` / `Complete Purchase`）之前，必须无条件暂停**，并在聊天窗口向我输出以下核对清单：
1. 当前结算页面的完整截图（需清晰包含商品明细、数量、收货地址、运费、税费及应付总额）；
2. 拟调用的支付方式名称及 Vault Hint 标识；
3. 价格校验结论：`应付总额 $XX.XX <= 预授权上限 $XX.XX（通过/超支）`。

只有在收到我明确回复「确认下单」后，你才被允许执行最终的支付提交点击，并在完成后将订单号与电子收据归档至 `/workspace/orders/` 目录。
```

#### 模板 33：专属邮箱 `+alias` 子别名定向触发 Routine 模板

- **适用场景**：利用每个 Grok Bot 专属 `@mail.grokbot.com` 邮箱原生支持的 `+alias` 加号子别名能力，将外部新闻通讯（Newsletters）、SaaS 电子发票（Invoices）、服务器告警（Alerts）分流到同一个 Bot 的不同子别名（如 `mybot+newsletters@mail.grokbot.com`），实现“指定别名定向触发对应 Routine + 保留完整 HTML/内嵌图片原样转发 + 周末汇总生成 Pages 精华周报”，让个人主邮箱彻底清净且不浪费多余 Routine 运行配额（官方在 [Routines 帮助文档](https://cursor.com/help/grok-bot/routines) 中支持单条 Routine 最高 200 次/小时、全账号所有 Bot 合计 300 次/小时）。
- **触发方式**：在 `Routines` 中新建邮件事件触发器（Trigger: `When an email arrives`），将收件地址过滤条件严格限定为 `收件人（To）包含 yourbot+newsletters@mail.grokbot.com`（同理可建 `+invoices`、`+alerts` 独立 Routine）。
- **出处**：源自 Grok Bot 工程师 `@SamSokolin` 发布的 `+alias` 官方特性说明（[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)）、官方 [Agent Email 帮助文档](https://cursor.com/help/grok-bot/agent-email)、官方 [Routines 帮助文档](https://cursor.com/help/grok-bot/routines)，以及社区 `@songsong275452` 与 `@gokul_i` 的 Newsletter 专属邮箱接管工作流（[https://x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371)）与 `@AIShovelLab` 的联动总结（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）。

```text
### 【Routine 配置元信息】
- **触发条件（Trigger）**：收到新邮件（Email received），且收件地址（`To` / `Delivered-To`）精确匹配子别名：
  - 分支 A：`yourbot+newsletters@mail.grokbot.com`（行业通讯与深度长文）
  - 分支 B：`yourbot+invoices@mail.grokbot.com`（账单、收据与订阅扣款通知）
  - 分支 C：`yourbot+alerts@mail.grokbot.com`（监控报警与紧急通知）

---

### 【Routine 执行提示词正文】
请检查刚刚触发本条 Routine 的入站邮件头（`To` 字段、发件人 `From`、主题 `Subject`），并严格按照收件子别名后缀执行以下对应的标准作业程序（SOP）：

#### 分支 A：若收件地址为 `+newsletters@mail.grokbot.com`
1. **静默归档与结构化入库（零打扰模式）**：
   - 提取邮件正文核心观点、发布日期、原文链接及关键数据图表描述；
   - 将其清洗为标准 Markdown 笔记，追加写入 `/workspace/inbox/newsletters/YYYY-WXX-digest.md`（按自然周分卷存储）；
   - **平时收到单封 Newsletter 时，严禁在聊天窗口弹窗提醒我，也严禁转发到我的个人主邮箱**。
2. **周六精华周报汇总（配合周六定时触发或满 15 篇触发）**：
   - 当检测到当前时间为周六上午 09:00（或本周累积归档满 15 篇通讯）时，读取本周 `YYYY-WXX-digest.md` 中的全部条目；
   - 按「🔥 本周必读 Top 3」、「🛠️ 新工具与开源项目」、「📊 行业关键硬数据」、「💡 选题灵感钩子」四个板块生成或更新一张名为 `Weekly Newsletter Briefing` 的 **Page（Canvas）**，并在聊天窗口向我推送该 Page 卡片。

#### 分支 B：若收件地址为 `+invoices@mail.grokbot.com`
1. **账单字段提取与台账登记**：
   - 解析邮件正文及 PDF 附件中的：`商户名称`、`扣款金额`、`币种`、`计费周期（月付/年付）`、`下次续费日期`；
   - 将记录追加写入 `/workspace/finance/subscriptions-ledger.csv`。
2. **异常扣款检测与原样转发**：
   - 若发现单笔金额 > $50 或属于首次出现的新增扣款商户，请调用邮件原样转发能力（完整保留原邮件的 **HTML 排版格式、正文内嵌图片 inline images 与 PDF 发票附件**），将其转发至我的财务归档邮箱 `[填写你的财务邮箱]`，并在聊天窗口向我发出简短审计提醒。

#### 分支 C：若收件地址为 `+alerts@mail.grokbot.com`
1. **紧急告警分级响应**：
   - 立即提取报错堆栈或故障服务名称，先在云电脑上执行一次连通性自检；
   - 若确认为 P0/P1 级故障，立即保留完整 HTML 与内嵌监控截图原样转发至我的主邮箱，同时在聊天窗口置顶告警。
```

#### 模板 34：BDK (`cursor-grokbot-agents`) 跨端调用命令模板

- **适用场景**：当你希望在本地电脑的 **Claude Code**、**Codex** 或 **Cursor IDE** 终端中直接向云端 **Grok Bot** 派发任务（例如：让云端 Bot 调用原生免费 X 检索查全网实测舆情、在云端渲染 20 秒 Remotion/Blender 视频，或唤醒云端长驻记忆），或者在 Agent 非交互式 Shell 中因标准输入（stdin）未闭合导致 CLI 挂起卡死、以及遭遇 Webhook 复杂 JSON 400 报错时，使用本套跨端命令与 Python 标准库桥接模板实现毫秒级无阻塞互通。
- **触发方式**：在本地终端、Claude Code / Codex 技能脚本或 Grok Bot 云端沙箱 Shell 中直接运行下方命令。
- **出处**：源自 `@gokul_i` 的 BDK 跨端工作流分享（[https://x.com/gokul_i/status/2111246539738288522](https://x.com/gokul_i/status/2111246539738288522)）、`@LLMJunky` 的智能体桥接实践（[https://x.com/LLMJunky/status/2110996403434963063](https://x.com/LLMJunky/status/2110996403434963063)）、`@StarkLJM`（Mr.鼓先生）使用 BDK 派单渲染 20 秒中国史动画的实测教程（[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411)）、`@37FlowAI` 追加 `< /dev/null` 修复非交互式 Shell 挂起卡死的排错方案（[https://x.com/37FlowAI/status/2111334386339823687](https://x.com/37FlowAI/status/2111334386339823687)）、`@mikan77_aoi` 用 4 次纯标准库 API 调用绕过 Webhook 400 报错的脚本范式（[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)），以及 `@AbhisheKumarA7` 的完成时 Webhook 零轮询唤醒方案（[https://x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578)）。

```bash
#!/usr/bin/env bash
# ==============================================================================
# 模板 34：BDK (cursor-grokbot-agents) 跨端双向派单与非交互防卡死脚本集
# ==============================================================================
set -euo pipefail

# ------------------------------------------------------------------------------
# 1. 安装/同步 cursor-grokbot-agents (BDK) 技能桥接并列出可用云端 Bot
# ------------------------------------------------------------------------------
# 在本地 Claude Code / Codex / Cursor 终端中验证 BDK 环境（注意追加 < /dev/null 闭合 stdin）
npx skills add cursor-grokbot-agents < /dev/null

# ------------------------------------------------------------------------------
# 2. 本地 CLI (Claude Code / Codex) -> 向云端专职 Grok Bot 派发任务
#    核心防坑（源自 @37FlowAI）：非交互式 Shell 调用任何 Agent CLI（如 bdk / pi / codex）
#    必须在末尾追加 `< /dev/null`，防止进程因等待 stdin EOF 信号而无限期挂起！
# ------------------------------------------------------------------------------
TARGET_BOT_HANDLE="@research-bot"
TASK_PROMPT="请调用内置免费 X 搜索工具，检索过去 48 小时内关于 Grok Bot Pages 和 Vault 的高赞实战帖（min_faves:20），提炼成结构化 Markdown 报告并保存至 /workspace/shared/x-intel-latest.md，完成后仅回复文件路径与 3 条核心结论。"

# 通过 BDK 非阻塞派单给云端 Grok Bot（闭合 stdin）
cursor-grokbot-agents send \
  --bot "${TARGET_BOT_HANDLE}" \
  --message "${TASK_PROMPT}" \
  --wait < /dev/null

# 若在云电脑内使用轻量级 Pi Agent + DeepSeek 省额度调度（源自 @hppzyy & @37FlowAI）：
# pi -p "读取 /workspace/raw.json 并生成清洗后的 Markdown 表格" < /dev/null

# ------------------------------------------------------------------------------
# 3. 零依赖 Python 标准库 4 步状态机桥接（源自 @mikan77_aoi）
#    适用场景：当直接向 Webhook POST 复杂多行代码块/特殊字符触发 HTTP 400 校验错误时，
#    使用纯 Python urllib.request 标准库执行干净的 UTF-8 JSON 编码与状态接力
# ------------------------------------------------------------------------------
python3 - <<'EOF' < /dev/null
import json
import os
import time
import urllib.request

BDK_ENDPOINT = os.environ.get("GROKBOT_BDK_API_URL", "https://cursor.com/api/grok-bot/v1")
API_TOKEN = os.environ.get("GROKBOT_API_TOKEN", "YOUR_TOKEN_HERE")
BOT_ID = os.environ.get("GROKBOT_TARGET_ID", "YOUR_BOT_ID")

def api_call(method: str, path: str, payload: dict | None = None) -> dict:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload else None
    req = urllib.request.Request(
        url=f"{BDK_ENDPOINT}{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "grokbot-stdlib-bridge/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

# 若你配置了实际凭证，可执行标准 4 步调用：
# Step 1: GET  /agents/{BOT_ID}/status          (检查目标 Bot 在线与空闲状态)
# Step 2: POST /agents/{BOT_ID}/threads         (创建干净的隔离任务会话上下文)
# Step 3: POST /threads/{THREAD_ID}/messages    (提交严格序列化的任务载荷，规避 Webhook 400)
# Step 4: GET  /threads/{THREAD_ID}/artifacts   (回收云端渲染好的 MP4 视频或 Markdown 产物)
print("BDK stdlib bridge template ready.")
EOF

# ------------------------------------------------------------------------------
# 4. 长耗时任务完成时主动触发 Webhook 唤醒 Grok Bot（零轮询省额度，源自 @AbhisheKumarA7）
#    在云电脑或家里的常开 Mac mini Worker 上跑完长任务后，最后一行回调触发唤醒：
# ------------------------------------------------------------------------------
# codex exec "完成全量构建与测试" < /dev/null && \
# curl -fsSL -X POST "${GROKBOT_ROUTINE_WEBHOOK_URL}" \
#   -H "Content-Type: application/json" \
#   -d '{"event":"build_done","status":"success","artifact":"/workspace/dist/bundle.zip"}' < /dev/null
```

#### 模板 35：确定性 Python 脚本零额度抓榜 + 阈值唤醒模板

- **适用场景**：针对每日定时抓取热榜、竞品价格、GitHub Trending 或运营指标等高频重复任务，彻底告别“每次让大模型开浏览器读网页烧掉大量周额度”的低效做法，改为践行 `@StarkLJM`（Mr.鼓先生）实测验证的**“AI 花 28.6 秒写一次确定性 Python 脚本 → 脚本每天 1.99 秒零模型额度跑日常抓取 → 仅当触发异常/突破阈值时才通过 Webhook 唤醒大模型介入”**的极致省电架构。
- **触发方式**：先将第一段提示词发给 Grok Bot 生成 `/workspace/scripts/deterministic_rank_fetcher.py`，再通过云电脑系统 `crontab` 定时运行该脚本（日常耗电 **0 Token**），并绑定一条仅在收到异常告警时才启动的 Webhook Routine。
- **出处**：源自 `@StarkLJM`（Mr.鼓先生）的“28.6 秒写脚本、每天 1.99 秒零额度抓 30 条榜单”实战案例与防御性编程规范（[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377) 与 [https://x.com/starkljm/status/2112818533797343312](https://x.com/starkljm/status/2112818533797343312)），以及 `@charlie_pmp` 关于三合一订阅周额度池防静默消耗的分析（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）。

```bash
#!/usr/bin/env python3
"""
模板 35：确定性 Python 脚本零额度抓榜 + 防御性空值校验 + 阈值唤醒模板
日常由系统 cron 直接执行本脚本（0 模型 Token 消耗）；
仅当检测到「字段结构缺失」或「新晋爆款突破阈值」时，才 POST Webhook 唤醒 Grok Bot 分析。
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

TARGET_API_URL = os.environ.get("RANK_SOURCE_URL", "https://example.com/api/v1/trending?limit=30")
WEBHOOK_URL = os.environ.get("GROKBOT_ALERT_WEBHOOK_URL", "")
OUTPUT_DIR = "/workspace/data/rankings"
SCORE_SPIKE_THRESHOLD = 9.0  # 仅当出现评分 >= 9.0 的新上榜项目时才唤醒 Bot

REQUIRED_FIELDS = {"id", "title", "url", "rank"}

def trigger_grokbot_webhook(reason: str, payload: dict) -> None:
    """仅在异常或高价值异动时唤醒 Grok Bot，平时保持 0 Token 静默。"""
    if not WEBHOOK_URL:
        print(f"[WAKE-TRIGGER] {reason}: {json.dumps(payload, ensure_ascii=False)}")
        return
    body = json.dumps({
        "trigger_reason": reason,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data": payload,
    }, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        print(f"Webhook notified ({resp.status}): {reason}")

def fetch_and_validate() -> int:
    start_ts = time.perf_counter()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    req = urllib.request.Request(
        TARGET_API_URL,
        headers={"User-Agent": "deterministic-fetcher/1.0"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        raw_data = json.loads(resp.read().decode("utf-8"))

    items = raw_data.get("items", [])
    if not isinstance(items, list) or len(items) == 0:
        trigger_grokbot_webhook("SCHEMA_DRIFT_EMPTY_LIST", {"url": TARGET_API_URL})
        return 1

    cleaned_records = []
    high_signal_hits = []

    for idx, item in enumerate(items[:30], start=1):
        # 防御性规则 1：核心字段缺失立即触发结构漂移告警，严禁静默吞错
        missing = REQUIRED_FIELDS - set(item.keys())
        if missing:
            trigger_grokbot_webhook(
                "SCHEMA_DRIFT_MISSING_FIELDS",
                {"index": idx, "missing_fields": sorted(list(missing)), "raw_sample": item},
            )
            return 2

        # 防御性规则 2（源自 @StarkLJM）：源数据缺失评分时严格存入 None (JSON null)，
        # 绝不允许用 0 或 0.0 填充，防止拉低后续均值与分位数统计！
        raw_score = item.get("score", None)
        score = float(raw_score) if raw_score is not None and raw_score != "" else None

        record = {
            "rank": int(item["rank"]),
            "id": str(item["id"]),
            "title": str(item["title"]).strip(),
            "url": str(item["url"]).strip(),
            "score": score,  # 严格保持 float 或 None (null)
        }
        cleaned_records.append(record)

        if score is not None and score >= SCORE_SPIKE_THRESHOLD and record["rank"] <= 5:
            high_signal_hits.append(record)

    # 计算均值时严格剔除 score is None 的样本
    valid_scores = [r["score"] for r in cleaned_records if r["score"] is not None]
    avg_score = round(sum(valid_scores) / len(valid_scores), 3) if valid_scores else None

     elapsed = round(time.perf_counter() - start_ts, 2)
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_path = os.path.join(OUTPUT_DIR, f"rank-{today_str}.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "date": today_str,
                "elapsed_seconds": elapsed,
                "count": len(cleaned_records),
                "valid_score_count": len(valid_scores),
                "avg_score": avg_score,
                "items": cleaned_records,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    print(f"[OK] Fetched {len(cleaned_records)} items in {elapsed}s (0 model tokens). Saved to {out_path}")

    # 仅当捕捉到高分异动时，才唤醒 Grok Bot 进行深度解读
    if high_signal_hits:
        trigger_grokbot_webhook(
            "HIGH_SIGNAL_BREAKOUT",
            {"file": out_path, "avg_score": avg_score, "hits": high_signal_hits},
        )
    return 0

if __name__ == "__main__":
    sys.exit(fetch_and_validate())
```

#### 模板 36：自迭代 Skill 防臃肿与冲突审计模板

- **适用场景**：当你允许专职 Bot 在日常复盘中自动将经验教训写入自己的 `SKILL.md`、`AGENTS.md` 或记忆文件时，随着时间推移极易出现 `@eze_is_1`（一泽Eze）所指出的“规则越写越长、前后条款互相打架、特殊 Case 补丁堆叠成屎山、甚至诱发盲目重试浪费额度”的退化现象。使用本模板每周或每两周对全库 Skill 进行一次正交化瘦身、冲突消解与路由边界审计。
- **触发方式**：建议配置为每周日晚上运行一次的维护型 Routine，或在感觉某个专职 Bot 响应变慢、指令遵循率下降时手动发送。
- **出处**：源自 `@eze_is_1`（一泽Eze）关于多 Bot 架构与自迭代 Skill 防臃肿法则的深度长文（[主帖](https://x.com/eze_is_1/status/2109850538045264151)、[进阶跟帖 1](https://x.com/eze_is_1/status/2109852993982206425)、[进阶跟帖 2](https://x.com/eze_is_1/status/2110532874000879886)、[进阶跟帖 3](https://x.com/eze_is_1/status/2110866224892850547)）、`@AIShovelLab` 关于用路由 Skill 阻止盲目重试的范式总结（[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)），以及 `@Khazix0918`（[https://x.com/Khazix0918/status/2111709708226797737](https://x.com/Khazix0918/status/2111709708226797737)）与 `@object_nullll`（[https://x.com/object_nullll/status/2111717423837778173](https://x.com/object_nullll/status/2111717423837778173)）关于“对话层收集上下文并委派执行、严禁裸聊硬扛重活”的架构讨论。

```text
你现在的角色是「Agent Skill 架构审计官」。请对我工作区中的所有自定义技能文件（扫描 `/workspace/.cursor/skills/**/SKILL.md`、`/home/box/.cursor/skills/**/SKILL.md` 以及项目根目录的 `AGENTS.md`）执行一次全面的**防臃肿瘦身、逻辑冲突消解与路由熔断审计**。

### 一、四大核心病灶扫描清单
请逐一读取目标 Skill 文件，重点排查以下四类因“历史自迭代追加”导致的劣化问题：

1. **⚔️ 前后矛盾与逻辑冲突（Contradictory Rules）**
   - 检查文件头部的基础原则与文件尾部历次复盘追加的 `补丁/注意事项/Hotfix` 是否存在冲突（例如：前文要求“精简输出不超过 300 字”，后文某次复盘又追加“必须完整展开所有原始数据表”）。
2. **🎈 同义重复与补丁膨胀（Patch Bloat & Redundancy）**
   - 找出因不同日期遇到相似报错而反复追加的多条碎片的“禁止……”或“务必……”，将其抽象合并为一条正交、通用的结构化规则；
   - 将属于一次性特定历史任务的临时上下文剥离出 `SKILL.md` 主文件，归档至 `references/` 或 `archive/` 子目录（按需加载，不常驻污染主上下文窗口）。
3. **🔁 盲目重试与额度黑洞（Blind Retry & Token Drain）**
   - 检查 Skill 是否缺少明确的**失败熔断与路由止损机制**（源自 `@AIShovelLab` 防盲目重试规范）：任何外部工具调用、网页抓取或 CLI 命令若连续失败 **2 次**，必须立即停止原地死循环重试，改为切换备用路由（如开启本机 IP 流量转发、改调确定性脚本或上报人工介入）。
4. **🏗️ 对话层与执行层职责错位（Conversational vs. Worker Layer Mismatch）**
   - 审计该 Skill 是否错误地让对话路由层直接硬扛超长代码生成、大批量网页遍历等重度苦力（源自 `@object_nullll` 架构准则）；若是，请将其改写为“对话层对齐验收标准（Acceptance Criteria）+ 委派给 `CloudAgent` / 本地 CLI Worker / 确定性 Python 脚本执行”。

### 二、审计报告与重构交付要求
1. **先出诊断对比表，再改文件**：
   - 请先输出一份结构化审计报告，列出每个被扫描的 `SKILL.md` 的：`当前行数/Token 估算`、`发现的冲突条款原句行号`、`冗余补丁条数`、`瘦身重构后的预计行数（目标压缩率 >= 30%，且核心约束零丢失）`。
2. **备份与原子替换**：
   - 在修改任何 `SKILL.md` 之前，先将原文件备份至同目录下的 `SKILL.md.bak-YYYYMMDD`；
   - 重构后的 `SKILL.md` 必须严格包含四个正交区块：`1. 触发边界与职责定位（When to Use / Not Use）`、`2. 标准执行流水线（Step-by-Step SOP）`、`3. 失败熔断与最多 2 次重试上限（Circuit Breaker）`、`4. 验收清单（Acceptance Checklist）`。
```

## 附录 D 连接器分类清单 · Connectors Catalog

在 Grok Bot 里，连接器（Connectors）是以插件形式装在整个账户下的。只要添加并在浏览器里完成授权，你名下的所有 Bot 都能共用。截至 2026-10-12 基线统计，[官方应用连接库](https://cursor.com/help/grok-bot/connect-apps)收录了 238 个插件，覆盖 10 大分类；而在 2026-10-13 至 2026-10-25（覆盖至 v0.75.5）版本周期内，[官方更新日志](https://x.ai/changelog/bot)与[官方帮助中心](https://cursor.com/help/grok-bot)又重磅扩容了 **1Password Brokered Sign-in（逐次代理授权免密登录）**、**Grok Bot Vault（内置加密保险箱）**、**Link / X Money 结账支付**、**iOS Calendar / Reminders / Contacts 原生三件套直连**、**X 插件全栈能力（X Chat `@chat` 端到端加密私信、Scheduled X Calls 预约通话、Livestreams RTMP/RTMPS 直播推流与弹幕治理）** 以及 **BDK（`cursor-grokbot-agents` 跨端双向桥接）**。

> [!NOTE]
> 📸 **截图位（待补）**：Connect Apps 应用市场与分类筛选视图

### D.1 十大官方分类全量连接器速查表

以下为[官方应用连接指南](https://cursor.com/help/grok-bot/connect-apps)覆盖的十大分类全量连接器速查表：

| 分类名称 | 收录总数 | 包含的全部插件清单（英文原名） | 类别属性与主要作用 |
|---|---|---|---|
| Password Managers | 1 | 1Password | 凭据管理：为云电脑提供受控的密码填充金库 |
| Productivity | 63 | Adobe Developer App Builder, Airtable, Asana, Atlassian, Atlassian Forge, Atlassian Teamwork Graph CLI, Box, Canva, ChatPRD, ClickUp, Coda, Craft, Descript, Fathom, Fireflies, GitBook, GitLab, Glean, Glean Developer Docs, Google Docs, Granola, GSAP, Guru, Harness, IcePanel, Jam, Jotform, Juicebox, LaunchDarkly, Linear, Listen Labs, MagicPath, Mem, Mintlify, Miro, Monday.com, Notion, OneDrive, Otter.ai, Paper, Playwright, Profound, Read AI, ReadMe, Readwise, Resend, Riverside, Runway, Sanity, Smartsheet, Svelte, Teams, TierZero, Todoist, Typeform, UiPath, Upwork, Webflow, Wix, Workable, Wrike, Xero, Zapier | 办公协作、项目管理、文档笔记与工作流触发 |
| Communication | 29 | ActiveCampaign, AgentMail, Ando, Bird, Brevo, Calendly, Customer.io, Fireflies, Gmail, Google Calendar, Infobip, Inkbox, Klaviyo, Knock, Linq, MailerLite, Mailgun, Migma, Nitrosend, Outlook, Outlook Calendar, postiz, Slack, Superhuman Mail, Typeform, Upwork, Workable, X, Zoom | 邮件收发、日程规划、IM 频道消息与社交沟通 |
| Design | 13 | Canva, Docs Canvas, Figma, Google Slides, Mobbin, Mural, Paper, PR Review Canvas, Refero, Slides.com, Superdesign, tldraw, Wonder | 视觉设计、原型预览、幻灯片制作与画板协作 |
| Code | 53 | Amazon Location Service, Appwrite, AWS Amplify, AWS Core, AWS Databases, AWS Deployments, AWS Serverless, Azure, Browserless, Browserstack, Clerk, Cloudflare, CockroachDB, Compound Engineering, Convex, Coralogix, Create Plugin, Datadog, Docker, Encore, Firebase, Floot, GoDaddy, incident.io, JFrog, Knock, Lightrun, MongoDB, Monk.io, Neon Postgres, Netlify, PagerDuty, ParadeDB, Pinecone, PlanetScale, Railway, Redis, Render, Runlayer, ScyllaDB, Sentry, Supabase, Superpowers, Temporal, turbopuffer, Turso, Twilio, Vantage, Vercel, WorkOS, Zscaler, GitHub, Origin | 代码托管、云原生基础设施、数据库与监控报警 |
| Data | 39 | Amplitude, Antimetal, Apify, Astronomer, AWS Data Analytics, Azure Cosmos DB, Braintrust, Bright Data, ClickHouse, Confidence by Spotify, Customer.io, Dagster, dbt Labs, Elastic, Exa, Firecrawl, Fullstory, Grafana Cloud, Grafana Labs, Hex, Hugging Face, Langfuse, Mixpanel, Monid, Observe by Snowflake, Omni Analytics, Omni Integrations, OpenSearch, Parallel, Pendo, PostHog, Postman, prisma, Semrush, Similarweb, Smartsheet, Snowflake, Statsig, ThoughtSpot | 数据仓库、埋点分析、网页数据抓取与模型可观测性 |
| Sales | 16 | Adspirer, Amplemarket, Apollo.io, Attio, Clarify, Clay, Customer.io, Gojiberry AI, Gong, Granola, HubSpot, Hunter, Monaco, Outreach, Salesforce, ZoomInfo | 客户关系管理、获客线索挖掘与销售跟进 |
| Finance | 25 | 1inch, Aave, Airwallex AgentOS, Airwallex Developer, Brex, Capital.com, Chargebee, Circle, Docusign, Kraken, Link, Mercury, Natural, Orthogonal, PayBox, Phantom, Ramp, Razorpay, RevenueCat, RevenueCat Play Billing, Revolut X, Shopify, Stripe, Whop, Xero | 支付网关、电商交易、对账报销与加密资产集成 |
| Research | 11 | Ahrefs, Context.dev, Context7, Crustdata, Harmonic, Parallel, Semrush, SuperMe, Treg, UserTesting, You.com | SEO 调研、商业情报洞察与网络研究 |
| Support | 3 | Intercom, MailerLite, Plain | 客户支持工单、消息归集与服务流流转 |

### D.2 核心高频连接器实战特性与边界

假设你在日常工作流中高频调用最常用的主流工具与系统级内置连接能力，它们在插件与原生集成模式下的核心支持能力和边界如下（完整涵盖原有高频插件及 v0.71.2–v0.75.5 新增连接器）：

| 工具名称 | 对应插件分类 | 核心支持能力 | 关键边界与防踩坑要点 | 来源 |
|---|---|---|---|---|
| Gmail | Communication | 检索阅读邮件、草拟、发送、打标签、清理垃圾箱 | 企业 Google 账户可能需要 IT 管理员在后台预先批准 Grok 应用 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Outlook / M365 | Communication / Productivity | Outlook 邮件与联系人、日历日程增删、OneDrive 文件检索、Teams 频道收发 | [官方插件库](https://cursor.com/help/grok-bot/connect-apps)拆分为 4 个独立插件，没有单一名为 Microsoft 365 的全家桶，需逐个添加 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Google Calendar | Communication | 读取日程空闲、创建/修改会议、应答邀请 | 插件无法修改 Google Meet 内部设置，也无法自动注入 Zoom 链接 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Slack | Communication | 以当前用户身份读取与发言、参与频道与工作流讨论 | 一个连接对应一个 Workspace；发起的 Routine 需单独配置事件监听 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Notion | Productivity | 检索页面与数据库、创建/更新记录、发布内容 | 支持连接第二个账户，可在调用时指明“使用我的工作 Notion” | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| GitHub | Code | 检索 PR、处理 Issue、代码审查、触发工作流 | 客户端自带内置集成（Connect GitHub 按钮），插件列表无卸载按钮 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| 1Password | Password Managers | 云电脑浏览器自动填充登录凭据 | 连接后仅读取名为“Shared with Grok Bot”的特定保险库，其他金库隔离 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| X (Twitter) | Communication | 原生搜索推文、时间线、趋势、书签与 X Chat | 插件会消耗开发账户 API 额度，付费 Grok Bot 计划附赠起始免费额度 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| 1Password Brokered Sign-in（v0.75.2 新版） | Password Managers | 与 `"1Password for Agents"` 同步上线，通过 `Review in 1Password` 在本地电脑/手机 1Password App 内逐次生物识别或 Passkey 审批注入凭据，无需共享密码库或 Service Account，Bot 永不接触明文密码 | 需本地安装并解锁 **1Password app 8.12.42+**；默认仅读取 Personal / Private vault 条目（Shared 或自定义库需迁入 Personal/Private 库才可读取）；旧版用户可在 `Settings → Connect apps` 断开重连以无缝升级 | [Connect Apps 文档](https://cursor.com/help/grok-bot/connect-apps) / [`@bot` 公告](https://x.com/bot/status/2113301060811161874) / [`@1Password` 公告](https://x.com/1Password/status/2113276767582498943) |
| Grok Bot Vault（v0.75.5 内置保险箱） | System Built-in (`Settings → Vault`) | 只写（write-only）加密存储 **Logins（含 2FA/TOTP）**、**Cards（支持手机摄像头 Scan 扫卡）** 与 **Contact info**；支持 **5 MB** CSV 批量导入（兼容 1Password、Chrome、Safari、Firefox、Bitwarden、LastPass）及明文 **Hint** 标签供 Bot 选卡/选号，底层通过 `BrowserSecureFill` 注入 | **高危审批红线**：保存在 Vault 中的银行卡在结账填充时**不会触发单独的逐笔 Vault 弹窗确认**（仅受通用购买审批约束），若需每笔消费手动把关切勿将卡常驻保存在 Vault 中（参见 `@kial` 与 `@JianWeiSignal` 警示）；建议遵循 `@martinpaulweiss` 的“一密一宅”法则与 `@LisaMAUSA` 的 Vault Tidy 去重模板 | [Secrets & Vault 文档](https://cursor.com/help/grok-bot/secrets) / [Work 文档](https://cursor.com/docs/grok-bot/work) / [`@bot` 公告](https://x.com/bot/status/2113754107861532677) |
| Link / X Money（v0.71.2 结账支付） | Finance / Built-in Checkout | 支持在结账流程中调用 Link 与 X Money 完成付款（需用户审批）；使用 X Card 经由 Grok Bot 完成的交易在账单流水中展示专属 Grok Bot 徽章（`@gofordylan` 实测） | 结账调用优先级为 `Vault → 聊天内 Secure Form → Link / X Money → Take over screen`；Elon Musk（`@elonmusk`）公开承诺若 Grok Bot 代购出错或泄露银行卡，SpaceX 将全额赔付（*"SpaceX will make you whole"*） | [Work 文档](https://cursor.com/docs/grok-bot/work) / [x.ai: Changelog](https://x.ai/changelog/bot) / [`@elonmusk` 承诺帖](https://x.com/elonmusk/status/2110610960474079445) |
| iOS Calendar / Reminders / Contacts（v0.75.2 原生三件套） | Mobile Built-in (iOS App) | Grok Bot iPhone 客户端在获得系统授权后，直接读取并操作 iOS 本地的 **Calendar（日历）**、**Reminders（提醒事项）** 与 **Contacts（通讯录）** | 仅限 iOS 客户端本地授权生效；配合 iOS v1.16+ 的 iPhone Action Button（iPhone 15 Pro 及后续机型）与 `"Hey Siri"` 快捷指令可实现随身全语音秘书（参见 `@TyeInBloom` 实战） | [Mobile 文档](https://cursor.com/help/grok-bot/mobile) / [Voice Chat 文档](https://cursor.com/help/grok-bot/voice-chat) / [x.ai: Changelog](https://x.ai/changelog/bot) |
| Agent Email `+alias` 与原样转发（v0.71.2 / v0.75.2） | Communication (`@mail.grokbot.com`) | 每个 Bot 的专属邮箱支持 `+alias` 加号子别名（如 `mybot+newsletters@mail.grokbot.com`）收发邮件并支持按指定 `+alias` 定向触发 Routine（`@SamSokolin`）；v0.75.2 起转发邮件完整保留 HTML 排版、内嵌图片与附件 | 可将各类 Newsletter 订阅至专属别名并由周六 Routine 汇总精华周报（`@songsong275452` / `@gokul_i`），避免主邮箱污染与 Routine 误触发消耗周额度 | [Agent Email 文档](https://cursor.com/help/grok-bot/agent-email) / [Routines 文档](https://cursor.com/help/grok-bot/routines) / [`@SamSokolin` 公告](https://x.com/SamSokolin/status/2110496237241667621) |
| X Chat（`@chat` 端到端加密私信） | Communication (X Plugin) | 打通 X `@chat` 私信收件箱与陌生人消息请求（message requests），支持分拣私信、逐条审查批准陌生人请求及起草发送回复（`@pjvann`） | 采用 `xchat_lite` 端到端加密，MCP 仅返回加密载荷与 Juicebox 配置；Bot 需在云端沙箱克隆官方 [`xchat-grokbot-helper`](https://github.com/xdevplatform/xchat-grokbot-helper) 运行 `xchat_tool.py`，配合用户 **4 位数字 X Chat PIN 码**在本地完成解密与发送 | [`xchat-grokbot-helper` 官方仓库](https://github.com/xdevplatform/xchat-grokbot-helper) / [`@pjvann` 公告](https://x.com/pjvann/status/2111104660773687646) / [Connect Apps 文档](https://cursor.com/help/grok-bot/connect-apps) |
| Scheduled X Calls（X 预约通话） | Communication (X Plugin) | 通过 `schedule_call`、`list_scheduled_calls` 等工具创建、查看及回复（RSVP）X 平台预约通话，并与 Spaces（语音空间）、Communities（社群）、Lists（列表读写与成员管理）及 Bookmarks 深度协同 | 若发现通話、直播、Spaces 或 Lists 工具缺失而其他 X 工具正常，只需在 `Settings → Connect apps` 中断开并重新连接（Reconnect）X 插件即可恢复；内置公开 X 读取免费，私有账号数据访问依规可能使用 `console.x.com` 额度 | [Connect Apps 文档](https://cursor.com/help/grok-bot/connect-apps) |
| Livestreams（RTMP/RTMPS 直播与弹幕治理） | Communication (X Plugin) | 支持创建与管理 RTMP/RTMPS 推流源（stream sources）、创建预约直播广播（scheduled broadcasts）、在直播结束后自动汇总弹幕聊天记录（summarize ended broadcast chat），以及管理直播间房管（moderators）与禁言名单（mutes） | 适合配合 OBS 或云电脑推流进行无人值守直播运营与播后复盘；若遇连接器工具列表未刷新，通过重连 X 插件解决 | [Connect Apps 文档](https://cursor.com/help/grok-bot/connect-apps) |
| BDK（`cursor-grokbot-agents` 跨端双向桥接） | Code / Developer Kit | 通过 Bot Developer Kit（BDK）与 `cursor-grokbot-agents` 技能桥接，实现本地编码 Agent（Claude Code、Codex、Cursor IDE）与云端 Grok Bot 双向派单与结果回收，并支持在常开 Mac mini 上注册 `Settings > Computer` 远程节点及部署 `cursor-agent worker`（`@ericzakariasson`） | 已在 `@StarkLJM`（本地 Claude Code 派单云端渲染 20 秒中国史动画）、`@kangxiaile`、`@z_lumia`、`@charlychoi`、`@pomufgd`、`@SyrianVeterans` 等工作流中验证；若遇 Webhook 复杂 JSON 报 HTTP 400，可参考 `@mikan77_aoi` 用 4 次标准库 API 调用直接桥接 | [Work 文档](https://cursor.com/docs/grok-bot/work) / [`@StarkLJM` 实战帖](https://x.com/starkljm/status/2109544938644107411) / [`@ericzakariasson` 教程](https://x.com/ericzakariasson/status/2114157733276525044) |

> **登录与结账调用优先级补充说明（源自[官方 Work 技术文档](https://cursor.com/docs/grok-bot/work)）**：
> - **网站登录（Sign-in）调用优先级**：Bot 云电脑上已保存的浏览器会话（Saved browser session） → **Grok Bot Vault** → **1Password（Brokered Sign-in / Shared Vault）** → 聊天内 **Secure Form** → **Take over screen（人工接管屏幕）**。例如 `@oxpsats` 将彭博社（Bloomberg）会员凭据存入 1Password 授权给 Grok Bot，即可全自动突破付费墙研读海外核心财经文章。
> - **结账支付（Checkout / Payment）调用优先级**：**Grok Bot Vault** → 聊天内 **Secure Form** → **Link / X Money** → **Take over screen（人工接管屏幕）**。

### D.3 热门未入库服务对策与高危黑名单

不少服务目前在 [Connect Apps 官方应用库](https://cursor.com/help/grok-bot/connect-apps)里没有官方插件，甚至有封号风险。常见缺失项的处理对策与社区踩坑警示如下：

| 服务名称 | 官方插件现状 | 替代操作路径 | 风险级别与避坑指南 | 来源 |
|---|---|---|---|---|
| WhatsApp | 无官方插件 | 云电脑浏览器登录 Web 版 | 极高风险：社区反馈用户将 Bot 接到 WhatsApp 后个人账号被封禁 | [r/GrokBot 封号反馈](https://www.reddit.com/r/GrokBot/comments/1w11r70/)  |
| LinkedIn | 无官方插件 | 云电脑浏览器登录 Web 版 | 高风险：社区反馈 Bot 自动发信后导致该账号所有登录会话被强制吊销 | [r/GrokBot 踢会话反馈](https://www.reddit.com/r/GrokBot/comments/1wp291u/)  |
| Google Drive / Sheets | 无独立插件 | 仅提供 Google Docs 与 Google Slides 插件 | 中风险：表格与网盘需借由浏览器网页版或通过其他办公插件间接读写 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| Zoom | 已列入市场但不可用 | 暂无可用插件连接 | 明确故障：登录授权报 Error 4700（Invalid redirect），目前只能在日历手动贴链接 | [learngrokbot: Plugins](https://learngrokbot.com/plugins)  |
| 自定义内部服务 | 无开箱即用插件 | 自建 MCP Server 挂载 | 低风险：地址必须为公网可访问的 HTTPS 协议，Bot 无法直接穿透本地 localhost | [forum.cursor.com 讨论](https://forum.cursor.com/t/grokbot-custom-connectors/169965) （Cursor 员工论坛回复） |
| 严苛反爬站点 / 内网私有设备 | 无独立插件（云机房 IP 易被拦截） | 开启桌面端 `Settings > Computer > Your computer > Route traffic through this computer` 或在云电脑配置 Tailscale | 低风险高收益：`@XueshiQiao` 验证开启本机流量路由后可借用家里/办公室真实住宅 IP 绕过云机房 Captcha 反爬拦截（v0.75.5 已修复本地流量转发稳定性）；`@lyuan1618` 验证在云电脑安装 Tailscale 可与家用 NAS 及内网服务器组建加密 LAN Mesh；企业管理员还可在后台配置出站域名白名单并勾选 `Apply to MCP servers`（参见[官方 Security 文档](https://cursor.com/docs/grok-bot/security)） | [Settings 文档](https://cursor.com/docs/grok-bot/settings) / [`@XueshiQiao` 实战帖](https://x.com/XueshiQiao/status/2112866936229183589) / [`@lyuan1618` 实战帖](https://x.com/lyuan1618/status/2114214704008798674) |

## 附录 E 版本更新日志 · Changelog Timeline

Grok Bot 迭代很快。官方更新日志（https://x.ai/changelog/bot）每个版本都标有发布日期（此前基线 v0.68.1 为 2026 年 10 月 7 日，最新 v0.75.5 为 2026 年 10 月 23 日）。如果按时间轴梳理[官方更新日志](https://x.ai/changelog/bot)从首发到最新版（涵盖 v0.17.0 至 v0.68.1 全部 49 个历史版本，以及 2026-10-13 至 2026-10-25 期间发布的 v0.71.2、v0.75.2、v0.75.5 与五项内部 Release Feed 重大特性）的核心改动，可以清晰看到这条完整演进时间线。原基线核对日期是 2026-10-12，最新增量核对日期已更新至 2026-10-25。

![Grok Bot 架构演进与版本里程碑时间轴](../images/fig-A1-3.png)

*图：Grok Bot 架构演进与版本里程碑时间轴*

### E.1 关键里程碑版本概览

| 阶段里程碑 | 对应核心版本 | 关键突破功能与行业意义 |
|---|---|---|
| 资格全面扩档 | v0.27.0 | 正式向 Cursor Pro、SuperGrok 和 X Premium+ 付费用户放开访问，奠定大众普及基础 |
| 跨平台与国际化 | v0.21.0 / v0.28.0 | 引入多语言包（含简体与繁体中文），上线 Webhook Routine 接口 |
| 团队协作与共享 | v0.30.0 / v0.31.0 | 上线 Bot 模板链接分享、Link 钱包支付卡审批，引入 Cloud Agent 独立打开模式 |
| 交互与表单重构 | v0.44.0 / v0.45.0 | 推出聊天内嵌表单（Chat forms）、邮件/Slack 草稿确认卡与企业级 Auto-review 规则 |
| 企业与安全治理 | v0.40.0 / v0.50.0 | 全面放开企业版，上线审计日志，推出 Route egress 本地电脑网络出口代理 |
| 团队 Bot 时代 | v0.61.0 | 推出 Team Bots 体系，实现全团队共享 Bot、Slack 深度双向打通与成员独立记账 |
| 主动性与办公扩展 | v0.66.0 / v0.68.1 | 星标主 Bot 具备主动揽活能力（Proactivity），原生支持 PPT 与 Google Slides 演示文稿生成 |
| 视频创作、支付赔付背书与 `+alias` 邮箱路由 | v0.71.2（2026-10-14） | 原生集成 Grok Imagine 生图/生视频与代码动效渲染；打通 Link 与 X Money 结账并获 Elon Musk 宣布 SpaceX 全额赔付背书；上线 `@mail.grokbot.com` 的 `+alias` 加号别名与定向 Routine 触发 |
| 三合一统一订阅与随身硬件语音交互 | The X Subscription（2026-10-18） / iOS v1.16（2026-10-19） | Grok Bot 正式并入 **The X Subscription**（$30 Premium / $100 Super / $200 Ultra 共享周额度池与 Prepaid Credits），上线两个月突破 80 万周付费用户；iPhone 15 Pro+ 支持侧边 Action Button 长按一键发起实时语音通话 |
| 实时交互画布、1Password 逐次授权与高频调度扩容 | Pages（2026-10-21） / v0.75.2（2026-10-22） | 上线 **Pages（Canvas）** 实时看板与三级分享权限；联合 1Password 首发 **Brokered Sign-in** 免共享库逐次授权登录；打通 iOS 原生日历/提醒事项/通讯录与邮件原样 HTML 转发；Routine 频次上限跃升至全账号 300 次/小时、单条 200 次/小时 |
| 内置加密保险箱与全栈凭据闭环 | v0.75.5（2026-10-23） | 正式上线 **Grok Bot Vault**（`Settings → Vault`），支持只写加密保存登录凭据（含 2FA）、银行卡（含手机扫卡与 5 MB CSV 导入）及联系人地址，配合明文 Hint 标签与 `BrowserSecureFill` 实现零明文暴露安全自动填充 |

### E.2 全量版本演进速查表（v0.17.0 至 v0.75.5）

| 版本号 | 核心功能改动与演进记录 | 适用范围 | 来源 |
|---|---|---|---|
| v0.75.5（2026-10-23） / `grok-bot-vault`（2026-10-22） | **Grok Bot Vault 正式全面上线**：开放 `Settings → Vault` 内置加密只写（write-only）保险箱，统一存储 **Logins（账号/密码/2FA TOTP）**、**Cards（信用卡/借记卡，支持移动端摄像头 Scan 扫卡识别）** 与 **Contact info（地址/电话/邮箱）**；支持从 1Password、Chrome、Safari、Firefox、Bitwarden、LastPass 批量导入最高 **5 MB** 的 CSV 文件；支持为每个条目添加 Bot 可读的明文 **Hint** 标签，底层通过 `BrowserSecureFill` 注入且永不向模型暴露明文（注意：已存入 Vault 的银行卡在结账填充时不会触发单独的逐笔 Vault 弹窗确认）；同步修复多项安全与稳定性问题（含本地电脑流量转发修复） | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot) / [Secrets & Vault 文档](https://cursor.com/help/grok-bot/secrets) / [`@bot` 公告](https://x.com/bot/status/2113754107861532677) |
| v0.75.2（2026-10-22） / `grok-bot-onepassword`（2026-10-22） | **1Password Brokered Sign-in 上线**：与 `"1Password for Agents"` 同步推出，支持在本地电脑或手机 **1Password app（需 8.12.42+）** 内通过生物识别或 Passkey 逐次审批登录请求（`Review in 1Password`），无需创建共享密码库或 Service Account，默认读取 Personal / Private vault；**iOS 原生三件套集成**：iPhone 客户端授权后可直接读写本地 **Calendar（日历）**、**Reminders（提醒事项）** 与 **Contacts（通讯录）**；**邮件原样转发**：`@mail.grokbot.com` 与外部连接邮箱转发邮件时完整保留 HTML 格式、正文内嵌图片与附件；**Routine 频率上限大幅上调**：提升至**全账号所有 Bot 合计 300 次/小时**、**单条 Routine 最高 200 次/小时**；**Auto-review 减噪**：对当前对话轮次中用户已明确下令的操作减少冗余二次确认卡片；同步实装 **Pages（Canvas）** 能力 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot) / [Connect Apps 文档](https://cursor.com/help/grok-bot/connect-apps) / [Routines 文档](https://cursor.com/help/grok-bot/routines) / [Agent Email 文档](https://cursor.com/help/grok-bot/agent-email) / [`@bot` 公告](https://x.com/bot/status/2113301060811161874) |
| Release Feed `grok-bot-pages`（2026-10-21） | **Pages（Canvas）实时交互页面与看板发布**：Bot 可通过底层 `WriteCanvas` / `EditCanvas` / `ReadCanvas` / `ListCanvases` 工具创建并持续热更新包含表格、图表、时间线与交互组件的实时网页应用（如周报大盘、Chief of Staff `Activity Dashboard` 多 Bot 协同看板），永久沉淀在右侧信息栏 `Bot info pane → Library` 中；支持三级分享权限：**Only you（仅自己）**、**Your team（团队可见，管理员可在 `Dashboard → Grok Bot → Bot capabilities` 全局关闭）** 与 **Anyone with the link（公开链接访问）** | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot) / [`@bot` 公告](https://x.com/bot/status/2112991843235610885) / [`@melvindvivas` 看板案例](https://x.com/melvindvivas/status/2113676935956160882) |
| Release Feed `grok-bot-on-the-action-button` / iOS v1.16（2026-10-19） | **iPhone Action Button 一键实时语音通话**：将 Grok Bot iOS 客户端更新至 **v1.16+** 后，在 **iPhone 15 Pro 及后续机型**上可通过 `Settings → Action Button → Shortcut → Grok Bot → Start Voice Chat` 直接呼叫主 Bot，或在 iOS **Shortcuts（快捷指令）** 中配置 `Start Voice Chat with Bot`（可选 `Ask Each Time` 或固定专职 Bot，亦支持 `"Hey Siri"` 语音唤醒及 `grokbot://app/v1/agent?id=YOUR_BOT_ID` URL Scheme）；通话支持静音、实时字幕展开及音色/语速/语种设置，挂断后自动在聊天流生成含通话时长与完整逐字稿的 **Voice chat card** 并立即跟进执行 | iOS 端（v1.16+） / 全员 | [Voice Chat 文档](https://cursor.com/help/grok-bot/voice-chat) / [Mobile 文档](https://cursor.com/help/grok-bot/mobile) / [`@bot` 公告](https://x.com/bot/status/2112246033178968161) |
| Release Feed `grok-bot-on-the-x-subscription`（2026-10-18 / 公告于 2026-10-13） | **并入 The X Subscription 三合一统一订阅**：单一计划打包整合 **Grok**、**Cursor** 与 **X Premium**，其中 **Premium（$30/月）**、**Super（$100/月）**、**Ultra（$200/月）** 包含 Grok Bot 权限（Free $0 与 Plus $8/月不含）；三端共享同一个每周固定重置的周额度池（weekly usage pool），超额用量与 Cursor 第三方模型调用从 `grok.com/dashboard/billing` 的 **Prepaid Credits（预付额度，支持 Auto Top-up 与月度封顶限额）** 中扣除；支持通过 `cursor.com/unify` 或 `accounts.x.ai/unify` 单向合并升级（不可退回 Legacy 独立计划，Web 端旧订阅自动按比例退费，但 **App Store / Google Play 订阅必须手动取消以防双扣**） | 全员 | [Plans 计费文档](https://cursor.com/help/grok-bot/plans) / [The X Subscription 总览](https://cursor.com/help/the-x-subscription/overview) / [`@bot` 公告](https://x.com/bot/status/2110063783796572496) |
| X Plugin 扩容：X Chat `@chat` / Calls / Livestreams（2026-10-16） | **X 插件全栈能力扩容**：正式打通 `@chat` 端到端加密私信收件箱与陌生人消息请求审批（底层由云电脑克隆 [`xchat-grokbot-helper`](https://github.com/xdevplatform/xchat-grokbot-helper) 配合 Juicebox 与 **4 位数字 X Chat PIN 码**本地解密）；同步支持 **Scheduled X Calls**（`schedule_call` / `list_scheduled_calls` 预约通话与 RSVP）以及 **Livestreams**（RTMP/RTMPS 推流源管理、预约直播广播、直播结束弹幕汇总、房管与禁言治理） | 全员 | [`xchat-grokbot-helper` 官方仓库](https://github.com/xdevplatform/xchat-grokbot-helper) / [`@pjvann` 公告](https://x.com/pjvann/status/2111104660773687646) / [Connect Apps 文档](https://cursor.com/help/grok-bot/connect-apps) |
| v0.71.2（2026-10-14） | **Grok Imagine 生图/生视频与代码动效渲染**：内置调用 `GenerateImage`、`GenerateVideo` 直接生成和编辑图像与视频，并支持结合云电脑代码渲染 Remotion / Motion Graphics 动态图形视频；**Link 与 X Money 结账支持**：支持调用 Link 与 X Money 付款（X Card 流水展示专属 Grok Bot 徽章），Elon Musk 于 10 月 15 日公开承诺代购差错或卡泄露由 SpaceX 全额赔付；**专属邮箱 `+alias` 加号别名**：`@mail.grokbot.com` 支持 `+alias` 子别名收发并支持按特定别名定向触发 Routine（`@SamSokolin`）；**通知与体验优化**：iOS 与 Android 推送通知支持 Deep-link 直达对应 Bot 聊天窗口，简化登录与账号关联流程，优化文件预览与下载体验 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot) / [`@bot` 视频公告](https://x.com/bot/status/2110566041772617908) / [`@elonmusk` 承诺帖](https://x.com/elonmusk/status/2110610960474079445) / [`@SamSokolin` 公告](https://x.com/SamSokolin/status/2110496237241667621) |
| v0.68.1 | 1:1 对话支持匹配 Bot 主题色；支持协同生成 PPT 和 Google Slides 演示文稿；草稿卡支持富文本排版邮件；Gmail 垃圾邮件检索与恢复；Team Bot 支持提及 Slack 用户组；输入框键入 `/` 不再弹出技能菜单；云电脑屏幕升至 1920×1200 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.68.0 | 新增马拉地语、泰米尔语、泰卢固语、斯瓦希里语和豪萨语；设置页支持移除其他电脑；Gmail 草稿支持别名发送；命令面板直接检索插件 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.67.0 | 全新设计的 Connect Apps 侧栏入口与新型工作状态展示 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.66.0 | 主动性（Proactivity）：星标主要 Bot 会主动发现潜在任务并提议代劳（需 v0.59.0 以上）；更稳定的自动更新机制 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.65.0 | 团队成员可与 Team Bot 发起独立语音通话；客户端自动更新可靠性增强 | Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.64.0 | 邮件与 Slack 草稿卡提供“停用草稿”选项以允许直接发送；已发布的 Team Bot 支持添加管理员协同维护 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.63.0 | Slack 线程中支持交互式审批卡（仅发起者可点击）；在 Slack 中可通过 Team Bot 私信个人 Bot | Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.62.0 | 选中文字按 `Cmd/Ctrl+L` 快速引用；输入框支持 `-` 或 `1.` 快速生成列表；输入拼写检查；团队管理端按名搜索 Team Bot | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.61.0 | 推出 Team Bots：全团队共享单个 Bot、在 Slack 中直接调用、成员间独立记账并保留私有笔记 | Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.60.0 | Outlook 邮件草稿卡支持：在对话中审核内容后直接一键发送 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.59.0 | 超时过期的 Auto-review 卡片提供“未来始终允许”选项；企业管理后台支持 Team Secrets 团队密钥注入 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.58.0 | 新增捷克语、丹麦语、芬兰语、匈牙利语与挪威语；企业版支持 30 天未活动电脑自动销毁（Terminate Inactive Computers） | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.57.0 | Projects 功能上线：支持启动 Cloud Agent 规划复杂任务并调度多子 Agent 协同；丰富链接预览卡片 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.56.0 | GitHub 增强、表格文件交互优化与更清晰的审批卡片展示 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.55.0 | 安装引导清单（Setup Checklist）与对话内嵌表单自动填充能力优化 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.54.0 | 搜索体验增强、HEIC 格式照片支持；企业管理员可在后台批量删除成员电脑与数据 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.53.0 | Mac 端支持连接 1Password 密码管理器并实现自动填充；支持直接向 Google Drive/OneDrive 上传文件 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.52.0 | GitHub 连接器优化；Routine 支持手动暂停与恢复 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.51.0 | 首次启动自动引导创建首个 Bot；支持彻底删除 Routine；Bot 支持自主微调标题与头像颜色外观 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.50.0 | 设置中推出“Route egress through this desktop”，支持将云电脑网络出口引流至本地设备 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.49.0 | 仓库授权卡支持 GitHub、GitLab、Bitbucket、Azure DevOps；消息中的文件路径可直接点击定位打开 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.48.0 | 多账户平滑切换；Marketplace 支持直接一键添加 Bot；企业版上线 Conversation Insights 统计大盘 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.46.0 | Usage & Billing 页面改版；对话列表支持右键重命名 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.45.0 | 邮件与 Slack 草稿卡机制（审核后发送或丢弃）；企业管理员可强制开启团队级 Auto-review 规则 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.44.0 | 聊天内嵌表单（Chat forms）：遇到登录或关键输入时在聊天框呈现表单；消息时间戳悬停查看；Mac 自动填充 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.41.0 | Marketplace 正式列出 Bot 模板；官方自研 Bot 带有 Verified 认证徽章 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.40.0 | 企业版全面开放（GA）；新增乌尔都语、泰语和孟加拉语；企业后台上线 Audit Logs 完整审计日志 | Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.39.0 | 新增越南语与印尼语支持；新增个性化问候语引导 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.38.0 | 企业组访问权限控制（Group Access）与侧边栏分组名称优化 | Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.37.0 | 安装流程调查日常使用工具；企业控制台显示企业试用期剩余天数 | 全员 / Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.36.0 | 消息中 PR 卡片支持右键复制链接；Routine 对话展示流优化；Always allow 规则增强 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.35.0 | 长周期任务执行稳定性提升；采购流程优化；共享 Bot 机制更新 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.34.0 | PR 链接卡片展示实时状态（Open/Draft/Merged/Closed）；Bot 可在指定侧栏分组下创建子 Bot | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.33.0 | 企业版支持组级别权限分配；管理后台支持一键开通团队试用；采购审批卡支持 Link 钱包绑卡一键支付 | Enterprise | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.32.0 | 国际化输入法兼容性修复；团队初始化设置流程优化 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.31.0 | 问答式上手引导推荐匹配 Bot；后台上线 Setup Checklist；HTML 生成文件提供实时代码预览；Cloud Agent 独立窗口 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.30.0 | 推出 Bot 模板公开与团队分享链接；采购审批卡对接 Link 快捷支付；新增阿拉伯语与希伯来语等 RTL 布局 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.29.0 | 设置页新增 Computers 机器列表管理并配置权限档位；移动端通知支持直接呈现 Bot 回复内容 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.28.0 | 新增俄语、土耳其语、意大利语和瑞典语支持，自动跟随系统语言 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.27.0 | Cursor Pro 订阅者正式开放使用；支持绑定个人 SuperGrok 及 X Premium+ 账户获取用量；Webhook 数据流增强 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.26.0 | 应用菜单增加“Check for Updates”与“Restart to Update”；从右到左排版修复 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.25.0 | 多选问答卡片；个人方案支持将月度按需限额设为 None、Fixed 或 Unlimited；GitHub Routine 支持单 PR 监听 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.24.0 | 设置项与插件支持右键复制直达链接；视频附件右键保存；多团队登录租户选择 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.22.0 | 团队初始化引导增强；多语言界面翻译校对与错位修复 | 全员 / Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.21.0 | 语言包支持简体中文、繁体中文、日文、韩文等；输入框 Emoji 选择；Routine 支持 Webhook URL 与密钥触发 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.20.0 | 全局快捷键 `Cmd/Ctrl+D` 语音听写输入；插件默认账号支持重命名编辑 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.19.0 | 设置新增 Manage Plan 方案升级通道；包含额度用尽时支持升级 Ultra 或绑定 SuperGrok Heavy；GPU 硬件加速 | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.18.0 | Usage & Billing 页面新增 Cancel Trial 提前取消试用按钮（取消将清空剩余试用额度） | 全员 | [x.ai: Changelog](https://x.ai/changelog/bot)  |
| v0.17.0 | 自助团队版 Standard 成员支持通过关联个人 SuperGrok Heavy 订阅使用 Grok Bot；丰富 Routine 触发器 | Teams | [x.ai: Changelog](https://x.ai/changelog/bot)  |


# 附录 F–J · FAQ、术语、竞品、资源、来源总表与勘误

## 附录 F FAQ（中文高频 20 问） · Frequently Asked Questions

### F.1 国内没有外币信用卡怎么开通 · Payment Without Foreign Card
很多人以为必须绑定海外信用卡。假设你查阅 Cursor 官方计划页，上面明确写着所有付费个人计划都包含 Grok Bot(https://cursor.com/cn/help/grok-bot/plans)。多位社区用户实测过，关掉代理，用浏览器无痕模式打开 Cursor 官网选 Pro 月付，把计费国家和币种切到 CNY，结账面板就会出现**支付宝付款**选项(https://x.com/i/status/2109157438226403420)。首次没刷出来的话，在结算页把美元和人民币来回切几次，或者在 App 内订阅时选不使用 Link 支付(https://www.amz123.com/t/lZiL8LFi)。国内无痕环境下支付宝人民币扣费与账号额度实时到账。自 2026 年 10 月上线 [The X Subscription](https://cursor.com/help/the-x-subscription/overview) 三合一订阅后，已持有旧版 Cursor Pro 的用户仍可保留原有支付宝订阅通道，也可在 [Grok Bot 档位页](https://cursor.com/help/grok-bot/plans) 管理升级。

### F.2 手机号验证收不到验证码怎么办 · Phone Verification
假设你翻阅社区帖子会发现，登录 Grok Bot 桌面端时常有强制绑定手机号的拦截，用大陆号码或接码平台容易报错(https://www.v2ex.com/t/1241829)。LINUX DO 上有用户反馈，把网络出口切到美国干净节点后，直接输 **+86 手机号**能顺利收到短信验证码进控制台(https://linux.do/t/topic/2743888)。也有用户反馈用 Google Voice 虚拟号能注册(https://www.v2ex.com/t/1241829)。要是提示号码验证次数过多，换个浏览器会话等冷却就行。此外，官方在 v0.71.2 更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）中进一步简化了客户端登录与账号关联流程，降低了初次鉴权的摩擦。

### F.3 境内网络直连官网与文档是否可用 · Network Access
很多人以为必须全局代理才能访问。国内评测文章实测指出，x.ai/bot 产品官网和 cursor.com/docs/grok-bot 官方文档在部分国内网络下可以直接直连(https://www.ai345.info/ai-guide/grok-bot-china-guide)。但客户端鉴权和远程云电脑连接对**网络稳定性**要求高，不同地区和运营商表现不一样(https://www.ai345.info/ai-guide/grok-bot-china-guide)。要是桌面端白屏或登录中断，先排查本地网络和代理路由规则。同时请注意，旧版技术文档域名已全面下线，官方所有技术架构与实操指南均已统一迁移至 [https://cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot) 与 [https://cursor.com/help/grok-bot](https://cursor.com/help/grok-bot)。若云电脑访问外部站点遭遇数据中心 IP 封锁或频繁验证码拦截，可参考 `@XueshiQiao`（[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)）验证的方案，在桌面端开启 `Settings > Computer > Your computer > Route traffic through this computer` 借用本机住宅 IP 转发流量（v0.75.5 已修复本地流量转发稳定性，详见 [https://x.ai/changelog/bot](https://x.ai/changelog/bot)）。

### F.4 哪些订阅档位可以使用 Grok Bot · Eligible Plans
网上套餐很多，官方文档写得很清楚：Cursor 所有个人付费计划和 Teams 计划都内置 Grok Bot(https://cursor.com/cn/help/grok-bot/plans)。要是你有 X 或 xAI 账号，关联 SuperGrok、SuperGrok Plus、Heavy 或者 X Premium+ 也能拿到额度，但 **SuperGrok Lite 档位不可用**(https://cursor.com/cn/help/grok-bot/plans)。两边的用量额度各自独立计算，不叠加，关联后也不能转移给其他 Cursor 账号(https://cursor.com/cn/help/grok-bot/plans)。自 2026 年 10 月起，官方正式推出三合一的 **The X Subscription**（`@bot` 公告：[https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)；官方总览：[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)），其中 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 档位直接打包包含 Grok、Cursor 与 X Premium 并天然共享同一个周额度池，而 **Free（$0）** 与 **Plus（$8/月）** 档位不包含 Grok Bot 权限（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。

### F.5 本地关机后任务还会继续执行吗 · Cloud VM Model
别把它当成跑在本地的桌面软件，它的核心是数据中心里的一台持久云电脑(https://cursor.com/docs/grok-bot)。它有独立的文件系统、终端和无头浏览器。你在本地合上电脑甚至关机，只要云端任务和定时任务还在队列里，后台就会**持续无人值守运行**(https://cursor.com/docs/grok-bot)。重新开机或者在手机 App 上登录，直接看交付文件和日志就行。如果你希望把家里常开的 Mac mini 变成云端 Bot 随时可调度的远程计算节点，还可以参考官方产品工程负责人 `@ericzakariasson`（[https://x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099) 与 [https://x.com/ericzakariasson/status/2114157733276525044](https://x.com/ericzakariasson/status/2114157733276525044)）分享的做法：在家用 Mac mini 上启动并登录 Grok Bot 桌面端，使其自动注册到 `Settings > Computer` 列表中，甚至让 Bot 自动在远程机器上配置并启动 `cursor-agent worker`。

### F.6 云电脑的真实硬件配置是多少 · Computer Specs
官方文档没有公开披露具体 CPU 型号和内存，官方未公布具体规格数字(https://cursor.com/docs/grok-bot)。社区帖称通过探针与系统命令测得为 8 核 CPU、16GB 内存、约 128GB 磁盘（个例）(https://www.v2ex.com/t/1235049)。这是多租户容器，默认没给公网独立 IP，磁盘主要用于常规办公和编译，不能拿来当**高性能持久 VPS**使。不过，这台云电脑足以胜任复杂的音视频合成与 3D 渲染工作——例如官方设计师 `@pengzheng_`（[https://x.com/pengzheng_/status/2113786630033322239](https://x.com/pengzheng_/status/2113786630033322239)）直接在云电脑里用 Python 脚本驱动 Blender 根据 1908 年专利图纸渲染出了 3D 外卖盒折痕铰链动画，而 `@lyuan1618`（[https://x.com/lyuan1618/status/2114214704008798674](https://x.com/lyuan1618/status/2114214704008798674)）则在云电脑内配置 Tailscale 将其与家庭 NAS 组建成私有局域网 Mesh。

### F.7 同账号下的多个 Bot 彼此隔离吗 · Shared VM Security
这是新手最容易踩的安全坑。官方文档写得很明确，同一个账号下的所有 Bot 共享同一台云电脑，包括文件、终端和浏览器登录态(https://cursor.com/help/grok-bot/computer-and-apps)。每个 Bot 有自己的工作屏幕，但**屏幕绝不是安全边界**(https://cursor.com/help/grok-bot/computer-and-apps)。你在 Bot A 登录了网站，Bot B 也能拿到 Cookie 去操作，Bot 之间没有权限沙箱隔离。根据官方企业安全文档（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)），管理员可通过配置云电脑出站域名白名单（如 `*.domain.com:443`）并勾选 `Apply to MCP servers` 来收紧网络访问边界。

### F.8 可以在云电脑里登录网银和核心主邮箱吗 · Sensitive Logins
千万别在云电脑里输入网银账号、主力邮箱或公司财务凭据。所有 Bot 共享浏览器会话，一旦哪个 Bot 碰到提示词注入或逻辑跑偏，就能顺着登录态乱动。社区就有真实事故，一位用户的财务 Bot 处理报表时，把包含敏感账户审计的数据误发进了公司 Slack 公开频道(https://cybernews.com/ai-news/grok-bot-leaks-bank-information/)。涉及资金和核心资产，必须守住**草稿优先原则**。针对必须登录的第三方业务站点（如 `@oxpsats` 在 [https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670) 中让 Bot 登录 Bloomberg 研读付费墙文章），官方现已推出 **1Password Brokered Sign-in**（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）与内置 **Grok Bot Vault**（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)），通过 `BrowserSecureFill` 注入凭据，使 Bot 全程无法在上下文或聊天记录中看到明文密码。

### F.9 微信如何接入以及是否存在封号风险 · WeChat Integration
国内用得最多的是微信接入。目前社区主流方案是用微信官方 ClawBot 或 iLink 插件，配合 Webhook Routine 搭桥(https://x.com/KinGao476942/status/2108171436213104836)。微信客户端要求 iOS ≥8.0.70 或 Android ≥8.0.69，登录二维码大概 5 分钟有效，要是报错 -14 说明凭证过期，重新扫码就行(https://xput.app/N4rlhi)。虽然社区帖称走官方接口不会封号，但腾讯官方可没给过免责背书。有用户自述同一个微信号千万别混用其他第三方 Hook 工具，必须留好**人工应急接管机制**(https://ele.ac.cn/2171/)。

### F.10 飞书如何接入以及有哪些调用频率限制 · Feishu Integration
Grok Bot 插件市场目前还没有官方飞书插件，国内主要是给飞书自定义机器人配 Webhook 来推消息(https://www.aitoolku.cn/tutorials/grok-feishu)。云电脑跑出结果后，调用 Webhook 往飞书群推富文本。aitoolku 教程提到，飞书自定义机器人在高频发送时有**约 20 条/分钟的频控限制**(https://www.aitoolku.cn/tutorials/grok-feishu)。要是你的 Routine 短时间内会打大量日志，记得先合并做摘要，再推到群里。在研发协同场景中，还可以参考 `@realbenzh`（[https://x.com/realbenzh/status/2111295936635015631](https://x.com/realbenzh/status/2111295936635015631)）的实践，将飞书、Linear、电子邮箱与团队文档统一接入 Grok Bot 汇总完整业务上下文，对齐验收标准后再通过 CLI 驱动构建交付。

### F.11 国内主流平台没有插件该如何处理数据 · Domestic Platforms Workaround
小红书、微信公众号、抖音在市场里都没有官方连接器。社区跑通的做法有四种：一是把公众号或小红书的公开链接发给 Bot 提取图文样式；二是人工从后台导出 CSV 报表或截图放进工作目录；三是在云电脑自带浏览器里扫码登录创作者后台，让 Bot 定点抓看板；四是让 Bot 产出文章和排版脚本，最后由**人工点击最终发布**(https://xiangyugongzuoliu.com/grokbot-use-cases/)。例如 `@bitman2140`（[https://x.com/bitman2140/status/2114210291546493153](https://x.com/bitman2140/status/2114210291546493153)）与 `@CyberAlice3269`（[https://x.com/CyberAlice3269/status/2112098767151468645](https://x.com/CyberAlice3269/status/2112098767151468645)）均通过多 Bot 流水线结合共享知识库 SOP，稳定跑通了微信公众号日更与多平台自媒体矩阵运营。

### F.12 复制中文回复出现乱码该怎么解决 · Chinese Character Encoding Bug
很多开发者反馈，在特定客户端版本里复制 Bot 输出的中文，粘出来全是乱码(https://www.v2ex.com/t/1247756)。在 v1.14.0 桌面端上这问题被集中录屏反馈过，是剪贴板字符编码转换的毛病，英文复制粘贴就没事(https://www.v2ex.com/t/1247756)。碰上乱码，临时办法是让 Bot 把最终文本直接存成**工作目录中的文本文件**，再去下载或打开文件复制，或者直接让 Bot 调用 v0.75.2 新增的 **Pages（Canvas）** 功能（[https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)）将排版好的长文或报表生成为在线可分享的网页卡片。

### F.13 Grok Bot 到底运行什么模型且能否手动切换 · Model Routing
设置里根本没有切换模型的下拉菜单。2026 年 10 月 7 日马斯克在 X 上宣布 Grok Bot 将改用 Opus 5.5(https://x.com/elonmusk/status/2107724314451878104)，Grok Bot 团队成员 @poteto 在 X 回复中说"yes, bot itself will run on opus 5.5"(https://x.com/poteto/status/2107734770990133319)。截至 10 月 13 日官方没有发布正式公告或模型选择器，切换是逐步推送的；10 月 6 日的第三方评测仍写着它跑在 Grok 4.7 上(https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)。这也是为什么 `@Khazix0918`（[https://x.com/Khazix0918/status/2111709708226797737](https://x.com/Khazix0918/status/2111709708226797737)）与 `@object_nullll`（[https://x.com/object_nullll/status/2111717423837778173](https://x.com/object_nullll/status/2111717423837778173)）在讨论中强调：不要把默认对话路由层直接当成 zero-shot 重度苦力裸用，而应让对话层负责对齐验收标准，再将重活委派给 Cursor Cloud Agents 或云电脑上的 CLI Workers（甚至像 `@kaelanyiu` 在 [https://x.com/kaelanyiu/status/2114213605566742884](https://x.com/kaelanyiu/status/2114213605566742884) 中那样设立一个定时跑分的“评测官 Meta-Evaluator Bot”动态调整 Worker CLI 调用的底层模型）。

### F.14 什么是 Skill 和 Routine 且二者有何区别 · Skills vs Routines
官方文档把两者的分工说得很清楚：Skill 是做某项特定任务的操作规程，相当于 SOP；Routine 则是具体的 Bot 在特定时间或事件触发下跑任务的排期计划(https://cursor.com/help/grok-bot/skills-routines-and-automations)。官方的 Teach a task 允许录制最长 10 分钟无声屏幕演示，但录出来的只是**草稿 Skill**(https://cursor.com/docs/grok-bot/work)。必须在草稿里补上异常处理和审批断点，测试通过后再放进 Routine 跑（详见官方 Routine 指南 [https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）。此外，正如 `@eze_is_1`（[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151)）在实战中所总结的，当你允许 Bot 在复盘中自动迭代修改自己的 Skill 时，必须定期对 Skill 文件做精简合并与冲突清理，防止 Skill 自我膨胀臃肿。

### F.15 账户下可以创建多少个 Bot 和 Routine · Hard Limits
系统有明确的硬指标。官方设计说明曾写每个账号大约 50 个 Bot，但 9 月 1 日 v0.31.0 已取消这个上限(https://x.ai/changelog/bot)。多 Bot 群聊里，每个群容纳 2 到 6 个 Bot(https://cursor.com/help/grok-bot/chat-and-collaboration)。自动化方面，每个 Bot 最多配 50 条 Routine，最小定时运行间隔不低于 5 分钟，系统只留最近 20 次的日志历史，而且**删除 Routine 无法撤销**(https://cursor.com/help/grok-bot/skills-routines-and-automations)。在 2026 年 10 月 22 日发布的 v0.75.2 版本（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）与最新官方 Routine 文档（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）中，官方将小时级运行频率配额大幅上调至**全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots）**，以及**单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**。

### F.16 审批卡机制是如何工作的 · Approvals Mechanism
Bot 准备执行敏感或产生外部影响的操作时，系统会暂停任务并弹出审批卡等人工确认。官方文档规定，要审批的操作包括资金支付、对外发邮件或消息、在外部平台公开发布内容以及删文件等(https://cursor.com/help/grok-bot/approvals-security-and-privacy)。后台跑自动化触发审批时，卡片如果**大约 10 分钟内未被确认**就会自动过期(https://cursor.com/help/grok-bot/approvals-security-and-privacy)。关键审批一定要接好通知渠道，省得任务被超时中断。在 v0.75.2（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）中，官方精简了冗余的 Auto-review 弹窗，对于用户在当前对话轮次中已明确下令执行的操作不再重复弹出二次确认卡；同时，企业与团队管理员现可在安全设置（[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）中用自然语言编写自定义 Auto-Review 规则，并将策略设为 `Block`（直接阻断）或 `Require approval`（要求审批）。

### F.17 云电脑如果重置或回滚会不会丢失数据 · Computer Reset & Data
官方提供了恢复、更新和重置三种维护操作。官方文档说明，重置云电脑后，持久化到工作磁盘以及 `/workspace` 目录下的个人文件会保留，但在终端里自行安装的系统依赖、全局软件包和临时服务可能会丢(https://cursor.com/cn/docs/grok-bot)。社区此前反映过，后台由于错误分配了重复实例，导致部分用户的会话和 Bot 被错误路由并产生**历史状态回滚事故**(https://www.v2ex.com/t/1241225)。重要配置最好在外部做好备份，具体恢复与重置流程可参阅官方云电脑恢复指南 [https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)。

### F.18 为什么额度消耗过快以及如何有效省额度 · Quota Burners & Saving
额度几小时跑光，通常是陷入了高频空转。比如高频定时反复抓没变动的网页、让 Bot 不断截屏重试，或者在多 Bot 群聊里没加约束引发互相唤醒与死循环(https://linux.do/t/topic/2807876)。省额度的核心是调度与执行分离：让 Bot 做统筹调度，脏活累活丢给云电脑轻量脚本或本地子代理跑，只在数据变动时才用 Webhook 唤醒 Bot，还要记得**关闭非必要的按需计费开关**(https://readcopilot.ionichina.com/articles/53772)。结合 2026 年 10 月中下旬的社区实战，还有五招立竿见影的省额度绝技：
1. **排查三合一池共享抽水与冗余 Routine**：如 `@charlie_pmp`（[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）所指出，升级到 The X Subscription 后，Grok Bot、Grok 与 Cursor 三端共享同一个周额度池，务必清理高频且未经精简的后台 Routine。
2. **“AI 写确定性脚本，脚本跑日常轮询”**：参考 `@StarkLJM`（[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377) 与 [https://x.com/starkljm/status/2112818533797343312](https://x.com/starkljm/status/2112818533797343312)）的范式，用 28.6 秒让 AI 写好带字段缺失告警与 `null` 值保护的确定性 Python 爬虫脚本，此后每天定时跑脚本仅耗时 1.99 秒，日常消耗 **0 模型额度**。
3. **利用 `+alias` 邮箱后缀精准触发 Routine**：按照官方工程师 `@SamSokolin`（[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)）与 [Agent Email 文档](https://cursor.com/help/grok-bot/agent-email) 的说明，配置仅当邮件发往特定 `+alias` 子别名（如 `mybot+invoices@mail.grokbot.com`）时才触发对应 Routine，杜绝垃圾邮件误触发。
4. **云电脑挂载 `pi` + DeepSeek API 或完成时 Webhook**：如 `@hppzyy`（[https://x.com/hppzyy/status/2111573227881529454](https://x.com/hppzyy/status/2111573227881529454)）所示，在云电脑里安装轻量级 Pi Agent（`pi`）配合廉价的 DeepSeek API Key 干苦力活；注意在非交互式 Shell 中调用 `pi -p "..."` 时，务必像 `@37FlowAI`（[https://x.com/37FlowAI/status/2111334386339823687](https://x.com/37FlowAI/status/2111334386339823687)）实测的那样在命令末尾追加 `< /dev/null` 闭合标准输入，防止进程等待 EOF 无限期卡死。或者像 `@AbhisheKumarA7`（[https://x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578)）那样在云电脑内跑 Codex CLI 并用完成时 Webhook 唤醒 Bot，实现零轮询耗电。

### F.19 市面上的代充、账号租用和炒币宣传是否安全 · Gray Market & Scams
围绕 Grok Bot 已经有不少黑灰产骗局。一些代充宣称低价代开并索要浏览器 Session JSON 文件，该店称 Session JSON 不含登录令牌，但把账号信息交给第三方仍有风险(https://claudemax.shop/blog/grok-bot-guide-supergrok)。还有宣传跨低价区订阅套利的，直接面临封号风险(https://linux.do/t/topic/2848179)。社交平台上晒 Bot 自动炒币从小几十块翻到上万刀的截图，全都是**虚假营销与钓鱼套路**(https://x.com/i/status/2102291280965640690)。

### F.20 培养一个稳定干活的 Bot 需要经过哪些阶段 · Bot Training Stages
一上来就让 Bot 独立干复杂业务基本都会翻车。社区摸索出来的养 Bot 经验分三个阶段：第一阶段是前几次交互，Bot 完成度通常只有 30% 到 40%，必须人工逐项纠错并让它记牢规则(https://www.v2ex.com/t/1240012)。第二阶段多轮对齐后，完成度能到 70% 左右，格式和边界基本收敛(https://www.v2ex.com/t/1240012)。到了第三阶段排除掉边界异常，再把它**固化为 Routine 投入无人值守**。中文社区新手还可以结合 `@chuyang_ai`（[https://x.com/chuyang_ai/status/2111357749103911004](https://x.com/chuyang_ai/status/2111357749103911004)）的入门视频课程与 `@itgoyo`（[https://x.com/itgoyo/status/2111332049193996421](https://x.com/itgoyo/status/2111332049193996421)）总结的 90 秒 5 大上手技巧，循序渐进完成从单 Bot 调教到多 Bot 协同的过渡。

### F.21 The X Subscription（$30/$100/$200）和原来的 Cursor Pro（$20）有什么区别？合并后还能退回吗？App Store 订阅怎么处理？ · The X Subscription Unification & Refunds
根据官方发布的 [The X Subscription 总览](https://cursor.com/help/the-x-subscription/overview)、[Grok Bot 档位说明](https://cursor.com/help/grok-bot/plans) 以及 `@bot` 官方公告（[https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)），两套体系的核心区别与迁移红线如下：
1. **三合一共享周额度池 vs 旧版独立计划**：**The X Subscription** 将 **Grok**、**Cursor** 与 **X Premium** 整合为单一订阅，包含 Grok Bot 的档位为 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）**（Free $0 与 Plus $8/月不含 Grok Bot）。在该体系下，三大产品**共享同一个周额度池（one weekly usage pool）**，每周固定重置且不结转。
2. **预付充值（Prepaid Credits）vs 旧版后付费账单**：在 The X Subscription 下，当周额度耗尽或调用非 Grok 系列的第三方模型时，系统会从 **Prepaid Credits（预付额度）** 中扣费（需前往 `grok.com/dashboard/billing` 的 `Additional usage credits` 充值，支持开启 Auto Top-up 与月度封顶上限）。而旧版后付费按需计费（On-demand monthly limit）仅适用于未迁移的旧版独立 Cursor 计划。
3. **单向切换不可逆**：既有 Cursor Pro（$20/月）、Pro+（$60/月）、Ultra（$200/月）及自助 Teams（$40/人/月）订户只要不主动切换，可一直保留旧版计划；一旦通过 `cursor.com/unify` 或 `accounts.x.ai/unify` 合并升级至 The X Subscription，**将无法退回旧版独立订阅计划**（[https://cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）。
4. **App Store / Google Play 双扣费预警**：合并升级时，网页端直接扣款的旧计划会自动取消并按剩余天数比例退款（prorated refunds）；但通过 **Apple App Store 或 Google Play** 订阅的渠道账单无法被官方自动取消或退款，你必须亲自前往 Apple ID 或 Google Play 订阅管理页手动取消，否则会遭遇双份扣费（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）。

### F.22 把银行卡存在 Grok Bot Vault 里和存在 1Password 里有什么区别？为什么说存进 Vault 的卡结账时不会单独弹 Vault 确认框？ · Grok Bot Vault vs 1Password & Checkout Approval Boundary
这是 2026 年 10 月 22–23 日上线 **1Password Brokered Sign-in**（[https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874)、`@1Password` 公告 [https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)）与 **Grok Bot Vault**（[https://x.com/bot/status/2113754107861532677](https://x.com/bot/status/2113754107861532677)）后最核心的安全边界问题：
1. **调用优先级与定位差异**：根据官方 [Work 技术文档](https://cursor.com/docs/grok-bot/work)，Bot 在**登录网站（Sign-in）**时的调用顺序为：`云电脑已存浏览器会话 → Vault → 1Password → 聊天内 Secure Form → 人工接管屏幕`；而在**结账支付（Checkout）**时的调用顺序为：`Vault → 聊天内 Secure Form → Link / X Money → 人工接管屏幕`。1Password Brokered Sign-in（要求桌面/移动端 1Password app ≥ 8.12.42，默认读取 Personal/Private 库，详见 [https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）会在每次登录时弹出 **Review in 1Password** 让你通过生物识别逐次批准；而内置 Vault（`Settings → Vault`）则把登录凭据（含 TOTP）、银行卡（支持手机摄像头 Scan 扫卡）和收货地址存储在只写（write-only）加密区，由 `BrowserSecureFill` 注入，且支持填写明文 **Hint** 供 Bot 识别用途（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）。
2. **存卡结账无单独 Vault 弹窗的关键红线**：正如官方 [Secrets & Vault 文档](https://cursor.com/help/grok-bot/secrets) 所明确规定，以及社区安全研究者 `@kial`（[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)）与 `@JianWeiSignal`（[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488) 及 [https://x.com/JianWeiSignal/status/2114195638988501103](https://x.com/JianWeiSignal/status/2114195638988501103)）第一时间发出的预警——**一旦你将银行卡保存在 Grok Bot Vault 中，Bot 在结账填充该卡时不会触发单独的逐笔 Vault 弹窗确认（filled at checkout without a separate per-charge Vault prompt）**，仅受通用购买审批规则约束。尽管 `@elonmusk`（[https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445)）公开承诺若 Grok Bot 代购出错或泄露卡号将由 SpaceX 全额赔付，但如果你希望每一笔消费都必须亲手输入卡号把关，**请勿将主力信用卡常驻保存在 Vault 中**（应从 Vault 移除，改在每次结账弹出聊天内 Secure Form 时单次输入且不勾选保存）。你也可以参考 `@martinpaulweiss`（[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)）的“一密一宅（One home per secret）”法则拆分管理凭据，或使用 `@LisaMAUSA`（[https://x.com/LisaMAUSA/status/2114208018388643852](https://x.com/LisaMAUSA/status/2114208018388643852)）分享的 `Vault Tidy` 模板定期清理去重。

### F.23 怎么用 iPhone 侧边 Action Button 一键跟指定的 Grok Bot 语音通话？ · iPhone Action Button Live Voice Chat
根据官方 [语音通话指南](https://cursor.com/help/grok-bot/voice-chat)、[移动端指南](https://cursor.com/help/grok-bot/mobile) 以及 `@bot` 官方发布帖（[https://x.com/bot/status/2112246033178968161](https://x.com/bot/status/2112246033178968161)），在配备 Action Button 的 **iPhone 15 Pro 及后续机型**上，只需将 Grok Bot iOS App 更新至 **v1.16 或更高版本**并至少打开过一次，即可按以下三种方式配置：
1. **直接呼叫默认主 Bot（Primary Bot）**：进入 iPhone 系统 `Settings → Action Button → Shortcut → Choose a Shortcut → Grok Bot → Start Voice Chat`，长按侧键即可盲呼主 Bot（实机演示参见 `@SawyerMerritt`：[https://x.com/SawyerMerritt/status/2112252980015579431](https://x.com/SawyerMerritt/status/2112252980015579431)）。
2. **呼叫指定专职 Bot 或每次弹窗选择**：打开 iOS **Shortcuts（快捷指令）** App，新建快捷指令并添加 Grok Bot 的 `Start Voice Chat with Bot` 动作，将目标设为某位固定专职 Bot 或 `Ask Each Time`（每次询问），再将该快捷指令绑定到 Action Button 或通过 `"Hey Siri"` 唤醒。
3. **URL Scheme 直达方案**：在快捷指令中通过 `Open URLs` 打开 `grokbot://app/v1/agent?id=YOUR_BOT_ID`。
通话挂断瞬间，聊天流会自动生成带完整逐字稿的 **Voice chat card** 并立即跟进执行。社区中，`@JCOMBuilds`（[https://x.com/JCOMBuilds/status/2112997408510452123](https://x.com/JCOMBuilds/status/2112997408510452123)）用它每天早晨一键语音唤醒助理 Bot `"Eve"` 调取 1Password 为妻子点星巴克；`@TyeInBloom`（[https://x.com/TyeInBloom/status/2113767679588770271](https://x.com/TyeInBloom/status/2113767679588770271)）将其与 v0.75.2 新增的 iOS 原生日历/提醒事项/通讯录权限打通；`@D__cup`（[https://x.com/D__cup/status/2114211130365358350](https://x.com/D__cup/status/2114211130365358350)）佩戴 Shokz 韶音骨传导耳机配合 Action Button 打造全天候免提外脑；而 `@guoxudong_`（[https://x.com/guoxudong_/status/2111767457560215771](https://x.com/guoxudong_/status/2111767457560215771)）更进一步用 ESP32 硬件语音盒子经 Cloudflare Tunnel 跑通了桌面语音交互闭环。

### F.24 本地的 Claude Code 和 Codex 怎么跟云端 Grok Bot 互相派活？ · BDK & Local-Cloud Hybrid Dispatch
通过官方 **BDK（Bot Developer Kit）** 与 `cursor-grokbot-agents` 技能桥接，本地终端里的 **Claude Code**、**Codex**、**Cursor IDE** 可以与云端 **Grok Bot** 实现双向互调（社区总结参见 `@AIShovelLab`：[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）：
1. **本地 CLI 向云端 Grok Bot 派发多媒体渲染与 X 检索任务**：`@StarkLJM`（[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411)）实测在本地 Claude Code 中通过 BDK 向云端 Grok Bot 派发“制作 20 秒《上下五千年》中国历史线条画动画”，云端沙箱渲染完成后直接向本地返回 `0:20` MP4 视频与 `2.7 MB` 源码包；`@kangxiaile`（[https://x.com/kangxiaile/status/2109752183889744216](https://x.com/kangxiaile/status/2109752183889744216)）则让本地 Claude Code 把实时 X 舆情与新库检索全部外包给享有免费公开 X 读取额度的云端 Grok Bot。该跨端工作流同样在 `@charlychoi`（[https://x.com/charlychoi/status/2111425470201995309](https://x.com/charlychoi/status/2111425470201995309)）、`@pomufgd`（[https://x.com/pomufgd/status/2110799518283497488](https://x.com/pomufgd/status/2110799518283497488)）与 `@SyrianVeterans`（[https://x.com/SyrianVeterans/status/2110661026538737879](https://x.com/SyrianVeterans/status/2110661026538737879)）中得到验证。
2. **双向互调与共享 Obsidian 知识库**：`@z_lumia`（[https://x.com/z_lumia/status/2113800469571313974](https://x.com/z_lumia/status/2113800469571313974)）跑通了本地 Claude Code/Codex 调取云端 Grok Bot 长期记忆、同时云端 Grok Bot 反向操控本地台式机 CLI 的双向闭环；`@frogchan9o1`（[https://x.com/frogchan9o1/status/2110883156891140416](https://x.com/frogchan9o1/status/2110883156891140416)）与 `@itsvlady`（[https://x.com/itsvlady/status/2110803638671020277](https://x.com/itsvlady/status/2110803638671020277)）则展示了让 Claude Code 与 Grok Bot 共用同一个 Obsidian Vault 目录沉淀所有笔记与日志。
3. **绕过 Webhook HTTP 400 报错的轻量级脚本方案**：当通过外部 Webhook 向 Grok Bot 推送复杂 JSON 触发 HTTP 400 校验错误时，可采用 `@mikan77_aoi`（[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）编写的零依赖 Python 标准库脚本，仅用 4 次 API 调用即可稳定完成本地 Claude Code 到云端 Grok Bot 的任务交接。

### F.25 怎么让多个 Bot 的进度一目了然，并用 Grok Bot 管理加密 X 私信（X Chat）与生成视频？ · Pages Dashboard, X Chat & Grok Imagine Video
在 v0.71.2 至 v0.75.5 版本周期内，这三项高阶能力已成为重度用户的标配：
1. **用 Pages（Canvas）搭建多 Bot 实时作战看板**：当专职 Bot 数量增加（如 `@milesdeutscher` 在 [https://x.com/milesdeutscher/status/2113653680834859262](https://x.com/milesdeutscher/status/2113653680834859262) 及子帖 [https://x.com/milesdeutscher/status/2113653818651189419](https://x.com/milesdeutscher/status/2113653818651189419) 中展示的 10+ Bot 蜂群），逐个点开聊天窗极易混乱。你可以参考 `@melvindvivas`（[https://x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882)、提示词帖 [https://x.com/melvindvivas/status/2113676938820895045](https://x.com/melvindvivas/status/2113676938820895045)、Routine 刷新帖 [https://x.com/melvindvivas/status/2113968491573514576](https://x.com/melvindvivas/status/2113968491573514576)，获 `@JayKurtz90` 于 [https://x.com/JayKurtz90/status/2113983882018119823](https://x.com/JayKurtz90/status/2113983882018119823) 盛赞）的做法，让幕僚长 Bot 利用 **Pages**（[https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)）创建包含时间线、进行中、已完成与待审批四栏视图的 `Activity Dashboard`，沉淀在右侧 `Bot info pane → Library` 中并按三级权限（`Only you` / `Your team` / `Anyone with the link`）分享。
2. **托管端到端加密的 X Chat 私信与陌生人请求**：如官方工程师 `@pjvann`（[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)）所宣布，Grok Bot 现可通过内置 X 插件克隆官方解密辅助库 [https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper)，配合你的 **4 位数字 X Chat PIN 码**与 Juicebox 密钥恢复机制，在云电脑本地解密 `xchat_lite` 私信、自动审查批准高质量陌生人消息请求（message requests），甚至管理预约通话（`schedule_call`）与直播推流弹幕汇总。
3. **Grok Imagine 原生生视频 + 代码级动效渲染**：自 v0.71.2 起（`@bot` 公告：[https://x.com/bot/status/2110566041772617908](https://x.com/bot/status/2110566041772617908) 与 [https://x.com/bot/status/2110772748805194127](https://x.com/bot/status/2110772748805194127)），Bot 不仅能直接调用 `GenerateImage` / `GenerateVideo` 生成和编辑视频，还能在云电脑中用代码渲染 Motion Graphics 动效，或结合 `@LisaMAUSA`（[https://x.com/LisaMAUSA/status/2114208018388643852](https://x.com/LisaMAUSA/status/2114208018388643852)）的 `SceneEdit Video Studio` 模板只对 MP4 成片中的单镜头进行局部修补替换。

## 附录 G 术语表 · Glossary

### G.1 身份与环境 · Identity & Environment
先理清底层对象：**Bot 角色实例**拥有独立人格预设、系统指令、记忆和工作屏幕，账号内 Bot 数量自 v0.31.0 起不再限制在约 50 个(https://x.ai/changelog/bot)。持久云电脑（Cloud Computer）是远端的执行环境，所有 Bot 共享这一套机器、文件目录和浏览器会话(https://cursor.com/help/grok-bot/computer-and-apps)。社区实测该环境通常提供 8 核 16GB 内存及约 128GB 磁盘(https://www.v2ex.com/t/1235049)。工作目录（`/workspace`）是用来持久化个人项目和交付成果的挂载空间，云电脑重置后里面的文件依然保留(https://cursor.com/cn/docs/grok-bot)。

在此基础上，2026 年 10 月版本新增了四项关键的身份、计费与环境术语：
- **The X Subscription（三合一统一订阅）**：由官方于 2026 年 10 月推出的统一订阅体系（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview) 與 [https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)），将 **Grok**、**Cursor** 与 **X Premium** 整合进同一套餐。其中 **Premium（$30/月）**、**Super（$100/月）** 与 **Ultra（$200/月）** 档位包含 Grok Bot 权限并共享同一个每周固定重置的周额度池（one weekly usage pool）；一旦从旧版独立计划合并升级（`cursor.com/unify`），无法退回旧计划（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。
- **Prepaid Credits（预付额度）**：The X Subscription 体系下的超额与第三方模型计费机制（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)）。当共享周额度池耗尽，或在 Cursor 中调用非 Grok 系列的第三方模型时，费用直接从用户在 `grok.com/dashboard/billing` 充值的 Prepaid Credits 中扣除，支持配置 Auto Top-up（自动充值）与月度额外消费封顶上限（Monthly additional usage limit）。
- **Plus Alias（`+alias` 专属邮箱加号别名）**：每个 Bot 的 `@mail.grokbot.com` 专属邮箱自 v0.71.2 起支持的子别名机制（如 `mybot+newsletters@mail.grokbot.com`，详见 [https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email) 与 `@SamSokolin` 发布帖 [https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)）。可用于收发邮件（转发时完整保留原邮件 HTML、内嵌图片与附件），并支持配置仅针对特定 `+alias` 收件触发的 Routine（如 `@songsong275452` 在 [https://x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371) 中展示的周六 Newsletter 精华汇总工作流）。
- **Pages（Canvas 实时交互页面）**：v0.75.2 上线的动态画布与微型 Web 应用载体（底层由 `WriteCanvas` / `EditCanvas` / `ReadCanvas` / `ListCanvases` 驱动，详见 [https://x.ai/changelog/bot](https://x.ai/changelog/bot) 与 [https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)）。永久保存在对应 Bot 右侧信息栏的 `Library` 中，支持表格、图表、时间线与交互式组件持续热更新，并提供 `Only you`、`Your team`、`Anyone with the link` 三级分享权限。

### G.2 任务编排与自动化 · Tasks & Orchestration
技能（Skill）是可复用的操作规程，无论是写提示词还是录制最长 10 分钟的无声屏幕操作（Teach a task），录出来的东西在人工审核补全前都只是草稿(https://cursor.com/docs/grok-bot/work)。例程（Routine）则是把 Skill 和特定触发条件绑定的排期机制，支持定时或事件触发，每个 Bot 最多 50 条且最小间隔不低于 5 分钟(https://cursor.com/help/grok-bot/skills-routines-and-automations)。多个 Bot 组队时，通常设一个**总管角色（Chief of Staff）**负责收集需求、排优先级和分发任务(https://x.com/0xRafy/status/2099278275906265417)。为了防止多 Bot 群聊互相唤醒烧干额度，社区提倡安静交接（Quiet Handoff），也就是在指令里明确要求收到了不用回、没有新信息不发回复(https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705)。

围绕跨端协同、高频调度与 X 生态深水区，新增以下核心编排术语：
- **Routine Hourly Cap（300/200 小时级运行上限）**：自 v0.75.2 起大幅提升的自动化频率配额（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)），全账号所有 Bot 合计最高可运行 **300 次/小时**，单条 Routine 最高可运行 **200 次/小时**（典型应用包括 `@Butlergrokbot` 在 [https://x.com/Butlergrokbot/status/2111860108070445394](https://x.com/Butlergrokbot/status/2111860108070445394) 的家庭事务总管，以及 `@sisiliu517` 在 [https://x.com/sisiliu517/status/2110869965612183642](https://x.com/sisiliu517/status/2110869965612183642) 的 24 小时中美时差双语 X 运营流水线）。
- **BDK（Bot Developer Kit / `cursor-grokbot-agents`）**：打通本地终端编码 Agent（Claude Code、Codex、Cursor IDE）与云端 Grok Bot 双向任务派发与结果回收的开发套件与技能桥接层（实战案例参见 `@StarkLJM` [https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411) 与 `@z_lumia` [https://x.com/z_lumia/status/2113800469571313974](https://x.com/z_lumia/status/2113800469571313974)）。
- **X Chat（`xchat_lite` / Juicebox / X Chat PIN）**：Grok Bot 内置 X 插件对端到端加密 X 私信与陌生人消息请求（message requests）的原生存取架构（`@pjvann` 公告：[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)）。MCP 接口返回加密消息载荷与 **Juicebox** 密钥恢复配置，Bot 在云电脑本地克隆官方仓库 [https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper) 并运行 `xchat_tool.py`，配合用户的 **4 位数字 X Chat PIN** 完成沙箱本地解密与回复。

### G.3 安全边界与系统治理 · Safety & Governance
审批机制（Approvals / Auto-review）用来拦截涉及支付、发邮件发消息、外部平台发帖或删文件等敏感动作，后台生成的审批卡大约 10 分钟不处理就会自动作废(https://cursor.com/help/grok-bot/approvals-security-and-privacy)。连接器与市场（Connectors & Marketplace）允许通过 `@` 调外部扩展对接各类 SaaS 平台(https://x.ai/bot/marketplace)。后端路由（Model Routing）由系统按任务特征分配模型，官方已实装由 **Opus 5.5 驱动执行**(https://x.com/poteto/status/2107734770990133319，团队成员 X 帖)。团队机器人（Team Bots）支持接入 Slack 开展群聊或私聊协作(https://x.ai/news/team-bots)。按需用量开关（On-demand Usage）关掉后，能防止额度跑完自动扣信用卡(https://readcopilot.ionichina.com/articles/53772)。

在凭据保险箱、零知识代理授权与企业级合规审计维度，新增以下核心治理术语：
- **Grok Bot Vault（`BrowserSecureFill` / `Hint`）**：v0.75.5 正式上线的内置只写（write-only）加密保险箱（路径：`Settings → Vault`，详见 [https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)、官方发布帖 [https://x.com/bot/status/2113754107861532677](https://x.com/bot/status/2113754107861532677) 及设计师 `@pengzheng_` 展示帖 [https://x.com/pengzheng_/status/2113757876053536891](https://x.com/pengzheng_/status/2113757876053536891)）。支持存储 Logins（含 2FA/TOTP）、Cards（支持手机摄像头 Scan 扫卡）与 Contact info，支持导入最大 **5 MB** 的密码管理器 CSV。Bot 可读取明文 **Hint** 标签挑选条目，并通过 `BrowserSecureFill` 注入网页，永远看不到明文密码或完整卡号/CVV；**但需注意：保存在 Vault 中的银行卡在结账自动填充时不会触发单独的逐笔 Vault 弹窗确认**（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）。
- **1Password Brokered Sign-in（1Password 逐次代理授权登录）**：v0.75.2 联合 `"1Password for Agents"` 发布的免共享库登录机制（[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)、[https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874) 与 [https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)）。无需新建共享 Vault 或配置 Service Account 令牌，当 Bot 需要登录时弹出 **Review in 1Password**，用户在本地 1Password App（≥ 8.12.42）中通过生物识别逐次批准，即可将 Personal/Private 库中的凭据零知识注入浏览器。
- **Inference Hooks（推理钩子，Beta）与企业合规控制**：官方 [企业安全文档](https://cursor.com/docs/grok-bot/security) 提供的推理前/推理后（Pre/post-inference）合规审计拦截钩子。配合出站网络白名单的 `Apply to MCP servers` 强制开关、自然语言自定义 Auto-Review 策略（`Block` / `Require approval`）、OpenTelemetry `cursor.surface=grok_bot` 遥测过滤以及 **ISO/IEC 27001** 与 **ISO/IEC 42001** 国际安全认证，构建完整的企业级治理防线。

## 附录 H 竞品对照 · Competitive Landscape

### H.1 竞品横向参数全貌 · Landscape Matrix
现在的通用 Agent 不再只是文本对话框，都带上了沙箱或操作系统执行能力。主流 Agent 产品的关键维度对照如下，数据来自官方公开说明与第三方实测记录。根据 `@wenser2010`（[https://x.com/wenser2010/status/2113683422409572523](https://x.com/wenser2010/status/2113683422409572523) 与 [https://x.com/wenser2010/status/2113683427069489614](https://x.com/wenser2010/status/2113683427069489614)）在 2026 年 10 月 23 日发布的横向对比分析，Grok Bot 自 8 月发布以来仅用两个月便突破了 **80 万周付费用户（800K weekly paid users）**，并通过 **$30/月** 的 [The X Subscription](https://cursor.com/help/the-x-subscription/overview)（一次打包 X Premium、Cursor 与 Grok Bot）形成了对 **$100/月** 起步的 OpenAI Dots 以及受限于美区/Meta 账号准入墙的 Meta Muse 的显著差异化优势。

| 产品维度 | Grok Bot | Meta Muse | ChatGPT Dots | OpenClaw / Hermes |
|---|---|---|---|---|
| 发起机构与发布 | xAI（2026-08-11 早期内测） | Meta（2026-09-08 正式发布） | OpenAI（基于 ChatGPT Pro） | Nous Research 等开源社区 |
| 准入门槛与起步价 | Cursor Pro（$20/月）或 SuperGrok；The X Subscription（$30/月打包 X Premium 与 Cursor） | 免费起步（提供用量计数器，受美区与 Meta 账号墙限制） | 需 ChatGPT Pro（$100/月） | 开源免费（需自备算力或 API） |
| 架构形态 | 常驻持久云电脑（多 Bot 共享）+ Pages 实时画布 + Vault/1Password | Muse Secure VM（单 Agent） | 个人工作沙箱（单 Agent） | 本地或自托管 VPS（多 profile） |
| 多 Agent 协作 | 支持群聊协同、总管调度与 BDK 跨端联动 Claude Code / Codex | 单一助理形态（不支持群聊） | 单一助理形态（下发 Codex） | 支持本地多 profile 拉群协作 |
| 核心强项 | 复杂长流程、X 深度整合、多 Bot、300 次/小时高频 Routine、80 万周付费生态 | 个人生活、免费门槛、社媒连接 | 依托 OpenAI 模型、连本地工程 | 数据私密、无锁区、自由度极高 |
| 主要短板 | 额度消耗快、无法自选模型 | 缺乏深度工作流编排、国内受限 | 资费昂贵、无多 Bot 编排 | 搭建门槛高、需自行维护环境 |

![主流个人 Agent 架构形态演进与坐标分布](../images/fig-A2-1.png)

*图：主流个人 Agent 架构形态演进与坐标分布*

### H.2 Meta Muse：个人生活琐事的免费入口 · Meta Muse
Meta 在 2026 年 9 月 8 日推出了个人 AI 智能体 Muse(https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)。它最大的亮点是**完全免费起步**，进阶档有 20 美元的 Power 和 100 美元的 Maximum(https://openassistant.us/blog/muse-vs-grok-bot)。Muse 跑在专用的 Muse Secure VM 里，接了 WhatsApp、Instagram、健康和流媒体生态，还能通过 Link by Stripe 做线上预订和支付(https://openassistant.us/blog/muse-vs-grok-bot)。第三方实测指出，处理餐厅推荐、生活行程时它很顺手；但测到多步骤商业运营时失误不少，比如答应退款却没真扣、客服回复卡壳等(https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)。同时，正如 `@wenser2010`（[https://x.com/wenser2010/status/2113683427069489614](https://x.com/wenser2010/status/2113683427069489614)）所指出的，Meta Muse 虽然免费，但严格受限于美国地区及 Meta 账号准入墙（US/Meta account gated），对跨区域商业团队与开发者生态的开放度远不及 Grok Bot。

### H.3 ChatGPT Dots：OpenAI 的单体沙箱 · ChatGPT Dots
OpenAI 的 Dots 架构基于 GPT-6 Astra，必须每月至少 100 美元的 ChatGPT Pro 账号，200 美元和 500 美元档位主要是额度更多(https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)。它是单 Dot 模式，没法像 Grok Bot 那样拉一支分工明确的 Bot 团队。Dots 的优势是能配合 Codex Chrome 插件借用本地浏览器会话绕过反爬，还能把写代码的任务直接丢给本地目录下的 Codex(https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)。但第三方实测反映，在复杂业务测试里 Dots 的**推进速度偏慢**，做开放内容创作时容易偷工减料(https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)。在性价比维度上，对比 OpenAI Dots 高达 **$100/月** 的起步门槛，Grok Bot 依托 **$30/月** 的 [The X Subscription](https://cursor.com/help/the-x-subscription/overview)（同时包含 X Premium、SuperGrok 与 Cursor IDE，详见 `@wenser2010` 对比帖 [https://x.com/wenser2010/status/2113683422409572523](https://x.com/wenser2010/status/2113683422409572523)），并在 v0.71.2–v0.75.5 中补齐了本地住宅 IP 流量转发（`Route traffic through this computer`）、BDK 本地 CLI 双向派单、Pages 实时画布、1Password 逐次授权与 Vault 保险箱，在全栈工程与商业自动化上拉开了代差。

### H.4 OpenClaw 与 Hermes：开源自托管的自由度 · Open Source Agents
社区横评普遍认为，这一代商业 Agent 的沙箱和执行架构受了 OpenClaw 等早期开源项目的启发(https://x.com/i/status/2105442725919367611)。Nous Research 的 Hermes Agent 在本地实现了类似 Grok Bot 的多 profile 体系，每个 profile 有独立人格、记忆、工具和工作目录，也能拉进一个会话里协作(https://www.v2ex.com/t/1240012)。开源方案最大的好处是**数据完全不出门**，还能随意换各种大模型，但代价是得自己折腾环境、网络穿透和守护进程，没商业软件那么开箱即用(https://www.v2ex.com/t/1240012)。此外，许多初学用户容易混淆云端通用智能体 **Grok Bot** 与本地编码 CLI 工具 **Claude Code / Codex** 的定位——正如 `@eze_is_1`（[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151) 及系列跟帖 [https://x.com/eze_is_1/status/2109852993982206425](https://x.com/eze_is_1/status/2109852993982206425)、[https://x.com/eze_is_1/status/2110532874000879886](https://x.com/eze_is_1/status/2110532874000879886)、[https://x.com/eze_is_1/status/2110866224892850547](https://x.com/eze_is_1/status/2110866224892850547)）与 `@lanvjian`（[https://x.com/lanvjian/status/2111085984855011349](https://x.com/lanvjian/status/2111085984855011349)）所剖析的：Claude Code 与 Codex 专精于本地代码库的深度工程开发，而 Grok Bot 则是 7×24 小时在线的云端数字员工中枢、X 情报雷达与跨应用浏览器调度台，两者通过 BDK 桥接组合才能发挥最大威力。

### H.5 选型决策：工作选 Grok Bot，生活选 Muse · Decision Guide
选工具不用比参数，看是工作还是生活。综合实测与社区反馈，要是想搭自动化工作流、盯店铺订单、巡检竞品或者跑多步骤团队任务，Grok Bot 靠持久云电脑和多 Bot 协同是性价比更高的选择(https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)。要是平时订票、查攻略、问日常问题，免费的 Meta Muse 足够轻快。如果身处境内受限网络且对**数据隐私高度敏感**，在本地部署一套开源的 Hermes 更踏实。而对于追求极致生产力的开发者、创作者与一人公司而言，参考官方客服舰队（[https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)，以 5 位专职 Bot 在工单暴涨 175% 时实现零新增招聘、单票成本降至 $0.20–$0.30、99% 退款全自动闭环）与 `@milesdeutscher`（[https://x.com/milesdeutscher/status/2113653680834859262](https://x.com/milesdeutscher/status/2113653680834859262)）的 10 大工作流范式，采用“**$30/月 The X Subscription（云端 Grok Bot 舰队 + X Premium + Cursor） + 本地 Claude Code / Codex 协同**”的双栈架构，是 2026 年最具投入产出比的标准答案。

## 附录 I 资源导航 · Resources & Community

### I.1 官方站点与一手文档 · Official Documentation
查一手资料最靠谱。官方文档中心汇总了所有操作指南和 API 说明，边界参数全在里面(https://cursor.com/docs/grok-bot)。桌面端和移动端安装包统一在官网首页下载(https://x.ai/bot)。要是给具体岗位做 SOP，官方团队写的 **27 篇岗位实战指南库**覆盖了工程、销售、法务、招聘等场景(https://x.ai/bot/guides)。官方新闻中心能看企业版和团队功能的公告(https://x.ai/news)，X 上的官方账号会同步版本更新时间线(https://x.com/bot)。

2026 年 10 月中下旬起，官方已将全部文档统一整合至 `cursor.com` 旗下的两大权威文档中心，并开源了端到端加密私信辅助工具库：
- **技术与企业架构文档中心（Technical & Enterprise Docs）**：总览入口（[https://cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)）、工作流与登录/结账优先级规范（[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)）、团队协作与治理（[https://cursor.com/docs/grok-bot/teams](https://cursor.com/docs/grok-bot/teams)）、企业级安全与合规（含 ISO/IEC 27001 与 ISO/IEC 42001 认证、Inference Hooks 及 `Apply to MCP servers` 出站网络白名单，[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)）、全局设置参考（[https://cursor.com/docs/grok-bot/settings](https://cursor.com/docs/grok-bot/settings)）以及官方行业与岗位用例（[https://cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases)）。
- **帮助中心与用户实操指南（Help Center & User Guides）**：帮助中心首页（[https://cursor.com/help/grok-bot](https://cursor.com/help/grok-bot)）、订阅与价格方案（[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans)，中文版：[https://cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)）、The X Subscription 三合一统一订阅总览（[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)）、Vault 与凭据安全指南（[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)）、第三方应用与连接器（含 1Password Brokered Sign-in 与 X 插件，[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)）、Routine 定时与事件触发（[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)）、专属邮箱 Agent Email 与 `+alias` 加号别名（[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)）、实时语音通话与 iPhone Action Button 配置（[https://cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)）、群聊协作（[https://cursor.com/help/grok-bot/group-chats](https://cursor.com/help/grok-bot/group-chats)）、移动端指南（[https://cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)）、实操教程（[https://cursor.com/help/grok-bot/how-to](https://cursor.com/help/grok-bot/how-to)）、常见问题解答（[https://cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)）以及云电脑恢复与重置（[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)）。
- **官方更新日志、标杆案例与开源辅助仓库**：版本演进更新日志（覆盖 v0.71.2、v0.75.2、v0.75.5 等，[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）、官方 5-Bot 客服自动化舰队案例（应对工单暴涨 175%、实现 0 新增招聘与 99% 退款全自动闭环，[https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)），以及 X Chat 端到端加密私信（`xchat_lite` + Juicebox + 4 位 PIN 码）沙箱本地解密官方辅助仓库（[https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper)）。

### I.2 中文开发者社区 · Chinese Developer Communities
国内开发者在网络、支付和本土集成上攒了不少经验。V2EX 的 AI 节点上有一线工程师讨论云电脑网络、乱码和多 Bot 架构(https://www.v2ex.com/t/1240012)。LINUX DO 集中讨论底层模型路由、额度监控和订阅避坑(https://linux.do)。SpaceXAI 中文社区（原 Cursor 中文社区）在广深京杭和武汉等地办过多场线下技术交流，适合交流**实战提示词**(https://luma.com/kss59f4e)。掘金也有开发者写过企业落地复盘(https://juejin.cn)。

### I.3 社区先行著作与致谢 · Community Guides & Acknowledgments
写这本书时，我参考并吸收了中文社区早期探索者的成果，在这里真诚致谢。Kin 写的《Grok Bot 橙皮书》最早介绍了大脑倾倒与反向提问的心智模型(https://github.com/KinGao294/grok-bot-orange-book)。超级峰的《粉皮书》用 55 个教学单元拆解了从开箱到多场景落地的路径(https://chaojifeng.me/downloads/grok-bot-course.md)。黄叔的《蓝皮书 v0.1》为早期架构梳理搭了清晰框架(https://ai.lzw.me)。花叔的系列开源橙皮书则在**开源协作与体例规范**上树立了标杆(https://github.com/alchaincyf/claude-code-orange-book)。本书作者 Mr.鼓先生（X：`@StarkLJM`；微信：`StarkLJM`）也将本书开源仓库维护在 GitHub（[https://github.com/LJMStark/grok-bot-blackbook](https://github.com/LJMStark/grok-bot-blackbook)），欢迎读者提交 Issue 与 PR 共建。

### I.4 优质视频笔记与横评 · Video Notes & Benchmarks
想看直观操作流程，可以看视频实测。AI for Mortals 作者 Pat Simmons 针对 Grok Bot、Meta Muse 和 ChatGPT Dots 做过一场三项对照测试（其中一项是连续四小时经营一家虚构咖啡公司），结论是 Grok Bot 三项都胜出，但他也提醒用量消耗快、实际要上 $100 档(https://www.aiformortals.co/blog/grok-bot-vs-meta-muse-vs-chatgpt-dots)。旧金山 Grok Bot Galaxy 开发者大会的演讲记录，也公开了企业级团队 Bot 的规模化演进实况(https://x.com/joshkim/status/2100996896575861157)。

2026 年 10 月中下旬，中英文社区涌现出一批覆盖 v0.71.2–v0.75.5 新特性的视频教程与深度横评：
- **新手入门与 90 秒核心技巧视频**：`@chuyang_ai`（初阳AI）发布了《Grok Bot 新手视频课程第 1 期》，讲解 Grok Bot 与 Claude Code 的定位区别、$30/月 The X Subscription 选型与 Routine 入门（[https://x.com/chuyang_ai/status/2111357749103911004](https://x.com/chuyang_ai/status/2111357749103911004)）；`@itgoyo`（小田切让）用 90 秒视频浓缩了专职 Bot 划分、Routine 调度、连接器绑定、云电脑文件持久化与多 Bot + Skill 复用 5 条铁律（[https://x.com/itgoyo/status/2111332049193996421](https://x.com/itgoyo/status/2111332049193996421)）；`@SawyerMerritt` 则晒出了 iPhone 侧边 Action Button 一键呼出 Grok Bot 实时语音通话的实机录屏（[https://x.com/SawyerMerritt/status/2112252980015579431](https://x.com/SawyerMerritt/status/2112252980015579431)）。
- **80 万周付费用户与三大大厂 Agent 横评**：`@wenser2010`（Wenser）复盘了 Grok Bot 发布两个月突破 80 万周付费用户的里程碑，并横向对比了 Grok Bot（$30/月打包 X Premium 与 Cursor）、OpenAI Dots（$100/月 Pro 起步）与 Meta Muse（免费但受限于美区与 Meta 账号墙）的生态与定价差异（[https://x.com/wenser2010/status/2113683422409572523](https://x.com/wenser2010/status/2113683422409572523) 与 [https://x.com/wenser2010/status/2113683427069489614](https://x.com/wenser2010/status/2113683427069489614)）。
- **10 大逆天工作流与多 Bot 架构长文**：`@milesdeutscher`（Miles Deutscher）发布了附带完整演示视频与 Prompt 结构的“10 大逆天 Grok Bot 用例”长推（[https://x.com/milesdeutscher/status/2113653680834859262](https://x.com/milesdeutscher/status/2113653680834859262)）；`@eze_is_1`（一泽Eze）撰写了 10 条高含金量实战心得与多 Bot 防臃肿 Skill 自迭代指南（[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151)），并获 `@lanvjian`（蓝海）推荐为区分 Grok Bot 与 Codex 定位的新手必看对比图（[https://x.com/lanvjian/status/2111085984855011349](https://x.com/lanvjian/status/2111085984855011349)）。

## 附录 J 本书来源总表 · Source Index

这里按全书章节顺序，汇总整理了调研中引用的核心原始链接，方便回溯核对。

### J.1 Part 1 起步篇来源 · Chapters 01 to 04
- §01 Grok Bot 是什么：官方文档概览（https://cursor.com/docs/grok-bot ）、Livemint 援引彭博社周活报道（https://www.livemint.com/ai/elon-musk-s-grok-bot-hits-418-000-weekly-users-after-one-month-11790093107144.html ）、云电脑与应用文档（https://cursor.com/help/grok-bot/computer-and-apps ）、官方用例库（https://cursor.com/help/grok-bot/use-cases ）、产品发布公告（https://x.ai/news/introducing-grok-bot  ）。
- §02 怎么才能用上：Cursor 官方计划说明页（https://cursor.com/cn/help/grok-bot/plans ）、Cursor 官方定价页（https://cursor.com/pricing ）、YuzuCMZ 支付宝订阅实测（https://x.com/i/status/2109157438226403420 ）、David 订阅经验（https://x.com/i/status/2108488671699816806 ）、X 会员绑定说明（https://x.com/i/status/2108748981069394279 ）、代充骗局警示（https://x.com/i/status/2102291280965640690 ）、国内直连评测（https://www.ai345.info/ai-guide/grok-bot-china-guide ）、官方故障排查（https://cursor.com/help/grok-bot/troubleshooting ）。
- §03 十分钟安装与开箱：官方下载主页（https://x.ai/bot ）、身份与访问控制（https://cursor.com/docs/grok-bot/identity-and-access ）、对话与协作（https://cursor.com/help/grok-bot/chat-and-collaboration ）、设置与通知（https://cursor.com/help/grok-bot/settings-and-notifications ）、移动端文档（https://cursor.com/help/grok-bot/mobile ）。
- §04 你的第一个任务：快速上手指南（https://cursor.com/help/grok-bot/get-started ）、团队成员建议（https://x.com/poteto/status/2107830403549831186 ）、社区橙皮书（https://github.com/KinGao294/grok-bot-orange-book ）。

### J.2 Part 2 核心概念篇来源 · Chapters 05 to 08
- §05 Bot：给每个同事一份岗位说明书：Bot 官方文档（https://cursor.com/help/grok-bot/bots ）、设计 Grok Bot 官方专文（https://x.ai/news/designing-grok-bot ）、V2EX 养 Bot 心得（https://www.v2ex.com/t/1240012 ）、模板指南（https://x.ai/bot/guides/templates-for-grok-bot ）。
- §06 云电脑：它的工位：文件与交付物（https://cursor.com/help/grok-bot/files-and-results ）、云电脑共享架构（https://cursor.com/help/grok-bot/computer-and-apps ）、云电脑工作与恢复帮助（https://cursor.com/cn/docs/grok-bot ）、V2EX 云电脑实测与重置讨论（https://www.v2ex.com/t/1241225 ）、代理文档（https://cursor.com/docs/grok-bot/proxies ）、私有网络（https://cursor.com/docs/grok-bot/private-networks ）。
- §07 Skill 与 Routine：教一次，让它照着做：技能与例程官方文档（https://cursor.com/help/grok-bot/skills-routines-and-automations ）、任务教学实操文档（https://cursor.com/docs/grok-bot/work ）。
- §08 审批与安全边界：审批与安全隐私文档（https://cursor.com/help/grok-bot/approvals-security-and-privacy ）、Cybernews 银行审计泄露报道（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/ ）。

### J.3 Part 3 扩展与集成篇来源 · Chapters 09 to 11
- §09 连接器与 Marketplace：市场概览文档（https://x.ai/bot/marketplace ）、插件市场官方公告（https://x.ai/news/grok-plugin-marketplace ）。
- §10 官方合作集成逐个讲：The Next Web 模型路由报道（https://thenextweb.com/news/grok-bot-claude-opus-midjourney-suno-musk ）、马斯克路由公告（https://x.com/elonmusk/status/2107724314451878104 ）、团队成员回复（https://x.com/poteto/status/2107734770990133319 ）、工程团队实战指南（https://x.ai/bot/guides/grok-bot-for-engineering ）、Team Bots 公告（https://x.ai/news/team-bots ）、X 整合公告（https://x.ai/news/grok-bot-and-x ）、搜索 X 功能发布（https://x.com/bot/status/2107949161878606089 ）、Bot 邮箱发布（https://x.com/bot/status/2108609764766908772 ）、财务连接（https://x.com/bot/status/2103936247995752705 ）、Shopify 连接（https://x.com/bot/status/2108228871938359347 ）。
- §11 中国用户的集成：没有插件也能用：KinGao 微信接入实操（https://x.com/KinGao476942/status/2108171436213104836 ）、微信集成排障指南（https://xput.app/N4rlhi ）、飞书接入教程（https://www.aitoolku.cn/tutorials/grok-feishu ）、国内平台用例分析（https://xiangyugongzuoliu.com/grokbot-use-cases/ ）。

### J.4 Part 4 至 Part 6 协作与实战篇来源 · Chapters 12 to 18
- §12 群聊与交接：群聊协作文档（https://cursor.com/help/grok-bot/chat-and-collaboration ）、多 Bot 额度消耗分析（https://forum.cursor.com/t/1-500-in-one-week-running-a-grok-bot-fleet-expected-or-a-bug/172705 ）。
- §13 编制案例库：Rafy 总管编制模式（https://x.com/0xRafy/status/2099278275906265417 ）、V2EX 数字员工流程尝试（https://www.v2ex.com/t/1241365 ）、企业案例公告（https://x.ai/news/grok-bot-for-enterprise ）。
- §14 个人与生活：马斯克下单买乐高（https://x.com/elonmusk/status/2109155867983786382 ）、旅行规划案例（https://x.com/fkysly/status/2108831626360930389 ）。
- §15 内容创作：Rowan Cheung 监控例程（https://x.com/rowancheung/status/2108328114552000842 ）、视频渲染实战（https://x.com/KinGao476942/status/2100224440948916593 ）。
- §16 赚钱与工作：新词选品建站案例（https://x.com/0xEcho99 ）、官方岗位实践指南集（https://x.ai/bot/guides ）。
- §17 中文内容工作室项目：微信下发与自媒体闭环（https://x.com/KinGao476942/status/2108171436213104836 ）、排障与落盘实践（https://xput.app/N4rlhi ）。
- §18 研发场景：工程团队落地指南（https://x.ai/bot/guides/grok-bot-for-engineering ）、Cursor 交接公告（https://x.com/bot/status/2105373767568621895 ）。

### J.5 Part 7 至 Part 9 成本与心智篇来源 · Chapters 19 to 24
- §19 额度去哪了：仪表盘使用率页面（https://cursor.com/dashboard/usage ）、LINUX DO 额度异常消耗帖（https://linux.do/t/topic/2807876 ）、在 Bot 中运行代码消耗（https://x.com/i/status/2107100457231651312 ）。
- §20 省钱心法：铁柱AGI 调度器省额度模式（https://readcopilot.ionichina.com/articles/53772 ）、外部模型执行层方案（https://x.com/i/status/2109088800903483616 ）。
- §21 事故档案：Slack 银行隐私外泄事件（https://cybernews.com/ai-news/grok-bot-leaks-bank-information/ ）、V2EX 云电脑回滚事故反馈（https://www.v2ex.com/t/1241225 ）、安全过滤器沉默故障（https://forum.cursor.com/t/grok-bot-primary-bot-silent-bot-failed-to-respond-since-oct-8-other-bots-ok-restart-this-bots-runner-only-do-not-reset/174138 ）、例程失败事件（https://forum.cursor.com/t/all-grok-bot-routines-failed-to-run/174125 ）。
- §22 常见故障速查：官方疑难解答（https://cursor.com/help/grok-bot/troubleshooting ）、中文剪贴板乱码 Bug（https://www.v2ex.com/t/1247756 ）。
- §23 别这么用：低价值例程反模式警示（https://x.com/kocer_eth/status/2101669438038634827 ）、代充会话风险说明（https://claudemax.shop/blog/grok-bot-guide-supergrok ）。
- §24 从聊天到管理：总管工作心智模型（https://x.com/0xRafy/status/2099278275906265417 ）、官方组织协同用例（https://cursor.com/help/grok-bot/use-cases ）。

### J.6 2026-10-25 增量更新来源（v0.71.2–v0.75.5 与 10 月中下旬社区实战）
- **官方技术文档与帮助中心体系（`cursor.com` 统一域名）**：
  - 技术与企业文档总览：[https://cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)
  - 工作流与登录/结账优先级（`work`）：[https://cursor.com/docs/grok-bot/work](https://cursor.com/docs/grok-bot/work)
  - 团队协作与治理（`teams`）：[https://cursor.com/docs/grok-bot/teams](https://cursor.com/docs/grok-bot/teams)
  - 企业级安全与合规（`security`）：[https://cursor.com/docs/grok-bot/security](https://cursor.com/docs/grok-bot/security)
  - 全局设置参考（`settings`）：[https://cursor.com/docs/grok-bot/settings](https://cursor.com/docs/grok-bot/settings)
  - 官方行业与岗位用例（`use-cases`）：[https://cursor.com/docs/grok-bot/use-cases](https://cursor.com/docs/grok-bot/use-cases)
  - 帮助中心首页：[https://cursor.com/help/grok-bot](https://cursor.com/help/grok-bot)
  - 订阅与价格方案（英文/中文）：[https://cursor.com/help/grok-bot/plans](https://cursor.com/help/grok-bot/plans) 、[https://cursor.com/cn/help/grok-bot/plans](https://cursor.com/cn/help/grok-bot/plans)
  - The X Subscription 三合一总览：[https://cursor.com/help/the-x-subscription/overview](https://cursor.com/help/the-x-subscription/overview)
  - Vault 与凭据安全（`secrets`）：[https://cursor.com/help/grok-bot/secrets](https://cursor.com/help/grok-bot/secrets)
  - 第三方应用与连接器（`connect-apps`）：[https://cursor.com/help/grok-bot/connect-apps](https://cursor.com/help/grok-bot/connect-apps)
  - Routine 定时与事件触发（`routines`，含 300 次/小时全局与 200 次/小时单条上限）：[https://cursor.com/help/grok-bot/routines](https://cursor.com/help/grok-bot/routines)
  - 专属邮箱 Agent Email 与 `+alias` 加号别名（`agent-email`）：[https://cursor.com/help/grok-bot/agent-email](https://cursor.com/help/grok-bot/agent-email)
  - 实时语音通话与 Action Button（`voice-chat`）：[https://cursor.com/help/grok-bot/voice-chat](https://cursor.com/help/grok-bot/voice-chat)
  - 群聊协作（`group-chats`）：[https://cursor.com/help/grok-bot/group-chats](https://cursor.com/help/grok-bot/group-chats)
  - 移动端指南（`mobile`）：[https://cursor.com/help/grok-bot/mobile](https://cursor.com/help/grok-bot/mobile)
  - 实操教程（`how-to`）：[https://cursor.com/help/grok-bot/how-to](https://cursor.com/help/grok-bot/how-to)
  - 常见问题解答（`faqs`）：[https://cursor.com/help/grok-bot/faqs](https://cursor.com/help/grok-bot/faqs)
  - 云电脑恢复与重置（`computer-recovery`）：[https://cursor.com/help/grok-bot/computer-recovery](https://cursor.com/help/grok-bot/computer-recovery)
  - 官方更新日志（v0.71.2 / v0.75.2 / v0.75.5）：[https://x.ai/changelog/bot](https://x.ai/changelog/bot)
  - 官方客服自动化标杆案例（5-Bot 舰队）：[https://x.ai/news/grok-bot-customer-support](https://x.ai/news/grok-bot-customer-support)
  - X Chat 端到端加密本地解密辅助仓库：[https://github.com/xdevplatform/xchat-grokbot-helper](https://github.com/xdevplatform/xchat-grokbot-helper)
- **官方与核心团队成员 X 公告及工作流（14 组）**：
  - `@bot` 官方发布 The X Subscription 三合一订阅（2026-10-13）：[https://x.com/bot/status/2110063783796572496](https://x.com/bot/status/2110063783796572496)
  - `@SamSokolin` 发布专属邮箱 `+alias` 加号别名与定向触发 Routine（2026-10-14）：[https://x.com/SamSokolin/status/2110496237241667621](https://x.com/SamSokolin/status/2110496237241667621)
  - `@bot` 官方发布 Grok Imagine 原生生视频与代码动效渲染（2026-10-15）：[https://x.com/bot/status/2110566041772617908](https://x.com/bot/status/2110566041772617908) 、[https://x.com/bot/status/2110772748805194127](https://x.com/bot/status/2110772748805194127)
  - `@elonmusk` 宣布 SpaceX 代购差错与银行卡安全全额赔付承诺及推荐帖（2026-10-15 / 2026-10-22）：[https://x.com/elonmusk/status/2110610960474079445](https://x.com/elonmusk/status/2110610960474079445) 、[https://x.com/elonmusk/status/2113329537509449744](https://x.com/elonmusk/status/2113329537509449744)（附 `@gofordylan` X Card 交易徽章晒单：[https://x.com/gofordylan/status/2110726444485607797](https://x.com/gofordylan/status/2110726444485607797)）
  - `@pjvann` 宣布 `@chat` 端到端加密私信与陌生人消息请求自动分拣（2026-10-16）：[https://x.com/pjvann/status/2111104660773687646](https://x.com/pjvann/status/2111104660773687646)
  - `@bot` 官方发布 iPhone Action Button 一键语音通话（2026-10-19）：[https://x.com/bot/status/2112246033178968161](https://x.com/bot/status/2112246033178968161)（附 `@SawyerMerritt` 实机演示：[https://x.com/SawyerMerritt/status/2112252980015579431](https://x.com/SawyerMerritt/status/2112252980015579431)）
  - `@bot` 官方发布 Pages（Canvas）实时报告与看板（2026-10-21）：[https://x.com/bot/status/2112991843235610885](https://x.com/bot/status/2112991843235610885)
  - `@bot` 与 `@1Password` 联合发布 1Password Brokered Sign-in 免共享库逐次审批登录（2026-10-22）：[https://x.com/bot/status/2113301060811161874](https://x.com/bot/status/2113301060811161874) 、[https://x.com/1Password/status/2113276767582498943](https://x.com/1Password/status/2113276767582498943)
  - `@bot` 官方发布 Grok Bot Vault 内置保险箱（2026-10-23）：[https://x.com/bot/status/2113754107861532677](https://x.com/bot/status/2113754107861532677)
  - `@leerob` 发起 $100 X Money 真实产品反馈悬赏主帖（2026-10-24）：[https://x.com/leerob/status/2113792409448714468](https://x.com/leerob/status/2113792409448714468)
  - `@pengzheng_` 分享检索 1908 年中餐外卖折盒专利并驱动 Blender 渲染 3D 铰链动画、内部设计工程日常工作流及 Vault 设计展示（2026-10-14 至 2026-10-24）：[https://x.com/pengzheng_/status/2113786630033322239](https://x.com/pengzheng_/status/2113786630033322239) 、[https://x.com/pengzheng_/status/2113804819274277015](https://x.com/pengzheng_/status/2113804819274277015) 、[https://x.com/pengzheng_/status/2110245240863178793](https://x.com/pengzheng_/status/2110245240863178793) 、[https://x.com/pengzheng_/status/2113757876053536891](https://x.com/pengzheng_/status/2113757876053536891)
  - `@ericzakariasson` 详解家用常开 Mac mini 注册为远程计算节点与自动部署 Cursor Worker（2026-10-24 / 2026-10-25）：[https://x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099) 、[https://x.com/ericzakariasson/status/2114157733276525044](https://x.com/ericzakariasson/status/2114157733276525044)
- **英文社区高赞工作流与实战案例（28 条核验帖子）**：
  - `@milesdeutscher` “10 大逆天 Grok Bot 用例”总帖与 10 个子工作流（2026-10-23）：主帖 [https://x.com/milesdeutscher/status/2113653680834859262](https://x.com/milesdeutscher/status/2113653680834859262) 、#10 Personal 𝕏 Assistant [https://x.com/milesdeutscher/status/2113653710631166414](https://x.com/milesdeutscher/status/2113653710631166414) 、#9 Competitor Monitor [https://x.com/milesdeutscher/status/2113653726217195817](https://x.com/milesdeutscher/status/2113653726217195817) 、#8 Lead List Builder [https://x.com/milesdeutscher/status/2113653741647999378](https://x.com/milesdeutscher/status/2113653741647999378) 、#7 Group Chat Manager [https://x.com/milesdeutscher/status/2113653756990816446](https://x.com/milesdeutscher/status/2113653756990816446) 、#6 Subscription Auditor [https://x.com/milesdeutscher/status/2113653772337770849](https://x.com/milesdeutscher/status/2113653772337770849) 、#5 Content Repurposer [https://x.com/milesdeutscher/status/2113653788196430242](https://x.com/milesdeutscher/status/2113653788196430242) 、#4 Morning Brief Routine [https://x.com/milesdeutscher/status/2113653803304296498](https://x.com/milesdeutscher/status/2113653803304296498) 、#3 Grok Swarms [https://x.com/milesdeutscher/status/2113653818651189419](https://x.com/milesdeutscher/status/2113653818651189419) 、#2 Build-Anything Agent [https://x.com/milesdeutscher/status/2113653833645818000](https://x.com/milesdeutscher/status/2113653833645818000) 、#1 Second Brain [https://x.com/milesdeutscher/status/2113653848581816595](https://x.com/milesdeutscher/status/2113653848581816595)
  - `@melvindvivas` Chief of Staff 幕僚长 `Activity Dashboard` 实时看板 Pages 用例与 `@JayKurtz90` 评价（2026-10-23）：[https://x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882) 、[https://x.com/melvindvivas/status/2113676938820895045](https://x.com/melvindvivas/status/2113676938820895045) 、[https://x.com/melvindvivas/status/2113968491573514576](https://x.com/melvindvivas/status/2113968491573514576) 、[https://x.com/JayKurtz90/status/2113983882018119823](https://x.com/JayKurtz90/status/2113983882018119823)
  - `@itsvlady` 与 `@frogchan9o1` 双栈 AI 账单与 Claude Code + Grok Bot 共用 Obsidian Vault 架构（2026-10-15）：[https://x.com/itsvlady/status/2110803638671020277](https://x.com/itsvlady/status/2110803638671020277) 、[https://x.com/frogchan9o1/status/2110883156891140416](https://x.com/frogchan9o1/status/2110883156891140416)
  - `@martinpaulweiss` “一密一宅（One home per secret）” Vault 与 1Password 权限分家法则（2026-10-25）：[https://x.com/martinpaulweiss/status/2114210343467536531](https://x.com/martinpaulweiss/status/2114210343467536531)
  - `@kial` 关于 Vault 已存银行卡结账无单独弹窗的风险提醒（2026-10-25）：[https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280)
  - `@JCOMBuilds` Action Button + 1Password 每日早晨语音点星巴克（2026-10-21）：[https://x.com/JCOMBuilds/status/2112997408510452123](https://x.com/JCOMBuilds/status/2112997408510452123)
  - `@TyeInBloom` iOS 原生日历/提醒事项/通讯录 + 1Password + Action Button + Hey Siri 联动（2026-10-23）：[https://x.com/TyeInBloom/status/2113767679588770271](https://x.com/TyeInBloom/status/2113767679588770271)
  - `@LisaMAUSA` Vault Tidy 与 SceneEdit Video Studio 模板（2026-10-25）：[https://x.com/LisaMAUSA/status/2114208018388643852](https://x.com/LisaMAUSA/status/2114208018388643852)
  - `@songsong275452`（引用 `@gokul_i`）专属 `@mail.grokbot.com` 邮箱接管 Newsletter 周报（2026-10-22）：[https://x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371)
  - `@Butlergrokbot` 基于 Routine 的家庭事务总管（2026-10-18）：[https://x.com/Butlergrokbot/status/2111860108070445394](https://x.com/Butlergrokbot/status/2111860108070445394)
  - `@AbhisheKumarA7` 云电脑安装 Codex CLI 并用完成时 Webhook 零轮询唤醒（2026-10-14）：[https://x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578)
- **中文社区深度长文、BDK 跨端联动与省额度实战（30+ 条核验帖子）**：
  - `@eze_is_1`（一泽Eze）10 条实战心得、多 Bot 架构与防臃肿 Skill 自迭代系列及 `@lanvjian` 推荐帖（2026-10-13 至 2026-10-16）：[https://x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151) 、[https://x.com/eze_is_1/status/2109852993982206425](https://x.com/eze_is_1/status/2109852993982206425) 、[https://x.com/eze_is_1/status/2110532874000879886](https://x.com/eze_is_1/status/2110532874000879886) 、[https://x.com/eze_is_1/status/2110866224892850547](https://x.com/eze_is_1/status/2110866224892850547) 、[https://x.com/lanvjian/status/2111085984855011349](https://x.com/lanvjian/status/2111085984855011349)
  - `@Khazix0918`（数字生命卡兹克）与 `@object_nullll` 关于对话路由层与重度执行委派的架构讨论（2026-10-18）：[https://x.com/Khazix0918/status/2111709708226797737](https://x.com/Khazix0918/status/2111709708226797737) 、[https://x.com/object_nullll/status/2111717423837778173](https://x.com/object_nullll/status/2111717423837778173)
  - `@StarkLJM`（Mr.鼓先生）BDK（`cursor-grokbot-agents`）跨端调用渲染 20 秒中国史动画及 28.6 秒写脚本每日 1.99 秒零额度抓榜单（2026-10-12 / 2026-10-18 / 2026-10-21）：[https://x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411) 、[https://x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377) 、[https://x.com/starkljm/status/2112818533797343312](https://x.com/starkljm/status/2112818533797343312)
  - BDK 跨端协同社区验证矩阵：`@charlychoi`（[https://x.com/charlychoi/status/2111425470201995309](https://x.com/charlychoi/status/2111425470201995309)）、`@pomufgd`（[https://x.com/pomufgd/status/2110799518283497488](https://x.com/pomufgd/status/2110799518283497488)）、`@SyrianVeterans`（[https://x.com/SyrianVeterans/status/2110661026538737879](https://x.com/SyrianVeterans/status/2110661026538737879)）、`@kangxiaile`（[https://x.com/kangxiaile/status/2109752183889744216](https://x.com/kangxiaile/status/2109752183889744216)）、`@mikan77_aoi`（4 次标准库 API 调用绕过 Webhook HTTP 400 报错，[https://x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045)）、`@z_lumia`（[https://x.com/z_lumia/status/2113800469571313974](https://x.com/z_lumia/status/2113800469571313974)）、`@AIShovelLab`（六大联动范式，[https://x.com/AIShovelLab/status/2113123121070817421](https://x.com/AIShovelLab/status/2113123121070817421)）
  - 省额度、非交互式排错、网络转发与 Vault 安全预警：`@hppzyy`（云机安装 `pi` + DeepSeek API Key 省额度，[https://x.com/hppzyy/status/2111573227881529454](https://x.com/hppzyy/status/2111573227881529454)）、`@37FlowAI`（追加 `< /dev/null` 修复非交互式 CLI 卡死，[https://x.com/37FlowAI/status/2111334386339823687](https://x.com/37FlowAI/status/2111334386339823687)）、`@XueshiQiao`（开启 `Route traffic through this computer` 借用本机住宅 IP 绕过反爬，[https://x.com/XueshiQiao/status/2112866936229183589](https://x.com/XueshiQiao/status/2112866936229183589)）、`@lyuan1618`（Tailscale 私有局域网 Mesh，[https://x.com/lyuan1618/status/2114214704008798674](https://x.com/lyuan1618/status/2114214704008798674)）、`@oxpsats`（1Password 共享彭博社凭据读研报，[https://x.com/oxpsats/status/2114207006064365670](https://x.com/oxpsats/status/2114207006064365670)）、`@JianWeiSignal`（中文社区首发 Vault 绑卡结账无二次弹窗预警，[https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488) 、[https://x.com/JianWeiSignal/status/2114195638988501103](https://x.com/JianWeiSignal/status/2114195638988501103)）、`@charlie_pmp`（三合一订阅周额度消耗变快归因，[https://x.com/charlie_pmp/status/2114214503416271131](https://x.com/charlie_pmp/status/2114214503416271131)）
  - 多 Bot 工作室、行业应用与硬件外设接入：`@CyberAlice3269`（1 CEO + 5 专职 Bot 自媒体工作室，[https://x.com/CyberAlice3269/status/2112098767151468645](https://x.com/CyberAlice3269/status/2112098767151468645)）、`@chuyang_ai`（新手视频教程第 1 期，[https://x.com/chuyang_ai/status/2111357749103911004](https://x.com/chuyang_ai/status/2111357749103911004)）、`@itgoyo`（90 秒 5 个上手技巧，[https://x.com/itgoyo/status/2111332049193996421](https://x.com/itgoyo/status/2111332049193996421)）、`@sisiliu517`（24 小时中美时差双语 X 运营，[https://x.com/sisiliu517/status/2110869965612183642](https://x.com/sisiliu517/status/2110869965612183642)）、`@realbenzh`（飞书 + Linear + `@orca_build` CLI 研发闭环，[https://x.com/realbenzh/status/2111295936635015631](https://x.com/realbenzh/status/2111295936635015631)）、`@bitman2140`（香港优才续签、孩子插班与全栈开发 8 大场景并行，[https://x.com/bitman2140/status/2114210291546493153](https://x.com/bitman2140/status/2114210291546493153)）、`@guoxudong_`（ESP32 硬件语音盒子 2 分钟全链路接入，[https://x.com/guoxudong_/status/2111767457560215771](https://x.com/guoxudong_/status/2111767457560215771)）、`@D__cup`（Shokz 骨传导耳机 + Action Button 全天候免提外脑，[https://x.com/D__cup/status/2114211130365358350](https://x.com/D__cup/status/2114211130365358350)）、`@wenser2010`（80 万周付费用户与竞品横评，[https://x.com/wenser2010/status/2113683422409572523](https://x.com/wenser2010/status/2113683422409572523) 、[https://x.com/wenser2010/status/2113683427069489614](https://x.com/wenser2010/status/2113683427069489614)）、`@kaelanyiu`（模型评测元 Bot 动态选型，[https://x.com/kaelanyiu/status/2114213605566742884](https://x.com/kaelanyiu/status/2114213605566742884)）

## 勘误页 · Corrections

### K.1 社区已知错误澄清 · Community Corrections
我核对一手资料时，发现社区里流传的一些说法有明显偏差，在这里逐一澄清。一是开放扩权日期：早期社区资料说是 8 月 21 日，但官方新闻发布时间其实是 **2026 年 8 月 26 日**(https://x.ai/news/grok-bot-more-plans)。二是 Cursor Pro 准入门槛：有早期资料断言 20 美元的 Pro 不含 Grok Bot、必须买 60 美元的 Pro+，官方计划说明页明确证实 Cursor Pro 个人计划已包含 Grok Bot(https://cursor.com/cn/help/grok-bot/plans)。三是模型锁定：早期传言说只能跑 Grok 自家模型，官方已经公布并实装了向 Claude Opus 5.5 的任务路由(https://x.com/elonmusk/status/2107724314451878104)。四是技能学习机制：有的文章说演示一遍就能学会，官方文档明确澄清屏幕教学录下来的只是草稿 Skill，必须人工补齐判断逻辑和断点后才能稳定排期(https://cursor.com/docs/grok-bot/work)。

### K.2 本书自身勘误记录 · Black Book Change Log
每一步都有出处，草稿里发现的纰漏我也全记在这里：一是早期版本删掉了一处无出处统计和一处虚构个人经历；二是讨论套餐定价时，SuperGrok 价格标签由改正；三是飞书集成的频控限制，20 条/分钟的出处改为 aitoolku；四是删除了 §15 里一处无出处的 **Opus 计费推测**。

#### 2026-10-25 版本修订记录（v261025，覆盖至 v0.75.5）
1. **官方文档域名迁移与失效链接全面清理**：随着官方将 Grok Bot 全部文档整合迁入 [https://cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)（技术与企业文档）与 [https://cursor.com/help/grok-bot](https://cursor.com/help/grok-bot)（帮助中心与用户指南），原先早期版本引用的旧域名链接已全部下线返回 404，本版已将全书所有官方文档引用全部更新为最新的 `cursor.com/docs/grok-bot/*` 与 `cursor.com/help/grok-bot/*` 有效地址。
2. **Routine 小时级运行频率上限校准**：根据 v0.75.2 更新与官方 [Routines 帮助文档](https://cursor.com/help/grok-bot/routines)，Routine 的频率配额已大幅上调至 **全账号所有 Bot 合计 300 次/小时（300 runs per hour across all Bots）** 以及 **单条 Routine 最高 200 次/小时（200 runs per hour for a single Routine）**，修订了旧版基于早期配额撰写的保守限制描述。
3. **The X Subscription 三合一统一订阅与预付 Credits 计费边界校准**：自 2026 年 10 月 13 日 / 18 日起，Grok Bot 正式并入 **The X Subscription**（Premium $30/月、Super $100/月、Ultra $200/月；Free $0 与 Plus $8/月不含 Grok Bot，详见 [官方计划说明](https://cursor.com/help/grok-bot/plans) 与 [The X Subscription 总览](https://cursor.com/help/the-x-subscription/overview)）。本版修正了旧版“默认独立订阅 + 后付费按需账单”的单一假设，明确区分了新旧两套体系：既有独立 Cursor Pro（$20/月）等旧计划只要不主动在 `cursor.com/unify` 或 `accounts.x.ai/unify` 切换仍可保留，但**一旦切换至 The X Subscription 即为单向不可逆操作**；在 The X Subscription 下，Grok Bot、Grok 与 Cursor 共享同一个每周重置的周额度池，超额消费及 Cursor 内调用第三方模型均从 `grok.com/dashboard/billing` 充值的 **Prepaid Credits（预付额度）** 中扣除；同时补充了 Apple App Store 与 Google Play 渠道订阅在合并时不会自动退订、需手动取消以防双份扣费的重要警示。
4. **Grok Bot Vault 绑卡结账审批边界与 1Password 新模式修订**：针对 v0.75.2 上线的 **1Password Brokered Sign-in**（[官方连接指南](https://cursor.com/help/grok-bot/connect-apps)，支持 1Password App 8.12.42+ 逐次弹窗审批 Personal / Private 库凭据，无需再建共享库或配置 Service Account Token）与 v0.75.5 上线的 **Grok Bot Vault**（[官方 Secrets & Vault 文档](https://cursor.com/help/grok-bot/secrets) 与 [Work 文档](https://cursor.com/docs/grok-bot/work)），本版特别校准并高亮了结账安全边界：虽然保存在 Vault 中的银行卡号与 CVV 为只写（write-only）状态且通过 `BrowserSecureFill` 注入、Bot 看不到明文，但**已保存在 Vault 中的银行卡在结账填充时不会触发单独的逐笔 Vault 弹窗确认**（仅受通用购买审批约束，详见 `@kial` [https://x.com/kial/status/2114201768414646280](https://x.com/kial/status/2114201768414646280) 与 `@JianWeiSignal` [https://x.com/JianWeiSignal/status/2114195530611855488](https://x.com/JianWeiSignal/status/2114195530611855488) 的实测提醒）；若希望每一笔消费都亲手输入卡号逐单把关，切勿将主力银行卡常驻保存在 Vault 中。
5. **作者联系信息统一校准**：全书作者 Mr.鼓先生的联系渠道统一校准为 X（`@StarkLJM`）、微信（`StarkLJM`）与 GitHub 开源仓库（[https://github.com/LJMStark/grok-bot-blackbook](https://github.com/LJMStark/grok-bot-blackbook)）。

### K.3 反馈通道与持续更新机制 · Feedback & Maintenance
AI 智能体和官方策略更新极快，本书按发布日期标注版次（当前为 v261012，并于 2026-10-25 发布 v261025 重大增量修订版，覆盖至 Grok Bot v0.75.5）。要是你在实操里发现界面变了、链接挂了或者参数不对，直接去代码仓库的 **GitHub Issues**（[https://github.com/LJMStark/grok-bot-blackbook](https://github.com/LJMStark/grok-bot-blackbook)）提反馈，或通过 X（`@StarkLJM`）与微信（`StarkLJM`）联系作者。我每周会对照官方更新日志（[https://x.ai/changelog/bot](https://x.ai/changelog/bot)）和社区一手实测复查，把每一次事实修正更新到这页勘误里。


# 联系作者 / 加入交流群

谢谢你读到这里。

这本书从第一个字到最后一条来源，都是一点点查、一点点核出来的。但 Grok Bot 迭代得太快了，书里写的东西，可能下周就变了；书里还空着的📸截图位，也要靠更多人一起补齐。

所以，特别想听到你的声音：

- 你按书里的步骤做，**哪一步卡住了**？
- 你发现了**过时的说法、失效的链接、写错的地方**？
- 你搭出了一个**好用的 Bot 编制、Skill 或 Routine**，愿意分享给更多人？
- 或者只是想找一群同样在"给 AI 派活"的人，交流踩过的坑？

都欢迎来找我。每一条反馈，我都会认真看；被采纳的勘误，会写进下一版的勘误页并致谢。

## 怎么找到我

| 渠道 | 账号 |
|---|---|
| X（Twitter） | [@StarkLJM](https://x.com/StarkLJM) |
| 微信 | StarkLJM（加好友请备注「黑皮书」） |
| 读者交流群 | 扫下方二维码加入 |

![读者交流群二维码](../images/contact-qr.png)

> [!NOTE]
*扫码加入交流群*

你也可以直接在 GitHub 仓库提 Issue：勘误、补充来源、分享实测截图，都可以。

如果这本书帮你少踩了一个坑，欢迎点个 ⭐ Star，或者把它转给一个正在研究 Grok Bot 的朋友。**每一步都有出处，每一个坑都有人踩过**——下一个坑，我们一起踩。

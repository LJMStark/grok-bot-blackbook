# 玩法大全 · 按场景 Playbook

> 整理于 2026-10-25。社区内容为作者自述，效果与数字未经本书核实。

## 🧭 方法论：从一次任务到稳定 Routine

| 标题 | 作者 / 账号 | 日期 | 链接 | 一句话摘要 |
|---|---|---|---|---|
| Task → Fix → Skill → Test → Routine | @Michael_Fenech_ | 2026-10-03 | [x.com/Michael_Fenech_/status/2106352565528977469](https://x.com/Michael_Fenech_/status/2106352565528977469) | 别从 Prompt 直接跳到 Routine，先换输入再测一遍 |
| 五阶段晋升法 | @kocer_eth | 2026-09-29 | [x.com/kocer_eth/status/2105008655770788250](https://x.com/kocer_eth/status/2105008655770788250) | 证明任务→抓方法→存 Skill→二次输入测试→排程 |
| 新手 7 步进阶 | @Michael_Fenech_ | 2026-10-01 | [x.com/Michael_Fenech_/status/2105697750645977298](https://x.com/Michael_Fenech_/status/2105697750645977298) | 给它工作而非聊天；高风险动作默认草稿 |
| 纠错先查来源 | @Michael_Fenech_ | 2026-10-04 | [x.com/Michael_Fenech_/status/2106729045878514147](https://x.com/Michael_Fenech_/status/2106729045878514147) | 被纠正时先回查日历/CRM/邮箱，不要再猜一次 |
| Computer use vs MCP vs API | @Michael_Fenech_ | 2026-09-21 | [x.com/Michael_Fenech_/status/2102048957777981938](https://x.com/Michael_Fenech_/status/2102048957777981938) | 低频验证用电脑操作，高频可靠走插件，结构化大量走 API |
| Grok 想、Bot 做 | @BotDirectoryAI | 2026-10-04 | [x.com/BotDirectoryAI/status/2106883332432945519](https://x.com/BotDirectoryAI/status/2106883332432945519) | Grok 负责调研比对，Grok Bot 负责打开 App 把事做完 |
| 10 条实战思考：Skill 自迭代防臃肿与长任务唤醒 | @eze_is_1 | 2026-10-13 | [x.com/eze_is_1/status/2109850538045264151](https://x.com/eze_is_1/status/2109850538045264151) | 定期修剪自迭代 Skill 防止规则打架与上下文膨胀；长耗时任务用 `wake on done` 或 Webhook 替代高频轮询 |
| 28.6 秒写确定性爬虫：每日 1.99 秒零额度抓榜单 | @StarkLJM | 2026-10-18 | [x.com/starkljm/status/2111803996734419377](https://x.com/starkljm/status/2111803996734419377) | 用 CLI 一次性生成带缺字段告警与 `null` 防御规则的 Python 爬虫，日常定拉榜单实现零模型额度消耗 |
| 模型评测元 Bot（Meta-Evaluator）动态分配 CLI 模型 | @kaelanyiu | 2026-10-25 | [x.com/kaelanyiu/status/2114213605566742884](https://x.com/kaelanyiu/status/2114213605566742884) | 每隔几天自动跑一次基准测试评估前沿模型，动态决定其余业务 Bot 在 CLI 中调用的主力模型 |

## 🗂️ 总助 / Chief of Staff

| 标题 | 作者 / 账号 | 日期 | 链接 | 一句话摘要 |
|---|---|---|---|---|
| 官方 Chief of Staff 工作流转述 | @0xRafy | 2026-09-13 | [x.com/0xRafy/status/2099278275906265417](https://x.com/0xRafy/status/2099278275906265417) | 每条重要事项给出 source / why it matters / next step |
| How I AI：Claire Vo 的 Chief 等 Bot | Claire Vo（YouTube） | — | [youtube.com/watch?v=QBmgF1kJSK4](https://www.youtube.com/watch?v=QBmgF1kJSK4) | 每小时扫邮箱日历 Slack、家庭"厨房桌报纸"、订阅砍价 Bot |
| 给总助 Bot 起独立名字的邮箱 | @petergyang | 2026-10-09 | [x.com/petergyang/status/2108624122339287335](https://x.com/petergyang/status/2108624122339287335) | 别用你自己的名字注册 Bot 邮箱，否则抄送措辞别扭 |
| 所有 Bot 每晚发语音备忘 | @PaulJLipsky | 2026-09-21 | [x.com/PaulJLipsky/status/2101851806330712339](https://x.com/PaulJLipsky/status/2101851806330712339) | 让每个 Bot 每晚用语音汇报当天工作 |
| 让 Bot 读官方 changelog | @jp_costa | 2026-10-07 | [x.com/jp_costa/status/2107629480374308893](https://x.com/jp_costa/status/2107629480374308893) | 每天读两次更新日志，提示对自己配置的影响 |
| 专属邮箱/别名接收 Newsletter + 周六汇总 Routine | @songsong275452 | 2026-10-22 | [x.com/songsong275452/status/2113108916229886371](https://x.com/songsong275452/status/2113108916229886371) | 把所有邮件通讯迁至仅供 Bot 读取的 `@mail.grokbot.com` 地址，每周六定跑 Routine 生成一份脱水周报 |
| 用 Pages 搭建 Chief of Staff 实时 Activity Dashboard | @melvindvivas | 2026-10-23 | [x.com/melvindvivas/status/2113676935956160882](https://x.com/melvindvivas/status/2113676935956160882) | 让总助维护一张共享 Page 看板，汇总所有专职 Bot 的时间线、进行中、已完成与待人工审批事项 |
| Grok Swarms：1 个总控 Bot 调度 10+ 专职 Bot 集群 | @milesdeutscher | 2026-10-23 | [x.com/milesdeutscher/status/2113653818651189419](https://x.com/milesdeutscher/status/2113653818651189419) | 由主控 Orchestrator Bot 并行拆解并指派 10 余个细分领域专职 Bot 协同完成市场调研与内容生产 |
| 跨平台群聊管家与晨间情报简报 Routine | @milesdeutscher | 2026-10-23 | [x.com/milesdeutscher/status/2113653756990816446](https://x.com/milesdeutscher/status/2113653756990816446) | 监控 WhatsApp/Discord/Slack/Telegram 群聊提炼待回事项，并结合日历、邮件与 X 定时推送晨报 |

## 📣 内容创作 / 自媒体

| 标题 | 作者 / 账号 | 日期 | 链接 | 一句话摘要 |
|---|---|---|---|---|
| 小红书内容团队工作流 | 觉醒AI | — | [jxxy.net](https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/) | 总助+自媒体+情报+美工四岗；三道硬门，发布权永远在人 |
| 媒体团队五岗 | 觉醒AI | — | [jxxy.net](https://www.jxxy.net/ai/articles/AdrianPunk115-2097311704547987756/) | 情报/选题/主笔/事实编辑/复盘，各自权限写进提示词 |
| 训练实录：规则落盘成文件 | 觉醒AI | — | [jxxy.net](https://www.jxxy.net/ai/articles/grok-bot-workflow-training/) | 调性卡、选题、规则都写进 md 文件，"对着文件而不是一句收到" |
| 九类场景与资源库 | 象鱼工作流 | — | [xiangyugongzuoliu.com](https://xiangyugongzuoliu.com/grokbot-use-cases/) | 国内平台无插件的绕法；第一周三只 Bot 就够 |
| 用 Grok Bot 做视频：八步流程 | 纯度AI | — | [chunduai.com](https://chunduai.com/tutorials/grok-bot-code-video) | 云电脑写前端代码逐帧截图合成视频 |
| Grok Bot 保姆级做视频教程 | 技术栈 | — | [jishuzhan.net](https://jishuzhan.net/article/2108434394092691458) | edge-tts 配音、响度与字幕规范、读 X 做选题 |
| 应用指南：闲鱼上架、小红书做图等 | Miles Ma | — | [immilesma.com](https://immilesma.com/blog/grok-bot-practical-guide/) | 闲鱼上架、小红书做图、做短视频、整理收藏 |
| 用 Skill 做科普动画 | @miles_mazy | 2026-10-10 | [x.com/miles_mazy/status/2108904379097166149](https://x.com/miles_mazy/status/2108904379097166149) | 用真实录音做传统乐器科普动画发小红书抖音 |
| 下载专家 Bot | @KinGao476942 | 2026-09-16 | [x.com/KinGao476942/status/2100073265716928662](https://x.com/KinGao476942/status/2100073265716928662) | 把公众号文章存成 PDF 归档到知识库 |
| 视频下载转写进知识库 | @KinGao476942 | 2026-09-16 | [x.com/KinGao476942/status/2100224440948916593](https://x.com/KinGao476942/status/2100224440948916593) | 下载抖音/X/B站视频、转写文案、存飞书 |
| 小红书 Grok Bot 博主名单 | @jedeeai | 2026-10-07 | [x.com/jedeeai/status/2107702960046412083](https://x.com/jedeeai/status/2107702960046412083) | 整理值得关注的小红书相关博主 |
| 24 小时跨时区中英文 X 账号自动化运营 | @sisiliu517 | 2026-10-15 | [x.com/sisiliu517/status/2110869965612183642](https://x.com/sisiliu517/status/2110869965612183642) | 按中美时差排布小时级 Routine（白天中文区、夜间英文区），每晚自动复盘互动数据迭代次日选题 |
| 1 个 CEO Bot + 5 个专职 Bot 的自媒体内容工作室 | @CyberAlice3269 | 2026-10-19 | [x.com/CyberAlice3269/status/2112098767151468645](https://x.com/CyberAlice3269/status/2112098767151468645) | 语音向 CEO Bot 下达指令，结合共享知识库与 SOP 调度情报、选题、撰稿、审校与配图 5 个专职 Bot |
| 爆款内容提取与多平台改写 Bot（Content Repurposer） | @milesdeutscher | 2026-10-23 | [x.com/milesdeutscher/status/2113653788196430242](https://x.com/milesdeutscher/status/2113653788196430242) | 自动抓取 X 高互动异常爆款帖，调用自定义 Agent Skill 一键改写为 LinkedIn 长文、Newsletter 与短视频口播稿 |
| 检索 1908 年专利并在 Blender 写铰链脚本生成 3D 折叠动画 | @pengzheng_ | 2026-10-24 | [x.com/pengzheng_/status/2113786630033322239](https://x.com/pengzheng_/status/2113786630033322239) | 让 Bot 考证中餐外卖盒折法并查出 1908 年原版专利，在 Blender 中按专利折痕写铰链脚本渲染无缝循环动画 |
| SceneEdit Video Studio：MP4 视频单镜头局部重绘模板 | @LisaMAUSA | 2026-10-25 | [x.com/LisaMAUSA/status/2114208018388643852](https://x.com/LisaMAUSA/status/2114208018388643852) | 定位成片 MP4 中的指定单镜头进行局部替换重渲并无缝拼接，免去整片重跑 |

## 🏠 个人与生活

| 标题 | 作者 / 账号 | 日期 | 链接 | 一句话摘要 |
|---|---|---|---|---|
| 欧洲旅行全程规划 | @fkysly | 2026-10-10 | [x.com/fkysly/status/2108831626360930389](https://x.com/fkysly/status/2108831626360930389) | 行程、餐饮、门票、租车全交给 Bot 规划 |
| 帮我买到售罄的 iPhone | @liam_fallen | 2026-10-11 | [x.com/liam_fallen/status/2109332219126784098](https://x.com/liam_fallen/status/2109332219126784098) | 给虚拟卡后 Bot 发邮件问店找到现货下单 |
| 连接财务插件算扣款 | @B_doong2daddy | 2026-10-01 | [x.com/B_doong2daddy/status/2105711764641833238](https://x.com/B_doong2daddy/status/2105711764641833238) | 只读查询未来 10 天自动扣款总额 |
| 台湾比价小帮手 | Darrell TW | — | [darrelltw.com](https://www.darrelltw.com/grok-bot-review/) | Teach a task 存比价技能，四站比价出表 |
| iPhone Action Button 语音唤醒 + 1Password 每天自动点星巴克 | @JCOMBuilds | 2026-10-21 | [x.com/JCOMBuilds/status/2112997408510452123](https://x.com/JCOMBuilds/status/2112997408510452123) | 每天早上长按手机操作按钮语音吩咐助理 Bot，通过 1Password 授权凭证自动完成星巴克下单 |
| iOS 日历/提醒/通讯录 + Action Button + Siri 捷径全联动 | @TyeInBloom | 2026-10-23 | [x.com/TyeInBloom/status/2113767679588770271](https://x.com/TyeInBloom/status/2113767679588770271) | 打通 iOS 原生日历、提醒事项与通讯录权限，配合 Action Button 与“Hey Siri”定向唤醒专职 Bot |
| 订阅审计砍价退订 Bot 与替代 Obsidian 的第二大脑 | @milesdeutscher | 2026-10-23 | [x.com/milesdeutscher/status/2113653772337770849](https://x.com/milesdeutscher/status/2113653772337770849) | 扫描周期性扣费项目并实时发信议价或退订；同时将 X 书签、长文与笔记建库做成免手动打标的第二大脑 |
| 韶音骨传导耳机 + Action Button 全天候随身语音助理 | @D__cup | 2026-10-25 | [x.com/D__cup/status/2114211130365358350](https://x.com/D__cup/status/2114211130365358350) | 全天佩戴不入耳骨传导耳机，随时按 iPhone Action Button 与 Grok Bot 语音交办事务 |
| 香港优才续签、孩子插班、备考与全栈开发等 8 大生活工作流 | @bitman2140 | 2026-10-25 | [x.com/bitman2140/status/2114210291546493153](https://x.com/bitman2140/status/2114210291546493153) | 用多个专职 Bot 长期跟进香港优才续签材料、孩子香港插班、备考计划、公众号与 X 运营及每日情报 |

## 💻 研发

| 标题 | 作者 / 账号 | 日期 | 链接 | 一句话摘要 |
|---|---|---|---|---|
| 指挥 Cursor 云端 Agent | @xiangxiang103 | 2026-10-11 | [x.com/xiangxiang103/status/2109265867859177552](https://x.com/xiangxiang103/status/2109265867859177552) | 直接让 Bot 用 Cursor 云端 Agent 写代码，无需装 CLI |
| 官方 6 套编制指南汇总 | @monokern | 2026-10-09 | [x.com/monokern/status/2108533543848558780](https://x.com/monokern/status/2108533543848558780) | DevRel、营销、销售、工程、手游等官方指南编制 |
| Peter Yang × Peng Zheng & Lauren Tan | Peter Yang（YouTube） | — | [youtube.com/watch?v=xZ5TEaleUdg](https://www.youtube.com/watch?v=xZ5TEaleUdg) | 工程负责人 Bot 委派给工程师 Bot 开 Cloud Agent |
| 本地 Claude Code / Codex 通过 BDK 派单云端 Grok Bot 渲染视频 | @StarkLJM | 2026-10-12 | [x.com/starkljm/status/2109544938644107411](https://x.com/starkljm/status/2109544938644107411) | 用 `cursor-grokbot-agents` 打通本地 CLI 与云端 Bot，将重度多媒体渲染与检索外包给云端并发执行 |
| 云电脑安装 Codex CLI + Webhook 完工零轮询唤醒 | @AbhisheKumarA7 | 2026-10-14 | [x.com/AbhisheKumarA7/status/2110484964143976578](https://x.com/AbhisheKumarA7/status/2110484964143976578) | 在 Grok Bot 云电脑内运行 Codex CLI，配置完成回调 Webhook 仅在长耗时编码结束时唤醒 Bot |
| 4 次 API 调用纯标准库脚本打通 Claude Code 与 Grok Bot | @mikan77_aoi | 2026-10-16 | [x.com/mikan77_aoi/status/2111043148088816045](https://x.com/mikan77_aoi/status/2111043148088816045) | 绕过 Webhook 400 格式报错，用无守护进程的 Python 标准库脚本实现本地 Claude Code 直接向 Grok Bot 派活 |
| 飞书 + Linear + 邮件上下文对齐后驱动 CLI 写代码 | @realbenzh | 2026-10-17 | [x.com/realbenzh/status/2111295936635015631](https://x.com/realbenzh/status/2111295936635015631) | 让 Grok Bot 聚合飞书、Linear 与邮件需求上下文，对齐验收标准后在云端交互式驱动 `@orca_build` CLI 编码 |
| ESP32 硬件语音助手通过 Cloudflare Tunnel + MCP 接入 Grok Bot | @guoxudong_ | 2026-10-18 | [x.com/guoxudong_/status/2111767457560215771](https://x.com/guoxudong_/status/2111767457560215771) | 串联 ESP32 硬件、Cloudflare Tunnel、Mac 语音转文字与本地 MCP 服务，2 分钟内完成硬件语音端到端交互 |
| 家用 Mac mini 常驻挂载与远程部署 `cursor-agent worker` | @ericzakariasson | 2026-10-24 | [x.com/ericzakariasson/status/2114095056630272099](https://x.com/ericzakariasson/status/2114095056630272099) | 将常开 Mac mini 注册到 `Settings > Computer` 供云端 Bot 远程调用，或让 Bot 自动配置远程机器运行 `cursor-agent worker` |

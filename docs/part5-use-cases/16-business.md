# §16 赚钱与工作 · Work & Business

[← 上一章：§15 内容创作 · Creators](../part5-use-cases/15-creators.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§17 从零搭一个“中文内容工作室” · Capstone A: Building a Chinese Content Studio →](../part6-capstones/17-capstone-a.md)

---

> **适合谁**：想用 Bot 辅助副业、跨境电商或团队业务的读者。16.3 的官方岗位指南面向用 Slack、CRM、ATS 的海外团队；国内小团队可以只借鉴"Bot 起草、人工发送"的分工方式。

很多人以为给 AI 一台电脑，就能全自动赚钱。真敢这么放手，账户额度一天就会烧光，搞不好还会被封号。我调研了一圈发现，Grok Bot 根本不是什么自动吐钞机，它就是一个不知疲倦的数字劳动力。能赚钱的工作流，从来不是让它从头到尾接管商业闭环，而是把它卡在整个链路里最枯燥、最耗时、确定性最高的环节。

![商业与工作流中的 Grok Bot 定位：充当高频数据过滤器与草稿发生器，决策与资金闸门由人把控](../../images/fig-16-1.png)

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

![官方五大职能岗位（销售、招聘、法务、客服、市场）的人机分工与审批卡闸门体系](../../images/fig-16-2.png)

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

---

[← 上一章：§15 内容创作 · Creators](../part5-use-cases/15-creators.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§17 从零搭一个“中文内容工作室” · Capstone A: Building a Chinese Content Studio →](../part6-capstones/17-capstone-a.md)

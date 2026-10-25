# §02 怎么才能用上 · Getting Access

[← 上一章：§01 Grok Bot 是什么 · What It Is](../part1-getting-started/01-what-it-is.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§03 十分钟安装与开箱 · Install in 10 Minutes →](../part1-getting-started/03-install.md)

---

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

![资格判定流程图——你有 Cursor 付费订阅？→ 有 → 直接用。没有 → 你有 SuperGrok / X Premium+ → 有 → 关联。是 Lite？→ 不行。都没有 → 免费试用 7 天。](../../images/fig-02-1.png)

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

![档位对比卡——三列：Cursor 线、SuperGrok 线、X Premium+ 线，每列按用量从低到高排列，中间用虚线连接同级别的档位。](../../images/fig-02-2.png)

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

![「骗局识别卡」——左列是可信信号（官方域名、有出处的社区实测、官方文档链接），右列是红旗信号（要你交 Session JSON、承诺回报率、低价区跳板、零阅读搬运、「国内体验版」）。](../../images/fig-02-3.png)

*图：「骗局识别卡」——左列是可信信号（官方域名、有出处的社区实测、官方文档链接），右列是红旗信号（要你交 Session JSON、承诺回报率、低价区跳板、零阅读搬运、「国内体验版」）。*

---

[← 上一章：§01 Grok Bot 是什么 · What It Is](../part1-getting-started/01-what-it-is.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§03 十分钟安装与开箱 · Install in 10 Minutes →](../part1-getting-started/03-install.md)

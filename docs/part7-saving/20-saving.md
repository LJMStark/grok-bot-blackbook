# §20 省钱心法 · Saving

[← 上一章：§19 额度去哪了 · Where Usage Goes](../part7-saving/19-usage.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§21 事故档案 · Incident Files →](../part8-pitfalls/21-incidents.md)

---

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

![调度器模式与全能 Bot 的 Token 消耗对比](../../images/fig-20-1.png)

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

![脚本轮询与 Webhook 按需唤醒架构](../../images/fig-20-2.png)

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

![外部执行层分流与数据边界](../../images/fig-20-3.png)

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

![Cursor 订阅与 SuperGrok 档位对应及权益不叠加判定图](../../images/fig-20-4.png)

*图：Cursor 订阅与 SuperGrok 档位对应及权益不叠加判定图*
> [!NOTE]
> 📸 **截图位（待补）**：Cursor Dashboard 中的 Monthly Limit 支出上限设置界面

---

[← 上一章：§19 额度去哪了 · Where Usage Goes](../part7-saving/19-usage.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§21 事故档案 · Incident Files →](../part8-pitfalls/21-incidents.md)

# §17 从零搭一个“中文内容工作室” · Capstone A: Building a Chinese Content Studio

[← 上一章：§16 赚钱与工作 · Work & Business](../part5-use-cases/16-business.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§18 研发场景：Bot + Cursor 云端 Agent + GitHub · Capstone B →](../part6-capstones/18-capstone-b.md)

---

很多新手刚上手时，习惯把所有杂事一股脑塞进同一个对话框。两三天后上下文彻底乱掉，最后只能推倒重来。搭建一个**四人内容工作室**，核心是从单聊转向团队协作。

账号内 Bot 数量自 9 月 1 日 v0.31.0 起不再限于约 50 个（https://x.ai/changelog/bot），群聊支持容纳 2 到 6 个 Bot（https://cursor.com/help/grok-bot/chat-and-collaboration）。这个项目不需要堆砌过多角色，团队成员建议先从最精炼的结构起步（https://x.com/poteto/status/2108097362283597916，团队成员 X 帖）。整个工作室只设四个角色：总编辑负责任务拆解与全局把控；选题情报员搜集线索与行业动态；文案主笔把选题扩写为草稿；审校排版员对照事实与平台规范做质检。

![四人内容工作室协作架构与信息流向](../../images/fig-17-1.png)

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

---

[← 上一章：§16 赚钱与工作 · Work & Business](../part5-use-cases/16-business.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§18 研发场景：Bot + Cursor 云端 Agent + GitHub · Capstone B →](../part6-capstones/18-capstone-b.md)

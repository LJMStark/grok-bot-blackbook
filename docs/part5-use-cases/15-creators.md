# §15 内容创作 · Creators

[← 上一章：§14 个人与生活 · Personal & Daily Life](../part5-use-cases/14-personal.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§16 赚钱与工作 · Work & Business →](../part5-use-cases/16-business.md)

---

很多人把 Grok Bot 当成另一个网页聊天窗口，每次想发内容就打开它问一句帮我写条推文。这种用法把它的后台例程和云电脑完全浪费了。我调研发现，做内容创作时，Grok Bot 真正的分水岭不是文笔，而是你从亲自干活的作者变成了调度流水线的**责任主编**。

> **适合谁**：做 X、公众号、小红书、短视频的个人创作者。15.1 需要 X 账号，例程示例把结果推到 Slack（没有 Slack 就把"Send it to me on Slack"改成"在对话里告诉我"）；15.3 涉及脚本和命令行，零代码读者可以只看思路，把提示词整段交给 Bot 去执行。

![内容创作从单次对话到无人值守流水线的演进路径](../../images/fig-15-1.png)

*图：内容创作从单次对话到无人值守流水线的演进路径*

### 15.1 X 监控 4 个 Routine · X Monitoring Routines

#### 场景
做内容天天自己刷推特找素材，效率太低了。2026 年 10 月 8 日，官方宣布 Grok Bot 原生支持搜索、阅读和监控 X【官方】（https://x.com/bot/status/2107949161878606089 ）。早在 8 月 30 日官方就宣布：关联 X 账号后，系统会自动创建开发者账户并附带一些初始额度【官方】（https://x.com/bot/status/2093822274067706170 ）。有了这个能力，就能让 Bot 充当全天候雷达。
Rowan Cheung 基于这次更新设计了 4 个监控例程【社区】（https://x.com/rowancheung/status/2108328114552000842 ）：挖别人在跑的真实 AI 工作流、盯自己品牌的提及和口碑、抓竞品品类里的潜在客户痛点，以及跟进刚加的新人脉。我看他的例程，结构写得很死：卡死时间和时区、限定时间窗口、写清过滤规则、定死输出字段、绑好 Slack 投递，严格禁止私自跟外界互动，没抓到结果时也有单行兜底。

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

#### Routine
官方规定每个 Bot 最多配 50 个 Routine，每个 Routine 保留最近 20 次运行记录，触发间隔至少 5 分钟【官方】（https://cursor.com/help/grok-bot/routines ）。在这套监控里，工作流挖掘、品牌提及和人脉跟进排在每个工作日早上的固定时间（8:30、9:00、9:15），潜在客户监听设为每 4 小时一次。时间一到，Bot 会唤醒云电脑，调 X 搜索接口抓最近 24 小时的帖子，去重过滤后通过 Slack 连接器把 Markdown 简报推到频道里。要是没抓到匹配内容，发一行说明就停，不吵人。

#### 成本
官方未公布单独搜索 X 的计费标准，所有交互都扣套餐自带的周额度【官方】（https://cursor.com/help/grok-bot/plans ）。社区有人算过一笔账，要是设成每 5 分钟跑一次 Routine，一个月触发 8,640 次，能把一个 33 美元的活烧成 397 美元（个例）【社区】（@fleyta88 https://x.com/fleyta88/status/2109346840382415019 ）。社区帖称在 Cursor Pro 订阅下，单条交互消息大约消耗 1% 周额度（个例）【社区】（@miniyarov https://x.com/miniyarov/status/2105428357273800799 ）。Rowan Cheung 把大部分监控设成每天跑一次，请求频次就压得很低。
成本实测状态：【实测·TODO待实测】测定 4 个 Routine 在 Cursor Pro 订阅下连续运行一周消耗的周用量百分比。

#### 坑
第一个坑是**禁止动作缺失**。提示词里要是没写死禁止私自发帖、回复和私信，Bot 可能会擅自去跟搜出来的推文互动，弄不好就封号甚至搞出公关事故。
第二个坑是后台审批超时。官方文档写明，后台或其他 Bot 触发的审批卡大约 10 分钟就会过期显示 Expired，动作就不执行了【官方】（official/docs-approvals-security-and-privacy.md 第 43 行）。第四个跟进例程起草任务前要等你回复，要是 10 分钟没理它，这一轮流程就中断了。
第三个坑是没搜到结果时的幻觉。要是没规定搜索落空怎么办，Bot 会为了交差拼凑旧消息甚至硬编推文。必须在提示词最后加一句，没结果就回一行单行说明。
第四个坑是例程空转。每天准时推的早报要是两周都没人看，额度就全打水漂了。社区经验指出，例程本身不是产出，能帮你做决定的例程才有价值，没产出的例程要及时删掉【社区】（https://x.com/kocer_eth/status/2101669438038634827 ）。

> [!NOTE]
> 📸 **截图位（待补）**：Grok Bot 中配置完成的 X 监控例程界面与 Slack 接收到的摘要通知
![X 监控 Routine 从搜索抓取、条件过滤到 Slack 投递的单向数据流](../../images/fig-15-2.png)

*图：X 监控 Routine 从搜索抓取、条件过滤到 Slack 投递的单向数据流*

### 15.2 公众号选题与日推 · WeChat Official Account Topics and Daily Pushes

#### 场景
做微信公众号有个现实问题：Grok Bot 没有任何国内平台的官方插件【社区】（https://xiangyugongzuoliu.com/grokbot-use-cases/ ）。后台的阅读量、完读率和用户画像全是非公开数据，公开网页抓不到，只能靠手动导数据或者提供材料。
觉醒AI 的 Adrian Punk 和 yvchengshanren 摸索出了一条自媒体流水线【社区】（https://www.jxxy.net/ai/articles/AdrianPunk115-2097311704547987756/ 与 https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/ ）。千万别指望建一个全能 Bot 搞定全部，那只是把找材料、写初稿和审校的堵点全堆在同一个窗口里。他们的做法是在云电脑 `/workspace/content-team/` 目录下按流程建文件夹，分出情报侦察员、选题策划师、内容主笔、事实编辑四个专职角色，靠文件传递交接。
跑这条线要守住**三道硬门**：输入的源文必须来自人工指定的公开链接或一手文档，禁止 Bot 翻不可信的二手谣言；专业数据必须来自真实的测试报告，禁止 Bot 自行瞎编；最终的排版入库和发布按钮必须由人工手动点击，绝不下放给 Bot【社区】（https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/ ）。

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

#### Routine
这个流程可以配成工作日早上的例程。设成每个工作日早晨 08:30 执行，Bot 先看 `/workspace/content-team/01-inbox/` 目录下有没有前一天沉淀的事实卡。只要有材料，就自动提炼出当天的 3 个选题 Brief 存入 `02-briefs/` 目录。
人工在对话中选定并回复批准后，触发主笔 Bot 生成完整初稿。因为国内平台没有官方接口，Bot 把初稿写入 `03-drafts/` 后就会停下，通过微信下发渠道或系统提示通知。我们把 Markdown 复制到排版工具或公众号后台，自己人工点击发布。

#### 成本
所有 Bot 运行都消耗账户的统一周额度【官方】（https://cursor.com/help/grok-bot/plans ）。Grok Bot 没有模型选单，也不显示每次请求的底层模型，所以别指望靠切便宜模型省额度【官方】（https://cursor.com/help/grok-bot/models ，转引自 carlstack 额度文章）。社区帖称 Pro 档每条消息约耗 1% 周额度（个例）【社区】（https://x.com/miniyarov/status/2105428357273800799 ）。【实测·TODO待实测】一次完整四岗交接的额度消耗。
成本实测状态：【实测·TODO待实测】测定公众号从线索汇总到成稿审校全流程单次消耗的周用量百分比。

#### 坑
第一个坑是模拟登录招来风控。象鱼工作流指出国内平台没有原生插件，如果在云电脑里用高频脚本刷新网页或模拟点击，容易触发平台的安全拦截甚至封号【社区】（https://xiangyugongzuoliu.com/grokbot-use-cases/ ）。切忌让 Bot 自动去公众号后台点发布，把发布权留在人类客户端。
第二个坑是主笔瞎编技术数据。主笔 Bot 写长文容易顺手编造出“性能提升 300%”或“某大厂全员采用”这类假数据。必须在角色描述和提示词里加上禁止项，要求所有数字必须追溯至真实材料，没有出处的数字一律不得写入【社区】（https://www.jxxy.net/ai/articles/AdrianPunk115-2097311704547987756/ ）。
第三个坑是共享云电脑带来的凭据泄漏风险。官方文档指出同一账号下的所有 Bot 共享同一台 Linux 云电脑、同一个浏览器登录态和同一个 `/workspace`【官方】（https://cursor.com/docs/grok-bot/work ）。前一个 Bot 保存了私有凭据，其他 Bot 都能直接读取，切勿在云电脑环境中存放主账号密码或私密会话凭据。
第四个坑是口头纠错未落盘。觉醒AI 指出，你在对话里纠正 Bot 的错误时，Bot 经常回答“记下了”，但只要没把规则写入 `voice.md` 或技能规则文件，下一次新建会话它照样犯同样的错误【社区】（https://www.jxxy.net/ai/articles/grok-bot-workflow-training/ ）。

> [!NOTE]
> 📸 **截图位（待补）**：/workspace/content-team/ 目录下生成的选题 Brief 与主笔初稿文件
![公众号内容流水线分工：情报、选题、主笔、编辑与人工发布守门](../../images/fig-15-3.png)

*图：公众号内容流水线分工：情报、选题、主笔、编辑与人工发布守门*

### 15.3 写代码渲染视频（ffmpeg） · Code-Rendered Video

#### 场景
传统短视频制作要么靠剪辑软件拼素材，要么靠文生视频模型抽卡。文生视频虽然画面逼真，但在数据图表、知识科普、产品演示和精确文字动效上根本对不齐节奏，改动一个字整段画面就会完全变形。
Leo Xiaolei 和 0xCarnagee 摸索出了一条纯代码渲染的视频管线【社区】（https://x.com/leo_xiaolei/status/2108159484401262882 与 https://x.com/0xCarnagee/status/2108501747643670780 ）：让 Grok Bot 编写基于 HTML Canvas 或 SVG 的前端动效页面，通过无头浏览器 Playwright 驱动 Chromium 逐帧截图，最后调用 ffmpeg 将连续图片与音频压制为竖屏 MP4 视频。
这套管线有两个核心支柱。第一是**放弃系统时钟**，页面暴露 `window.seek(t)` 纯时间函数，输入任意时间戳 t 永远渲染出完全一致的静态画面，粒子等随机特效采用 Mulberry32 算法锁定随机种子；第二是使用 edge-tts 生成配音并显式传入 `boundary='WordBoundary'` 导出词级时间戳，让口播念出的每一个字充当画面动效的时钟基准。

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

#### Routine
为了避免白天交互时长时间占用云电脑资源，可以将渲染包装为夜间渲染队列例程。
在 `/workspace/studio/` 目录下编写 `render-queue.sh`，利用 Linux `flock` 文件锁确保同一时间只有一个渲染任务运行。在设置中配置 Routine：每天晚上 23:00 自动检查 `/workspace/studio/projects/` 目录下带有 `APPROVED` 与 `READY` 标记的项目。
若存在待渲染工程，Routine 启动 Playwright 和 ffmpeg 批量压制成片，自动生成 `contact.png` 联系表并打上 `PASSED` 标记。次日早晨 08:00 交付 Bot 将最终成片与联系表推送过来，即便合上笔记本也能在夜间全自动完成压制。

#### 成本
官方帮助页没有列出云电脑计算时长的单独收费项，按现有说明，Bot 的工作都计入周额度【推测】（https://cursor.com/help/grok-bot/plans ）。在速度与资源消耗方面，社区实测表明在 Grok Bot 云电脑上运行 4 秒示例视频（120 帧），全流程从生成到压制约耗时 10 到 14 秒【社区】（作者自述，https://chunduai.com/tutorials/grok-bot-code-video ；代码 https://gist.github.com/threerocks/5f6f6d5b3801a400bb5343379082580c ）；在 2 核无 GPU 的 Linux 机器上，15 秒动效的草稿渲染约 48 秒，带运动模糊的 60fps 终版约 6 分钟【社区】（https://chunduai.com/tutorials/grok-bot-motion-studio ，整理自 https://x.com/0xCarnagee/status/2108501747643670780 ）。
成本实测状态：【实测·TODO待实测】测定 60 秒 30fps 动效短视频在云电脑上完整渲染单次消耗的周用量百分比。

#### 坑
第一个坑是未核对静帧直接渲染整片。1 分钟 30fps 的视频需要截取 1800 张高清图片，在无显卡的云电脑上单次渲染可能耗费二十多分钟【社区】（https://chunduai.com/tutorials/grok-bot-code-video ）。如果代码中存在排版错位，整段渲染全部报废。必须在提示词里强制执行硬门禁：静帧未获人工确认，严禁启动全片渲染。
第二个坑是中文字体缺失导致乱码。官方说明云电脑做"电脑更新"、Recover 或 Reset 后会移除手动安装的应用和软件包（普通软件更新会保留）【官方】（https://cursor.com/help/grok-bot/computer-recovery ）。如果系统中缺少思源黑体或 Noto Sans CJK，Canvas 渲染出的中文字符会全部退化为空白方块。必须将中文字体安装命令写入环境初始化脚本 `bootstrap.sh` 中，并在渲染前通过 `fc-list :lang=zh` 进行校验【社区】（https://chunduai.com/tutorials/grok-bot-code-video ）。
第三个坑是模型“看不了视频”的审片盲区。当前大模型只能接受静态图片输入，无法直接回放 MP4 视频。如果直接问 Bot 成片质量，它只能根据文字描述凭空推断。必须通过 ffmpeg 提取每 0.5 秒一帧拼成带时间码的联系表（Contact Sheet），新开一个没有制作上下文的独立审片 Bot 会话进行挑错；同时配音语气与卡点模型完全无法试听，必须戴上耳机亲自听一遍。
第四个坑是音频起振杂音与字幕字号偏差。代码生成的占位音效若未添加 2 到 12 毫秒的淡入淡出，拼接处会产生轻微爆音；而在使用 ASS 格式烧录字幕时，思源黑体的字号不是屏幕像素，实际高度等于 FontSize 除以 1.448，必须通过一帧静帧量测矫正【社区】（同上）。

> [!NOTE]
> 📸 **截图位（待补）**：云电脑终端运行 render.py 逐帧截图与生成的审片联系表 contact.png
![代码渲染视频流水线：口播时间戳驱动 Canvas 动效、Playwright 逐帧截图与 ffmpeg 压制](../../images/fig-15-4.png)

*图：代码渲染视频流水线：口播时间戳驱动 Canvas 动效、Playwright 逐帧截图与 ffmpeg 压制*

### 15.4 配图 skill 与小红书图卡 · Illustration Skills and Xiaohongshu Graphic Cards

#### 场景
视觉卡片是小红书等社交平台的第一入口。很多创作者直接用生图模型生成图文卡片，但图像模型做不到多张卡片风格一致，画面上生成的文字也基本全错。觉醒AI 在实战中甚至彻底关闭了纯 AI 配图，因为低质假图极易被平台识别判定为低质内容【社区】（https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/ ）。
Miles Ma 提出的知识图卡流程给出了切实可行的方案【社区】（https://immilesma.com/blog/grok-bot-practical-guide/ 原文 https://x.com/miles_mazy/status/2098708209095819605 ）：让 Grok Bot 担任小红书编辑，围绕特定主题制作一套符合 3:4 竖屏比例（1080×1440）的六联张图卡，涵盖封面、框选截图、整屏保存、当前窗口、剪贴板历史与快捷键对照表。
这套方案的关键是将视觉资产拆分为**代码排版层**与素材层：Bot 负责查阅官方资料，编写规范的 SVG 矢量排版代码与配套文案，同时在云电脑上直接输出无损 PNG 成图，并生成一个 HTML 画廊供创作者直观验收。

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
生成 SVG 矢量代码和借助云电脑渲染 PNG 图卡属于轻量级纯文本与无头浏览器操作，不涉及第三方生图 API 扣费，完全受控于 Cursor 套餐自带的周用量【官方】（https://cursor.com/help/grok-bot/plans ）。社区创作者实测表明，制作一套 6 张高清图卡仅需数次轮次的上下文交互，额度消耗极低【社区】（https://immilesma.com/blog/grok-bot-practical-guide/ ）。
成本实测状态：【实测·TODO待实测】测定 6 张 1080×1440 知识图卡从 SVG 生成到 PNG 导出全流程消耗的周额度。

#### 坑
第一个坑是画幅比例错误。小红书移动端的标准展示比例是 3:4（即 1080×1440 像素），许多新手让 Bot 产出图片时未限定分辨率，默认生成 16:9 或 1:1，导致发布后关键内容被平台截断。必须在提示词中将 1080×1440 像素作为硬指标写死。
第二个坑是让图像模型直接画文字。大模型生成图像时的字符渲染机制不同于字体排版，画面中的文字必定变成错别字或不可读字符。解决办法是让图像模型仅负责无字纯背景或插图，所有文字和排版一律由 SVG 或 HTML Canvas 代码通过绝对坐标叠加【社区】（https://chunduai.com/tutorials/grok-bot-code-video ）。
第三个坑是伪造透明背景的假 PNG 与假截图。觉醒AI 踩过的典型坑是 Bot 直接输出了一张带棋盘格背景的所谓透明图，拼合后画面粗糙不堪【社区】（https://www.jxxy.net/ai/articles/grok-bot-xiaohongshu-team-workflow/ ）。对于软件教程类配图，必须由创作者提供真实截图或由 Bot 在云电脑浏览器中截取真实页面，坚决不用 AI 臆造的虚拟软件界面。
第四个坑是严禁脚本自动发帖。由于国内平台具备严格的设备指纹与风控检测，任何利用云电脑脚本在网页端模拟发布笔记的行为都会招致账号降权甚至限流。必须将最终的图片与文案导出至本地，在官方手机客户端进行人工复核与发布【社区】（https://xiangyugongzuoliu.com/grokbot-use-cases/ ）。

> [!NOTE]
> 📸 **截图位（待补）**：生成的 6 张 1080×1440 小红书知识图卡预览画廊与 SVG 源文件
![小红书知识图卡的分层架构：底层代码绘制、中层文字排版与顶层人工审核发布](../../images/fig-15-5.png)

*图：小红书知识图卡的分层架构：底层代码绘制、中层文字排版与顶层人工审核发布*

---

[← 上一章：§14 个人与生活 · Personal & Daily Life](../part5-use-cases/14-personal.md) ｜ [📖 返回目录](../../README.md#-目录) ｜ [下一章：§16 赚钱与工作 · Work & Business →](../part5-use-cases/16-business.md)

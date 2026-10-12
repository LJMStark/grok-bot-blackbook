#!/usr/bin/env python3
"""从 /workspace/grok-bot-blackbook/chapters 生成 docs/ 分章、book/ 全书单文件、docsify 侧栏。只做格式与导航，不改正文。"""
import re, os, json
SRC = '/workspace/grok-bot-blackbook/chapters'
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = [
 ('part0-preface', '封面与前言', [('00-cover-preface','00-preface')]),
 ('part1-getting-started', 'Part 1 起步 · Getting Started', [('01-what-it-is','01-what-it-is'),('02-access','02-access'),('03-install','03-install'),('04-first-task','04-first-task')]),
 ('part2-core-concepts', 'Part 2 核心概念 · Core Concepts', [('05-bots','05-bots'),('06-computer','06-computer'),('07-skills-routines','07-skills-routines'),('08-approvals-safety','08-approvals-safety')]),
 ('part3-integrations', 'Part 3 扩展与集成 · Integrations', [('09-connectors','09-connectors'),('10-partners','10-partners'),('11-china-integrations','11-china-integrations')]),
 ('part4-multi-bot', 'Part 4 多 Bot 协作 · Multi-Bot', [('12-groups','12-groups'),('13-blueprints','13-blueprints')]),
 ('part5-use-cases', 'Part 5 热门用例 · Use Cases', [('14-personal','14-personal'),('15-creators','15-creators'),('16-business','16-business')]),
 ('part6-capstones', 'Part 6 完整落地项目 · Capstones', [('17-capstone-a','17-capstone-a'),('18-capstone-b','18-capstone-b')]),
 ('part7-saving', 'Part 7 省钱 · Usage & Saving', [('19-usage','19-usage'),('20-saving','20-saving')]),
 ('part8-pitfalls', 'Part 8 避坑与事故 · Pitfalls', [('21-incidents','21-incidents'),('22-troubleshooting','22-troubleshooting'),('23-antipatterns','23-antipatterns')]),
 ('part9-mental-models', 'Part 9 心智模型 · Mental Models', [('24-mental-models','24-mental-models')]),
 ('appendix', '附录 · Appendices', [('A1-appendix','A1-appendix'),('A2-appendix','A2-appendix'),(None,'99-contact')]),
]
H1_FIX = {'A1-appendix': '# 附录 A–E · 速查、价格、模板、连接器、更新日志', 'A2-appendix': '# 附录 F–J · FAQ、术语、竞品、资源、来源总表与勘误'}

def transform(name, text):
    L = text.split('\n'); out = []; fence = False
    if name in H1_FIX and L[0].startswith('# '): L[0] = H1_FIX[name]
    for l in L:
        if l.startswith('```'): fence = not fence; out.append(l); continue
        if fence: out.append(l); continue
        l = l.replace('](figures/', '](../../images/')
        m = re.match(r'^>\s*📸\s*截图[:：]\s*(.*)$', l)
        if m:
            out += ['> [!NOTE]', f'> 📸 **截图位（待补）**：{m.group(1)}']; continue
        if l.startswith('【实测·TODO待实测'):
            out += ['> [!TIP]', f'> 🧪 {l}']; continue
        out.append(l)
    s = '\n'.join(out).rstrip() + '\n'
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s

def title_of(s): return s.split('\n',1)[0].lstrip('# ').strip()

chapters = []  # (folder, slug, text)
for folder, ptitle, items in PARTS:
    os.makedirs(f'{R}/docs/{folder}', exist_ok=True)
    for src, slug in items:
        if src is None: t = open(f'{R}/tools/contact.md').read()
        else: t = transform(src, open(f'{SRC}/{src}.md').read())
        chapters.append((folder, slug, t, ptitle))

def link(i):
    f, s, t, _ = chapters[i]; return f'../{f}/{s}.md', title_of(t)

for i, (f, s, t, _) in enumerate(chapters):
    nav = ['[📖 返回目录](../../README.md#-目录)']
    if i > 0: p, pt = link(i-1); nav.insert(0, f'[← 上一章：{pt}]({p})')
    if i < len(chapters)-1: n, nt = link(i+1); nav.append(f'[下一章：{nt} →]({n})')
    bar = ' ｜ '.join(nav)
    h1, rest = t.split('\n', 1)
    body = f'{h1}\n\n{bar}\n\n---\n{rest.rstrip()}\n\n---\n\n{bar}\n'
    open(f'{R}/docs/{f}/{s}.md', 'w').write(body)

# 全书单文件（book/ 下，图片路径 ../images/）
full = []
for f, s, t, _ in chapters:
    full.append(t.replace('](../../images/', '](../images/'))
open(f'{R}/book/blackbook-full.md', 'w').write('\n\n'.join(full))

# docsify 侧栏
side = ['- [首页](/)', '- [精选资料库](resources/README.md)']
for folder, ptitle, items in PARTS:
    side.append(f'- **{ptitle}**')
    for f, s, t, _ in chapters:
        if f == folder: side.append(f'  - [{title_of(t)}](docs/{f}/{s}.md)')
open(f'{R}/_sidebar.md', 'w').write('\n'.join(side) + '\n')
json.dump([(f, s, title_of(t), p) for f, s, t, p in chapters], open(f'{R}/tools/toc.json', 'w'), ensure_ascii=False, indent=1)
print(len(chapters), 'chapters')

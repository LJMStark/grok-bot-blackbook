#!/usr/bin/env python3
"""book/blackbook-full.md -> pdf/grok-bot-blackbook.pdf（Chrome headless，Noto CJK，带书签与目录）"""
import markdown, re, json, os, subprocess, glob
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = '/tmp/pdfbuild'; os.makedirs(f'{B}/img', exist_ok=True)
for f in glob.glob(f'{R}/images/*.png'):
    o = f'{B}/img/' + os.path.basename(f)[:-4] + '.jpg'
    if not os.path.exists(o):
        im = Image.open(f).convert('RGB'); im.thumbnail((1600, 1600)); im.save(o, quality=82)
md = open(f'{R}/book/blackbook-full.md').read()
md = md.replace('![读者交流群二维码](../images/contact-qr.png)', '')
md = re.sub(r'\]\(\.\./images/([^)]+)\.png\)', r'](img/\1.jpg)', md)
# 章节内互链在 PDF 中无意义，保留文字
md = re.sub(r'\]\(\.\./docs/[^)]*\)', ']()', md)
ext = ['tables', 'fenced_code', 'toc', 'sane_lists', 'attr_list']
html = markdown.markdown(md, extensions=ext, extension_configs={'toc': {'slugify': lambda v, s: 'h-' + str(abs(hash(v)) % 10**10)}})
# GitHub alerts -> 样式块
html = re.sub(r'<blockquote>\s*<p>\[!(NOTE|TIP|WARNING)\]\s*', lambda m: f'<blockquote class="alert {m.group(1).lower()}"><p>', html)
# 章节分页 + 目录
toc = []
def h1(m):
    i = len(toc); toc.append(re.sub('<[^>]+>', '', m.group(2))); return f'<h1 id="ch{i}"{m.group(1)}>{m.group(2)}</h1>'
html = re.sub(r'<h1 id="[^"]*"([^>]*)>(.*?)</h1>', h1, html)
tochtml = '<section class="toc"><h2 class="toct">目录</h2><ol>' + ''.join(f'<li><a href="#ch{i}">{t}</a></li>' for i, t in enumerate(toc) if i > 0) + '</ol></section>'
cover = '<section class="cover"><img src="img/cover.jpg"></section>'
css = '''@page{size:A4;margin:18mm 16mm 18mm 16mm}
body{font-family:"Noto Serif CJK SC","Noto Sans CJK SC",serif;font-size:10.5pt;line-height:1.75;color:#1a1a1a}
h1,h2,h3,h4{font-family:"Noto Sans CJK SC",sans-serif;line-height:1.35}
h1{page-break-before:always;font-size:22pt;border-bottom:3px solid #f26b1d;padding-bottom:6px}
h2{font-size:15pt;margin-top:1.4em;border-left:5px solid #f26b1d;padding-left:8px}
h3{font-size:12.5pt}h4{font-size:11pt}
a{color:#b4470c;text-decoration:none;word-break:break-all}
img{max-width:100%;max-height:200mm;display:block;margin:8px auto;page-break-inside:avoid}
p em:only-child{display:block;text-align:center;color:#666;font-size:9pt}
table{border-collapse:collapse;width:100%;font-size:9pt;margin:8px 0;page-break-inside:auto}
th,td{border:1px solid #ccc;padding:4px 6px;vertical-align:top}th{background:#f4f4f4}
tr{page-break-inside:avoid}
pre{background:#f6f6f6;padding:8px;font-size:8.5pt;white-space:pre-wrap;word-break:break-all;border-radius:4px}
code{font-family:"Noto Sans Mono CJK SC",monospace;font-size:9pt}
blockquote{border-left:4px solid #ddd;margin:8px 0;padding:2px 12px;color:#444;background:#fafafa}
blockquote.note{border-color:#4a90d9;background:#eef5fc}blockquote.tip{border-color:#2e9e5b;background:#eefaf2}
.cover{page-break-after:always;text-align:center}.cover img{max-height:260mm;margin:0 auto}
.toc ol{font-size:10.5pt;line-height:2}.toct{border:none}
'''
open(f'{B}/book.html', 'w').write(f'<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>Grok Bot 黑皮书：从零到一支 AI 团队</title><style>{css}</style></head><body>{cover}{tochtml}{html}</body></html>')
os.makedirs(f'{R}/pdf', exist_ok=True)
out = f'{R}/pdf/grok-bot-blackbook.pdf'
subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer', '--generate-pdf-document-outline', f'--print-to-pdf={out}', f'file://{B}/book.html'], check=True, timeout=600)
print(out, os.path.getsize(out) // 1024, 'KB', len(toc), 'chapters')

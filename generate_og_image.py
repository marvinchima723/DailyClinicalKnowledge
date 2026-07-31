from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1200, 630

# 创建深色渐变背景
img = Image.new('RGB', (WIDTH, HEIGHT), '#0a0a0c')
draw = ImageDraw.Draw(img)

# 绘制渐变背景
for y in range(HEIGHT):
    ratio = y / HEIGHT
    r = int(10 + (22 - 10) * ratio)
    g = int(10 + (24 - 10) * ratio)
    b = int(12 + (40 - 12) * ratio)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

# 添加绿色光晕效果（右上角）
for i in range(20):
    alpha = int(30 - i * 1.2)
    x = WIDTH - 300 + i * 15
    y = -100 + i * 10
    r = 200 + i * 20
    draw.ellipse([x - r, y - r, x + r, y + r], fill=(52, 199, 89, alpha))

# 加载字体
font_path_cn = '/System/Library/Fonts/Hiragino Sans GB.ttc'
font_path_en = '/System/Library/Fonts/HelveticaNeue.ttc'

try:
    font_title = ImageFont.truetype(font_path_en, 96)
    font_subtitle = ImageFont.truetype(font_path_cn, 48)
    font_tag = ImageFont.truetype(font_path_en, 28)
    font_small = ImageFont.truetype(font_path_en, 24)
except Exception as e:
    print(f"Font load error: {e}")
    font_title = ImageFont.load_default()
    font_subtitle = font_title
    font_tag = font_title
    font_small = font_title

# 主标题
title = "Sports Rehab Daily"
bbox = draw.textbbox((0, 0), title, font=font_title)
title_w = bbox[2] - bbox[0]
draw.text(((WIDTH - title_w) // 2, 180), title, fill='#f5f5f7', font=font_title)

# 副标题
subtitle = "运动康复 · 24小时行业动态"
bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
subtitle_w = bbox[2] - bbox[0]
draw.text(((WIDTH - subtitle_w) // 2, 310), subtitle, fill='#a1a1a6', font=font_subtitle)

# 分隔线
line_y = 400
draw.line([(WIDTH//2 - 200, line_y), (WIDTH//2 + 200, line_y)], fill='#38383a', width=2)

# 分类标签
categories = ["🏆 赛事", "🎓 研究", "🏥 临床", "🤖 科技", "💰 融资", "⭐ 明星"]
tag_spacing = 150
start_x = (WIDTH - (len(categories) - 1) * tag_spacing) // 2
for i, tag in enumerate(categories):
    bbox = draw.textbbox((0, 0), tag, font=font_tag)
    tag_w = bbox[2] - bbox[0]
    draw.text((start_x + i * tag_spacing - tag_w // 2, 440), tag, fill='#34c759', font=font_tag)

# 底部小字
footer = "Daily Report · GitHub Pages"
bbox = draw.textbbox((0, 0), footer, font=font_small)
footer_w = bbox[2] - bbox[0]
draw.text(((WIDTH - footer_w) // 2, 560), footer, fill='#6e6e73', font=font_small)

# 保存，控制文件大小
output_path = '/Users/mma/Dropbox/0-临床专家/运动损伤/og-image.png'
img.save(output_path, 'PNG', optimize=True)

file_size = os.path.getsize(output_path)
print(f"Generated: {output_path}")
print(f"Size: {file_size / 1024:.1f} KB")
print(f"Dimensions: {WIDTH}x{HEIGHT}")

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[3]
ASSETS = ROOT / "company" / "workspace" / "outputs" / "final_outputs" / "lp_hp_project" / "ai_starter_lab_lp" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def font(size: int, bold: bool = False):
    candidates = [
        r"C:\Windows\Fonts\YuGothB.ttc" if bold else r"C:\Windows\Fonts\YuGothR.ttc",
        r"C:\Windows\Fonts\meiryob.ttc" if bold else r"C:\Windows\Fonts\meiryo.ttc",
        r"C:\Windows\Fonts\msgothic.ttc",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()


W, H = 960, 720
img = Image.new("RGB", (W, H), "#fbfcf8")
draw = ImageDraw.Draw(img)

for y in range(H):
    r = int(251 - y * 0.03)
    g = int(252 - y * 0.02)
    b = int(248 - y * 0.01)
    draw.line((0, y, W, y), fill=(r, g, b))

for x, y, color in [(120, 120, "#44c7a1"), (790, 130, "#ffc857"), (680, 590, "#ff6b5f")]:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.ellipse((x - 150, y - 150, x + 150, y + 150), fill=color + "55")
    layer = layer.filter(ImageFilter.GaussianBlur(26))
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    draw = ImageDraw.Draw(img)

draw.rounded_rectangle((90, 86, 870, 630), radius=28, fill="#ffffff", outline="#d9e2dc", width=3)
draw.rounded_rectangle((130, 132, 520, 560), radius=22, fill="#17222f")
draw.rounded_rectangle((152, 166, 498, 532), radius=18, fill="#f5fbff")

title_font = font(42, True)
body_font = font(26, False)
small_font = font(21, False)

draw.text((184, 205), "AI Roadmap", font=title_font, fill="#17222f")
cards = [
    ("今日の作業を整理", "#e7f8f2"),
    ("プロンプトを型化", "#fff4cc"),
    ("発信につなげる", "#ffe2df"),
]
for i, (text, fill) in enumerate(cards):
    y = 285 + i * 82
    draw.rounded_rectangle((184, y, 462, y + 52), radius=14, fill=fill)
    draw.text((206, y + 13), text, font=small_font, fill="#17222f")

draw.rounded_rectangle((575, 158, 815, 240), radius=18, fill="#e7f8f2")
draw.text((600, 181), "30日設計", font=body_font, fill="#16745e")
draw.rounded_rectangle((575, 272, 815, 354), radius=18, fill="#fff4cc")
draw.text((600, 295), "個別相談", font=body_font, fill="#8a6500")
draw.rounded_rectangle((575, 386, 815, 468), radius=18, fill="#ffe2df")
draw.text((600, 409), "実務導線", font=body_font, fill="#9d342d")

draw.text((575, 525), "AIを調べるだけで終わらせない。", font=small_font, fill="#425266")
draw.text((575, 558), "仕事・発信・商品作りへ。", font=small_font, fill="#425266")

img.save(ASSETS / "hero-ai-workspace.png")
print(ASSETS / "hero-ai-workspace.png")


from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[3]
ASSETS = ROOT / "company" / "workspace" / "outputs" / "final_outputs" / "lp_hp_project" / "ai_workstyle_audit_lp" / "assets"
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
img = Image.new("RGB", (W, H), "#f8fafc")
draw = ImageDraw.Draw(img)

for x, y, color in [(160, 130, "#2563eb"), (800, 170, "#a3e635"), (660, 590, "#93c5fd")]:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.ellipse((x - 180, y - 180, x + 180, y + 180), fill=color + "55")
    layer = layer.filter(ImageFilter.GaussianBlur(30))
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    draw = ImageDraw.Draw(img)

draw.rounded_rectangle((92, 80, 868, 638), radius=30, fill="#ffffff", outline="#d8e0ea", width=3)

title_font = font(42, True)
body_font = font(24, False)
small_font = font(20, False)

draw.text((140, 125), "AI Workstyle Audit", font=title_font, fill="#101828")
draw.text((142, 180), "業務をAI化しやすい順に整理", font=body_font, fill="#526070")

cols = [
    (142, 250, "すぐ試す", "#dbeafe"),
    (370, 250, "準備する", "#ecfccb"),
    (598, 250, "今はやらない", "#eef2f7"),
]

tasks = {
    "すぐ試す": ["メール返信", "議事録要約", "投稿文下書き"],
    "準備する": ["顧客FAQ", "資料テンプレ", "商品案整理"],
    "今はやらない": ["完全自動化", "複雑な判断", "個人情報処理"],
}

for x, y, title, fill in cols:
    draw.rounded_rectangle((x, y, x + 190, y + 300), radius=18, fill=fill)
    draw.text((x + 22, y + 22), title, font=body_font, fill="#101828")
    for i, item in enumerate(tasks[title]):
        yy = y + 82 + i * 62
        draw.rounded_rectangle((x + 18, yy, x + 172, yy + 42), radius=12, fill="#ffffff")
        draw.text((x + 34, yy + 10), item, font=small_font, fill="#101828")

draw.rounded_rectangle((142, 585, 818, 612), radius=13, fill="#101828")
draw.text((330, 586), "30日ロードマップを作成", font=small_font, fill="#ffffff")

img.save(ASSETS / "audit-hero.png")
print(ASSETS / "audit-hero.png")


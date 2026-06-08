from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "final_outputs" / "lp_hp_project" / "ai_business_diagnosis_lp" / "assets" / "ai-diagnosis-hero.png"


def rounded(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (1200, 900), "#f7fbf8")
    d = ImageDraw.Draw(img)

    rounded(d, (80, 70, 1120, 830), 38, "#ffffff", "#d8e7e1", 4)
    rounded(d, (130, 125, 1070, 250), 28, "#0f766e")
    for x, color in [(170, "#f4b942"), (210, "#e76f51"), (250, "#ffffff")]:
        d.ellipse((x, 165, x + 28, 193), fill=color)

    rounded(d, (155, 310, 500, 710), 26, "#e5f2ec", "#b8d8cb", 3)
    rounded(d, (550, 310, 1045, 430), 24, "#fff7e4", "#f0d088", 3)
    rounded(d, (550, 470, 1045, 590), 24, "#eaf1f7", "#bdd0df", 3)
    rounded(d, (550, 630, 1045, 750), 24, "#f8e9e2", "#edc3b5", 3)

    for y in [350, 400, 505, 555, 665, 715]:
        rounded(d, (615, y, 930, y + 18), 9, "#172026")
        rounded(d, (615, y + 34, 980, y + 48), 7, "#8aa09a")

    d.line((510, 510, 550, 370), fill="#0f766e", width=8)
    d.line((510, 510, 550, 530), fill="#0f766e", width=8)
    d.line((510, 510, 550, 690), fill="#0f766e", width=8)
    d.ellipse((462, 462, 558, 558), fill="#0f766e")
    d.ellipse((490, 490, 530, 530), fill="#ffffff")

    rounded(d, (205, 375, 450, 420), 16, "#ffffff")
    rounded(d, (205, 455, 450, 500), 16, "#ffffff")
    rounded(d, (205, 535, 450, 580), 16, "#ffffff")
    rounded(d, (205, 615, 390, 660), 16, "#f4b942")

    img.save(OUT, optimize=True)


if __name__ == "__main__":
    main()

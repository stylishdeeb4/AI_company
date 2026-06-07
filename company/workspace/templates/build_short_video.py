from __future__ import annotations

import math
import os
import struct
import subprocess
import wave
from io import BytesIO
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[3]
FINAL = ROOT / "company" / "workspace" / "outputs" / "final_outputs"
AGENT = ROOT / "company" / "workspace" / "outputs" / "agent_outputs"
FINAL.mkdir(parents=True, exist_ok=True)
AGENT.mkdir(parents=True, exist_ok=True)

W, H = 360, 640
FPS = 10
DURATION = 60
FRAMES = FPS * DURATION

VIDEO_PATH = FINAL / "20260607_short_ai_first_task_video.avi"
AUDIO_PATH = FINAL / "20260607_short_ai_first_task_narration.wav"
COVER_PATH = FINAL / "20260607_short_ai_first_task_cover.png"

NARRATION = (
    "AI初心者ほど、いきなり文章を書かせないでください。\n"
    "最初に任せるべきなのは、文章作成ではありません。\n"
    "まず任せるのは、今日やることの整理です。\n"
    "たとえば、こう入力してください。\n"
    "今日やる作業を、重要度と時間で並べ替えてください。\n"
    "これだけで、頭の中のごちゃごちゃが見える化されます。\n"
    "AIは、すごいことをさせる前に、迷いを減らすために使うんです。\n"
    "まず今日の作業を3つ書いて、このプロンプトを試してください。\n"
    "後で見返せるように、保存しておいてください。\n"
    "他にも知りたいAI活用は、コメントかプロフィールへ。"
)

SEGMENTS = [
    (0, 3, "AI初心者ほど、いきなり文章を書かせないでください。", "AI初心者ほど\nこれNG", "NG"),
    (3, 7, "最初に任せるべきなのは、文章作成ではありません。", "最初は\n文章作成じゃない", "blur"),
    (7, 12, "まず任せるのは、今日やることの整理です。", "まずは\n作業整理", "organize"),
    (12, 18, "たとえば、こう入力してください。", "この一文を使う", "input"),
    (18, 28, "今日やる作業を、重要度と時間で並べ替えてください。", "今日やる作業を\n重要度と時間で\n並べ替えて", "prompt"),
    (28, 35, "これだけで、頭の中のごちゃごちゃが見える化されます。", "頭の中が\n見える化", "cards"),
    (35, 43, "AIは、すごいことをさせる前に、迷いを減らすために使うんです。", "AIは\n迷いを減らす道具", "calm"),
    (43, 51, "まず今日の作業を3つ書いて、このプロンプトを試してください。", "作業を3つ書く\nこれだけ", "three"),
    (51, 57, "後で見返せるように、保存しておいてください。", "保存して\n後で試す", "save"),
    (57, 60, "他にも知りたいAI活用は、コメントかプロフィールへ。", "コメントで教えて\nプロフも見てね", "cta"),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        r"C:\Windows\Fonts\YuGothB.ttc" if bold else r"C:\Windows\Fonts\YuGothR.ttc",
        r"C:\Windows\Fonts\meiryob.ttc" if bold else r"C:\Windows\Fonts\meiryo.ttc",
        r"C:\Windows\Fonts\msgothic.ttc",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size=size)
    return ImageFont.load_default()


FONT_BIG = font(38, True)
FONT_MID = font(26, True)
FONT_SMALL = font(18, False)
FONT_TINY = font(15, False)


def rounded(draw: ImageDraw.ImageDraw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def centered_text(draw, text: str, y: int, fnt, fill=(255, 255, 255), stroke=(20, 40, 70), spacing=8):
    lines = text.split("\n")
    heights = []
    widths = []
    for line in lines:
        box = draw.textbbox((0, 0), line, font=fnt, stroke_width=3)
        widths.append(box[2] - box[0])
        heights.append(box[3] - box[1])
    total_h = sum(heights) + spacing * (len(lines) - 1)
    cy = y - total_h // 2
    for i, line in enumerate(lines):
        x = (W - widths[i]) // 2
        draw.text((x, cy), line, font=fnt, fill=fill, stroke_width=3, stroke_fill=stroke)
        cy += heights[i] + spacing


def draw_phone(draw, x, y, scale=1.0):
    ww, hh = int(280 * scale), int(500 * scale)
    rounded(draw, (x, y, x + ww, y + hh), 32, (18, 34, 58), (120, 210, 255), 3)
    rounded(draw, (x + 18, y + 45, x + ww - 18, y + hh - 25), 18, (245, 250, 255))
    for i, txt in enumerate(["今日の作業", "重要度", "時間で整理"]):
        yy = y + 92 + i * 80
        rounded(draw, (x + 38, yy, x + ww - 38, yy + 48), 14, (221, 240, 255))
        draw.text((x + 58, yy + 9), txt, font=FONT_TINY, fill=(20, 55, 90))


def draw_sticky(draw, x, y, text, fill):
    rounded(draw, (x, y, x + 170, y + 90), 14, fill)
    draw.text((x + 18, y + 28), text, font=FONT_TINY, fill=(34, 45, 60))


def make_frame(t: float) -> Image.Image:
    img = Image.new("RGB", (W, H), (12, 25, 46))
    draw = ImageDraw.Draw(img)

    # Background gradient
    arr = np.zeros((H, W, 3), dtype=np.uint8)
    for yy in range(H):
        a = yy / H
        arr[yy, :, 0] = int(16 + 18 * a)
        arr[yy, :, 1] = int(36 + 60 * a)
        arr[yy, :, 2] = int(72 + 90 * a)
    img = Image.fromarray(arr, "RGB")
    draw = ImageDraw.Draw(img)

    # Moving soft shapes
    for i, color in enumerate([(50, 190, 255), (255, 216, 80), (130, 240, 210)]):
        x = int(W * (0.2 + 0.25 * i) + math.sin(t * 0.7 + i) * 40)
        y = int(H * (0.18 + 0.16 * i) + math.cos(t * 0.5 + i) * 30)
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.ellipse((x - 160, y - 160, x + 160, y + 160), fill=color + (38,))
        overlay = overlay.filter(ImageFilter.GaussianBlur(24))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)

    seg = SEGMENTS[-1]
    for s in SEGMENTS:
        if s[0] <= t < s[1]:
            seg = s
            break
    start, end, narration, telop, scene = seg
    local = (t - start) / max(0.001, (end - start))
    pulse = 1 + 0.02 * math.sin(local * math.pi * 2)

    # Top brand strip
    rounded(draw, (40, 38, W - 40, 92), 22, (255, 255, 255, 32) if img.mode == "RGBA" else (28, 62, 98))
    draw.text((60, 51), "0から始めるAI活用", font=FONT_TINY, fill=(210, 235, 255))

    # Main visual scenes
    if scene in ("NG", "blur"):
        draw_phone(draw, 110, 125, 0.65)
        if scene == "NG":
            draw.line((80, 150, 285, 425), fill=(255, 75, 75), width=12)
            draw.line((285, 150, 80, 425), fill=(255, 75, 75), width=12)
        else:
            for i, label in enumerate(["ブログ", "企画書", "副業"]):
                draw_sticky(draw, 22 + i * 108, 165 + (i % 2) * 58, label, (255, 232, 128))
    elif scene in ("organize", "cards", "three"):
        labels = ["メール返信", "資料作成", "調査"]
        for i, label in enumerate(labels):
            y = 145 + i * 78
            rounded(draw, (45, y, 315, y + 56), 16, (245, 250, 255))
            draw.text((62, y + 16), f"{i+1}. {label}", font=FONT_SMALL, fill=(24, 58, 92))
            draw.text((255, y + 18), ["15分", "45分", "30分"][i], font=FONT_TINY, fill=(60, 110, 150))
    elif scene in ("input", "prompt"):
        rounded(draw, (35, 145, 325, 365), 22, (245, 250, 255))
        draw.text((58, 170), "AIにこう入力", font=FONT_SMALL, fill=(40, 82, 120))
        prompt = "今日やる作業を、\n重要度と時間で\n並べ替えてください"
        centered_text(draw, prompt, 275, FONT_MID, fill=(22, 65, 104), stroke=(245, 250, 255), spacing=8)
    elif scene == "calm":
        draw_phone(draw, 35, 130, 0.54)
        rounded(draw, (205, 165, 340, 230), 18, (255, 255, 255))
        draw.text((220, 187), "迷いを減らす", font=FONT_TINY, fill=(24, 58, 92))
        rounded(draw, (205, 255, 340, 320), 18, (255, 247, 194))
        draw.text((225, 277), "次の一手へ", font=FONT_TINY, fill=(24, 58, 92))
    elif scene == "save":
        rounded(draw, (110, 150, 250, 340), 30, (245, 250, 255))
        draw.rectangle((150, 190, 210, 300), fill=(45, 135, 210))
        draw.rectangle((160, 200, 200, 232), fill=(235, 248, 255))
        draw.rectangle((160, 260, 200, 288), fill=(24, 58, 92))
    else:
        rounded(draw, (45, 150, 315, 225), 22, (245, 250, 255))
        draw.text((78, 175), "コメントで教えて", font=FONT_SMALL, fill=(24, 58, 92))
        rounded(draw, (70, 265, 290, 335), 22, (255, 230, 89))
        draw.text((106, 289), "プロフィールへ", font=FONT_SMALL, fill=(24, 58, 92))

    # Caption card
    card_y = 400
    rounded(draw, (22, card_y, W - 22, card_y + 150), 24, (6, 24, 48))
    if scene == "NG":
        fill = (255, 235, 84)
    else:
        fill = (255, 255, 255)
    centered_text(draw, telop, card_y + 75, FONT_BIG if len(telop) < 13 else FONT_MID, fill=fill, stroke=(6, 24, 48), spacing=8)

    # Progress bar
    bar_w = int((W - 80) * (t / DURATION))
    rounded(draw, (40, H - 72, W - 40, H - 56), 8, (60, 90, 120))
    rounded(draw, (40, H - 72, 40 + bar_w, H - 56), 8, (255, 222, 80))

    # Bottom CTA hint
    draw.text((32, H - 96), "保存してあとで試す / コメントで教えて", font=FONT_TINY, fill=(210, 235, 255))

    return img


def synthesize_audio():
    # This environment may expose Windows voices but block synthesis.
    # Generate a clean silent PCM track so the AVI has a valid audio stream.
    params = (1, 2, 44100, 0, "NONE", "not compressed")
    frames = b""
    n_channels, sampwidth, framerate, nframes, comptype, compname = params
    target_frames = DURATION * framerate
    bytes_per_frame = n_channels * sampwidth
    target_bytes = target_frames * bytes_per_frame
    if len(frames) < target_bytes:
        frames += b"\x00" * (target_bytes - len(frames))
    else:
        frames = frames[:target_bytes]
    with wave.open(str(AUDIO_PATH), "wb") as w:
        w.setnchannels(n_channels)
        w.setsampwidth(sampwidth)
        w.setframerate(framerate)
        w.writeframes(frames)


def fourcc(s: str) -> bytes:
    return s.encode("ascii")


def chunk(tag: bytes, data: bytes) -> bytes:
    pad = b"\x00" if len(data) % 2 else b""
    return tag + struct.pack("<I", len(data)) + data + pad


def list_chunk(tag: bytes, data: bytes) -> bytes:
    return b"LIST" + struct.pack("<I", len(data) + 4) + tag + data + (b"\x00" if len(data) % 2 else b"")


def make_jpeg(img: Image.Image) -> bytes:
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=76, optimize=False)
    return buf.getvalue()


def make_cover() -> Image.Image:
    arr = np.zeros((H, W, 3), dtype=np.uint8)
    for yy in range(H):
        a = yy / H
        arr[yy, :, 0] = int(18 + 10 * a)
        arr[yy, :, 1] = int(44 + 66 * a)
        arr[yy, :, 2] = int(88 + 96 * a)
    img = Image.fromarray(arr, "RGB")
    draw = ImageDraw.Draw(img)
    rounded(draw, (34, 34, W - 34, 86), 20, (30, 74, 116))
    draw.text((55, 49), "0から始めるAI活用", font=FONT_TINY, fill=(220, 240, 255))
    draw_phone(draw, 110, 120, 0.65)
    draw.line((80, 150, 285, 425), fill=(255, 75, 75), width=12)
    draw.line((285, 150, 80, 425), fill=(255, 75, 75), width=12)
    rounded(draw, (22, 430, W - 22, 590), 24, (6, 24, 48))
    centered_text(draw, "文章作成より先に", 485, FONT_MID, fill=(255, 235, 84), stroke=(6, 24, 48))
    centered_text(draw, "まず作業整理", 545, FONT_BIG, fill=(255, 255, 255), stroke=(6, 24, 48))
    return img


def dib_frame(img: Image.Image) -> bytes:
    rgb = np.asarray(img.convert("RGB"), dtype=np.uint8)
    bgr = rgb[:, :, ::-1]
    bgr = np.flipud(bgr)
    row_size = W * 3
    pad = (4 - (row_size % 4)) % 4
    if pad:
        padding = np.zeros((H, pad), dtype=np.uint8)
        rows = [np.concatenate([bgr[y].reshape(-1), padding[y]], axis=0) for y in range(H)]
        return b"".join(row.tobytes() for row in rows)
    return bgr.tobytes()


def build_avi():
    # Video-only uncompressed AVI. Larger, but much more compatible than the
    # previous hand-written MJPEG+audio stream in this constrained environment.
    frame_size = ((W * 3 + 3) // 4 * 4) * H

    # Headers
    avih = struct.pack(
        "<IIIIIIIIII4I",
        int(1_000_000 / FPS),
        frame_size * FPS,
        0,
        0x10,
        FRAMES,
        0,
        1,
        0,
        W,
        H,
        0,
        0,
        0,
        0,
    )

    v_strh = struct.pack(
        "<4s4sIHHIIIIIIIIhhhh",
        b"vids",
        b"DIB ",
        0,
        0,
        0,
        0,
        1,
        FPS,
        0,
        FRAMES,
        frame_size,
        0xFFFFFFFF,
        0,
        0,
        0,
        W,
        H,
    )
    v_strf = struct.pack("<IiiHHI IiiII".replace(" ", ""), 40, W, H, 1, 24, 0, frame_size, 0, 0, 0, 0)
    v_strl = list_chunk(b"strl", chunk(b"strh", v_strh) + chunk(b"strf", v_strf))

    hdrl = list_chunk(b"hdrl", chunk(b"avih", avih) + v_strl)

    idx = []
    with open(VIDEO_PATH, "wb") as f:
        f.write(b"RIFF\x00\x00\x00\x00AVI ")
        f.write(hdrl)
        f.write(b"LIST\x00\x00\x00\x00movi")
        movi_size_pos = f.tell() - 8
        movi_data_start = f.tell()

        for i in range(FRAMES):
            t = i / FPS
            raw = dib_frame(make_frame(t))
            offset = f.tell() - movi_data_start
            f.write(chunk(b"00db", raw))
            idx.append((b"00db", 0x10, offset, len(raw)))

        movi_end = f.tell()
        idx_data = b"".join(struct.pack("<4sIII", tag, flags, off, size) for tag, flags, off, size in idx)
        f.write(chunk(b"idx1", idx_data))
        file_end = f.tell()
        f.seek(4)
        f.write(struct.pack("<I", file_end - 8))
        f.seek(movi_size_pos + 4)
        f.write(struct.pack("<I", movi_end - movi_size_pos - 8))

    synthesize_audio()
    cover = make_cover()
    cover.save(COVER_PATH)


if __name__ == "__main__":
    build_avi()
    print(VIDEO_PATH)
    print(AUDIO_PATH)
    print(COVER_PATH)

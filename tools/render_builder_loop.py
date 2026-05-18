from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_GIF = ROOT / "assets" / "builder-loop.gif"
OUT_POSTER = ROOT / "assets" / "builder-loop-poster.png"

WIDTH, HEIGHT = 960, 340
FRAMES = 56
FPS_MS = 80


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


TITLE = font(28, True)
LABEL = font(17, True)
SMALL = font(13)
MONO = font(14)

NODES = [
    ("messy idea", "ambiguous workflow", (112, 142), "#4f7cff"),
    ("product loop", "what happens next", (318, 142), "#13b8a6"),
    ("visible state", "contracts + replay", (532, 142), "#f2a93b"),
    ("shipped proof", "tests + docs + demo", (750, 142), "#f66f61"),
]

CONSOLE_LINES = [
    'prompt  "make this workflow understandable"',
    "state   typed contracts / logs / replay",
    "ship    demo + tests + docs, then tighten",
    "taste   small surface, clear controls",
]


def draw_grid(draw: ImageDraw.ImageDraw) -> None:
    for x in range(0, WIDTH, 32):
        draw.line((x, 0, x, HEIGHT), fill=(26, 41, 63, 13), width=1)
    for y in range(0, HEIGHT, 32):
        draw.line((0, y, WIDTH, y), fill=(26, 41, 63, 13), width=1)


def rounded_card(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=width)


def render_frame(i: int) -> Image.Image:
    phase = (i / FRAMES) * len(NODES)
    active = int(phase) % len(NODES)
    pulse = phase - int(phase)

    image = Image.new("RGB", (WIDTH, HEIGHT), "#f7f9fc")
    draw = ImageDraw.Draw(image)
    draw_grid(draw)

    draw.rounded_rectangle((26, 24, WIDTH - 26, HEIGHT - 24), radius=24, fill="#ffffff", outline="#dce3ee", width=1)
    draw.text((58, 50), "Shehao's builder loop", fill="#121826", font=TITLE)
    draw.text((60, 88), "small systems for messy workflows", fill="#667085", font=SMALL)

    # connector rail
    rail_y = 170
    for idx in range(len(NODES) - 1):
        x1 = NODES[idx][2][0] + 82
        x2 = NODES[idx + 1][2][0] - 8
        draw.line((x1, rail_y, x2, rail_y), fill="#d9e0ea", width=5)
        if idx == active % (len(NODES) - 1):
            px = x1 + (x2 - x1) * pulse
            draw.line((x1, rail_y, px, rail_y), fill=NODES[active][3], width=5)

    for idx, (name, desc, (x, y), color) in enumerate(NODES):
        is_active = idx == active
        box = (x, y, x + 156, y + 94)
        shadow = 8 if is_active else 4
        draw.rounded_rectangle((box[0] + shadow, box[1] + shadow, box[2] + shadow, box[3] + shadow), radius=18, fill="#e8edf5")
        rounded_card(draw, box, "#ffffff", color if is_active else "#dce3ee", 3 if is_active else 1)
        draw.ellipse((x + 18, y + 18, x + 34, y + 34), fill=color)
        draw.text((x + 18, y + 46), name, fill="#121826", font=LABEL)
        draw.text((x + 18, y + 70), desc, fill="#667085", font=SMALL)

    console = (60, 258, 900, 304)
    draw.rounded_rectangle(console, radius=12, fill="#121826")
    draw.ellipse((82, 276, 92, 286), fill="#f66f61")
    draw.ellipse((100, 276, 110, 286), fill="#f2a93b")
    draw.ellipse((118, 276, 128, 286), fill="#13b8a6")
    line = CONSOLE_LINES[active]
    cursor_on = (i // 4) % 2 == 0
    draw.text((150, 272), line + ("  |" if cursor_on else "   "), fill="#eaf2ff", font=MONO)
    return image


def main() -> int:
    frames = [render_frame(i) for i in range(FRAMES)]
    frames[42].save(OUT_POSTER)
    frames[0].save(
        OUT_GIF,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    print(OUT_GIF)
    print(OUT_POSTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

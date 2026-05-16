from pathlib import Path
import shutil
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CAPTURES = ROOT / "assets" / "rpg-demo-latest"
OUT_GIF = ROOT / "assets" / "rpg-demo-profile-loop.gif"
OUT_POSTER = ROOT / "assets" / "rpg-demo-profile-loop-poster.png"
TMP = Path("/private/tmp/rpg-refactor-profile-loop")

WIDTH = 896
HEIGHT = 504
FPS = 8
FRAMES_PER_SCENE = 10
TRANSITION_FRAMES = 3

SCENES = [
    ("home.png", "01 Product entry", "One sentence opens the episode."),
    ("portfolio-top.png", "02 Case-study layer", "The loop is framed as an inspectable AI runtime."),
    ("reviewer.png", "03 Reviewer mode", "A locked demo path makes the product easy to evaluate."),
    ("play-ending-top.png", "04 Runtime inspector", "State, role, choices, inventory, and ending compiler are visible."),
    ("portfolio-advisor.png", "05 Advisor channel", "A side assistant can reason without taking control."),
    ("portfolio-ending.png", "06 Ending compiler", "The run resolves into a reviewable outcome."),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica.ttc",
        "/System/Library/Fonts/SFNS.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


FONT_LABEL = font(18, True)
FONT_SUB = font(16)
FONT_META = font(13, True)


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    ratio = max(target_w / image.width, target_h / image.height)
    resized = image.resize(
        (round(image.width * ratio), round(image.height * ratio)),
        Image.Resampling.LANCZOS,
    )
    left = max(0, (resized.width - target_w) // 2)
    top = max(0, (resized.height - target_h) // 2)
    return resized.crop((left, top, left + target_w, top + target_h))


def rounded_rect(draw: ImageDraw.ImageDraw, xy, radius: int, fill, outline=None, width: int = 1) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def label_width(draw: ImageDraw.ImageDraw, text: str, font_obj: ImageFont.FreeTypeFont) -> int:
    bbox = draw.textbbox((0, 0), text, font=font_obj)
    return bbox[2] - bbox[0]


def load_scene(name: str) -> Image.Image:
    source = CAPTURES / name
    if not source.exists():
        raise FileNotFoundError(source)
    image = Image.open(source).convert("RGB")
    image = cover(image, (WIDTH, HEIGHT))
    return image.filter(ImageFilter.UnsharpMask(radius=1.0, percent=105, threshold=3))


def annotate(image: Image.Image, scene_index: int, label: str, subtitle: str) -> Image.Image:
    frame = image.convert("RGBA")
    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Subtle bottom readability gradient only; the screenshot remains the asset.
    for y in range(HEIGHT - 150, HEIGHT):
        alpha = int(92 * ((y - (HEIGHT - 150)) / 150) ** 1.35)
        draw.line((0, y, WIDTH, y), fill=(0, 0, 0, alpha))

    chip_w = max(370, label_width(draw, subtitle, FONT_SUB) + 52)
    chip_w = min(chip_w, WIDTH - 44)
    chip_h = 78
    chip_x = 22
    chip_y = HEIGHT - chip_h - 20
    rounded_rect(
        draw,
        (chip_x, chip_y, chip_x + chip_w, chip_y + chip_h),
        18,
        (5, 7, 12, 184),
        outline=(255, 255, 255, 44),
        width=1,
    )
    draw.text((chip_x + 22, chip_y + 15), label.upper(), font=FONT_META, fill=(222, 178, 78, 245))
    draw.text((chip_x + 22, chip_y + 39), subtitle, font=FONT_SUB, fill=(245, 240, 230, 230))

    frame.alpha_composite(overlay)
    return frame.convert("RGB")


def blend(a: Image.Image, b: Image.Image, amount: float) -> Image.Image:
    if amount <= 0:
        return a
    if amount >= 1:
        return b
    return Image.blend(a, b, amount)


def main() -> int:
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir(parents=True, exist_ok=True)

    rendered = [
        annotate(load_scene(name), idx, label, subtitle)
        for idx, (name, label, subtitle) in enumerate(SCENES)
    ]

    frame_i = 0
    for idx, scene in enumerate(rendered):
        next_scene = rendered[(idx + 1) % len(rendered)]
        for local in range(FRAMES_PER_SCENE):
            if local >= FRAMES_PER_SCENE - TRANSITION_FRAMES:
                t = (local - (FRAMES_PER_SCENE - TRANSITION_FRAMES) + 1) / (TRANSITION_FRAMES + 1)
                frame = blend(scene, next_scene, t * t * (3 - 2 * t))
            else:
                frame = scene
            frame.save(TMP / f"frame_{frame_i:03d}.png", quality=92)
            frame_i += 1

    rendered[3].save(OUT_POSTER, quality=94)
    palette = TMP / "palette.png"
    run([
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-framerate",
        str(FPS),
        "-i",
        str(TMP / "frame_%03d.png"),
        "-vf",
        f"fps={FPS},palettegen=max_colors=128:reserve_transparent=0",
        str(palette),
    ])
    run([
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-framerate",
        str(FPS),
        "-i",
        str(TMP / "frame_%03d.png"),
        "-i",
        str(palette),
        "-lavfi",
        f"fps={FPS}[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5",
        "-loop",
        "0",
        str(OUT_GIF),
    ])
    print(OUT_GIF)
    print(OUT_POSTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

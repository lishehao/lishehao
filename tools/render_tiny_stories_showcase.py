from pathlib import Path
import shutil
import subprocess
import sys

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "assets" / "tiny-stories-showcase.html"
OUT_GIF = ROOT / "assets" / "tiny-stories-product-loop.gif"
OUT_POSTER = ROOT / "assets" / "tiny-stories-product-loop-poster.png"
TMP = Path("/private/tmp/tiny-stories-profile-frames")
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
WIDTH = 1040
HEIGHT = 650
WINDOW_HEIGHT = 740
FRAMES = 56
FPS = 14


def run(cmd: list[str], quiet: bool = False) -> None:
    subprocess.run(
        cmd,
        check=True,
        stdout=subprocess.DEVNULL if quiet else None,
        stderr=subprocess.DEVNULL if quiet else None,
    )


def main() -> int:
    if not CHROME.exists():
        print(f"Chrome not found: {CHROME}", file=sys.stderr)
        return 1
    if not HTML.exists():
        print(f"HTML not found: {HTML}", file=sys.stderr)
        return 1
    shutil.rmtree(TMP, ignore_errors=True)
    TMP.mkdir(parents=True, exist_ok=True)

    base = HTML.as_uri()
    for i in range(FRAMES):
        frame_path = TMP / f"frame_{i:03d}.png"
        url = f"{base}?frame={i}&total={FRAMES}"
        run([
            str(CHROME),
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=800",
            f"--window-size={WIDTH},{WINDOW_HEIGHT}",
            f"--screenshot={frame_path}",
            url,
        ], quiet=True)
        with Image.open(frame_path) as image:
            image.crop((0, 0, WIDTH, HEIGHT)).save(frame_path)

    shutil.copyfile(TMP / "frame_045.png", OUT_POSTER)
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
        "fps=14,scale=1040:-1:flags=lanczos,palettegen=max_colors=192",
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
        "fps=14,scale=1040:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=4",
        "-loop",
        "0",
        str(OUT_GIF),
    ])
    print(OUT_GIF)
    print(OUT_POSTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

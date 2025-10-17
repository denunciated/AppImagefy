#!/usr/bin/env python3
from pathlib import Path
import sys
import subprocess

app_dir = Path.home() / "AppImages"
app_dir.mkdir(parents=True, exist_ok=True)

apps = [f.name for f in app_dir.iterdir() if f.is_file() and f.suffix.lower() == ".appimage"]

if len(sys.argv) > 1 and sys.argv[1] == "--rofi-mode":
    if not apps:
        print("(no AppImages found)")
    else:
        for a in apps:
            print(a)
    sys.exit(0)

if not apps:
    apps = ["(no AppImages found)"]

# Launch Rofi as dmenu
rofi = subprocess.Popen(
    ["rofi", "-dmenu", "-p", "AppImages:"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

choice, _ = rofi.communicate("\n".join(apps))
choice = choice.strip()

app_path = app_dir / choice
if app_path.is_file() and app_path.suffix.lower() == ".appimage":
    subprocess.Popen(
        [str(app_path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

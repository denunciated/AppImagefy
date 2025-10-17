#!/usr/bin/env python3
from pathlib import Path
import sys
import subprocess
import os

app_dir = Path.home() / "AppImages"
app_dir.mkdir(parents=True, exist_ok=True)

def list_appimages():
    apps = [f.name for f in app_dir.iterdir() if f.is_file() and f.suffix.lower() == ".appimage"]
    if not apps:
        print("(No AppImages found)")
        sys.exit(0)  
    else:
        for app in apps:
            print(app)  

def launch_app(name: str):
    app_path = app_dir / name
    if app_path.is_file() and app_path.suffix.lower() == ".appimage":
        subprocess.Popen(
            [str(app_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
    else:
        print(f"Error: {app_path} is not a valid AppImage", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ("--rofi-mode", "-dmenu"):
        list_appimages()
    elif len(sys.argv) == 2:
        launch_app(sys.argv[1])
    else:
        print("Error: Invalid arguments", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

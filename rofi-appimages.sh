#!/usr/bin/env bash

PYTHON_SCRIPT="$HOME/.config/hypr/UserScripts/appimages.py"

if [ "$1" = "-dmenu" ]; then
    # Run with dmenu
    selected=$(python3 "$PYTHON_SCRIPT" -dmenu | rofi -dmenu)
    [ -n "$selected" ] && python3 "$PYTHON_SCRIPT" "$selected"
else
    if [ -z "$1" ]; then
        # No argument: list AppImages
        python3 "$PYTHON_SCRIPT"
    else
        # Argument provided: launch the selected AppImage
        python3 "$PYTHON_SCRIPT" "$1"
    fi
fi

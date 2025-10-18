#!/usr/bin/env bash

APPS=$(cd ~/AppImages/; ls -1 | grep -i .appimage)
if [ "$1" = "-dmenu" ]; then
    selected=$(echo $APPS  | xargs -n1 echo | rofi -dmenu)
    [ -n "$selected" ] && ~/AppImages/$selected
else
    if [ -z "$1" ];then
        echo $APPS | xargs -n1 echo
    else
       coproc ( ~/AppImages/$1 > /dev/null  2>&1 )
    fi
fi

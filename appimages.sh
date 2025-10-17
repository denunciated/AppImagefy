#!/usr/bin/env bash

APPS=$(cd ~/AppImages/; ls | grep -i .appimage)
if [ "$1" = "-dmenu" ]; then
    selected=$(echo $APPS | rofi -dmenu)
    [ -n "$selected" ] && ~/AppImages/$selected
else
    if [ -z "$1" ];then
        echo $APPS
    else
       coproc ( ~/AppImages/$1 > /dev/null  2>&1 )
    fi
fi 

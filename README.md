# AppImagefy
Maps AppImages to add on Rofi.

## Usage of python script:
1. Add the AppImages on $HOME/AppImages. 
2. Get the .sh script and paste on the $HOME/.config/hypr/scripts
3. Get the .py script and paste on the $HOME/.config/hypr/UserScripts
4. Use the examples below to use the scripts

### Example of adding to your rofi menu
bind = $mainMod, D, exec, pkill rofi; rofi -show drun -modi "drun,filebrowser,󱝑 appimgs:$HOME/.config/hypr/scripts/rofi-appimages.sh,run,window" (from [JaKooLit](https://github.com/JaKooLit/) dots)

### Example of using as standalone
bind = $mainMod ALT, D, exec, $HOME/Github/AppImagefy/rofi-appimages.sh -dmenu (from [JaKooLit](https://github.com/JaKooLit/) dots)

## Usage of .sh script:
1. Get the .sh script and paste on the $HOME/.config/hypr/scripts
2. Use one of the examples below to use the script

### Example of adding to your rofi menu
bind = $mainMod, D, exec, pkill rofi; rofi -show drun -modi "drun,filebrowser,󱝑 appimgs:$HOME/.config/hypr/scripts/appimage.sh,run,window"

### Example of using as standalone
bind = $mainMod ALT, D, exec, $HOME/.config/hypr/scripts/appimage.sh -dmenu

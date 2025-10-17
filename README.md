# AppImagefy
Maps AppImages to add on Rofi.

## Usage:
Add the AppImages on $HOME/AppImages and then add the script to the rofi, you can use it as a standalone with python3 appimagefy.py or add it to your rofi menu.

### Example of adding to your rofi menu
bind = $mainMod, D, exec, pkill rofi; rofi -show drun -modi "drun,filebrowser,AppImages:$HOME/rofi/scripts/appimages.py --rofi-mode,run,window" (from [JaKooLit](https://github.com/JaKooLit/)
 dots)

### Example of using as standalone
bind = $mainMod, D, exec, python $HOME/rofi/scripts/appimages.py

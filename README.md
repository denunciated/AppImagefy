# AppImagefy

A lightweight utility to integrate your AppImages into Rofi, making them easily searchable and launchable from your application launcher.

## Features

- 🚀 Launch AppImages directly from Rofi
- 🔍 Automatically scans your AppImages directory
- 🎨 Integrates seamlessly with Hyprland and Rofi
- 📁 Two implementations available: Python and Shell script

## Prerequisites

- [Rofi](https://github.com/davatorium/rofi) - Application launcher
- AppImages stored in `$HOME/AppImages/`
- (Optional) Hyprland window manager

## Installation

1. **Create the AppImages directory:**
   ```bash
   mkdir -p ~/AppImages
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/denunciated/AppImagefy.git
   cd AppImagefy
   ```

3. **Set up the scripts:**
   
   Choose either the Python or Shell implementation:

   **For Python version:**
   ```bash
   cp rofi-appimages.sh ~/.config/hypr/scripts/
   cp appimages.py ~/.config/hypr/UserScripts/
   chmod +x ~/.config/hypr/scripts/rofi-appimages.sh
   chmod +x ~/.config/hypr/UserScripts/appimages.py
   ```

   **For Shell version:**
   ```bash
   cp appimages.sh ~/.config/hypr/scripts/
   chmod +x ~/.config/hypr/scripts/appimages.sh
   ```

4. **Place your AppImages:**
   Move your `.AppImage` files to `~/AppImages/`

## Usage

### Option 1: Integrated with Rofi Menu

Add AppImages as a custom mode in your Rofi launcher.

**Using Python version:**
```bash
bind = $mainMod, D, exec, pkill rofi; rofi -show drun -modi "drun,filebrowser,󱝑 appimgs:$HOME/.config/hypr/scripts/rofi-appimages.sh,run,window"
```

**Using Shell version:**
```bash
bind = $mainMod, D, exec, pkill rofi; rofi -show drun -modi "drun,filebrowser,󱝑 appimgs:$HOME/.config/hypr/scripts/appimages.sh,run,window"
```

### Option 2: Standalone Launcher

Launch AppImages in a dedicated Rofi menu.

**Using Python version:**
```bash
bind = $mainMod ALT, D, exec, $HOME/.config/hypr/scripts/rofi-appimages.sh -dmenu
```

**Using Shell version:**
```bash
bind = $mainMod ALT, D, exec, $HOME/.config/hypr/scripts/appimages.sh -dmenu
```

## How It Works

1. The script scans `~/AppImages/` for all `.AppImage` files
2. It presents them in a Rofi menu with their filenames
3. When you select an AppImage, it executes it with proper permissions

## Customization

### Change AppImages Directory

Edit the script and modify the directory path:

```bash
# Default location
APPIMAGE_DIR="$HOME/AppImages"

# Change to your preferred location
APPIMAGE_DIR="$HOME/.local/appimages"
```

### Using with Other Window Managers

While the examples show Hyprland configuration, these scripts work with any window manager. Simply bind the script to your preferred keybinding system.

## Troubleshooting

**AppImages not appearing in Rofi:**
- Ensure AppImages are in `~/AppImages/`
- Check that `.AppImage` files have execute permissions: `chmod +x ~/AppImages/*.AppImage`
- Verify the script path in your configuration

**Script not executing:**
- Confirm scripts have execute permissions
- Check that all paths in your config match your actual file locations

## Credits

Configuration examples adapted from [JaKooLit's](https://github.com/JaKooLit/) Hyprland dotfiles.

## License

[WTFPL](LICENSE) - Do What The F*ck You Want To Public License

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/denunciated/AppImagefy/issues).

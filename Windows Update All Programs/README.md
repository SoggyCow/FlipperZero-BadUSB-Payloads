# Winget Auto-Upgrader Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the silent upgrade of all installed applications managed by [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/), the official Windows Package Manager built into Windows 10/11.  
It opens a Command Prompt and runs `winget upgrade --all -h` to quietly upgrade every updatable package (apps, tools, runtimes, etc.) without user interaction or progress output.

Using Flipper Zero’s **BadUSB** feature with DuckyScript, the script opens a standard Command Prompt (no elevation required) and executes the winget upgrade command.

> **Note:** winget must be pre-installed on the target system (it is included by default on Windows 11 and most recent Windows 10 builds). No admin rights are needed for most upgrades, but some packages may still prompt or require elevation.

## Usage Instructions

### 1. Save the Script
- Filename: `winget_auto_upgrade.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > winget_auto_upgrade.txt`
- Ensure USB mode is active
- Connect to the target Windows machine and press **Run**

The script will:
- Open the Run dialog (Win + R)
- Launch a standard Command Prompt
- Execute: winget upgrade --all -h && exit

## Installation Verification / Execution Confirmation

The upgrade runs silently if:
- winget is installed and functional
- An internet connection is available
- The terminal window closes automatically when complete

To verify upgrades occurred:
- Open a new Command Prompt manually
- Run: `winget upgrade`
- If no (or very few) updates are listed, the script successfully processed available upgrades

## Requirements

- **OS**: Windows 10 (1809+) / 11 with winget installed
- **winget**: Must be pre-installed (App Installer from Microsoft Store or via Settings → Optional Features)
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for downloading updates
- **Admin Privileges**: Not required for the script itself (some packages may still elevate)

## Technical Notes

- **No Chocolatey Dependency**: Uses built-in winget instead of Chocolatey
- **No Elevation**: Opens regular cmd (most winget upgrades do not require admin)
- **Silent Mode**: The `-h` (hidden) flag suppresses all output and progress bars
- **Shell**: Uses Command Prompt (cmd) for maximum compatibility
- **Delays**: Adjusted timing (DELAY 900 after opening cmd) to ensure prompt is ready
- **Exit Behavior**: `&& exit` closes the window immediately after completion
- **Testing Recommendation**: Always test in a virtual machine or isolated environment first
- **Security**: Upgrading packages downloads and installs software from official sources — use only in authorized environments

## Disclaimer

This script is provided for educational and research purposes only.  
Use it exclusively on systems you own or have explicit written permission to access.  
The author is not responsible for any misuse, security incidents, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
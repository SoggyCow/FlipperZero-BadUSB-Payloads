# VLC Media Player Installation Script for Flipper Zero

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of [VLC Media Player](https://www.videolan.org/vlc/), a lightweight, open-source multimedia platform, via [Chocolatey](https://chocolatey.org/) on Windows systems. Using Flipper Zero’s **BadUSB** feature with DuckyScript, it simulates keystrokes to open an elevated Command Prompt and silently install VLC.

> Note: Chocolatey must be pre-installed. Run the Chocolatey setup script first if needed.

## Usage Instructions

### 1. Prepare the Script
- Save as: `install_vlc.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Execute on Host Machine
- On Flipper: Navigate to `Main Menu > Bad USB > install_vlc.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install vlc -y`.

## Installation Verification

VLC installs silently if:
- Chocolatey is installed.
- An internet connection is active.
- Administrative privileges are granted.

## Requirements

- **OS**: Windows 10/11
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Needed for elevated Command Prompt
- **System Compatibility**: Lightweight, compatible with VLC requirements

## Technical Notes

- **Chocolatey Dependency**: Requires Chocolatey to be pre-installed.
- **Elevation**: Uses elevated Command Prompt; may trigger a UAC prompt.
- **Silent Install**: The `-y` flag suppresses prompts.
- **Shell**: Uses Command Prompt for compatibility.
- **Delays**: Includes `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Adjust for slower systems (e.g., `DELAY 700+`).
- **Version**: Installs the latest stable VLC release (e.g., 3.x as of October 2025). See [Chocolatey Package Page](https://community.chocolatey.org/packages/vlc).
- **Testing**: Validate in a virtual machine or sandbox before deployment.

## Disclaimer

This script is for educational purposes only. Use only on systems you own or have explicit permission to modify. The author, SoggyCow, is not liable for misuse or system damage.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
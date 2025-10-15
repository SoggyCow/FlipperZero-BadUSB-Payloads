# WinGet Installation Script for Flipper Zero

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of **WinGet**, Microsoft’s command-line package manager, via [Chocolatey](https://chocolatey.org/) on Windows systems. Using Flipper Zero’s **BadUSB** feature with DuckyScript, it simulates keyboard input to open an elevated Command Prompt, perform a silent installation, and close the terminal.

> Note: Chocolatey must be pre-installed. Run `install_chocolatey.txt` first if needed.

## Usage Instructions

### 1. Save the Payload
- Filename: `install_winget.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper Zero
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Upload to: `SD Card/badusb/`.

### 3. Deploy on Target Machine
- On Flipper: Navigate to `Main Menu > Bad USB > install_winget.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install winget -y && exit`.

## Installation Confirmation

Successful installation requires:
- Chocolatey installed and functional.
- Active internet connection for package download.
- Administrative privileges for elevation.
- Command Prompt compatibility with Chocolatey.

Installs the latest WinGet version (e.g., 1.x as of October 2025). See [Chocolatey Package Page](https://community.chocolatey.org/packages/winget).

## Requirements

- **OS**: Windows 10/11 (WinGet compatible)
- **Chocolatey**: Must be pre-installed
- **Admin Privileges**: Required for elevated command execution
- **Internet Access**: Needed for package download
- **Flipper Zero**: BadUSB mode enabled
- **Command Prompt**: Must support Chocolatey commands

## Technical Notes

- **Delays**: Uses `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Increase for slower systems (e.g., `DELAY 700+`).
- **Silent Install**: The `-y` flag suppresses prompts; `&& exit` closes the terminal.
- **Redundancy**: WinGet may already be installed natively; this script ensures installation or update via Chocolatey.
- **Testing**: Validate in a virtual machine or sandbox before production use.

## Disclaimer

This script is for educational and authorized purposes only. Use only on systems you own or have explicit permission to modify. The author, SoggyCow, is not liable for misuse or damage.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
# Thunderbird Installation Script for Flipper Zero

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of [Mozilla Thunderbird](https://www.thunderbird.net/), a secure open-source email client, via [Chocolatey](https://chocolatey.org/) on Windows systems. Using Flipper Zero’s **BadUSB** feature with DuckyScript, it simulates keyboard input to open an elevated Command Prompt and silently install Thunderbird.

> Note: Chocolatey must be pre-installed. Run `install_chocolatey.txt` first if needed.

## Usage Instructions

### 1. Save the Script
- Filename: `install_thunderbird.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Deploy on Target Machine
- On Flipper: Navigate to `Main Menu > Bad USB > install_thunderbird.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install thunderbird -y`.

## Installation Verification

Thunderbird installs silently if:
- Chocolatey is installed.
- Administrative privileges are granted.
- An internet connection is available.

Verify installation via: [Chocolatey Package Page](https://community.chocolatey.org/packages/thunderbird). Installs the latest stable version (e.g., 115.x+ as of October 2025).

## Requirements

- **OS**: Windows 10/11
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Needed for elevated Command Prompt
- **Command Prompt**: Must support Chocolatey commands

## Technical Notes

- **Elevation**: Uses elevated Command Prompt; may trigger a UAC prompt.
- **Silent Install**: The `-y` flag suppresses prompts.
- **Shell**: Uses Command Prompt for compatibility.
- **Delays**: Includes `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Adjust for slower systems (e.g., `DELAY 700+`).
- **Testing**: Validate in a virtual machine or sandbox before deployment.

## Disclaimer

This script is for educational purposes only. Use only on systems you own or have explicit permission to access. The author, SoggyCow, is not liable for misuse or unintended outcomes.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
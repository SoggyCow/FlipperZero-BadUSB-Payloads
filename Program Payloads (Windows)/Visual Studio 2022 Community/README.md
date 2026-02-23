# Visual Studio 2022 Community Installation Script for Flipper Zero

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of [Visual Studio 2022 Community Edition](https://visualstudio.microsoft.com/vs/community/), a free and powerful IDE, via [Chocolatey](https://chocolatey.org/) on Windows systems. Using Flipper Zero’s **BadUSB** feature with DuckyScript, it opens an elevated Command Prompt and silently installs Visual Studio.

> Note: Chocolatey must be pre-installed, or the script will fail.

## Usage Instructions

### 1. Save the Script
- Filename: `install_visualstudio2022.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_visualstudio2022.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install visualstudio2022community -y`.

## Installation Confirmation

Visual Studio installs silently if:
- Chocolatey is installed.
- Administrative privileges are granted.
- An internet connection is available.
- The system meets Visual Studio’s requirements.

## Requirements

- **OS**: Windows 10/11 (64-bit)
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Needed for elevated Command Prompt
- **System Specs**:
  - Minimum 8 GB RAM
  - 20–50 GB disk space
  - Compatible CPU/GPU (see [Visual Studio Requirements](https://learn.microsoft.com/en-us/visualstudio/releases/2022/system-requirements))

## Technical Notes

- **Chocolatey Dependency**: Requires Chocolatey to be pre-installed.
- **Elevation**: Uses elevated Command Prompt; may trigger a UAC prompt.
- **Silent Install**: The `-y` flag suppresses prompts.
- **Shell**: Uses Command Prompt for stability.
- **Delays**: Includes `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Adjust for slower systems (e.g., `DELAY 700+`).
- **Version**: Installs the latest stable Visual Studio 2022 Community release (e.g., 17.x as of October 2025). See [Chocolatey Package Page](https://community.chocolatey.org/packages/visualstudio2022community).
- **Testing**: Due to the large install size, validate in a virtual machine or sandbox first.

## Disclaimer

This script is provided for educational purposes only. Use only on systems you own or have explicit permission to configure. The author, SoggyCow, is not liable for damage or misuse.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
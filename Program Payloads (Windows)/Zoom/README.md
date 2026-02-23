# Zoom Installation Script for Flipper Zero

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of [Zoom](https://zoom.us/), a widely-used video conferencing application, via [Chocolatey](https://chocolatey.org/) on Windows systems. It uses Flipper Zero’s **BadUSB** feature with DuckyScript to simulate keystrokes, open an elevated Command Prompt, and perform a silent Zoom installation.

> Note: Chocolatey must be pre-installed. Run the Chocolatey installation script first if needed.

## Usage

The script is executed via Flipper Zero’s BadUSB keyboard emulation. Follow these steps:

### 1. Save Script
- Save as `install_zoom.txt` in UTF-8 plain text format.

### 2. Upload to Flipper Zero
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Deploy the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_zoom.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install zoom -y`.

## Installation Verification

Zoom installs silently if:
- Chocolatey is installed.
- An internet connection is available.

## Prerequisites

- **OS**: Windows 10/11
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Needed for elevated Command Prompt

## Technical Notes

- **Chocolatey Dependency**: Requires Chocolatey to be pre-installed.
- **Elevation**: Uses elevated Command Prompt; may trigger a UAC prompt.
- **Silent Install**: The `-y` flag suppresses user prompts.
- **CMD Compatibility**: Uses Command Prompt for broad system support.
- **Delays**: Includes `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Adjust for slower systems (e.g., `DELAY 700+`).
- **Testing**: Validate in a virtual machine or sandbox before deployment.

## Disclaimer

This script is provided for educational purposes only. Use only on systems you own or have explicit permission to access. The author, SoggyCow, is not liable for unintended outcomes or misuse.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
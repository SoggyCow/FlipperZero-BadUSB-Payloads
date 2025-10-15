# mIRC Installation Script for Flipper Zero

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of [mIRC](https://www.mirc.com/), a popular IRC client, via [Chocolatey](https://chocolatey.org/) on Windows systems. It leverages Flipper Zero’s **BadUSB** feature with DuckyScript to open an elevated Command Prompt and perform a silent installation.

> Note: Chocolatey must be pre-installed on the target system. See `install_chocolatey.txt` for setup if needed.

## Usage Guide

### 1. Save the Payload
- Filename: `install_mirc.txt`
- Format: UTF-8 encoded plain text

### 2. Transfer to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Upload to: `SD Card/badusb/`

### 3. Execute on Target Machine
- On Flipper: Navigate to `Main Menu > Bad USB > install_mirc.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and select **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install mirc -y`.

## Post-Install Verification

If Chocolatey is installed and an internet connection is available:
- mIRC installs silently without user interaction.
- Installs the latest stable version (e.g., 7.x as of October 2025).
- Verify via: [Chocolatey Package Page](https://community.chocolatey.org/packages/mirc).

## Requirements

- **OS**: Windows 10/11
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Needed for elevated Command Prompt
- **System Compatibility**: Lightweight, compatible with mIRC requirements

## Payload Notes

- **Admin Privileges**: Required for Chocolatey installation; may trigger a UAC prompt.
- **Silent Install**: The `-y` flag ensures no user prompts.
- **Shell**: Uses CMD for broad compatibility.
- **Delays**: Includes `DELAY 1000`, `500`, and `1500` ms. Increase (e.g., `700+` ms) for slower systems.
- **Failure Modes**:
  - No Chocolatey: Script aborts.
  - No internet: Download fails.
  - UAC blocked: Elevation fails.
- **Testing**: Validate in a virtual machine before physical deployment.

## Disclaimer

This script is for educational purposes only. Use responsibly on systems you own or have explicit permission to access. The author is not liable for improper use or outcomes.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
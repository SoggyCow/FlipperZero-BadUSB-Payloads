# Wireshark Installation Script for Flipper Zero

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of [Wireshark](https://www.wireshark.org/), a powerful network protocol analyzer, via [Chocolatey](https://chocolatey.org/) on Windows systems. Using Flipper Zero’s **BadUSB** feature with DuckyScript, it opens an elevated Command Prompt and silently installs Wireshark.

> Note: Chocolatey must be pre-installed on the target system.

## Usage Instructions

### 1. Save the Script
- Filename: `install_wireshark.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_wireshark.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install wireshark -y`.

## Installation Verification

Wireshark installs silently if:
- Chocolatey is installed.
- Administrative privileges are available.
- An internet connection is active.

## Prerequisites

- **OS**: Windows 10/11
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Needed for elevated Command Prompt
- **Hardware**: Compatible with Wireshark requirements (RAM, NIC, etc.)

## Technical Notes

- **Chocolatey Dependency**: Requires Chocolatey to be pre-installed.
- **Elevation**: Uses elevated Command Prompt; may trigger a UAC prompt.
- **Silent Install**: The `-y` flag suppresses installer prompts.
- **Shell**: Uses Command Prompt for broad compatibility.
- **Delays**: Includes `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Adjust for slower systems (e.g., `DELAY 700+`).
- **Version**: Installs the latest Wireshark version (e.g., 4.x as of October 2025). See [Chocolatey Package Page](https://community.chocolatey.org/packages/wireshark).
- **Testing**: Validate in a virtual machine or sandbox before deployment.

## Disclaimer

This script is provided for educational purposes only. Use only on systems you own or have explicit permission to configure. The author, SoggyCow, is not liable for misuse or system impact.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
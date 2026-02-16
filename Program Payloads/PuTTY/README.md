# PuTTY Installation Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the installation of [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), the most popular free, open-source SSH and telnet client for Windows.  
PuTTY provides secure remote terminal access (SSH, Telnet, Rlogin, Raw), SFTP/SCP file transfer via its companion tool PSCP, key generation (PuTTYgen), tunneling/port forwarding, saved sessions, serial console support, and is widely used by system administrators, developers, network engineers, and anyone needing terminal access to Linux/Unix servers, routers, embedded devices, or cloud instances.

Using Flipper Zero’s **BadUSB** feature with DuckyScript, the script opens an elevated Command Prompt and silently installs PuTTY (including full integration with Windows context menus and file associations) via [Chocolatey](https://chocolatey.org/).

> **Note:** Chocolatey must be pre-installed on the target system. If it is not, run a Chocolatey installation payload first.

## Usage Instructions

### 1. Save the Script
- Filename: `install_putty.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_putty.txt`
- Ensure USB mode is active
- Connect to the target Windows machine and press **Run**

The script will:
- Open the Run dialog (Win + R)
- Launch an elevated Command Prompt (cmd with CTRL + SHIFT + ENTER)
- Execute: choco install putty.install -y && exit

## Installation Verification

PuTTY installs silently if:
- Chocolatey is already installed
- Administrative privileges are granted (UAC prompt accepted)
- An internet connection is available

After installation:
- Look for “PuTTY” in the Start menu
- Or check the installation path (typically `C:\Program Files\PuTTY`)
- Launch PuTTY to confirm the configuration window opens
- Right-click any .ppk file or use context menu on folders to verify shell integration

## Requirements

- **OS**: Windows 10 / 11
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for Chocolatey package download
- **Admin Privileges**: Required for elevated Command Prompt

## Technical Notes

- **Chocolatey Dependency**: The script assumes Chocolatey is already present
- **Elevation**: Opens an elevated cmd.exe (may show UAC prompt)
- **Silent Install**: Uses -y to suppress all prompts
- **Shell**: Uses Command Prompt (cmd) for broad compatibility
- **Package Choice**: Uses `putty.install` (recommended package that adds file associations, context menus, and full Windows integration)
- **Delays**: Standard timing (DELAY 1000, 500, 1500). Increase if the target system is slow
- **Testing Recommendation**: Always test in a virtual machine or isolated environment first
- **Security**: SSH clients are generally low-risk, but verify SSH key handling and use only in authorized environments

## Disclaimer

This script is provided for educational and research purposes only.  
Use it exclusively on systems you own or have explicit written permission to access.  
The author is not responsible for any misuse, security incidents, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
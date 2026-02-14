# Bitwarden Edge Installation Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the installation of the [Bitwarden Edge extension](https://bitwarden.com/download/) — the official Bitwarden password manager browser extension specifically packaged for Microsoft Edge.  
It provides secure password generation, autofill, vault access, TOTP code generation, secure notes, passkey support, and cross-device sync directly within the Edge browser, with end-to-end encryption and zero-knowledge architecture.

Using Flipper Zero’s **BadUSB** feature with DuckyScript, the script opens an elevated Command Prompt and silently installs the Bitwarden Edge extension via [Chocolatey](https://chocolatey.org/).

> **Note:** Chocolatey must be pre-installed on the target system. If it is not, run a Chocolatey installation payload first.  
> This package installs the Bitwarden extension for Microsoft Edge only.

## Usage Instructions

### 1. Save the Script
- Filename: `install_bitwarden-edge.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_bitwarden-edge.txt`
- Ensure USB mode is active
- Connect to the target Windows machine and press **Run**

The script will:
- Open the Run dialog (Win + R)
- Launch an elevated Command Prompt (cmd with CTRL + SHIFT + ENTER)
- Execute: choco install bitwarden-edge -y && exit

## Installation Verification

Bitwarden Edge installs silently if:
- Chocolatey is already installed
- Administrative privileges are granted (UAC prompt accepted)
- An internet connection is available
- Microsoft Edge is installed on the system

After installation:
- Open Microsoft Edge
- Go to `edge://extensions/` or check the Extensions menu
- Look for “Bitwarden” in the list (should appear enabled)
- Click the Bitwarden icon in the toolbar to confirm it loads and prompts for login/setup

## Requirements

- **OS**: Windows 10 / 11
- **Browser**: Microsoft Edge (Chromium-based)
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for Chocolatey package download
- **Admin Privileges**: Required for elevated Command Prompt

## Technical Notes

- **Chocolatey Dependency**: The script assumes Chocolatey is already present
- **Elevation**: Opens an elevated cmd.exe (may show UAC prompt)
- **Silent Install**: Uses -y to suppress all prompts
- **Shell**: Uses Command Prompt (cmd) for broad compatibility
- **Extension Scope**: Installs only for Edge (use `bitwarden` package for the full desktop app, or other browser-specific packages for Chrome/Firefox)
- **Delays**: Standard timing (DELAY 1000, 500, 1500). Increase if the target system is slow
- **Testing Recommendation**: Always test in a virtual machine or isolated environment first
- **Security**: Browser extensions handle sensitive credential data — verify the installation and use only in authorized environments

## Disclaimer

This script is provided for educational and research purposes only.  
Use it exclusively on systems you own or have explicit written permission to access.  
The author is not responsible for any misuse, security incidents, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
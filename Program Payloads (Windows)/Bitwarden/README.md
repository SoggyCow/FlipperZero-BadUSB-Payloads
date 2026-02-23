# Bitwarden Installation Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the installation of [Bitwarden](https://bitwarden.com/), a free and open-source password manager that securely stores, generates, and autofills passwords, passkeys, TOTP codes, secure notes, credit cards, and identities across devices.  
Bitwarden offers end-to-end encryption, cross-platform sync (desktop, mobile, browser extensions), self-hosting options (via Vaultwarden or official server), zero-knowledge architecture, and premium features like emergency access, 2FA authenticator, and file attachments.

Using Flipper Zero’s **BadUSB** feature with DuckyScript, the script opens an elevated Command Prompt and silently installs the Bitwarden desktop client via [Chocolatey](https://chocolatey.org/).

> **Note:** Chocolatey must be pre-installed on the target system. If it is not, run a Chocolatey installation payload first.

## Usage Instructions

### 1. Save the Script
- Filename: `install_bitwarden.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_bitwarden.txt`
- Ensure USB mode is active
- Connect to the target Windows machine and press **Run**

The script will:
- Open the Run dialog (Win + R)
- Launch an elevated Command Prompt (cmd with CTRL + SHIFT + ENTER)
- Execute: choco install bitwarden -y && exit

## Installation Verification

Bitwarden installs silently if:
- Chocolatey is already installed
- Administrative privileges are granted (UAC prompt accepted)
- An internet connection is available

After installation:
- Look for “Bitwarden” in the Start menu or system tray
- Or check the installation path (typically `C:\Program Files\Bitwarden`)
- Launch Bitwarden to confirm the login/setup window appears

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
- **Delays**: Standard timing (DELAY 1000, 500, 1500). Increase if the target system is slow
- **Testing Recommendation**: Always test in a virtual machine or isolated environment first
- **Security**: Password managers handle sensitive data — verify the installation source and use only in authorized environments

## Disclaimer

This script is provided for educational and research purposes only.  
Use it exclusively on systems you own or have explicit written permission to access.  
The author is not responsible for any misuse, security incidents, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
# NirLauncher Installation Script for Flipper Zero

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of **NirLauncher**, a collection of over 200 portable utilities from NirSoft for diagnostics, password recovery, and network monitoring. It uses Flipper Zero’s **BadUSB** DuckyScript to simulate keyboard input, open an elevated Command Prompt, and perform a silent installation via Chocolatey.

> Note: Chocolatey must be pre-installed on the target system. See `install_chocolatey.txt` for setup if needed.

## Use Case

Ideal for forensic and adversarial workstations requiring lightweight tools for password analysis, system auditing, and utility benchmarking without complex installations.

## Execution Steps

### 1. Save Payload
- File: `install_nirlauncher.txt`
- Encoding: Plain text, UTF-8

### 2. Transfer to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Upload to: `SD Card/badusb/`

### 3. Launch on Target System
- On Flipper: Navigate to `Main Menu > Bad USB > install_nirlauncher.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and select **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install nirlauncher -y`.

## Requirements

- **OS**: Windows 10/11
- **Chocolatey**: Must be pre-installed
- **Admin Privileges**: Required for elevated installation
- **Internet Access**: Needed to download the package
- **CMD Compatibility**: Must support Chocolatey commands
- **System Specs**: Lightweight; refer to NirSoft requirements

## Technical Notes

- **Delays**: Uses `DELAY 1000`, `500`, and `1500` ms. Increase for slower systems (e.g., `700+` ms).
- **Silent Install**: The `-y` flag suppresses user prompts.
- **Elevation**: `CTRL + SHIFT + ENTER` may trigger a UAC prompt.
- **Package**: Installs the latest stable NirLauncher version (e.g., 1.x as of October 2025).
- **Security**: Some NirSoft utilities may trigger antivirus flags. Use ethically and with authorization.
- **Testing**: Test in a virtual machine before deployment.

## Disclaimer

Use this script only on systems you own or have explicit permission to access. Some NirLauncher utilities may raise security or legal concerns if misused. The author is not liable for any misuse or violations.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
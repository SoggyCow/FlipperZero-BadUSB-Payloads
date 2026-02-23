# Chocolatey Installation Script

Author: SoggyCow  
License: MIT

## Overview

This script automates the installation of [Chocolatey](https://chocolatey.org), a package manager for Windows. It serves as a prerequisite for any automation relying on Chocolatey (`choco install`) commands. The script opens an elevated PowerShell session, bypasses the execution policy, downloads the official installer from the Chocolatey community site, executes it, and closes PowerShell.

## Usage

Designed for use with keystroke injection tools like Flipper Zero’s BadUSB feature.

### Steps:
1. **Save the Script**  
   Save as `install_chocolatey.txt` in a format compatible with your device (e.g., UTF-8 plain text).

2. **Load to Device**  
   Transfer the script to your keystroke injection device following its setup instructions.

3. **Deploy the Script**  
   - Connect the device to the target Windows machine.
   - Run the script to:
     - Open PowerShell with administrator privileges.
     - Download and execute the installer from `https://community.chocolatey.org/install.ps1`.
     - Close PowerShell upon completion.

> Note: This script must be run before any `choco install` payloads.

## Prerequisites

- **OS**: Windows 10/11
- **Device**: Keystroke injection tool (e.g., Flipper Zero with BadUSB)
- **Internet Access**: Required to download the installer
- **Admin Privileges**: Needed to adjust execution policy and install Chocolatey

## Important Notes

- **Dependency**: Required for all Chocolatey-based automation scripts.
- **Admin Privileges**: Must run in a user context allowing elevated PowerShell.
- **Source Verification**: Script pulls from `https://community.chocolatey.org/install.ps1`. Verify the source before execution.
- **Delays**: Timing is calibrated for typical systems. Adjust delays for slower or faster machines if needed.

## Disclaimer

This script is provided for educational purposes only. Running scripts with admin privileges or automated downloads carries risks. The author, SoggyCow, is not liable for misuse or adverse outcomes.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
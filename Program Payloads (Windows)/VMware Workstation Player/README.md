# VMware Workstation Player Installation Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the installation of [VMware Workstation Player](https://www.vmware.com/products/workstation-player.html), a free virtualization software from VMware (Broadcom).  
VMware Workstation Player allows users to run multiple operating systems (Windows, Linux, macOS guests, etc.) as virtual machines on a Windows host, with support for snapshots, shared folders, drag-and-drop, USB passthrough, 3D acceleration, and bridged/NAT networking — ideal for testing, development, learning, running legacy software, or isolated environments.

Using Flipper Zero’s **BadUSB** feature with DuckyScript, the script opens an elevated Command Prompt and silently installs VMware Workstation Player via [Chocolatey](https://chocolatey.org/).

> **Note:** Chocolatey must be pre-installed on the target system. If it is not, run a Chocolatey installation payload first.

## Usage Instructions

### 1. Save the Script
- Filename: `install_vmware-workstation-player.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_vmware-workstation-player.txt`
- Ensure USB mode is active
- Connect to the target Windows machine and press **Run**

The script will:
- Open the Run dialog (Win + R)
- Launch an elevated Command Prompt (cmd with CTRL + SHIFT + ENTER)
- Execute: choco install vmware-workstation-player -y && exit

## Installation Verification

VMware Workstation Player installs silently if:
- Chocolatey is already installed
- Administrative privileges are granted (UAC prompt accepted)
- An internet connection is available

After installation:
- Look for “VMware Workstation Player” in the Start menu
- Or check the installation path (typically `C:\Program Files (x86)\VMware\VMware Player`)
- Launch VMware Workstation Player to confirm the main interface opens

## Requirements

- **OS**: Windows 10 / 11 (64-bit recommended)
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for Chocolatey package download
- **Admin Privileges**: Required for elevated Command Prompt
- **Hardware**: CPU with virtualization support (Intel VT-x or AMD-V) enabled in BIOS/UEFI

## Technical Notes

- **Chocolatey Dependency**: The script assumes Chocolatey is already present
- **Elevation**: Opens an elevated cmd.exe (may show UAC prompt)
- **Silent Install**: Uses -y to suppress all prompts
- **Shell**: Uses Command Prompt (cmd) for broad compatibility
- **Delays**: Standard timing (DELAY 1000, 500, 1500). Increase if the target system is slow
- **Testing Recommendation**: Always test in a virtual machine or isolated environment first
- **Security**: Virtualization software requires elevated privileges and can expose the host if VMs are compromised — use only in authorized environments

## Disclaimer

This script is provided for educational and research purposes only.  
Use it exclusively on systems you own or have explicit written permission to access.  
The author is not responsible for any misuse, security incidents, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
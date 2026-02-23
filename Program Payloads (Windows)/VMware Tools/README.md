# VMware Tools Installation Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the installation of [VMware Tools](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-08BB9465-D40A-4E16-9D15-8C6B7D9E0E9E.html), the official suite of utilities and drivers provided by VMware for guest operating systems running inside VMware virtual machines.  
VMware Tools enhances virtual machine performance and management by installing optimized drivers (graphics, network, SCSI), enabling features like better mouse integration, shared folders, drag-and-drop/copy-paste between host and guest, automatic resolution adjustment, time synchronization, graceful shutdown/restart, and heartbeat monitoring.

Using Flipper Zero’s **BadUSB** feature with DuckyScript, the script opens an elevated Command Prompt and silently installs VMware Tools via [Chocolatey](https://chocolatey.org/).

> **Note:** Chocolatey must be pre-installed on the target system. If it is not, run a Chocolatey installation payload first.  
> VMware Tools is typically most useful when installed **inside** a VMware virtual machine guest OS (not on the host).

## Usage Instructions

### 1. Save the Script
- Filename: `install_vmware-tools.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_vmware-tools.txt`
- Ensure USB mode is active
- Connect to the target Windows machine (ideally a VM guest) and press **Run**

The script will:
- Open the Run dialog (Win + R)
- Launch an elevated Command Prompt (cmd with CTRL + SHIFT + ENTER)
- Execute: choco install vmware-tools -y && exit

## Installation Verification

VMware Tools installs silently if:
- Chocolatey is already installed
- Administrative privileges are granted (UAC prompt accepted)
- An internet connection is available

After installation:
- Look for “VMware Tools” in the system tray (icon may appear after reboot)
- Check Programs and Features for “VMware Tools”
- Reboot the guest VM if prompted
- Verify improved performance (smoother mouse, better resolution, shared folders available, etc.)

## Requirements

- **OS**: Windows 10 / 11 (guest OS inside VMware virtual machine)
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for Chocolatey package download
- **Admin Privileges**: Required for elevated Command Prompt
- **Environment**: Best used inside a VMware Workstation/Player/Fusion/ESXi virtual machine

## Technical Notes

- **Chocolatey Dependency**: The script assumes Chocolatey is already present
- **Elevation**: Opens an elevated cmd.exe (may show UAC prompt)
- **Silent Install**: Uses -y to suppress all prompts
- **Shell**: Uses Command Prompt (cmd) for broad compatibility
- **Reboot Recommended**: VMware Tools often requires a reboot for full driver activation
- **Delays**: Standard timing (DELAY 1000, 500, 1500). Increase if the target system is slow
- **Testing Recommendation**: Always test in a virtual machine or isolated environment first
- **Security**: Guest tools improve integration but require elevated privileges inside the VM — use only in authorized environments

## Disclaimer

This script is provided for educational and research purposes only.  
Use it exclusively on systems you own or have explicit written permission to access.  
The author is not responsible for any misuse, security incidents, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
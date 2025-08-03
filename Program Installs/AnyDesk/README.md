# 🛠️ AnyDesk Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT License

---

## 📋 Overview

This script automates the installation of [AnyDesk](https://anydesk.com), a remote desktop software, using [Chocolatey](https://chocolatey.org), a package manager for Windows.  
Designed for use with Flipper Zero’s **BadUSB** feature, it leverages DuckyScript to simulate keyboard input and execute a PowerShell command in a hidden window for silent installation.

> ⚠️ **Important**: Chocolatey must be pre-installed. Run the Chocolatey installation script before using this payload.

---

## 🚀 Usage

This script is intended for use with Flipper Zero's **BadUSB** functionality. Steps:

### 1. Save the Script
Save the DuckyScript as a `.txt` file, e.g., `install_anydesk.txt`.

### 2. Upload to Flipper Zero
- Connect your Flipper Zero via USB or Bluetooth.
- Use the **qFlipper** or **Flipper Mobile** app to transfer the script to:  
  `SD Card/badusb/install_anydesk.txt`

### 3. Run the Script
- On Flipper Zero, navigate to:  
  `Main Menu > Bad USB`
- Select `install_anydesk.txt`.
- Ensure **USB mode** is active (USB logo visible).
- Connect Flipper Zero to a Windows target via USB.
- Press **Run** — the script will:
  - Open the Windows Run dialog.
  - Execute a hidden PowerShell command to silently install AnyDesk via Chocolatey.

### ✅ Verify Installation
AnyDesk will install automatically if Chocolatey is present and the machine has internet access.

---

## 🧰 Prerequisites

- Windows operating system  
- Chocolatey installed (run install script first)  
- Flipper Zero with BadUSB functionality  
- Active internet connection  
- Administrative privileges on target system

---

## ⚠️ Important Notes

- **Chocolatey Dependency**: This script will fail if Chocolatey is not installed.  
- **Admin Privileges**: Required to complete installation.  
- **Silent Installation**: Uses `-y` flag for no prompts.  
- **Hidden Execution**: PowerShell runs in a hidden window (`-W Hidden`) — some antivirus software may detect this as suspicious behavior.  
- **Timing Delays**: Script uses `DELAY 1000`, `DELAY 500`. Adjust values upward for slower systems.  
- **Testing Recommended**: Use a virtual machine or controlled environment when first testing.

---

## ⚖️ Disclaimer

This script is provided **as-is** for educational purposes.  
Use responsibly and **only** on systems you own or are authorized to access.  
The author (**SoggyCow**) is not liable for damage or misuse.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

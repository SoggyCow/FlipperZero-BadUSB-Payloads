# Proton Drive Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## ☁️ Overview

Installs [Proton Drive](https://proton.me/drive), a secure file sync and cloud storage client, using [Chocolatey](https://chocolatey.org/) on Windows.  
Crafted for **Flipper Zero’s BadUSB** with **DuckyScript**, simulating keystrokes to launch elevated **Command Prompt (CMD)** and perform a silent install.

> ⚠️ Chocolatey must already be installed. Refer to `install_chocolatey.txt`.

---

## 🚀 Usage Instructions

### 1. Save Script

- Filename: `install_protondrive.txt`  
- Format: UTF-8 plain text

### 2. Upload to Flipper Zero

- Connect via **USB/Bluetooth**  
- Use **qFlipper** or **Flipper Mobile App**  
- Destination folder: `SD Card/badusb/`

### 3. Execute

- Navigate:  
  `Main Menu > Bad USB > install_protondrive.txt`
- Ensure USB mode is active (USB icon visible)
- Connect Flipper to target Windows system  
- Press **Run**

Actions performed:
- Opens Windows Run dialog  
- Launches elevated CMD (UAC prompt may appear)  
- Executes install command:  
  `choco install protondrive -y`

---

## ✅ Installation Verification

Succeeds if:
- Chocolatey is installed  
- Internet is available  
- `protondrive` package exists  
- Admin privileges are granted

> Check package status: [Chocolatey: Proton Drive](https://community.chocolatey.org/packages/protondrive)

---

## 📋 Requirements

- Windows 10/11  
- Chocolatey pre-installed  
- Flipper Zero w/ BadUSB enabled  
- Internet connection  
- Admin rights  
- Proton Drive system compatibility (generally lightweight)

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Pre-install Chocolatey—see `install_chocolatey.txt`

- **Package Availability:**  
  As of August 2025, `protondrive` may not exist in Chocolatey repo.  
  Confirm before deployment.

- **CMD Shell Preference:**  
  Ensures wide compatibility across systems

- **Silent Install Flag:**  
  `-y` disables prompts

- **Timing Delays:**  
  Default: `DELAY 1000`, `500`, `1500`  
  Adjust for system responsiveness

- **Pre-deployment Testing:**  
  Use VMs or sandbox environments to verify stability

---

## ⚠️ Disclaimer

This script is provided **as-is** for educational purposes.  
Run only on machines you **own or are authorized to access**.  
Author disclaims responsibility for misuse or collateral impact.

---

## 📄 License

Licensed under the **MIT License**  
Refer to the [LICENSE](LICENSE) file

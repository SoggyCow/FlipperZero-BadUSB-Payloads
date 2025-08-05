# Proton Pass Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🔐 Overview

Installs [Proton Pass](https://proton.me/pass), a secure password manager by Proton, via [Chocolatey](https://chocolatey.org/) on Windows.  
Built for **Flipper Zero’s BadUSB** using **DuckyScript**, simulating keystrokes to launch an elevated **Command Prompt** and execute a silent install.

> ⚠️ Chocolatey must be installed beforehand. See `install_chocolatey.txt`.

---

## 🚀 Usage Instructions

### 1. Save Script

- File name: `install_protonpass.txt`  
- Format: UTF-8 plain text

### 2. Upload to Flipper Zero

- Connect via **USB/Bluetooth**  
- Transfer with **qFlipper** or **Flipper Mobile**  
- Destination folder: `SD Card/badusb/`

### 3. Run Script

- Flipper Path:  
  `Main Menu > Bad USB > install_protonpass.txt`  
- Confirm USB mode active (USB icon visible)  
- Plug into target Windows system  
- Press **Run**

Script actions:
- Opens Windows Run dialog  
- Launches elevated CMD (may prompt UAC)  
- Executes install:  
  `choco install protonpass -y`

---

## ✅ Installation Verification

Succeeds if:
- Chocolatey is installed  
- Internet is accessible  
- `protonpass` package is available  
- Admin rights granted

> As of August 2025, package availability may be limited.  
> Check Chocolatey: [Package Page](https://community.chocolatey.org/packages/protonpass)

---

## 📋 Requirements

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero w/ BadUSB enabled  
- Internet access  
- Admin privileges  
- Proton Pass system requirements (low footprint)

---

## ⚙️ Technical Notes

- **Dependency Warning:**  
  Chocolatey must be present—see `install_chocolatey.txt`

- **Package Availability:**  
  Confirm `protonpass` exists on Chocolatey repo

- **Silent Install Flag:**  
  `-y` skips prompts

- **CMD Shell:**  
  Ensures maximum compatibility

- **Timing Delays:**  
  Defaults: `DELAY 1000`, `500`, `1500`  
  Adjust upward for slower machines

- **Testing Environment:**  
  VM/sandbox recommended for verification

---

## ⚠️ Disclaimer

This script is provided **as-is** for educational use only.  
Use only on systems you **own or are authorized to access**.  
The author is not responsible for misuse or any resulting effects.

---

## 📄 License

Licensed under the **MIT License**  
Refer to the [LICENSE](LICENSE) file

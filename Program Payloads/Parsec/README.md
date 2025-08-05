# Parsec Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🎮 Overview

This script automates installation of [Parsec](https://parsec.app/), a low-latency remote desktop and game-streaming tool, via [Chocolatey](https://chocolatey.org/) on Windows.  
Designed for **Flipper Zero’s BadUSB** feature, it uses **DuckyScript** to simulate keystrokes, launch elevated **Command Prompt (CMD)**, and install Parsec silently.

> ⚠️ **Important:** Chocolatey must be installed first. This script will fail if Chocolatey is missing.

---

## 🚀 Usage Instructions

Runs via Flipper Zero’s **BadUSB keyboard emulation**.

### 1. Save the Script

- Save to: `install_parsec.txt`

### 2. Upload to Flipper Zero

- Connect Flipper via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the script to:  
  `SD Card/badusb/`

### 3. Execute the Script

- On Flipper:  
  `Main Menu > Bad USB`
- Select `install_parsec.txt`
- Ensure USB mode is active (USB icon visible)
- Connect Flipper to target Windows machine
- Press **Run**

This triggers:
- Windows Run dialog
- Elevated CMD (may trigger UAC)
- Chocolatey-based silent install of Parsec

---

## ✅ Installation Verification

Parsec installs without user prompts if:
- Chocolatey is present  
- Internet connection is available

---

## 📦 Prerequisites

- Windows OS (Windows 10/11 recommended)  
- Chocolatey installed  
- Flipper Zero with BadUSB enabled  
- Internet access  
- Admin privileges  
- System compatibility (e.g., GPU/RAM suitable for Parsec—see [official requirements](https://parsec.app/support))

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Chocolatey must be pre-installed—run setup script first.

- **Elevation Needed:**  
  CMD launched with admin rights; UAC may trigger.

- **Silent Install:**  
  Uses `-y` flag to suppress prompts

- **CMD Compatibility:**  
  CMD used for maximum support—verify Chocolatey functions in CMD

- **Timing Delays:**  
  Defaults: `DELAY 1000`, `DELAY 500`, `DELAY 1500`. On slower systems, increase to `DELAY 700+`

- **Parsec Version:**  
  Chocolatey installs latest stable version. Check [package page](https://community.chocolatey.org/packages/parsec) for details

- **Testing Environment:**  
  Test in VM or sandbox before deploying live

---

## ⚖️ Disclaimer

This script is provided **as-is** for educational use only.  
Deploy only on systems you **own or are authorized to access**.  
Author (SoggyCow) is **not liable** for misuse or damage.

---

## 📄 License

Licensed under the **MIT License**  
See the [LICENSE](LICENSE) file for terms

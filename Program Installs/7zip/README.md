# 7-Zip Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 📦 Overview

This script installs [7-Zip](https://www.7-zip.org/), a lightweight open-source file archiver, using [Chocolatey](https://chocolatey.org/) on Windows.  
Crafted for **Flipper Zero's BadUSB** feature, it uses **DuckyScript** to emulate keystrokes, elevate to **CMD**, and silently install 7-Zip.

> ⚠️ **Note:** Ensure Chocolatey is pre-installed before using this script.

---

## 🧪 Usage

This script runs via Flipper Zero’s **BadUSB keyboard emulation**.

### 1. Save Script

- Save script to a `.txt` file (e.g., `install_7zip.txt`)

### 2. Upload to Flipper Zero

- Connect via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer file to:  
  `SD Card/badusb/`

### 3. Execute Script

- On Flipper, navigate to:  
  `Main Menu > Bad USB`
- Select `install_7zip.txt`
- Confirm USB mode is active (USB icon visible)
- Connect to target Windows machine
- Press **Run**

The script:
- Opens Windows Run dialog
- Elevates to CMD (UAC may prompt)
- Executes Chocolatey command for silent 7-Zip install

---

## ✅ Verify Installation

7-Zip installs without user prompts if:
- Chocolatey is available
- Internet connection is active

---

## 🔧 Prerequisites

- Windows operating system  
- Chocolatey pre-installed  
- Flipper Zero with BadUSB enabled  
- Internet access  
- Admin rights on target system

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Must be installed first or script will fail.

- **Elevation Required:**  
  CMD runs as administrator; UAC may prompt.

- **Silent Install:**  
  `-y` flag skips confirmation dialogs.

- **CMD Usage:**  
  Selected for system compatibility; verify Chocolatey functions under CMD.

- **Delay Calibration:**  
  Default: `DELAY 1000`, `DELAY 500`, `DELAY 1500`  
  For lag-prone systems, increase (e.g., `DELAY 700`)

- **7-Zip Version:**  
  Installs latest stable (e.g., 24.x as of Aug 2025)  
  Refer to [Chocolatey Package](https://community.chocolatey.org/packages/7zip) for updates

- **Testing:**  
  Validate in VM before deployment

---

## ⚖️ Disclaimer

This script is provided **as-is** for educational purposes.  
Use only on systems you **own or have permission** to access.  
Author (SoggyCow) is **not responsible** for misuse or damage.

---

## 📄 License

Licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full terms.

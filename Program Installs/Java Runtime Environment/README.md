# Java Runtime Environment Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## ☕ Overview

Installs [Java Runtime Environment 8](https://www.java.com/) using [Chocolatey](https://chocolatey.org/) on Windows.  
Designed for **Flipper Zero's BadUSB** feature via **DuckyScript**, launching elevated CMD for silent deployment.

> ⚠️ Requires Chocolatey to be installed before execution.

---

## 🚀 Usage Instructions

### 1. Script Setup

- Save file as: `install_java.txt`

### 2. Transfer to Flipper

- Connect via **USB/Bluetooth**
- Use **qFlipper** or **Flipper Mobile**
- Upload to:  
  `SD Card/badusb/`

### 3. Execute on Host System

- On Flipper: `Main Menu > Bad USB`
- Select script: `install_java.txt`
- Ensure USB mode is active
- Connect to target Windows device
- Tap **Run**

Script performs:
- Opens Windows Run dialog  
- Launches elevated CMD (UAC may prompt)  
- Executes Chocolatey command to install JRE 8 silently

---

## ✅ Installation Confirmation

Java SE installs silently if:
- Chocolatey is present  
- Admin rights are granted  
- Internet is available

---

## 📦 Requirements

- Windows 10 or 11  
- Chocolatey pre-installed  
- Flipper Zero w/ BadUSB enabled  
- Active internet connection  
- Admin privileges  
- System specs compatible with Java Runtime (lightweight footprint)

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:** Required prior to execution  
- **Elevation Handling:** CMD launched with admin rights; UAC may appear  
- **Silent Install:** `-y` flag suppresses prompts  
- **Shell Used:** CMD for broad compatibility  
- **Delay Calibration:**  
  - Defaults: `DELAY 1000`, `500`, `1500`  
  - For slower systems: increase to `DELAY 700+`

- **Version Installed:**  
  Installs JRE (e.g., 8u351 or later as of August 2025)  
  See [Chocolatey Package Page](https://community.chocolatey.org/packages/jre8)

- **Test Environment:** Run in VM or sandbox before live deployment

---

## ⚖️ Disclaimer

Use responsibly and only on systems you **own or have explicit permission to modify**.  
Provided **as-is**—author is **not liable** for unintended consequences.

---

## 📄 License

Licensed under the **MIT License**  
Refer to [LICENSE](LICENSE) for full terms

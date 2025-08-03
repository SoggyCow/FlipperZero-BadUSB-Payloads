# Docker Desktop Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🐳 Overview

This script automates the installation of [Docker Desktop](https://www.docker.com/products/docker-desktop/), a containerized development platform, via [Chocolatey](https://chocolatey.org/) on Windows.  
Built for **Flipper Zero’s BadUSB** functionality, it leverages **DuckyScript** to emulate keystrokes, open an elevated **Command Prompt (CMD)**, and silently install Docker Desktop.

> ⚠️ **Note:** Chocolatey must be installed on the target system prior to running this script.

---

## 🚀 Usage Instructions

Designed for execution via Flipper Zero’s **BadUSB keyboard emulation**.

### 1. Save the Script

- Save to a `.txt` file (e.g., `install_docker.txt`)

### 2. Upload to Flipper Zero

- Connect via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer script to:  
  `SD Card/badusb/`

### 3. Run the Script

- On Flipper:  
  `Main Menu > Bad USB`
- Select `install_docker.txt`
- Confirm USB mode is active
- Connect Flipper to target Windows machine
- Press **Run**

Actions performed:
- Open Windows Run dialog
- Launch elevated CMD (UAC prompt may appear)
- Execute Chocolatey install command for Docker Desktop

---

## ✅ Installation Verification

Docker Desktop installs automatically if:
- Chocolatey is present  
- Internet access is available

---

## 📦 Prerequisites

- Compatible Windows editions:  
  Windows 10/11 Pro, Enterprise, or Education  
  Windows Server 2019/2022

- Chocolatey pre-installed  
- Flipper Zero with BadUSB enabled  
- Active internet connection  
- Admin privileges on target system  
- Docker Desktop system requirements:  
  - WSL 2 or Hyper-V enabled  
  - Minimum 4 GB RAM

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Run the Chocolatey installer first; script fails if missing.

- **Admin Rights Required:**  
  CMD launches with elevation; may trigger UAC.

- **Silent Installation:**  
  `-y` flag skips all user prompts

- **CMD Usage:**  
  CMD used for compatibility—ensure Chocolatey runs properly from CMD

- **Delay Calibration:**  
  Defaults: `DELAY 1000`, `DELAY 500`, `DELAY 1500`  
  For slower systems: increase to `DELAY 700` or higher

- **Docker Requirements:**  
  May require manual enablement of WSL 2 or Hyper-V  
  Check [Chocolatey Docker Package](https://community.chocolatey.org/packages/docker-desktop) for latest version info

- **Testing Environment:**  
  Test in VM with compatible Windows edition before deployment

---

## ⚖️ Disclaimer

This script is provided **as-is** for educational use only.  
Deploy only on systems you **own or have explicit permission** to modify.  
Author (SoggyCow) assumes **no responsibility** for misuse or system issues.

---

## 📄 License

Distributed under the **MIT License**  
See the [LICENSE](LICENSE) file for details.

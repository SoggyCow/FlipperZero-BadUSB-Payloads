# Git Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🗃️ Overview

This script installs [Git](https://git-scm.com/), a widely-used version control system, via [Chocolatey](https://chocolatey.org/) on Windows.  
Designed for **Flipper Zero's BadUSB** feature, it uses **DuckyScript** to emulate keystrokes, open an elevated **Command Prompt (CMD)**, and silently deploy Git.

> ⚠️ **Note:** Chocolatey must be pre-installed. Run the Chocolatey installation script before using this module.

---

## 🚀 Usage

Runs via Flipper Zero's **BadUSB keyboard emulation**.

### 1. Save the Script

- Save to a `.txt` file (e.g., `install_git.txt`)

### 2. Upload to Flipper Zero

- Connect via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer script to:  
  `SD Card/badusb/`

### 3. Execute the Script

- Navigate:  
  `Main Menu > Bad USB`
- Select `install_git.txt`
- Confirm USB mode is active (USB icon displayed)
- Connect Flipper to target Windows device
- Press **Run**

Script will:
- Open Windows Run dialog
- Elevate to Command Prompt (UAC may trigger)
- Run Chocolatey command to silently install Git

---

## ✅ Installation Verification

Git installs silently if:
- Chocolatey is installed  
- Internet connection is active

---

## 📦 Prerequisites

- Windows operating system  
- Chocolatey installed  
- Flipper Zero with BadUSB enabled  
- Active internet connection  
- Admin privileges on target system

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Script will fail if Chocolatey isn’t present.

- **Elevation Required:**  
  CMD is elevated. UAC prompt may appear.

- **Silent Install:**  
  Uses `-y` flag to skip prompts.

- **CMD Compatibility:**  
  CMD selected for broader support; ensure Chocolatey is functional via CMD.

- **Delay Timing:**  
  Default: `DELAY 1000`, `DELAY 500`, `DELAY 1500`. For slower systems, increase to `DELAY 700`.

- **Git Version:**  
  Installs latest stable release (e.g., 2.46.x as of August 2025)  
  See [Chocolatey Git Package](https://community.chocolatey.org/packages/git) for details

- **Environment Safety:**  
  Test in a VM or sandbox first

---

## ⚖️ Disclaimer

This script is provided **as-is** for educational purposes.  
Use only on systems you **own or have permission** to access.  
Author (SoggyCow) assumes **no responsibility** for misuse or consequences.

---

## 📄 License

Licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for terms.

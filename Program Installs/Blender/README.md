# Blender Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧵 Overview

Installs [Blender](https://www.blender.org/), a free and open-source 3D creation suite, using [Chocolatey](https://chocolatey.org/)  
Engineered for **Flipper Zero’s BadUSB** feature via **DuckyScript**—launches elevated CMD and silently installs Blender.

> ⚠️ Requires Chocolatey pre-installation. Run Chocolatey install script first.

---

## 🚀 Usage Guide

### 1. Script Setup

- Save as: `install_blender.txt`

### 2. Upload to Flipper Zero

- Connect via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile**
- Transfer to:  
  `SD Card/badusb/`

### 3. Execution Flow

- On Flipper:  
  `Main Menu > Bad USB`
- Select: `install_blender.txt`
- Confirm USB mode active (USB icon on screen)
- Plug into Windows machine
- Hit **Run**

This will:
- Trigger Windows Run dialog  
- Elevate into CMD (UAC may prompt)  
- Install Blender via Chocolatey silently

---

## ✅ Verification & Outcome

Installs without user interaction if:
- Chocolatey is installed  
- Internet connection available  
- Admin rights granted

---

## 📦 Requirements

- Windows 10 or 11  
- Chocolatey installed  
- Flipper Zero w/ BadUSB  
- Internet access  
- Admin privileges  
- Blender-compatible hardware (GPU, 8GB RAM recommended)

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:** Must be installed beforehand
- **Admin Elevation:** CMD runs as admin—UAC may appear
- **Silent Install:** `-y` flag used for automated deployment
- **Shell Choice:** CMD selected for compatibility
- **Delay Tuning:**  
  Defaults: `DELAY 1000`, `DELAY 500`, `DELAY 1500`  
  For laggy systems: try `DELAY 700+`

- **Package Versioning:**  
  Typically installs latest stable Blender (e.g., 4.x as of August 2025)  
  See [Chocolatey Package Page](https://community.chocolatey.org/packages/blender) for details

- **Testing Recommendations:**  
  Validate in VM/sandbox before use in production environments

---

## ⚖️ Disclaimer

Educational use only.  
Run only on systems you **own or are authorized to control**.  
Author assumes **no responsibility** for script misuse or system impact.

---

## 📄 License

Licensed under the **MIT License**  
See [LICENSE](LICENSE) for terms

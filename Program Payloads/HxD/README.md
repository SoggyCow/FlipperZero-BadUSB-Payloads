# HxD Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🔍 Overview

Installs [HxD](https://mh-nexus.de/en/hxd/), a lightweight and feature-rich hex editor, using [Chocolatey](https://chocolatey.org/).  
Built for **Flipper Zero’s BadUSB**, this DuckyScript payload automates a silent, elevated installation via simulated keystrokes.

> ⚠️ **Chocolatey must be installed prior to executing this script.** See `install_chocolatey.txt`.

---

## 🚀 Deployment Instructions

### 1. Prepare the Script

- Save as: `install_hxd.txt`  
- Format: Plain UTF-8 `.txt` compatible with Flipper Zero

### 2. Upload to Flipper

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile**  
- Place in:  
  `SD Card/badusb/`

### 3. Run on Target Machine

- On Flipper Zero:  
  `Main Menu > Bad USB > install_hxd.txt`
- Confirm USB mode is active  
- Connect to Windows machine  
- Press **Run**

The script will:
- Open the Windows Run dialog  
- Launch elevated CMD (may trigger UAC)  
- Execute:  
  `choco install hxd -y`

---

## ✅ Installation Check

- Installs silently with admin rights  
- Requires active internet  
- Latest stable version (e.g., 2.5+ as of August 2025)  
- Chocolatey package: [hxd](https://community.chocolatey.org/packages/hxd)

---

## 📋 Prerequisites

| Requirement                        | Details                                    |
|------------------------------------|--------------------------------------------|
| OS                                 | Windows 10/11                              |
| Chocolatey                         | Must be installed                          |
| Privileges                         | Admin required                             |
| Internet Connection                | Required for Chocolatey install            |
| Flipper Zero with BadUSB           | Enabled and functional                     |
| CMD Compatibility                  | Must support Chocolatey commands           |

---

## ⚙️ Technical Notes

- **Elevation Trigger:**  
  UAC prompt may surface depending on system settings

- **Delay Values:**  
  Defaults: `DELAY 1000`, `500`, `1500`  
  Increase for slower machines (e.g., `DELAY 700+`)

- **Shell Compatibility:**  
  Uses CMD for universal support

- **Controlled Testing:**  
  Recommend VM or sandbox before production use

---

## ⚠️ Disclaimer

Provided as-is for **educational purposes**.  
Use only on systems you **own or have authorized access** to.  
Author not responsible for misuse or deployment consequences.

---

## 📄 License

Licensed under the **MIT License**  
See `LICENSE` file for full terms.

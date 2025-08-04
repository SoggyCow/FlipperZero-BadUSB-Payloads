# Epic Games Launcher Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🎮 Overview

Installs the [Epic Games Launcher](https://www.epicgames.com/store/en-US/download), a digital storefront and game manager, using [Chocolatey](https://chocolatey.org/) on Windows.  
Built for **Flipper Zero’s BadUSB**, the script simulates keystrokes via **DuckyScript** to elevate CMD and silently install the launcher.

> ⚠️ Requires Chocolatey pre-installed. Use `install_chocolatey.txt` prior to deployment.

---

## 🚀 Usage Instructions

### 1. Save the Script

- Filename: `install_epicgameslauncher.txt`  
- Encoding: UTF-8 `.txt` for Flipper Zero compatibility

### 2. Upload to Flipper

- Connect via **USB/Bluetooth**  
- Use **qFlipper** or **Flipper Mobile App**  
- Upload to:  
  `SD Card/badusb/`

### 3. Execute on Target Machine

- On Flipper:  
  `Main Menu > Bad USB > install_epicgameslauncher.txt`
- Confirm USB mode active (USB icon visible)  
- Connect Flipper to target system  
- Press **Run**

Execution steps:
- Triggers Windows Run dialog  
- Opens elevated CMD (may show UAC prompt)  
- Runs silent install:  
  `choco install epicgameslauncher -y`

---

## ✅ Installation Verification

- Requires no user input  
- Epic Games Launcher installs quietly if Chocolatey is present and internet is active  
- Version: Latest stable per Chocolatey's package [listing](https://community.chocolatey.org/packages/epicgameslauncher)

---

## 📋 Prerequisites

- OS: Windows 10/11  
- Chocolatey installed  
- Admin rights  
- Flipper Zero with BadUSB enabled  
- Active internet connection  
- CMD must support Chocolatey  
- Hardware compatibility with Epic Games Launcher (e.g., ≥4GB RAM, supported GPU)

---

## ⚙️ Technical Notes

- **Admin Elevation:**  
  May trigger UAC on systems with default security

- **Silent Mode:**  
  `-y` suppresses installer prompts

- **Timing Delays:**  
  Defaults: `DELAY 1000`, `500`, `1500`  
  Adjust upward for laggy systems

- **Shell Choice:**  
  CMD selected for universal system compatibility

- **Deployment Testing:**  
  Use VMs or sandboxed environments for first-run validation

---

## ⚠️ Disclaimer

Educational use only.  
Deploy only to machines you **own or have permission to access**.  
No responsibility assumed by the author for misuse or system impact.

---

## 📄 License

Licensed under the **MIT License**  
Full terms in the [LICENSE](LICENSE) file

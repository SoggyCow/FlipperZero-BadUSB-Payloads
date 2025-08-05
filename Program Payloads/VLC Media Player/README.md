# VLC Media Player Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🎵 Overview

Automates the installation of [VLC Media Player](https://www.videolan.org/vlc/)—a lightweight, open-source multimedia platform—using [Chocolatey](https://chocolatey.org/)  
Built for **Flipper Zero’s BadUSB** functionality via **DuckyScript**, simulating keystrokes to launch elevated CMD and silently deploy VLC.

> ⚠️ Requires Chocolatey pre-installation. Run the Chocolatey setup script first.

---

## 🚀 Usage Instructions

### 1. Prepare the Script

- Save as: `install_vlc.txt`

### 2. Upload to Flipper

- Connect via **USB/Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer to: `SD Card/badusb/`

### 3. Execute on Host Machine

- On Flipper:  
  `Main Menu > Bad USB`
- Select: `install_vlc.txt`
- Ensure USB mode is active
- Connect Flipper to target Windows system
- Tap **Run**

Execution will:
- Open the Windows Run dialog  
- Launch elevated Command Prompt (UAC may prompt)  
- Install VLC Media Player silently via Chocolatey

---

## ✅ Installation Verification

No user interaction needed if:
- Chocolatey is installed  
- Internet connection is active  
- Admin rights are granted

---

## 📦 Requirements

- Windows 10 or 11  
- Chocolatey installed  
- Flipper Zero w/ BadUSB  
- Internet access  
- Admin privileges  
- VLC-compatible system (lightweight footprint)

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Must be installed beforehand

- **Elevation / UAC Handling:**  
  Elevated CMD launch—UAC may appear

- **Silent Install Flag:**  
  Uses `-y` to bypass prompts

- **Shell Choice:**  
  CMD used for compatibility

- **Delay Heuristics:**  
  Defaults: `DELAY 1000`, `500`, `1500`  
  For slower systems: increase to `DELAY 700+`

- **Version Coverage:**  
  Installs latest VLC stable release (e.g., 3.x as of August 2025)  
  See [Chocolatey Package Page](https://community.chocolatey.org/packages/vlc)

- **Environment Testing:**  
  Recommended in VM or sandbox before full deployment

---

## ⚖️ Disclaimer

Educational use only.  
Use on systems you **own or have explicit authorization to modify**.  
Author assumes **no responsibility** for misuse or system damage.

---

## 📄 License

Licensed under the **MIT License**  
See [LICENSE](LICENSE) for details

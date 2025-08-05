# FileZilla Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🌐 Overview

Installs [FileZilla](https://filezilla-project.org/), a widely used open-source FTP client, via [Chocolatey](https://chocolatey.org/) on Windows.  
Designed for **Flipper Zero’s BadUSB** functionality, using **DuckyScript** to open elevated CMD and execute a silent installation.

> ⚠️ Requires Chocolatey to be installed beforehand.

---

## 🚀 Usage Instructions

### 1. Save the Script

- Filename: `install_filezilla.txt`  
- Format: Plain `.txt`, compatible with Flipper Zero

### 2. Upload to Flipper Zero

- Connect via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Upload to:  
  `SD Card/badusb/`

### 3. Execute the Script

- On Flipper Zero:  
  `Main Menu > Bad USB`
- Select: `install_filezilla.txt`
- Verify USB mode is active (USB logo displayed)
- Plug into target Windows machine
- Tap **Run**

Script actions:
- Opens Windows Run dialog  
- Launches elevated CMD (UAC may appear)  
- Executes Chocolatey command to install FileZilla silently

---

## ✅ Installation Verification

FileZilla installs without manual interaction if:
- Chocolatey is installed  
- Admin privileges are available  
- Internet connection is active

---

## 📦 Requirements

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero with BadUSB enabled  
- Active internet connection  
- Admin privileges  
- FileZilla-compatible system (typically lightweight)

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Must be pre-installed on the system

- **Elevation / UAC Handling:**  
  CMD is launched with admin privileges; UAC may be triggered

- **Silent Installation Flag:**  
  `-y` used to bypass user prompts

- **Shell Choice:**  
  CMD selected for system compatibility

- **Delay Tuning:**  
  - Defaults: `DELAY 1000`, `500`, `1500`  
  - For slower machines: increase to `DELAY 700+`

- **Version Installed:**  
  Latest stable FileZilla version (e.g., 3.x as of August 2025)  
  See [Chocolatey Package Page](https://community.chocolatey.org/packages/filezilla)

- **Testing Recommendation:**  
  Run in VM or sandbox before deploying live

---

## ⚖️ Disclaimer

Educational use only.  
Use only on systems you **own or have permission to modify**.  
Author assumes **no liability** for misuse or system consequences.

---

## 📄 License

Licensed under the **MIT License**  
See the [LICENSE](LICENSE) file for full terms

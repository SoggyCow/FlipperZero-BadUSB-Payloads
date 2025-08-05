# CrystalDiskInfo Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 💽 Overview

Installs [CrystalDiskInfo](https://crystalmark.info/en/software/crystaldiskinfo/), a disk monitoring and SMART diagnostic tool, using [Chocolatey](https://chocolatey.org/).  
Built for **Flipper Zero’s BadUSB** functionality via **DuckyScript**, this payload opens an elevated CMD and performs a silent install with no user prompts.

> ⚠️ Requires Chocolatey pre-installed. See `install_chocolatey.txt`.

---

## 🚀 Usage Instructions

### 1. Prepare the Script

- Save as: `install_crystaldiskinfo.txt`  
- Format: UTF-8 `.txt`, compatible with Flipper Zero

### 2. Upload to Flipper Zero

- Use **qFlipper** or **Flipper Mobile App**
- Transfer to: `SD Card/badusb/`

### 3. Execute on Target Machine

- Navigate:  
  `Main Menu > Bad USB > install_crystaldiskinfo.txt`
- Ensure USB mode is active (USB icon visible)
- Connect Flipper to Windows system
- Tap **Run**

Script behavior:
- Opens Windows **Run dialog**  
- Launches **elevated CMD** (UAC may prompt)  
- Executes Chocolatey install command:  
  `choco install crystaldiskinfo -y`

---

## ✅ Verification

Installation proceeds automatically if:
- Chocolatey is installed  
- Internet access is available  
- Admin privileges are granted

> Latest stable CrystalDiskInfo release (e.g., 9.x as of August 2025) will be deployed.  
Check: [Chocolatey Package Page](https://community.chocolatey.org/packages/crystaldiskinfo)

---

## 📦 Prerequisites

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero with BadUSB functionality enabled  
- Internet connection  
- Administrative privileges  
- Compatible storage controller (for SMART data access)

---

## ⚙️ Technical Notes

- **Elevation Required:**  
  CMD launched with `CTRL-SHIFT ENTER`; UAC may appear

- **Silent Install Flag:**  
  `-y` suppresses user confirmation

- **CMD vs PowerShell:**  
  CMD selected for broader compatibility

- **Delay Profile:**  
  - Standard: `DELAY 1000`, `500`, `1500`  
  - Slower systems: consider `DELAY 700+`

- **Failure Modes:**  
  - Chocolatey not installed  
  - No internet access  
  - UAC prompts blocked  
  - System lacks SMART-compatible disk

- **Testing Advice:**  
  Validate in sandbox or VM prior to live deployment

---

## ⚖️ Disclaimer

For educational use only.  
Use only on systems you **own or are authorized to configure**.  
Author assumes **no liability** for data loss, system impact, or misuse.

---

## 📄 License

Licensed under the **MIT License**  
Refer to [LICENSE](LICENSE) for full terms

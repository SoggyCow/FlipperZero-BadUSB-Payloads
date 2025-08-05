# Visual Studio 2022 Community Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧰 Overview

Installs [Visual Studio 2022 Community Edition](https://visualstudio.microsoft.com/vs/community/)—a powerful free IDE—via [Chocolatey](https://chocolatey.org/) on Windows.  
Optimized for **Flipper Zero's BadUSB** function using **DuckyScript** to launch elevated CMD and trigger silent installation.

> ⚠️ **Important:** Requires Chocolatey installed beforehand. This script will fail if Chocolatey is missing.

---

## 🚀 Usage Instructions

### 1. Save the Script

- Filename: `install_visualstudio2022.txt`

### 2. Upload to Flipper

- Connect via **USB or Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer to:  
  `SD Card/badusb/`

### 3. Run the Script

- On Flipper:  
  `Main Menu > Bad USB`
- Select: `install_visualstudio2022.txt`
- Confirm USB mode is active
- Plug into target Windows host
- Tap **Run**

Actions performed:
- Opens Windows Run dialog  
- Launches elevated CMD (may trigger UAC)  
- Executes Chocolatey install command silently

---

## ✅ Installation Confirmation

Visual Studio installs with no manual input if:
- Chocolatey is present  
- Admin rights granted  
- Internet is available  
- System meets Visual Studio requirements

---

## 📦 Requirements

- Windows 10/11 (64-bit required)  
- Chocolatey pre-installed  
- Flipper Zero with BadUSB enabled  
- Internet connection  
- Admin privileges  
- System specs:  
  - Minimum 8 GB RAM  
  - 20–50 GB disk space  
  - Compatible CPU/GPU (see official [Visual Studio Requirements](https://learn.microsoft.com/en-us/visualstudio/releases/2022/system-requirements))

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:** Must be installed prior  
- **Elevation / UAC Handling:** CMD runs with admin rights  
- **Silent Install Flag:** `-y` suppresses prompts  
- **Shell Compatibility:** CMD used for stability  
- **Timing Heuristics:**  
  - Default delays: `DELAY 1000`, `500`, `1500`  
  - Adjust for slow machines: try `DELAY 700+`

- **Version Installed:**  
  Installs latest stable Visual Studio 2022 Community (e.g., 17.x as of August 2025)  
  See [Chocolatey Package Page](https://community.chocolatey.org/packages/visualstudio2022community)

- **Testing Guidance:**  
  Due to install size, use VMs or sandbox environments for validation

---

## ⚖️ Disclaimer

Provided **as-is** for educational purposes.  
Use only on systems you **own or are authorized to configure**.  
Author assumes **no responsibility** for damage or misuse.

---

## 📄 License

Distributed under the **MIT License**  
See the [LICENSE](LICENSE) file for terms.

# H2testw Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🔍 Overview

Installs [H2testw](https://www.heise.de/download/product/h2testw-50539), a utility for testing the integrity and performance of USB drives, SD cards, and other storage devices, via [Chocolatey](https://chocolatey.org/).  
Crafted for **Flipper Zero's BadUSB** feature using **DuckyScript**, this payload launches an elevated CMD session and executes a silent installer.

> ⚠️ Requires Chocolatey pre-installation on the target system.

---

## 🚀 Usage Instructions

### 1. Save and Transfer the Payload

- Save as: `install_h2testw.txt`  
- Format: Plain `.txt` compatible with Flipper Zero

### 2. Upload to Flipper

- Connect Flipper Zero via USB/Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Upload to:  
  `SD Card/badusb/`

### 3. Deploy the Payload

- Menu Navigation:  
  `Main Menu > Bad USB > install_h2testw.txt`
- Confirm USB mode is active (USB icon visible)  
- Plug Flipper into Windows machine  
- Press **Run**

Script performs:
- Opens Windows **Run dialog**  
- Launches **elevated CMD** (UAC may appear)  
- Executes:  
  `choco install h2testw -y`

---

## ✅ Installation Verification

If Chocolatey is installed and internet access is available:
- H2testw installs silently  
- No user input is required  
- Version deployed: Latest stable (e.g., 1.4 as of August 2025)  
- Reference: [Chocolatey Package Page](https://community.chocolatey.org/packages/h2testw)

---

## 📋 Requirements

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero with BadUSB functionality enabled  
- Internet access on target system  
- Admin privileges  
- Basic disk I/O compatible hardware (USB, SD, etc.)

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Required for package retrieval

- **Privilege Elevation:**  
  CMD launched with `CTRL-SHIFT ENTER`; UAC may be triggered

- **Silent Install:**  
  `-y` flag used to suppress prompts

- **Shell Environment:**  
  CMD chosen for broad compatibility

- **Execution Delays:**  
  Standard: `DELAY 1000`, `500`, `1500`  
  Consider increasing to `700+` on slower hosts

- **Testing Advice:**  
  Sandbox or VM validation recommended prior to live deployment

---

## ⚠️ Disclaimer

This script is provided **as-is**, for educational use only.  
Deploy only on systems you **own or are authorized to access**.  
Author assumes **no responsibility** for data loss or misuse.

---

## 📄 License

Licensed under the **MIT License**  
Refer to [LICENSE](LICENSE) for full terms

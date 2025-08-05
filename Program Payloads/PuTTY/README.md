# PuTTY Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🛠 Overview

Automates the installation of [PuTTY](https://www.putty.org/), a popular open-source SSH and Telnet client, using [Chocolatey](https://chocolatey.org/) on Windows.  
Designed for **Flipper Zero’s BadUSB** function using **DuckyScript** to open an elevated Command Prompt and silently install PuTTY.

> ⚠️ Requires pre-installed Chocolatey on target system.

---

## 🚀 Deployment Instructions

### 1. Save the Payload

- Filename: `install_putty.txt`  
- Format: UTF-8 encoded `.txt`, compatible with Flipper Zero BadUSB

### 2. Transfer to Flipper Zero

- Connect via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Upload to:  
  `SD Card/badusb/`

### 3. Execute on Target System

- Navigate: `Main Menu > Bad USB`  
- Select: `install_putty.txt`  
- Verify USB mode is active (USB logo visible)  
- Plug into Windows machine  
- Tap **Run**

Payload actions:
- Opens Windows **Run Dialog**  
- Launches **elevated CMD** (UAC may appear)  
- Executes: `choco install putty.install -y`

---

## ✅ Verification & Results

- **Silent install**: No user interaction required  
- **Version**: Latest stable (e.g., 0.81+ as of August 2025)  
- Visit: [Chocolatey Package Page](https://community.chocolatey.org/packages/putty.install)

---

## 📋 System Prerequisites

- Windows 10/11 OS  
- Chocolatey pre-installed  
- Flipper Zero with BadUSB enabled  
- Internet connection on target system  
- Admin privileges to launch elevated CMD  
- PuTTY system compatibility (lightweight footprint)

---

## ⚙️ Technical Notes

- **Admin Rights Required**: Elevated CMD may trigger UAC  
- **Silent Flag**: `-y` bypasses user prompts  
- **Shell**: CMD used for maximal system compatibility  
- **Timing Delays**:  
  - Standard: `DELAY 1000`, `500`, `1500`  
  - For slower systems: increase `DELAY 500` to `700+`  

- **Failure Modes**:  
  - If Chocolatey isn’t installed, script aborts  
  - No fallback mechanisms—validate environment first

- **Sandbox Testing**:  
  Use a virtual machine to verify behavior before live deployment

---

## ⚖️ Disclaimer

Educational and lawful use only.  
Only deploy on machines with **explicit permission**.  
Author assumes **no liability** for unintended consequences.

---

## 📄 License

Licensed under the **MIT License**  
See the [LICENSE](LICENSE) file for full terms.

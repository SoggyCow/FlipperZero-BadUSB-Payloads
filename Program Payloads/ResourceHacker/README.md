# ResourceHacker Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🛠️ Overview

Installs [ResourceHacker](http://www.angusj.com/resourcehacker/), a free utility for viewing, extracting, and editing resources in Windows executables.  
This payload uses **Flipper Zero’s BadUSB** and **DuckyScript** to simulate keystrokes, elevate CMD, and install the **portable version** via [Chocolatey](https://chocolatey.org/).

> ⚠️ Requires Chocolatey. Deploy `install_chocolatey.txt` before running this script.

---

## 🚀 Usage Guide

### Step 1: Save the Script

- Filename: `install_resourcehacker.txt`  
- Format: UTF-8 `.txt` for BadUSB compatibility

### Step 2: Upload to Flipper Zero

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile**  
- Path: `SD Card/badusb/`

### Step 3: Run on Target System

- On Flipper:  
  `Main Menu > Bad USB > install_resourcehacker.txt`
- Ensure USB mode is enabled (USB icon visible)  
- Plug into target Windows machine  
- Press **Run**

The script will:
- Open Windows Run dialog  
- Elevate to admin CMD (UAC may appear)  
- Execute:  
  `choco install resourcehacker.portable -y`

---

## ✅ Verify Installation

- Silent install with no user interaction  
- Portable version requires no registry or system integration  
- Chocolatey package: [resourcehacker.portable](https://community.chocolatey.org/packages/resourcehacker.portable)

---

## 📋 Requirements

| Requirement                | Details                                           |
|----------------------------|---------------------------------------------------|
| OS                         | Windows 10/11                                     |
| Chocolatey                 | Must be pre-installed                             |
| Admin Privileges           | Required for elevation                            |
| Internet Connection        | Required to download package                      |
| Flipper Zero               | BadUSB mode enabled                               |
| CMD Compatibility          | Must support Chocolatey commands                  |

---

## ⚙️ Technical Details

- **Shell Choice:** CMD for universal compatibility  
- **Elevation:** May trigger User Account Control (UAC)  
- **Timing Delays:**  
  - Defaults: `DELAY 1000`, `500`, `1500`  
  - Adjust upward for slow systems (e.g., `DELAY 700+`)  
- **Package Version:** 5.x or newer as of August 2025  
- **Testing Strategy:** Always validate in sandbox or VM environment

---

## ⚠️ Disclaimer

For educational and authorized use only.  
Deploy only on systems you **own or have explicit permission** to control.  
Author assumes no responsibility for misuse or outcomes of deployment.

---

## 📄 License

Licensed under the **MIT License**  
See the included `LICENSE` file for full terms.

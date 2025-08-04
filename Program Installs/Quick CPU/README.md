# Quick CPU Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🚀 Overview

Installs [Quick CPU](https://coderbag.com/product/quickcpu), a lightweight utility for tuning CPU performance, power settings, and thermal management, via [Chocolatey](https://chocolatey.org/) on Windows.  
Built for **Flipper Zero’s BadUSB**, this payload uses **DuckyScript** to simulate keystrokes and launch an elevated CMD session for a hands-free install.

> ⚠️ Requires Chocolatey to be installed prior to execution. See `install_chocolatey.txt`.

---

## 🧠 Usage Instructions

### 1. Prepare the Payload

- Filename: `install_quickcpu.txt`  
- Format: UTF-8 plain `.txt` for Flipper Zero compatibility

### 2. Upload to Flipper Zero

- Connect via USB/Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Upload to:  
  `SD Card/badusb/`

### 3. Deploy on Target System

- Menu Navigation:  
  `Main Menu > Bad USB > install_quickcpu.txt`  
- Ensure USB mode is active  
- Connect to Windows machine  
- Press **Run**

Execution flow:
- Opens Windows Run dialog  
- Launches elevated CMD (UAC prompt may appear)  
- Executes:  
  `choco install quickcpu -y`

---

## ✅ Installation Verification

- Installs silently if Chocolatey and internet access are available  
- As of August 2025, package availability should be verified:  
  [Chocolatey Package Page](https://community.chocolatey.org/packages/quickcpu)

---

## 📋 Requirements

| Requirement               | Description                                       |
|---------------------------|---------------------------------------------------|
| OS                        | Windows 10/11                                     |
| Chocolatey Installed      | Must be pre-installed                             |
| Admin Privileges          | Required for elevation                            |
| Internet Connection       | Required to download package                      |
| Flipper Zero              | BadUSB enabled and functional                     |
| CMD Compatibility         | Must support Chocolatey commands                  |
| Quick CPU Compatibility   | Refer to vendor specs (minimal requirements)      |

---

## ⚙️ Technical Notes

- **Privilege Elevation:**  
  Uses `CTRL-SHIFT ENTER` to elevate CMD; UAC may appear

- **Silent Install Flag:**  
  `-y` suppresses any user prompts

- **Timing Delays:**  
  Default: `DELAY 1000`, `500`, `1500`  
  Adjust for slower systems: try `DELAY 700+`

- **Shell Selection:**  
  CMD chosen for compatibility across host configurations

- **Testing Recommendation:**  
  Validate in sandbox, VM, or offline testbed before live deployment

- **Package Availability:**  
  Quick CPU may not always be present in Chocolatey repo—verify manually

---

## ⚠️ Disclaimer

This script is provided **as-is** for educational purposes.  
Use only on machines you **own or are explicitly authorized** to configure.  
Author disclaims responsibility for misuse, damage, or side effects.

---

## 📄 License

Licensed under the **MIT License**  
Refer to the `LICENSE` file for full details.

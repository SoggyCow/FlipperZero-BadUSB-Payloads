# Rename My TV Series 2 Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🎬 Overview

Installs **Rename My TV Series 2**, a utility for renaming episode files using online TV database info, via [Chocolatey](https://chocolatey.org/) on Windows.  
Scripted for **Flipper Zero’s BadUSB**, this DuckyScript payload simulates keystrokes to launch an elevated CMD and silently deploy the application.

> ⚠️ Requires Chocolatey pre-installed. Use `install_chocolatey.txt` before running this script.

---

## 🚀 Usage Instructions

### 1. Prepare the Payload

- Filename: `install_renamemytvseries2.txt`  
- Format: UTF-8 plain text `.txt` compatible with Flipper Zero

### 2. Upload to Flipper Zero

- Connect via USB/Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Destination:  
  `SD Card/badusb/`

### 3. Execute on Target Machine

- Menu: `Main Menu > Bad USB > install_renamemytvseries2.txt`  
- Ensure USB mode is active (USB icon visible)  
- Connect to a Windows system  
- Press **Run**

Payload performs:
- Opens Windows Run dialog  
- Elevates to CMD via simulated `CTRL + SHIFT + ENTER` (UAC may appear)  
- Executes:  
  `choco install renamemytvseries2 -y`

---

## ✅ Verification

- Installs silently if Chocolatey and internet access are present  
- Package version: latest stable (as of August 2025)  
- Check availability: [Chocolatey Package Page](https://community.chocolatey.org/packages/renamemytvseries2)

---

## 📋 Requirements

| Component                   | Description                                     |
|----------------------------|-------------------------------------------------|
| OS                         | Windows 10/11                                   |
| Chocolatey                 | Must be installed beforehand                    |
| Internet Connection        | Required to fetch package                       |
| Admin Privileges           | Needed for elevation and installation           |
| Flipper Zero               | BadUSB enabled                                  |
| CMD Shell                  | Must support Chocolatey                         |
| RAM & Disk                 | Typically lightweight (verify vendor specs)     |

---

## ⚙️ Technical Notes

- **Timing Delays:**  
  Defaults: `DELAY 1000`, `500`, `1500`  
  Use `DELAY 700+` for slower systems

- **Silent Flag:**  
  `-y` bypasses install prompts

- **Package Availability Warning:**  
  Package may not be available on Chocolatey—verify before execution

- **Testing Advice:**  
  Deploy first in VM or sandbox before live use

---

## ⚠️ Disclaimer

For educational use only.  
Deploy only on systems you **own or are explicitly authorized** to modify.  
Author is not liable for misuse or unintended results.

---

## 📄 License

Licensed under the **MIT License**  
See `LICENSE` file for full terms.

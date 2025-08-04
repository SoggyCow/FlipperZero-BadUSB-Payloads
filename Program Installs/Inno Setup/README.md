# Inno Setup Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 📦 Overview

Installs [Inno Setup](https://jrsoftware.org/isinfo.php), a leading open-source installer compiler for Windows applications, via [Chocolatey](https://chocolatey.org/).  
Designed for **Flipper Zero’s BadUSB** using **DuckyScript**, this payload simulates keyboard input to elevate CMD and silently deploy Inno Setup.

> ⚠️ Chocolatey must be installed prior to using this payload. See `install_chocolatey.txt`.

---

## 🚀 Usage Instructions

### 1. Prepare the Payload

- Filename: `install_innosetup.txt`  
- Format: UTF-8 plain `.txt`, compatible with Flipper Zero

### 2. Upload to Flipper

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Upload to:  
  `SD Card/badusb/`

### 3. Execute on Host System

- Menu:  
  `Main Menu > Bad USB > install_innosetup.txt`  
- Confirm USB mode is active (USB icon visible)  
- Connect to Windows machine  
- Press **Run**

Script behavior:
- Opens Windows Run dialog  
- Launches elevated Command Prompt (UAC may trigger)  
- Executes:  
  `choco install innosetup -y`

---

## ✅ Installation Verification

- No user interaction required  
- Installs latest stable Inno Setup version (e.g., 6.x+ as of August 2025)  
- Check Chocolatey: [Inno Setup Package](https://community.chocolatey.org/packages/innosetup)

---

## 📋 Requirements

| Requirement            | Description                                   |
|------------------------|-----------------------------------------------|
| OS                     | Windows 10/11                                 |
| Chocolatey             | Must be pre-installed                         |
| Admin Privileges       | Required for elevation                        |
| Internet Connection    | Required for package download                 |
| Flipper Zero           | BadUSB feature enabled                        |
| CMD Compatibility      | Must support Chocolatey commands              |

---

## ⚙️ Technical Notes

- **Privilege Elevation:**  
  Uses `CTRL-SHIFT ENTER`; may show UAC prompt

- **Silent Installation:**  
  `-y` flag prevents interactive dialogs

- **Timing Delays:**  
  - Defaults: `DELAY 1000`, `500`, `1500`  
  - Adjust for slower systems: use `DELAY 700+`

- **Shell Environment:**  
  CMD selected for universal compatibility

- **Testing Strategy:**  
  Validate payload in VM or sandbox before field deployment

---

## ⚠️ Disclaimer

Use for educational and authorized purposes only.  
Run only on systems you **own or have explicit permission to access**.  
Author is not liable for misuse or resulting consequences.

---

## 📄 License

Licensed under the **MIT License**  
See the `LICENSE` file for full terms

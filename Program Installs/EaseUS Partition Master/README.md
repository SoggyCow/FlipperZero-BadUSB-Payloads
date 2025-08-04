# EaseUS Partition Master Free Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧱 Overview

Installs **EaseUS Partition Master Free**, a disk partition management utility for resizing, merging, and formatting drives, using [Chocolatey](https://chocolatey.org/) on Windows.  
Powered by **Flipper Zero’s BadUSB** functionality, this **DuckyScript** payload simulates keyboard input to launch elevated CMD and silently deploy the tool.

> ⚠️ Chocolatey must be installed prior to execution. See `install_chocolatey.txt`.

---

## 🚀 Usage Instructions

### 1. Save Script

- File name: `install_partitionmasterfree.txt`  
- Format: Plain `.txt`, UTF-8 encoded

### 2. Upload to Flipper

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Upload to:  
  `SD Card/badusb/`

### 3. Execute on Target Machine

- Navigate:  
  `Main Menu > Bad USB > install_partitionmasterfree.txt`  
- Confirm USB mode active (USB icon visible)  
- Connect Flipper to Windows host  
- Tap **Run**

Script actions:
- Opens Windows Run dialog  
- Elevates CMD (`CTRL + SHIFT + ENTER`, triggers UAC if enabled)  
- Executes:  
  `choco install partitionmasterfree -y`

---

## ✅ Verification

- Discord installs silently if:
  - Chocolatey is installed  
  - Internet access is active  
  - Admin rights are granted  
  - CMD is Chocolatey-compatible

Check Chocolatey package: [partitionmasterfree](https://community.chocolatey.org/packages/partitionmasterfree)

---

## 📋 Prerequisites

| Requirement              | Description                                        |
|--------------------------|----------------------------------------------------|
| OS                       | Windows 10/11                                      |
| Chocolatey               | Must be installed                                  |
| Admin Privileges         | Required                                           |
| Internet Connection      | Required for package download                      |
| Flipper Zero             | BadUSB functionality enabled                       |
| CMD Compatibility        | Required                                           |
| System Specs             | Typically lightweight; verify with EaseUS docs     |

---

## ⚙️ Technical Notes

- **Timing Delays:**  
  Uses `DELAY 1000`, `500`, `1500` for stable execution  
  Tune upward for slower systems (`700+`)

- **Silent Install:**  
  `-y` flag suppresses prompts

- **Elevation Method:**  
  Simulates `CTRL + SHIFT + ENTER`; UAC may appear

- **Package Availability:**  
  Confirm that `partitionmasterfree` exists in Chocolatey repo (as of August 2025)

- **Testing Protocol:**  
  Run in a VM or sandbox before deploying to production environments

---

## ⚠️ Disclaimer

This payload is provided **as-is**, strictly for educational use.  
Deploy only on systems you **own or have explicit authorization** to modify.  
Author assumes no liability for misuse or consequences.

---

## 📄 License

Licensed under the **MIT License**  
See the included `LICENSE` file for full terms

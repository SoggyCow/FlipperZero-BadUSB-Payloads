# BleachBit Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧼 Overview

Installs [BleachBit](https://www.bleachbit.org/), an open-source privacy tool for cleaning junk files, clearing cache, and wiping sensitive data from Windows systems.  
Designed for **Flipper Zero’s BadUSB** and scripted in **DuckyScript**, this payload automates silent deployment via **elevated CMD** using [Chocolatey](https://chocolatey.org/).

> ⚠️ Chocolatey must be installed before executing this module (`install_chocolatey.txt`).

---

## 🧰 Usage Instructions

### 1. Save Payload

- File name: `install_bleachbit.txt`  
- Format: UTF-8 encoded plain text `.txt` (compatible with Flipper Zero)

### 2. Upload to Flipper

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Destination path:  
  `SD Card/badusb/`

### 3. Execute on Target System

- Navigate:  
  `Main Menu > Bad USB > install_bleachbit.txt`  
- Confirm USB mode is active (USB icon visible)  
- Plug Flipper into target machine  
- Tap **Run**

Execution Flow:
- Opens Windows Run dialog  
- Launches elevated CMD (`CTRL + SHIFT + ENTER`) — may trigger UAC  
- Executes command:  
  `choco install bleachbit -y`

---

## ✅ Verification & Environment

| Requirement               | Description                                           |
|---------------------------|--------------------------------------------------------|
| Windows OS                | Windows 10/11                                          |
| Chocolatey                | Must be pre-installed                                  |
| Admin Privileges          | Required for elevated install                          |
| Internet Connectivity     | Necessary for Chocolatey package download              |
| CMD Compatibility         | Must accept Chocolatey commands                        |
| System Specs              | Lightweight footprint; see [BleachBit requirements](https://www.bleachbit.org/documentation) |

---

## ⚙️ Technical Notes

- **Silent Install:**  
  `-y` flag suppresses prompts during installation

- **Delays for Reliability:**  
  Uses `DELAY 1000`, `500`, `1500`  
  Increase for slower hosts (`700+` recommended)

- **Version Installed:**  
  Latest stable (e.g., v4.x as of August 2025)  
  Check package: [Chocolatey: bleachbit](https://community.chocolatey.org/packages/bleachbit)

- **Security Consideration:**  
  BleachBit can permanently erase files and logs—use with caution

- **Testing Advice:**  
  Deploy initially in a sandbox or VM to verify behavior before field use

---

## ⚠️ Disclaimer

Use only on systems you **own or have explicit authorization** to modify.  
This payload is offered **as-is**, and the author is **not responsible** for misuse, data loss, or unintended consequences.

---

## 📄 License

Distributed under the **MIT License**  
Refer to the `LICENSE` file for full terms.

# TestDisk Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧠 Overview

Automates the silent installation of [TestDisk](https://www.cgsecurity.org/wiki/TestDisk), a powerful open-source data recovery utility for partition repair and file restoration.  
Uses **Chocolatey** for deployment and **DuckyScript** via **Flipper Zero's BadUSB** to simulate elevation and command execution.

> 🔑 **Requires Chocolatey** pre-installed on the target machine

---

## 🚀 Usage Instructions

### 1. Save the Payload

- Filename: `install_testdisk.txt`  
- Format: Plain `.txt` compatible with Flipper Zero

### 2. Transfer to Flipper

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Destination:  
  `SD Card/badusb/`

### 3. Execute

- Navigate:  
  `Main Menu > Bad USB > install_testdisk.txt`
- Confirm: USB mode is active (USB icon visible)  
- Plug into target Windows machine  
- Press **Run**

Script flow:
- Opens Windows **Run dialog**  
- Elevates to **Admin CMD** (UAC may prompt)  
- Executes:  
  `choco install testdisk -y`

---

## 🧪 Installation Verification

- Installs latest stable version (e.g., 7.2+)  
- No interaction required if Chocolatey and internet access are in place  
- Package source: [Chocolatey: TestDisk](https://community.chocolatey.org/packages/testdisk)

---

## ⚙️ Requirements

- Windows 10 or 11  
- Chocolatey installed  
- Internet access  
- Admin privileges  
- Flipper Zero with BadUSB support  
- CMD must support Chocolatey commands

---

## ⚠️ Technical Notes

- **Chocolatey Dependency:**  
  Run Chocolatey install script first

- **Privilege Elevation:**  
  Uses `CTRL-SHIFT ENTER` for elevated CMD  
  May trigger UAC prompt

- **Silent Install:**  
  Uses `-y` flag to suppress dialogs

- **Execution Delays:**  
  Default: `DELAY 1000`, `500`, `1500`  
  Adjust for slower hosts: up to `DELAY 700+`

- **Testing Advice:**  
  Validate payload in VM or controlled host before deployment

---

## 🛡️ Disclaimer

Educational use only.  
Deploy only on systems you **own or have explicit permission to access**.  
Author assumes no responsibility for misuse or system impact.

---

## 📄 License

Licensed under the **MIT License**  
See [LICENSE](LICENSE) for full terms

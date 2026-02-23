# NVIDIA Display Driver Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🎮 Overview

Silently installs the [NVIDIA Display Driver](https://www.nvidia.com/Download/index.aspx) via [Chocolatey](https://chocolatey.org/) on Windows.  
Engineered for **Flipper Zero’s BadUSB**, leveraging **DuckyScript** to elevate CMD and execute a silent install for NVIDIA graphics hardware.

> ⚠️ Chocolatey **must be pre-installed**. See `install_chocolatey.txt`.

---

## 🚀 Usage Instructions

### 1. Prepare the Script

- Save as: `install_nvidia.txt`  
- Format: UTF-8 plain text (Flipper-compatible)

### 2. Transfer to Flipper Zero

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Upload to: `SD Card/badusb/`

### 3. Execute the Payload

- Menu: `Main Menu > Bad USB > install_nvidia.txt`  
- Confirm USB mode is active  
- Connect to target Windows machine  
- Press **Run**

Script actions:
- Opens **Run dialog**  
- Launches **elevated CMD** (may trigger UAC prompt)  
- Executes: `choco install nvidia-display-driver -y`

---

## ✅ Verification Checklist

- Chocolatey installed  
- Active internet connection  
- System has compatible **NVIDIA GPU**  
- Admin privileges available

> Latest NVIDIA drivers will be installed automatically (e.g., Game Ready or Studio depending on system).

Check status via:  
[Chocolatey Package Page](https://community.chocolatey.org/packages/nvidia-display-driver)

---

## 📋 Requirements

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero with BadUSB enabled  
- Internet access  
- Admin rights  
- NVIDIA GPU with Chocolatey-compatible driver support

---

## ⚙️ Execution Notes

- **Privilege Elevation:**  
  Required to install drivers via CMD; triggers UAC

- **Silent Flag:**  
  `-y` bypasses all user prompts

- **Shell:**  
  CMD selected for compatibility

- **Timing Delays:**  
  Standard: `DELAY 1000`, `500`, `1500`  
  Tune upward (`500` → `700+`) for slower systems

- **GPU Detection:**  
  Script fails silently if no supported GPU is present

- **Virtualization Caveat:**  
  Virtual machines typically lack GPU passthrough—test on physical hardware

---

## ⚠️ Disclaimer

Provided for **educational use only**.  
Deploy only on systems you **own or are authorized to modify**.  
Author is **not liable** for misuse or unintended consequences.

---

## 📄 License

Licensed under the **MIT License**  
See the [LICENSE](LICENSE) file for details.

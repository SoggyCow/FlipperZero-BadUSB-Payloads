# Paint.NET Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🎨 Overview

This script installs [Paint.NET](https://www.getpaint.net/), a user-friendly image editor, via [Chocolatey](https://chocolatey.org/) on Windows.  
Designed for **Flipper Zero’s BadUSB** feature, it uses **DuckyScript** to simulate keystrokes, elevate to **Command Prompt (CMD)**, and silently install Paint.NET.

> ⚠️ **Important:** Requires Chocolatey to be installed prior to execution.

---

## 🚀 Usage Instructions

Runs via Flipper Zero’s **BadUSB keyboard emulation**.

### 1. Save the Script

- Save to a `.txt` file (e.g., `install_paintnet.txt`)

### 2. Upload to Flipper Zero

- Connect via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer to:  
  `SD Card/badusb/`

### 3. Execute the Script

- On Flipper:  
  `Main Menu > Bad USB`
- Select `install_paintnet.txt`
- Confirm USB mode is active
- Plug into target Windows machine
- Press **Run**

This will:
- Launch Windows Run dialog
- Open elevated CMD (UAC may appear)
- Execute Chocolatey command to silently install Paint.NET

---

## ✅ Installation Verification

Paint.NET installs automatically if:
- Chocolatey is installed  
- Internet connection is active

---

## 📦 Prerequisites

- Windows 10/11 (recommended)  
- Chocolatey pre-installed  
- Flipper Zero with BadUSB enabled  
- Admin privileges  
- Internet access  
- Required system components (e.g., .NET Framework)

---

## ⚙️ Technical Notes

- **Chocolatey Required:**  
  Must be installed beforehand

- **Elevation Needed:**  
  CMD is run as admin; UAC may appear

- **Silent Install:**  
  `-y` flag ensures prompt-free install

- **CMD Compatibility:**  
  CMD chosen for broader support—verify it handles Chocolatey properly

- **Delay Calibration:**  
  Defaults: `DELAY 1000`, `DELAY 500`, `DELAY 1500`  
  For slower systems: increase to `DELAY 700+`

- **Paint.NET Version:**  
  Installs latest stable (e.g., 5.x as of August 2025)  
  See [Chocolatey Package](https://community.chocolatey.org/packages/paint.net) for details

- **Testing Environment:**  
  Validate in VM or sandbox before deployment

---

## ⚖️ Disclaimer

This script is provided **as-is** for educational purposes.  
Only run on systems you **own or are authorized to modify**.  
Author (SoggyCow) assumes **no liability** for misuse or consequences.

---

## 📄 License

Licensed under the **MIT License**  
Refer to [LICENSE](LICENSE) for full terms

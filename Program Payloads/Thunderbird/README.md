# Thunderbird Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 📧 Overview

Installs [Mozilla Thunderbird](https://www.thunderbird.net/), a secure open-source desktop email client, via [Chocolatey](https://chocolatey.org/) on Windows.  
Engineered for **Flipper Zero’s BadUSB** using **DuckyScript**, this payload launches elevated CMD and deploys the client silently.

> ⚠️ Requires Chocolatey pre-installed. See `install_chocolatey.txt`.

---

## 🚀 Usage Instructions

### 1. Save the Script

- File: `install_thunderbird.txt`  
- Format: Plain UTF-8 `.txt` compatible with Flipper Zero

### 2. Upload to Flipper

- Connect via **USB/Bluetooth**  
- Use **qFlipper** or **Flipper Mobile App**  
- Upload to:  
  `SD Card/badusb/`

### 3. Deploy on Target Machine

- On Flipper:  
  `Main Menu > Bad USB > install_thunderbird.txt`
- Ensure USB mode is active (USB icon visible)  
- Plug into Windows machine  
- Press **Run**

Script actions:
- Launches Windows Run dialog  
- Opens elevated CMD (may trigger UAC)  
- Executes silent install:  
  `choco install thunderbird -y`

---

## ✅ Installation Check

- No user input required  
- Version installed: Latest stable (e.g., 115.x+ as of August 2025)  
- View on Chocolatey: [Thunderbird Package](https://community.chocolatey.org/packages/thunderbird)

---

## 📋 Prerequisites

- Windows 10/11  
- Chocolatey pre-installed  
- Admin privileges  
- Internet connection  
- Flipper Zero with BadUSB enabled  
- CMD must support Chocolatey

---

## ⚙️ Technical Notes

- **Privilege Elevation:**  
  UAC prompt may be triggered during CMD launch

- **Silent Install Flag:**  
  `-y` skips all installer dialogs

- **Timing Delays:**  
  Defaults: `DELAY 1000`, `500`, `1500`  
  Consider increasing to `DELAY 700+` for slower machines

- **Shell Preference:**  
  CMD selected for compatibility across systems

- **Testing Protocol:**  
  Validate in VM or sandbox prior to deployment

---

## ⚠️ Disclaimer

Use for educational purposes only.  
Deploy only on systems you **own or are authorized to access**.  
Author assumes no liability for misuse or unintended outcomes.

---

## 📄 License

Licensed under the **MIT License**  
Refer to the [LICENSE](LICENSE) file for full terms

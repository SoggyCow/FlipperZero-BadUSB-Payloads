# Dropbox Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## ☁️ Overview

Automates silent installation of [Dropbox](https://www.dropbox.com), a cloud-based file sync and backup client, via [Chocolatey](https://chocolatey.org/).  
Leverages **Flipper Zero’s BadUSB** interface with **DuckyScript** to elevate and execute the command chain inside an admin-level CMD session.

> 🔔 Chocolatey must be installed beforehand. Run the install payload first.

---

## 🎮 Usage Instructions

### 1. Save the Payload

- File name: `install_dropbox.txt`  
- Format: Plain `.txt` for Flipper Zero compatibility

### 2. Transfer to Device

- Connect via USB/Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Copy to:  
  `SD Card/badusb/`

### 3. Execute via BadUSB

- Navigate on Flipper:  
  `Main Menu > Bad USB > install_dropbox.txt`
- Ensure USB mode is active (USB logo visible)  
- Plug into target Windows machine  
- Press **Run**

Script flow:
- Opens Run dialog  
- Elevates CMD prompt (UAC may appear)  
- Executes install command:  
  `choco install dropbox -y`

---

## ✔️ Post-Execution Verification

- Dropbox installs silently  
- No user interaction required  
- Internet connection must be active  
- Version deployed: Latest stable (e.g., 187.4+ as of August 2025)  
- Chocolatey link: [Dropbox Package](https://community.chocolatey.org/packages/dropbox)

---

## 📋 Requirements

- Windows 10/11  
- Chocolatey installed  
- Admin rights on target system  
- Flipper Zero with BadUSB support  
- Internet access  
- CMD shell with Chocolatey compatibility

---

## ⚙️ Technical Notes

- **Elevation:**  
  Triggered via `CTRL-SHIFT ENTER`  
  UAC confirmation may be required

- **Silent Mode:**  
  `-y` flag suppresses install prompts

- **Timing Delays:**  
  `DELAY 1000`, `500`, `1500`  
  Can be increased for slower hosts (`700+` suggested)

- **Shell Compatibility:**  
  CMD chosen for broad support across hosts

- **Testing Advice:**  
  Use sandbox or VM first to validate behavior

---

## ⚠️ Disclaimer

This script is provided **as-is**, for educational use only.  
Deploy only on systems you **own or are authorized to access**.  
Author assumes no responsibility for misuse or unintended consequences.

---

## 📄 License

Licensed under the **MIT License**  
See [LICENSE](LICENSE) for full text

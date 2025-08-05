# Tailscale Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🔐 Overview

Installs [Tailscale](https://tailscale.com/), a secure, zero-config VPN, using [Chocolatey](https://chocolatey.org/)  
Built for **Flipper Zero’s BadUSB** using **DuckyScript** to launch an elevated CMD and install silently.

> ⚠️ Requires Chocolatey to be installed beforehand

---

## 🚀 Usage Instructions

### 1. Script Preparation

- Save as: `install_tailscale.txt`

### 2. Transfer to Flipper

- Connect via **USB/Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Upload to: `SD Card/badusb/`

### 3. Execution Steps

- On Flipper: `Main Menu > Bad USB`
- Select: `install_tailscale.txt`
- Ensure USB mode is active
- Connect Flipper to target Windows host
- Press **Run**

Script will:
- Open Run dialog  
- Launch elevated CMD (may trigger UAC prompt)  
- Run Chocolatey command to install Tailscale silently

---

## ✅ Installation Verification

Tailscale installs with no user input if:
- Chocolatey is present  
- Admin rights granted  
- Internet access available

---

## 📦 Requirements

- Windows 10/11  
- Chocolatey pre-installed  
- Flipper Zero with BadUSB  
- Internet connection  
- Admin privileges  
- System specs compatible with Tailscale (minimal footprint)

---

## ⚙️ Technical Notes

- **Dependency:** Chocolatey must be installed first  
- **Elevation:** Admin CMD required; UAC may display  
- **Silent Install:** Uses `-y` flag to suppress prompts  
- **Shell Choice:** CMD preferred for broader compatibility  
- **Delay Tuning:**  
  - Defaults: `DELAY 1000`, `DELAY 500`, `DELAY 1500`  
  - For slower systems: raise to `DELAY 700+`

- **Version:** Installs latest stable Tailscale package  
  - See [Chocolatey Package Page](https://community.chocolatey.org/packages/tailscale)

- **Sandbox Testing:** Recommended in VMs before deployment

---

## ⚖️ Disclaimer

This script is provided **as-is** for educational use.  
Run only on systems you **own or are authorized to control**.  
Author accepts **no liability** for unintended use or impact.

---

## 📄 License

Licensed under the **MIT License**  
See [LICENSE](LICENSE) for full terms

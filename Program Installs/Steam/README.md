# Steam Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🕹️ Overview

Installs [Steam](https://store.steampowered.com/)—a digital platform for games—using [Chocolatey](https://chocolatey.org/) via simulated keystrokes.  
Built for **Flipper Zero's BadUSB** using **DuckyScript** to elevate CMD and perform silent installation.

> ⚠️ Requires Chocolatey pre-installation. Run the Chocolatey install script first.

---

## 🚀 Usage Instructions

### 1. Prepare the Script

- Save as `install_steam.txt`

### 2. Transfer to Flipper Zero

- Connect Flipper via **USB/Bluetooth**
- Use **qFlipper** or **Flipper Mobile**
- Upload to: `SD Card/badusb/`

### 3. Execute on Target Machine

- Flipper Menu: `Main Menu > Bad USB`
- Select: `install_steam.txt`
- Ensure USB mode is active
- Plug Flipper into Windows host
- Press **Run**

Flipper will:
- Open Run dialog  
- Launch elevated CMD (UAC may appear)  
- Execute Chocolatey command to install Steam silently

---

## ✅ Verification & Outcome

Steam installs automatically if:
- Chocolatey is installed  
- Internet connection is available  
- Admin rights are granted

---

## 📦 Requirements

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero w/ BadUSB  
- Internet access  
- Admin rights  
- System specs suitable for Steam (RAM, GPU, etc.)

---

## ⚙️ Technical Notes

- **Dependency:** Requires Chocolatey  
- **Elevation:** CMD prompts for admin; UAC may display  
- **Silent Install:** `-y` flag prevents prompts  
- **Timing Delays:**  
  - Defaults: `DELAY 1000`, `DELAY 500`, `DELAY 1500`  
  - Adjust delays for slower systems

- **Version:** Installs latest Steam version via Chocolatey  
  - Check [Chocolatey Package Page](https://community.chocolatey.org/packages/steam) for current version

- **Testing Recommended:** VM/sandbox preferred prior to live deployment

---

## ⚖️ Disclaimer

Provided **as-is** for educational use only.  
Use strictly on devices you **own or have permission** to access.

---

## 📄 License

Licensed under the **MIT License**  
See [LICENSE](LICENSE) for full details

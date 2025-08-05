# Google Drive Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## ☁️ Overview

Installs [Google Drive for Desktop](https://www.google.com/drive/download/) via [Chocolatey](https://chocolatey.org/) silently, using **Flipper Zero’s BadUSB** keyboard emulation with **DuckyScript**.  
It opens elevated CMD and launches the install command without prompts.

> ⚠️ Requires Chocolatey to be installed prior to execution

---

## 🚀 Usage Instructions

### 1. Prepare the Script

- Save as: `install_googledrive.txt`

### 2. Upload to Flipper

- Connect via **USB/Bluetooth**
- Use **qFlipper** or **Flipper Mobile**
- Transfer to: `SD Card/badusb/`

### 3. Execute on Target

- On Flipper:  
  `Main Menu > Bad USB`
- Select: `install_googledrive.txt`
- Verify USB mode is active
- Connect Flipper to Windows machine
- Press **Run**

Script performs:
- Launches Run dialog  
- Elevates to CMD (UAC may prompt)  
- Executes install command via Chocolatey

---

## ✅ Verification

Google Drive installs automatically if:
- Chocolatey is present  
- Internet connection active  
- Admin privileges granted

---

## 📦 Requirements

- Windows 10/11  
- Chocolatey pre-installed  
- Flipper Zero w/ BadUSB enabled  
- Internet access  
- Admin rights  
- Google Drive-compatible system (lightweight)

---

## ⚙️ Technical Notes

- **Chocolatey Required:**  
  Must be installed prior to execution

- **Elevation / UAC:**  
  CMD elevated—UAC may appear

- **Silent Install:**  
  `-y` flag prevents user prompts

- **CMD Shell:**  
  Chosen for broader compatibility

- **Delay Heuristics:**  
  Defaults: `DELAY 1000`, `500`, `1500`  
  Slow systems: increase `DELAY` to `700+`

- **Version Installed:**  
  Installs latest stable Google Drive (as of August 2025)  
  See [Chocolatey Package Page](https://community.chocolatey.org/packages/googledrive)

- **Testing Strategy:**  
  Run in VM/sandbox before full deployment

---

## ⚖️ Disclaimer

For educational use only.  
Use responsibly on systems you **own or are authorized to modify**.  
Author assumes **no liability** for improper use.

---

## 📄 License

MIT License – see [LICENSE](LICENSE)

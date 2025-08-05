# Microsoft Visual C++ Redistributable Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧱 Overview

Installs [Microsoft Visual C++ Redistributable for Visual Studio 2015–2022](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) via [Chocolatey](https://chocolatey.org/)  
Built for **Flipper Zero’s BadUSB** via **DuckyScript**, simulating keystrokes to elevate CMD and perform silent install.

> ⚠️ Requires Chocolatey to be installed beforehand

---

## 🚀 Usage Instructions

### 1. Prepare the Script

- Save as: `install_vcredist140.txt`

### 2. Upload to Flipper

- Connect via **USB or Bluetooth**
- Use **qFlipper** or **Flipper Mobile**
- Upload to: `SD Card/badusb/`

### 3. Execute on Host

- Navigate: `Main Menu > Bad USB`
- Select: `install_vcredist140.txt`
- Confirm USB mode active (USB icon on Flipper screen)
- Plug into Windows host
- Press **Run**

Script will:
- Trigger Windows Run dialog  
- Launch elevated CMD (UAC may prompt)  
- Silently install Microsoft Visual C++ Redistributable

---

## ✅ Verification & Outcome

Installs automatically if:
- Chocolatey is installed  
- Internet connection available  
- Admin rights granted

---

## 📦 Requirements

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero w/ BadUSB  
- Internet access  
- Admin privileges  
- System compatibility (Visual C++ is lightweight)

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:** Must be installed first  
- **Elevation Handling:** CMD runs with admin rights; may trigger UAC  
- **Silent Installation:** `-y` flag used to suppress prompts  
- **Shell Compatibility:** CMD preferred over PowerShell  
- **Delay Profile:**  
  - Defaults: `DELAY 1000`, `500`, `1500`  
  - For slower machines: try `DELAY 700+`

- **Version Coverage:**  
  Installs Visual Studio 2015–2022 redistributable (vcredist140, ~14.x as of Aug 2025)  
  See [Chocolatey Package Page](https://community.chocolatey.org/packages/vcredist140)

- **Testing Environment:** VM/sandbox testing recommended

---

## ⚖️ Disclaimer

Educational script only.  
Use only on systems you **own or are authorized to modify**.  
Author assumes **no liability** for misuse or damage.

---

## 📄 License

MIT License – see [LICENSE](LICENSE)

# mIRC Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 💬 Overview

Installs [mIRC](https://www.mirc.com/), a legacy but still-popular IRC client, via [Chocolatey](https://chocolatey.org/) on Windows systems.  
Engineered for **Flipper Zero’s BadUSB** feature using **DuckyScript** to open elevated Command Prompt and execute a silent install.

> ⚠️ Chocolatey must be installed beforehand. See `install_chocolatey.txt`.

---

## 🚀 Usage Guide

### 1. Save the Payload

- Filename: `install_mirc.txt`  
- Format: UTF-8 encoded `.txt` for Flipper Zero BadUSB

### 2. Transfer to Flipper

- Use **qFlipper** or **Flipper Mobile App**
- Destination: `SD Card/badusb/`

### 3. Execute on Target Machine

- On Flipper:  
  `Main Menu > Bad USB` > `install_mirc.txt`  
- Connect to Windows machine via USB  
- Ensure USB mode is active (USB icon visible)  
- Press **Run**

Payload performs:
- Opens **Windows Run dialog**  
- Launches **elevated CMD** (UAC may be triggered)  
- Executes: `choco install mirc -y`

---

## ✅ Post-Install Verification

If Chocolatey is installed and internet is active:
- mIRC installs silently  
- No user interaction required  
- Version: Latest stable (e.g., 7.x as of August 2025)  
- Confirm via: [Chocolatey Package Page](https://community.chocolatey.org/packages/mirc)

---

## 📋 Requirements

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero with BadUSB enabled  
- Internet access for download  
- Admin rights to run elevated CMD  
- System compatibility with mIRC (typically lightweight)

---

## ⚙️ Payload Notes

- **Admin Privileges:**  
  Required for Chocolatey install; triggers elevated CMD

- **Silent Flag:**  
  `-y` ensures non-interactive install

- **Shell Selection:**  
  CMD chosen for compatibility

- **Timing Delays:**  
  - Standard: `DELAY 1000`, `500`, `1500`  
  - If unreliable: bump delays (`500` → `700+`)

- **Failure Modes:**  
  - Missing Chocolatey = abort  
  - Network outage = failed download  
  - UAC blocking = elevation failure

- **Sandbox Test First:**  
  Validate in a VM before deploying to physical systems

---

## ⚠️ Disclaimer

For educational purposes only.  
Use responsibly on systems you **own or are authorized to access**.  
Author assumes **no liability** for improper use or outcomes.

---

## 📄 License

Distributed under the **MIT License**  
See the [LICENSE](LICENSE) file for details.

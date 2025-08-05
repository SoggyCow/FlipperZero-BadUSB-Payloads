# TeamViewer Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🖥️ Overview

Automates the installation of [TeamViewer](https://www.teamviewer.com/)—a remote desktop and support tool—using [Chocolatey](https://chocolatey.org/)  
Built for **Flipper Zero’s BadUSB** feature using **DuckyScript** to elevate into CMD and install silently.

> ⚠️ **Note:** Chocolatey must be pre-installed. Run the Chocolatey installer script first.

---

## 🚀 Usage Instructions

Executed via **Flipper Zero keyboard emulation**.

### 1. Save the Script

- Save to `.txt` (e.g., `install_teamviewer.txt`)

### 2. Upload to Flipper Zero

- Connect via **USB/Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer to:  
  `SD Card/badusb/`

### 3. Run the Script

- Navigate: `Main Menu > Bad USB`
- Select `install_teamviewer.txt`
- Ensure USB mode is active
- Connect Flipper to target machine
- Tap **Run**

Flipper will:
- Open Windows Run dialog  
- Launch elevated CMD (UAC may prompt)  
- Execute Chocolatey install silently

---

## ✅ Verify Installation

- No interaction required post-launch  
- Installs if Chocolatey and internet access are available

---

## 📦 Prerequisites

- Windows 10/11  
- Chocolatey installed  
- Flipper Zero with BadUSB enabled  
- Internet connection  
- Admin rights  
- Basic system resources (TeamViewer is lightweight)

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Required prior to execution

- **UAC / Elevation Handling:**  
  CMD runs with admin rights—may prompt

- **Silent Install:**  
  `-y` flag suppresses user prompts

- **CMD vs. PowerShell:**  
  CMD used for broader system compatibility

- **Timing Delays:**  
  Baseline: `DELAY 1000`, `500`, `1500`  
  For slower machines: try `DELAY 700+`

- **Version Installed:**  
  Typically installs latest stable (e.g., 15.x in Aug 2025)  
  Verify at [Chocolatey Package Page](https://community.chocolatey.org/packages/teamviewer)

- **Testing Protocol:**  
  Run in VM or sandbox prior to live deployment

---

## ⚖️ Disclaimer

Use only on systems you **own or are authorized to access**.  
Author is not liable for misuse or system damage.

---

## 📄 License

MIT License – see [LICENSE](LICENSE)

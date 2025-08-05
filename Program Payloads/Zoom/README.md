# Zoom Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🎥 Overview

This script automates installation of [Zoom](https://zoom.us/), a leading video conferencing app, via [Chocolatey](https://chocolatey.org/) for Windows.  
It’s designed for Flipper Zero’s **BadUSB** function and leverages **DuckyScript** to simulate keystrokes, elevate to **Command Prompt (CMD)**, and silently deploy Zoom.

> ⚠️ **Important:** Chocolatey must be installed beforehand. Run the Chocolatey install script first.

---

## 🚀 Usage

Executed via Flipper Zero’s **BadUSB keyboard emulation**. Steps below:

### 1. Save Script

Save contents to a `.txt` file, e.g. `install_zoom.txt`.

### 2. Upload to Flipper Zero

- Connect Flipper via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer file to:  
  `SD Card/badusb/`

### 3. Deploy the Script

- On Flipper, navigate:  
  `Main Menu > Bad USB`
- Select `install_zoom.txt`
- Verify USB mode is active
- Connect Flipper to target Windows device
- Press **Run**

Script will:
- Open Windows Run dialog
- Trigger elevated CMD (UAC may prompt)
- Execute silent Zoom install via Chocolatey

---

## ✅ Installation Verification

Zoom installs silently if:
- Chocolatey is present
- Internet connection is active

---

## 📦 Prerequisites

- Windows OS  
- Chocolatey installed  
- Flipper Zero with BadUSB enabled  
- Internet access  
- Admin rights on target system

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Must be installed—install script required beforehand.

- **Elevation:**  
  CMD launched with admin privileges; may trigger UAC.

- **Silent Install:**  
  `-y` bypasses user prompts.

- **CMD Compatibility:**  
  Uses Command Prompt for broader system support—ensure CMD handles Chocolatey.

- **Execution Timing:**  
  Includes `DELAY 1000`, `DELAY 500`, `DELAY 1500`. Increase delays on slower devices (e.g. `DELAY 700`).

- **Testing Environment:**  
  Run on virtual machine or sandbox first to ensure predictable behavior.

---

## ⚖️ Disclaimer

Provided **as-is** for educational use only.  
Do **not** deploy without explicit system access rights.  
Author (SoggyCow) is **not responsible** for unintended outcomes.

---

## 📄 License

Licensed under the **MIT License**.  
Refer to [LICENSE](LICENSE) for details.

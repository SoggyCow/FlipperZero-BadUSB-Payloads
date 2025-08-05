# Python Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🐍 Overview

This script automates the installation of [Python](https://www.python.org/), a widely-used programming language, using [Chocolatey](https://chocolatey.org/) on Windows.  
It's designed for **Flipper Zero's BadUSB** function, using **DuckyScript** to simulate keystrokes, open an elevated **Command Prompt (CMD)**, and silently install Python.

> ⚠️ **Important:** Chocolatey must be installed prior to running this script. Use the Chocolatey installation script first.

---

## 🚀 Usage Instructions

The script executes through Flipper Zero’s **BadUSB keyboard emulation**.

### 1. Save Script

Save the payload to a `.txt` file (e.g., `install_python.txt`) compatible with Flipper Zero.

### 2. Upload to Flipper Zero

- Connect via **USB** or **Bluetooth**
- Use **qFlipper** or **Flipper Mobile App**
- Transfer to SD card path:  
  `SD Card/badusb/`

### 3. Deploy the Script

- On Flipper, go to:  
  `Main Menu > Bad USB`
- Select the `install_python.txt` script
- Ensure USB mode is active
- Connect Flipper to the target Windows machine
- Hit **Run**

Actions performed:
- Opens the Windows Run dialog
- Launches an elevated CMD (UAC prompt may appear)
- Runs Chocolatey install command for Python silently

---

## ✅ Installation Verification

Python installs silently without user interaction if:
- Chocolatey is present
- Internet connection is active

---

## 📦 Prerequisites

- Windows OS  
- Chocolatey installed  
- Flipper Zero with BadUSB enabled  
- Admin privileges on the target system  
- Internet access to fetch the Python package

---

## ⚙️ Notes & Considerations

- **Chocolatey Required:**  
  Script fails if Chocolatey isn’t already installed.

- **Admin Rights Needed:**  
  CMD launched with elevation; UAC prompt may appear.

- **Silent Install:**  
  The `-y` flag bypasses user confirmation.

- **CMD Usage:**  
  CMD is used for broader system compatibility—confirm Chocolatey functions correctly in CMD.

- **Execution Delays:**  
  Includes `DELAY 1000`, `DELAY 500`, `DELAY 1500`. For slower devices, consider increasing delays (e.g., to `DELAY 700`).

- **Python Version:**  
  The `python` package typically installs the latest Python 3.x (e.g., 3.12.x as of August 2025). Refer to [Chocolatey Python Package](https://community.chocolatey.org/packages/python) for version specifics.

- **Safe Testing:**  
  Run in a virtual machine before production use.

---

## ⚖️ Disclaimer

This script is intended for **educational purposes only**.  
Use responsibly and **only** on systems you own or have explicit permission to access.  
The author (SoggyCow) assumes **no liability** for any misuse, damage, or unintended outcomes.

---

## 📄 License

Distributed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full terms.

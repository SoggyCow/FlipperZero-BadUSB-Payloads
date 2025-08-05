# Adobe Acrobat Reader Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 📘 Overview

This script automates the installation of [Adobe Acrobat Reader](https://get.adobe.com/reader/), a widely-used PDF viewer, using [Chocolatey](https://chocolatey.org/), a Windows package manager.  
Built for Flipper Zero's **BadUSB** feature, it uses **DuckyScript** to simulate keyboard input, open an elevated **Command Prompt (CMD)**, and silently install Acrobat Reader.

> ⚠️ **Important:** This script assumes Chocolatey is already installed. Run the Chocolatey install script first.

---

## 🧪 Usage

This script runs via Flipper Zero's **BadUSB emulation**, which mimics a keyboard to execute commands.

### 1. Save the Script

Save the contents to a `.txt` file (e.g., `install_adobereader.txt`) compatible with Flipper Zero.

### 2. Upload to Flipper Zero

- Connect your Flipper via **USB** or **Bluetooth**
- Use the **qFlipper app** or **Flipper Mobile app**
- Transfer the file to:  
  `SD Card/badusb/`

### 3. Execute the Script

- On Flipper Zero, navigate to:  
  `Main Menu > Bad USB`
- Select the script (`install_adobereader.txt`)
- Confirm USB mode is active (USB logo visible)
- Connect Flipper to target Windows machine
- Press **Run**

The script will:
- Open the Windows Run dialog
- Launch an elevated Command Prompt (may trigger UAC)
- Run a Chocolatey command to silently install Acrobat Reader

---

## ✅ Installation Verification

Provided Chocolatey is installed and internet access is available, Acrobat Reader will install **without user interaction**.

---

## 📦 Prerequisites

- Windows OS
- Chocolatey pre-installed
- Flipper Zero with BadUSB functionality
- Internet connection
- Admin privileges on the target system

---

## ⚙️ Technical Notes

- **Chocolatey Dependency:**  
  Script will fail if Chocolatey is missing.

- **Elevation Required:**  
  CMD is launched with admin privileges; may prompt for UAC.

- **Silent Install:**  
  `-y` flag avoids user prompts.

- **CMD vs. PowerShell:**  
  This script uses CMD instead of PowerShell for broader compatibility.

- **Delay Calibration:**  
  Script uses: `DELAY 1000`, `DELAY 500`, `DELAY 1500`. Adjust for slower systems (e.g., `DELAY 700`).

- **Sandbox Testing:**  
  Run in a virtual environment before live deployment.

---

## ⚖️ Disclaimer

This script is provided **as-is** for educational purposes.  
Use only on systems you **own or have explicit permission** to access.  
The author (SoggyCow) is **not liable** for any misuse or resulting damage.

---

## 📄 License

Licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full terms.

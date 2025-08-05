# Node.js Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧭 Overview

This script automates the installation of [Node.js](https://nodejs.org/), a JavaScript runtime, using [Chocolatey](https://chocolatey.org/), a package manager for Windows. Designed for Flipper Zero's **BadUSB** feature, it uses **DuckyScript** to simulate keyboard inputs and silently execute a PowerShell command in a hidden window.

> ⚠️ **Important:** Chocolatey must be pre-installed on the target machine. Run the Chocolatey installation script first.

---

## 🚀 Usage

This script is intended for use with Flipper Zero's **BadUSB** functionality, which emulates a keyboard to execute commands.

### 1. Save the Script

Save the script to a `.txt` file (e.g., `install_nodejs.txt`) compatible with Flipper Zero.

### 2. Upload to Flipper Zero

- Connect your Flipper Zero to a computer via **USB** or **Bluetooth**
- Use the **qFlipper app** or **Flipper Mobile app** to transfer the script to:  
  `SD Card/badusb/`

### 3. Run the Script

- On Flipper Zero, navigate to:  
  `Main Menu > Bad USB`
- Select the script (`install_nodejs.txt`)
- Ensure USB mode is active (USB logo should be displayed)
- Connect Flipper Zero to the target Windows machine
- Press the **Run** button

The script will:
- Open the Windows Run dialog
- Execute a PowerShell command that installs Node.js silently via Chocolatey

---

## ✅ Verification

Node.js will install without user interaction, assuming:
- Chocolatey is installed
- Internet access is available

---

## 📦 Prerequisites

- A Windows operating system
- Chocolatey pre-installed
- Flipper Zero with BadUSB functionality enabled
- Internet connection to download Node.js
- Administrative privileges on the target machine

---

## ⚙️ Important Notes

- **Chocolatey Dependency:**  
  This script requires Chocolatey. If absent, the install will fail.
  
- **Administrative Privileges:**  
  Chocolatey needs admin rights—ensure the target account is elevated.

- **Silent Installation:**  
  `-y` flag ensures no user prompts.

- **Hidden Execution:**  
  PowerShell uses `-W Hidden` for discretion, though security software may flag it.

- **Timing Delays:**  
  Script uses `DELAY 1000` and `DELAY 500` for reliability. On slower systems, try `DELAY 700` or higher.

- **Testing First:**  
  Run in a VM or safe testbed before deploying live.

---

## ⚖️ Disclaimer

This script is provided as-is for **educational purposes only**. Use responsibly and **only on systems you own or have permission to access**.  
The author (SoggyCow) is **not responsible** for any misuse, data loss, or system damage.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

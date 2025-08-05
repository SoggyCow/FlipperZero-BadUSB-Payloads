# WinGet Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 📦 Overview

Installs **WinGet**, Microsoft’s command-line package manager, via [Chocolatey](https://chocolatey.org/) on Windows.  
Scripted for **Flipper Zero’s BadUSB**, this DuckyScript payload simulates keyboard input to elevate CMD, execute a silent install, and close the terminal post-deployment.

> ⚠️ Requires Chocolatey. Run `install_chocolatey.txt` before using this payload.

---

## 🧰 Usage Instructions

### 1. Save the Payload

- File name: `install_winget.txt`  
- Format: UTF-8 plain `.txt` (compatible with Flipper Zero)

### 2. Upload to Flipper Zero

- Connect via USB or Bluetooth  
- Transfer using **qFlipper** or **Flipper Mobile App**  
- Upload to:  
  `SD Card/badusb/`

### 3. Deploy on Target Machine

- On Flipper:  
  `Main Menu > Bad USB > install_winget.txt`  
- Ensure USB mode is active (USB icon visible)  
- Plug Flipper into a Windows machine  
- Tap **Run**

Payload executes:
- Opens Run dialog  
- Launches elevated CMD (`CTRL + SHIFT + ENTER`) — may trigger UAC  
- Runs:  
  `choco install winget -y && exit`

---

## ✅ Installation Confirmation

Success requires:
- Chocolatey installed and functional  
- Internet connection to pull Chocolatey packages  
- Admin rights for elevation  
- CMD compatibility with Chocolatey

Latest WinGet version (e.g., 1.x as of August 2025) is installed from Chocolatey:  
[Chocolatey Package: winget](https://community.chocolatey.org/packages/winget)

---

## 📋 Requirements

| Component             | Description                                     |
|-----------------------|-------------------------------------------------|
| OS                    | Windows 10/11 only (WinGet compatibility)       |
| Chocolatey            | Pre-installed                                   |
| Admin Privileges      | Required for elevated command execution         |
| Internet Access       | Required to download the package                |
| Flipper Zero          | BadUSB mode must be enabled                     |
| CMD Shell             | Must support Chocolatey commands                |

---

## ⚙️ Technical Notes

- **Timing Delays:**  
  Default: `DELAY 1000`, `500`, `1500`  
  Adjust upwards for slower machines (e.g., `DELAY 700+`)

- **Silent Install Flag:**  
  `-y` bypasses prompts  
  `&& exit` ensures terminal closure after execution

- **Redundancy Warning:**  
  WinGet may already be installed natively—this script enforces update via Chocolatey

- **Testing Recommendation:**  
  Run in virtual machine or sandbox before deploying in production environments

---

## ⚠️ Disclaimer

Use for **educational and authorized purposes only**.  
Run only on systems you **own or have explicit permission to modify**.  
Author assumes no liability for misuse or damage.

---

## 📄 License

Released under the **MIT License**  
See the `LICENSE` file for full terms.

# Macrium Reflect Free Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🔒 Overview

Automates installation of **Macrium Reflect Free**, a disk imaging and backup tool, using [Chocolatey](https://chocolatey.org/) and **Flipper Zero’s BadUSB** functionality.  
Payload simulates keyboard input to elevate CMD and run a silent install command.

> ⚠️ Requires prior installation of Chocolatey. Use `install_chocolatey.txt`.

---

## ⚙️ Setup & Execution

### 1. Save Script

- File name: `install_reflect-free.txt`  
- Format: Plain `.txt`, UTF-8 encoded

### 2. Upload to Flipper

- Connect via USB or Bluetooth  
- Transfer via **qFlipper** or **Flipper Mobile App**  
- Destination path:  
  `SD Card/badusb/`

### 3. Execute on Target

- On Flipper:  
  `Main Menu > Bad USB > install_reflect-free.txt`  
- Confirm USB logo is displayed (USB mode active)  
- Plug Flipper into target Windows machine  
- Tap **Run**

Script flow:
- Opens Windows Run dialog  
- Elevates CMD (`CTRL + SHIFT + ENTER`) — may invoke UAC  
- Executes:  
  `choco install reflect-free -y`

---

## 📦 Installation Checklist

| Component                 | Requirement/Note                                     |
|---------------------------|------------------------------------------------------|
| OS                        | Windows 10/11                                        |
| Chocolatey                | Must be pre-installed                                |
| Admin Privileges          | Required to run elevated CMD                         |
| Internet Access           | Necessary for package retrieval                      |
| CMD Compatibility         | CMD must support Chocolatey commands                 |
| RAM/Disk Space            | Minimum 1 GB RAM / 500 MB disk space (verify specs)  |
| Script Delays             | `DELAY 1000`, `500`, `1500` (tune for slower systems)|

---

## 🛠 Technical Notes

- **Elevation Handling:**  
  Simulates `CTRL + SHIFT + ENTER`; may prompt UAC

- **Silent Deployment:**  
  Uses `-y` switch for no user interaction

- **Timing Adjustments:**  
  Tune delays upward (`500 ➞ 700+`) if timing issues arise

- **Chocolatey Package:**  
  Installs latest version (e.g., 8.x as of August 2025)  
  Check Chocolatey package: [reflect-free](https://community.chocolatey.org/packages/reflect-free)

- **Sandbox Testing:**  
  Recommended before live use (e.g., on virtual machines)

---

## ⚠️ Disclaimer

Use responsibly on devices you **own or have permission to modify**.  
This payload is offered for **educational purposes**, without warranty.  
Author assumes no liability for unintended effects.

---

## 📄 License

Distributed under the **MIT License**  
See included `LICENSE` file for details

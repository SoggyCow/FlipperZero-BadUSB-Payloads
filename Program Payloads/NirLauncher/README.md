# NirLauncher Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🛠️ Overview

Installs **NirLauncher**, a bundle of 200+ portable utilities from NirSoft for diagnostics, password recovery, and network monitoring.  
Uses Flipper Zero’s **BadUSB** DuckyScript to simulate keyboard input, elevate CMD, and execute a **silent Chocolatey install**.

> ⚠️ Requires Chocolatey installed beforehand. Use `install_chocolatey.txt`.

---

## 🐛 Use Case

Perfect for forensic and adversarial workstations needing compact tooling for password analysis, system audit, and utility benchmarking—without heavy installs.

---

## 📦 Execution Steps

### 1. Save Payload

- File: `install_nirlauncher.txt`  
- Encoding: Plain `.txt`, UTF-8

### 2. Transfer to Flipper

- Connect Flipper via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Upload to:  
  `SD Card/badusb/`

### 3. Launch on Target System

- On Flipper:  
  `Main Menu > Bad USB > install_nirlauncher.txt`  
- Confirm USB mode (USB icon shown)  
- Plug into target Windows machine  
- Tap **Run**

Payload simulates:
- `Win + R` ➞ Open Run dialog  
- `cmd` + `CTRL + SHIFT + ENTER` ➞ Elevate  
- Run command:  
  `choco install nirlauncher -y`

---

## ✅ Requirements Matrix

| Component             | Requirement                                           |
|-----------------------|--------------------------------------------------------|
| OS                    | Windows 10/11                                          |
| Chocolatey            | Must be installed first                                |
| Admin Privileges      | Required for elevated install                          |
| Internet Access       | Needed to fetch package                                |
| CMD Compatibility     | Supports Chocolatey commands                           |
| System Specs          | Lightweight; check NirSoft specs                       |

---

## ⚙️ Technical Notes

- **Timing Delays:**  
  `DELAY 1000`, `500`, `1500` — increase for slower systems (`700+`)

- **Silent Install:**  
  `-y` flag avoids user prompts

- **Elevation Trigger:**  
  `CTRL + SHIFT + ENTER` may prompt UAC

- **Package Version:**  
  Chocolatey installs latest stable NirLauncher (e.g., 1.x in Aug 2025)

- **Security Concerns:**  
  Some NirSoft utilities may be flagged by antivirus—intended use must be ethical and authorized

- **VM Testing:**  
  Strongly recommended before field deployment

---

## ⚠️ Disclaimer

Use this script **only** on systems you **own or have explicit permission** to access.  
Certain utilities bundled in NirLauncher may raise software or legal concerns if misused.  
Author is not liable for misuse or breach of terms.

---

## 📄 License

Licensed under the **MIT License**  
See included `LICENSE` file for full terms

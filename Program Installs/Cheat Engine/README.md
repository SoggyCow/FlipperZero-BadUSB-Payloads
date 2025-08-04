# Cheat Engine Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🎯 Overview

Installs [Cheat Engine](https://cheatengine.org/), an open-source memory scanner, debugger, and trainer-building utility widely used for educational and development purposes.  
This payload leverages **Flipper Zero’s BadUSB** interface via **DuckyScript** to simulate keystrokes, elevate CMD, and trigger a silent install using [Chocolatey](https://chocolatey.org/).

> ⚠️ Requires Chocolatey to be pre-installed. Run `install_chocolatey.txt` first.

---

## 🚀 Deployment Instructions

### 1. Prepare the Payload

- Filename: `install_cheatengine.txt`  
- Format: UTF-8 `.txt` compatible with Flipper Zero BadUSB

### 2. Upload to Flipper Zero

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Copy to:  
  `SD Card/badusb/`

### 3. Execute on Target Machine

- On Flipper:  
  `Main Menu > Bad USB > install_cheatengine.txt`  
- Ensure USB mode is active (USB icon visible)  
- Connect Flipper to Windows target  
- Press **Run**

Script actions:
- Opens Windows Run dialog  
- Launches elevated CMD (UAC prompt may appear)  
- Executes:  
  `choco install cheatengine -y`

---

## ✅ Post-Install Validation

- No user interaction required  
- Latest stable release (e.g., 7.x as of August 2025)  
- See Chocolatey: [cheatengine package](https://community.chocolatey.org/packages/cheatengine)

---

## 📋 Requirements

| Requirement              | Description                                       |
|--------------------------|---------------------------------------------------|
| Windows Version          | Windows 10/11                                     |
| Chocolatey Installed     | Must be pre-installed                             |
| Admin Privileges         | Required for elevation                            |
| Internet Connection      | Required to download Cheat Engine                 |
| Flipper Zero             | BadUSB enabled and functional                     |
| CMD Compatibility        | Must support Chocolatey                          |
| Cheat Engine Requirements| See official documentation for system specs       |

---

## ⚙️ Technical Notes

- **Shell Compatibility:** Uses CMD for maximum deployment reach  
- **Privilege Elevation:** May trigger UAC depending on system security  
- **Silent Execution:** `-y` flag ensures hands-free installation  
- **Timing Delays:**  
  - Defaults: `DELAY 1000`, `500`, `1500`  
  - Increase delays for sluggish systems (e.g., `DELAY 700+`)  
- **Testing Protocol:** Validate in sandbox or VM prior to live deployment

---

## ⚠️ Responsible Use

Cheat Engine can be flagged by game anti-cheat mechanisms.  
Deploy **only** in environments where usage is legal, ethical, and **explicitly permitted**.  
Intended for debugging, education, and software analysis—not for bypassing safeguards.

---

## 📄 License

Licensed under the **MIT License**  
See the `LICENSE` file for full details.

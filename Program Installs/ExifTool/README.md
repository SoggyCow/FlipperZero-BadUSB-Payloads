# ExifTool Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧠 Overview

Installs [ExifTool](https://exiftool.org/), a robust command-line utility for reading, writing, and manipulating metadata across file formats (images, documents, audio, etc.), using [Chocolatey](https://chocolatey.org/).  
Purpose-built for **Flipper Zero’s BadUSB**, this payload uses **DuckyScript** to simulate keystrokes, elevate CMD, and deploy a silent install.

> ⚠️ Requires Chocolatey pre-installed. Use `install_chocolatey.txt` prior to execution.

---

## 🚀 Deployment Instructions

### 1. Prepare Script

- Save as: `install_exiftool.txt`  
- Format: UTF-8 `.txt` compatible with Flipper Zero

### 2. Upload to Flipper

- Connect via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile**  
- Path:  
  `SD Card/badusb/`

### 3. Execute on Target

- Navigation:  
  `Main Menu > Bad USB > install_exiftool.txt`  
- Confirm USB mode active  
- Plug into target Windows machine  
- Press **Run**

Payload flow:
- Opens Windows Run dialog  
- Elevates to CMD (may show UAC prompt)  
- Executes:  
  `choco install exiftool -y`

---

## ✅ Post-Install Confirmation

- No user input required  
- Installs latest stable version (12.x+ as of Aug 2025)  
- Requires Chocolatey and internet connectivity  
- Chocolatey page: [ExifTool Package](https://community.chocolatey.org/packages/exiftool)

---

## 📋 Requirements

| Requirement                        | Description                                  |
|------------------------------------|----------------------------------------------|
| OS                                 | Windows 10/11                                |
| Chocolatey                         | Must be installed                            |
| Admin Privileges                   | Required                                     |
| Internet Connection                | Needed for package download                  |
| Flipper Zero with BadUSB           | Functional and active                        |
| CMD Compatibility                  | CMD must support Chocolatey                  |

---

## ⚙️ Technical Considerations

- **Elevation Prompt:**  
  UAC may appear if system defaults require confirmation

- **Silent Install:**  
  `-y` bypasses prompts and proceeds automatically

- **Delays Used:**  
  Defaults: `DELAY 1000`, `500`, `1500`  
  Adjust for slower systems as needed (e.g., `DELAY 700+`)

- **Testing Strategy:**  
  Always validate in controlled VM or test rig before live use

---

## ⚠️ Disclaimer

For educational use only.  
Deploy only on systems you **own or are authorized to control**.  
The author assumes no liability for misuse or effects caused by execution.

---

## 📄 License

Licensed under the **MIT License**  
See `LICENSE` file for full terms.

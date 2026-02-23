# Visual C++ Redistributable 2015 Update 3 Installer via Chocolatey

**Author:** SoggyCow  
**License:** MIT

---

## 🧩 Overview

Installs the **Microsoft Visual C++ Redistributable for Visual Studio 2015 Update 3**, required for many C++ applications.  
Built for **Flipper Zero’s BadUSB** using **DuckyScript**, this payload automates silent deployment via **elevated CMD** using [Chocolatey](https://chocolatey.org/).

> ⚠️ Ensure Chocolatey is installed beforehand (`install_chocolatey.txt` module required).

---

## 🛠️ Usage Instructions

### 1. Save Payload

- File name: `install_vcredist2015.txt`  
- Encoding: UTF-8 plain `.txt` file (Flipper-compatible)

### 2. Upload to Flipper

- Use **qFlipper** or **Flipper Mobile App**  
- Path: `SD Card/badusb/`

### 3. Deploy on Target

- On Flipper:  
  `Main Menu > Bad USB > install_vcredist2015.txt`  
- Confirm USB mode active (USB icon visible)  
- Connect to Windows machine  
- Tap **Run**

Execution Flow:
- Launches Windows Run dialog  
- Elevates to admin CMD (CTRL+SHIFT+ENTER) — triggers UAC if active  
- Runs:  
  `choco install vcredist2015 -y`

---

## 🧪 Verification & Requirements

| Requirement               | Description                                           |
|---------------------------|--------------------------------------------------------|
| Windows OS                | Windows 10/11                                          |
| Chocolatey                | Must be installed beforehand                           |
| Admin Privileges          | Required for elevated install                          |
| Internet Connectivity     | Required for Chocolatey package retrieval              |
| CMD Compatibility         | Must accept Chocolatey commands                        |
| Runtime Dependencies      | Supports VS 2015-built C++ apps                        |

---

## ⚙️ Technical Notes

- **Silent Install:**  
  `-y` flag enables non-interactive installation

- **Delays for Reliability:**  
  `DELAY 1000`, `500`, `1500` tuned for average systems  
  Increase delays if failure occurs on slower hosts

- **Package Version:**  
  Latest stable Visual C++ Redistributable 2015 Update 3 (check [Chocolatey package](https://community.chocolatey.org/packages/vcredist2015))

- **Testing Recommendation:**  
  Use VM or sandbox first to verify payload behavior

---

## ⚠️ Disclaimer

Use only on systems with **explicit authorization**.  
Author provides no warranties; script is delivered **as-is**. Improper use may result in unintended system changes.

---

## 📄 License

Released under the **MIT License**  
See attached `LICENSE` file for full legal terms.

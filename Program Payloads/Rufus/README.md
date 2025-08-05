# Rufus Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🛠 Overview

Deploys [Rufus](https://rufus.ie)—the trusted utility for creating bootable USB drives—via [Chocolatey](https://chocolatey.org/) on Windows using **Flipper Zero’s BadUSB** functionality.  
Scripted in **DuckyScript**, it simulates keystrokes to open an elevated CMD and perform a silent Rufus install.

> ⚠️ Requires Chocolatey pre-installed. See `install_chocolatey.txt`.

---

## 🔧 Usage

### 1. Prepare Payload

- File name: `install_rufus.txt`  
- Format: UTF-8 `.txt` for Flipper Zero compatibility

### 2. Upload to Flipper Zero

- Connect via USB/Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Transfer to:  
  `SD Card/badusb/`

### 3. Deploy on Target System

- From Flipper Menu:  
  `Main Menu > Bad USB > install_rufus.txt`  
- Confirm USB mode is active  
- Connect to target system  
- Run the script to:

Execution Steps:
- Open Windows Run dialog  
- Launch elevated CMD (UAC may appear)  
- Execute:  
  `choco install rufus -y`

---

## ✅ Verification

Rufus installs automatically assuming:
- Chocolatey is present  
- Internet connection available  
- Admin privileges granted  
- CMD compatible with Chocolatey

---

## 🧾 Requirements

| Component            | Details                                              |
|---------------------|------------------------------------------------------|
| Windows OS          | Windows 10/11 recommended                            |
| Chocolatey          | Must be installed beforehand                         |
| Admin Privileges    | Needed for install                                    |
| Internet Access     | Required to fetch Chocolatey package                 |
| Flipper Zero        | BadUSB functionality enabled                         |
| CMD Compatibility   | Chocolatey must work from command line               |
| Rufus Compatibility | Generally lightweight—check vendor documentation     |

---

## 🧪 Deployment Tips

- **Timing Delays:**  
  Default delays: `DELAY 1000`, `500`, `1500`  
  Tune delays for slower hosts (e.g. `DELAY 700+`)

- **Silent Install:**  
  `-y` flag ensures no user prompts

- **Elevation Method:**  
  Simulates `CTRL + SHIFT + ENTER` to elevate CMD (triggers UAC)

- **Chocolatey Check:**  
  If install fails, verify Chocolatey presence via:  
  `choco -v`

- **Package Version:**  
  Rufus typically installs v4.x+ — verify at:  
  [Chocolatey Rufus Package](https://community.chocolatey.org/packages/rufus)

- **Safe Testing:**  
  Recommend sandbox or virtual machine for dry runs

---

## ⚠️ Disclaimer

Provided **as-is** for educational/authorized use only.  
Use on machines you **own or are authorized** to configure.  
The author disclaims liability for misuse or unintended effects.

---

## 📄 License

Licensed under the **MIT License**  
Refer to the `LICENSE` file for full terms.

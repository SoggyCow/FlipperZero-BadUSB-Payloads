# IDA Free Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🧠 Overview

Installs **IDA Free**, Hex-Rays' respected disassembler and reverse engineering suite, via [Chocolatey](https://chocolatey.org/) using **Flipper Zero’s BadUSB** functionality.  
Written in **DuckyScript**, the payload simulates elevated keyboard input to silently deploy IDA Free on Windows systems.

> ⚠️ Requires prior installation of Chocolatey. Refer to `install_chocolatey.txt` in your payload stack.

---

## 🔧 Usage

### 1. Save & Upload

- Save as: `install_ida-free.txt`  
- Format: UTF-8 `.txt` for Flipper Zero compatibility  
- Upload using **qFlipper** or **Flipper Mobile App** to:  
  `SD Card/badusb/`

### 2. Deploy via Flipper Zero

- Path: `Main Menu > Bad USB > install_ida-free.txt`  
- Ensure USB mode is active (USB logo visible)  
- Connect to target Windows host  
- Press **Run** to initiate:

Execution Steps:
- Opens Windows Run dialog  
- Elevates CMD via simulated `CTRL + SHIFT + ENTER` (may trigger UAC)  
- Executes:  
  `choco install ida-free -y`

---

## ✅ Installation Confirmation

Successful if:
- Chocolatey is installed and functioning  
- System has internet connectivity  
- CMD accepts Chocolatey commands  
- Admin privileges granted

---

## 📋 Requirements

| Component           | Details                                                   |
|---------------------|------------------------------------------------------------|
| OS                  | Windows 10/11, 64-bit required for IDA Free               |
| Chocolatey          | Must be installed beforehand                              |
| Admin Privileges    | Required for elevation                                    |
| Internet Access     | Needed to fetch IDA Free via Chocolatey                   |
| Flipper Zero        | With BadUSB functionality enabled                         |
| System Specs        | Minimum: 4 GB RAM, 1 GB disk; verify via Hex-Rays docs    |
| CMD Shell           | Must support Chocolatey execution                         |

---

## ⚙️ Technical Notes

- **Delay Tuning:**  
  Uses `DELAY 1000`, `500`, `1500` for reliability  
  Adjust for slower systems (`DELAY 700+` if needed)

- **Elevation Method:**  
  Simulates `CTRL + SHIFT + ENTER` to trigger elevated CMD  
  May prompt UAC

- **Silent Install Flag:**  
  `-y` ensures no prompts during install

- **Package Versioning:**  
  Installs latest available IDA Free (e.g., v8.x as of August 2025)  
  Validate on [Chocolatey Package Page](https://community.chocolatey.org/packages/ida-free)

- **Controlled Testing:**  
  Run in a sandbox or VM before deploying on live hosts

---

## 🔐 Responsible Use

IDA Free is a powerful reverse engineering tool.  
Use only for legitimate educational or security research purposes.  
Respect software licensing and local laws.

---

## ⚠️ Disclaimer

This script is provided **as-is** for educational use.  
Use only on systems you **own or have explicit authorization** for.  
The author (SoggyCow) is not liable for any misuse or resulting damage.

---

## 📄 License

Released under the **MIT License**  
See accompanying `LICENSE` file for full terms.

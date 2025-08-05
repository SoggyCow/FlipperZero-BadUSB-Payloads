# 🔐 Proton VPN Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT License

---

## 📦 Overview

This script automates installation of [Proton VPN](https://protonvpn.com), a security-focused VPN client, using [Chocolatey](https://chocolatey.org) on Windows.  
Built for use with Flipper Zero’s **BadUSB** feature, it uses DuckyScript to simulate keyboard input and execute a PowerShell command silently in a hidden window.

> ⚠️ **Important**: Chocolatey must be installed _prior_ to running this script.

---

## 🚀 Usage Instructions

Designed for Flipper Zero’s BadUSB mode (keyboard emulation):

### 1. Save the Script
Save the DuckyScript as a `.txt` file, e.g., `install_protonvpn.txt`.

### 2. Transfer to Flipper Zero
- Connect via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile** to upload the script to:  
  `SD Card/badusb/install_protonvpn.txt`

### 3. Execute the Script
- On Flipper Zero:  
  Navigate to `Main Menu > Bad USB`
- Select `install_protonvpn.txt`.
- Confirm **USB mode** is active (USB icon should be displayed).
- Plug Flipper Zero into the target Windows machine.
- Press **Run** — the payload will:
  - Launch Windows Run dialog (`Win + R`)
  - Run a hidden PowerShell command that installs Proton VPN via Chocolatey

### ✅ Verification
If Chocolatey is installed and internet access is available, Proton VPN will be installed automatically.

---

## 🧰 Requirements

- Windows operating system  
- Chocolatey pre-installed  
- Flipper Zero with BadUSB capability  
- Internet connection on target machine  
- Admin privileges for software installation

---

## ⚠️ Notes & Caveats

- **Chocolatey Dependency**: You must install Chocolatey first.  
- **Admin Rights**: Required to execute the install successfully.  
- **Silent Install**: The `-y` flag suppresses user prompts.  
- **Stealth Mode**: PowerShell runs hidden (`-W Hidden`), but AV software (e.g. Defender) may flag the behavior.  
- **Timing Reliability**: Script includes `DELAY 1000` and `DELAY 500`. On slow systems, increase these (e.g. to `DELAY 700`).  
- **Testing**: Run in a sandbox or VM environment first to verify behavior safely.

---

## ⚖️ Disclaimer

This script is offered **as-is** for educational purposes only.  
Use it responsibly — only on systems you own or have **explicit authorization** to access.  
The author (**SoggyCow**) is not liable for misuse, data loss, or damages.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

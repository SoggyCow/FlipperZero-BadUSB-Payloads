# Recuva Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 📦 Overview

Installs [Recuva](https://www.ccleaner.com/recuva), a user-friendly data recovery tool for retrieving deleted files from HDDs, USB drives, SD cards, and more.  
Engineered for **Flipper Zero’s BadUSB** using **DuckyScript**.  
Script launches elevated **CMD**, then uses **Chocolatey** for silent deployment.

> 🔔 Chocolatey **must be installed** prior to running this payload.

---

## 🎮 Usage Instructions

### 1. Prepare the Payload

- Filename: `install_recuva.txt`  
- Format: `.txt` compatible with Flipper Zero

### 2. Transfer to Device

- Connect via USB/Bluetooth  
- Use **qFlipper** or **Flipper Mobile App**  
- Target directory:  
  `SD Card/badusb/`

### 3. Execution Flow

- Navigate:  
  `Main Menu > Bad USB > install_recuva.txt`
- Confirm: USB mode enabled (USB icon visible)  
- Plug into target Windows system  
- Press **Run**

Payload performs:
- Opens **Run dialog**  
- Elevates to **Admin CMD**  
- Executes silently:  
  `choco install recuva -y`

---

## ✔️ Verification Steps

- Recuva installs without prompts  
- Latest version deployed (e.g. 1.53+)  
- Target system must have internet access  
- View Chocolatey listing: [chocolatey.org/packages/recuva](https://community.chocolatey.org/packages/recuva)

---

## ⚙️ Requirements

- Windows 10/11  
- Chocolatey pre-installed  
- Flipper Zero BadUSB enabled  
- Internet connection  
- Admin rights  
- CMD compatibility with Chocolatey

---

## 🧪 Notes & Adjustments

- **Delays Used:**  
  `DELAY 1000`, `500`, `1500`  
  ⏱ Increase delay values for slower hosts: try `700+`

- **Elevation Trigger:**  
  Uses `CTRL-SHIFT ENTER`; UAC dialog may appear

- **Silent Install:**  
  `-y` flag bypasses prompts

- **Testing Recommendation:**  
  Verify payload in VM or sandboxed machine first

---

## ⚠️ Disclaimer

This payload is provided **as-is** for educational use.  
Use only on systems you **own or are authorized to access**.  
No responsibility taken for misuse or system impact.

---

## 📄 License

Licensed under the **MIT License**  
See [LICENSE](LICENSE) for terms

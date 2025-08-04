# Discord Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 💬 Overview

Deploys **Discord**, the ubiquitous voice and chat platform for gamers and communities, via [Chocolatey](https://chocolatey.org/) on Windows.  
Tailored for **Flipper Zero’s BadUSB**, this payload uses **DuckyScript** to simulate keystrokes that open an elevated command prompt and execute a silent install of Discord.

> ⚠️ Requires Chocolatey installed prior to execution. See `install_chocolatey.txt`.

---

## 🧰 Usage Instructions

### 1. Save the Payload

- Filename: `install_discord.txt`  
- Encoding: UTF-8 plain text `.txt`

### 2. Upload to Flipper

- Connect Flipper Zero via USB or Bluetooth  
- Use **qFlipper** or **Flipper Mobile**  
- Upload to: `SD Card/badusb/`

### 3. Execute on Target Windows Host

- Navigate: `Main Menu > Bad USB > install_discord.txt`  
- Confirm USB mode is active (USB icon displayed)  
- Plug into target system  
- Press **Run** to initiate:

Execution Flow:
- Triggers Windows Run dialog  
- Launches elevated CMD (`CTRL + SHIFT + ENTER`)  
- Executes command:  
  `choco install discord.install -y`

---

## ✅ Installation Confirmation

Successful if:
- Chocolatey is pre-installed  
- Internet connection is available  
- Admin privileges are granted  
- CMD shell accepts Chocolatey commands

---

## 📋 Requirements

| Component             | Description                                           |
|-----------------------|-------------------------------------------------------|
| Windows OS            | Windows 10/11 recommended                            |
| Chocolatey            | Pre-installed                                         |
| Admin Privileges      | Required for elevation and install                   |
| Internet Connection   | Needed to pull Discord package from repository       |
| Flipper Zero          | Must have BadUSB enabled and working                 |
| System Specs          | Minimum 4 GB RAM; check [Discord system requirements](https://support.discord.com/hc/en-us/articles/1500000182362) |
| CMD Compatibility     | Must be able to run Chocolatey commands              |

---

## ⚙️ Technical Considerations

- **Silent Flag:**  
  `-y` suppresses user prompts during installation

- **Timing Delays:**  
  `DELAY 1000`, `500`, `1500` used for reliability  
  Tune delays (e.g., `DELAY 700+`) for slower hosts

- **Elevation Method:**  
  Simulates `CTRL + SHIFT + ENTER`  
  May trigger UAC prompt (if enabled)

- **Package Check:**  
  Confirms installation of latest stable Discord version (e.g., v1.x as of Aug 2025)  
  Chocolatey page: [discord.install](https://community.chocolatey.org/packages/discord.install)

- **Testing Recommendation:**  
  Verify payload in sandbox or VM before live deployment

---

## 🚨 Disclaimer

This script is distributed **as-is**, intended for educational use only.  
Use only on systems you **own or are explicitly authorized** to modify.  
The author (SoggyCow) is not responsible for misuse or unintended outcomes.

---

## 📄 License

Released under the **MIT License**  
Refer to the `LICENSE` file for complete terms.

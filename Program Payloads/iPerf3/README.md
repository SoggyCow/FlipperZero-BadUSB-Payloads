# iPerf3 Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 🌐 Overview

Automates installation of **iPerf3**, a lightweight, open-source utility for testing network throughput and performance.  
Uses **Flipper Zero’s BadUSB** DuckyScript to simulate keyboard input, launch elevated CMD, and run Chocolatey install command.

> ⚠️ Requires Chocolatey pre-installed (`install_chocolatey.txt` should be run first)

---

## 🧪 Use Case

Ideal for network diagnostics, bandwidth benchmarking, or validating tunnel throughput.  
This script can be paired with client/server deployments for LAN/WAN profiling.

---

## 📦 Setup & Execution

### 1. Save the Script

- File name: `install_iperf3.txt`  
- Encoding: Plain `.txt`, UTF-8

### 2. Upload to Flipper Zero

- Connect via USB/Bluetooth  
- Transfer via **qFlipper** or **Flipper Mobile**  
- Path:  
  `SD Card/badusb/`

### 3. Execute on Target Windows System

- Flipper navigation:  
  `Main Menu > Bad USB > install_iperf3.txt`  
- Confirm USB mode active (USB icon visible)  
- Plug Flipper into target host  
- Tap **Run**

Payload actions:
- Launches Run dialog  
- Opens elevated CMD (`CTRL + SHIFT + ENTER`)  
- Executes:  
  `choco install iperf3 -y`

---

## 🔍 Installation Checklist

| Item                    | Detail                                            |
|-------------------------|----------------------------------------------------|
| OS                      | Windows 10/11 recommended                          |
| Chocolatey              | Required prior to execution                        |
| Admin Privileges        | Required for elevated CMD                          |
| Internet Connectivity   | Necessary for package retrieval                    |
| CMD Compatibility       | Should support Chocolatey commands                 |
| System Requirements     | Lightweight; see [iperf3 specs](https://iperf.fr)  |

---

## ⚙️ Technical Notes

- **Timing Delays:**  
  Uses `DELAY 1000`, `500`, `1500` — adjust upward for slower machines

- **Elevation Protocol:**  
  Simulates `CTRL + SHIFT + ENTER`, may trigger UAC

- **Silent Install Flag:**  
  `-y` ensures no user prompts

- **Chocolatey Repository Status:**  
  Installs latest stable `iperf3` (typically 3.x as of August 2025)  
  Check package: [iperf3 on Chocolatey](https://community.chocolatey.org/packages/iperf3)

- **Test Environment Recommendation:**  
  Initial deployment should be tested in VM/sandbox

---

## ⚠️ Disclaimer

This script is provided **as-is** for educational use only.  
Run on devices you **own or have permission to modify**.  
Author assumes no responsibility for misuse or consequences.

---

## 📄 License

Distributed under the **MIT License**  
See included `LICENSE` file for details

# All Apps Installation Script via Chocolatey for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

---

## 📦 Overview

Deploys a wide array of tools—dev platforms, security utilities, cloud clients, and system optimizers—using **Chocolatey** via **Flipper Zero’s BadUSB**. The script uses **DuckyScript** to simulate keyboard input, escalate to admin CMD, and mass-install packages silently.

> ⚠️ Chocolatey must be pre-installed (see `install_chocolatey.txt` payload).

---

## 🛠️ Usage Instructions

### 1. Save Payload

- Filename: `install_all_apps.txt`  
- Encoding: UTF-8 `.txt` (Flipper-compatible)

### 2. Upload to Flipper

- Use qFlipper or Flipper Mobile  
- Path: `SD Card/badusb/`

### 3. Execute Payload

- Menu path:  
  `Main Menu > Bad USB > install_all_apps.txt`  
- Confirm USB mode is active  
- Connect Flipper to Windows target  
- Tap **Run**

Execution Flow:
- Opens Run dialog  
- Launches elevated CMD (CTRL+SHIFT+ENTER) — triggers UAC  
- Updates Chocolatey  
- Installs all packages with:  
  `choco install [packages] -y --ignore-checksums`

---

## 📋 Included Applications

Grouped by function for tactical indexing:

| Category           | Packages                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------|
| Dev Tools          | git, visualstudio2022community, python, nodejs, innosetup, resourcehacker                            |
| Reverse Engineering| ida-free, hxd, cheatengine, exiftool                                                                 |
| Comms & Cloud      | discord, googledrive, dropbox, zoom, protonvpn, thunderbird                                         |
| Remote Control     | teamviewer, anydesk, parsec, putty                                                                   |
| System Tools       | bleachbit, crystaldiskinfo, 7zip, quickcpu, macrium-reflect, tailscale, recuva, testdisk            |
| Media              | vlc, paint.net, renamemytvseries2                                                                    |
| Gaming             | steam, epicgameslauncher                                                                             |
| Containerization   | docker-desktop                                                                                       |
| Runtime Libraries  | vcredist2015, vcredist140, javaruntime                                                               |
| Security & Privacy | protonpass, protondrive, bleachbit, nirlauncher                                                     |
| Bandwidth Tools    | iperf3, wireshark                                                                                     |
| Miscellaneous      | notepadplusplus, rufus, easeus-partition-master, mirc                                               |
| Build & Format     | filezilla, innosetup                                                                                 |

> ⚠️ Packages such as `protonpass`, `quickcpu`, `easeus-partition-master`, etc., may not be available on Chocolatey as of August 2025. Verify before deployment.

---

## 🔐 Requirements

| Component            | Notes                                                                 |
|----------------------|-----------------------------------------------------------------------|
| OS                   | Windows 10/11                                                         |
| Chocolatey           | Must be pre-installed                                                 |
| Admin Privileges     | Required for CMD escalation                                           |
| Internet Connection  | Required for package fetch                                            |
| CMD Compatibility    | Must support Chocolatey syntax                                        |
| Target Readiness     | Test in VM or sandbox before live deployment                         |

---

## ⚙️ Technical Insights

- **Silent Install:**  
  Uses `-y` and `--ignore-checksums` for non-interactive deployment

- **Delays Used:**  
  `DELAY 1000`, `500`, `1500`—tune for system latency

- **Timing Failures:**  
  Increase delays for slow boots or UAC latency (`700+` recommended)

- **Versioning:**  
  Installs latest stable Chocolatey packages (check [Chocolatey](https://community.chocolatey.org/) per app)

- **Risk Notes:**  
  Tools like `cheatengine`, `ida-free`, and `nirlauncher` may trigger antivirus heuristics

---

## ⚠️ Disclaimer

Educational use only. Author assumes no liability for misuse, unintended system changes, or violations of EULAs. Always test safely and deploy ethically.

---

## 📄 License

This payload is distributed under the **MIT License**  
See the accompanying `LICENSE` file for details.

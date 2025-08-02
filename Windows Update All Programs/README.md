# 🛠 Winget Auto-Upgrader  
**Flipper Zero BadUSB Script for Automated Windows Package Updates**

## 🧰 Overview  
This script automates application updates on Windows 10/11 via `winget`, leveraging Flipper Zero's BadUSB capabilities. It simulates keypresses to open the Command Prompt, execute `winget upgrade --all`, and confirm the upgrade prompt—all without manual input.

## ✨ Features  
- 🔧 Simulates `Win + R` to launch the Run dialog  
- 🖥️ Opens `cmd` and executes: `winget upgrade --all`  
- ✅ Automatically inputs `Y` to confirm upgrades  
- ⏱ Built-in delays for reliable cross-device execution

## ⚙️ Requirements  
- A Windows 10 or 11 system with [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/) installed  
- Flipper Zero with BadUSB enabled  
- This script saved to `badusb/Winget Upgrade All Apps.txt` on Flipper Zero’s SD card

## 📦 Installation  
1. Download `Winget Upgrade All Apps.txt` from this repository  
2. Copy it to your Flipper Zero's `badusb` directory  
3. Safely eject your Flipper Zero device

## 🚀 Usage  
1. Connect Flipper Zero to the target Windows system via USB  
2. Navigate to: `BadUSB → Winget Upgrade All Apps.txt`  
3. Run the script. It will:  
   - Open Run (`Win + R`)  
   - Launch `cmd` and execute: `winget upgrade --all`  
   - Wait for the prompt and input `Y`  
4. Script finishes after confirming all updates

## ⚠️ Notes  
- 🛂 Admin rights may be required for some application upgrades  
- ⏲ Modify `DELAY` values (e.g. `DELAY 1000`) to match target system performance  
- 🔒 Use responsibly—BadUSB scripts can modify system behavior  
- 🧪 Always test on a safe, authorized system prior to deployment

## 🤝 Contributing  
Pull requests and issue reports are welcome! Contributions that improve reliability, modularity, or safety are especially appreciated.

## 👤 Author  
**SoggyCow** — [GitHub Profile](https://github.com/SoggyCow)

## 📄 License  
Distributed under the [MIT License](./LICENSE)

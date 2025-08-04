# **FlipperZero BadUSB Scripts**

**Crafted by [SoggyCow](https://github.com/SoggyCow)**

Welcome to a growing collection of **BadUSB payloads** engineered for [Flipper Zero](https://flipperzero.one/). This repository showcases practical, tactical, and occasionally mischievous scripts written to leverage Flipper’s built-in USB emulation capabilities using **Ducky Script**.

## **🧠 Purpose**

Created as a public archive to share my work and contribute useful payloads to the Flipper Zero community. These scripts range from quick demos to more involved utilities designed for adversarial testing, creative automation, and software installation.

## **📁 Contents**

Each script is stored in its own folder with clear naming. You’ll find:  
- **🔐 Brute-force & lock-screen bypass payloads**  
- **⚙️ System tweaks, prank scripts, and automation examples**  
- **📦 Software installation scripts** for various applications via Chocolatey  
- **📋 Helpful documentation** and usage notes per payload

## **🧩 Available Scripts**

Below is a list of the current BadUSB scripts in this repository, each designed to automate specific tasks on a Windows system using Flipper Zero’s BadUSB feature:  
- **Install 7zip** – File archiver  
- **Install AdobeReader** – PDF reader  
- **Install AnyDesk** – Remote desktop software  
- **Install Bitwarden** – Secure password manager (via Chocolatey)  
- **Install BleachBit** – System cleaner and privacy tool  
- **Install Blender** – 3D modeling and animation software  
- **Install Cheat Engine** – Game memory scanner/debugger  
- **Install CrystalDiskInfo** – Disk health monitoring tool  
- **Install Discord** – Gaming/community communication  
- **Install Docker Desktop** – Containerization platform  
- **Install Dropbox** – Cloud storage client  
- **Install EaseUS Partition Master Free** – Partition manager *(availability unconfirmed)*  
- **Install Epic Games Launcher** – Gaming platform  
- **Install ExifTool** – Metadata editing tool  
- **Install FileZilla** – FTP client  
- **Install Git** – Version control system  
- **Install Google Drive** – Cloud storage client  
- **Install H2testw** – Storage device testing tool  
- **Install HxD** – Lightweight hex editor  
- **Install IDA Free** – Reverse-engineering disassembler  
- **Install Inno Setup** – Installer creation tool  
- **Install Java Runtime** – Java runtime environment  
- **Install Macrium Reflect Free** – Disk imaging and backup  
- **Install Microsoft Visual C++ Redistributable 2015** – Runtime library for Visual Studio 2015  
- **Install Microsoft Visual C++ Redistributable 140** – Runtime library for Visual Studio 2017/2019/2022  
- **Install NirLauncher** – Utility toolset  
- **Install Node.js** – JavaScript runtime  
- **Install Notepad++** – Text editor  
- **Install Paint.NET** – Image editing software  
- **Install Parsec** – Remote desktop for gaming  
- **Install Proton Drive** – Secure cloud storage client *(availability unconfirmed)*  
- **Install Proton Pass** – Proton’s password manager *(availability unconfirmed)*  
- **Install ProtonVPN** – VPN client  
- **Install PuTTY** – SSH and telnet client  
- **Install Python** – Programming language  
- **Install Quick CPU** – CPU optimizer *(availability unconfirmed)*  
- **Install Recuva** – Data recovery tool  
- **Install Rename My TV Series 2** – Episode renamer *(availability unconfirmed)*  
- **Install ResourceHacker** – EXE resource editor  
- **Install Rufus** – Bootable USB drive creator  
- **Install Steam** – Gaming platform  
- **Install Tailscale** – VPN for secure networking  
- **Install TeamViewer** – Remote desktop software  
- **Install TestDisk** – Data recovery tool  
- **Install Thunderbird** – Open-source email client  
- **Install VLC** – Media player  
- **Install Visual Studio 2022 Community** – IDE for development  
- **Install WinGet** – Microsoft CLI package manager *(includes terminal closure)*  
- **Install Wireshark** – Network protocol analyzer  
- **Install Zoom** – Video conferencing tool  
- **Install iPerf3** – Network bandwidth tester  
- **Install mIRC** – IRC client  
- **Install All Apps** – Bulk install: 7zip, adobereader, anydesk, etc *(some packages may be unavailable)*  

## **💡 How to Use**

1. **Clone or Download the Repo**: Download the repository or clone it using `git clone https://github.com/SoggyCow/flipperzero-badusb-scripts.git`.  
2. **Load Scripts onto Flipper Zero**:  
   - Connect your Flipper Zero to a computer via USB or Bluetooth.  
   - Use the qFlipper app or Flipper Mobile app to transfer the desired script(s) to the `SD Card/badusb/` folder.  
3. **Run the Script**:  
   - On Flipper Zero, navigate to **Main Menu > Bad USB**.  
   - Select the script (e.g., `install_bitwarden.txt`) and ensure USB mode is active (USB logo displayed).  
   - Connect Flipper Zero to the target Windows machine via USB.  
   - Press the **Run** button to execute the script.  
4. **Verify Execution**: Ensure **Chocolatey** is pre-installed on the target system, an internet connection is available, and administrative privileges are granted (most scripts trigger a UAC prompt).

## **📢 Important Notes**

- **Chocolatey Dependency**: All scripts require **Chocolatey** to be pre-installed on the target system. Run the [Chocolatey installation script](https://github.com/SoggyCow/choco-install-script) first.  
- **Package Availability**: Some packages (e.g., `protonpass`, `protondrive`, `quickcpu`, `renamemytvseries2`, `easeus-partition-master`) may not be available in the [Chocolatey Community Repository](https://community.chocolatey.org/packages) as of August 2025. Verify package existence before running these scripts or consider alternative installation methods.  
- **Administrative Privileges**: Most scripts open an elevated CMD, which may trigger a UAC prompt if enabled.  
- **Timing Delays**: Scripts use delays (e.g., `DELAY 1000`, `DELAY 500`) for reliable execution. Adjust delays for slower systems if execution fails.  
- **Testing**: Test scripts in a controlled environment (e.g., a virtual machine) to avoid unintended consequences.  
- **Responsible Use**: Some tools (e.g., `cheatengine`, `nirlauncher`, `ida-free`) may be flagged by antivirus software or have sensitive uses. Use them responsibly and only for legitimate purposes, such as educational or security research activities.

## **📬 Disclaimer**

These scripts are for **educational and research purposes only**. Always have permission before deploying any payload on a system. **SoggyCow** is not responsible for misuse or any resulting issues.

## **📬 Contributions**

Ideas, forks, and pull requests are welcome. If you have a script or improvement, send it in—let’s make this toolbox sharp.

---

Enjoy the payloads. Hack responsibly.  
— **SoggyCow**

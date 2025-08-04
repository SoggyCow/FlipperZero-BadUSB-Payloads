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

### **Available Scripts**

Below is a list of the current BadUSB scripts in this repository, each designed to automate specific tasks on a Windows system using Flipper Zero’s BadUSB feature:

- **[Install Bitwarden](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_bitwarden)**: Installs Bitwarden, a secure password manager, via Chocolatey.
- **[Install Proton Pass](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_protonpass)**: Installs Proton Pass, a password manager by Proton (package availability unconfirmed).
- **[Install Proton Drive](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_protondrive)**: Installs Proton Drive, a secure cloud storage client (package availability unconfirmed).
- **[Install Thunderbird](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_thunderbird)**: Installs Thunderbird, an open-source email client, via Chocolatey.
- **[Install Epic Games Launcher](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_epicgameslauncher)**: Installs the Epic Games Launcher for gaming and store access.
- **[Install HxD](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_hxd)**: Installs HxD, a lightweight hex editor, via Chocolatey.
- **[Install ExifTool](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_exiftool)**: Installs ExifTool, a metadata editing tool, via Chocolatey.
- **[Install ResourceHacker](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_resourcehacker)**: Installs ResourceHacker, a utility for editing Windows executable resources.
- **[Install Cheat Engine](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_cheatengine)**: Installs Cheat Engine, a memory scanner and debugger for games.
- **[Install Inno Setup](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_innosetup)**: Installs Inno Setup, an installer creation tool, via Chocolatey.
- **[Install Quick CPU](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_quickcpu)**: Installs Quick CPU, a CPU performance optimizer (package availability unconfirmed).
- **[Install Rufus](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_rufus)**: Installs Rufus, a tool for creating bootable USB drives.
- **[Install IDA Free](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_ida-free)**: Installs IDA Free, a disassembler for reverse engineering.
- **[Install Discord](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_discord)**: Installs Discord, a communication platform for gaming and communities.
- **[Install Rename My TV Series 2](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_renamemytvseries2)**: Installs Rename My TV Series 2, a TV episode renaming tool (package availability unconfirmed).
- **[Install EaseUS Partition Master Free](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_partitionmasterfree)**: Installs EaseUS Partition Master Free, a disk partition manager (package availability unconfirmed).
- **[Install Macrium Reflect Free](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_reflect-free)**: Installs Macrium Reflect Free, a disk imaging and backup tool.
- **[Install iPerf3](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_iperf3)**: Installs iPerf3, a network bandwidth testing tool.
- **[Install NirLauncher](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_nirlauncher)**: Installs NirLauncher, a collection of system utilities.
- **[Install BleachBit](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_bleachbit)**: Installs BleachBit, a system cleaning and privacy tool.
- **[Install Microsoft Visual C++ Redistributable 2015](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_vcredist2015)**: Installs the Visual C++ Redistributable for Visual Studio 2015 Update 3.
- **[Install WinGet](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_winget)**: Installs WinGet, Microsoft’s command-line package manager, and closes the terminal.
- **[Install All Apps](https://github.com/SoggyCow/flipperzero-badusb-scripts/tree/main/install_all_apps)**: Updates Chocolatey and installs a large set of applications, including 7zip, adobereader, anydesk, and more (some packages’ availability unconfirmed).

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

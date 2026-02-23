# TeamSpeak 3 Server Installation Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the installation of the [TeamSpeak 3 Server](https://www.teamspeak.com/), the official server software for hosting TeamSpeak voice communication servers.  
The TeamSpeak server allows you to run your own private or public voice server with channels, user permissions, server groups, virtual servers, file transfer, custom icons, banners, and persistent data storage — commonly used by gaming communities, clans, organizations, and teams.

Using Flipper Zero’s **BadUSB** feature with DuckyScript, the script opens an elevated Command Prompt and silently installs the TeamSpeak 3 Server via [Chocolatey](https://chocolatey.org/).

> **Note:** Chocolatey must be pre-installed on the target system. If it is not, run a Chocolatey installation payload first.

## Usage Instructions

### 1. Save the Script
- Filename: `install_teamspeak3-server.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_teamspeak3-server.txt`
- Ensure USB mode is active
- Connect to the target Windows machine and press **Run**

The script will:
- Open the Run dialog (Win + R)
- Launch an elevated Command Prompt (cmd with CTRL + SHIFT + ENTER)
- Execute: choco install teamspeak-server -y && exit

## Installation Verification

TeamSpeak 3 Server installs silently if:
- Chocolatey is already installed
- Administrative privileges are granted (UAC prompt accepted)
- An internet connection is available

After installation:
- Check the installation directory (typically `C:\Program Files\TeamSpeak 3 Server`)
- Look for the service “TeamSpeak 3 Server” in services.msc
- Or run the server manually from the folder to confirm it starts
- Default admin token is displayed in the logs on first start (check the log files in the server directory)

## Requirements

- **OS**: Windows 10 / 11 (Server editions also supported)
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for Chocolatey package download
- **Admin Privileges**: Required for elevated Command Prompt and service installation

## Technical Notes

- **Chocolatey Dependency**: The script assumes Chocolatey is already present
- **Elevation**: Opens an elevated cmd.exe (may show UAC prompt)
- **Silent Install**: Uses -y to suppress all prompts
- **Shell**: Uses Command Prompt (cmd) for broad compatibility
- **Service**: The package usually installs TeamSpeak as a Windows service (auto-start by default)
- **First Run**: On first launch, a privilege key (admin token) is generated — check logs
- **Delays**: Standard timing (DELAY 1000, 500, 1500). Increase if the target system is slow
- **Testing Recommendation**: Always test in a virtual machine or isolated environment first
- **Security**: Voice servers can expose ports and require careful configuration. Use only in authorized environments

## Disclaimer

This script is provided for educational and research purposes only.  
Use it exclusively on systems you own or have explicit written permission to access.  
The author is not responsible for any misuse, security incidents, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
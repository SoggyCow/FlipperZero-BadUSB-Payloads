# iPerf3 Installation Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the installation of [iPerf3](https://iperf.fr/), a widely used open-source tool for measuring TCP, UDP, and SCTP bandwidth performance on IP networks. iPerf3 allows users to test network throughput, latency, jitter, and packet loss between two endpoints (client/server mode), making it essential for network diagnostics, benchmarking, and troubleshooting.

The script uses Flipper Zero’s **BadUSB** feature with DuckyScript to open an elevated Command Prompt and silently install iPerf3 via [Chocolatey](https://chocolatey.org/).

> Note: Chocolatey must be pre-installed. Run a Chocolatey installation script first if needed.

## Usage Instructions

### 1. Save the Script
- Filename: `install_iperf3.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_iperf3.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install iperf3 -y && exit`.

## Installation Verification

iPerf3 installs silently if:
- Chocolatey is installed.
- Administrative privileges are granted.
- An internet connection is available.

After installation, verify by running `iperf3 --version` in a new Command Prompt.

## Requirements

- **OS**: Windows 10/11
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Needed for elevated Command Prompt

## Technical Notes

- **Chocolatey Dependency**: Requires Chocolatey to be pre-installed.
- **Elevation**: Uses elevated Command Prompt; may trigger a UAC prompt.
- **Silent Install**: The `-y` flag suppresses confirmation prompts.
- **Shell**: Uses Command Prompt for maximum compatibility.
- **Delays**: Includes standard delays (`DELAY 1000`, `DELAY 500`, `DELAY 1500`). Increase values for slower systems if needed.
- **Testing**: Always test in a virtual machine or isolated environment first.
- **Security**: Network testing tools may be flagged by security software. Use only in authorized environments.

## Disclaimer

This script is provided for educational and research purposes only. Use exclusively on systems you own or have explicit written permission to access. The author is not responsible for any misuse, security incidents, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
# Docker Desktop Installation Script for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This script automates the installation of **Docker Desktop** — the official container runtime and development platform — via [Chocolatey](https://chocolatey.org/) on Windows. Using Flipper Zero’s **BadUSB** feature with DuckyScript, it opens an elevated Command Prompt and silently installs Docker Desktop.

> **Important:** Chocolatey must be pre-installed. Run `install_chocolatey.txt` first if needed.

## Usage Instructions

### 1. Save the Script
- Filename: `install_docker.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_docker.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install docker-desktop -y`.

## Installation Verification

Docker Desktop installs silently if:
- Chocolatey is installed.
- Administrative privileges are granted.
- An internet connection is available.

Verify installation via: [Chocolatey Package Page](https://community.chocolatey.org/packages/docker-desktop). Installs the latest stable version (as of October 2025).

## Requirements

- **OS**:  
  Windows 10/11 Pro, Enterprise, or Education (64-bit)  
  Windows Server 2019/2022  
- **Virtualization**: WSL 2 (recommended) or Hyper-V enabled
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Required
- **Hardware**: Minimum 4 GB RAM (8+ GB recommended)

## Technical Notes

- **Chocolatey Dependency**: Script will fail without Chocolatey.
- **Elevation**: Uses elevated Command Prompt; may trigger UAC prompt.
- **Silent Install**: The `-y` flag suppresses all prompts.
- **Shell**: Uses Command Prompt for maximum compatibility.
- **Delays**: Includes `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Adjust for slower systems (e.g., `DELAY 700+`).
- **Post-Install**: Docker Desktop may require a reboot and manual WSL 2/Hyper-V setup on first launch.
- **Testing**: Strongly recommended in a virtual machine with a compatible Windows edition.

## Disclaimer

This script is for **educational and authorized use only**.  
Use **only** on systems you own or have explicit permission to modify.  
The author, SoggyCow, is not liable for system instability, data loss, or misuse.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
# AnyDesk Installation Script for Linux (Flipper Zero BadUSB)

Author: [SoggyCow](https://github.com/SoggyCow)  
License: MIT

## Overview

This DuckyScript payload automates the installation of **AnyDesk** on **Debian/Ubuntu-based Linux distributions** (Ubuntu, Linux Mint, Pop!_OS, Debian, etc.) using the official AnyDesk APT repository.

It adds the official GPG key and repository, updates the package list, and installs the `anydesk` package — ensuring you get the latest stable version with automatic updates.

The payload uses Flipper Zero’s **BadUSB** feature to simulate keyboard input, open a terminal (Ctrl+Alt+T), display brief instructions, and execute the required commands with `sudo`.

> Important: The user **must manually enter their sudo password** when prompted (typically 2–3 times during key import, repo addition, and installation) — this is a standard Linux security feature and cannot be automated.

## Usage Instructions

### 1. Save the Script
- Filename: `install-anydesk-linux.txt` (or similar)
- Format: UTF-8 plain text with **LF** line endings (not CRLF)

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install-anydesk-linux.txt`.
- Ensure USB mode is active.
- Connect to the target Linux machine and press **Run**.

The script will:
- Open the default terminal (Ctrl+Alt+T on GNOME, Cinnamon, many XFCE/Pop!_OS setups).
- Print short instructions.
- Run: `wget ... | gpg ... | sudo tee ... && echo ... | sudo tee ... && sudo apt update -y && sudo apt install anydesk -y`
- Wait ~30 seconds (covers multiple sudo prompts + key/repo setup + package download/install).
- Show completion message and exit the terminal.

## Installation Verification

After running:
- Open any terminal or your applications menu.
- Launch with: `anydesk`
- Or search for **"AnyDesk"** in your menu.
- Check version: `anydesk --version`

The package installs the latest stable release from the official AnyDesk repository (e.g., 7.1.x series as of early 2026).  
Verify repo addition: `cat /etc/apt/sources.list.d/anydesk-stable.list`

## Requirements

- **OS**: Ubuntu, Debian, Linux Mint, Pop!_OS or other Debian-based distro with `apt`
- **Desktop Environment**: Must support **Ctrl+Alt+T** to open terminal (GNOME, Cinnamon, most XFCE setups)
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for downloading GPG key, repo metadata, and AnyDesk package
- **Sudo Privileges**: User must have sudo access and be prepared to enter password multiple times
- **Terminal**: Default terminal emulator must respond to Ctrl+Alt+T

## Technical Notes

- **Terminal Shortcut**: Uses `GUI t` (Ctrl+Alt+T) — works on most popular desktop environments.
- **Sudo Prompts**: Multiple `sudo` calls (key import, repo write, apt update/install) — user types password as needed.
- **Official Repository**: Uses `deb.anydesk.com` with signed-by keyring for secure, up-to-date installs.
- **Delays**: `DELAY 30000` accounts for authentication, network operations, and installation time. Increase on slower systems/connections.
- **Launch Command**: `anydesk` (creates desktop/menu integration on most environments)
- **Testing**: Always test first in a virtual machine (e.g., VirtualBox/VMware with Ubuntu guest).

## Disclaimer

This script is for educational and personal use only. Use exclusively on systems you own or have explicit permission to access. The author, SoggyCow, is not responsible for any misuse, data loss, or system issues.

AnyDesk installation adds a third-party repository — review the source if security is a concern.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
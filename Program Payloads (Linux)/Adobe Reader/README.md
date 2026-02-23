# Adobe Acrobat Reader Installation Script for Linux (Flipper Zero BadUSB)

Author: [SoggyCow](https://github.com/SoggyCow)  
License: MIT

## Overview

This DuckyScript payload automates the installation of **Adobe Acrobat Reader DC** on Linux using the community-maintained `acrordrdc` snap package.  

The snap provides a Wine-wrapped version of Adobe Acrobat Reader DC (the closest equivalent to the Windows Adobe Reader experience on modern Linux, as Adobe discontinued native Linux support years ago).

It uses Flipper Zero’s **BadUSB** feature to simulate keyboard input, open a terminal (Ctrl+Alt+T), display brief instructions, and run the necessary `apt` and `snap` commands with `sudo`.

> Important: The user **must manually enter their sudo password** when prompted — this is a standard Linux security feature and cannot be automated.

## Usage Instructions

### 1. Save the Script
- Filename: `install-adobereader-linux.txt` (or similar)
- Format: UTF-8 plain text with **LF** line endings (not CRLF)

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install-adobereader-linux.txt`.
- Ensure USB mode is active.
- Connect to the target Linux machine and press **Run**.

The script will:
- Open the default terminal (Ctrl+Alt+T on GNOME, Cinnamon, many XFCE/Pop!_OS setups).
- Print short instructions.
- Run: `sudo apt update -y && sudo apt install snapd -y && sudo snap install acrordrdc`
- Wait ~25 seconds (covers password entry + snapd setup if needed + snap download/install).
- Show completion message and exit the terminal.

## Installation Verification

After running:
- Open any terminal or your applications menu.
- Launch with: `acrordrdc`
- Or search for **"Acrobat Reader"** or **"Adobe Acrobat"** in your menu.

The snap pulls the latest available version from snapcraft.io (Wine-based DC build).  
Verify snap status: `snap info acrordrdc`

## Requirements

- **OS**: Ubuntu, Debian, Linux Mint, Pop!_OS or other distro with `apt` and snap support
- **Desktop Environment**: Must support **Ctrl+Alt+T** to open terminal (GNOME, Cinnamon, most XFCE setups)
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for `apt update`, snapd install (if missing), and snap download
- **Sudo Privileges**: User must have sudo access and be prepared to enter password
- **Snap Support**: Most modern Ubuntu-based distros have snapd pre-installed; script adds it if needed

## Technical Notes

- **Terminal Shortcut**: Uses `GUI t` (Ctrl+Alt+T) — works on most popular desktop environments.
- **Sudo Prompt**: Cannot be bypassed — user must type password manually.
- **Snap Installation**:
  - Installs `snapd` if missing (harmless if already present)
  - Installs `acrordrdc` snap (sandboxed Wine wrapper for Adobe Acrobat Reader DC)
- **Delays**: `DELAY 25000` accounts for sudo authentication, potential snapd setup, and snap download time. Increase on slower connections.
- **Launch Command**: `acrordrdc` (creates desktop integration on most environments)
- **Testing**: Always test first in a virtual machine (e.g., VirtualBox/VMware with Ubuntu guest).

## Disclaimer

This script is for educational and personal use only. Use exclusively on systems you own or have explicit permission to access. The author, SoggyCow, is not responsible for any misuse, data loss, or system issues.

Adobe Acrobat Reader DC via snap is a community solution — it may not support every PDF feature perfectly due to Wine compatibility.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
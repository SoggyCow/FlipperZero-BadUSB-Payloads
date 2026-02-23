# 7-Zip Installation Script for Linux (Flipper Zero BadUSB)

Author: [SoggyCow](https://github.com/SoggyCow)  
License: MIT

## Overview

This DuckyScript payload automates the installation of **7-Zip** (via the `p7zip-full` and `p7zip-rar` packages) on **Debian/Ubuntu-based Linux distributions** (Ubuntu, Linux Mint, Pop!_OS, Debian, etc.).  

It uses Flipper Zero’s **BadUSB** feature to simulate keyboard input, open a terminal (Ctrl+Alt+T), display brief instructions, and run the appropriate `apt` commands with `sudo`.

> Important: The user **must manually enter their sudo password** when prompted — this is a standard Linux security feature and cannot be automated.

## Usage Instructions

### 1. Save the Script
- Filename: `install-7zip-linux.txt` (or similar)
- Format: UTF-8 plain text with **LF** line endings (not CRLF)

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install-7zip-linux.txt`.
- Ensure USB mode is active.
- Connect to the target Linux machine and press **Run**.

The script will:
- Open the default terminal (Ctrl+Alt+T on GNOME, Cinnamon, many XFCE/Pop!_OS setups).
- Print short instructions.
- Run: `sudo apt update -y && sudo apt install p7zip-full p7zip-rar -y`
- Wait ~18 seconds (covers password entry + package download/install).
- Show completion message and exit the terminal.

## Installation Verification

After running:
- Open any terminal.
- Type: `7z --help`
- You should see the 7-Zip help output.

The packages install the latest available version from the distribution repositories (typically 16.x–24.x series depending on your distro release).

## Requirements

- **OS**: Debian, Ubuntu, Linux Mint, Pop!_OS or other Debian-based distro with `apt`
- **Desktop Environment**: Must support **Ctrl+Alt+T** to open terminal (GNOME, Cinnamon, most XFCE setups)
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for `apt update` and package download
- **Sudo Privileges**: User must have sudo access and be prepared to enter password
- **Terminal**: Default terminal emulator must respond to Ctrl+Alt+T

## Technical Notes

- **Terminal Shortcut**: Uses `GUI t` (Ctrl+Alt+T) — works on most popular desktop environments.
- **Sudo Prompt**: Cannot be bypassed — user must type password manually.
- **Non-interactive Flags**: `-y` makes `apt` auto-confirm package installation.
- **Package Choice**:
  - `p7zip-full`: Core 7-Zip command-line tool
  - `p7zip-rar`: Adds RAR decompression support
- **Delays**: `DELAY 18000` gives time for password entry + package operations. Increase if your connection is slow.
- **Testing**: Always test first in a virtual machine (e.g., VirtualBox/VMware with Ubuntu guest).

## Disclaimer

This script is for educational and personal use only. Use exclusively on systems you own or have explicit permission to access. The author, SoggyCow, is not responsible for any misuse, data loss, or system issues.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
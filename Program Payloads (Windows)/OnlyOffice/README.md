# ONLYOFFICE Installer for Flipper Zero BadUSB

This repository contains a BadUSB script for the Flipper Zero that automates the installation of ONLYOFFICE Desktop Editors on a Windows system using Chocolatey.

**Author:** CayleRose  
**Platform:** Flipper Zero (BadUSB)  
**Target:** Windows 10/11 with Chocolatey installed

## Prerequisites

- Flipper Zero configured for BadUSB functionality.
- Windows 10 or Windows 11 target system.
- Chocolatey package manager pre-installed.
- Administrative access to run an elevated Command Prompt.
- Internet connection to download ONLYOFFICE.

## Usage

1. Copy `install_onlyoffice.txt` to your Flipper Zero’s BadUSB directory.
2. Connect the Flipper Zero to the target Windows machine.
3. Run the script from the Flipper Zero BadUSB interface.
4. Approve the UAC prompt if Windows displays one.
5. The script opens an elevated Command Prompt and runs `choco install onlyoffice -y`.

## Notes

- The Chocolatey package ID is `onlyoffice`.
- Chocolatey must already be installed on the target system.
- The installer downloads ONLYOFFICE from the package’s configured source.
- Installation time depends on the target system and network connection.
- Test in a virtual machine before using on a system you rely on.
- Use only on systems you own or have permission to modify.

## Disclaimer

This script is provided for educational and personal use. Always obtain proper authorization before running BadUSB scripts on any system. The author, CayleRose, is not responsible for misuse, damage, or other issues caused by this script.

## License

This project is licensed under the MIT License.
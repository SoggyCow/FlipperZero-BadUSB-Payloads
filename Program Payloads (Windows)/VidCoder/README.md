# VidCoder Installer for Flipper Zero BadUSB

## Overview
**VidCoder** is an open-source video transcoding and encoding application for Windows, allowing users to convert videos to various formats, add subtitles, and customize encoding settings with an intuitive interface.

This repository contains a BadUSB script for the Flipper Zero to automate the installation of VidCoder using Chocolatey on a Windows system. The script assumes Chocolatey is pre-installed and runs with administrative privileges to silently install VidCoder and close the terminal.

**Author**: [SoggyCow](https://github.com/SoggyCow)  
**Platform**: Flipper Zero (BadUSB)  
**Target**: Windows systems with Chocolatey installed

## Prerequisites
- **Flipper Zero**: Configured for BadUSB functionality.
- **Target System**: 
  - Windows OS.
  - Chocolatey package manager pre-installed.
  - Administrative access to run Command Prompt.
  - Internet connection for Chocolatey to download VidCoder.

## Usage
1. Clone or download this repository.
2. Copy the script to your Flipper Zero's BadUSB directory.
3. Connect the Flipper Zero to the target Windows machine.
4. Run the script via the Flipper Zero BadUSB interface.
5. The script will execute automatically, opening an admin Command Prompt, installing VidCoder, and closing the terminal.

## Notes
- Ensure the target system has Chocolatey installed. If not, you may need to modify the script to include Chocolatey installation.
- The script uses delays (`DELAY`) to account for system response times. Adjust these values if the target system is slower or faster.
- Use responsibly and only on systems you have permission to modify.

## Disclaimer
This script is provided for educational purposes only. The author, SoggyCow, is not responsible for any misuse or damage caused by this script. Always obtain proper authorization before running BadUSB scripts on any system.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
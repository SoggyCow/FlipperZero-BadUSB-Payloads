# FreeCAD Installer for Flipper Zero BadUSB

## Overview
**FreeCAD** is an open-source parametric 3D CAD modeler, designed for product design, mechanical engineering, and other 3D modeling tasks, with support for a wide range of file formats and customizable workflows.

This repository contains a BadUSB script for the Flipper Zero to automate the installation of FreeCAD using Chocolatey on a Windows system. The script assumes Chocolatey is pre-installed and runs with administrative privileges to silently install FreeCAD (pre-release version) and close the terminal.

**Author**: [SoggyCow](https://github.com/SoggyCow)  
**Platform**: Flipper Zero (BadUSB)  
**Target**: Windows systems with Chocolatey installed

## Prerequisites
- **Flipper Zero**: Configured for BadUSB functionality.
- **Target System**: 
  - Windows OS.
  - Chocolatey package manager pre-installed.
  - Administrative access to run Command Prompt.
  - Internet connection for Chocolatey to download FreeCAD.

## Usage
1. Clone or download this repository.
2. Copy the script to your Flipper Zero's BadUSB directory.
3. Connect the Flipper Zero to the target Windows machine.
4. Run the script via the Flipper Zero BadUSB interface.
5. The script will execute automatically, opening an admin Command Prompt, installing FreeCAD, and closing the terminal.

## Notes
- The script installs the pre-release version of FreeCAD (`--pre` flag). Remove the flag in the script if you prefer the stable version.
- Ensure the target system has Chocolatey installed. If not, you may need to modify the script to include Chocolatey installation.
- The script uses delays (`DELAY`) to account for system response times. Adjust these values if the target system is slower or faster.
- Use responsibly and only on systems you have permission to modify.

## Disclaimer
This script is provided for educational purposes only. The author, SoggyCow, is not responsible for any misuse or damage caused by this script. Always obtain proper authorization before running BadUSB scripts on距离 any system.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
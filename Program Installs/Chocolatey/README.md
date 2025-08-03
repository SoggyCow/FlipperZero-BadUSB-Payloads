# Chocolatey Installation Automation Script

**Author**: [SoggyCow](https://github.com/SoggyCow)

## Overview

This script automates the installation of [Chocolatey](https://chocolatey.org/), a popular package manager for Windows. It opens PowerShell with administrative privileges, bypasses the execution policy, downloads and runs the official Chocolatey installation script from `https://community.chocolatey.org/install.ps1`, and then closes PowerShell.

## Usage

This script is designed for use with a keystroke injection tool (e.g., USB Rubber Ducky). To use it:

1. **Save the Script**: Save the script to a file compatible with your keystroke injection tool (e.g., `install_choco.txt`).
2. **Configure Your Device**: Load the script onto your device per its instructions.
3. **Run the Script**: Plug the device into a Windows machine. The script will:
   - Launch PowerShell as an administrator.
   - Install Chocolatey by downloading and executing the official installation script.
   - Close PowerShell after completion.

### Prerequisites

- A Windows operating system.
- A keystroke injection tool or a method to simulate keyboard inputs.
- An active internet connection to download the Chocolatey installation script.

## Important Notes

- **Administrative Privileges**: The script requires admin rights to set the execution policy and install Chocolatey. Ensure the user account has sufficient permissions.
- **Security**: The script downloads and executes a script from `https://community.chocolatey.org/install.ps1`. Verify the source is trusted to avoid security risks.
- **Delays**: The script includes timing delays to ensure proper execution. Adjust them if needed for slower or faster systems.

## Disclaimer

This script is provided as-is for educational purposes. Use it responsibly and understand the risks of automating administrative tasks and downloading scripts from the internet. The author [](https://github.com/SoggyCow) is not responsible for any issues arising from its use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

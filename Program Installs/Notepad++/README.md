# Notepad++ Installation Script via Chocolatey

**Author**: [SoggyCow](https://github.com/SoggyCow)

## Overview

This script automates the installation of [Notepad++](https://notepad-plus-plus.org/), a popular text editor, using [Chocolatey](https://chocolatey.org/), a package manager for Windows. It assumes Chocolatey is already installed on the system and silently installs Notepad++ by running a PowerShell command in the background.

## Usage

This script is designed for use with a keystroke injection tool (e.g., USB Rubber Ducky). To use it:

1. **Save the Script**: Save the script to a file compatible with your keystroke injection tool (e.g., `install_notepadpp.txt`).
2. **Configure Your Device**: Load the script onto your device according to its instructions.
3. **Run the Script**: Plug the device into a Windows machine. The script will:
   - Open the Windows Run dialog.
   - Execute a PowerShell command in a hidden window to install Notepad++ silently using Chocolatey.
   - Complete the installation without user interaction.

### Prerequisites

- A Windows operating system.
- [Chocolatey](https://chocolatey.org/) must be pre-installed on the system.
- A keystroke injection tool or a method to simulate keyboard inputs.
- An active internet connection to download the Notepad++ package via Chocolatey.
- Administrative privileges to run the Chocolatey install command.

## Important Notes

- **Chocolatey Requirement**: The script assumes Chocolatey is already installed. If Chocolatey is not installed, the script will fail.
- **Administrative Privileges**: Installing software via Chocolatey typically requires admin rights. Ensure the user account has sufficient permissions.
- **Silent Installation**: The `-y` flag ensures the installation proceeds without prompting for user confirmation.
- **Hidden PowerShell Window**: The PowerShell command runs in a hidden window (`-W Hidden`) to minimize visibility during execution.
- **Delays**: The script includes timing delays to ensure proper execution. Adjust them if needed for slower or faster systems.

## Disclaimer

This script is provided as-is for educational purposes. Use it responsibly and ensure you understand the implications of automating software installations. The author [](https://github.com/SoggyCow) is not responsible for any issues arising from its use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

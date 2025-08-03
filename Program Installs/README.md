Chocolatey Installation Script
Author: SoggyCow
Overview
This script automates the installation of Chocolatey, a package manager for Windows. It is a prerequisite for any scripts that use Chocolatey to install software (e.g., choco install commands). The script opens PowerShell with administrative privileges, bypasses the execution policy, downloads and runs the official Chocolatey installation script, and closes PowerShell.
Usage
This script is designed for use with a keystroke injection tool (e.g., USB Rubber Ducky). To use it:

Save the Script: Save the script to a file compatible with your keystroke injection tool (e.g., install_choco.txt).
Configure Your Device: Load the script onto your device per its instructions.
Run the Script: Plug the device into a Windows machine. The script will:
Open PowerShell as an administrator.
Install Chocolatey by downloading and executing the official installation script from https://community.chocolatey.org/install.ps1.
Close PowerShell after completion.



Important: You must run this script before using any other scripts that rely on Chocolatey to install software.
Prerequisites

A Windows operating system.
A keystroke injection tool or a method to simulate keyboard inputs.
An active internet connection to download the Chocolatey installation script.
Administrative privileges to set the execution policy and install Chocolatey.

Important Notes

Prerequisite for Chocolatey Scripts: This script must be executed first to install Chocolatey before running any scripts that use choco commands.
Administrative Privileges: The script requires admin rights to set the execution policy and install Chocolatey. Ensure the user account has sufficient permissions.
Security: The script downloads and executes a script from https://community.chocolatey.org/install.ps1. Verify the source is trusted to avoid security risks.
Delays: The script includes timing delays to ensure proper execution. Adjust them if needed for slower or faster systems.

Disclaimer
This script is provided as-is for educational purposes. Use it responsibly and understand the risks of automating administrative tasks and downloading scripts from the internet. The author (SoggyCow) is not responsible for any issues arising from its use.
License
This project is licensed under the MIT License - see the LICENSE file for details.

# Flipper Zero BadUSB: Install Balabolka via Chocolatey

## Overview
This repository contains a Flipper Zero BadUSB script designed to install Balabolka, a free Text-to-Speech program, on a Windows machine using Chocolatey. The script automates the process of opening an elevated Command Prompt, installing Balabolka silently, and closing the terminal.

**Author**: SoggyCow  
**Script File**: `install_balabolka.txt`

## What It Does
The `install_balabolka.txt` script performs the following actions on a Windows machine:
1. Opens the Run dialog (`Win + R`).
2. Types `cmd` to open the Command Prompt.
3. Uses `Ctrl + Shift + Enter` to request an elevated (Administrator) Command Prompt.
4. Executes a Chocolatey command to install Balabolka silently using `choco install balabolka -y`.
5. Closes the Command Prompt window.

**Note**: This script assumes Chocolatey is pre-installed on the target machine. If Chocolatey is not installed, the script will fail. Use this script responsibly and only in environments where you have permission to install software.

## Requirements
- A Flipper Zero device with BadUSB functionality enabled.
- A Windows machine (tested on Windows 10/11) with Chocolatey pre-installed.
- The Flipper Zero must be connected as a USB device to the target machine.

## Usage
1. **Copy the Script**: Save the `install_balabolka.txt` script to your Flipper Zero's SD card in the `badusb` directory.
2. **Connect Flipper Zero**: Plug the Flipper Zero into the target Windows machine via USB.
3. **Run the Script**: On the Flipper Zero, navigate to the BadUSB menu, select `install_balabolka.txt`, and execute it.
4. **Verify**: The script will run automatically, and Balabolka will be installed on the target machine. You can verify this by checking for Balabolka in the Start menu or Program Files.

## Script Details
The script (`install_balabolka.txt`) contains the following commands:
- `DELAY 1000`: Waits 1 second to ensure the system is ready.
- `GUI r`: Opens the Run dialog.
- `DELAY 500`: Waits 0.5 seconds for the dialog to appear.
- `STRING cmd`: Types `cmd` to open Command Prompt.
- `CTRL-SHIFT ENTER`: Opens Command Prompt with admin privileges.
- `DELAY 1500`: Waits 1.5 seconds for the elevated prompt to load.
- `STRING choco install balabolka -y && exit`: Installs Balabolka silently via Chocolatey and exits the terminal.
- `ENTER`: Executes the command.

## Disclaimer
This script is provided for educational purposes only. Installing software without user consent may violate system policies or terms of service. Use this script only in environments where you have explicit permission to install software. The author is not responsible for any misuse or damage caused by this script.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details (if included in the repository).

## Contributing
Feel free to fork this repository, submit pull requests, or open issues for improvements or bug reports. Contributions are welcome!
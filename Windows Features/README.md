# Flipper Zero BadUSB: Disable Windows UAC

## Overview
This repository contains a Flipper Zero BadUSB script designed to disable Windows User Account Control (UAC) by modifying the Windows registry. The script automates the process of opening an elevated Command Prompt, setting the UAC prompt level to 0, and exiting the terminal.

**Author**: SoggyCow  
**Script File**: `disable_UAC.txt`

**Note**: Disabling UAC reduces security by allowing applications to run with administrative privileges without prompting the user. Use this script responsibly and only in controlled environments where you understand the implications.

## Requirements
- A Flipper Zero device with BadUSB functionality enabled.
- A Windows machine (tested on Windows 10/11).
- The Flipper Zero must be connected as a USB device to the target machine.

## License
This project is licensed under the MIT License.
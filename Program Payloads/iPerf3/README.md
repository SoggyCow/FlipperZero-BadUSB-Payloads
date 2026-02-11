```markdown
# iPerf3 Installation Script for Flipper Zero

Author: [SoggyCow](https://github.com/SoggyCow)  
License: MIT

## Overview

This script silently installs [iPerf3](https://iperf.fr/), the industry-standard network performance testing tool, via [Chocolatey](https://chocolatey.org/) on Windows systems. Using Flipper Zero’s **BadUSB** feature with DuckyScript, it opens an elevated Command Prompt and performs a quiet installation.

> Note: Chocolatey must be pre-installed. Run a separate Chocolatey installation script first if needed.

## Usage Instructions

### 1. Save the Script
- Filename: `install_iperf3.txt`
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Run the Script
- On Flipper: Navigate to `Main Menu > Bad USB > install_iperf3.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open the Run dialog (`Win + R`).
- Launch an elevated Command Prompt (`cmd` with `CTRL + SHIFT + ENTER`).
- Execute: `choco install iperf3 -y && exit`

## Installation Verification

iPerf3 installs silently if:
- Chocolatey is already installed
- Administrative privileges are granted (UAC accepted)
- An internet connection is available

After installation, verify by opening a terminal and running:

```bash
iperf3 --version
```

You can also check the [Chocolatey Package Page](https://community.chocolatey.org/packages/iperf3).

## Requirements

- **OS**: Windows 10 / 11
- **Chocolatey**: Must be pre-installed
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required for package download
- **Admin Privileges**: Needed for elevated Command Prompt

## Technical Notes

- **Chocolatey Dependency**: Requires Chocolatey to be pre-installed.
- **Elevation**: Opens an elevated Command Prompt; may trigger a UAC prompt.
- **Silent Install**: The `-y` flag suppresses all prompts.
- **Auto-close**: `&& exit` closes the terminal window when finished.
- **Delays**: Includes `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Increase delays (e.g. 800–2000 ms) on slower systems or if UAC takes longer.
- **Testing**: Always test in a virtual machine or sandbox environment first.

## Script Source

```text
REM Title: Install iPerf3 via Chocolatey (Admin CMD)
REM Author: SoggyCow
REM Description: Assumes Chocolatey is pre-installed; installs iPerf3 silently and closes terminal

DELAY 1000
GUI r
DELAY 500
STRING cmd
CTRL-SHIFT ENTER
DELAY 1500
STRING choco install iperf3 -y && exit
ENTER
```

## Disclaimer

This script is provided for **educational**, **security research**, and **authorized penetration testing** purposes only.  
Do not use on systems you do not own or have explicit written permission to access.  
The author, SoggyCow, is not responsible for any misuse or damage caused by this script.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
```

Feel free to copy this directly into your repository.

Let me know if you'd like to add sections like:
- common post-install test commands
- how to install a specific version
- error troubleshooting tips
- or a more "red team" flavored tone
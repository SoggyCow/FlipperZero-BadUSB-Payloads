**Author:** [SoggyCow](https://github.com/SoggyCow)

# Flipper Zero BadUSB – Install iPerf3 via Chocolatey

**Target:** Windows  
**Requirements:**  
- Chocolatey package manager already installed on the target system  
- Ability to elevate to administrator privileges

### Description

This BadUSB payload opens an elevated Command Prompt and silently installs iPerf3 using Chocolatey with automatic confirmation. The terminal window closes immediately after execution completes.

### Usage

1. Place the payload file in the `/badusb/` directory on the Flipper Zero SD card  
2. Select and execute the file from the BadUSB menu

### Behavior Notes

- A delay is included after triggering the run dialog to allow time for the UAC elevation prompt  
- If Chocolatey is not installed, the command will fail silently after the prompt is accepted  
- No error checking or fallback behavior is implemented

### Limitations

- Requires Chocolatey to be pre-installed  
- UAC elevation prompt requires manual confirmation unless UAC is disabled on the target  
- No mechanism is included to install Chocolatey itself

Repository maintained by @SoggyCow
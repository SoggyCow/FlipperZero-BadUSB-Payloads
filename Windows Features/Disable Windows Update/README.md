# Disable Windows 11 Automatic Updates (GoodUSB) for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This GoodUSB payload disables automatic Windows Update checks, downloads, and installations on Windows 11 by:

- Stopping and disabling the Windows Update service (`wuauserv`)
- Stopping and disabling related services (`bits`, `WaaSMedicSvc`)
- Setting registry keys to prevent auto-updates (`NoAutoUpdate = 1`)
- Setting an extreme pause date (2099) as a fallback

**Strong warning:**  
Disabling automatic updates significantly increases security risk. Systems become vulnerable to known exploits, malware, and missing security patches.  
Use **only** on isolated test/lab machines, air-gapped systems, or devices where you intentionally want to control updates manually.

Changes may be partially or fully reverted by:
- Windows Update Medic service
- Group Policy refresh
- Major feature updates
- Manual Windows repair operations

A reboot is strongly recommended after execution for full effect.

## Usage Instructions

### 1. Save the Script
- Filename: `disable_Windows-Update.txt` (or any name you prefer)
- Format: UTF-8 plain text

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 3. Run the Payload
- On Flipper: Navigate to `Main Menu > Bad USB > disable_Windows-Update.txt`
- Ensure USB mode is active
- Connect to the target Windows 11 machine and press **Run**

The payload will:
- Show an introduction and warning message in Notepad (with author credit)
- Count down from 5 and close Notepad without saving
- Launch elevated PowerShell
- Stop/disable Windows Update-related services
- Apply registry changes to block auto-updates
- Display completion message with reboot reminder
- Wait for user confirmation before closing

## Execution Notes

- **Duration**: 30–90 seconds
- **User interaction**:
  - Accept UAC prompt for PowerShell elevation
  - Press Enter in PowerShell to proceed after reading warnings
- **Visibility**: PowerShell window remains open with status messages (red/green text)
- **Revert methods** (manual):
  - Set services back to Manual/Automatic
  - Delete or set `NoAutoUpdate` to 0 in registry
  - Run `sfc /scannow` or Windows Update troubleshooter
  - Re-enable via Group Policy (gpedit.msc)
- **Detection**: May be flagged by EDR/antivirus as suspicious registry/service modification

## Requirements

- **OS**: Windows 11
- **Internet Access**: Not required (all actions local)
- **Flipper Zero**: BadUSB feature enabled
- **Admin Privileges**: Required (UAC prompt will appear)
- **PowerShell**: Available (default on Windows)

## Technical Notes

- Disables core services: `wuauserv`, `bits`, `WaaSMedicSvc`
- Registry path: `HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU`
- Fallback: Sets pause expiry to year 2099
- Includes friendly warning messages and author attribution throughout
- No cleanup of temporary changes — changes are persistent until manually reverted
- **Recommendation**: Test only in VMs or disposable systems — never on production or daily-driver devices

## Disclaimer

This payload is provided strictly for educational, research, red-team, and authorized testing purposes only.  
Disabling security updates on production systems is dangerous and not recommended.  
Do not use on systems you do not own or have explicit written permission to modify.  
The author is not responsible for any security incidents, data loss, system instability, exploitation, legal consequences, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
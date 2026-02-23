# Data Exfiltration via FTP (Desktop + Documents + Pictures + Videos + Downloads) for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This BadUSB payload opens a hidden PowerShell window and silently creates a ZIP archive containing the entire contents of the user's Desktop, Documents, Pictures, Videos, and Downloads folders.  
The archive is then uploaded to a remote FTP server and the temporary ZIP file is deleted. Explorer is forcefully restarted at the end to minimize visual clues.

**Critical warnings:**
- This is a highly malicious payload capable of large-scale data theft.
- Requires the target to have internet access and the FTP server to be reachable and writable.
- FTP transmits credentials and data in clear text (extremely insecure).
- No encryption or error handling for failed uploads / large folders.
- Can take a very long time (many minutes to hours) on systems with large user folders.
- Will likely be detected by modern EDR/antivirus when executed.

Use **only** in authorized penetration testing, red-team exercises, or controlled lab environments with explicit permission.

## Usage Instructions

### 1. Customize the Script
Before saving, replace the placeholder values:
- `$ftp="ftp://yourftp.com"` → your actual FTP server URL
- `$user="ftpuser"` → your FTP username
- `$pass="ftppass"` → your FTP password

### 2. Save the Script
- Filename: `exfil_ftp_userfolders.txt` (or any name you prefer)
- Format: UTF-8 plain text

### 3. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer the file to: `SD Card/badusb/`

### 4. Run the Payload
- On Flipper: Navigate to `Main Menu > Bad USB > exfil_ftp_userfolders.txt`
- Ensure USB mode is active
- Connect to the target Windows machine and press **Run**

The payload will:
- Open hidden PowerShell (bypassing execution policy)
- Create ZIPs of Desktop, Documents, Pictures, Videos, Downloads
- Merge them into one archive (`%TEMP%\p.zip`)
- Upload the archive to the specified FTP server
- Delete the local ZIP
- Force-restart explorer.exe
- Close the PowerShell window

## Execution Notes

- **Duration**: Heavily depends on folder size and upload speed (seconds to hours)
- **Visibility**: PowerShell window is hidden, but:
  - CPU/disk usage spikes
  - Network traffic to FTP server
  - Explorer restart may cause brief desktop flicker
- **Failure cases**:
  - No internet → upload silently fails
  - FTP credentials wrong → upload fails silently
  - Folders too large → ZIP creation may fail or timeout
  - Antivirus/Defender → script blocked or quarantined
- **Detection likelihood**: Very high on monitored/enterprise systems

## Requirements

- **OS**: Windows 10 / 11
- **Internet Access**: Required for FTP upload
- **FTP Server**: Must be online, accepting anonymous or credential-based uploads, and have write permission
- **Flipper Zero**: BadUSB feature enabled
- **PowerShell**: Available (default on Windows)

## Technical Notes

- Uses `System.IO.Compression.FileSystem` to create ZIPs
- Appends folders into a single archive (not nested cleanly)
- `-WindowStyle Hidden` + `-ExecutionPolicy Bypass` to reduce visibility
- No cleanup of partial ZIPs if upload fails
- Restarts explorer to hide any temporary anomalies
- **Strong recommendation**: Replace FTP with HTTPS upload (WebClient + Invoke-WebRequest) in real engagements — FTP is trivial to sniff

## Disclaimer

This script is provided strictly for educational, research, red-team, and authorized penetration testing purposes only.  
Executing this payload on systems you do not own or have explicit written permission to test is illegal in virtually every jurisdiction and may result in severe criminal charges.  
The author is not responsible for any misuse, legal consequences, data breaches, financial loss, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
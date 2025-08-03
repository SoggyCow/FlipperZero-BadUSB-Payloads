# 🧰 Chocolatey Installation Script

**Author:** SoggyCow  
**Purpose:** Automates the installation of [Chocolatey](https://chocolatey.org), a package manager for Windows systems.

---

## 📦 Overview

This script is a setup prerequisite for any automation utilizing Chocolatey (`choco install`). It opens PowerShell with elevated permissions, bypasses the execution policy, downloads the official install script from the Chocolatey community site, executes it, and gracefully closes PowerShell.

---

## ⚙️ Usage

This script is intended for use with keystroke injection tools (e.g., USB Rubber Ducky).

### Steps:

1. **Save the Script**  
   Save the payload as a compatible file (`install_choco.txt`) per your tool’s specifications.

2. **Load Your Device**  
   Transfer the script to your keystroke injection device and follow its setup instructions.

3. **Deploy the Script**  
   On plug-in:
   - PowerShell opens with administrator rights.
   - Downloads and executes: `https://community.chocolatey.org/install.ps1`
   - Closes PowerShell upon completion.

> ⚠️ **Important:** This must be executed before any `choco install` usage.

---

## 🧱 Prerequisites

- Windows OS  
- Keystroke injection tool or virtual keyboard input system  
- Internet access to fetch Chocolatey installer  
- Administrative rights to adjust execution policy and perform the install

---

## 📝 Important Notes

- 🔑 **Setup Dependency:** This is a foundational install for any future Chocolatey-based automation.
- 🧑‍💻 **Admin Privileges Required:** Ensure your user context allows elevated PowerShell.
- 🛡️ **Verify Source:** This script pulls from `https://community.chocolatey.org/install.ps1`. Confirm trustworthiness before executing.
- ⏱️ **Delays:** Script timing is calibrated for typical machines. Modify as needed for performance variance.

---

## ⚖️ Disclaimer

This script is supplied _as-is_ for educational purposes. Execution carries inherent risks—especially with admin privileges and automated downloads. The author, SoggyCow, assumes no liability for misuse or adverse outcomes.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for full terms.

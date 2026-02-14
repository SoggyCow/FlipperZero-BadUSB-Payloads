# Flipper Zero BadUSB Scripts

Author: [SoggyCow](https://github.com/SoggyCow)  
License: MIT

## Purpose

This repository is a collection of **BadUSB payloads** designed by SoggyCow for [Flipper Zero](https://flipperzero.one/), utilizing **DuckyScript** to leverage its USB emulation capabilities. The scripts range from practical utilities to creative automations and software installations, created to support the Flipper Zero community and showcase adversarial testing and automation techniques.

## Contents

Scripts are organized in individual folders with descriptive names, including:
- Brute-force and lock-screen bypass payloads
- System tweaks, pranks, and automation scripts
- Software installation scripts using Chocolatey
- Detailed documentation and usage instructions for each payload

## How to Use

1. **Clone or Download the Repo**:  
   Clone with `git clone https://github.com/SoggyCow/flipperzero-badusb-payloads.git` or download directly.

2. **Load Scripts onto Flipper Zero**:  
   - Connect Flipper Zero via USB or Bluetooth.
   - Use **qFlipper** or **Flipper Mobile App** to transfer scripts to `SD Card/badusb/`.

3. **Run the Script**:  
   - Navigate to `Main Menu > Bad USB` on Flipper Zero.
   - Select the desired script (e.g., `install_nmap.txt`).
   - Ensure USB mode is active.
   - Connect to the target Windows machine and press **Run**.

4. **Verify Execution**:  
   - Confirm **Chocolatey** is pre-installed.
   - Ensure internet access and administrative privileges (most scripts trigger a UAC prompt).

## Important Notes

- **Chocolatey Dependency**: Scripts require **Chocolatey** pre-installed. Use the [Chocolatey installation script](https://github.com/SoggyCow/FlipperZero-BadUSB-Payloads/blob/main/Program%20Payloads/Install%20Chocolatey.txt) if needed.
- **Package Availability**: Verify package availability in the [Chocolatey Community Repository](https://community.chocolatey.org/packages) before running, as some packages may not be available (e.g., `protonpass`, `protondrive`).
- **Admin Privileges**: Scripts typically open an elevated Command Prompt, which may trigger a UAC prompt.
- **Delays**: Scripts use delays (e.g., `DELAY 1000`, `DELAY 500`). Adjust for slower systems if needed.
- **Testing**: Test in a virtual machine before deploying to avoid unintended consequences.
- **Responsible Use**: Some tools (e.g., `nirlauncher`) may trigger antivirus flags or have sensitive applications. Use only for legitimate, authorized purposes.

## Disclaimer

These scripts are for **educational and research purposes only**. Use only on systems you own or have explicit permission to access. **SoggyCow** is not liable for misuse or any resulting issues.

## Contributions

Contributions, ideas, and pull requests are welcome. Submit your scripts or improvements to enhance this collection.

---

Enjoy the payloads and use them responsibly.  
— **SoggyCow**
# Enable Windows Hyper-V – Flipper Zero BadUSB Payload

**Title:** Enable Windows Hyper-V (Win+X method)  
**Author:** [SoggyCow](https://github.com/SoggyCow)  
**Description:** A DuckyScript payload designed for **Flipper Zero** (BadUSB mode) that opens an elevated PowerShell or Windows Terminal via the Win+X power user menu, then enables the Hyper-V optional Windows feature without forcing an immediate restart.  

Intended for **personal convenience** on your own machines — quick Hyper-V setup in labs or test environments without clicking through the GUI every time.

**Requirements:**
- Logged in as an Administrator
- UAC set to default (not "Always notify")
- Virtualization enabled in BIOS/UEFI (check Task Manager → Performance → CPU → Virtualization: Enabled)

**Target OS:** Windows 11 (compatible with 24H2 / 25H2 builds)

**What is Hyper-V?**  
Hyper-V is Microsoft's built-in hypervisor for creating and running virtual machines (VMs) directly on Windows. It allows you to run multiple operating systems (Linux, older Windows versions, etc.) in isolated environments on the same physical hardware — useful for development, testing, security research, or running legacy software.

## How the Payload Works (High-Level)
1. Presses **Win + X** to open the power user menu.
2. Sends the accelerator key (typically **A** for the admin entry, e.g., "Terminal (Admin)" or "Windows PowerShell (Admin)").
3. Triggers UAC elevation → manually click **Yes**.
4. Waits for the elevated console to focus.
5. Runs `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All -NoRestart`.
6. Exits the console.

The `-NoRestart` flag avoids an immediate reboot (reboot later when convenient).

## Usage on Flipper Zero
1. Create a new file in the BadUSB app on your Flipper Zero (or edit via qFlipper on PC).
2. Paste/adapt the DuckyScript logic matching the described sequence.
3. Save it (e.g., as `hyperv-enable.txt` or any name).
4. Go to BadUSB app → select your script → Run.
5. Plug Flipper into your Windows PC on a clean desktop (close other apps for best results).
6. Wait 2–4 seconds → UAC prompt → click **Yes**.
7. Hyper-V installs in ~30–90 seconds. Verify in "Turn Windows features on or off" or via PowerShell.

## Reliability Tips
- Allow sufficient delay (1.2–2 seconds) after selecting the admin menu item for the elevated window to open and focus.
- Test manually first: Win + X → press the underlined admin letter → accept UAC → run the enable command.
- If **A** doesn’t select the correct entry (customized menu), check the underlined letter and adjust (e.g., **T** in some setups).
- Increase delays if timing/focus issues occur (common on slower machines or with active notifications).

## Disclaimer
For **authorized personal or educational use only** on devices you own or have permission to modify. Enabling Hyper-V installs a hypervisor layer — use responsibly.

## License
MIT License – feel free to fork, modify, and share with credit to the original author.
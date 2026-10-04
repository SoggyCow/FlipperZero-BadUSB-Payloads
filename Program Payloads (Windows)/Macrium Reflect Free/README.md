# Macrium Reflect Free Installation Script (Chocolatey) for Flipper Zero

**Author:** CayleRose  
**License:** MIT

Installs [Macrium Reflect Free](https://www.macrium.com/reflectfree) — a disk imaging and backup tool — via [Chocolatey](https://chocolatey.org/).

This payload is written in DuckyScript for **Flipper Zero BadUSB**. It opens an elevated Command Prompt and silently installs Macrium Reflect Free.

> **Prerequisite:** Chocolatey must already be installed. Run `install_chocolatey.txt` first if needed.

---

## Deployment

### 1. Prepare the script
- Save the payload as `install_reflect.txt`
- Use UTF-8 encoding

### 2. Copy to Flipper Zero
- Connect the Flipper via USB or Bluetooth
- Use **qFlipper** or the Flipper Mobile app
- Place the file in:  
  `SD Card/badusb/`

### 3. Run on target
1. On the Flipper: **Main Menu → Bad USB → install_reflect.txt**
2. Confirm USB mode is active
3. Plug the Flipper into the target Windows machine
4. Press **Run**

**What the payload does:**
- Opens the Windows Run dialog
- Launches an elevated Command Prompt (UAC prompt may appear)
- Runs: `choco install reflect-free -y`

---

## Requirements

| Requirement                  | Notes                              |
|-----------------------------|------------------------------------|
| OS                          | Windows 10 / 11                    |
| Chocolatey                  | Must be pre-installed              |
| Administrator privileges    | Required                           |
| Internet connection         | Needed to download the package     |
| Flipper Zero (BadUSB)       | Functional and in USB mode         |

---

## Notes

- **UAC prompt** — May appear depending on system settings. The payload continues once approved.
- **Silent install** — The `-y` flag skips confirmation prompts.
- **Timing** — Default delays are `DELAY 1000`, `500`, and `1500`. Increase them on slower machines if needed.
- **Testing** — Always test in a virtual machine or controlled environment before real use.

Package reference: [reflect-free on Chocolatey](https://community.chocolatey.org/packages/reflect-free)

---

## Disclaimer

For educational and authorized use only.  
Run this payload **only** on systems you own or have explicit permission to modify.  
The author accepts no responsibility for misuse or any resulting damage.

---

## License

MIT License — see the `LICENSE` file for full terms.
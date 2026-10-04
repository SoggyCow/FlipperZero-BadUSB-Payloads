# ExifTool Installation Script (Chocolatey) for Flipper Zero

**Author:** SoggyCow  
**License:** MIT

Installs [ExifTool](https://exiftool.org/) — a powerful command-line tool for reading, writing, and editing metadata in images, documents, audio, and other files — via [Chocolatey](https://chocolatey.org/).

This payload is written in DuckyScript for **Flipper Zero BadUSB**. It opens an elevated Command Prompt and silently installs ExifTool.

> **Prerequisite:** Chocolatey must already be installed. Run `install_chocolatey.txt` first if needed.

---

## Deployment

### 1. Prepare the script
- Save the payload as `install_exiftool.txt`
- Use UTF-8 encoding

### 2. Copy to Flipper Zero
- Connect the Flipper via USB or Bluetooth
- Use **qFlipper** or the Flipper Mobile app
- Place the file in:  
  `SD Card/badusb/`

### 3. Run on target
1. On the Flipper: **Main Menu → Bad USB → install_exiftool.txt**
2. Confirm USB mode is active
3. Plug the Flipper into the target Windows machine
4. Press **Run**

**What the payload does:**
- Opens the Windows Run dialog
- Launches an elevated Command Prompt (UAC prompt may appear)
- Runs: `choco install exiftool -y`

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

Package reference: [ExifTool on Chocolatey](https://community.chocolatey.org/packages/exiftool)

---

## Disclaimer

For educational and authorized use only.  
Run this payload **only** on systems you own or have explicit permission to modify.  
The author accepts no responsibility for misuse or any resulting damage.

---

## License

MIT License — see the `LICENSE` file for full terms.
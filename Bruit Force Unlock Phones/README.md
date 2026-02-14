Here’s the GitHub README for your 4-digit PIN brute-force BadUSB payload generator script, in the same style as the previous ones:

# 4-Digit PIN Brute-Force Payload Generator for Flipper Zero

**Author:** [SoggyCow](https://github.com/SoggyCow)  
**License:** MIT

## Overview

This Python script generates a DuckyScript-compatible BadUSB payload that attempts every possible 4-digit PIN (0000–9999) by typing each number followed by ENTER, with a 1-second delay between attempts.

Intended use case:  
- Unlocking Windows PIN-protected screens  
- Testing weak/default PINs on locked devices  
- Educational demonstrations of brute-force attack feasibility against short PINs

The generated file can be placed directly in the Flipper Zero's `/badusb/` folder and executed from the BadUSB menu.

**Important:** This script produces a very long payload (~40,000 lines, ~800 KB). Flipper Zero has file size and execution time limits — running all 10,000 attempts can take over 2.5 hours.

## Usage Instructions

### 1. Run the Generator Script
- Save the Python code as `generate_pin_bf.py`
- Run it on your computer (requires Python 3)
- It will automatically create `full_4digit_bf.txt` in your Documents folder

### 2. Upload to Flipper
- Connect Flipper Zero via USB or Bluetooth
- Use **qFlipper** or **Flipper Mobile App**
- Transfer `full_4digit_bf.txt` to: `SD Card/badusb/`

### 3. Run the Payload
- On Flipper: Navigate to `Main Menu > Bad USB > full_4digit_bf.txt`
- Ensure USB mode is active
- Connect to the locked/target Windows machine and press **Run**

The payload will:
- Type each 4-digit combination (0000 → 9999)
- Press ENTER after each attempt
- Wait 1000 ms (1 second) between attempts

## Execution Notes

- **Duration**: ~2.8 hours for all 10,000 attempts (plus any lockout delays imposed by Windows)
- **Windows PIN lockout behavior**:
  - After ~4–10 wrong attempts → temporary lockout (30 seconds to several minutes)
  - After more failures → longer lockouts or "Something happened" error
  - The 1-second delay helps avoid immediate rate-limiting, but real-world success is low on modern systems
- **File size warning**: Some older Flipper firmware versions may struggle with files >500 KB — test first

## Requirements

- **Python**: 3.x (to run the generator script)
- **Flipper Zero**: BadUSB feature enabled
- **Target**: Windows device using 4-digit PIN lock screen
- **Admin Privileges**: Not required to run the payload

## Technical Notes

- **Output format**: Standard DuckyScript syntax (STRING + ENTER + DELAY)
- **Range**: 0000 to 9999 (zero-padded with .zfill(4))
- **No randomization**: Attempts are sequential (predictable but simple)
- **Customization ideas**:
  - Change DELAY to 500–2000 ms
  - Add WAIT_FOR_BUTTON_PRESS after every 50–100 attempts
  - Split into multiple files (e.g. 0000–2499, 2500–4999, etc.)
- **Testing Recommendation**: Test only on devices you own. Never use on unauthorized systems.

## Disclaimer

This script is provided for educational, research, and security testing purposes only.  
Brute-forcing PINs on devices you do not own or have explicit written permission to test is illegal in most jurisdictions.  
The author is not responsible for any misuse, legal consequences, security incidents, data loss, or damage resulting from the use of this script.

## License

Licensed under the MIT License. See the `LICENSE` file for full details.
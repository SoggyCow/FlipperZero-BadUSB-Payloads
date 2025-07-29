# 🔐 Flipper Zero: BadUSB 4-Digit PIN Brute Force Script

This folder contains a Python tool and its output payload designed to brute-force 4-digit PINs on Android devices using Flipper Zero's BadUSB feature. The generated script emulates keystrokes over USB, cycling through all combinations from `0000` to `9999`.

---

## 📁 Contents

- `Generate_BadUSB_Brute_Force.py`: Python script that auto-generates a full BadUSB brute force payload.
- `full_4digit_bf.txt`: The generated payload, formatted for Flipper Zero's BadUSB module. It contains all 0000 - 9999 possibilities.
- `top65_4digit_bf.txt`: I found this one online, made by defplex.wordpress.com, modified by rf-bandit.
- `README.md`: You're reading it.

---

## 🚀 Usage Flow

1. **Run the Python Generator**
   ```bash
   python Generate_BadUSB_Brute_Force.py
2. The generated file is located in your Documents folder.

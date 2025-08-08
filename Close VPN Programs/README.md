# **Program Termination Scripts for Flipper Zero BadUSB**

**Author**: [SoggyCow](https://github.com/SoggyCow)

## **Overview**

This folder contains a collection of **BadUSB scripts** designed for [Flipper Zero](https://flipperzero.one/) to terminate running programs on a Windows system, particularly on servers without monitors where remote access is disrupted. These scripts use **DuckyScript** to simulate keyboard inputs, opening a Command Prompt and executing `taskkill` commands to forcefully close specified processes. This is especially useful in scenarios where launching a VPN (e.g., Hide.me VPN) on a local server closes the remote connection, and connecting a monitor or restarting the server is impractical. Using BadUSB to terminate the problematic process is a faster solution.

## **Purpose**

These scripts are crafted to provide a quick and automated way to close programs that interfere with server connectivity, such as VPN clients, without requiring physical access to the server. They are ideal for IT administrators or users managing headless servers via remote connections over the internet.

## **Usage**

These scripts are intended for use with Flipper Zero's **BadUSB** functionality, which emulates a keyboard to execute commands. To use them:

1. **Save the Script**: Save the script to a `.txt` file (e.g., `close_hidemevpn.txt`) compatible with Flipper Zero.
2. **Upload to Flipper Zero**:
   - Connect your Flipper Zero to a computer via USB or Bluetooth.
   - Use the qFlipper app or Flipper Mobile app to transfer the script to the `SD Card/badusb/close_programs/` folder.
3. **Run the Script**:
   - On Flipper Zero, navigate to **Main Menu > Bad USB**.
   - Select the script (e.g., `close_hidemevpn.txt`) and ensure USB mode is active (USB logo displayed).
   - Connect Flipper Zero to the target Windows machine (e.g., the headless server) via USB.
   - Press the **Run** button to execute the script, which will:
     - Open the Windows Run dialog.
     - Launch a Command Prompt.
     - Execute `taskkill` commands to forcefully terminate the specified processes.
4. **Verify Termination**: Ensure the target program (e.g., Hide.me VPN) is closed, restoring remote connectivity if applicable.

## **Prerequisites**

- A Windows operating system (Windows 10/11 recommended for compatibility).
- Flipper Zero with **BadUSB** functionality enabled.
- Administrative privileges may be required for some `taskkill` commands, depending on the process.
- Physical USB access to the target machine (e.g., the headless server).

## **Important Notes**

- **Process Names**: Ensure the process names in the script (e.g., `hide.me.exe`, `hidemevpn.exe`) match the exact names used by the target program. Check Task Manager or the program’s documentation for accuracy.
- **Administrative Privileges**: Some processes may require elevated permissions to terminate. If the script fails, consider modifying it to open an elevated Command Prompt (e.g., using `CTRL-SHIFT ENTER` as in other scripts).
- **Timing Delays**: The scripts use delays (e.g., `DELAY 1000`, `DELAY 500`) for reliable execution. If the script fails, increase delays (e.g., `DELAY 500` to `DELAY 700`) for slower systems.
- **Testing**: Test scripts in a controlled environment (e.g., a local machine or virtual machine) before deploying on a production server to avoid unintended consequences.
- **Responsible Use**: Only terminate processes on systems you own or have explicit permission to manage. Improper use of `taskkill` could disrupt critical services.

## **Disclaimer**

These scripts are provided as-is for **educational and research purposes**. Use them responsibly and only on systems you own or have explicit permission to access. The author ([SoggyCow](https://github.com/SoggyCow)) is not responsible for any issues arising from their use, including unintended process termination or service disruptions.

## **Contributions**

Ideas, forks, and pull requests for additional program termination scripts are welcome. If you have a script to close other problematic processes, send it in to enhance this collection.

## **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
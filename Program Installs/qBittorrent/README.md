# **qBittorrent Installation Script via Chocolatey for Flipper Zero**

**Author**: [SoggyCow](https://github.com/SoggyCow)

## **Overview**

This script automates the installation of **[qBittorrent](https://www.qbittorrent.org/)**, a free and open-source BitTorrent client for downloading and sharing files, using **[Chocolatey](https://chocolatey.org/)**, a package manager for Windows. Designed for Flipper Zero's **BadUSB** feature, it uses DuckyScript to simulate keyboard inputs, opening an elevated Command Prompt (CMD), executing a Chocolatey command to silently install qBittorrent, and closing the terminal afterward.

**Important**: This script requires **[Chocolatey](https://chocolatey.org/)** to be pre-installed. You **must** run the [Chocolatey installation script](https://github.com/SoggyCow/choco-install-script) first.

## **Usage**

This script is intended for use with Flipper Zero's **BadUSB** functionality, which emulates a keyboard to execute commands. To use it:

1. **Save the Script**: Save the script to a `.txt` file (e.g., `install_qbittorrent.txt`) compatible with Flipper Zero.
2. **Upload to Flipper Zero**:
   - Connect your Flipper Zero to a computer via USB or Bluetooth.
   - Use the qFlipper app or Flipper Mobile app to transfer the script to the `SD Card/badusb/` folder.
3. **Run the Script**:
   - On Flipper Zero, navigate to **Main Menu > Bad USB**.
   - Select the script (`install_qbittorrent.txt`) and ensure USB mode is active (USB logo displayed).
   - Connect Flipper Zero to the target Windows machine via USB.
   - Press the **Run** button to execute the script, which will:
     - Open the Windows Run dialog.
     - Launch an elevated Command Prompt (may trigger a UAC prompt).
     - Execute a Chocolatey command to install **qBittorrent** silently and close the terminal.
4. **Verify Installation**: **qBittorrent** will install without user interaction, and the terminal will close automatically, provided **Chocolatey** is installed and an internet connection is available.

## **Prerequisites**

- A Windows operating system (Windows 10/11 recommended for **qBittorrent** compatibility).
- **[Chocolatey](https://chocolatey.org/)** pre-installed (run the Chocolatey installation script first).
- Flipper Zero with **BadUSB** functionality enabled.
- An active internet connection to download the **qBittorrent** package via **Chocolatey**.
- Administrative privileges to execute the **Chocolatey** install command.
- System requirements for **qBittorrent** (typically lightweight; check [qBittorrent requirements](https://www.qbittorrent.org/)).

## **Important Notes**

- **Chocolatey Dependency**: This script will fail if **Chocolatey** is not installed. Run the **Chocolatey installation script** first.
- **Administrative Privileges**: **Chocolatey** requires admin rights to install software. The script opens an elevated CMD, which may trigger a UAC prompt if enabled.
- **Silent Installation**: The `-y` flag ensures **qBittorrent** installs without user prompts, and the `&& exit` command closes the terminal after installation.
- **Command Prompt Usage**: This script uses CMD for compatibility with some systems. Ensure CMD supports Chocolatey commands on the target system.
- **Timing Delays**: The script uses delays (`DELAY 1000`, `DELAY 500`, `DELAY 1500`) for reliable execution. If the script fails, increase delays (e.g., `DELAY 500` to `DELAY 700`) for slower systems.
- **qBittorrent Version**: The `qbittorrent` package typically installs the latest stable version (e.g., 4.x as of August 2025). Check the [Chocolatey package page](https://community.chocolatey.org/packages/qbittorrent) for details.
- **Testing**: Test the script in a controlled environment (e.g., a virtual machine) to avoid unintended consequences.
- **Responsible Use**: **qBittorrent** is a tool for file sharing via the BitTorrent protocol. Use it responsibly and only for legitimate purposes, adhering to legal and ethical guidelines.

## **Disclaimer**

This script is provided as-is for **educational purposes**. Use it responsibly and only on systems you own or have explicit permission to access. The author ([SoggyCow](https://github.com/SoggyCow)) is not responsible for any issues arising from its use, including potential misuse in violation of software terms or legal regulations.

## **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

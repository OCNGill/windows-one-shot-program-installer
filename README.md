# Windows One-Shot Program Installer 🚀

**Make My Computer Great Again** - A user-friendly tool to search, select, and install Windows applications in one go.

---

## 🎯 Overview

The **Windows One-Shot Program Installer** is a Streamlit-based web application that simplifies the process of reinstalling or setting up Windows applications. Instead of manually searching for and installing programs one by one, this tool lets you:

1. **Search** for apps using Windows Package Manager (`winget`)
2. **Add** them to your installation queue with a single click
3. **Install** everything at once with minimal interaction

Perfect for setting up a new PC, helping friends/family, or recovering from a system reset.

---

## ✨ Features

- 🔍 **Smart Search**: Automatically handles typos (e.g., "7 zip" → "7zip")
- 🎨 **Modern UI**: Clean, intuitive web interface built with Streamlit
- 💾 **Disk Monitoring**: Real-time display of available storage space
- 📦 **Batch Installation**: Install multiple programs sequentially
- 🎉 **Visual Feedback**: Progress bars, success notifications, and celebration effects
- ⚡ **One-Click Launch**: Simple `.bat` file handles all dependencies

---

## 🚀 Quick Start

### Prerequisites
- **Windows 11** (or Windows 10 with `winget` installed)
- **Python 3.x** (automatically checked by launcher)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/OCNGill/windows-one-shot-program-installer.git
   cd windows-one-shot-program-installer
   ```

2. **Run the launcher**:
   Double-click `make_my_computer_great_again.bat`

   The launcher will:
   - Check for Python
   - Install Streamlit if needed
   - Launch the app in your browser

---

## 📖 How to Use

1. **Search**: Enter an app name (e.g., "Chrome", "Discord", "7zip")
2. **Add**: Click the **➕ Add** button next to your desired programs
3. **Review**: Check the sidebar to see your selections and disk space
4. **Install**: Click **🚀 INSTALL ALL** to begin batch installation

---

## 🛠️ Technical Details

### Architecture
- **Backend**: Python 3.x
- **Frontend**: Streamlit
- **Package Manager**: Windows Package Manager (`winget`)
- **Launcher**: Batch script (`.bat`)

### File Structure
```
windows-one-shot-program-installer/
├── app.py                          # Main Streamlit application
├── winget_wrapper.py               # Winget command interface
├── manager.py                      # Package list manager
├── make_my_computer_great_again.bat # Launcher script
├── Design.md                       # Architecture documentation
├── Requirements.md                 # Functional requirements
├── Project_Definition.md           # Project overview
└── README.md                       # This file
```

---

## 🎨 Screenshots

The app features:
- **Main Search Area**: Clean input field with smart search
- **Results Grid**: Structured table with "Add" buttons
- **Sidebar**: Disk usage, selected apps, and install button
- **Progress Tracking**: Real-time installation status

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is open source and available under the MIT License.

---

## 💖 Support / Donate

If you find this project helpful, you can support ongoing work — thank you!

<p align="center">
	<img src="qr-paypal.png" alt="PayPal QR code" width="180" style="margin:8px;">
	<img src="qr-venmo.png" alt="Venmo QR code" width="180" style="margin:8px;">
</p>


**Donate:**

- [![PayPal](https://img.shields.io/badge/PayPal-Donate-009cde?logo=paypal&logoColor=white)](https://paypal.me/gillsystems) https://paypal.me/gillsystems
- [![Venmo](https://img.shields.io/badge/Venmo-Donate-3d95ce?logo=venmo&logoColor=white)](https://venmo.com/Stephen-Gill-007) https://venmo.com/Stephen-Gill-007

---


<p align="center">
	<img src="Gillsystems_logo_with_donation_qrcodes.png" alt="Gillsystems logo with QR codes and icons" width="800">
</p>

<p align="center">
	<a href="https://paypal.me/gillsystems"><img src="paypal_icon.png" alt="PayPal" width="32" style="vertical-align:middle;"></a>
	<a href="https://venmo.com/Stephen-Gill-007"><img src="venmo_icon.png" alt="Venmo" width="32" style="vertical-align:middle;"></a>
</p>

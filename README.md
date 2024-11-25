# Autosend Message

A Python script that allows you to schedule messages to be automatically sent at a specified time. The script features a colorful command-line interface and uses PyAutoGUI for message automation.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📝 Description

This script enables users to:
- Set up automated message sending
- Schedule messages for a specific time
- Auto-type messages using PyAutoGUI
- Monitor waiting time with a visual countdown
- Features a stylish magenta-colored terminal interface
- While this project was made for discord messages, it'll work for anything!

## 🔧 Requirements

```
python 3.6+
pyautogui
```

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/JacobsProjects/Auto-message-sender.git
```

2. Install the required packages:
```bash
pip install pyautogui colorama
```

## 🚀 Usage

1. Run the script:
```bash
python autosend.py
```

2. Follow the prompts:
   - Enter the message you want to send
   - Specify the time in 24-hour format (HH:MM)
   - Switch to your target window/application
   - Wait for the scheduled time

3. The script will:
   - Display a countdown
   - Automatically type and send your message at the specified time
   - Close after successful delivery

## ⚠️ Important Notes

- Ensure your target window/application is active when the scheduled time arrives
- Keep the script window open until the message is sent
- The script uses PyAutoGUI, so don't move your mouse or type while the message is being sent
- Time format must be in 24-hour format (HH:MM)

## 👨‍💻 Author

**JacobsProjects**

* Discord: jc9808

## 🎨 Acknowledgments

- Uses colorama for terminal styling
- PyAutoGUI for automation
- ASCII art title banner

## 📜 Changelog

### Version 1.0.0
- Initial release
- Basic message scheduling functionality
- Magenta-colored interface
- ASCII art banner

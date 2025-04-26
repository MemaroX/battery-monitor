# 🔋 Battery Monitor with Telegram Notifications

Monitor your Android device's battery status and get Telegram notifications when fully charged.

## Features
- Real-time battery monitoring via Termux
- Telegram notifications at 100% charge
- Configurable check intervals
- Detailed logging system

## Installation
```bash
git clone https://github.com/MemaroX/battery-monitor.git
cd battery-monitor
pip install -r requirements.txt
```
## Configuration
1. Copy 'config.example.json' to 'config.json'
2. Add your Telegram bot token and chat ID
3. Run with 'python src/battery_monitor.py'

## Requirements
- Termux with Termux:API
- Python 3.8+



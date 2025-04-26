import json
import logging
import os
import time
from pathlib import Path
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('battery_monitor.log'),
        logging.StreamHandler()
    ]
)

class BatteryMonitor:
    def __init__(self):
        self.config = self.load_config()
        self.last_notification_time = 0

    def load_config(self):
        config_path = Path('src/config.json')
        if not config_path.exists():
            raise FileNotFoundError("config.json not found. Create from config.example.json")

        with open(config_path) as f:
            return json.load(f)

    def get_battery_status(self):
        try:
            output = os.popen('termux-battery-status').read()
            return json.loads(output)
        except Exception as e:
            logging.error(f"Battery status error: {e}")
            return None

    def send_notification(self, message):
        try:
            response = requests.post(
                f"https://api.telegram.org/bot{self.config['bot_token']}/sendMessage",
                data={
                    "chat_id": self.config['chat_id'],
                    "text": message
                },
                timeout=10
            )
            return response.status_code == 200
        except Exception as e:
            logging.error(f"Notification failed: {e}")
            return False

    def run(self):
        logging.info("Starting battery monitor...")
        while True:
            battery = self.get_battery_status()
            if battery:
                self.check_battery(battery)
            time.sleep(self.config.get('interval', 60))

    def check_battery(self, battery):
        current_time = time.time()
        if (battery['percentage'] == 100 and
            battery['plugged'] != "UNPLUGGED" and
            current_time - self.last_notification_time > 3600):

            if self.send_notification("🔋 Battery fully charged!"):
                self.last_notification_time = current_time
                logging.info("Notification sent")

if __name__ == "__main__":
    monitor = BatteryMonitor()
    monitor.run()


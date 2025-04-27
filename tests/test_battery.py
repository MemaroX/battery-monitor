from src.battery_monitor import BatteryMonitor
import pytest

def test_battery_initialization():
    try:
	monitor = BatteryMonitor()
	assert monitor.config is not None
    except FileNotFoundError:
	pytest.skip("config.json not found - create from config.example.json")

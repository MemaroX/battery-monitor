from src.battery_monitor import BatteryMonitor
import pytest

def test_battery_initialization():
    monitor = BatteryMonitor()
    assert monitor.config is not None

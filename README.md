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

## Feature Development

We use a feature flag system for controlled rollouts:

```bash
# Check available features
python -c "from feature.experimental import FeatureManager; print(FeatureManager().features)"
```
# Enable a feature (edit features/flags.json)

Current experimental features:
- 'low_battery_alert': Notify when battery < 20%
- 'multi_device' : Monitor multiple devices

Contributing New Features
1. Create an issue with the 'new-feature' label
2. Impement behind a feature flag
3. Submit PR ( Request-Pull) with:
    - Code implementation
    - Updated documentation
    - Tests

## Implementation Flow for New Features

1. **Label Creation** :
    ```bash
    gh label create "new-feature" --color "#0052CC" --description "Features in development"
    ```
2. **Development Process** :
    ```python
    # Check feature status anywhere in code
    if FeatureManager().is_enabled("your_feature"):
        # New behavio
    else:
        # Exisiting behavior
3. **Release Managment** :
    - Feature start disabled in 'flags.json'
    - Enable via PR when stable
    - Remove flage checks after full rollout


from dataclasses import dataclass
import json
from pathlib import Path

@dataclass
class Feature:
    name: str
    enabled: bool
    description: str
    owner: str = None  # Add this line to make owner optional

class FeatureManager:
    def __init__(self):
        self.features = self._load_features()
    
    def _load_features(self):
        with open(Path(__file__).parent / "flags.json") as f:
            data = json.load(f)
        return {
            name: Feature(
                name=name,
                enabled=attrs["enabled"],
                description=attrs["description"],
                owner=attrs.get("owner")  # Safely get optional owner
            )
            for name, attrs in data["new_features"].items()
        }
    
    def is_enabled(self, feature_name):
        return self.features.get(feature_name, Feature("", False, "")).enabled

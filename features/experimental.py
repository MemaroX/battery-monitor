from dataclasses import dataclass
import json
from pathlib import Path

@dataclass
class Feature:
    name: str
    enabled: bool
    description: str

class FeatureManager:
    def __init__(self):
        self.features = self._load_features()
    
    def _load_features(self):
        with open(Path(__file__).parent / "flags.json") as f:
            data = json.load(f)
        return {
            name: Feature(name, **attrs)
            for name, attrs in data["new_features"].items()
        }
    
    def is_enabled(self, feature_name):
        return self.features.get(feature_name, Feature("", False, "")).enabled

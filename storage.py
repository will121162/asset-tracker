import json
from pathlib import Path

stored_assets_and_strings = {
    "assets": {},
    "existing_strings": [],
    "blocked_strings": [],

}

data_file = Path(__file__).parent / "assets.json"

def load_data():
    if data_file.exists():
        print("Loading data...")
        with data_file.open() as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                save_data(stored_assets_and_strings)
                return stored_assets_and_strings
    else:
        save_data(stored_assets_and_strings)
        return stored_assets_and_strings

def save_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=2)
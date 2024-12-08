import json
import os
from datetime import datetime

DATA_FILE = "key_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def filter_data(start_date, end_date):
    data = load_data()
    filtered = {}
    for app, keys in data.items():
        for key, values in keys.items():
            timestamps = [
                ts for ts in values["timestamps"]
                if start_date <= datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') <= end_date
            ]
            if timestamps:
                filtered[key] = len(timestamps)
    return filtered

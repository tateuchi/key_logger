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
        for key, value in keys.items():
            if "timestamps" in value:
                timestamps = [
                    ts for ts in value["timestamps"]
                    if start_date <= datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') <= end_date
                ]
                if timestamps:
                    if key not in filtered:
                        filtered[key] = 0
                    filtered[key] += len(timestamps)

    return filtered

def get_date_range(data):
    timestamps = []
    for app, keys in data.items():
        for key, value in keys.items():
            if "timestamps" in value:
                timestamps.extend(value["timestamps"])
    
    if not timestamps:
        return None, None

    timestamps = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in timestamps]
    
    return min(timestamps), max(timestamps)

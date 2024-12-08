import json
from pynput import keyboard
from datetime import datetime
from utils.data_handler import load_data, save_data
from utils.app_detector import get_active_window

def on_press(key):
    data = load_data()
    active_app = get_active_window()
    try:
        key_str = key.char if key.char else str(key)
    except AttributeError:
        key_str = str(key)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if active_app not in data:
        data[active_app] = {}

    if key_str not in data[active_app]:
        data[active_app][key_str] = {"count": 0, "timestamps": []}

    data[active_app][key_str]["count"] += 1
    data[active_app][key_str]["timestamps"].append(timestamp)

    save_data(data)

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()

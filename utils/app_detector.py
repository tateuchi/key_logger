import psutil

def get_active_window():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name']:
            return process.info['name']
    return "Unknown"

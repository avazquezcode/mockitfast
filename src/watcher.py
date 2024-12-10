import os
import time


def watch_modification(file_path, interval, callback_on_modified=None):
    last_modified = os.path.getmtime(file_path)
    while True:
        current_modified = os.path.getmtime(file_path)
        if current_modified != last_modified:
            last_modified = current_modified
            callback_on_modified()

        # wait for next check
        time.sleep(interval)

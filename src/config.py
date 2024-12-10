import os


class Config:
    def __init__(self):
        self.host = os.environ.get("HOST")
        self.port = int(os.environ.get("PORT"))
        self.router_config_path = os.environ.get("ROUTER_CONFIG_PATH")
        self.watcher_interval_seconds = int(os.environ.get(
            "WATCHER_INTERVAL_SECONDS"))

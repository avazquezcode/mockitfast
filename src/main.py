import logging

from watcher import watch_modification
from server import Server
from config import Config

from dotenv import load_dotenv


if __name__ == "__main__":
    # Parse config and setup server
    try:
        load_dotenv()
        config = Config()
        server = Server(config)
    except Exception as e:
        logging.error(f"Error occurred on initial setup: {e}")
        exit(1)

    # Start server and start watching for changes on router file
    try:
        server.start()
        watch_modification(config.router_config_path,
                           config.watcher_interval_seconds,
                           server.restart)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        server.stop()
        exit(1)

import os
import signal
import uvicorn
import logging

from api.app import get_app
from config.config import Config

from multiprocessing import Process
from domain.model import Router
from pydantic_core import from_json


class Server:
    process = None

    def __init__(self, config: Config):
        self.config = config

    def start(self):
        self.process = Process(target=self.start_app_server)
        self.process.start()
        logging.info("Server is running")

    def restart(self):
        os.kill(self.process.pid, signal.SIGTERM)
        self.start()
        logging.info("Server is restarting")

    def stop(self):
        os.kill(self.process.pid, signal.SIGTERM)
        logging.info("Server is stopped")

    def load_router(self):
        router_config = open(self.config.router_config_path, 'r').read()
        return Router.model_validate(
            from_json(
                router_config,
                allow_partial=True
            )
        )

    def start_app_server(self):
        app = get_app(self.load_router(), self.config)
        uvicorn.run(
            app,
            host=self.config.host,
            port=self.config.port,
        )

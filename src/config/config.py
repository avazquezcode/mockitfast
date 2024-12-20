import os

ENV_TRUE_VALUES = ("true", "1")

# defaults
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 3000
DEFAULT_WATCHER_INTERVAL = 1
DEFAULT_HEALTH_CHECK_PATH = "/health/check"


class Config:
    host = DEFAULT_HOST
    port = DEFAULT_PORT
    watcher_interval_seconds = DEFAULT_WATCHER_INTERVAL
    router_config_path = None
    is_health_check_enabled = False
    health_check_path = DEFAULT_HEALTH_CHECK_PATH

    def load_from_env(self):
        #  Server configs
        self.host = os.getenv("HOST", default=DEFAULT_HOST)
        self.port = load_int("PORT", default=DEFAULT_PORT)

        #  Router configs
        self.router_config_path = os.getenv("ROUTER_CONFIG_PATH")

        # File watcher configs
        self.watcher_interval_seconds = load_int(
            "WATCHER_INTERVAL_SECONDS", default=DEFAULT_WATCHER_INTERVAL)

        # Health check configs
        self.is_health_check_enabled = load_bool("HEALTH_CHECK_ENABLED")
        self.health_check_path = os.getenv(
            "HEALTH_CHECK_PATH", default=DEFAULT_HEALTH_CHECK_PATH)


def load_int(env_var, default):
    try:
        return int(os.getenv(env_var, default))
    except ValueError:
        raise ValueError(f"{env_var} must be an integer")


def load_bool(env_var, default="False"):
    return os.getenv(env_var, default).lower() in ENV_TRUE_VALUES

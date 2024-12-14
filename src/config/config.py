import os

ENV_TRUE_VALUES = ('true', '1')


class Config:
    def __init__(self):
        #  Server configs
        self.host = os.environ.get("HOST", default="0.0.0.0")
        self.port = int(os.environ.get("PORT", default="3000"))

        #  Router configs
        self.router_config_path = os.environ.get("ROUTER_CONFIG_PATH")

        # File watcher configs
        self.watcher_interval_seconds = int(
            os.environ.get("WATCHER_INTERVAL_SECONDS", default=1))

        #  Health check configs
        health_check_enabled_val = os.getenv(
            "HEALTH_CHECK_ENABLED",
            default="False"
        ).lower()
        self.is_health_check_enabled = health_check_enabled_val in ENV_TRUE_VALUES
        self.health_check_path = os.environ.get(
            "HEALTH_CHECK_PATH", default="/health/check")

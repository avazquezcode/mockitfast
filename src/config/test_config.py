import unittest
from unittest.mock import patch
import os

# Assuming the provided code is in a module named config_module
from config.config import Config, load_int, load_bool, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_WATCHER_INTERVAL, DEFAULT_HEALTH_CHECK_PATH, ENV_TRUE_VALUES


class TestConfig_LoadFromEnv(unittest.TestCase):
    @patch.dict(os.environ, {}, clear=True)
    def test_default_config(self):
        config = Config()
        config.load_from_env()

        self.assertEqual(config.host, DEFAULT_HOST)
        self.assertEqual(config.port, DEFAULT_PORT)
        self.assertEqual(config.watcher_interval_seconds,
                         DEFAULT_WATCHER_INTERVAL)
        self.assertFalse(config.is_health_check_enabled)
        self.assertEqual(config.health_check_path, DEFAULT_HEALTH_CHECK_PATH)
        self.assertIsNone(config.router_config_path)  # No default provided

    @patch.dict(os.environ, {"HOST": "127.0.0.1", "PORT": "8080", "WATCHER_INTERVAL_SECONDS": "5", "HEALTH_CHECK_ENABLED": "true", "HEALTH_CHECK_PATH": "/status"}, clear=True)
    def test_config_with_env_variables_partially_provided(self):
        config = Config()
        config.load_from_env()

        self.assertEqual(config.host, "127.0.0.1")
        self.assertEqual(config.port, 8080)
        self.assertEqual(config.watcher_interval_seconds, 5)
        self.assertTrue(config.is_health_check_enabled)
        self.assertEqual(config.health_check_path, "/status")
        self.assertIsNone(config.router_config_path)  # No default provided

    @patch.dict(os.environ, {"HOST": "127.0.0.1", "PORT": "8080", "WATCHER_INTERVAL_SECONDS": "5", "HEALTH_CHECK_ENABLED": "true", "HEALTH_CHECK_PATH": "/status", "ROUTER_CONFIG_PATH": "config.json"}, clear=True)
    def test_config_with_env_variables_all_provided(self):
        config = Config()
        config.load_from_env()

        self.assertEqual(config.host, "127.0.0.1")
        self.assertEqual(config.port, 8080)
        self.assertEqual(config.watcher_interval_seconds, 5)
        self.assertTrue(config.is_health_check_enabled)
        self.assertEqual(config.health_check_path, "/status")
        self.assertEqual(config.router_config_path, "config.json")

    @patch.dict(os.environ, {"PORT": "not_an_int"}, clear=True)
    def test_load_int_invalid_value(self):
        with self.assertRaises(ValueError) as context:
            load_int("PORT", default=DEFAULT_PORT)
        self.assertIn("PORT must be an integer", str(context.exception))

    def test_load_bool(self):
        for true_value in ENV_TRUE_VALUES:
            with patch.dict(os.environ, {"TEST_BOOL": true_value}):
                self.assertTrue(load_bool("TEST_BOOL"))

        for false_value in ["false", "0", "no", ""]:
            with patch.dict(os.environ, {"TEST_BOOL": false_value}):
                self.assertFalse(load_bool("TEST_BOOL"))

        with patch.dict(os.environ, {}, clear=True):  # Test default value
            self.assertFalse(load_bool("TEST_BOOL"))

    def test_load_int_with_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(load_int("MISSING_ENV", default=42), 42)

    def test_load_bool_with_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(load_bool("MISSING_BOOL", default="false"))
            self.assertTrue(load_bool("MISSING_BOOL", default="true"))


if __name__ == "__main__":
    unittest

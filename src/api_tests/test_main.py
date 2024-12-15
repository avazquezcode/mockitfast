from api.app import get_app
from domain.model import Router
from config.config import Config

from fastapi.testclient import TestClient

import unittest
from dataclasses import dataclass


class Test(unittest.TestCase):
    router = Router()
    router.endpoints = []
    config = Config()

    # enable health check
    config.is_health_check_enabled = True

    app = get_app(router, config)
    client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/health/check")
        print(response)
        assert response.status_code == 200
        assert response.json() == {"success": True}


if __name__ == '__main__':
    unittest.main()

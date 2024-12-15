from api_tests.endpoints import get_endpoints
from api.app import get_app
from domain.model import Router
from config.config import Config

from fastapi.testclient import TestClient

import unittest
from dataclasses import dataclass


class Test(unittest.TestCase):
    router = Router(
        endpoints=get_endpoints(),
    )
    config = Config()
    config.is_health_check_enabled = True
    app = get_app(router, config)
    client = TestClient(app)

    def test_get_plain_text(self):
        response = self.client.get("/api/test/endpoint")
        assert response.headers == {
            "content-type": "text/plain",
            "content-length": "4"
        }
        assert response.status_code == 200
        assert response.text == "test"

    def test_health_check(self):
        response = self.client.get("/health/check")
        assert response.status_code == 200
        assert response.json() == {"success": True}


if __name__ == '__main__':
    unittest.main()

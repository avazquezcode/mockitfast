import unittest
from dataclasses import dataclass

from api.tests.endpoints import get_endpoints
from api.app import get_app
from domain.model import Router
from config.config import Config

from fastapi.testclient import TestClient

CONTENT_TYPE_HEADER = "content-type"


class Test(unittest.TestCase):
    router = Router(
        endpoints=get_endpoints(),
    )
    config = Config()
    config.is_health_check_enabled = True
    app = get_app(router, config)
    client = TestClient(app)

    # Basic cases

    def test_get_plain_text(self):
        response = self.client.get("/text")
        assert CONTENT_TYPE_HEADER in response.headers
        assert response.headers[CONTENT_TYPE_HEADER] == "text/plain"
        assert response.status_code == 200
        assert response.text == "test"

    def test_get_json(self):
        response = self.client.get("/json")
        assert CONTENT_TYPE_HEADER in response.headers
        assert response.headers[CONTENT_TYPE_HEADER] == "application/json"
        assert response.status_code == 200
        assert response.json() == {"success": True}

    def test_get_html(self):
        response = self.client.get("/html")
        assert CONTENT_TYPE_HEADER in response.headers
        assert response.headers[CONTENT_TYPE_HEADER] == "text/html"
        assert response.status_code == 200
        assert response.text == "<p>hey</p>"

    # Templating

    def test_templating_get_plain_text(self):
        response = self.client.get("/text/1")
        assert CONTENT_TYPE_HEADER in response.headers
        assert response.headers[CONTENT_TYPE_HEADER] == "text/plain"
        assert response.status_code == 200
        assert response.text == "test 1"

    def test_templating_get_json(self):
        response = self.client.get("/json/1")
        assert CONTENT_TYPE_HEADER in response.headers
        assert response.headers[CONTENT_TYPE_HEADER] == "application/json"
        assert response.status_code == 200
        assert response.json() == {
            "success": True,
            "user_id_1": "abc",
            "abc": "1",
        }

    #  Delay
    def test_delay(self):
        response = self.client.get("/delay")
        assert CONTENT_TYPE_HEADER in response.headers
        assert response.headers[CONTENT_TYPE_HEADER] == "text/plain"
        assert response.status_code == 200
        assert response.text == "test"

    # Health check

    def test_health_check(self):
        response = self.client.get("/health/check")
        assert response.status_code == 200
        assert response.json() == {"success": True}


if __name__ == '__main__':
    unittest.main()

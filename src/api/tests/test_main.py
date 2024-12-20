import unittest

from api.tests.endpoints import get_endpoints, SUPPORTED_METHODS
from api.app import get_app
from domain.model import Router
from config.config import Config

from fastapi.testclient import TestClient

HEADER_CONTENT_TYPE = "content-type"
HEADER_LOCATION = "location"


class Test(unittest.TestCase):
    # ------------- #
    # Initial Setup #
    # ------------- #

    router = Router(
        endpoints=get_endpoints(),
    )
    config = Config()
    config.is_health_check_enabled = True
    app = get_app(router, config)
    client = TestClient(app)

    # ------------- #
    # Basic cases   #
    # ------------- #

    def test_plain_text(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/text")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/plain"
            assert response.status_code == 200
            assert response.text == "test"

    def test_json(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/json")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "application/json"
            assert response.status_code == 200
            assert response.json() == {"success": True}

    def test_html(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/html")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/html"
            assert response.status_code == 200
            assert response.text == "<p>hey</p>"

    def test_xml(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/xml")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "application/xml"
            assert response.status_code == 200
            assert response.text == "<accounts></accounts>"

    def test_redirect(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(
                method, "/redirect", follow_redirects=False
            )
            assert HEADER_LOCATION in response.headers
            assert response.headers[HEADER_LOCATION] == "http://google.com"
            assert response.status_code == 307

    def test_no_content_type_str(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/no-content-type-str")
            assert HEADER_CONTENT_TYPE not in response.headers
            assert response.status_code == 200
            assert response.text == "test"

    def test_no_content_type_json(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/no-content-type-json")
            assert HEADER_CONTENT_TYPE not in response.headers
            assert response.status_code == 200
            assert response.json() == {"success": True}

    # --------------- #
    # Path Templating #
    # --------------- #

    def test_path_templating_plain_text(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/text/1")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/plain"
            assert response.status_code == 200
            assert response.text == "test 1"

    def test_path_templating_json(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/json/1")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "application/json"
            assert response.status_code == 200
            assert response.json() == {
                "success": True,
                "user_id_1": "abc",
                "abc": "1",
            }

    def test_path_templating_html(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/html/1")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/html"
            assert response.status_code == 200
            assert response.text == "<p>1</p>"

    def test_path_templating_xml(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/xml/1")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "application/xml"
            assert response.status_code == 200
            assert response.text == "<accounts_1></accounts_1>"

    #  Test precedence of path variables (among the rest)
    def test_path_templating_plain_text_precedence(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/text/1?user_id=2")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/plain"
            assert response.status_code == 200
            assert response.text == "test 1"

    # ---------------- #
    # Query Templating #
    # ---------------- #

    def test_query_templating_plain_text(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(
                method, "/text_templating?user_id=1"
            )
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/plain"
            assert response.status_code == 200
            assert response.text == "test 1"

    def test_query_templating_json(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(
                method, "/json_templating?user_id=1"
            )
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "application/json"
            assert response.status_code == 200
            assert response.json() == {
                "success": True,
                "user_id_1": "abc",
                "abc": "1",
            }

    def test_query_templating_html(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(
                method, "/html_templating?user_id=1"
            )
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/html"
            assert response.status_code == 200
            assert response.text == "<p>1</p>"

    def test_query_templating_xml(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(
                method, "/xml_templating?user_id=1"
            )
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "application/xml"
            assert response.status_code == 200
            assert response.text == "<accounts_1></accounts_1>"

    #  Test precedence of query parameters variables (among header ones)
    def test_query_templating_plain_text_precedence(self):
        for method in SUPPORTED_METHODS:
            headers = {"user_id": "3"}
            response = self.client.request(
                method, "/text_templating?user_id=1", headers=headers
            )
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/plain"
            assert response.status_code == 200
            assert response.text == "test 1"

    # ------------------ #
    # Headers Templating #
    # ------------------ #

    def test_headers_templating_plain_text(self):
        for method in SUPPORTED_METHODS:
            headers = {"user_id": "1"}
            response = self.client.request(
                method, "/text_templating", headers=headers)
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/plain"
            assert response.status_code == 200
            assert response.text == "test 1"

    def test_headers_templating_json(self):
        for method in SUPPORTED_METHODS:
            headers = {"user_id": "1"}
            response = self.client.request(
                method, "/json_templating", headers=headers)
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "application/json"
            assert response.status_code == 200
            assert response.json() == {
                "success": True,
                "user_id_1": "abc",
                "abc": "1",
            }

    def test_headers_templating_html(self):
        for method in SUPPORTED_METHODS:
            headers = {"user_id": "1"}
            response = self.client.request(
                method, "/html_templating", headers=headers
            )
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/html"
            assert response.status_code == 200
            assert response.text == "<p>1</p>"

    def test_headers_templating_xml(self):
        for method in SUPPORTED_METHODS:
            headers = {"user_id": "1"}
            response = self.client.request(
                method, "/xml_templating", headers=headers
            )
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "application/xml"
            assert response.status_code == 200
            assert response.text == "<accounts_1></accounts_1>"

    # ------------- #
    # Delay         #
    # ------------- #

    def test_delay(self):
        for method in SUPPORTED_METHODS:
            response = self.client.request(method, "/delay")
            assert HEADER_CONTENT_TYPE in response.headers
            assert response.headers[HEADER_CONTENT_TYPE] == "text/plain"
            assert response.status_code == 200
            assert response.text == "test"

    # ------------- #
    # Health check  #
    # ------------- #

    def test_health_check(self):
        response = self.client.get("/health/check")
        assert response.status_code == 200
        assert response.json() == {"success": True}


if __name__ == '__main__':
    unittest.main()

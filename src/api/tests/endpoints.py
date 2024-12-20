from domain.model import Endpoint, Response

SUPPORTED_METHODS = [
    "GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "TRACE", "CONNECT",
]


def get_endpoints() -> list[Endpoint]:
    endpoints = []
    for method in SUPPORTED_METHODS:
        endpoints.extend(_get_base_endpoints(method))
    return endpoints


def _get_base_endpoints(method: str) -> list[Endpoint]:
    return [
        # Plain text endpoint
        Endpoint(
            path="/text",
            method=method,
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                body="test"
            ),
        ),
        # JSON endpoint
        Endpoint(
            path="/json",
            method=method,
            response=Response(
                headers={"Content-Type": "application/json"},
                status=200,
                body={
                    "success": True,
                },
            ),
        ),
        # HTML endpoint
        Endpoint(
            path="/html",
            method=method,
            response=Response(
                headers={"Content-Type": "text/html"},
                status=200,
                body="<p>hey</p>",
            ),
        ),
        # XML endpoint
        Endpoint(
            path="/xml",
            method=method,
            response=Response(
                headers={"Content-Type": "application/xml"},
                status=200,
                body="<accounts></accounts>",
            ),
        ),
        # Redirect
        Endpoint(
            path="/redirect",
            method=method,
            response=Response(
                headers={"Content-Type": "redirect",
                         "location": "http://google.com"},
                status=307,
            ),
        ),
        # No content type (string)
        Endpoint(
            path="/no-content-type-str",
            method=method,
            response=Response(
                status=200,
                body="test",
            ),
        ),
        # No content type (json)
        Endpoint(
            path="/no-content-type-json",
            method=method,
            response=Response(
                status=200,
                body={
                    "success": True,
                },
            ),
        ),
        # Plain text endpoint - with templating
        Endpoint(
            path="/text_templating",
            method=method,
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                body="test {user_id}"
            ),
        ),
        # JSON endpoint - with templating
        Endpoint(
            path="/json_templating",
            method=method,
            response=Response(
                headers={"Content-Type": "application/json"},
                status=200,
                body={
                    "success": True,
                    "user_id_{user_id}": "abc",
                    "abc": "{user_id}",
                },
            ),
        ),
        # HTML endpoint - with templating
        Endpoint(
            path="/html_templating",
            method=method,
            response=Response(
                headers={"Content-Type": "text/html"},
                status=200,
                body="<p>{user_id}</p>"
            ),
        ),
        # XML endpoint - with templating
        Endpoint(
            path="/xml_templating",
            method=method,
            response=Response(
                headers={"Content-Type": "application/xml"},
                status=200,
                body="<accounts_{user_id}></accounts_{user_id}>",
            ),
        ),
        # Plain text endpoint - with path templating
        Endpoint(
            path="/text/{user_id}",
            method=method,
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                body="test {user_id}"
            ),
        ),
        # JSON endpoint - with path templating
        Endpoint(
            path="/json/{user_id}",
            method=method,
            response=Response(
                headers={"Content-Type": "application/json"},
                status=200,
                body={
                    "success": True,
                    "user_id_{user_id}": "abc",
                    "abc": "{user_id}",
                },
            ),
        ),
        # HTML endpoint - with path templating
        Endpoint(
            path="/html/{user_id}",
            method=method,
            response=Response(
                headers={"Content-Type": "text/html"},
                status=200,
                body="<p>{user_id}</p>"
            ),
        ),
        # XML endpoint - with path templating
        Endpoint(
            path="/xml/{user_id}",
            method=method,
            response=Response(
                headers={"Content-Type": "application/xml"},
                status=200,
                body="<accounts_{user_id}></accounts_{user_id}>",
            ),
        ),
        # Delay
        Endpoint(
            path="/delay",
            method=method,
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                delay=1,
                body="test"
            ),
        ),
    ]

from domain.model import Endpoint, Response


def get_endpoints() -> list[Endpoint]:
    return [
        # GET: Plain text endpoint
        Endpoint(
            path="/text",
            method="GET",
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                body="test"
            ),
        ),
        # GET: JSON endpoint
        Endpoint(
            path="/json",
            method="GET",
            response=Response(
                headers={"Content-Type": "application/json"},
                status=200,
                body={
                    "success": True,
                },
            ),
        ),
        # GET: HTML endpoint
        Endpoint(
            path="/html",
            method="GET",
            response=Response(
                headers={"Content-Type": "text/html"},
                status=200,
                body="<p>hey</p>",
            ),
        ),
        # GET: XML endpoint
        Endpoint(
            path="/xml",
            method="GET",
            response=Response(
                headers={"Content-Type": "application/xml"},
                status=200,
                body="<accounts></accounts>",
            ),
        ),
        # GET: Redirect
        Endpoint(
            path="/redirect",
            method="GET",
            response=Response(
                headers={"Content-Type": "redirect",
                         "location": "http://google.com"},
                status=307,
            ),
        ),
        # GET: No content type (string)
        Endpoint(
            path="/no-content-type-str",
            method="GET",
            response=Response(
                status=200,
                body="test",
            ),
        ),
        # GET: No content type (json)
        Endpoint(
            path="/no-content-type-json",
            method="GET",
            response=Response(
                status=200,
                body={
                    "success": True,
                },
            ),
        ),
        # GET: Plain text endpoint - with templating
        Endpoint(
            path="/text/{user_id}",
            method="GET",
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                body="test {user_id}"
            ),
        ),
        # GET: JSON endpoint - with templating
        Endpoint(
            path="/json/{user_id}",
            method="GET",
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
        # GET: HTML endpoint - with templating
        Endpoint(
            path="/html/{user_id}",
            method="GET",
            response=Response(
                headers={"Content-Type": "text/html"},
                status=200,
                body="<p>{user_id}</p>"
            ),
        ),
        # GET: XML endpoint - with templating
        Endpoint(
            path="/xml/{user_id}",
            method="GET",
            response=Response(
                headers={"Content-Type": "application/xml"},
                status=200,
                body="<accounts_{user_id}></accounts_{user_id}>",
            ),
        ),
        # GET: Plain text endpoint - with query templating
        Endpoint(
            path="/text_query_templating",
            method="GET",
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                body="test {user_id}"
            ),
        ),
        # GET: JSON endpoint - with query templating
        Endpoint(
            path="/json_query_templating",
            method="GET",
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
        # GET: HTML endpoint - with query templating
        Endpoint(
            path="/html_query_templating",
            method="GET",
            response=Response(
                headers={"Content-Type": "text/html"},
                status=200,
                body="<p>{user_id}</p>"
            ),
        ),
        # GET: XML endpoint - with query templating
        Endpoint(
            path="/xml_query_templating",
            method="GET",
            response=Response(
                headers={"Content-Type": "application/xml"},
                status=200,
                body="<accounts_{user_id}></accounts_{user_id}>",
            ),
        ),
        # Delay
        Endpoint(
            path="/delay",
            method="GET",
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                delay=1,
                body="test"
            ),
        ),
    ]

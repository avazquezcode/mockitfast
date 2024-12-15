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

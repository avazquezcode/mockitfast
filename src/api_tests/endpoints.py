from domain.model import Endpoint, Response


def get_endpoints() -> list[Endpoint]:
    return [
        # Plain text endpoint
        Endpoint(
            path="/api/test/endpoint",
            method="GET",
            response=Response(
                headers={"Content-Type": "text/plain"},
                status=200,
                body="test"
            ),
        ),
    ]

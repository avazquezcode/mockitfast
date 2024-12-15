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
    ]

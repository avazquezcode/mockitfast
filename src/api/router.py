from domain.model import Router
from api.handler import Handler
from fastapi import APIRouter
from fastapi import Response as FastAPIResponse

CONTENT_TYPE_HEADER = "Content-Type"
DEFAULT_CONTENT_TYPE = "undefined"


def get_api_router(router: Router) -> APIRouter:
    api_router = APIRouter()

    for endpoint in router.endpoints:
        handler = Handler(endpoint.response)
        content_type = get_content_type(endpoint.response.headers)
        response_examples = build_response_examples(endpoint, content_type)

        api_router.add_api_route(
            endpoint.path,
            handler.response,
            methods=[endpoint.method],
            name=endpoint.name,
            description=endpoint.description,
            status_code=endpoint.response.status,
            response_class=FastAPIResponse,
            responses=response_examples,
        )

    return api_router


def get_content_type(headers) -> str:
    if headers and CONTENT_TYPE_HEADER in headers:
        return headers[CONTENT_TYPE_HEADER]
    return DEFAULT_CONTENT_TYPE


def build_response_examples(endpoint, content_type) -> dict:
    return {
        endpoint.response.status: {
            "description": "Mocked response",
            "content": {
                content_type: {
                    "example": endpoint.response.body,
                }
            },
        }
    }

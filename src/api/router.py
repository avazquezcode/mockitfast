import json
import time

from domain.model import Router, Response

from fastapi import APIRouter
from fastapi import Response as FastAPIResponse
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse, RedirectResponse


class Handler:
    def __init__(self, response_config: Response):
        self.data = response_config

    def response(self):
        if self.data.delay is not None:
            time.sleep(self.data.delay)

        body = self.data.body
        if type(body) is dict:
            body = json.dumps(body)

        return FastAPIResponse(body, self.data.status, self.data.headers)


def get_api_router(router: Router) -> APIRouter:
    api_router = APIRouter()

    for endpoint in router.endpoints:
        handler = Handler(endpoint.response)
        content_type_header = "application/json"  #  default
        if endpoint.response.headers and "Content-Type" in endpoint.response.headers:
            content_type_header = endpoint.response.headers["Content-Type"]

        response_class = map_response_class(content_type_header)
        api_router.add_api_route(endpoint.path,
                                 handler.response,
                                 methods=[endpoint.method],
                                 name=endpoint.name,
                                 description=endpoint.description,
                                 status_code=endpoint.response.status,
                                 response_class=response_class,
                                 responses={
                                     endpoint.response.status: {
                                         "description": "Mocked response",
                                         "content": {
                                             content_type_header: {
                                                 "example": endpoint.response.body
                                             }
                                         }
                                     },
                                 },
                                 )
    return api_router


def map_response_class(content_type: str):
    match content_type:
        case "application/json":
            return JSONResponse
        case "text/html":
            return HTMLResponse
        case "text/plain":
            return PlainTextResponse
        case "redirect":
            return RedirectResponse
        case _:
            return FastAPIResponse

from fastapi import FastAPI

from domain.model import Router
from api.router import get_api_router


def get_app(router: Router):
    app = FastAPI()
    app.description = "Mockitfast API"
    app.title = "Mockitfast"

    for endpoint in router.endpoints:
        app.include_router(get_api_router(endpoint))

    return app

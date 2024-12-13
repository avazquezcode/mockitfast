from fastapi import FastAPI

from domain.model import Router
from api.router import get_api_router
from api.healtcheck import health_check


def get_app(router: Router):
    app = FastAPI()
    app.description = "Mockitfast API"
    app.title = "Mockitfast"

    api_router = get_api_router(router)

    # Add API health check
    api_router.add_api_route('/health/check', endpoint=health_check)

    app.include_router(api_router)
    return app

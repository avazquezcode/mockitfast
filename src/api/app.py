from fastapi import FastAPI

from domain.model import Router
from api.router import get_api_router
from api.healtcheck import health_check
from config.config import Config


def get_app(router: Router, config: Config):
    app = FastAPI()
    app.description = "Mockitfast API"
    app.title = "Mockitfast"

    api_router = get_api_router(router)

    if config.is_health_check_enabled:
        api_router.add_api_route(
            config.health_check_path,
            endpoint=health_check
        )

    app.include_router(api_router)
    return app

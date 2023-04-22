
from middlewares import RedisMiddleware

from fastapi import FastAPI
from routers.user_router import user_router
from config import get_settings
from fastapi_pagination import add_pagination


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title='Тестовое приложение',
        version='0.0.1a'
    )

    app.include_router(user_router)
    app.add_middleware(
        RedisMiddleware,
        settings=settings
    )
    add_pagination(app)
    return app


app = create_app()

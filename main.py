from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from pydantic.dataclasses import dataclass
# from dataclasses import dataclass

from fastapi import FastAPI, Query, Path, APIRouter, HTTPException
from starlette.responses import Response
from routers.user_router import user_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='Тестовое приложение',
        version='0.0.1a'
    )

    app.include_router(user_router)
    return app


app = create_app()

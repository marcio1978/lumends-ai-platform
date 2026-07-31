from fastapi import FastAPI

from app.api.health import router as health_router
from app.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.include_router(health_router)

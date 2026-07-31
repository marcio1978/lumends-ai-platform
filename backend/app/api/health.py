from fastapi import APIRouter

from app.settings import settings

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "application": settings.APP_NAME,
        "version": settings.VERSION,
    }

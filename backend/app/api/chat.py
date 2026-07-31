from fastapi import APIRouter

from app.core.engine import LAPEngine


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


engine = LAPEngine()


@router.post("/")
async def chat(message: str):

    result = engine.process(message)

    return result

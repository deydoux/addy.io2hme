from fastapi import APIRouter
from .routes.aliases import router as aliases_router


router = APIRouter(prefix="/api/v1")
router.include_router(aliases_router)

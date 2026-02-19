
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .routes.aliases import router as aliases_router

from os import environ


token = environ.get("HME_TOKEN")
if not token:
	raise ValueError("HME_TOKEN environment variable is not set")

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
	if credentials.credentials != token:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid token",
		)


router = APIRouter(prefix="/api/v1", dependencies=[Depends(verify_token)])
router.include_router(aliases_router)

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from .api import api_router
from .icloud import HideMyEmail


cookies = (Path(__file__).resolve().parents[1] / "cookies.txt").read_text()

@asynccontextmanager
async def lifespan(app: FastAPI):
	async with HideMyEmail(cookies) as hme:
		app.state.hme = hme
		yield

app = FastAPI(docs_url=None, openapi_url=None, redoc_url=None, lifespan=lifespan)
app.include_router(api_router)

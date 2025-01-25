from dotenv import load_dotenv
from fastapi import FastAPI

from routes import base

load_dotenv(".env")

app = FastAPI()

app.include_router(base.base_router, prefix="/api/v1", tags=["Base"])

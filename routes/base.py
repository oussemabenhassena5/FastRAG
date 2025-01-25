import os

from fastapi import APIRouter

base_router = APIRouter()


@base_router.get("/")
async def root():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "message": "Server is up and running",
        "app_name": app_name,
        "app_version": app_version,
    }

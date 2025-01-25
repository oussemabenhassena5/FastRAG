from fastapi import APIRouter, Depends

from helpers.config import Settings, get_settings

base_router = APIRouter()


@base_router.get("/")
async def root(app_settings: Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "message": "Server is up and running",
        "app_name": app_name,
        "app_version": app_version,
    }

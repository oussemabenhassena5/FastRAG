from fastapi import APIRouter, UploadFile,Depends
from helpers.config import Settings, get_settings



data_router = APIRouter()

@data_router.get("/upload/{project_id}")
async def upload_data(project_id: str,file: UploadFile,app_settings: Settings = Depends(get_settings)):
from .BaseController import BaseController
from fastapi import HTTPException, UploadFile


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576  # convert MB to bytes

    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            raise HTTPException(status_code=400, detail="File type not allowed")
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            raise HTTPException(status_code=400, detail="File size too large")

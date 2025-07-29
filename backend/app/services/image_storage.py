# services/image_storage.py
import os
import uuid
import shutil
from fastapi import UploadFile

UPLOAD_FOLDER = "uploaded_images"

def save_image_locally(file: UploadFile) -> str:
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return filename  # Tu peux construire l'URL à partir de ça dans la route

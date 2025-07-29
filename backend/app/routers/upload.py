# routers/upload.py
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import FileResponse
from utils.auth import get_current_user
import os
from services.image_storage import save_image_locally
from models.user import User


UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "uploaded_images")
router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/image")
async def upload_image(file: UploadFile = File(...), user: User = Depends(get_current_user)):
    # Vérification du type MIME (exemple pour images seulement)
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    filename = save_image_locally(file)
    foodimage = f"/upload/image/{filename}"
    return {"filename": filename, "url": foodimage}


@router.get("/image/{filename}")
def get_image(filename: str, user: User = Depends(get_current_user)):
    filepath = os.path.join(UPLOAD_DIR, filename)

    if not os.path.isfile(filepath):
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(filepath, media_type="image/jpeg")
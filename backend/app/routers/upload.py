# routers/upload.py
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from services.image_storage import save_image_locally
from utils.auth import get_current_user
from models.user import User


router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/image")
async def upload_image(file: UploadFile = File(...), user: User = Depends(get_current_user)):
    # Vérification du type MIME (exemple pour images seulement)
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    filename = save_image_locally(file)
    image_url = f"/images/{filename}"
    return {"filename": filename, "url": image_url}
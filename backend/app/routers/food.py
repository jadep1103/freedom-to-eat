from fastapi import APIRouter, HTTPException, Depends 
from db.database import get_db
from utils.auth import get_current_user
from models.user import User 
from sqlalchemy.orm import Session
from schema.entry import FoodEntryCreate, FoodEntryUpdate, FoodEntryRead
from crud import food as food_crud

# Create a new router for food-related endpoints
router = APIRouter(prefix="/food", tags=["Food"])

# Add a nex food entry 
@router.post("/", response_model=FoodEntryRead)
def create_entry(entry: FoodEntryCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """
    Create a new food entry.
    """
    new_entry = FoodEntryCreate(**entry.dict())
    return food_crud.create_food_entry(db, new_entry, user.id)

# Read a food entry by ID 
@router.get("/{entry_id}", response_model=FoodEntryRead)
def read_entry(entry_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user) ):
    """
    Retrieve a food entry by its ID.
    """
    entry = food_crud.get_food_entry(db, entry_id, user.id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

# Read all food entries 
@router.get("/", response_model=list[FoodEntryRead])
def read_all_entries(db: Session=Depends(get_db), user: User = Depends(get_current_user)):
    """
    Retrieve all food entries.
    """
    return food_crud.get_all_food_entries(db,user.id)

# Update partially a food entry (patch like-only allowed)
@router.patch("/{entry_id}", response_model=FoodEntryUpdate)
def update_entry(entry_id: str, updated_entry: FoodEntryUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    """
    Update a food entry by its ID.
    """
    entry = food_crud.update_food_entry(db,entry_id, updated_entry, user.id)
    if not entry: 
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

# Delete a food entry
@router.delete("/{entry_id}", summary = "Delete a food entry")
def delete_entry(entry_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user) ):
    deleted = food_crud.delete_food_entry(db,entry_id,user.id)
    if not deleted:
        raise HTTPException(status_code=404, details="Entry not found")
    return {"message": "Entry deleted successfully"}


from sqlalchemy.orm import Session
from uuid import UUID
from models.food import FoodEntry
from schema.entry import FoodEntryCreate, FoodEntryUpdate, FoodEntryRead

def create_food_entry(db: Session, entry: FoodEntryCreate, user_id: str) -> FoodEntryRead:
    db_entry = FoodEntry(**entry.dict(), user_id = user_id)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return FoodEntryRead.from_orm(db_entry)

def get_food_entry(db: Session, entry_id: str, user_id: str) -> FoodEntryRead | None:
    db_entry = db.query(FoodEntry).filter(FoodEntry.id == UUID(entry_id), FoodEntry.user_id == user_id).first()
    if not db_entry:
        return None
    return FoodEntryRead.from_orm(db_entry)

def get_all_food_entries(db: Session, user_id : str) -> list[FoodEntryRead]:
    db_entries = db.query(FoodEntry).filter(FoodEntry.user_id ==  user_id).all()
    return [FoodEntryRead.from_orm(entry) for entry in db_entries]

def update_food_entry(db: Session, entry_id: str, updated_entry: FoodEntryUpdate, user_id: str) -> FoodEntryRead | None:
    db_entry = db.query(FoodEntry).filter(FoodEntry.id == UUID(entry_id), FoodEntry.user_id == user_id).first()
    if not db_entry:
        return None
    
    update_data = updated_entry.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_entry, key, value)
    
    db.commit()
    db.refresh(db_entry)
    return FoodEntryRead.from_orm(db_entry)

def delete_food_entry(db: Session, entry_id: str, user_id: str) -> bool:
    db_entry = db.query(FoodEntry).filter(FoodEntry.id == UUID(entry_id), FoodEntry.user_id == user_id).first()
    if not db_entry:
        return False
    db.delete(db_entry)
    db.commit()
    return True

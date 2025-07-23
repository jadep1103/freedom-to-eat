from sqlalchemy.orm import Session
from uuid import UUID
from models.food import FoodEntryModel
from schema.entry import FoodEntryCreate, FoodEntryUpdate, FoodEntry

def create_food_entry(db: Session, entry: FoodEntryCreate) -> FoodEntry:
    db_entry = FoodEntryModel(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return FoodEntry.from_orm(db_entry)

def get_food_entry(db: Session, entry_id: str) -> FoodEntry | None:
    db_entry = db.query(FoodEntryModel).filter(FoodEntryModel.id == UUID(entry_id)).first()
    if not db_entry:
        return None
    return FoodEntry.from_orm(db_entry)

def get_all_food_entries(db: Session) -> list[FoodEntry]:
    db_entries = db.query(FoodEntryModel).all()
    return [FoodEntry.from_orm(entry) for entry in db_entries]

def update_food_entry(db: Session, entry_id: str, updated_entry: FoodEntryUpdate) -> FoodEntry | None:
    db_entry = db.query(FoodEntryModel).filter(FoodEntryModel.id == UUID(entry_id)).first()
    if not db_entry:
        return None
    
    update_data = updated_entry.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_entry, key, value)
    
    db.commit()
    db.refresh(db_entry)
    return FoodEntry.from_orm(db_entry)

def delete_food_entry(db: Session, entry_id: str) -> bool:
    db_entry = db.query(FoodEntryModel).filter(FoodEntryModel.id == UUID(entry_id)).first()
    if not db_entry:
        return False
    db.delete(db_entry)
    db.commit()
    return True

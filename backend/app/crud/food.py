import uuid 
from schema.entry import FoodEntry,FoodEntryCreate, FoodEntryUpdate
from db.database import food_db

def create_food_entry(entry : FoodEntryCreate) -> FoodEntry:
	"""
	Create a new food entry in the database.
	"""
	food_db[entry.id] = entry
	return entry

def get_food_entry(entry_id: str) -> FoodEntry:
	"""
	Retrieve a food entry by its ID.
	"""
	return food_db.get(entry_id)

def get_all_food_entries() -> list[FoodEntry]:
	"""
	Retrieve all food entries from the database.
	"""
	return list(food_db.values())

def update_food_entry(entry_id: str, updated_entry: FoodEntryUpdate) -> FoodEntry:
	"""
	Update a food entry by its id - Patch like update 
	"""
	existing_entry = food_db.get(entry_id)
	if not existing_entry: 
		return None
	entry_data = existing_entry.dict()
	#Apply updates only to fields that are provided
	update_data = updated_entry.dict(exclude_unset=True)
	entry_data.update(update_data)
	# Create a new FoodEntry instance with the updated data (passage dict to FoodEntry)
	updated = FoodEntry(**entry_data)
	food_db[entry_id] = updated
	return updated

def delete_food_entry(entry_id: str) -> bool:  
	"""
	Delete a food entry by its id
	"""
	if entry_id in food_db:
		del food_db[entry_id]
		return True
	else: 
		return False
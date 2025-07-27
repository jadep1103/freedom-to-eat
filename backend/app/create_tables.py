# create_tables.py

from db.database import engine
from models.base import Base
from models.user import User
from models.food import FoodEntry

print("Création des tables en cours...")
Base.metadata.create_all(bind=engine)
print("Tables créées avec succès.")

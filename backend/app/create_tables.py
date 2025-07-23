# create_tables.py

from db.database import engine
from models.food import Base

print("Création des tables en cours...")
Base.metadata.create_all(bind=engine)
print("Tables créées avec succès.")

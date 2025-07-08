from sqlalchemy import create_engine
from sqlalchemy.orm import Session 

# Create a SQLAlchemy engine -> connect to PostgreSQL database 
DATABASE_URL = "postgresql+psycopg2://jadepillercammal@localhost:5432/food_entries"
engine = create_engine(DATABASE_URL)


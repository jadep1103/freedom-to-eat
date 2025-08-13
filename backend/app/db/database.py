from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import dotenv
from config import DATABASE_URL

# Create a SQLAlchemy engine -> connect to PostgreSQL database 
engine = create_engine(DATABASE_URL)

Session = sessionmaker(engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
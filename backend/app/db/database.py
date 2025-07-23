from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a SQLAlchemy engine -> connect to PostgreSQL database 
DATABASE_URL = "postgresql+psycopg2://jadepillercammal@localhost:5432/food_entries"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine, autoflash=False, autocommit=False, expire_on_commit=False)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
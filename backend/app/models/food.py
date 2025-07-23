from .base import Base 
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Enum
from enum import Enum as EnumPy
from sqlalchemy.dialects.postgresql import UUID as Uuid
from sqlalchemy.dialects.postgresql import ARRAY # For multi-select fields
from sqlalchemy.types import Enum as EnumSQLAlchemy
from uuid import uuid4

# Creating Enum classes for each multi-select 

class LocationEnum(str,EnumPy):
    home = "Home"
    gym = "Gym"
    work = "Work"
    restaurant = "Restaurant"
    outside = "Outside"
      
class CompanyEnum(str,EnumPy):
    family = "Family"
    colleagues = "Colleagues"   
    friends = "Friends"
    alone = "Alone"

class MealTypeEnum(str,EnumPy):
    breakfast = "Breakfast"
    lunch = "Lunch"
    dinner = "Dinner"
    snack = "Snack"
    other = "Other"

class EmotionsEnum(str, EnumPy):
    happy = "Happy"
    sad = "Sad"
    anxious = "Anxious"
    excited = "Excited"
    relaxed = "Relaxed"
    calm = "Calm"
    angry = "Angry"
    frustrated = "Frustrated"
    overwhelmed = "Overwhelmed"
    accomplished = "Accomplished"
    selfconscious = "Self-conscious"
    proud = "Proud"
    numb = "Numb"

class FoodEntry(Base): 
    __tablename__= 'food_entries'
    id = Column(Uuid, primary_key=True, default=uuid4)  # Use UUID for unique identifier
    timestamp = Column(DateTime, nullable = False)
    location = Column(EnumSQLAlchemy(LocationEnum), nullable = True) 
    company = Column(EnumSQLAlchemy(CompanyEnum), nullable = True)  #Transformer en Enum de SQLAlchemy
    mealtype = Column(EnumSQLAlchemy(MealTypeEnum), nullable = True)
    hungerlevel = Column(Integer, nullable = True)
    fullnesslevel = Column(Integer, nullable = True)
    stresslevel = Column(Integer, nullable = True)
    satisfactionlevel = Column(Integer, nullable = True)
    energylevel = Column(Integer, nullable = True)
    emotions = Column(ARRAY(EnumSQLAlchemy(EmotionsEnum)), nullable = True)
    atemindfully = Column(Boolean, nullable = True)
    fooddetails = Column(String, nullable = True) 
    notes = Column(String, nullable = True) 
    foodimage = Column(String, nullable = True)  # Store image path or URL -> Pydantic handles the validation of the image URL or path
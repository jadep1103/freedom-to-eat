from pydantic import BaseModel,conint,constr,Field,HttpUrl
from datetime import datetime 
from typing import Optional,List 
from enum import Enum
from uuid import uuid4, UUID

# Creating Enum classes for each multi-select 

class Location(str,Enum):
    home = "Home"
    gym = "Gym"
    work = "Work"
    restaurant = "Restaurant"
    outside = "Outside"
      
class Company(str,Enum):
    family = "Family"
    colleagues = "Colleagues"   
    friends = "Friends"
    alone = "Alone"

class MealType(str,Enum):
    breakfast = "Breakfast"
    lunch = "Lunch"
    dinner = "Dinner"
    snack = "Snack"
    other = "Other"

class Emotions(str, Enum):
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

class SleepEnv(str, Enum):
    home = "Home"
    hotel = "Hotel"
    someone_elses_home = "Another home"
    outside = "Outside"



class FoodEntryCreate(BaseModel): 
    timestamp: datetime 
    location : Optional[Location] = None
    company : Optional[Company] = None
    mealtype : Optional[MealType] = None
    hungerlevel : Optional[conint(ge=1, le=10)] = None  
    fullnesslevel : Optional[conint(ge=1, le=10)] = None  
    stresslevel : Optional[conint(ge=1, le=10)] = None  
    satisfactionlevel : Optional[conint(ge=1, le=10)] = None
    energylevel : Optional[conint(ge=1, le=10)] = None
    emotions : Optional[List[Emotions]]= None
    atemindfully : Optional[bool] = None  
    fooddetails : Optional[constr(min_length=1, max_length=800)] = None  
    notes : Optional[constr(min_length=1, max_length=1000)] = None    
    foodimage : Optional[HttpUrl] = None  # URL or path to food image

    class Config: 
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models
        from_attributes = True  # Allow attributes to be read from SQLAlchemy models

class FoodEntryUpdate(BaseModel): 
    timestamp: Optional[datetime] = None 
    location : Optional[Location] = None
    company : Optional[Company] = None
    mealtype : Optional[MealType] = None
    hungerlevel : Optional[conint(ge=1, le=10)] = None  
    fullnesslevel : Optional[conint(ge=1, le=10)] = None  
    stresslevel : Optional[conint(ge=1, le=10)] = None  
    satisfactionlevel : Optional[conint(ge=1, le=10)] = None
    energylevel : Optional[conint(ge=1, le=10)] = None
    emotions : Optional[List[Emotions]]= None
    atemindfully : Optional[bool] = None  
    fooddetails : Optional[constr(min_length=1, max_length=800)] = None  
    notes : Optional[constr(min_length=1, max_length=1000)] = None    
    foodimage : Optional[HttpUrl] = None  # URL or path to food image
    class Config: 
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models
        from_attributes = True  # Allow attributes to be read from SQLAlchemy models


class FoodEntryRead(BaseModel):
    id: UUID
    timestamp: datetime
    location : Optional[Location] = None
    company : Optional[Company] = None
    mealtype : Optional[MealType] = None
    hungerlevel: Optional[conint(ge=1, le=10)] = None
    fullnesslevel: Optional[conint(ge=1, le=10)] = None
    stresslevel: Optional[conint(ge=1, le=10)] = None
    satisfactionlevel: Optional[conint(ge=1, le=10)] = None
    energylevel: Optional[conint(ge=1, le=10)] = None
    emotions: Optional[List[Emotions]] = None
    atemindfully: Optional[bool] = None
    fooddetails: Optional[constr(min_length=1, max_length=800)] = None
    notes: Optional[constr(min_length=1, max_length=1000)] = None
    foodimage: Optional[HttpUrl] = None
    class Config: 
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models
        from_attributes = True  # Allow attributes to be read from SQLAlchemy models


class ExerciseEntry(BaseModel): 
    id :str = Field(default_factory=lambda: str(uuid4()))  
    timestamp: datetime 
    location :  Optional[List[Location]] = None
    company :  Optional[List[Company]] = None
    exercise_type : constr(min_length=1, max_length=800)
    duration : conint(ge=1) # in minutes
    intensity_level : Optional[conint(ge=1, le=10)] = None  
    mood_before :  Optional[List[Emotions]] = None
    mood_after :  Optional[List[Emotions]] = None
    notes : Optional[constr(min_length=1, max_length=1000)] = None    


class ExerciseEntryCreate(BaseModel): 
    timestamp: datetime 
    location :  Optional[List[Location]] = None
    company :  Optional[List[Company]] = None
    exercise_type : constr(min_length=1, max_length=800)
    duration : conint(ge=1) # in minutes
    intensity_level : Optional[conint(ge=1, le=10)] = None  
    mood_before :  Optional[List[Emotions]] = None
    mood_after :  Optional[List[Emotions]] = None
    notes : Optional[constr(min_length=1, max_length=1000)] = None   
   
class ExerciseEntryUpdate(BaseModel): 
    timestamp: Optional[datetime] = None
    location :  Optional[List[Location]] = None
    company :  Optional[List[Company]] = None
    exercise_type : Optional[constr(min_length=1, max_length=800)]
    duration : Optional[conint(ge=1)] # in minutes
    intensity_level : Optional[conint(ge=1, le=10)] = None  
    mood_before :  Optional[List[Emotions]] = None
    mood_after :  Optional[List[Emotions]] = None
    notes : Optional[constr(min_length=1, max_length=1000)] = None   
   

class SleepEntry(BaseModel): 
    id :str = Field(default_factory=lambda: str(uuid4()))  
    timestamp: datetime 
    sleep_duration : Optional[conint(ge=1, le=10)] = None   
    quality :  Optional[conint(ge=1, le=10)] = None  
    sleep_environment : Optional[List[SleepEnv]] = None
    notes : Optional[constr(min_length=1, max_length=1000)] = None   

class SleepEntryCreate(BaseModel): 
    timestamp: datetime 
    sleep_duration : Optional[conint(ge=1, le=10)] = None   
    quality :  Optional[conint(ge=1, le=10)] = None  
    sleep_environment : Optional[List[SleepEnv]] = None
    notes : Optional[constr(min_length=1, max_length=1000)] = None  

class SleepEntryUpdate(BaseModel): 
    timestamp: Optional[datetime] = None 
    sleep_duration : Optional[conint(ge=1, le=10)] = None   
    quality :  Optional[conint(ge=1, le=10)] = None  
    sleep_environment : Optional[List[SleepEnv]] = None
    notes : Optional[constr(min_length=1, max_length=1000)] = None  


class MoodEntry(BaseModel): 
    id :str = Field(default_factory=lambda: str(uuid4()))  
    timestamp: datetime 
    mood : List[Emotions] # e.g., happy, sad, anxious
    intensity :  Optional[conint(ge=1, le=10)] = None   # 1-10 scale
    triggers :  Optional[constr(min_length=1, max_length=1000)] = None  # e.g., events, people
    coping_strategies :  Optional[constr(min_length=1, max_length=5000)] = None # e.g., meditation, exercise
    notes : Optional[constr(min_length=1, max_length=1000)] = None 


class MoodEntryCreate(BaseModel): 
    timestamp: datetime 
    mood : List[Emotions] # e.g., happy, sad, anxious
    intensity :  Optional[conint(ge=1, le=10)] = None   # 1-10 scale
    triggers :  Optional[constr(min_length=1, max_length=1000)] = None  # e.g., events, people
    coping_strategies :  Optional[constr(min_length=1, max_length=5000)] = None # e.g., meditation, exercise
    notes : Optional[constr(min_length=1, max_length=1000)] = None 

class MoodEntryUpdate(BaseModel): 
    timestamp: Optional[datetime] = None
    mood : Optional[List[Emotions]] # e.g., happy, sad, anxious
    intensity :  Optional[conint(ge=1, le=10)] = None   # 1-10 scale
    triggers :  Optional[constr(min_length=1, max_length=1000)] = None  # e.g., events, people
    coping_strategies :  Optional[constr(min_length=1, max_length=5000)] = None # e.g., meditation, exercise
    notes : Optional[constr(min_length=1, max_length=1000)] = None 


class JournalEntry(BaseModel): 
    id :str = Field(default_factory=lambda: str(uuid4()))  
    timestamp: datetime 
    title : constr(min_length=1, max_length=1000)
    content : constr(min_length=1, max_length=10000) 
    tags : Optional[list[str]] = None  # e.g., personal, work, relationships
    notes : Optional[constr(min_length=1, max_length=1000)] = None 

class JournalEntryCreate(BaseModel): 
    timestamp: datetime 
    title : constr(min_length=1, max_length=1000)
    content : constr(min_length=1, max_length=10000) 
    tags : Optional[list[str]] = None  # e.g., personal, work, relationships
    notes : Optional[constr(min_length=1, max_length=1000)] = None 

class JournalEntryUpdate(BaseModel): 
    timestamp: Optional[datetime] = None
    title : Optional[constr(min_length=1, max_length=1000)]
    content : Optional[constr(min_length=1, max_length=10000)]
    tags : Optional[list[str]] = None  # e.g., personal, work, relationships
    notes : Optional[constr(min_length=1, max_length=1000)] = None 



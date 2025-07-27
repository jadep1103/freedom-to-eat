from pydantic import BaseModel, EmailStr
from uuid import UUID

#Ce que l'utilisateur envoie lorsqu'il s'inscrit 
class UserCreate(BaseModel): 
    username: str
    email: EmailStr
    password: str

#Quand il se connecte
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Pour éviter les return user (confirmation d'inscription etc...)
class UserOut(BaseModel): 
    id : UUID
    username : str
    email : EmailStr
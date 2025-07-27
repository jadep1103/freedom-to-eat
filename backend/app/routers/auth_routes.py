from fastapi import APIRouter, HTTPException, Depends 
from db.database import get_db
from sqlalchemy.orm import Session
from schema.user_entry import UserCreate, UserOut, UserLogin
from models.user import User 
from utils.auth import hash_password, verify_password, generate_access_token

# Create a new router for user authentification 
router = APIRouter(prefix = "/auth", tags=["auth"])

#Sign-up
@router.post("/signup")
def signup(user : UserCreate, db : Session = Depends(get_db)):
    # Check if existing user 
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user: 
        raise HTTPException(status_code = 400, detail="Email already registered, please login")
    h_psw = hash_password(user.password)
    new_user = User( email = user.email, hashed_password = h_psw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message" : "User created successfully, user_id : {new_user.id}"}

#Login
@router.post("/login")
def login(user : UserLogin, db : Session = Depends(get_db)): 
    # Check if account exists 
    db_user = db.query(User).filter(User.email == user.email).first()
    correct_password = verify_password(user.password, db_user.hashed_password)
    if not db_user or not correct_password: 
        raise HTTPException(status_code = 401, detail = "Invalid email or password")
    
    token = generate_access_token({"sub": db_user.email})#Generate access token
    return {"access_token" : token, "token_type" : "bearer"}

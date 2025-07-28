from passlib.context import CryptContext 
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from db.database import get_db
from fastapi import HTTPException, Depends, status 
from models.user import User 
from sqlalchemy.orm import  Session 
from config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordBearer

# Hash context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Hash passwords 
def hash_password(password : str): 
    return pwd_context.hash(password)

# Verify password 
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Generate a token (jwt)
def generate_access_token(data : dict):

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire}) #Add expiration date

    encoded_token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_token

# Get current user 
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User: 
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )
    try: 
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None: 
            raise credentials_exception
    except JWTError: 
        raise credentials_exception 
    user = db.query(User).filter(User.id == user_id).first()
    if user is None: 
        raise credentials_exception
    return user 

    

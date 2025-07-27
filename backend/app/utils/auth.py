from passlib.context import CryptContext 
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES

# Hash context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

    encoded_token = jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)

    return encoded_token


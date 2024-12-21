from datetime import datetime, timedelta
from fastapi import HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from utils.config import config

SECRET_KEY = config.jwt_secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    '''Function to hash passwords'''
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    '''Function to verify passwords'''
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    '''Function to create JWT token'''
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    '''Function to verify JWT token'''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError as e:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,"Token has expired") from e
    except jwt.JWTError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND,"Invalid token") from e

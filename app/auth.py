# System Imports
from typing import Annotated

# Libs Imports
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import hashlib

# Local Imports
from model.models import User


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

JWT_KEY = "cW1nT8kIC7L8ZnijSHckA2c8f4TgN0DQcI6utcVgZJUdyFv0v0Bek8hxSKESeQV0zjMaK56x2CrzrMuyQBVB7lZ3NiSdvuxJTu18YD55nIBQLRIklzaiYT24iDGJihxvqnsZsmuwJaRFpygLBoRTaa5kVp9eQdmSBWwQ3SooRWTwsWaZDm9CVm3yb3P3X4IAlaAJwT4k"


def hash_password(password: str):
    return hashlib.sha256(f'{password}'.encode('utf-8')).hexdigest()


async def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        decoded = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
    except JWTError:
        return credentials_exception
    return decoded

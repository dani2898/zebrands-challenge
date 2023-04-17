import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']  # 30 minutes
ALGORITHM = os.environ['ALGORITHM']
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']     

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt
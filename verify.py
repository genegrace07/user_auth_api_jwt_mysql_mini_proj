from auth import SECRET_KEY,ALGORITHM
from fastapi import HTTPException,status
from jose import jwt

def verify_token(token:str):
    try:
        decode_token=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decode_token
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Token invalid or expired')
from auth import SECRET_KEY,ALGORITHM
from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

oauth_scheme = OAuth2PasswordBearer(tokenUrl='user/login')
def verify_token(token):
    #print(token)
    try:
        decode_token=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decode_token
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=str(e))
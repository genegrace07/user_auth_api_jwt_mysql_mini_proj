from fastapi import FastAPI,HTTPException,status,Depends
from auth import router as user_router
from jose import jwt
from auth import SECRET_KEY,ALGORITHM,bearer_scheme
from fastapi.security import OAuth2PasswordBearer
from auth import login_post

app=FastAPI()
app.include_router(user_router)

def verify_token(token:str):
    try:
        decode_token=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decode_token
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Token invalid or expired')
@app.get('/protected')
async def protected(bearer=Depends(bearer_scheme)):
    if bearer:
        user=verify_token(bearer)
        return {'access_token':bearer,'token_payload':user,'token_type':'bearer'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid login')
##to be continue: verify and protected,get token manually and automatically by login bearer
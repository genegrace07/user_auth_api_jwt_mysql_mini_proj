from fastapi import FastAPI,HTTPException,status,Depends
from auth import router as user_router
from action import router as action_router
from jose import jwt
from auth import SECRET_KEY,ALGORITHM,bearer_scheme
from fastapi.security import OAuth2PasswordBearer
from auth import login_post
from verify import verify_token

app=FastAPI()
app.include_router(user_router)
app.include_router(action_router)

@app.get('/protected')
async def protected(bearer=Depends(bearer_scheme)):
    if bearer:
        user=verify_token(bearer)
        return {'access_token':bearer,'token_payload':user,'token_type':'bearer'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid login')

##to be continue: get token manually and automatically by login bearer
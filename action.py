from fastapi import APIRouter,Depends,HTTPException,status
from auth import bearer_scheme
from verify import verify_token
from fastapi.security import OAuth2PasswordRequestForm,HTTPBearer
from dependency import depend_verify
from jose import jwt
from passlib.context import CryptContext

router = APIRouter(prefix="/user",tags=["User"])
pwd_context = CryptContext(schemes=['sha256_crypt'],deprecated='auto')

@router.get('/me')
async def get_me(get_bearer=Depends(bearer_scheme)):
    if get_bearer:
        user=verify_token(get_bearer)
        return {'access_token':get_bearer,'user':user}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid token or expired')

@router.post('/oauth_scheme')
async def oauth_scheme(form_data=Depends(OAuth2PasswordRequestForm),verify_user=Depends(depend_verify)):
    username=form_data.username
    password=form_data.password
    credentials=verify_user.login(username)

    if len(credentials) == 0:
        return {'message':'Invalid login'}
    u_name,pwd=credentials[0]
    verify_pwd=pwd_context.verify(password,pwd)
    if not verify_pwd:
        return {'message':'Password invalid'}



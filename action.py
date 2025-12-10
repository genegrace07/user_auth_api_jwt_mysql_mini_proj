from fastapi import APIRouter,Depends,HTTPException,status
from auth import bearer_scheme
from verify import verify_token
from fastapi.security import OAuth2PasswordRequestForm,HTTPBearer,OAuth2PasswordBearer
from dependency import depend_verify
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter(prefix="/user",tags=["User"])
pwd_context = CryptContext(schemes=['sha256_crypt'],deprecated='auto')
SECRET_KEY = 'mysecretkey'
ALGORITHM = 'HS256'
exp_time=15
oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/oauth_login')

@router.get('/me')
async def get_me(get_bearer=Depends(bearer_scheme)):
    if get_bearer:
        user=verify_token(get_bearer)
        return {'access_token':get_bearer,'user':user}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid token or expired')

@router.post('/oauth_login')
async def oauth_login(form_data=Depends(OAuth2PasswordRequestForm),verify_user=Depends(depend_verify)):
    username=form_data.username
    password=form_data.password
    credentials=verify_user.select_all(username)

    if len(credentials) == 0:
        return {'message':'Invalid login'}
    u_id,u_name,pwd,created=credentials[0]
    verify_pwd=pwd_context.verify(password,pwd)
    if not verify_pwd:
        return {'message':'Password invalid'}

    exp = datetime.utcnow() + timedelta(minutes=exp_time)
    for_payload = {'id':u_id,'username':u_name,'exp':exp.timestamp()}
    token=jwt.encode(for_payload,SECRET_KEY,algorithm=ALGORITHM)
    return {'access_token':token,'token_type':'bearer','user':{'id':u_id,'username':u_name}}



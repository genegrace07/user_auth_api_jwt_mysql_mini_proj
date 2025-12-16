from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from verify import verify_token,oauth_scheme
from dependency import depend_verify
from dependency import depend_users
from passlib.context import CryptContext

router = APIRouter(prefix='/user',tags=['user'])
pwd_context=CryptContext(schemes=['sha256_crypt'],deprecated='auto')

@router.get('/view_users')
async def view_users(get_token=Depends(oauth_scheme),get_users=Depends(depend_verify)):
    if get_token:
        result=get_users.all_users()
        return result
@router.post('/change_password')
async def change_password(password:str,token=Depends(oauth_scheme),get_userdb=Depends(depend_users)):
    if token:
        user=verify_token(token)
        #print(user)
        hash_password=pwd_context.hash(password)
        get_userdb.update_password(hash_password,user['username'])
        return {'message':'password updated'}








from fastapi import APIRouter,Depends,HTTPException
from passlib.context import CryptContext
from maindb import Users
from dependency import depend_users,depend_verify
from passlib.hash import sha256_crypt
from jose import

router = APIRouter(prefix='/user',tags=['User'])
pwd_context = CryptContext(schemes=['sha256_crypt'],deprecated='auto')

@router.post('/signup')
async def signup_post(username:str,password:str,sign_service=Depends(depend_users),verify_service=Depends(depend_verify)):
    if verify_service.check_username(username):
        return f'{username} already exist'

    pwd_hash=pwd_context.hash(password)
    sign_service.signup(username,pwd_hash)
    return f'{username} successfully added'
@router.post('/login')
async def login_post(username:str,password:str,login_service=Depends(depend_users)):
    check_login=login_service.login(username)
    if len(check_login) == 0:
        raise HTTPException(status_code=400,detail='Login failed, username not found')

    hash_pwd=check_login[0][1]
    #print(hash_pwd) ##check hashed password
    check_pwd=pwd_context.verify(password,hash_pwd)
    if not check_pwd:
        return HTTPException(status_code=400,detail='Invalid password')
    return 'Login successfully'






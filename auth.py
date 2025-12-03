from fastapi import APIRouter,Depends
from passlib.context import CryptContext
from maindb import Users
from dependency import depend_users,depend_verify
from passlib.hash import sha256_crypt

router = APIRouter(prefix='/user',tags=['User'])
pwd_context = CryptContext(schemes=['sha256_crypt'],deprecated='auto')

@router.post('/signup')
async def signup_post(username:str,password:str,sign_service=Depends(depend_users),verify_service=Depends(depend_verify)):
    if verify_service.check_username(username):
        return f'{username} already exist'

    pwd_hash=pwd_context.hash(password)
    sign_service.signup(username,pwd_hash)
    return f'{username} successfully added'

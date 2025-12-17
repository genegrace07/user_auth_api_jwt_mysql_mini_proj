from fastapi import APIRouter,Depends,HTTPException,status
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
@router.post('/delete_user')
async def delete_user(user_id:int,token=Depends(oauth_scheme),login_service=Depends(depend_users),delete_service=Depends(depend_users)):
    verified_token=verify_token(token)
    #print(verified_token)
    u_name=verified_token['username']
    if u_name == 'jinbei':
        delete_service.delete_user(user_id)
        return {'message':'user deleted successfully'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Not authorized')








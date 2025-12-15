from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from verify import verify_token,oauth_scheme
from dependency import depend_verify

router = APIRouter(prefix='/user',tags=['user'])

@router.get('/view_users')
async def view_users(get_token=Depends(oauth_scheme),get_users=Depends(depend_verify)):
    if get_token:
        result=get_users.all_users()
        return result








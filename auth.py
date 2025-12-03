from fastapi import APIRouter,Depends
from dependencies import get_user_service

router=APIRouter(prefix='/signup',tags=['user'])

@router.post('/signup')
async def signup(username:str,password:str,user_service=Depends(get_user_service)):
    result = user_service.signup(username, password)
    return result
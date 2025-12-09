from fastapi import APIRouter,Depends,HTTPException,status
from auth import bearer_scheme
from verify import verify_token

router = APIRouter(prefix="/user",tags=["User"])

@router.get('/me')
async def get_me(get_bearer=Depends(bearer_scheme)):
    if get_bearer:
        user=verify_token(get_bearer)
        return {'access_token':get_bearer,'user':user}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid token or expired')



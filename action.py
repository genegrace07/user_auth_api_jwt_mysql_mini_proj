# from fastapi import APIRouter,Depends,HTTPException,status
# from verify import verify_token
# from fastapi.security import OAuth2PasswordRequestForm,HTTPBearer,OAuth2PasswordBearer
# from dependency import depend_verify
# from jose import jwt
# from passlib.context import CryptContext
# from datetime import datetime, timedelta

# @router.get('/me')
# async def get_me(get_bearer=Depends(bearer_scheme)):
#     if get_bearer:
#         user=verify_token(get_bearer)
#         return {'access_token':get_bearer,'user':user}
#     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid token or expired')




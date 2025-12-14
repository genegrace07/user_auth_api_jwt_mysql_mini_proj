from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from passlib.context import CryptContext
from dependency import depend_users,depend_verify
from jose import jwt
from datetime import datetime,timedelta

router = APIRouter(prefix='/user',tags=['User'])
pwd_context = CryptContext(schemes=['sha256_crypt'],deprecated='auto')
exp_time = 60
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
@router.post('/signup')
async def signup_post(username:str,password:str,sign_service=Depends(depend_users),verify_service=Depends(depend_verify)):
    if verify_service.check_username(username):
        return f'{username} already exist'

    pwd_hash=pwd_context.hash(password)
    sign_service.signup(username,pwd_hash)
    return f'{username} successfully added'
@router.get('/signup')
async def signup_get():
    return {"message": "Signup endpoint"}


@router.post('/login')
async def login_post(form:OAuth2PasswordRequestForm=Depends(),verify_user=Depends(depend_verify)):
    username=form.username
    password=form.password
    credentials=verify_user.select_all(username)

    if len(credentials) == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid login')
    u_id,u_name,pwd,created=credentials[0]
    verify_pwd=pwd_context.verify(password,pwd)
    if not verify_pwd:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid password')

    exp = datetime.utcnow() + timedelta(minutes=exp_time)
    for_payload = {'id':u_id,'username':u_name,'exp':exp}
    token=jwt.encode(for_payload,SECRET_KEY,algorithm=ALGORITHM)
    return {'access_token':token,'token_type':'bearer','user':{'id':u_id,'username':u_name}}

##NORMAL LOGIN BACKUP
# @router.post('/login')
# async def login_post(username:str,password:str,login_service=Depends(depend_users),users_info=Depends(depend_verify)):
#     check_login=login_service.login(username)
#     if len(check_login) == 0:
#         raise HTTPException(status_code=400,detail='Login failed, username not found')
#
#     hash_pwd=check_login[0][1]
#     #print(hash_pwd) ##check hashed password
#     check_pwd=pwd_context.verify(password,hash_pwd)
#     if not check_pwd:
#         return HTTPException(status_code=400,detail='Invalid password')
#
#     users_details=users_info.select_all()
#     user_id=users_details[0][0]
#     user_username = users_details[0][1]
#     exp=datetime.utcnow() + timedelta(minutes=exp_time)
#     for_payload={"id":user_id,"user":user_username,"exp":exp}
#     token=jwt.encode(for_payload,SECRET_KEY,algorithm=ALGORITHM)
#     return {'access_token':token,'token_type':'bearer','user':check_login}

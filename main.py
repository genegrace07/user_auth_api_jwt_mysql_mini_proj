from fastapi import FastAPI,Depends
from auth import router as auth_router
from verify import verify_token
from verify import oauth_scheme

app=FastAPI()
app.include_router(auth_router)
@app.get('/protected')
async def protected(oath_bearer=Depends(oauth_scheme)):
    if oath_bearer:
        user=verify_token(oath_bearer)
        return {'access_token':oath_bearer,'token_payload':user,'token_type':'bearer'}


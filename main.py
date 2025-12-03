from fastapi import FastAPI
from auth import router as user_router

app=FastAPI()
app.include_router(user_router)
def verify():
    pass


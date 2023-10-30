from fastapi import FastAPI
from auth.router import auth_router

app = FastAPI()
app.include_router(auth_router)

@app.get('/hello')
async def hello() -> str:
    return "Hello world!"

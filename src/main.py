from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
async def hello() -> str:
    return "Hello world!"

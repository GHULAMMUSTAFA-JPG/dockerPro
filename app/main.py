from fastapi import FastAPI

app : FastAPI = FastAPI()



@app.get("/")
async def home():
    return "hello jan so gai ho"
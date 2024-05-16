from fastapi import FastAPI

app : FastAPI = FastAPI()



@app.get("/")
async def home():
    return {"Message":"hello jan so gai ho"}
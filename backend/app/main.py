from fastapi import FastAPI
from routers import food

app = FastAPI(title = "Freedom to Eat API")

@app.get("/")
async def root(): 
    return {"message" : "Welcome to the Freedom to Eat API!"}

app.include_router(food.router)
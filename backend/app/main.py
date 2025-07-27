from fastapi import FastAPI
from routers import food, auth_routes

app = FastAPI(title = "Freedom to Eat API")

@app.get("/")
async def root(): 
    return {"message" : "Welcome to the Freedom to Eat API!"}

app.include_router(food.router)
app.include_router(auth_routes.rooter)
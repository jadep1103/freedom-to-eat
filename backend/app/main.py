from fastapi import FastAPI
from routers import food, auth_routes

app = FastAPI(
    title="Freedom to Eat API",
    description="API de journal alimentaire",
    version="1.0",
    swagger_ui_init_oauth={
        "clientId": "swagger-ui",  # optionnel, peut être vide
        "scopes": {},              # pas de scopes ici
        "usePkceWithAuthorizationCodeGrant": False
    }
)


@app.get("/")
async def root(): 
    return {"message" : "Welcome to the Freedom to Eat API!"}

app.include_router(food.router)
app.include_router(auth_routes.router)
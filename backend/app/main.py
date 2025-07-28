from fastapi import FastAPI
from routers import food, auth_routes, upload
from services.image_storage import save_image_locally
from fastapi.staticfiles import StaticFiles

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
app.include_router(upload.router)
app.mount("/images", StaticFiles(directory="uploaded_images"), name="images")
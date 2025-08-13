from fastapi import FastAPI
from routers import food, auth_routes, upload
from services.image_storage import save_image_locally
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



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

# MIDDLEWARE

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(): 
    return {"message" : "Welcome to the Freedom to Eat API!"}

app.include_router(food.router)
app.include_router(auth_routes.router)
app.include_router(upload.router)

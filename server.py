from fastapi import FastAPI
from app.routers import generate

app = FastAPI()

app.include_router(generate.router)

from fastapi import FastAPI

from api.v1.routes import api_v1_router

app = FastAPI(title="Empta")

app.include_router(api_v1_router, prefix="/api/v1")


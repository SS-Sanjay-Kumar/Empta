from fastapi import APIRouter

from .endpoints import health, crud

api_v1_router = APIRouter()

api_v1_router.include_router(
    health.healthRouter,
    prefix="/health",
    tags=["Health"]
)

api_v1_router.include_router(
    crud.crudRouter,
    prefix="/crud",
    tags=["CRUD"]
)

from fastapi import APIRouter

from .endpoints.product_routes import product_router

api_v1_router = APIRouter()

api_v1_router.include_router(
    product_router,
    prefix="/product",
    tags=["Product"]
)

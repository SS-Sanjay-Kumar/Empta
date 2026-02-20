from fastapi import APIRouter, HTTPException, status

product_router = APIRouter()

@product_router.get("/health", status_code=status.HTTP_200_OK)
def check_health():
    return {"status", "ok"}
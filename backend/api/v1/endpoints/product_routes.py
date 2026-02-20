from fastapi import APIRouter, HTTPException, status

from backend.models.product_models import ProductCreate, ProductCreateResponse
from backend.lib.database import SessionLocal

product_router = APIRouter()

@product_router.get("/health", status_code=status.HTTP_200_OK)
def check_health():
    return {"status", "ok"}

# add new products to the store
@product_router.post("/add", status_code=status.HTTP_201_CREATED, response_model = ProductCreateResponse)
def add_new_products(product: ProductCreate):
    try:
        db_session = SessionLocal()
        db_session.add(product)
        db_session.commit()
        db_session.refresh()

        return db_session
    except:
        raise HTTPException
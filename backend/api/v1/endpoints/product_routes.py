from fastapi import APIRouter, HTTPException, status

from models.product_models import ProductCreate, ProductCreateResponse
from lib.database import SessionLocal
from schemas.product_schemas import Product
product_router = APIRouter()

@product_router.get("/health", status_code=status.HTTP_200_OK)
def check_health():
    return {"status", "ok"}

# add new products to the store
@product_router.post("/add", status_code=status.HTTP_201_CREATED, response_model = ProductCreateResponse)
def add_new_products(product: ProductCreate):
    try:
        db_session = SessionLocal()
        db_product = Product(**product.dict())
        db_session.add(db_product)
        db_session.commit()
        db_session.refresh(db_product)
        db_session.close()
        
        return db_product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))
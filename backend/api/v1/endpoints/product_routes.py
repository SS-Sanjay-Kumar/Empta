from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


from schemas.product_schemas import ProductCreate, ProductCreateResponse
from models.product_models import Product
from lib.database import SessionLocal

product_router = APIRouter()

@product_router.get("/health", status_code=status.HTTP_200_OK)
def check_health():
    return {"status", "ok"}

# add new products to the store
@product_router.post(
        "/add",
        status_code=status.HTTP_201_CREATED,
        response_model = ProductCreateResponse
)
def add_new_products(product: ProductCreate):
    db: Session = SessionLocal()
    try:
        db = SessionLocal()
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product
    
    except SQLAlchemyError as sqla_e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= f"Error with SQLAlchemy: {sqla_e}")
    finally:
        db.close()

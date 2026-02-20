from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from schemas.product_schemas import ProductCreate, ProductCreateResponse
from models.product_models import Product
from lib.database import get_db

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
def add_new_products(
    product: ProductCreate, 
    db: Session = Depends(get_db)
):
    try:
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product
    
    except SQLAlchemyError as sqla_e:
        db.rollback()
        print("Error in add_new_products: ", sqla_e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Error with SQLAlchemy")

@product_router.get(
        "/get-product/{product_id}",
        status_code=status.HTTP_200_OK, 
        response_model=ProductCreateResponse
)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    try:
        product = db.get(Product, product_id)

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID does not exist")

        return product
        
    except SQLAlchemyError as sqla_e:
        print("Error in add_new_products: ", sqla_e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Error with SQLAlchemy")


@product_router.get(
    "/get-all-products",
    status_code=status.HTTP_200_OK
)
def get_all_products(db:Session = Depends(get_db)):
    try:
        stmt = select(Product)

        products = db.execute(stmt).scalars().all()

        return products
    
    except SQLAlchemyError as sqla_e:
        print("Error in add_new_products: ", sqla_e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Error with SQLAlchemy")

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


from models.crud import Product
from schemas.crud import ProductCreate, ProductResponse

load_dotenv()


engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(bind = engine)

crudRouter = APIRouter()

@crudRouter.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):
    db = SessionLocal()

    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    db.close()
    return db_product

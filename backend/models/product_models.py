from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    product_name = Column(String(100), nullable=False)
    product_type = Column(String(100), nullable=False)
    manufactured_by = Column(String(100), nullable=False)
    product_price = Column(Numeric(10, 2), nullable=False)
    product_stock = Column(Integer, nullable=False)
    product_reviews = Column(Numeric(2, 1), nullable=False)
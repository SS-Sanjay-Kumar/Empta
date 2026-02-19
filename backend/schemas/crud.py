from pydantic import BaseModel

class ProductCreate(BaseModel):
    product_name: str
    product_price: float
    product_quantity: int
    manufactured_by: str
    product_reviews: float

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, condecimal, conint

class ProductCreate(BaseModel):
    # id is generated in db
    product_name: str
    product_type: str
    manufactured_by: str
    product_price: condecimal(max_digits=10, decimal_places=2)
    product_stock: conint(ge=0)
    product_reviews: condecimal(ge=1, le=5, decimal_places=1)

class ProductCreateResponse(ProductCreate):
    id: int

    class Config:
        orm_mode: True 
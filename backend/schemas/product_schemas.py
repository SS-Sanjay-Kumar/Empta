from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from decimal import Decimal

class ProductCreate(BaseModel):
    # id is generated in db
    product_name: str
    product_type: str
    manufactured_by: str
    product_description : Optional[str] = None
    product_price: Decimal = Field(..., max_digits=10, decimal_places=2)
    product_stock: int = Field(...,ge=0)
    product_reviews: Decimal = Field(..., ge=1, le=5, decimal_places=1)

class ProductCreateResponse(ProductCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
    
class ProductUpdate(BaseModel):
    # Use Field() for constraints in Pydantic V2
    product_name: Optional[str] = None
    product_type: Optional[str] = None
    manufactured_by: Optional[str] = None
    product_description: Optional[str] = None
    
    product_price: Optional[Decimal] = Field(None, max_digits=10, decimal_places=2)
    product_stock: Optional[int] = Field(None, ge=0)
    product_reviews: Optional[Decimal] = Field(None, ge=1, le=5, decimal_places=1)

    # This replaces 'class Config' and 'orm_mode'
    model_config = ConfigDict(from_attributes=True)
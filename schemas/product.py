# backend/schemas/product.py
from pydantic import BaseModel

class ProductOut(BaseModel):
    code: str
    name: str
    price_tax_included: int

    class Config:
        from_attributes = True
        orm_mode = True
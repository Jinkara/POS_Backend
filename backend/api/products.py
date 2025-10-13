# backend/api/products.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crud.products import get_by_code
from schemas.product import ProductOut

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/{code}", response_model=ProductOut)
def get_product(code: str, db: Session = Depends(get_db)):
    p = get_by_code(db, code)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductOut.from_orm(p)
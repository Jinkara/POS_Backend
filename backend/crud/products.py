# backend/crud/products.py
from sqlalchemy.orm import Session
from db.models import Product

def get_by_code(db: Session, code: str) -> Product | None:
    return db.query(Product).filter(Product.code == code).first()

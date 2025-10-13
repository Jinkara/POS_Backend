# backend/main.py
from fastapi import FastAPI
from db.session import Base, engine

Base.metadata.create_all(bind=engine)

from api.products import router as products_router
from api.purchases import router as purchases_router

app = FastAPI(title="POS API")

# ルーター登録
app.include_router(products_router)
app.include_router(purchases_router)

@app.get("/")
def root():
    return {"ok": True}

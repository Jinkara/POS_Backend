# backend/schemas/purchase.py
from pydantic import BaseModel, Field
# from typing import List

class PurchaseItem(BaseModel):
    code: str
    quantity: int = Field(ge=1)

class PurchaseRequest(BaseModel):
    empCd: str
    storeCd: str
    posNo: str
    items: list[PurchaseItem]

class PurchaseResult(BaseModel):
    success: bool
    totalTaxIncluded: int
    totalExTax: int
    tradeId: int

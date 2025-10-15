# backend/api/purchases.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from crud.trades import create_trade_with_details
from schemas.purchase import PurchaseRequest, PurchaseResult

router = APIRouter(prefix="/purchases", tags=["purchases"])

@router.post("", response_model=PurchaseResult)
def purchase(payload: PurchaseRequest, db: Session = Depends(get_db)):
    trade = create_trade_with_details(
        db,
        emp_cd=payload.empCd or "9999999999",
        store_cd=payload.storeCd or "30",
        pos_no=payload.posNo or "90",
        items=[(it.code, it.quantity) for it in payload.items],
    )
    return {
        "success": True,
        "totalTaxIncluded": trade.total_amt,
        "totalExTax": trade.total_amt_ex_tax,
        "tradeId": trade.id,
    }

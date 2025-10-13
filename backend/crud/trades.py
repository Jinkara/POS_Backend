# backend/crud/trades.py
from sqlalchemy.orm import Session
from db.models import Trade, TradeDetail, Product

def create_trade_with_details(
    db: Session,
    emp_cd: str,
    store_cd: str,
    pos_no: str,
    items: list[tuple[str, int]],  # (code, quantity)
):
    # 商品を一括取得
    codes = [c for c, _ in items]
    products = {p.code: p for p in db.query(Product).filter(Product.code.in_(codes)).all()}

    # 合計計算
    total = 0
    details: list[TradeDetail] = []
    for code, qty in items:
        p = products.get(code)
        if not p:
            # 見つからない商品はスキップ（MVP）
            continue
        line = p.price_tax_included * qty
        total += line
        details.append(
            TradeDetail(
                prod_code=p.code,
                prod_name=p.name,
                prod_price=p.price_tax_included,
                quantity=qty,
            )
        )

    trade = Trade(emp_cd=emp_cd, store_cd=store_cd, pos_no=pos_no,
                  total_amt=total, total_amt_ex_tax=0)
    trade.details = details
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return trade

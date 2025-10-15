# backend/db/models.py
from sqlalchemy import Column, Integer, String, CHAR, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from db.session import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(25), unique=True, nullable=False)       # JAN
    name = Column(String(100), nullable=False)
    price_tax_included = Column(Integer, nullable=False)

class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    emp_cd  = Column(CHAR(10), nullable=False)
    store_cd = Column(CHAR(5), nullable=False)
    pos_no  = Column(CHAR(3), nullable=False)
    total_amt = Column(Integer, nullable=False, default=0)        # 税込
    total_amt_ex_tax = Column(Integer, nullable=False, default=0) # 税抜（MVPでは0でもOK）
    details = relationship("TradeDetail", back_populates="trade", cascade="all, delete-orphan")

class TradeDetail(Base):
    __tablename__ = "trade_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    trade_id = Column(Integer, ForeignKey("trades.id"), nullable=False)
    prod_code  = Column(String(25), nullable=False)
    prod_name  = Column(String(100), nullable=False)
    prod_price = Column(Integer, nullable=False)
    quantity   = Column(Integer, nullable=False, default=1)
    trade = relationship("Trade", back_populates="details")

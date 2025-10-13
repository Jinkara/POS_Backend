# backend/db/session.py
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base, Session

load_dotenv()

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_NAME = os.getenv("MYSQL_DB")
SSL_ENABLED = os.getenv("MYSQL_SSL", "false").lower() == "true"
SSL_CA_PATH = os.getenv("MYSQL_SSL_CA")

# mysql+pymysql で安全にURLを構築
database_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME,
    query={"charset": "utf8mb4"}
)

# SSL対応
connect_args = {}
if SSL_ENABLED and SSL_CA_PATH:
    ca_abs = str(Path(SSL_CA_PATH).resolve())
    if not Path(ca_abs).is_file():
        raise FileNotFoundError(f"❌ SSL CA file not found: {ca_abs}")
    connect_args = {
        "ssl_ca": ca_abs
    }


engine = create_engine(
    database_url,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=1800,
    connect_args=connect_args
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=Session)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

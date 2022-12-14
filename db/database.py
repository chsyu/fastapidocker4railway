from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./shopping-cart.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:IVkhNKmf8CHe1Kgf2RRY@containers-us-west-118.railway.app:7181/railway"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
) 

# engine = create_engine(SQLALCHEMY_DATABASE_URL) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
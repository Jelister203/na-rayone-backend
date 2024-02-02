from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


"""
Вот это - полный пиздец. Без этих строк, таблицы в бд не создаются.
"""

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:ebwerv@db:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from address_book.database import Base


class Address(Base):
    __tablename__ = "Address"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

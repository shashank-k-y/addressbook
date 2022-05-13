from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateAddressbyAddress(BaseModel):
    address: str


class Address(BaseModel):
    id: Optional[int] = None
    address: str
    latitude: float
    longitude: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

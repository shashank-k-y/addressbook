from typing import Optional

from pydantic import BaseModel


class CreateAddressbyAddress(BaseModel):
    address: str


class Address(BaseModel):
    id: Optional[int] = None
    address: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True

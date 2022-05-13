from typing import List

from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    status
)
from sqlalchemy.orm import Session
from geopy.exc import GeocoderTimedOut

from . import models
from .database import SessionLocal, engine
from address_book.crud import (
    create_address,
    delete_address,
    get_address_by_id,
    get_all_address,
    update_address,
    get_address_by_co_ordinates
)

from .schemas import Address, CreateAddressbyAddress
from address_book.geopy_utils import get_location_co_ordinates

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
        # raise HTTPException(
        #     status_code=400, detail="Email already registered"
        # )
#     return crud.create_user(db=db, user=user)


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

@app.post(
    "/addressbook", response_model=Address, status_code=status.HTTP_201_CREATED
)
def create_address_in_address_book(
    request: CreateAddressbyAddress, db: Session = Depends(get_db)
):
    try:
        co_ordinates = get_location_co_ordinates(address=request.address)
    except GeocoderTimedOut:
        raise HTTPException(
            status_code=400, detail="geopy taking too long to respond."
        )

    if not co_ordinates:
        raise HTTPException(
            status_code=400, detail="geopy was not able to seacrh the address"
        )

    address_item = get_address_by_co_ordinates(
        db=db, co_ordinates=co_ordinates
    )
    if address_item:
        raise HTTPException(
            status_code=400, detail="Address already exists"
        )

    return create_address(
        db=db, co_ordinates=co_ordinates, address=request.address
    )


@app.get(
    "/addressbook", response_model=List[Address],
    status_code=status.HTTP_200_OK
)
def get_all_addresses(db: Session = Depends(get_db)):
    return get_all_address(db=db)


@app.get(
    "/addressbook/{address_id}", response_model=Address,
    status_code=status.HTTP_200_OK
)
def get_address(address_id: int, db: Session = Depends(get_db)):
    address_instance = get_address_by_id(db=db, address_id=address_id)
    if not address_instance:
        raise HTTPException(status_code=404, detail="address not found")

    return address_instance


@app.put(
    "/addressbook/{address_id}", response_model=Address,
    status_code=status.HTTP_200_OK
)
def update_address_by_id(
    address_id: int,
    address: Address,
    db: Session = Depends(get_db)
):
    address_instance_to_update = get_address_by_id(
        db=db, address_id=address_id
    )
    if not address_instance_to_update:
        raise HTTPException(
            status_code=404, detail="address not found for the given id"
        )

    return update_address(
        db=db, address_object=address_instance_to_update, address=address
    )


@app.delete(
    "/addressbook/{address_id}", status_code=status.HTTP_200_OK
)
def delete_address_from_addressbook(
    address_id: int, db: Session = Depends(get_db)
):
    address_instance = get_address_by_id(db=db, address_id=address_id)
    if not address_instance:
        raise HTTPException(status_code=404, detail="address not found")

    delete_address(db=db, address_object=address_instance)
    return "address deleted successfully!"

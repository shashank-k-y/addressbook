from sqlalchemy.orm import Session

from address_book.models import Address
from address_book import schemas


def insert_into_table(db: Session, model_object: object) -> None:
    db.add(model_object)
    db.commit()
    db.refresh(model_object)


def create_address(db: Session, co_ordinates: tuple, address: str):
    address_object = Address(
        address=address,
        latitude=co_ordinates[0],
        longitude=co_ordinates[1]
    )
    insert_into_table(db=db, model_object=address_object)
    return address_object


def get_all_address(db: Session):
    return db.query(Address).all()


def get_address_by_id(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()


def get_address_by_co_ordinates(db: Session, co_ordinates: tuple):
    return db.query(Address).filter(
        Address.latitude == co_ordinates[0],
        Address.longitude == co_ordinates[1]
    ).first()


def update_address(
    db: Session, address_object: object, address: schemas.Address
):
    address_object.address = address.address
    address_object.latitude = address.latitude
    address_object.longitude = address.longitude
    db.commit()
    db.refresh(address_object)
    return address_object


def delete_address(db: Session, address_object: object):
    db.delete(address_object)
    db.commit()

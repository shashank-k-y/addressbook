from sqlalchemy.orm import Session

from .models import Address


def insert_into_table(db: Session, model_object: object) -> None:
    db.add(model_object)
    db.commit()
    db.refresh(model_object)


def update_column(db: Session, model_object: object, data: dict) -> None:
    model_object.update(data)
    db.commit()


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


def update_address(db: Session, model_object: object, data: dict):
    update_column(db=db, model_object=model_object, data=data)
    db.refresh(model_object)
    return model_object

from sqlalchemy import (
    Column,
    String,
    Integer
)
from . import (
    SESSION,
    BASE
)


class moidata(BASE):
    __tablename__ = "keklyf"
    friday_id = Column(String(14), primary_key=True)

    def __init__(self, friday_id):
        self.friday_id = friday_id


moidata.__table__.create(checkfirst=True)

def add_usersid_in_db(friday_id: int):
    id_user = moidata(str(friday_id))
    SESSION.add(id_user)
    SESSION.commit()

def get_all_users():
    stark = SESSION.query(moidata).all()
    SESSION.close()
    return stark

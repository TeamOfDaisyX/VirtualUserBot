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
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


moidata.__table__.create(checkfirst=True)

def add_usersid_in_db(chat_id: int):
    id_user = moidata(str(chat_id))
    SESSION.add(id_user)
    SESSION.commit()

def get_all_users():
    stark = SESSION.query(moidata).all()
    SESSION.close()
    return stark

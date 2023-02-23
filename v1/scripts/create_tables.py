from ..model.users_model import Users

from ..utils.db import db

def create_tables():
    with db:
        db.create_tables([Users])
        print("TABLAS CREADAS!")
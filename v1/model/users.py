import peewee

from ..utils.db import db

class Users(peewee.Model):
    id = peewee.AutoField(unique=True, index=True)
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()

    class Meta:
        database = db
import peewee

from ..utils.db import db

class Country(peewee.Model):
    id = peewee.AutoField(unique=True, index=True)
    name = peewee.CharField()
    trial534 = peewee.CharField()

    class Meta:
        database = db
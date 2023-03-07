import peewee

from ..utils.db import db

class League(peewee.Model):
    id = peewee.AutoField(unique=True, index=True)
    country_id = peewee.IntegerField()
    name = peewee.CharField()
    trial534 = peewee.CharField()

    class Meta:
        database = db
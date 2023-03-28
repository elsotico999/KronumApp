import peewee

from ..utils.db import db

class Team(peewee.Model):
    id = peewee.AutoField(unique=True, index=True)
    team_api_id = peewee.IntegerField()
    team_fifa_api_id = peewee.IntegerField()
    team_long_name = peewee.CharField()
    team_short_name	 = peewee.CharField()

    class Meta:
        database = db
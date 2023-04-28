import peewee

from ..utils.db import db

class Team_attributes(peewee.Model):
    id = peewee.AutoField(unique=True, index=True)
    team_api_id = peewee.IntegerField()
    team_fifa_api_id = peewee.IntegerField()
    date = peewee.DateField()
    buildupplayspeed = peewee.IntegerField()
    buildupplayspeedclass = peewee.CharField()
    buildupplaydribbling = peewee.IntegerField()
    buildupplaydribblingclass = peewee.CharField()
    buildupplaypassing = peewee.IntegerField()
    buildupplaypassingclass = peewee.CharField()
    buildupplaypositioningclass = peewee.CharField()
    chancecreationpassing = peewee.IntegerField()
    chancecreationpassingclass = peewee.CharField()
    chancecreationcrossing = peewee.IntegerField()
    chancecreationcrossingclass = peewee.CharField()
    chancecreationshooting = peewee.IntegerField()
    chancecreationshootingclass = peewee.CharField()
    chancecreationpositioningclass = peewee.CharField()
    defencepressure = peewee.IntegerField()
    defencepressureclass = peewee.CharField()
    defenceaggression = peewee.IntegerField()
    defenceaggressionclass = peewee.CharField()
    defenceteamwidth = peewee.IntegerField()
    defenceteamwidthclass = peewee.CharField()
    defencedefenderlineclass = peewee.CharField()

    class Meta:
        database = db 
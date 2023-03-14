import peewee

from ..utils.db import db

class Match(peewee.Model):
    id = peewee.AnyField(unique=True, index=True)
    country_id = peewee.IntegerField()
    league_id = peewee.IntegerField()
    season = peewee.TextField()
    stage = peewee.IntegerField()
    date = peewee.TextField()
    match_api_id = peewee.IntegerField()
    home_team_api_id = peewee.IntegerField()
    away_team_api_id = peewee.IntegerField()
    home_team_goal = peewee.IntegerField()
    away_team_goal = peewee.IntegerField()
    home_player_x1 = peewee.IntegerField()
    home_player_x2 = peewee.IntegerField()
    home_player_x3 = peewee.IntegerField()
    home_player_x4 = peewee.IntegerField()
    home_player_x5 = peewee.IntegerField()
    home_player_x6 = peewee.IntegerField()
    home_player_x7 = peewee.IntegerField()
    home_player_x8 = peewee.IntegerField()
    home_player_x9 = peewee.IntegerField()
    home_player_x10 = peewee.IntegerField()
    home_player_x11 = peewee.IntegerField()
    away_player_x1 = peewee.IntegerField()
    away_player_x2 = peewee.IntegerField()
    away_player_x3 = peewee.IntegerField()
    away_player_x4 = peewee.IntegerField()
    away_player_x5 = peewee.IntegerField()
    away_player_x6 = peewee.IntegerField()
    away_player_x7 = peewee.IntegerField()
    away_player_x8 = peewee.IntegerField()
    away_player_x9 = peewee.IntegerField()
    away_player_x10 = peewee.IntegerField()
    away_player_x11 = peewee.IntegerField()
    home_player_y1 = peewee.IntegerField()
    home_player_y2 = peewee.IntegerField()
    home_player_y3 = peewee.IntegerField()
    home_player_y4 = peewee.IntegerField()
    home_player_y5 = peewee.IntegerField()
    home_player_y6 = peewee.IntegerField()
    home_player_y7 = peewee.IntegerField()
    home_player_y8 = peewee.IntegerField()
    home_player_y9 = peewee.IntegerField()
    home_player_y10 = peewee.IntegerField()
    home_player_y11 = peewee.IntegerField()
    away_player_y1 = peewee.IntegerField()
    away_player_y2 = peewee.IntegerField()
    away_player_y3 = peewee.IntegerField()
    away_player_y4 = peewee.IntegerField()
    away_player_y5 = peewee.IntegerField()
    away_player_y6 = peewee.IntegerField()
    away_player_y7 = peewee.IntegerField()
    away_player_y8 = peewee.IntegerField()
    away_player_y9 = peewee.IntegerField()
    away_player_y10 = peewee.IntegerField()
    away_player_y11 = peewee.IntegerField()
    home_player_1 = peewee.IntegerField()
    home_player_2 = peewee.IntegerField()
    home_player_3 = peewee.IntegerField()
    home_player_4 = peewee.IntegerField()
    home_player_5 = peewee.IntegerField()
    home_player_6 = peewee.IntegerField()
    home_player_7 = peewee.IntegerField()
    home_player_8 = peewee.IntegerField()
    home_player_9 = peewee.IntegerField()
    home_player_10 = peewee.IntegerField()
    home_player_11 = peewee.IntegerField()
    away_player_1 = peewee.IntegerField()
    away_player_2 = peewee.IntegerField()
    away_player_3 = peewee.IntegerField()
    away_player_4 = peewee.IntegerField()
    away_player_5 = peewee.IntegerField()
    away_player_6 = peewee.IntegerField()
    away_player_7 = peewee.IntegerField()
    away_player_8 = peewee.IntegerField()
    away_player_9 = peewee.IntegerField()
    away_player_10 = peewee.IntegerField()
    away_player_11 = peewee.IntegerField()
    goal = peewee.TextField()
    shoton = peewee.TextField()
    shotoff = peewee.TextField()
    foulcommit = peewee.TextField()
    card = peewee.TextField()
    cross = peewee.TextField()
    corner = peewee.TextField()
    possession = peewee.TextField()
    b365h = peewee.DoubleField()
    b365d = peewee.DoubleField()
    b365a = peewee.DoubleField()
    bwh = peewee.DoubleField()
    bwd = peewee.DoubleField()
    bwa = peewee.DoubleField()
    iwh = peewee.DoubleField()
    iwd = peewee.DoubleField()
    iwa = peewee.DoubleField()
    lbh = peewee.DoubleField()
    lbd = peewee.DoubleField()
    lba = peewee.DoubleField()
    psh = peewee.DoubleField()
    psd = peewee.DoubleField()
    psa = peewee.DoubleField()
    whh = peewee.DoubleField()
    whd = peewee.DoubleField()
    wha = peewee.DoubleField()
    sjh = peewee.DoubleField()
    sjd = peewee.DoubleField()
    sja = peewee.DoubleField()
    vch = peewee.DoubleField()
    vcd = peewee.DoubleField()
    vca = peewee.DoubleField()
    gbh = peewee.DoubleField()
    gbd = peewee.DoubleField()
    gba = peewee.DoubleField()
    bsh = peewee.DoubleField()
    bsd = peewee.DoubleField()
    bsa = peewee.DoubleField()

    class Meta:
        database = db
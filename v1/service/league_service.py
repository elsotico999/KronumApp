from fastapi import HTTPException, status

from ..schema import league_schema
from ..model.league_model import League

def get_leagues(id: int = None, name:str=None, country_id:int=None):
    list_leagues = []
    leagues = League.filter()

    for l in leagues:
        print(l.name)
        list_leagues.append(
            league_schema.League(id=str(l),name=l.name,id_country=str(l.country_id))
        )
    return list_leagues
    
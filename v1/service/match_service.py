from fastapi import HTTPException, status

from ..schema import match_schema
from ..model.match_model import Match

def get_matches(id: int):
    list_matches = []
    matches = Match.filter()

    for m in matches:
        print(m,m.season)
        list_matches.append(
            match_schema.Match(
                id=str(m),
                country_id = str(m.country_id),
                league_id = str(m.league_id),
                season = m.season,
                stage = m.stage,
                date = m.date,
                # match_api_id = str(m.match_api_id),
                # home_team_api_id = str(m.home_team_api_id),
                # away_team_api_id = str(m.away_team_api_id),
                # home_team_goal = str(m.home_team_goal),
                # away_team_goal = str(m.away_team_goal),
                # name=l.name,
                # id_country=str(l.country_id)
                
                )
        )
    return list_matches
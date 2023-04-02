from fastapi import HTTPException, status

from ..schema import team_schema
from ..service import team_service
from ..model.team_model import Team

def get_teams(id: int = None):
    list_teams = []
    teams = Team.filter()

    for t in teams: 
        print(t,t.team_api_id,t.team_fifa_api_id, t.team_long_name, t.team_short_name)
        list_teams.append(
            team_schema.Team(id=str(t), team_api_id=t.team_api_id,  team_fifa_api_id=t.team_fifa_api_id, team_long_name=t.team_long_name, team_short_name=t.team_short_name)
        )
    return list_teams

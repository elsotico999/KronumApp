from fastapi import HTTPException, status

from ..schema import team_schema
from ..service import team_service
from ..model.team_model import Team

def get_teams(id: int = None):
    list_teams = []
    teams = Team.filter()

    for t in teams: 
        list_teams.append(
            team_schema.Team(id=str(t), t_api_id=t.team_api_id,  t_fifa_id=t.team_fifa_id, t_api_id=t.team_api_id, t_long_name=t.team_long_name, t_short_name=t.team_short_name)
        )
    return list_teams

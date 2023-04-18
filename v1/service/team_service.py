from fastapi import HTTPException, status

from ..schema import team_schema
from ..service import team_service
from ..model.team_model import Team

def get_teams(id: int = None):
    list_teams = []
    teams = Team.filter()

    for t in teams: 
        list_teams.append(
            team_schema.Team(id=str(t), team_api_id=t.team_api_id,  team_fifa_api_id=t.team_fifa_api_id, team_long_name=t.team_long_name, team_short_name=t.team_short_name)
        )
    return list_teams

def get_team(id: int):
    list_teams = []
    teams = Team.filter()
    team = {}
    for t in teams:
        if(str(id) == str(t)):            
            team = team_schema.Team(id=str(t), team_api_id=t.team_api_id,  team_fifa_api_id=t.team_fifa_api_id, team_long_name=t.team_long_name, team_short_name=t.team_short_name) 
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Team not found")
    # return team_schema.Team( id = team.id, team_api_id=team.team_api_id,  team_fifa_api_id=team.team_fifa_api_id, team_long_name=team.team_long_name, team_short_name=team.team_short_name)
    return team
from fastapi import HTTPException, status

from ..schema import team_schema
from ..schema import teamattributes_schema
from ..model.team_model import Team
from ..model.teamattibutes_model import Team_attributes

def get_teams(id: int = None):
    list_teams = []
    teams = Team.filter()

    for t in teams: 
        list_teams.append(
            team_schema.Team(id=str(t), team_api_id=t.team_api_id,  team_fifa_api_id=t.team_fifa_api_id, team_long_name=t.team_long_name, team_short_name=t.team_short_name)
        )
    return list_teams

def get_team(id: int):

    teams = Team.filter()
    team = {}
    for t in teams:
        if(str(id) == str(t)):            
            team = team_schema.Team(id=str(t), team_api_id=t.team_api_id,  team_fifa_api_id=t.team_fifa_api_id, team_long_name=t.team_long_name, team_short_name=t.team_short_name) 
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Team not found")
    # return team_schema.Team( id = team.id, team_api_id=team.team_api_id,  team_fifa_api_id=team.team_fifa_api_id, team_long_name=team.team_long_name, team_short_name=team.team_short_name)
    return team

def get_team_attributes(team_id: int):
    teams_att = Team_attributes.filter()
    list_teams_attr = []
    # print(teams_att)
    for at in teams_att:
        if(str(at.team_api_id) == str(team_id)):
            list_teams_attr.append(teamattributes_schema.TeamAttibute(
                id=str(at), 
                team_api_id=at.team_api_id, 
                team_fifa_api_id=at.team_fifa_api_id, 
                date=str(at.date), 
                buildupplayspeed=at.buildupplayspeed,
                buildupplayspeedclass=at.buildupplayspeedclass,
                buildupplaydribbling=at.buildupplaydribbling,
                buildupplaydribblingclass=at.buildupplaydribblingclass,
                buildupplaypassing=at.buildupplaypassing,
                buildupplaypassingclass=at.buildupplaypassingclass,
                buildupplaypositioningclass=at.buildupplaypositioningclass,
                chancecreationpassing=at.chancecreationpassing,
                chancecreationpassingclass=at.chancecreationpassingclass,
                chancecreationcrossing=at.chancecreationcrossing,
                chancecreationcrossingclass=at.chancecreationcrossingclass,
                chancecreationshooting=at.chancecreationshooting,
                chancecreationshootingclass=at.chancecreationshootingclass,
                chancecreationpositioningclass=at.chancecreationpositioningclass,
                defencepressure=at.defencepressure,
                defencepressureclass=at.defencepressureclass,
                defenceaggression=at.defenceaggression,
                defenceaggressionclass=at.defenceaggressionclass,
                defenceteamwidth=at.defenceteamwidth,
                defenceteamwidthclass=at.defenceteamwidthclass,
                defencedefenderlineclass=at.defencedefenderlineclass,
            ))
    return list_teams_attr
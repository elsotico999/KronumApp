from pydantic import BaseModel ,Field 
from typing import Optional

class TeamAttBase(BaseModel):

    team_api_id: Optional[int]=Field()
    team_fifa_api_id: Optional[int]=Field()
    date: Optional[str]=Field()
    buildupplayspeed: Optional[int]=Field()
    buildupplayspeedclass: Optional[str]=Field()
    buildupplaydribbling: Optional[int]=Field()
    buildupplaydribblingclass: Optional[str]=Field()
    buildupplaypassing: Optional[int]=Field()
    buildupplaypassingclass: Optional[str]=Field()
    buildupplaypositioningclass: Optional[str]=Field()
    chancecreationpassing: Optional[int]=Field()
    chancecreationpassingclass: Optional[str]=Field()
    chancecreationcrossing: Optional[int]=Field()
    chancecreationcrossingclass: Optional[str]=Field()
    chancecreationshooting: Optional[int]=Field()
    chancecreationshootingclass: Optional[str]=Field()
    chancecreationpositioningclass: Optional[str]=Field()
    defencepressure: Optional[int]=Field()
    defencepressureclass: Optional[str]=Field()
    defenceaggression: Optional[int]=Field()
    defenceaggressionclass: Optional[str]=Field()
    defenceteamwidth: Optional[int]=Field()
    defenceteamwidthclass: Optional[str]=Field()
    defencedefenderlineclass: Optional[str]=Field()

class TeamAttibute(TeamAttBase):
    id: Optional[int]= Field(..., example="1")
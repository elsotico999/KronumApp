from pydantic import BaseModel ,Field 
from typing import Optional

class TeamBase(BaseModel):
    team_api_id: Optional[int]=Field()
    team_fifa_api_id: Optional[int]=Field() 
    team_long_name: Optional[str]=Field()
    team_short_name: Optional[str]=Field()

class Team(TeamBase):
    id: Optional[int] = Field(..., example="1")
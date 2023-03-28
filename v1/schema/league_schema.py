from pydantic import BaseModel ,Field 
from typing import Optional

class LeagueBase(BaseModel):
    
    name: Optional[str] = Field (
        ...,
        min_length=3,
        max_length=50,
        example="Liga de Fútbol"
    )
    
class League(LeagueBase):
    id: Optional[int] = Field(..., example="1")


    
from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None
    team_api_id: Optional[int] = None
    team_fifa_api_id: Optional[int] = None
    team_long_name: Optional[str] = None
    team_short_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
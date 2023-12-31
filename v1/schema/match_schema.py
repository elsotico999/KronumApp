from pydantic import BaseModel ,Field 
from typing import Optional

class MatchBase(BaseModel):
    country_id: Optional[int] = Field ()
    league_id: Optional[int] = Field ()
    season: Optional[str] = Field ()
    stage: Optional[str] = Field ()
    date: Optional[int] = Field ()
    stage: Optional[int] = Field ()
    date: Optional[str] = Field ()
    match_api_id: Optional[int] = Field ()
    home_team_api_id: Optional[int] = Field ()
    away_team_api_id: Optional[int] = Field ()
    home_team_goal: Optional[int] = Field ()
    away_team_goal: Optional[int] = Field ()
    home_player_x1: Optional[int] = Field ()
    home_player_x2: Optional[int] = Field ()
    home_player_x3: Optional[int] = Field ()
    home_player_x4: Optional[int] = Field ()
    home_player_x5: Optional[int] = Field ()
    home_player_x6: Optional[int] = Field ()
    home_player_x7: Optional[int] = Field ()
    home_player_x8: Optional[int] = Field ()
    home_player_x9: Optional[int] = Field ()
    home_player_x10: Optional[int] = Field ()
    home_player_x11: Optional[int] = Field ()
    away_player_x1: Optional[int] = Field ()
    away_player_x2: Optional[int] = Field ()
    away_player_x3: Optional[int] = Field ()
    away_player_x4: Optional[int] = Field ()
    away_player_x5: Optional[int] = Field ()
    away_player_x6: Optional[int] = Field ()
    away_player_x7: Optional[int] = Field ()
    away_player_x8: Optional[int] = Field ()
    away_player_x9: Optional[int] = Field ()
    away_player_x10: Optional[int] = Field ()
    away_player_x11: Optional[int] = Field ()
    home_player_y1: Optional[int] = Field ()
    home_player_y2: Optional[int] = Field ()
    home_player_y3: Optional[int] = Field ()
    home_player_y4: Optional[int] = Field ()
    home_player_y5: Optional[int] = Field ()
    home_player_y6: Optional[int] = Field ()
    home_player_y7: Optional[int] = Field ()
    home_player_y8: Optional[int] = Field ()
    home_player_y9: Optional[int] = Field ()
    home_player_y10: Optional[int] = Field ()
    home_player_y11: Optional[int] = Field ()
    away_player_y1: Optional[int] = Field ()
    away_player_y2: Optional[int] = Field ()
    away_player_y3: Optional[int] = Field ()
    away_player_y4: Optional[int] = Field ()
    away_player_y5: Optional[int] = Field ()
    away_player_y6: Optional[int] = Field ()
    away_player_y7: Optional[int] = Field ()
    away_player_y8: Optional[int] = Field ()
    away_player_y9: Optional[int] = Field ()
    away_player_y10: Optional[int] = Field ()
    away_player_y11: Optional[int] = Field ()
    home_player_1: Optional[int] = Field ()
    home_player_2: Optional[int] = Field ()
    home_player_3: Optional[int] = Field ()
    home_player_4: Optional[int] = Field ()
    home_player_5: Optional[int] = Field ()
    home_player_6: Optional[int] = Field ()
    home_player_7: Optional[int] = Field ()
    home_player_8: Optional[int] = Field ()
    home_player_9: Optional[int] = Field ()
    home_player_10: Optional[int] = Field ()
    home_player_11: Optional[int] = Field ()
    away_player_1: Optional[int] = Field ()
    away_player_2: Optional[int] = Field ()
    away_player_3: Optional[int] = Field ()
    away_player_4: Optional[int] = Field ()
    away_player_5: Optional[int] = Field ()
    away_player_6: Optional[int] = Field ()
    away_player_7: Optional[int] = Field ()
    away_player_8: Optional[int] = Field ()
    away_player_9: Optional[int] = Field ()
    away_player_10: Optional[int] = Field ()
    away_player_11: Optional[int] = Field ()
    goal: Optional[str] = Field ()
    shoton: Optional[str] = Field ()
    shotoff: Optional[str] = Field ()
    foulcommit: Optional[str] = Field ()
    card: Optional[str] = Field ()
    cross: Optional[str] = Field ()
    corner: Optional[str] = Field ()
    possession: Optional[str] = Field ()
    b365h: Optional[float] = Field ()
    b365d: Optional[float] = Field ()
    b365a: Optional[float] = Field ()
    bwh: Optional[float] = Field ()
    bwd: Optional[float] = Field ()
    bwa: Optional[float] = Field ()
    iwh: Optional[float] = Field ()
    iwd: Optional[float] = Field ()
    iwa: Optional[float] = Field ()
    lbh: Optional[float] = Field ()
    lbd: Optional[float] = Field ()
    lba: Optional[float] = Field ()
    psh: Optional[float] = Field ()
    psd: Optional[float] = Field ()
    psa: Optional[float] = Field ()
    whh: Optional[float] = Field ()
    whd: Optional[float] = Field ()
    wha: Optional[float] = Field ()
    sjh: Optional[float] = Field ()
    sjd: Optional[float] = Field ()
    sja: Optional[float] = Field ()
    vch: Optional[float] = Field ()
    vcd: Optional[float] = Field ()
    vca: Optional[float] = Field ()
    gbh: Optional[float] = Field ()
    gbd: Optional[float] = Field ()
    gba: Optional[float] = Field ()
    bsh: Optional[float] = Field ()
    bsd: Optional[float] = Field ()
    bsa: Optional[float] = Field ()
class Match(MatchBase):
    id: Optional[int] = Field(...,example="12",)
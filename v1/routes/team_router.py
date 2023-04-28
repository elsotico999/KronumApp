from fastapi import APIRouter, Depends, Body, Query, Path
from fastapi import status
from typing  import List, Optional
from ..schema import team_schema
from ..service import team_service
from ..utils.db import get_db

router = APIRouter(prefix="/api/v1/team")

@router.get("/",tags=["team"],status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def teams(id:Optional[int] = Query(None)):
    if(id == None):
        return team_service.get_teams(id)
    else:
       return team_service.get_team(id) 

@router.get('/{team_id}',tags=["team"],status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def team(id:Optional[int]):
    return team_service.get_team(id)

@router.get('/team_attributes/{team_id}',tags=["team"],status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def team_attributes(team_id:Optional[int]):
    return team_service.get_team_attributes(team_id)

# @router.get('/players_team/{team_id}', tags=['team'], status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
# def team_players(team_id:Optional[int]):
#     # tabla player y player atributes
#     return team_id
# @router.get('/team_attributes/{team_id}',tags=["team"],
#             status_code=status.HTTP_200_OK,
#             dependencies=[Depends(get_db)])
# # def team_attributes(team_id:Optional[int]):
# #     return team_service.get_team_attributes(team_id)9701kVV

from fastapi import APIRouter, Depends, Body, Query, Path
from fastapi import status
from typing  import List, Optional
from ..schema import team_schema
from ..service import team_service
from ..utils.db import get_db

router = APIRouter(prefix="/api/v1/country")

@router.get("/",
            tags=["country"],
            status_code=status.HTTP_200_OK,
            dependencies=[Depends(get_db)])
def teams(id:Optional[int] = Query(None)):
    return team_service.get_teams(id)
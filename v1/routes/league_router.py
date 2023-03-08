from fastapi import APIRouter, Depends, Body, Query, Path
from fastapi import status
from typing import List, Optional
from ..schema import league_schema
from ..service import league_service
from ..utils.db import get_db
from ..service.auth_service import get_current_user

router = APIRouter(prefix="/api/v1/league")

@router.get("/", tags=["league"],status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def get_leagues(id:Optional[int] = Query(None), name:Optional[str] = Query(None),country_id:Optional[int] = Query(None)):
    return league_service.get_leagues(id,name,country_id)
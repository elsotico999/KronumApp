from fastapi import APIRouter, Depends, Body,Query,Path
from fastapi import status
from typing import List, Optional
# from ..schema import match_schema
from ..service import match_service
from ..utils.db import get_db

router = APIRouter(prefix="/api/v1/match")

@router.get("/",
            tags=["match"],
            status_code=status.HTTP_200_OK,
            dependencies=[Depends(get_db)])
def matches( id:Optional[int] = Query(None)):
    return match_service.get_matches(id)
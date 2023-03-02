from fastapi import APIRouter, Depends, Body,Query,Path
from fastapi import status
from typing import List, Optional
from ..schema import country_schema
from ..service import country_service
from ..utils.db import get_db
from ..service.auth_service import get_current_user

router = APIRouter(prefix="/api/v1/country")

@router.get("/", 
            tags=["country"],
            status_code=status.HTTP_200_OK, 
            # response_model=country_schema.Country,
            dependencies=[Depends(get_db)])
def countries( id: Optional[int] = Query(None),name:Optional[str] = Query(None)):
    return country_service.get_countries(id,name)

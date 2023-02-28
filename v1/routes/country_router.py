from fastapi import APIRouter, Depends, Body
from fastapi import status

from ..schema import country_schema
from ..service import country_service
from ..utils.db import get_db
from ..service.auth_service import get_current_user

router = APIRouter(prefix="/api/v1/country")

@router.get("/")
def countries():
    # CUIDADO CON LA FUNCION!
    return {"message": "paises"}
# @router.get(
#     "/",
#     tags=["country"],
#     status_code=status.HTTP_200_OK,
#     response_model=country_schema.Country,
#     dependencies=[Depends(get_db)]
# )
# def get_countries(country=country_schema):
#     pass
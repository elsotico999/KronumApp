from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from ..schema import user_schema
from ..service import user_service

from ..utils.db import get_db

router = APIRouter(prefix="/api/v1")

@router.post (
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)

def create_user(user: user_schema.UserRegister = Body(...)):
    return user_service.create_user(user)
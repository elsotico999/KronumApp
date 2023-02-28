from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from ..schema import user_schema
from ..service import user_service
from ..service import auth_service
from ..schema.token_schema import Token

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
'''--'''
@router.post ("/login",tags=["users"], response_model=Token)
async def login_from_access_token(form_data:OAuth2PasswordRequestForm=Depends()):
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")
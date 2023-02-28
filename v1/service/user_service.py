from fastapi import HTTPException, status

from passlib.context import CryptContext

from ..model.users_model import Users as UserModel
from ..schema import user_schema
from ..service.auth_service import get_password_hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user:user_schema.UserRegister):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username))
    if get_user:
        msg = "La Dirección de correo ya existe!"
        if get_user.username == user.username:
            msg = "El nombre de Usuario ya existe!"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    db_user = UserModel(
        username = user.username,
        email = user.email,
        password = get_password_hash(user.password)
    )
    db_user.save()

    return user_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email
    )
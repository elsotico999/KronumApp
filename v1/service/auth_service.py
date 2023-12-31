from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from passlib.context import CryptContext

from ..model.users_model import Users as UserModel
from ..model.team_model import Team as TeamModel
from ..schema.token_schema import TokenData
from ..utils.settings import Settings

settings = Settings()

SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.token_expires

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")

def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(email: str):
    # user y team
    user = UserModel.filter((UserModel.email == email)).first()
    team = TeamModel.filter((TeamModel.id == user.id_team)).first()
    data = {
        'id': user.id,
        'email':user.email,
        'password':user.password,
        'id_team':user.id_team,
        'team_api_id':team.team_api_id,
        'team_fifa_api_id':team.team_fifa_api_id,
        'team_long_name': team.team_long_name,
        'team_short_name': team.team_short_name
    }
    return data
def authenticate_user(username: str, password: str):
    user = get_user(username)
    
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def generate_token(username, password):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email/username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return create_access_token(
        data={"id": user['id'],
            "email": user['email'],
            'team_api_id':user['team_api_id'],
            'team_fifa_api_id':user['team_fifa_api_id'],
            'team_long_name': user['team_long_name'],
            'team_short_name': user['team_short_name']}, expires_delta=access_token_expires
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
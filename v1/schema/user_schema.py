from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class Userbase(BaseModel):
    email:EmailStr = Field (
        ...,
        example="testmail@testmail.com"
    )
    username: str = Field (
        ...,
        min_length=3,
        max_length=50,
        example="UnUsername"
    )

class User(Userbase):
    id: int = Field(
        ...,
        example="9"
    )
class UserRegister(Userbase):
    password: str = Field (
        ...,
        min_length=8,
        max_length=64,
        example="strongpass"
    )

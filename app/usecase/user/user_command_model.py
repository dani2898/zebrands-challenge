
from pydantic import BaseModel, Field

class UserLoginModel(BaseModel):
    """UserLoginModel represents a model for user login."""

    email: str = Field(
        example="example@test.com"
    )
    password: str = Field(
        example="password"
    )

class UserCreateModel(BaseModel):
    """UserCreateModel represents a model for user creation."""

    email: str = Field(
        example="example@test.com"
    )
    password: str = Field(
        example="password"
    )
    firstname: str = Field(
        example="firstname"
    )
    lastname: str = Field(
        example="lastname"
    )

class UserUpdateModel(BaseModel):
    """UserUpdateModel represents a model for user update."""

    email: str = Field(
        example="example@test.com"
    )
    firstname: str = Field(
        example="firstname"
    )
    lastname: str = Field(
        example="lastname"
    )

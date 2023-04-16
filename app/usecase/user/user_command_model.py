
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
    """UserLoginModel represents a model for user login."""

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

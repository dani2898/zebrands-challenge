from pydantic import BaseModel, Field
from datetime import datetime

from app.domain.user import User

class UserReadModel(BaseModel):
    """UserReadModel represents data structure as a read model."""

    id: str = Field(
        example="uuid"
    )
    email: str = Field(
        example="example@example.com"
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
    created_at: datetime = Field(example='2023-15-04T08:23:45+00:00')
    updated_at: datetime = Field(example='2023-15-04T08:23:45+00:00')

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(user: User) -> "UserReadModel":
        return UserReadModel(
            id=str(user.id),
            email=user.email,
            password=user.password,
            firstname=user.firstname,
            lastname=user.lastname,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

class TokenReadModel(BaseModel):
    """TokenModel represents data structure as a read model."""

    access_token: str = Field(
        example="xxxx.yyyy.zzzz"
    )
    token_type: str = Field(
        example="Bearer"
    )
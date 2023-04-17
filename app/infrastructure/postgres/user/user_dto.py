
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from typing import Union

from app.domain.user import User
from app.infrastructure.postgres.database import Base
from app.usecase.user import UserReadModel



class UserDTO(Base):
    """UserDTO is a data transfer object associated with User entity."""

    __tablename__ = "user"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    email: Union[str, Column] = Column(String(255), unique=True, nullable=False)
    password: Union[str, Column] = Column(String(255), nullable=False)
    firstname: Union[str, Column] = Column(String(255), nullable=False)
    lastname: Union[str, Column] = Column(String(255), nullable=True)
    created_at: Union[datetime, Column] = Column(DateTime, index=True, nullable=False)
    updated_at: Union[datetime, Column] = Column(DateTime, index=True, nullable=False)

    def to_entity(self) -> User:
        return User(
            id=self.id,
            email=self.email,
            password=self.password,
            firstname=self.firstname,
            lastname=self.lastname,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def to_read_model(self) -> UserReadModel:
        return UserReadModel(
            id=str(self.id),
            email=self.email,
            password=self.password,
            firstname=self.firstname,
            lastname=self.lastname,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(user: User) -> "UserDTO":
        return UserDTO(
            id=user.id,
            email=user.email,
            password=user.password,
            firstname=user.firstname,
            lastname=user.lastname,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
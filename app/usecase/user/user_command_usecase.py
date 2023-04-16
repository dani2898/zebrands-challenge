from abc import ABC, abstractmethod
from datetime import datetime
from typing import cast, Optional
from uuid import uuid4

from passlib.context import CryptContext

from app.domain.user import (
    User, 
    UserRepository,
    EmailAlreadyExistError,
    )

from .user_command_model import UserCreateModel
from .user_query_model import UserReadModel

class UserCommandUsecaseUnitOfWork(ABC):
    """Defines an interface based on Unit of Work pattern."""

    user_repository: UserRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

    @abstractmethod
    def flush(self):
        raise NotImplementedError


class UserCommandUsecase(ABC):
    """
    UserCommandUsecase defines a command usecase inteface related User entity.
    """

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str):
        raise NotImplementedError
    
    @abstractmethod
    def create_user(self, data: UserCreateModel)-> Optional[UserReadModel]:
        raise NotImplementedError


class UserCommandUsecaseImpl(UserCommandUsecase):
    """
    UserCommandUsecaseImpl implements a command usecases related User entity.
    """

    def __init__(
        self,
        uow: UserCommandUsecaseUnitOfWork,
    ):
        self.uow: UserCommandUsecaseUnitOfWork = uow
        self.pwd_crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_crypt.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password: str):
        return self.pwd_crypt.hash(password)
    
    def create_user(
        self, data: UserCreateModel
    ) -> Optional[UserReadModel]:
        try:
            uuid = str(uuid4())
            user = User(
                id=uuid,
                email=data.email,
                password=self.get_password_hash(data.password),
                firstname=data.firstname,
                lastname=data.lastname,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )

            existing_user = self.uow.user_repository.find_by_email(data.email)
            
            if existing_user is not None:
                raise EmailAlreadyExistError

            self.uow.user_repository.create(user)
            self.uow.commit()

            created_user = self.uow.user_repository.find_by_id(uuid)
        except Exception:
            self.uow.rollback()
            raise

        return UserReadModel.from_entity(cast(User, created_user))


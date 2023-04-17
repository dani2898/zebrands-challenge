from abc import ABC, abstractmethod
from datetime import datetime
from typing import cast, Optional
from uuid import uuid4

from passlib.context import CryptContext

from app.domain.user import (
    User, 
    UserRepository,
    EmailAlreadyExistError,
    UserNotFoundError
    )

from .user_command_model import(
    UserCreateModel,
    UserUpdateModel
)

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
    def get_password_hash(self, password: str):
        raise NotImplementedError
       
    @abstractmethod
    def create_user(self, data: UserCreateModel)-> Optional[UserReadModel]:
        raise NotImplementedError
    
    @abstractmethod
    def update_user(self, user_id: str, data: UserUpdateModel)-> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_user_by_id(self, user_id: str):
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

    def update_user(
        self, user_id: str, data: UserUpdateModel
    ) -> Optional[UserReadModel]:
        try:
            existing_user = self.uow.user_repository.find_by_id(user_id)
            if existing_user is None:
                raise UserNotFoundError
            
            email_exist = self.uow.user_repository.find_by_email(data.email)
            
            if email_exist is not None and email_exist.email != existing_user.email:
                raise EmailAlreadyExistError
            
            user = User(
                id=existing_user.id,
                email=data.email,
                password=existing_user.password,
                firstname=data.firstname,
                lastname=data.lastname,
                created_at=existing_user.created_at,
                updated_at=datetime.now()
            )
            self.uow.user_repository.update(user_id, user)
            self.uow.commit()
            
            updated_user = self.uow.user_repository.find_by_id(user_id)

        except Exception:
            self.uow.rollback()
            raise

        return UserReadModel.from_entity(cast(User, updated_user))
    
    def delete_user_by_id(self, id: str):
        try:
            existing_user = self.uow.user_repository.find_by_id(id)
            if existing_user is None:
                raise UserNotFoundError

            self.uow.user_repository.delete_user_by_id(id)

            self.uow.commit()

        except Exception:
            self.uow.rollback()
            raise
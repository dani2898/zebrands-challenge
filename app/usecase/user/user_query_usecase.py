from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.user import UserNotFoundError

from .user_query_model import UserReadModel
from .user_query_service import UserQueryService


class UserQueryUsecase(ABC):
    """UserQueryUsecase defines a query usecase inteface related User entity."""

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def get_users(self) -> List[UserReadModel]:
        raise NotImplementedError

class UserQueryUsecaseImpl(UserQueryUsecase):
    """UserQueryUsecaseImpl implements a query usecases related User entity."""

    def __init__(self, user_query_service: UserQueryService):
        self.user_query_service: UserQueryService = user_query_service

    def get_user_by_email(self, email: str) -> Optional[UserReadModel]:
        try:
            user = self.user_query_service.find_by_email(email)
            if user is None:
                return False
        except:
            raise

        return user
    
    def get_users(self) -> List[UserReadModel]:
        try:
            users = self.user_query_service.find_all()
        except:
            raise

        return users


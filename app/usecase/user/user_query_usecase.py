from abc import ABC, abstractmethod
from typing import Optional

from app.domain.user import UserNotFoundError

from .user_query_model import UserReadModel
from .user_query_service import UserQueryService


class UserQueryUsecase(ABC):
    """UserQueryUsecase defines a query usecase inteface related User entity."""

    @abstractmethod
    def fetch_user_by_email(self, email: str) -> Optional[UserReadModel]:
        raise NotImplementedError


class UserQueryUsecaseImpl(UserQueryUsecase):
    """UserQueryUsecaseImpl implements a query usecases related User entity."""

    def __init__(self, user_query_service: UserQueryService):
        self.user_query_service: UserQueryService = user_query_service

    def fetch_user_by_email(self, email: str) -> Optional[UserReadModel]:
        try:
            user = self.user_query_service.find_by_email(email)
            if user is None:
                return False
        except:
            raise

        return user


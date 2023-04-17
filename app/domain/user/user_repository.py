from abc import ABC, abstractmethod
from typing import Optional

from app.domain.user import User


class UserRepository(ABC):
    """UserRepository defines a repository interface for User entity."""

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[User]:
        raise NotImplementedError
    
    @abstractmethod
    def create(self, user: User) -> Optional[User]:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, user_id: str, user: User) -> Optional[User]:
        raise NotImplementedError
    
    @abstractmethod
    def delete_user_by_id(self, user_id: str):
        raise NotImplementedError
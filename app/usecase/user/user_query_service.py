from abc import ABC, abstractmethod
from typing import List, Optional

from .user_query_model import UserReadModel

class UserQueryService(ABC):
    """UserQueryService defines a query service inteface related User entity."""

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[UserReadModel]:
        raise NotImplementedError
    
    @abstractmethod
    def find_all(self) -> List[UserReadModel]:
        raise NotImplementedError

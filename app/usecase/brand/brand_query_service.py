from abc import ABC, abstractmethod
from typing import List, Optional

from .brand_query_model import BrandReadModel

class BrandQueryService(ABC):
    """BrandQueryService defines a query service inteface related Brand entity."""
    
    @abstractmethod
    def find_all(self) -> List[BrandReadModel]:
        raise NotImplementedError

from abc import ABC, abstractmethod

from typing import List, Optional

from .product_query_model import ProductReadModel
class ProductQueryService(ABC):
    """ProductQueryService defines a query service inteface related Product entity."""
   
    @abstractmethod
    def find_all(self) -> List[ProductReadModel]:
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, product_id: str) -> Optional[ProductReadModel]:
        raise NotImplementedError
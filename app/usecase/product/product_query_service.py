from abc import ABC, abstractmethod

from typing import List

from .product_query_model import ProductReadModel
class ProductQueryService(ABC):
    """ProductQueryService defines a query service inteface related Product entity."""
   
    @abstractmethod
    def find_all(self) -> List[ProductReadModel]:
        raise NotImplementedError
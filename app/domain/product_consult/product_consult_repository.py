from abc import ABC, abstractmethod
from typing import Optional

from app.domain.product_consult import ProductConsult

class ProductConsultRepository(ABC):
    """ProductConsultRepository defines a repository interface for ProductConsult entity."""
    
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[ProductConsult]:
        raise NotImplementedError
    
    @abstractmethod
    def create(self, product_consult: ProductConsult) -> Optional[ProductConsult]:
        raise NotImplementedError
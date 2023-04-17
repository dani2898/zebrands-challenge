from abc import ABC, abstractmethod
from typing import Optional

from app.domain.product import Product

class ProductRepository(ABC):
    """ProductRepository defines a repository interface for Product entity."""

    @abstractmethod
    def find_by_sku(self, sku: str) -> Optional[Product]:
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Product]:
        raise NotImplementedError
    
    @abstractmethod
    def create(self, product: Product) -> Optional[Product]:
        raise NotImplementedError
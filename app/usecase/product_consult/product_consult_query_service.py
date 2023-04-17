from abc import ABC, abstractmethod

class ProductConsultQueryService(ABC):
    """ProductConsultQueryService defines a query service inteface related ProductConsult entity."""
   
    @abstractmethod
    def get_count(self, product_id: str) -> int:
        raise NotImplementedError
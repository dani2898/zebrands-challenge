from abc import ABC, abstractmethod

from .product_consult_query_service import ProductConsultQueryService


class ProductConsultQueryUsecase(ABC):
    """ProductConsultQueryUsecase defines a query usecase inteface related ProductConsult entity."""
    
    @abstractmethod
    def get_count(self, product_id: str) -> int:
        raise NotImplementedError
class ProductConsultQueryUsecaseImpl(ProductConsultQueryUsecase):
    """ProductConsultQueryUsecaseImpl implements a query usecases related ProductConsult entity."""

    def __init__(self, product_consult_query_service: ProductConsultQueryService):
        self.product_consult_query_service: ProductConsultQueryService = product_consult_query_service

    def get_count(self, product_id: str) -> int:
        try:
            count = self.product_consult_query_service.get_count(product_id)
        except:
            raise

        return count
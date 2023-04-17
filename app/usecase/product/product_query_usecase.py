from abc import ABC, abstractmethod
from typing import List, Optional

from .product_query_model import ProductReadModel
from .product_query_service import ProductQueryService


class ProductQueryUsecase(ABC):
    """ProductQueryUsecase defines a query usecase inteface related Product entity."""

    @abstractmethod
    def get_products(self) -> List[ProductReadModel]:
        raise NotImplementedError

class ProductQueryUsecaseImpl(ProductQueryUsecase):
    """ProductQueryUsecaseImpl implements a query usecases related Product entity."""

    def __init__(self, product_query_service: ProductQueryService):
        self.product_query_service: ProductQueryService = product_query_service

    def get_products(self) -> List[ProductReadModel]:
        try:
            products = self.product_query_service.find_all()
        except:
            raise

        return products
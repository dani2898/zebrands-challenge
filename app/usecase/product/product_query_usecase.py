from abc import ABC, abstractmethod
from typing import List, Optional

from .product_query_service import ProductQueryService


class ProductQueryUsecase(ABC):
    """ProductQueryUsecase defines a query usecase inteface related Product entity."""


class ProductQueryUsecaseImpl(ProductQueryUsecase):
    """ProductQueryUsecaseImpl implements a query usecases related Product entity."""

    def __init__(self, product_query_service: ProductQueryService):
        self.product_query_service: ProductQueryService = product_query_service



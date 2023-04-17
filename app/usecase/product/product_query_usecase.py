from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.product import ProductNotFoundError
from app.domain.product_consult import ProductConsultError
from .product_query_model import ProductReadModel
from .product_query_service import ProductQueryService
from app.usecase.product_consult.product_consult_command_usecase import (
    ProductConsultCommandUsecase
)

class ProductQueryUsecase(ABC):
    """ProductQueryUsecase defines a query usecase inteface related Product entity."""

    @abstractmethod
    def get_products(self) -> List[ProductReadModel]:
        raise NotImplementedError
    
    @abstractmethod
    def get_product_by_id(self, product_id: str, 
                          product_consult_command_usecase: ProductConsultCommandUsecase
                          ) -> Optional[ProductReadModel]:
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
    
    
    def get_product_by_id(self, product_id: str, 
                          product_consult_command_usecase: ProductConsultCommandUsecase
                          ) -> Optional[ProductReadModel]:
        try:
            product = self.product_query_service.find_by_id(product_id)
            if product is None:
                raise ProductNotFoundError

            product_consult = product_consult_command_usecase.create_product_consult(product_id)
            
            if product_consult is None:
                raise ProductConsultError
        except:
            raise

        return product
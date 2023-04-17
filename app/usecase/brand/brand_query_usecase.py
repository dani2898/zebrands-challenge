from abc import ABC, abstractmethod
from typing import List


from .brand_query_model import BrandReadModel
from .brand_query_service import BrandQueryService


class BrandQueryUsecase(ABC):
    """BrandQueryUsecase defines a query usecase inteface related Brand entity."""

    @abstractmethod
    def get_brands(self) -> List[BrandReadModel]:
        raise NotImplementedError

class BrandQueryUsecaseImpl(BrandQueryUsecase):
    """BrandQueryUsecaseImpl implements a query usecases related Brand entity."""

    def __init__(self, brand_query_service: BrandQueryService):
        self.brand_query_service: BrandQueryService = brand_query_service
    
    def get_brands(self) -> List[BrandReadModel]:
        try:
            brands = self.brand_query_service.find_all()
        except:
            raise

        return brands


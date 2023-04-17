from abc import ABC

from .product_consult_query_service import ProductConsultQueryService


class ProductConsultQueryUsecase(ABC):
    """ProductConsultQueryUsecase defines a query usecase inteface related ProductConsult entity."""

class ProductConsultQueryUsecaseImpl(ProductConsultQueryUsecase):
    """ProductConsultQueryUsecaseImpl implements a query usecases related ProductConsult entity."""

    def __init__(self, product_consult_query_service: ProductConsultQueryService):
        self.product_consult_query_service: ProductConsultQueryService = product_consult_query_service

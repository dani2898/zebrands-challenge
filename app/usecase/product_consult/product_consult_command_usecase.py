from abc import ABC, abstractmethod
from datetime import datetime
from typing import cast, Optional
from uuid import uuid4

from app.domain.product_consult import (
    ProductConsult,
    ProductConsultRepository,
    )

from .product_consult_query_model import ProductConsultReadModel
class ProductConsultCommandUsecaseUnitOfWork(ABC):
    """Defines an interface based on Unit of Work pattern."""

    product_consult_repository: ProductConsultRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

    @abstractmethod
    def flush(self):
        raise NotImplementedError


class ProductConsultCommandUsecase(ABC):
    """
    ProductConsultCommandUsecase defines a command usecase inteface related ProductConsult entity.
    """

    @abstractmethod
    def create_product_consult(self, product_id: str)-> Optional[ProductConsultReadModel]:
        raise NotImplementedError

class ProductConsultCommandUsecaseImpl(ProductConsultCommandUsecase):
    """
    ProductConsultCommandUsecaseImpl implements a command usecases related ProductConsult entity.
    """

    def __init__(
        self,
        uow: ProductConsultCommandUsecaseUnitOfWork,
    ):
        self.uow: ProductConsultCommandUsecaseUnitOfWork = uow

    def create_product_consult(
        self, product_id: str
    ) -> Optional[ProductConsultReadModel]:
        try:
            uuid = str(uuid4())
            product_consult = ProductConsult(
                id=uuid,
                product_id=product_id,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )

            self.uow.product_consult_repository.create(product_consult)
            self.uow.commit()

            created_product_consult = self.uow.product_consult_repository.find_by_id(uuid)
        except Exception:
            self.uow.rollback()
            raise

        return ProductConsultReadModel.from_entity(cast(product_consult, created_product_consult))
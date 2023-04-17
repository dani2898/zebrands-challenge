from abc import ABC, abstractmethod
from datetime import datetime
from typing import cast, Optional
from uuid import uuid4

from app.domain.product import (
    Product,
    ProductRepository,
    SkuAlreadyExistError
    )

from .product_command_model import (
    ProductCreateModel
)

from .product_query_model import ProductReadModel
class ProductCommandUsecaseUnitOfWork(ABC):
    """Defines an interface based on Unit of Work pattern."""

    product_repository: ProductRepository

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


class ProductCommandUsecase(ABC):
    """
    ProductCommandUsecase defines a command usecase inteface related Product entity.
    """

    @abstractmethod
    def create_product(self, data: ProductCreateModel)-> Optional[ProductReadModel]:
        raise NotImplementedError


class ProductCommandUsecaseImpl(ProductCommandUsecase):
    """
    ProductCommandUsecaseImpl implements a command usecases related Product entity.
    """

    def __init__(
        self,
        uow: ProductCommandUsecaseUnitOfWork,
    ):
        self.uow: ProductCommandUsecaseUnitOfWork = uow

    def create_product(
        self, data: ProductCreateModel
    ) -> Optional[ProductReadModel]:
        try:
            uuid = str(uuid4())
            product = Product(
                id=uuid,
                sku=data.sku,
                name=data.name,
                description=data.description,
                stock=data.stock,
                price=data.price,
                status=data.status,
                brand_id=str(data.brand_id),
                created_at=datetime.now(),
                updated_at=datetime.now()
            )

            existing_product = self.uow.product_repository.find_by_sku(data.sku)
            
            if existing_product is not None:
                raise SkuAlreadyExistError

            self.uow.product_repository.create(product)
            self.uow.commit()

            created_product = self.uow.product_repository.find_by_id(uuid)
        except Exception:
            self.uow.rollback()
            raise

        return ProductReadModel.from_entity(cast(Product, created_product))
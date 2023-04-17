from abc import ABC, abstractmethod
from datetime import datetime
from typing import cast, Optional
from uuid import uuid4

from app.domain.product import (
    Product,
    ProductRepository,
    SkuAlreadyExistError,
    ProductNotFoundError
    )

from .product_command_model import (
    ProductCreateModel,
    ProductUpdateModel
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

    @abstractmethod
    def update_product(self, product_id: str, data: ProductUpdateModel)-> Optional[ProductReadModel]:
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
    
    def update_product(
        self, product_id: str, data: ProductUpdateModel
    ) -> Optional[ProductReadModel]:
        try:
            existing_product = self.uow.product_repository.find_by_id(product_id)
            if existing_product is None:
                raise ProductNotFoundError
            
            sku_exist = self.uow.product_repository.find_by_sku(data.sku)
            
            if sku_exist and sku_exist.sku != existing_product.sku:
                raise SkuAlreadyExistError
            
            product = Product(
                id=existing_product.id,
                sku=data.sku,
                name=data.name,
                description=data.description,
                stock=data.stock,
                price=data.price,
                status=data.status,
                brand_id=data.brand_id,
                created_at=existing_product.created_at,
                updated_at=datetime.now()
            )
            self.uow.product_repository.update(product_id, product)
            self.uow.commit()
            
            updated_product = self.uow.product_repository.find_by_id(product_id)
        except Exception:
            self.uow.rollback()
            raise

        return ProductReadModel.from_entity(cast(Product, updated_product))
    
    def delete_product_by_id(self, id: str):
        try:
            existing_product = self.uow.product_repository.find_by_id(id)
            if existing_product is None:
                raise ProductNotFoundError

            self.uow.product_repository.delete_product_by_id(id)

            self.uow.commit()

        except Exception:
            self.uow.rollback()
            raise
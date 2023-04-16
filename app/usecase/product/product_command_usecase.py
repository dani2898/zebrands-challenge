from abc import ABC, abstractmethod

from app.domain.product import (
    ProductRepository,
    )

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


class ProductCommandUsecaseImpl(ProductCommandUsecase):
    """
    ProductCommandUsecaseImpl implements a command usecases related Product entity.
    """

    def __init__(
        self,
        uow: ProductCommandUsecaseUnitOfWork,
    ):
        self.uow: ProductCommandUsecaseUnitOfWork = uow

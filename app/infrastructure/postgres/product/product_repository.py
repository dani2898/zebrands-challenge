from sqlalchemy.orm.session import Session

from app.domain.product import  ProductRepository
from app.usecase.product import ProductCommandUsecaseUnitOfWork

class ProductRepositoryImpl(ProductRepository):
    """ProductRepositoryImpl implements CRUD operations related Product entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session


class ProductCommandUsecaseUnitOfWorkImpl(ProductCommandUsecaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        product_repository: ProductRepository,
    ):
        self.session: Session = session
        self.product_repository: ProductRepository = product_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def flush(self):
        self.session.flush()

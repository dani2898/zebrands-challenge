from typing import Optional
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.domain.product import  Product, ProductRepository
from app.usecase.product import ProductCommandUsecaseUnitOfWork
from .product_dto import ProductDTO

class ProductRepositoryImpl(ProductRepository):
    """ProductRepositoryImpl implements CRUD operations related Product entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_sku(self, sku: str) -> Optional[Product]:
        try:
            product_dto = self.session.query(ProductDTO).filter_by(sku=sku).one()
        except NoResultFound:
            return None
    
        return product_dto.to_entity()
    
    def find_by_id(self, id: str) -> Optional[Product]:
        try:
            user_dto = self.session.query(ProductDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return user_dto.to_entity()
    
    def create(self, product: Product):
        product_dto = ProductDTO.from_entity(product)
        try:
            self.session.add(product_dto)
        except:
            raise

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

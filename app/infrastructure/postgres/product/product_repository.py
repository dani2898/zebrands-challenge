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
            product_dto = self.session.query(ProductDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return product_dto.to_entity()
    
    def create(self, product: Product):
        product_dto = ProductDTO.from_entity(product)
        try:
            self.session.add(product_dto)
        except:
            raise

    def update(self, product_id: str, product: Product):
        product_dto = ProductDTO.from_entity(product)
        try:
            _product = self.session.query(ProductDTO).filter_by(
                id=product_id
            ).one()
            _product.sku = product_dto.sku
            _product.name = product_dto.name
            _product.description = product_dto.description
            _product.stock = product_dto.stock
            _product.price = product_dto.price
            _product.status = product_dto.status
            _product.brand_id = product_dto.brand_id
            _product.updated_at = product_dto.updated_at

        except Exception:
            raise

    def delete_product_by_id(self, id: str):
        try:
            _product = self.session.query(ProductDTO).filter_by(
                id=id
            ).one()
            _product.status = 0

        except Exception:
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

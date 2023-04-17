from typing import Optional
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.domain.product_consult import  ProductConsult, ProductConsultRepository
from app.usecase.product_consult import ProductConsultCommandUsecaseUnitOfWork
from .product_consult_dto import ProductConsultDTO

class ProductConsultRepositoryImpl(ProductConsultRepository):
    """ProductConsultRepositoryImpl implements CRUD operations related ProductConsult entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[ProductConsult]:
        try:
            product_consult = self.session.query(ProductConsultDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return product_consult.to_entity()
    
    def create(self, product_consult: ProductConsult):
        product_consult_dto = ProductConsultDTO.from_entity(product_consult)
        try:
            self.session.add(product_consult_dto)
        except:
            raise

class ProductConsultCommandUsecaseUnitOfWorkImpl(ProductConsultCommandUsecaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        product_consult_repository: ProductConsultRepository,
    ):
        self.session: Session = session
        self.product_consult_repository: ProductConsultRepository = product_consult_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def flush(self):
        self.session.flush()

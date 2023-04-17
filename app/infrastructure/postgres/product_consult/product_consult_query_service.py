from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.usecase.product_consult import ProductConsultQueryService
from .product_consult_dto import ProductConsultDTO

class ProductConsultQueryServiceImpl(ProductConsultQueryService):
    """ProductConsultQueryServiceImpl implements READ operations 
    related ProductConsult entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def get_count(self, product_id: str) -> int:
        try:
            consult_count = self.session.query(ProductConsultDTO).filter_by(
                product_id=product_id,
            ).count()
        except NoResultFound:
            return None
        except:
            raise
        return consult_count
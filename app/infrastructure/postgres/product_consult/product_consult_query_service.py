from sqlalchemy.orm.session import Session

from app.usecase.product_consult import ProductConsultQueryService

class ProductConsultQueryServiceImpl(ProductConsultQueryService):
    """ProductConsultQueryServiceImpl implements READ operations 
    related ProductConsult entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session
from sqlalchemy.orm.session import Session

from app.usecase.product import ProductQueryService


class ProductQueryServiceImpl(ProductQueryService):
    """ProductQueryServiceImpl implements READ operations related Product entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session


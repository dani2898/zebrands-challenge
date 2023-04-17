from sqlalchemy.orm.session import Session

from typing import List
from app.usecase.product import ProductQueryService, ProductReadModel

from .product_dto import ProductDTO

class ProductQueryServiceImpl(ProductQueryService):
    """ProductQueryServiceImpl implements READ operations related Product entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_all(self) -> List[ProductReadModel]:
        try:
            product_dtos = (
                self.session.query(ProductDTO)
                .filter_by(status=True)
                .order_by(ProductDTO.name)
                .limit(50)
                .all()
            )
        except:
            raise
        if len(product_dtos) == 0:
            return []

        return list(map(lambda product_dto: product_dto.to_read_model(), product_dtos))

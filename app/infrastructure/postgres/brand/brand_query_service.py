from typing import List, Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.usecase.brand import BrandQueryService, BrandReadModel

from .brand_dto import BrandDTO


class BrandQueryServiceImpl(BrandQueryService):
    """BrandQueryServiceImpl implements READ operations related Brand entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session
    
    def find_all(self) -> List[BrandReadModel]:
        try:
            brand_dtos = (
                self.session.query(BrandDTO)
                .order_by(BrandDTO.name)
                .limit(50)
                .all()
            )
        except:
            raise
        if len(brand_dtos) == 0:
            return []

        return list(map(lambda brand_dto: brand_dto.to_read_model(), brand_dtos))

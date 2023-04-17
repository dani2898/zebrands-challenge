from datetime import datetime
from sqlalchemy import Column, String, DateTime
from typing import Union

from app.domain.product_consult import ProductConsult
from app.infrastructure.postgres.database import Base
from app.usecase.product_consult import ProductConsultReadModel



class ProductConsultDTO(Base):
    """ProductConsultDTO is a data transfer object associated with ProductConsult entity."""

    __tablename__ = "product_consult"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    product_id: Union[str, Column] = Column(String(255), unique=True, nullable=False)
    created_at: Union[datetime, Column] = Column(DateTime, index=True, nullable=False)
    updated_at: Union[datetime, Column] = Column(DateTime, index=True, nullable=False)

    def to_entity(self) -> ProductConsult:
        return ProductConsult(
            id=self.id,
            product_id=self.product_id,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def to_read_model(self) -> ProductConsultReadModel:
        return ProductConsultReadModel(
            id=str(self.id),
            product_id=str(self.product_id),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(product_consult: ProductConsult) -> "ProductConsultDTO":
        return ProductConsultDTO(
            id=product_consult.id,
            product_id=product_consult.product_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
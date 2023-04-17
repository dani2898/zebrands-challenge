from pydantic import BaseModel, Field
from datetime import datetime

from app.domain.product_consult import ProductConsult

class ProductConsultReadModel(BaseModel):
    """ProductConsultReadModel represents data structure as a read model."""

    id: str = Field(
        example="uuid"
    )
    product_id: str = Field(
        example="uuid"
    )
    created_at: datetime = Field(example='2023-15-04T08:23:45+00:00')
    updated_at: datetime = Field(example='2023-15-04T08:23:45+00:00')

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(product_consult: ProductConsult) -> "ProductConsultReadModel":
        return ProductConsultReadModel(
            id=str(product_consult.id),
            product_id=str(product_consult.product_id),
            created_at=product_consult.created_at,
            updated_at=product_consult.updated_at,
        )

from pydantic import BaseModel, Field
from datetime import datetime

from app.domain.brand import Brand

class BrandReadModel(BaseModel):
    """BrandReadModel represents data structure as a read model."""

    id: str = Field(
        example="uuid"
    )
    name: str = Field(
        example="name"
    )
    description: str = Field(
        example="description"
    )
    created_at: datetime = Field(example='2023-15-04T08:23:45+00:00')
    updated_at: datetime = Field(example='2023-15-04T08:23:45+00:00')

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(brand: Brand) -> "BrandReadModel":
        return BrandReadModel(
            id=str(brand.id),
            name=brand.name,
            description=brand.description,
            created_at=brand.created_at,
            updated_at=brand.updated_at,
        )

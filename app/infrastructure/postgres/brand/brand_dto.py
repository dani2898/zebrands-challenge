
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from typing import Union

from app.domain.brand import Brand
from app.infrastructure.postgres.database import Base
from app.usecase.brand import BrandReadModel



class BrandDTO(Base):
    """BrandDTO is a data transfer object associated with Brand entity."""

    __tablename__ = "brand"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    name: Union[str, Column] = Column(String(255), unique=True, nullable=False)
    description: Union[str, Column] = Column(String(255), unique=True, nullable=False)
    created_at: Union[datetime, Column] = Column(DateTime, index=True, nullable=False)
    updated_at: Union[datetime, Column] = Column(DateTime, index=True, nullable=False)

    def to_entity(self) -> Brand:
        return Brand(
            id=self.id,
            name=self.name,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def to_read_model(self) -> BrandReadModel:
        return BrandReadModel(
            id=str(self.id),
            name=self.name,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(brand: Brand) -> "BrandDTO":
        return BrandDTO(
            id=brand.id,
            name=brand.name,
            description=brand.description,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
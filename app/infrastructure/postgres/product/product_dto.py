
from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Numeric
from typing import Union

from app.domain.product import Product
from app.infrastructure.postgres.database import Base
from app.usecase.product import ProductReadModel



class ProductDTO(Base):
    """ProductDTO is a data transfer object associated with Product entity."""

    __tablename__ = "product"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    sku: Union[str, Column] = Column(String(255), unique=True, nullable=False)
    name: Union[str, Column] = Column(String(255), nullable=False)
    description: Union[str, Column] = Column(String(255), nullable=False)
    stock: Union[int, Column] = Column(Integer, nullable=True)
    price: Union[Numeric, Column] = Column(Numeric, nullable=True)
    status: Union[bool, Column] = Column(Boolean, nullable=True)
    brand_id: Union[int, Column] = Column(String(255), nullable=True)
    created_at: Union[datetime, Column] = Column(DateTime, index=True, nullable=False)
    updated_at: Union[datetime, Column] = Column(DateTime, index=True, nullable=False)

    def to_entity(self) -> Product:
        return Product(
            id=self.id,
            sku=self.sku,
            name=self.name,
            description=self.description,
            stock=self.stock,
            price=self.price,
            status=self.status,
            brand_id=self.brand_id,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def to_read_model(self) -> ProductReadModel:
        return ProductReadModel(
            id=str(self.id),
            sku=self.sku,
            name=self.name,
            description=self.description,
            stock=self.stock,
            price=self.price,
            status=self.status,
            brand_id=self.brand_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(product: Product) -> "ProductDTO":
        return ProductDTO(
            id=product.id,
            sku=product.sku,
            name=product.name,
            description=product.description,
            stock=product.stock,
            price=product.price,
            status=product.status,
            brand_id=product.brand_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
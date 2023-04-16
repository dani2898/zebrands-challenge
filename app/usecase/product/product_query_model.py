from pydantic import BaseModel, Field
from datetime import datetime

from app.domain.product import Product

class ProductReadModel(BaseModel):
    """ProductReadModel represents data structure as a read model."""

    id: str = Field(
        example="c56d20c7-ebc4-43f1-9808-4a298fd61554"
    )
    sku: str = Field(
        example="XYZ12345"
    )
    name: str = Field(
        example="Colchón"
    )
    description: str = Field(
        example="Colchón matrimonial"
    )
    stock: str = Field(
        example=15
    )
    price: str = Field(
        example=17000.00
    )
    status: str = Field(
        example=1
    )
    brand_id: str = Field(
        example="65c4a456-6f01-4d5c-8397-6bcb8dd43286"
    )
    created_at: datetime = Field(example='2023-15-04T08:23:45+00:00')
    updated_at: datetime = Field(example='2023-15-04T08:23:45+00:00')

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(product: Product) -> "ProductReadModel":
        return ProductReadModel(
            id=str(product.id),
            sku=product.sku,
            name=product.name,
            description=product.description,
            stock=product.stock,
            price=product.price,
            status=product.status,
            brand_id=product.brand_id,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )

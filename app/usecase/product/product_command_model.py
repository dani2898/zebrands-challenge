
from pydantic import BaseModel, Field

class ProductCreateModel(BaseModel):
    """ProductCreateModel represents a model for product creation."""

    sku: str = Field(
        example="XYZ12345"
    )
    name: str = Field(
        example="Colchón"
    )
    description: str = Field(
        example="Colchón matrimonial"
    )
    stock: int = Field(
        example=15
    )
    price: float = Field(
        example=17000.00
    )
    status: bool = Field(
        example=1
    )
    brand_id: str = Field(
        example="uuid"
    )

class ProductUpdateModel(ProductCreateModel):
    """ProductUpdateModel represents a model for product creation."""

    pass

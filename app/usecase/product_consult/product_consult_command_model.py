
from pydantic import BaseModel, Field

class ProductConsultCreateModel(BaseModel):
    """ProductConsultCreateModel represents a model for product_consult creation."""

    product_id: str = Field(
        example="uuid"
    )


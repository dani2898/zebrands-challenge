from pydantic import BaseModel, Field

from app.domain.brand import (
    BrandNotFoundError
)

class ErrorMessageBrandNotFound(BaseModel):
    detail: str = Field(example=BrandNotFoundError.message)
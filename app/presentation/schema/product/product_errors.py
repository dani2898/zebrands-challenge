from pydantic import BaseModel, Field

from app.domain.product import (
    SkuAlreadyExistError,
    ProductNotFoundError
)

class ErrorMessageSkuAlreadyExists(BaseModel):
    detail: str = Field(example=SkuAlreadyExistError.message)

class ErrorMessageProductNotFound(BaseModel):
    detail: str = Field(example=ProductNotFoundError.message)
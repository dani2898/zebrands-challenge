from pydantic import BaseModel, Field

from app.domain.user import (
    UserUnauthorizedError,
    EmailAlreadyExistError
)

class ErrorMessageUserUnauthorizedError(BaseModel):
    detail: str = Field(example=UserUnauthorizedError.message)

class ErrorMessageEmailAlreadyExists(BaseModel):
    detail: str = Field(example=EmailAlreadyExistError.message)
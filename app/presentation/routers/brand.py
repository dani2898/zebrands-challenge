from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.interface_adapters.security import JWTBearer

from app.domain.brand import (
    BrandNotFoundError
)

from app.interface_adapters.session.session_manager import (
    brand_query_usecase,
)
from app.presentation.schema.brand.brand_errors import (
    ErrorMessageBrandNotFound
)

from app.usecase.brand import (
    BrandQueryUsecase,
    BrandReadModel,
)


router = APIRouter()

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

@router.get(
    "/",
    response_model=List[BrandReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageBrandNotFound,
        },
    },
    dependencies=[Depends(JWTBearer())]
)
async def list_brands(
    brand_query_usecase: BrandQueryUsecase = Depends(brand_query_usecase),
):
    try:
        brands = brand_query_usecase.get_brands()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if len(brands) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=BrandNotFoundError.message,
        )

    return brands
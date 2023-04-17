from fastapi import APIRouter, Depends, HTTPException, status

from app.domain.product import (
    SkuAlreadyExistError
)
from app.presentation.schema.product.product_errors import (
    ErrorMessageSkuAlreadyExists
)

from app.interface_adapters.session.session_manager import (
    product_query_usecase,
    product_command_usecase,
)

from app.usecase.product import (
    ProductCommandUsecase,
    ProductCreateModel,
    ProductReadModel
)

router = APIRouter()


@router.post(
    "/create",
    response_model=ProductReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "model": ErrorMessageSkuAlreadyExists,
        },
    },
)
async def create_product(
    data: ProductCreateModel,
    product_command_usecase: ProductCommandUsecase = Depends(product_command_usecase),
):
    try:
        product = product_command_usecase.create_product(data)
    except SkuAlreadyExistError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return product
from fastapi import APIRouter, Depends, HTTPException, status

from app.domain.product_consult import (
    ProductConsultError
)

from app.interface_adapters.session.session_manager import (
    product_consult_query_usecase,
)

from app.usecase.product_consult import (
    ProductConsultQueryUsecase,
)

router = APIRouter()

@router.get(
    "/{product_id}",
    response_model=int,
    status_code=status.HTTP_200_OK,
)
async def get_count_of_consults_by_product_id(
    product_id: str,
    product_consult_query_usecase: ProductConsultQueryUsecase = Depends(product_consult_query_usecase),
):
    try:
        product_consult = product_consult_query_usecase.get_count(
            product_id)
    except ProductConsultError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return product_consult
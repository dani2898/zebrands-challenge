from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.domain.product import (
    SkuAlreadyExistError,
    ProductNotFoundError
)
from app.presentation.schema.product.product_errors import (
    ErrorMessageSkuAlreadyExists,
    ErrorMessageProductNotFound
)

from app.interface_adapters.session.session_manager import (
    product_query_usecase,
    product_command_usecase,
)

from app.usecase.product import (
    ProductCommandUsecase,
    ProductQueryUsecase,
    ProductCreateModel,
    ProductUpdateModel,
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

@router.put(
    "/{product_id}",
    response_model=ProductReadModel,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageProductNotFound,
        },
    },
)
async def update_product(
    product_id: str,
    data: ProductUpdateModel,
    product_command_usecase: ProductCommandUsecase = Depends(product_command_usecase),
):
    try:
        updated_product = product_command_usecase.update_product(
            product_id, data
        )
    except ProductNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except SkuAlreadyExistError as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return updated_product

@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageProductNotFound,
        },
    }
)
async def delete_product(
    product_id: str,
    product_command_usecase: ProductCommandUsecase = Depends(product_command_usecase),
):
    try:
        product_command_usecase.delete_product_by_id(product_id)

    except ProductNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
@router.get(
    "/",
    response_model=List[ProductReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageProductNotFound,
        },
    }
)
async def list_products(
    product_query_usecase: ProductQueryUsecase = Depends(product_query_usecase),
):
    try:
        products = product_query_usecase.get_products()
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if len(products) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ProductNotFoundError.message,
        )

    return products
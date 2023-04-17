from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from starlette.responses import JSONResponse
from typing import List

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
    product_consult_command_usecase,
    user_query_usecase    
)

from app.usecase.product import (
    ProductCommandUsecase,
    ProductQueryUsecase,
    ProductCreateModel,
    ProductUpdateModel,
    ProductReadModel
)

from app.usecase.product_consult import (
    ProductConsultCommandUsecase
)

from app.usecase.user import (
    UserQueryUsecase,
    UserReadModel
)

router = APIRouter()

# Send email

async def send_mail(message, user_query_usecase):

    conf = ConnectionConfig(
        MAIL_USERNAME="fasttest2023api@outlook.com",
        MAIL_FROM="fasttest2023api@outlook.com",
        MAIL_PASSWORD="mailing2023",
        MAIL_PORT=587,
        MAIL_SERVER="smtp.office365.com",
        MAIL_TLS=True,
        MAIL_SSL=False
        )
        
    users = user_query_usecase.get_users()
    emails = []

    for user in users:
        emails.append(user.email)

    message = MessageSchema(
        subject="Product",
        recipients=emails,  # List of recipients, as many as you can pass
        body=message,
        subtype="html"
        )
 
    fm = FastMail(conf)
    await fm.send_message(message)
    print(message)
 
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

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
    user_query_usecase: UserQueryUsecase = Depends(user_query_usecase),
):
    try:
        product = product_command_usecase.create_product(data)

        await send_mail("New product added to the catalog", user_query_usecase)
    except SkuAlreadyExistError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Check that the info you registered is correct"
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
    user_query_usecase: UserQueryUsecase = Depends(user_query_usecase),
):
    try:
        updated_product = product_command_usecase.update_product(
            product_id, data
        )

        await send_mail(f"{updated_product.name} has been updated", user_query_usecase)
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
    user_query_usecase: UserQueryUsecase = Depends(user_query_usecase),
):
    try:
        product_command_usecase.delete_product_by_id(product_id)
        
        await send_mail(f"Product with ID {product_id} has been deleted", user_query_usecase)

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

@router.get(
    "/{product_id}",
    response_model=ProductReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageProductNotFound,
        },
    }
)
async def get_product_by_id(
    product_id: str,
    product_query_usecase: ProductQueryUsecase = Depends(product_query_usecase),
    product_consult_command_usecase: ProductConsultCommandUsecase = Depends(product_consult_command_usecase),
):
    try:
        product = product_query_usecase.get_product_by_id(product_id, product_consult_command_usecase)
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

    return product
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.interface_adapters.security import (
    JWTBearer
)

from app.domain.user import (
    EmailAlreadyExistError,
    UserNotFoundError
)

from app.interface_adapters.session.session_manager import (
    user_query_usecase,
    user_command_usecase,
)
from app.presentation.schema.user.user_errors import (
    ErrorMessageEmailAlreadyExists,
    ErrorMessageUserNotFound
)

from app.usecase.user import (
    UserCommandUsecase,
    UserCreateModel,
    UserUpdateModel,
    UserQueryUsecase,
    UserReadModel,
)


router = APIRouter()

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

@router.post(
    "/register",
    response_model=UserReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "model": ErrorMessageEmailAlreadyExists,
        },
    },
    dependencies=[Depends(JWTBearer())]
)
async def create_user(
    data: UserCreateModel,
    user_command_usecase: UserCommandUsecase = Depends(user_command_usecase),
):
    try:
        user = user_command_usecase.create_user(data)
    except EmailAlreadyExistError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return user

@router.put(
    "/{user_id}",
    response_model=UserReadModel,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageUserNotFound,
        },
    },
)
async def update_user(
    user_id: str,
    data: UserUpdateModel,
    user_command_usecase: UserCommandUsecase = Depends(user_command_usecase),
):
    try:
        updated_user = user_command_usecase.update_user(
            user_id, data
        )
    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except EmailAlreadyExistError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return updated_user

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageUserNotFound,
        },
    }
)
async def delete_user(
    user_id: str,
    user_command_usecase: UserCommandUsecase = Depends(user_command_usecase),
):
    try:
        user_command_usecase.delete_user_by_id(user_id)

    except UserNotFoundError as e:
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
    response_model=List[UserReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageUserNotFound,
        },
    }
)
async def list_users(
    user_query_usecase: UserQueryUsecase = Depends(user_query_usecase),
):
    try:
        users = user_query_usecase.get_users()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if len(users) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=UserNotFoundError.message,
        )

    return users
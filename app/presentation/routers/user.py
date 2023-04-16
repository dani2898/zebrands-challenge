from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT

from app.domain.user import (
    EmailAlreadyExistError,
)

from app.interface_adapters.session.session_manager import (
    user_query_usecase,
    user_command_usecase,
)
from app.presentation.schema.user.user_errors import (
    ErrorMessageEmailAlreadyExists
)
from app.usecase.user import (
    UserCommandUsecase,
    UserCreateModel,
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
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return user
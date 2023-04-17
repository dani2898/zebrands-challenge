from fastapi import APIRouter, Depends, HTTPException, status
import app.auth as auth
from app.interface_adapters.session.session_manager import (
    user_command_usecase,
    user_query_usecase
)

from app.presentation.schema.user.user_errors import (
    ErrorMessageUserUnauthorizedError
)

from app.usecase.user import (
    UserLoginModel,
    TokenReadModel,
    UserCommandUsecase,
    UserQueryUsecase
)

router = APIRouter()

@router.post(
    "/login",
    response_model=TokenReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_401_UNAUTHORIZED:{
            "model": ErrorMessageUserUnauthorizedError
        }
    },
    )
async def login(
    data: UserLoginModel,
    user_query_usecase: UserQueryUsecase = Depends(user_query_usecase),
    user_command_usecase: UserCommandUsecase = Depends(user_command_usecase),
):
    
    user = user_query_usecase.get_user_by_email(data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong email, user not found.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    #Verify password

    password_match = user_command_usecase.verify_password(data.password, user.password)
    
    if not password_match:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password doesn't match, verify the information.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    try:
        
        access_token = auth.create_access_token(data.email)
        
    except Exception as e:
        print(e)

    return {
            "access_token": access_token,
            "token_type": "Bearer"
        }


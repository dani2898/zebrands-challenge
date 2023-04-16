from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.infrastructure.postgres.database import SessionLocal

from app.domain.user import UserRepository

from app.infrastructure.postgres.user import (
    UserCommandUsecaseUnitOfWorkImpl,
    UserQueryServiceImpl,
    UserRepositoryImpl
    )

from app.usecase.user import (
    UserCommandUsecase,
    UserCommandUsecaseImpl,
    UserCommandUsecaseUnitOfWork,
    UserQueryService,
    UserQueryUsecase,
    UserQueryUsecaseImpl,
)


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def user_query_usecase(session: Session = Depends(get_session)) -> UserQueryUsecase:
    user_query_service: UserQueryService = UserQueryServiceImpl(session)
    return UserQueryUsecaseImpl(user_query_service)

def user_command_usecase(session: Session = Depends(get_session)) -> UserCommandUsecase:
    user_repository: UserRepository = UserRepositoryImpl(session)
    uow: UserCommandUsecaseUnitOfWork = UserCommandUsecaseUnitOfWorkImpl(
        session,
        user_repository=user_repository,
    )
    return UserCommandUsecaseImpl(uow)
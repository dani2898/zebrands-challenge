from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.infrastructure.postgres.database import SessionLocal

# User
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

# Product

from app.domain.product import ProductRepository

from app.infrastructure.postgres.product import (
    ProductCommandUsecaseUnitOfWorkImpl,
    ProductQueryServiceImpl,
    ProductRepositoryImpl
    )

from app.usecase.product import (
    ProductCommandUsecase,
    ProductCommandUsecaseImpl,
    ProductCommandUsecaseUnitOfWork,
    ProductQueryService,
    ProductQueryUsecase,
    ProductQueryUsecaseImpl,
)

# Product consult

from app.domain.product_consult import ProductConsultRepository

from app.infrastructure.postgres.product_consult import (
    ProductConsultCommandUsecaseUnitOfWorkImpl,
    ProductConsultQueryServiceImpl,
    ProductConsultRepositoryImpl
    )

from app.usecase.product_consult import (
    ProductConsultCommandUsecase,
    ProductConsultCommandUsecaseImpl,
    ProductConsultCommandUsecaseUnitOfWork,
    ProductConsultQueryService,
    ProductConsultQueryUsecase,
    ProductConsultQueryUsecaseImpl,
)

def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# USER DEFINITION SESSION MANAGER

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

# PRODUCT DEFINITION SESSION MANAGER

def product_query_usecase(session: Session = Depends(get_session)) -> ProductQueryUsecase:
    product_query_service: ProductQueryService = ProductQueryServiceImpl(session)
    return ProductQueryUsecaseImpl(product_query_service)

def product_command_usecase(session: Session = Depends(get_session)) -> ProductCommandUsecase:
    product_repository: ProductRepository = ProductRepositoryImpl(session)
    uow: ProductCommandUsecaseUnitOfWork = ProductCommandUsecaseUnitOfWorkImpl(
        session,
        product_repository=product_repository,
    )
    return ProductCommandUsecaseImpl(uow)

# PRODUCT CONSULT DEFINITION SESSION MANAGER

def product_consult_query_usecase(session: Session = Depends(get_session)) -> ProductConsultQueryUsecase:
    product_consult_query_service: ProductConsultQueryService = ProductConsultQueryServiceImpl(session)
    return ProductConsultQueryUsecaseImpl(product_consult_query_service)

def product_consult_command_usecase(session: Session = Depends(get_session)) -> ProductConsultCommandUsecase:
    product_consult_repository: ProductConsultRepository = ProductConsultRepositoryImpl(session)
    uow: ProductConsultCommandUsecaseUnitOfWork = ProductConsultCommandUsecaseUnitOfWorkImpl(
        session,
        product_consult_repository=product_consult_repository,
    )
    return ProductConsultCommandUsecaseImpl(uow)
from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.domain.user import User, UserRepository
from app.usecase.user import UserCommandUsecaseUnitOfWork

from .user_dto import UserDTO

class UserRepositoryImpl(UserRepository):
    """UserRepositoryImpl implements CRUD operations related User entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_email(self, email: str) -> Optional[User]:
        try:
            user_dto = self.session.query(UserDTO).filter_by(email=email).one()
        except NoResultFound:
            return None
    
        return user_dto.to_entity()
    
    def find_by_id(self, id: str) -> Optional[User]:
        try:
            user_dto = self.session.query(UserDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return user_dto.to_entity()
    
    def create(self, user: User):
        user_dto = UserDTO.from_entity(user)
        try:
            self.session.add(user_dto)
        except:
            raise

    def update(self, user_id: str, user: User):
        user_dto = UserDTO.from_entity(user)
        try:
            _user = self.session.query(UserDTO).filter_by(
                id=user_id
            ).one()
            _user.email = user_dto.email
            _user.firstname = user_dto.firstname
            _user.lastname = user_dto.lastname
            _user.updated_at = user_dto.updated_at

        except Exception:
            raise

    def delete_user_by_id(self, id: str):
        try:
            self.session.query(UserDTO).filter_by(id=id).delete()
        except:
            raise

class UserCommandUsecaseUnitOfWorkImpl(UserCommandUsecaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        user_repository: UserRepository,
    ):
        self.session: Session = session
        self.user_repository: UserRepository = user_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def flush(self):
        self.session.flush()

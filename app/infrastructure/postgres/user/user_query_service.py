from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.usecase.user import UserQueryService, UserReadModel

from .user_dto import UserDTO


class UserQueryServiceImpl(UserQueryService):
    """UserQueryServiceImpl implements READ operations related User entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_email(self, email: str) -> Optional[UserReadModel]:
        try:
            user_dto = self.session.query(UserDTO).filter_by(email=email).one()

        except NoResultFound:
            return None
        except:
            raise
        return user_dto.to_read_model()

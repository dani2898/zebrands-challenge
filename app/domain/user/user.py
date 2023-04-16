from typing import Optional
from datetime import datetime

class User:
    """Represents entity of user."""

    def __init__(
        self,
        id: str,
        email: str,
        password: str,
        firstname:str,
        lastname: Optional[str],
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id: str = id
        self.email: str = email
        self.password: str = password
        self.firstname: str = firstname
        self.lastname: Optional[str] = lastname
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, User):
            return self.id == o.id

        return False

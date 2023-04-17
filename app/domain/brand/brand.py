from datetime import datetime

class Brand:
    """Represents entity of brand."""

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id: str = id
        self.name: str = name
        self.description: str = description
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Brand):
            return self.id == o.id

        return False

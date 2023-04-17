from datetime import datetime

class ProductConsult:
    """Represents entity of product_consult."""

    def __init__(
        self,
        id: str,
        product_id: str,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id: str = id
        self.product_id: str = product_id
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, ProductConsult):
            return self.id == o.id

        return False

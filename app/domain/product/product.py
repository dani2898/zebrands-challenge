from typing import Optional
from datetime import datetime

class Product:
    """Represents entity of product."""

    def __init__(
        self,
        id: str,
        sku: str,
        name: str,
        description:str,
        stock: int,
        price: float,
        status: bool,
        brand_id: str,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id: str = id
        self.sku: str = sku
        self.name: str = name
        self.description: str = description
        self.stock: int = stock
        self.price: int = price
        self.status: int = status
        self.brand_id: int = brand_id
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Product):
            return self.id == o.id

        return False

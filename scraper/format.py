from dataclasses import dataclass


@dataclass
class Info:
    """Scraped info about product"""

    name: str
    brand: str
    price: float
    quantity: int
    valid: bool = True

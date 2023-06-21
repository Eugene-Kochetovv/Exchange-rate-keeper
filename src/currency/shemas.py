from dataclasses import dataclass


@dataclass
class NewTicker:
    currency_name: str
    price: float
    data: float

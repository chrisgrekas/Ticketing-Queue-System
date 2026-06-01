from __future__ import annotations
from typing import Optional


class Person:
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount
        self.next: Optional[Person] = None
        self.prev: Optional[Person] = None
        self.tickets: list = []

    def __repr__(self) -> str:
        return f"{self.name} wants {self.amount} ticket(s)"

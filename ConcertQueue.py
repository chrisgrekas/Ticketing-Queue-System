from __future__ import annotations
from typing import Optional
from ticket import Ticket
from person import Person


class ConcertQueue:
    def __init__(self, name: str, capacity: int, location: str, cost: float):
        self.name = name
        self.capacity = capacity
        self.location = location
        self.cost = cost
        self.size = 0
        self.head: Optional[Person] = None
        self.tail: Optional[Person] = None

    def __repr__(self) -> str:
        return (
            f"Event: {self.name} | Venue: {self.location} | "
            f"Capacity: {self.capacity} | Price: {self.cost}"
        )

    def is_empty(self) -> bool:
        return self.size == 0

    def has_space(self) -> bool:
        return self.capacity is None or self.capacity > self.size

    def enqueue(self, name: str, amount: int) -> None:
        if not self.has_space():
            print("Queue is full.")
            return
        person = Person(name, amount)
        if self.is_empty():
            self.head = person
            self.tail = person
        else:
            self.tail.next = person
            person.prev = self.tail
            self.tail = person
        self.size += 1
        print(f"{person.name} added to the queue.")

    def dequeue(self) -> Optional[Person]:
        if self.is_empty():
            print("Queue is empty.")
            return None
        person = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = person.next
            self.head.prev = None
        self.size -= 1
        if self.capacity >= person.amount:
            self.capacity -= person.amount
            for _ in range(person.amount):
                person.tickets.append(Ticket())
            print(f"{person.name} purchased {person.amount} ticket(s).")
        else:
            print(f"Not enough tickets available for {person.name}.")
        return person

    def dequeue_by_value(self, name: str) -> Optional[Person]:
        current = self.head
        while current is not None:
            if current.name == name:
                break
            current = current.next
        if current is None:
            return None
        if current is self.head:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        elif current is self.tail:
            self.tail = current.prev
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
        else:
            current.next.prev = current.prev
            current.prev.next = current.next
        self.size -= 1
        return current

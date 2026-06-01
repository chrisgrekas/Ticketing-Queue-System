# Ticketing Queue System

A Python implementation of a doubly linked list queue for managing concert ticket sales. People join the queue, get served in order, and receive generated tickets on checkout.

---

## Requirements

- Python 3.10+

No external dependencies.

---

## Running

```bash
python main.py
```

---

## Project Structure

```
Ticketing-Queue-System/
├── main.py          # Entry point and demo
├── ConcertQueue.py  # Queue logic (doubly linked list)
├── person.py        # Node representing a person in the queue
└── ticket.py        # Ticket with a unique UUID
```

---

## API

### `Ticket`

Generates a unique ticket ID on instantiation (`TCT-<uuid>`).

### `Person(name, amount)`

A queue node holding the person's name, requested ticket count, and issued tickets.

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | Person's name |
| `amount` | `int` | Tickets requested |
| `tickets` | `list` | Tickets issued after checkout |
| `next` | `Person \| None` | Next node in queue |
| `prev` | `Person \| None` | Previous node in queue |

### `ConcertQueue(name, capacity, location, cost)`

| Method | Description |
|--------|-------------|
| `enqueue(name, amount)` | Add a person to the back of the queue |
| `dequeue()` | Serve the person at the front; issues tickets if capacity allows |
| `dequeue_by_value(name)` | Remove a specific person by name from anywhere in the queue |
| `is_empty()` | Returns `True` if the queue has no members |
| `has_space()` | Returns `True` if the queue is below capacity |

---

## Future Plans

- CLI interactive menu
- Ticket price calculation per person
- SQLite persistence

---

## License

MIT

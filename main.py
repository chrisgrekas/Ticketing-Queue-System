from ConcertQueue import ConcertQueue

concert = ConcertQueue("Lex", 5, "OAKA", 15)
print("--- Pre-sale started! ---")
print(concert)
print("-" * 30)

while not concert.is_empty():
    person = concert.dequeue()
    if person and person.tickets:
        print(f"Tickets for {person.name}:")
        for ticket in person.tickets:
            print(f"  {ticket}")

print("\n--- Box office closed! ---")
concert.enqueue("Christos", 3)
concert.enqueue("Maria", 4)
concert.enqueue("Nikos", 1)

removed = concert.dequeue_by_value("Maria")
if removed:
    print(f"Removed: {removed.name}")
else:
    print("Not found.")

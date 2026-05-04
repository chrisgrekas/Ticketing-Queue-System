from ConcertQueue import ConcertQueue

concert = ConcertQueue("Lex", 5, "OAKA", 15)
print("--- Ξεκινάει η προπώληση! ---")
print(concert)
print("-" * 30)

# concert.enqueue("Christos", 3)
# concert.enqueue("Maria", 4)
# concert.enqueue("Nikos", 1)
# print("-" * 30)

while not concert.is_empty():
    current_person = concert.dequeue()
    
    if current_person.tickets:
        print(f"🎫 Τα εισιτήρια του/της {current_person.get_value()}:")
        for ticket in current_person.tickets:
            print(f"   {ticket}")

print("\n--- Το ταμείο έκλεισε! ---")
concert.enqueue("Christos", 3)
concert.enqueue("Maria", 4)
concert.enqueue("Nikos", 1)

removed = concert.dequeue_by_value("Maria")
if removed:
    print(f"Αφαιρέθηκε: {removed.get_value()}")
else:
    print(" Δεν βρέθηκε!")
from ticket import Ticket
from person import Person

class ConcertQueue:
    def __init__(self,name,capacity,location,cost):
        self.head=None
        self.tail=None
        self.name=name
        self.capacity=capacity
        self.location=location
        self.cost=cost
        self.max_size=100
        self.size=0
    
    def __repr__(self):
        return f" Event Name: {self.name}, with max capacity :{self.capacity}. It will take place into : {self.location} and the price of the ticket will be {self.cost} "
    
    def get_size(self):
        return self.size
    def has_space(self):
        if self.max_size==None:
            return True
        else:
            return self.max_size>self.get_size()
    def is_empty(self):
        return self.size==0
    def enqueue(self,name,amount):
        if self.has_space():
            person_to_add=Person(name,amount)
            print(f"{person_to_add.get_value()} added to the Queue!")
            if self.is_empty():
                self.head=person_to_add
                self.tail=person_to_add
            else:
                self.tail.set_next_person(person_to_add)
                person_to_add.set_prev_person(self.tail)
                self.tail=person_to_add
            self.size+=1
        else:
            print("Sorry, the queue is full!")

    def dequeue(self):
        if self.get_size()>0:
            person_to_remove=self.head
            print(f"{person_to_remove.get_value()}has been served!")
            if self.get_size()==1:
                self.head=None
                self.tail=None
            else:
                self.head=person_to_remove.get_next_person()
                self.head.set_prev_person(None)

            self.size-=1
            return person_to_remove
        
        else:
            print("The Queue is empty!")

# --- ΔΟΚΙΜΗ ΣΥΣΤΗΜΑΤΟΣ (ΤΑΜΕΙΟ) ---

# 1. Δημιουργούμε την εκδήλωση με μικρό capacity (π.χ. 5 εισιτήρια) για να δούμε τι θα γίνει 
concert = ConcertQueue("Lex", 5, "OAKA", 15)
print("--- Ξεκινάει η προπώληση! ---")
print(concert)
print("-" * 30)

# 2. Μπαίνουν πελάτες στην ουρά
concert.enqueue("Christos", 3)
concert.enqueue("Maria", 4)  # Η Μαρία ζητάει 4, αλλά θα έχουν μείνει μόνο 2!
concert.enqueue("Nikos", 1)
print("-" * 30)

# 3. Ξεκινάει η εξυπηρέτηση (όσο η ουρά ΔΕΝ είναι άδεια)
while not concert.is_empty():
    current_person = concert.dequeue()
    
    # Εδώ τραβάμε τα δεδομένα από το αντικείμενο Person που μας επέστρεψε η dequeue
    name = current_person.get_value()
    tickets_wanted = current_person.amount
    
    print(f"\n> Στο ταμείο: Ο/Η {name} ζητάει {tickets_wanted} εισιτήρια.")
    
    # Έλεγχος διαθεσιμότητας
    if concert.capacity >= tickets_wanted:
        # Υπάρχουν αρκετά εισιτήρια! Τα αφαιρούμε από το Event.
        concert.capacity -= tickets_wanted
        
        # Εδώ κανονικά θα φτιάχναμε και τα αντικείμενα Ticket!
        print(f"✅ Επιτυχία! Δόθηκαν {tickets_wanted} εισιτήρια. Απομένουν: {concert.capacity}")
    else:
        # Δεν φτάνουν τα εισιτήρια!
        print(f"❌ Αποτυχία... Έχουμε μόνο {concert.capacity} διαθέσιμα. Η κράτηση ακυρώθηκε.")

print("\n--- Το ταμείο έκλεισε! ---")






        

# concert=ConcertQueue("Lex",60000,"OAKA",15)
# print(concert)
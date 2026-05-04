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
        # self.max_size=capacity
        self.size=0
    
    def __repr__(self):
        return f" Event Name: {self.name}, with max capacity :{self.capacity}. It will take place into : {self.location} and the price of the ticket will be {self.cost} "
    
    def get_size(self):
        return self.size
    def has_space(self):
        if self.capacity==None:
            return True
        else:
            return self.capacity>self.get_size()
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
            print(f"{person_to_remove.get_value()} has been served!")
            if self.get_size()==1:
                self.head=None
                self.tail=None
            else:
                self.head=person_to_remove.get_next_person()
                self.head.set_prev_person(None)

            self.size-=1
            # ελέγχος διαθεσιμότητας
            if self.capacity>=person_to_remove.amount:
                self.capacity-=person_to_remove.amount
                for _ in range(person_to_remove.amount):
                    person_to_remove.add_ticket(Ticket())
                print(f"{person_to_remove.get_value()} αγόρασε {person_to_remove.amount} εισητήρια.")
            else:
                print(f"Δεν υπάρχουν αρκέτα διαθέσημα εισητήρια για τόν /την {person_to_remove.get_value()}")
            return person_to_remove
        
        else:
            print("The Queue is empty!")
    def dequeue_by_value(self,value):
        current=self.head
        person_to_remove=None
        while current !=None:
            if current.get_value()==value:
                person_to_remove=current
                break
            current=current.get_next_person()
        if person_to_remove==None:
            return None
        if person_to_remove == self.head:
            self.head = person_to_remove.get_next_person()
            if self.head is not None:        
                self.head.set_prev_person(None)
            else:
                self.tail = None            
        elif person_to_remove == self.tail:
            self.tail = person_to_remove.get_prev_person()
            if self.tail is not None:
                self.tail.set_next_person(None)
            else:
                self.head=None

            
        else:
            next_person=person_to_remove.get_next_person()
            prev_person=person_to_remove.get_prev_person()
            next_person.set_prev_person(prev_person)
            prev_person.set_next_person(next_person)
        self.size-=1
        return person_to_remove
                
        

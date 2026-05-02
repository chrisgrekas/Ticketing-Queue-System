class Person:
    def __init__(self,name,amount,next_person=None,prev_person=None,):
        self.name=name
        self.next_person=next_person
        self.prev_person=prev_person
        self.amount=amount
        self.tickets=[]

    def __repr__(self):
        return f"{self.name} wants {self.amount} tickets!"
    
    def set_next_person(self,next_person):
        self.next_person=next_person
    def get_next_person(self):
        return self.next_person
    def set_prev_person(self,prev_person):
        self.prev_person=prev_person
    def get_prev_person(self):
        return self.prev_person
    def get_value(self):
        return self.name
    def add_ticket(self,ticket):
        return self.tickets.append(ticket)
    
# chris=Person("Christos",3)
# print(chris)

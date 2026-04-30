import uuid
class Ticket:
    def __init__(self):
        self.id="TCT- "+str(uuid.uuid4())
    
    def __str__(self):
        return f"{self.id} has been sold"

# my_ticket=Ticket()
# print(my_ticket)
    
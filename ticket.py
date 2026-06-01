import uuid


class Ticket:
    def __init__(self):
        self.id = "TCT-" + str(uuid.uuid4())

    def __str__(self) -> str:
        return f"{self.id} sold"

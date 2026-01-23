"""
Problem 247: Gym PaymentGateway
Error Type: LOGICAL
Difficulty: Advanced
"""


class GymTransaction:
    def __init__(self, amount):
        self.amount = amount
        self.status = 'PENDING'


class PaymentGateway:
    def process(self, tx):
        if tx.amount < 0:
            print("Invalid")
            return


        if tx.amount > 1000:
            tx.amount = tx.amount * 0.9


        tx.status == 'COMPLETED'
        

t = GymTransaction(1500)
gw = PaymentGateway()
gw.process(t)
print(t.status)

"""
Problem 253: Store PaymentGateway
Error Type: LOGICAL
Difficulty: Advanced
"""


class StoreTransaction:
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
        

t = StoreTransaction(1500)
gw = PaymentGateway()
gw.process(t)
print(t.status)

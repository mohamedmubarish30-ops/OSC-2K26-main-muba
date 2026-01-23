"""
Problem 265: Weather PaymentGateway
Error Type: LOGICAL
Difficulty: Advanced
"""


class WeatherTransaction:
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
        

t = WeatherTransaction(1500)
gw = PaymentGateway()
gw.process(t)
print(t.status)

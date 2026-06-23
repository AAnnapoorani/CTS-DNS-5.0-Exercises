class PaymentGateway:
    def make_payment(self, amount):
        print("Payment of Rs.", amount, "processed")

class PaymentAdapter:
    def __init__(self, gateway):
        self.gateway = gateway
    def process_payment(self, amount):
        self.gateway.make_payment(amount)

gateway = PaymentGateway()
adapter = PaymentAdapter(gateway)
adapter.process_payment(5000)
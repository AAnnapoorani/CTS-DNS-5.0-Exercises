class CreditCardPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "using Credit Card")

class PayPalPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "using PayPal")

class PaymentContext:
    def __init__(self, payment_method):
        self.payment_method = payment_method
    def make_payment(self, amount):
        self.payment_method.pay(amount)

payment = PaymentContext(CreditCardPayment())
payment.make_payment(1000)
payment = PaymentContext(PayPalPayment())
payment.make_payment(2000)
from abc import ABC, abstractmethod

# You’re building a payment system that supports PayPal, but now you want to add support for Stripe.

# Violates OCP: You must modify this function every time you add a new method
class PaymentProcessor:
    def process(self, method, amount):
        if method == "paypal":
            print(f"Processing ${amount} with PayPal")
        elif method == "stripe":
            print(f"Processing ${amount} with Stripe")

class PaymentGateway(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class PayPalGateway(PaymentGateway):
    def process(self, amount):
        print(f"Processing ${amount} with PayPal")

class StripeGateway(PayPalGateway):
    def process(self, amount):
        print(f"Processing ${amount} with Stripe")

class NewPaymentProcessor:
    @staticmethod
    def process_payment(payment_gateway: PaymentGateway, amount):
        payment_gateway.process(amount)

if __name__ == "__main__":
    paypal_gateway = PayPalGateway()
    stripe_gateway = StripeGateway()

    NewPaymentProcessor.process_payment(paypal_gateway, 100)
    NewPaymentProcessor.process_payment(stripe_gateway, 150)
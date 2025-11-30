from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class PayPalPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


cc = CreditCardPayment()
pp = PayPalPayment()
cc.pay(1000)
pp.pay(500)

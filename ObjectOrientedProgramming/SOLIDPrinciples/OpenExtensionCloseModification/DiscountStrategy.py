from abc import ABC, abstractmethod

# You have a base class that calculates discounts. Currently, it only supports regular
# Refactor using strategy pattern so new customer types (like "employee", "student") can be added by extending, not modifying the base class.

# Initial version
class DiscountCalculator:
    def calculate(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.9
        elif customer_type == "vip":
            return amount * 0.8
        return None

class Discount(ABC):
    @abstractmethod
    def calculate(self):
        pass

    def show_discount(self):
        print("Discount: %f" % self.calculate())

class RegularDiscount(Discount):
    def __init__(self):
        self.amount = 0.9

    def calculate(self):
        return self.amount

class VIPDiscount(Discount):
    def __init__(self):
        self.amount = 0.8

    def calculate(self):
        return self.amount

class NewDiscountCalculator:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def calculate(self):
        self.discount_strategy.calculate()

    def show_discount(self):
        self.discount_strategy.show_discount()


if __name__ == "__main__":
    new_discount_calculator = NewDiscountCalculator(RegularDiscount())
    new_discount_calculator.calculate()
    new_discount_calculator.show_discount()

    new_discount_calculator.discount_strategy = VIPDiscount()
    new_discount_calculator.calculate()
    new_discount_calculator.show_discount()